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

## Phase 1 expansion — Full RESO ingestion + Dash projection (Apr 2026)

Three migrations land the Phase-1 foundation for full RESO 8-resource
ingestion, source-of-record / lifecycle taxonomy, stewardship, perf, and
the `v_dash_*` projection layer that is the SIR-affiliate contract surface
to Anywhere Dash.

### 8 new RESO resource tables (hybrid typed + `raw jsonb`)

Each table follows the pattern `id uuid pk` + `source_id` + RESO-DD
canonical typed columns + `raw jsonb` (RESO record verbatim) +
`content_hash` (change detection) + soft-delete + `locked_fields jsonb`
(stewardship) + per-resource indexes. The `raw` column is GIN-indexed
(`jsonb_path_ops`) for arbitrary RESO field reach without schema churn.

| Table | RESO Resource | Notes |
|---|---|---|
| `public.members` | Member | Roster identities + designations (`x_sm_sir_designation`). |
| `public.offices` | Office | Companies-via-Office hierarchy (`main_office_key`). |
| `public.contacts` | Contacts | PII; `service_role`-only RLS (no anon/authenticated SELECT). |
| `public.open_houses` | OpenHouse | Append-only; no soft-delete sweep. |
| `public.showings` | ShowingAppointment | Service-role only. |
| `public.history_transactional` | HistoryTransactional | Append-only audit trail; bounded by `history_transactional_lookback_days`. |
| `public.internet_tracking_events` | InternetTracking | Append-only events; bounded by `tracking_lookback_days`. |
| `public.teams` | Teams | Team roster grouping; FK-shape to `members.member_key` via `team_lead_key`. |

### Stewardship (`locked_fields`)

`locked_fields jsonb default '{}'::jsonb` lives on the 6 editable canonical
tables (`properties`, `members`, `offices`, `contacts`, `teams`,
`open_houses`). When an agent edits a field through an Atlas/Pipeline UI,
the field is "locked" — subsequent syncs **strip the locked column from
the UPDATE payload** so source overwrites are blocked while INSERT-time
defaults still flow.

| Artefact | Purpose |
|---|---|
| `public.property_field_overrides` | Append-only audit of every lock/unlock action. |
| `public.cdl_lock_field(table_name, row_id, field, source_value, by, reason)` | `SECURITY DEFINER` RPC. Locks a field + writes audit row. |
| `public.cdl_unlock_field(table_name, row_id, field, by)` | `SECURITY DEFINER` RPC. Releases lock + writes audit row. |

Both RPCs are granted to `authenticated` only (no anon execution).

### Source of record + lifecycle

`public.mls_sources` is now the canonical taxonomy. Columns:

- `kind text not null check (kind in ('internal','legacy-internal','brand-network','external'))`
- `is_internal boolean default false`
- `is_sunsetting boolean default false`, `sunset_at timestamptz`

Phase-1 seed rows: `matrix-internal` (internal), `qobrix`
(legacy-internal, sunsetting), `dash` (brand-network, disabled until
Phase-2.5). HU + KZ inbound is bundled under `dash` since those markets
author directly in Anywhere Dash.

`public.properties` / `public.properties_published` carry
`lifecycle_state` + `lifecycle_state_changed_at`. Transitions are
audited in `public.property_lifecycle_events` (append-only). The
`v_dash_properties` view filters `lifecycle_state = 'Active'` per the
Dash-network contract (Active inventory only); other lifecycle states
remain queryable directly on `properties_published`.

### SIR brand markers

`x_sm_*` platform-extension prefix per
[`platform-extensions.md`](platform-extensions.md):

- `properties.x_sm_is_sir_branded boolean default false`
- `properties.x_sm_sir_office_id text`
- `properties_published.x_sm_is_sir_branded`, `x_sm_sir_office_id`
- `members.x_sm_sir_designation text`

The `v_dash_*` views alias these back to bare Dash names
(`is_sir_branded`, `sir_office_id`, `designation`).

### Read-path performance indexes (`properties_published`)

Migration `20260426140000_cdl_properties_published_perf_indexes.sql`:

- 8 selective B-tree indexes (keyset pagination, status/visibility,
  lifecycle state, property type, geo, price, per-source pagination,
  SIR branding).
- 2 GIN trigram indexes (`pg_trgm`) on `title_en` + `description_en` for
  fuzzy free-text.
- Statistics targets bumped to 500/200 on high-cardinality columns
  (`price`, `city`, `listing_agent_key`, `country`, `property_type`).
- Autovacuum tuned (`autovacuum_vacuum_scale_factor=0.05`,
  `autovacuum_analyze_scale_factor=0.02`).
