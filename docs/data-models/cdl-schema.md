# CDL Schema — Common Data Layer for Sharp Matrix Apps

> **Scope.** The Matrix **CDL (Common Data Layer)** is the shared,
> cross-app data platform for Sharp Matrix. It is the **single home for
> any business data that needs to be read by more than one app**: MLS
> listings + media (today), and any future shared domains such as
> agent/office directories, valuation snapshots, market analytics,
> document libraries, etc. App-private data (drafts, app-specific
> workflow state) stays on the **app DB**, not the CDL.
>
> **Status (Apr 2026, ADR-012 / ADR-013 / ADR-014).** The Matrix CDL
> lives on a **dedicated Supabase project** `ofzcokolkeejgqfjaszq`
> (Matrix Data Model Studio), separate from the SSO project
> `xgubaguglsnokjyudgvc`. The CDL is owned and managed exclusively by
> [`matrix-platform-foundation/supabase/cdl/`](https://github.com/sharpsir-group/matrix-platform-foundation/tree/main/supabase/cdl)
> and is **not** linked to Lovable.
>
> The schema actually deployed on the CDL project today is the **MLS
> listings layer** described below — `public.properties`,
> `public.properties_published`, `public.property_media`, the
> `cdl_staging.*` raw/mapped tables, and the **MLS Sync control plane**
> (`mls_settings`, `mls_sync_jobs`, `mls_sync_state`,
> `mls_orchestrator_runs`). Additional shared domains will be added as
> new schemas / tables on the same CDL project as the platform grows.
> The earlier "18 `mls_*` domain tables" model documented in ADR-014
> was an aspirational design and was **not** built; see
> [ADR-014](../architecture/decisions/ADR-014.md) for the updated
> status note. Per-broker listing-management tables (drafts, contacts,
> checklists, syndications, etc.) for the `matrix-mls` app live on the
> **app DB** (`wckwfbbqiupvallmhqbu`), not the CDL.

## Architecture at a glance

```
                            ┌──────────────────────────┐
RESO Web API (external)   ──►│  reso-import EF         │
RESO 2.0 mls_2_0 API      ──►│  (OData 4.01 + OAuth)   │
                             └──────────┬───────────────┘
                                        │ landing
                                        ▼
                             ┌──────────────────────────┐
                             │  cdl_staging.listings_raw │
                             └──────────┬───────────────┘
                                        │ field-mapping-apply
                                        ▼
                             ┌──────────────────────────┐
                             │ cdl_staging.listings_mapped │
                             └──────────┬───────────────┘
                                        │ listing-merge (upsert + soft-delete)
                                        ▼
                             ┌──────────────────────────┐
                             │  public.properties        │
                             │  public.property_media    │
                             └──────────┬───────────────┘
                                        │ listing-publish (snapshot)
                                        ▼
                             ┌──────────────────────────┐
                             │ public.properties_published │ ◄── listings-search EF
                             │ (anon-readable, RLS-gated)  │ ◄── direct anon reads
                             └──────────────────────────┘
```

Three logical layers, all hosted on `ofzcokolkeejgqfjaszq`:

1. **5-stage ingestion pipeline** — `reso-import` → `field-mapping-apply` → `listing-merge` → `media-import` → `listing-publish`.
2. **MLS Sync admin control plane** — `mls-sync` (lifted monolith ported from cy-web-2v0) and `mls-sync-orchestrator` (chains the 5 stages). Both share the same control-plane tables and expose the same action surface.
3. **Read-side EF** — `listings-search` for filtered/paginated reads of `public.properties_published` from app UIs (e.g. `matrix-atlas-mls` "Application" sidebar).

## Tables

### `public.properties` — canonical listings

The canonical, mutable listing row. Multi-source via `(source_id, source_listing_key)` natural key.

| Column | Type | Notes |
|--------|------|-------|
| `id` | uuid PK | |
| `source_id` | text | e.g. `reso-cyprus-1`; FK-shape to `mls_settings.source_id` |
| `source_listing_key` | text | external system's primary key (RESO `ListingKey`) |
| `content_hash` | text | for change detection in `listing-merge` |
| `is_visible` | boolean | gates publish |
| `is_deleted`, `deleted_at` | bool, ts | soft-delete on full sync |
| `listing_id` | text | RESO `ListingId` (human-friendly) |
| `title_en`, `slug` | text | display |
| `address`, `city`, `country`, `postal_code`, `district` | text | location |
| `latitude`, `longitude` | float8 | |
| `price`, `currency` | numeric, text | |
| `status` | text | RESO StandardStatus (`Active`, `Pending`, `Closed`, …) |
| `property_type` | text | RESO PropertyType |
| `bedrooms`, `bathrooms`, `year_built` | int | |
| `area_sqm`, `land_area_sqm` | numeric | |
| `description_en` | text | |
| `listing_agent_key` | text | RESO `ListAgentKey` |
| `virtual_tour_url` | text | |
| `created_at`, `updated_at` | timestamptz | |

Unique constraint: `(source_id, source_listing_key)`.

### `public.property_media` — image / tour / video / floorplan rows

| Column | Type | Notes |
|--------|------|-------|
| `id` | uuid PK | |
| `property_id` | uuid FK → `properties(id)` ON DELETE CASCADE | |
| `url` | text | unique with `property_id` |
| `kind` | text | check: `image`, `tour`, `video`, `floorplan` |
| `ord` | int | display order |
| `source_listing_key` | text | trace back to source row |
| `created_at` | timestamptz | |

Unique: `(property_id, url)`. The `bulk_update_property_media(p_source_id, p_updates jsonb)` RPC replaces the legacy `bulk_update_property_images(jsonb)` (the latter is kept as a single-tenant alias).

### `public.properties_published` — public snapshot

The `listing-publish` EF rewrites this snapshot from `public.properties` filtered by `is_visible AND NOT is_deleted`. Same column set as `properties` plus `published_at`. **RLS enabled**: `anon` and `authenticated` may `SELECT` rows where `is_visible AND NOT is_deleted`.

### `cdl_staging.listings_raw` / `cdl_staging.listings_mapped`

Staging schema (exposed to PostgREST via `db_extra_search_path`). Holds the raw RESO payload and the post-mapping output keyed by `staging_batch_id`. Cleared per batch by the merge stage.

### `public.field_mappings`

Per-source mapping rows used by `field-mapping-apply`. Reference table managed by data-ops.

### `public.ingest_audit`

Append-only log: `(fn, source_id, job_id, caller_sub, payload_summary, result, created_at)`. One row per stage call.

### MLS Sync control plane (added 2026-04-26)

| Table | Per-row scope | Purpose |
|-------|---------------|---------|
| `public.mls_settings` | unique on `tenant_id` | RESO creds, schedule (`schedule_mode`), engine selector (`sync_mode` ∈ `monolith` \| `orchestrator`), `source_id`, `sync_resources` jsonb, `is_active`, `last_synced_at` / `last_full_synced_at` |
| `public.mls_sync_jobs` | `(tenant_id, id)` | Job ledger. `engine` ∈ `monolith` \| `orchestrator`, status, stage, progress, stats, log_messages, caller_sub |
| `public.mls_sync_state` | `(tenant_id, resource)` | CDC cursor: `last_sync_at`, `last_modification_ts`, `etag` |
| `public.mls_orchestrator_runs` | `(tenant_id, job_id, stage)` | Per-stage state for the orchestrator EF (FK `job_id` → `mls_sync_jobs(id)` ON DELETE CASCADE) |

Both engines share these tables. The atlas-side UI picks which EF to call based on `mls_settings.sync_mode`.

### RPCs

| Function | Purpose |
|---|---|
| `public.bulk_update_property_media(p_source_id text, p_updates jsonb)` | Replaces image rows in `property_media` for a given source. Used by the lifted `mls-sync` monolith. |
| `public.bulk_update_property_images(updates jsonb)` | Single-tenant alias for backwards compatibility with cy-web-2v0 callers. |
| `public.schedule_mls_resume(job_id uuid)` | Stub for the orchestrator's "self-chain on timeout" path. Bumps `updated_at`. Will be wired to `pg_net` once that extension is enabled. |

## Edge functions (CDL project, all `verify_jwt: false`)

All EFs verify `Authorization: Bearer <SSO JWT>` themselves (HS256 first via `SSO_JWT_SECRET` / `JWT_SECRET`, JWKS ES256/RS256 fallback via `SSO_JWKS_URL`) and check `scope` ∈ `SSO_ALLOWED_SCOPES` (default `system_admin,org_admin`; `listings-search` defaults to a broader allow-list via `SSO_LISTINGS_SCOPES`).

### Pipeline (5 stages)

| EF | Reads | Writes | Contract |
|----|-------|--------|----------|
| `reso-import` | RESO API or caller-supplied records | `cdl_staging.listings_raw` | `{ sourceId, jobId, records?, fetchOptions? }` → `{ success, stagedCount, stagingBatchId }` |
| `field-mapping-apply` | `listings_raw`, `field_mappings` | `cdl_staging.listings_mapped` | `{ stagingBatchId, sourceId, jobId }` → `{ success, mappedCount, skippedCount, errors }` |
| `listing-merge` | `listings_mapped` | `public.properties` (upsert + soft-delete) | `{ stagingBatchId, sourceId, jobId, incremental }` → `{ success, inserted, updated, softDeleted, unchanged }` |
| `media-import` | RESO Media or caller-supplied list | `public.property_media` | `{ sourceId, jobId, media?, fetchOptions? }` → `{ success, imported, failed, skippedDuplicates }` |
| `listing-publish` | `public.properties` (visible, not deleted) | `public.properties_published` | `{ jobId, sourceId, dryRun }` → `{ success, published, removed, snapshotAt }` |

Every stage writes one row to `public.ingest_audit`.

### Admin control plane (`mls-sync` + `mls-sync-orchestrator`)

| EF | Engine | Path |
|----|--------|------|
| `mls-sync` | Lifted monolith (port of `cy-web-2v0/mls-sync`) | Direct to `public.properties` and `public.property_media` |
| `mls-sync-orchestrator` | Chains stages 1→5 of the pipeline above | Same tables, via the staged path |

Both share the action surface (so the matrix-atlas-mls hooks are mode-agnostic):

```
get-settings | save-settings | list-jobs | get-job | get-running-job |
get-recent-job | has-previous-sync | start | cancel | resume | test
```

`mls-sync` additionally supports `sync-media` and `watchdog` (cron entry point that resumes stale jobs and triggers per-tenant scheduled syncs).

### Read EF (`listings-search`)

POST request body:

```json
{
  "q": "free-text",
  "filters": {
    "city": "...", "country": "...", "district": "...",
    "status": "Active", "property_type": "Villa",
    "currency": "EUR",
    "minPrice": 100000, "maxPrice": 2000000,
    "minBedrooms": 2, "minBathrooms": 1,
    "minAreaSqm": 50, "maxAreaSqm": 500,
    "sourceId": "reso-cyprus-1"
  },
  "page": 0, "pageSize": 20,
  "sort": { "field": "price", "direction": "desc" },
  "includeMedia": true
}
```

Response: `{ data, total, page, pageSize }`. Sortable fields: `published_at, price, bedrooms, bathrooms, area_sqm, year_built, city, country, status, property_type`.

`public.properties_published` is also exposed for direct anon `SELECT` (RLS: `is_visible AND NOT is_deleted`) for simple pages that don't need server-side filtering.

## Auth & multi-tenancy

- All admin EFs (`mls-sync`, `mls-sync-orchestrator`, the 5 pipeline stages) require `scope` ∈ `SSO_ALLOWED_SCOPES` (default `system_admin,org_admin`).
- `listings-search` allows `self,team,global,org_admin,system_admin` by default (overridable via `SSO_LISTINGS_SCOPES`).
- The control-plane tables are tenant-scoped: every row carries `tenant_id` extracted from the JWT (`tenant_id` / `tenant.id` / `active_role.tenant_id`). The EFs run as `service_role` and enforce isolation by always filtering on the verified `tenant_id`.
- `public.properties` / `public.properties_published` / `public.property_media` are **not** tenant-scoped today — they share a single CDL-wide listing dataset keyed by `source_id`. Tenant-vs-source mapping for read access is handled at the EF layer when needed (e.g. `listings-search` can be filtered to `filters.sourceId`). Multi-tenant scoping of the canonical listings tables remains an open item if/when distinct tenants run distinct MLS feeds against the same CDL.

## Migrations applied

In order (see `matrix-platform-foundation/supabase/cdl/migrations/`):

1. `20260425160712_cdl_ingestion_schema.sql` — `cdl_staging` schema, `properties`, `property_media`, `properties_published`, `field_mappings`, `ingest_audit`, storage bucket `cdl-media`.
2. `20260425162326_cdl_staging_grants.sql` — schema grants for `service_role` / `authenticated`. Requires `cdl_staging` to be added to PostgREST exposed schemas (one-off project setting).
3. `20260426120000_cdl_mls_sync_control_plane.sql` — `mls_settings` / `mls_sync_jobs` / `mls_sync_state` / `mls_orchestrator_runs`, `bulk_update_property_media` (+ legacy alias), `schedule_mls_resume`, `cdl_set_updated_at` triggers, RLS on `properties_published`.

## Atlas-side wiring (`matrix-atlas-mls`)

- `MLS Sync` admin page (`/mls-sync`) calls the CDL `mls-sync` or `mls-sync-orchestrator` EF based on `mls_settings.sync_mode`.
- `Listings Search` page (`/listings-search`, under the `Application` sidebar group) calls the CDL `listings-search` EF.
- `useProperties` reads `public.properties_published` from the CDL anon client (no longer the SSO project).
- The cy-web-2v0 app-DB copy of `mls-sync` is retired; its `mls_settings` / `mls_sync_jobs` / `mls_sync_state` migrations are marked superseded by the CDL control-plane migration.

## Source repos

- CDL workspace: [`matrix-platform-foundation/supabase/cdl/`](https://github.com/sharpsir-group/matrix-platform-foundation/tree/main/supabase/cdl)
  - `migrations/` — DB schema, RPCs, RLS
  - `functions/{reso-import,field-mapping-apply,listing-merge,media-import,listing-publish,mls-sync,mls-sync-orchestrator,listings-search}/`
  - `config.toml` — every EF registered with `verify_jwt = false`
  - `README.md` — operational doc + smoke tests
- Atlas consumer: `matrix-atlas-mls` at `/home/bitnami/matrix-atlas-mls` (sidebar groups `Overview` / `Application` / `MLS Sync` / `Administration`)
- Original monolith source: `cy-web-2v0/supabase/functions/mls-sync` at `/home/bitnami/cy-web-2v0/supabase/functions/mls-sync` (the cy-web project keeps it as a legacy fallback; the canonical version is the CDL-hosted port)

## Cross-reference

| Topic | See |
|---|---|
| ADR — dedicated CDL project | [ADR-012](../architecture/decisions/ADR-012.md) |
| ADR — single owning repo | [ADR-013](../architecture/decisions/ADR-013.md) |
| ADR — ingestion pipeline + status note on the actual implementation | [ADR-014](../architecture/decisions/ADR-014.md) |
| RESO canonical fields | [reso-canonical-schema.md](reso-canonical-schema.md) |
| Platform extensions (`x_sm_*`) | [platform-extensions.md](platform-extensions.md) |
| Security model (JWT, RLS helpers) | [../platform/security-model.md](../platform/security-model.md) |