- `public.cdl_analyze_published()` `SECURITY DEFINER` RPC — `mls-sync`
  calls this at the end of every sync that touched the snapshot, so
  query plans stay current after large UPDATEs.

### Phase-2 intelligence-layer placeholders

Migration `20260426141000_cdl_phase2_intelligence_foundation.sql`:

- `vector` extension enabled (pgvector).
- `embedding vector(1536)` + `feature_vector jsonb` + `marketing_metadata jsonb`
  on both `public.properties` and `public.properties_published`.
- Partial indexes on `id where embedding is not null`; GIN on
  `marketing_metadata`. Empty until the Phase-2 `embed-properties` EF
  starts populating them; reads are unaffected.

### Dash projection (`v_dash_*` views)

Migration `20260426150000_cdl_dash_views.sql` — 7 views with
`with (security_invoker = true)` so RLS evaluates as the caller.
Storage tables stay RESO snake_case; views give Dash callers Dash names
without a destructive schema rename. See
[`dash-data-model.md`](dash-data-model.md) for the field-by-field map.

| View | Backed by | Filter | Grants |
|---|---|---|---|
| `v_dash_properties` | `properties_published` | `is_visible AND NOT is_deleted AND lifecycle_state='Active'` | anon, authenticated |
| `v_dash_members` | `members` | `NOT is_deleted` | anon, authenticated |
| `v_dash_offices` | `offices` | `NOT is_deleted` | anon, authenticated |
| `v_dash_teams` | `teams` | `NOT is_deleted` | anon, authenticated |
| `v_dash_property_media` | `property_media JOIN properties` | `NOT properties.is_deleted` | anon, authenticated |
| `v_dash_open_houses` | `open_houses` | `NOT is_deleted` | anon, authenticated |
| `v_dash_contacts` | `contacts` | `NOT is_deleted` | **service_role only** (PII) |

Phase-1 v_dash_properties is intentionally a minimal slice. Full Dash
field coverage (`propertyDetails.*`, `days_on_market`, `list_price_usd`,
denormalised `office.*`) is deferred to the Phase-2.5 `dash-export` EF.

### Read-side Edge Function updates (`listings-search`)

The `listings-search` EF added in this phase:

- **Keyset pagination** on `(published_at desc, id desc)` — cursors are
  base64url JSON `{published_at, id}`, returned as `nextCursor` and
  passed back as `cursor`. Prevents O(N) deep-page scans.
- **Estimated counts** by default (`countMode: 'estimated'`). Exact
  counts are opt-in via `estimateCount: false` for admin dashboards.
- **HTTP caching** — `Cache-Control: public, s-maxage=60,
  stale-while-revalidate=120` plus `ETag` (W/-prefixed quick-hash) and
  `If-None-Match` short-circuit to `304`. CDN-friendly.

See [`read-path-performance.md`](read-path-performance.md) for the full
budget + tuning playbook.

## Migrations index (current)

| # | File | Purpose |
|---|---|---|
| 1 | `20260425160712_cdl_ingestion_schema.sql` | Base ingestion schema |
| 2 | `20260425162326_cdl_staging_grants.sql` | Staging grants |
| 3 | `20260426120000_cdl_mls_sync_control_plane.sql` | MLS Sync control plane |
| 4 | `20260426130000_cdl_full_reso_ingestion.sql` | 8 RESO tables + stewardship + lifecycle + SIR markers |
| 5 | `20260426140000_cdl_properties_published_perf_indexes.sql` | Read-path indexes + autovacuum tuning + `cdl_analyze_published` RPC |
| 6 | `20260426141000_cdl_phase2_intelligence_foundation.sql` | pgvector + Phase-2 column placeholders |
| 7 | `20260426150000_cdl_dash_views.sql` | 7 `v_dash_*` projection views |

## Cross-reference

| Topic | See |
|---|---|
| ADR — dedicated CDL project | [ADR-012](../architecture/decisions/ADR-012.md) |
| ADR — single owning repo | [ADR-013](../architecture/decisions/ADR-013.md) |
| ADR — ingestion pipeline + status note on the actual implementation | [ADR-014](../architecture/decisions/ADR-014.md) |
| RESO canonical fields | [reso-canonical-schema.md](reso-canonical-schema.md) |
| Platform extensions (`x_sm_*`) | [platform-extensions.md](platform-extensions.md) |
| Read-path perf budgets | [read-path-performance.md](read-path-performance.md) |
| Dash projection map | [dash-data-model.md](dash-data-model.md) |
| Security model (JWT, RLS helpers) | [../platform/security-model.md](../platform/security-model.md) |
