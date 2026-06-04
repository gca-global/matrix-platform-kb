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

1. **6-stage ingestion pipeline** (Phase 1 Best-in-Class, Apr 2026) — `reso-import` → `field-mapping-apply` → `listing-merge` → `media-import` (page-capped, writes to `cdl_staging.media_staging`) → `media-merge` (single SQL RPC into `public.property_media`) → `listing-publish`. Side resources (members/offices/contacts/openHouses/showings/history/tracking) run as a synchronous final stage on `mls-sync.run-side-resources`.
2. **MLS Sync admin control plane** — `mls-sync-orchestrator` is the only sync engine; `mls-sync` (lifted monolith ported from cy-web-2v0) handles admin/CRUD/read actions and proxies `start` to the orchestrator. Both share the same control-plane tables and expose the same action surface.
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

### `cdl_staging.media_staging` (added 2026-04-26)

PK `(staging_batch_id, source_listing_key, url)`; columns `(source_id, kind, ord, created_at)`. Populated by the page-capped `media-import` EF (RESO fetch mode) — each invocation appends up to `pagesPerInvocation` pages of OData results keyed by a single `stagingBatchId` so the orchestrator's outer loop can resume across iterations without re-doing work. Drained at the end of the run by the `public.merge_media_from_staging(p_batch_id, p_source_id)` RPC, which:

1. Upserts the staged rows into `public.property_media` (conflict on `(property_id, url)` after resolving `source_listing_key` → `properties.id`).
2. Soft-prunes target rows for the listings present in this batch whose URLs are no longer in the feed.
3. Counts orphan staging rows (no matching `properties.id`) for observability without failing the run.
4. Deletes the processed staging rows.

This pattern keeps the EF I/O-bound (no inserts on a heavily-indexed table inside the EF) and confines all merge work to a single fast SQL call.

### `public.field_mappings`

Per-source mapping rows used by `field-mapping-apply`. Reference table managed by data-ops.

### `public.ingest_audit`

Append-only log: `(fn, source_id, job_id, caller_sub, payload_summary, result, created_at)`. One row per stage call.

### MLS Sync control plane (added 2026-04-26)

| Table | Per-row scope | Purpose |
|-------|---------------|---------|
| `public.mls_settings` | unique on `tenant_id` | RESO creds, schedule (`schedule_mode`), `source_id`, `sync_resources` jsonb, `is_active`, `last_synced_at` / `last_full_synced_at`. (The legacy `sync_mode` column was dropped in `20260426170000_cdl_drop_sync_mode.sql` — see Phase 1 Best-in-Class plan below.) |
| `public.mls_sync_jobs` | `(tenant_id, id)` | Job ledger. `engine` ∈ `monolith` \| `orchestrator` (informational on legacy rows; new jobs always run on the orchestrator), status, stage, progress, stats, log_messages, caller_sub |
| `public.mls_sync_state` | `(tenant_id, resource)` | CDC cursor: `last_sync_at`, `last_modification_ts`, `etag` |
| `public.mls_orchestrator_runs` | `(tenant_id, job_id, stage)` | Per-stage state for the orchestrator EF (FK `job_id` → `mls_sync_jobs(id)` ON DELETE CASCADE) |

`mls-sync-orchestrator` is the only engine for new sync work; `mls-sync.start` proxies to it (see Best-in-Class Phase 1 below). The `engine` column on existing job rows is preserved for historical readability.

### RPCs

| Function | Purpose |
|---|---|
| `public.bulk_update_property_media(p_source_id text, p_updates jsonb)` | Replaces image rows in `property_media` for a given source. Used by legacy `mls-sync.sync-media` admin path. |
| `public.bulk_update_property_images(updates jsonb)` | Single-tenant alias for backwards compatibility with cy-web-2v0 callers. |
| `public.merge_media_from_staging(p_batch_id uuid, p_source_id text)` | Drains `cdl_staging.media_staging` for a batch into `public.property_media` (upsert + soft-prune); returns `(merged, deleted, orphaned)`. Called as the `media-merge` stage by `mls-sync-orchestrator`. |
| `public.schedule_mls_resume(job_id uuid)` | Stub for the orchestrator's "self-chain on timeout" path. Bumps `updated_at`. Will be wired to `pg_net` once that extension is enabled. |

## Edge functions (CDL project, all `verify_jwt: false`)

All EFs verify `Authorization: Bearer <SSO JWT>` themselves (HS256 first via `SSO_JWT_SECRET` / `JWT_SECRET`, JWKS ES256/RS256 fallback via `SSO_JWKS_URL`) and check `scope` against an allow-list. Three allow-lists exist:

- **Admin EFs** (`mls-sync`, `mls-sync-orchestrator`, the 5 pipeline stages, `listing-publish`, …) use `SSO_ALLOWED_SCOPES` (default `system_admin,org_admin`) — set project-wide to `system_admin,org_admin`.
- **Broker-scope read EFs** (`cdl-contacts-read`, `cdl-contact-listings-read`, `cdl-engagement-read`, `cdl-read`) use their **own** `SSO_READ_SCOPES` (default `self,team,global,org_admin,system_admin`) so a Broker (`self`) session can read. This is deliberately decoupled from the shared `SSO_ALLOWED_SCOPES` (which stays admin-only so the admin EFs are not widened). Mirrors how `listings-search` uses `SSO_LISTINGS_SCOPES`. Leave `SSO_READ_SCOPES` unset to keep the broad default.
- **Broker-scope write EF** (`cdl-write`) uses its **own** `SSO_WRITE_SCOPES` (default `self,team,global,org_admin,system_admin`) so a Broker session can author CRM rows (contacts, showings, prospecting, …). Like the read EFs, it is decoupled from the shared `SSO_ALLOWED_SCOPES`; pointing it there would 403 every non-admin broker write. Leave `SSO_WRITE_SCOPES` unset to keep the broad default. (Authz scoping/owner-clamp is still enforced inside the EF as that mapping lands — see deferred note below.)

> **Owner-clamp deferred (accepted residual risk):** the PII read EFs (`cdl-contacts-read`, `cdl-contact-listings-read`, `cdl-engagement-read`) currently return **org-wide** rows for any allowed scope — no per-`owner_member_key` clamp. The `scopeToOwner` path exists but is inert because there is **no SSO-user → `member_key` mapping**: `members` are keyed on legacy Cyprus/Qobrix emails while SSO logins are Azure AD staff, and the JWT carries no `member_key`. Enforcing real owner-clamp requires first building that identity mapping (member_key claim or mapping table). Tracked as a follow-up.

### Pipeline (6 stages — Phase 1 Best-in-Class, Apr 2026)

| EF | Reads | Writes | Contract |
|----|-------|--------|----------|
| `reso-import` | RESO API or caller-supplied records | `cdl_staging.listings_raw` | `{ sourceId, jobId, records?, fetchOptions{...,pagesPerInvocation} }` → `{ success, stagedCount, stagingBatchId, hasMore, nextSkip }` |
| `field-mapping-apply` | `listings_raw`, `field_mappings` | `cdl_staging.listings_mapped` | `{ stagingBatchId, sourceId, jobId }` → `{ success, mappedCount, skippedCount, errors }` |
| `listing-merge` | `listings_mapped` | `public.properties` (upsert + soft-delete) | `{ stagingBatchId, sourceId, jobId, incremental }` → `{ success, inserted, updated, softDeleted, unchanged }` |
| `media-import` | RESO Media or caller-supplied list | `cdl_staging.media_staging` (fetch mode) or `public.property_media` (legacy items mode) | `{ sourceId, jobId, stagingBatchId?, fetchOptions{...,pagesPerInvocation=5} }` → `{ success, stagingBatchId, hasMore, nextSkip, staged, pages }` |
| `media-merge` (RPC, no EF) | `cdl_staging.media_staging` | `public.property_media` (upsert + soft-prune) + drains staging | `merge_media_from_staging(p_batch_id uuid, p_source_id text)` → `{ merged, deleted, orphaned }` |
| `listing-publish` | `public.properties` (visible, not deleted) | `public.properties_published` | `{ jobId, sourceId, dryRun }` → `{ success, published, removed, snapshotAt }` |

Every EF stage writes one row to `public.ingest_audit`. The `media-import` EF is now invoked in a loop by `mls-sync-orchestrator` — each invocation fetches up to `pagesPerInvocation` pages of RESO Media (default 5) and threads `stagingBatchId` across iterations, so a single EF instance never approaches the 400s wall-clock even for the ~250K-row catalogue. The merge into the indexed target table happens once via `media-merge`.

### Admin control plane (`mls-sync-orchestrator` + `mls-sync`)

| EF | Role (post-Phase 1) | Path |
|----|---------------------|------|
| `mls-sync-orchestrator` | **Sole sync engine.** Chains the 6 pipeline stages (reso-import → field-mapping-apply → listing-merge → media-import (looped) → media-merge RPC → listing-publish) plus `run-side-resources`. | Staged: `cdl_staging.*` → `public.properties` / `public.property_media` |
| `mls-sync` | Admin/CRUD/read API — settings, jobs, resource CRUD, media admin, watchdog. `start` action is a thin proxy that forwards to `mls-sync-orchestrator`. | Direct admin to control-plane tables; `sync-media` legacy direct-to-media path retained for ops |

Both share the action surface (so the matrix-atlas-mls hooks are engine-agnostic):

```
get-settings | save-settings | list-jobs | get-job | get-running-job |
list-running-jobs | get-recent-job | has-previous-sync | start |
cancel | resume | test | run-side-resources
```

`mls-sync` additionally supports `sync-media`, `watchdog` (cron entry point that resumes stale jobs and triggers per-tenant scheduled syncs), `lock-field` / `unlock-field`, and the per-resource CRUD/list/test actions used by the Atlas data-management UI.

`cancel` is cooperative: it sets `cancel_requested = true` on the job row; the orchestrator's per-stage check (`isCancelRequested`) raises a `CancelledError` at the next safe point and finalises the job as `cancelled` (it never overwrites that with `completed`). The `start` action defaults `incremental = true` when the caller omits it (matches the Atlas "Incremental sync" button and is the safe default for cron Phase 2).

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

- All admin EFs (`mls-sync`, `mls-sync-orchestrator`, the 5 pipeline EF stages plus the `media-merge` RPC) require `scope` ∈ `SSO_ALLOWED_SCOPES` (default `system_admin,org_admin`).
- `listings-search` allows `self,team,global,org_admin,system_admin` by default (overridable via `SSO_LISTINGS_SCOPES`).
- The broker-scope read EFs (`cdl-contacts-read`, `cdl-contact-listings-read`, `cdl-engagement-read`, `cdl-read`) allow `self,team,global,org_admin,system_admin` by default via their own `SSO_READ_SCOPES` (NOT the shared `SSO_ALLOWED_SCOPES`). Do not point these at `SSO_ALLOWED_SCOPES` — that admin-only project value would 403 every Broker session. Owner-clamp is deferred (see Edge-functions note above).
- The broker-scope write EF (`cdl-write`) allows `self,team,global,org_admin,system_admin` by default via its own `SSO_WRITE_SCOPES` (NOT the shared `SSO_ALLOWED_SCOPES`). Same rule: do not point it at `SSO_ALLOWED_SCOPES` or every Broker contact create/update/delete 403s.
- The control-plane tables are tenant-scoped: every row carries `tenant_id` extracted from the JWT (`tenant_id` / `tenant.id` / `active_role.tenant_id`). The EFs run as `service_role` and enforce isolation by always filtering on the verified `tenant_id`.
- `public.properties` / `public.properties_published` / `public.property_media` are **not** tenant-scoped today — they share a single CDL-wide listing dataset keyed by `source_id`. Tenant-vs-source mapping for read access is handled at the EF layer when needed (e.g. `listings-search` can be filtered to `filters.sourceId`). Multi-tenant scoping of the canonical listings tables remains an open item if/when distinct tenants run distinct MLS feeds against the same CDL.

## Migrations applied

In order (see `matrix-platform-foundation/supabase/cdl/migrations/`):

1. `20260425160712_cdl_ingestion_schema.sql` — `cdl_staging` schema, `properties`, `property_media`, `properties_published`, `field_mappings`, `ingest_audit`, storage bucket `cdl-media`.
2. `20260425162326_cdl_staging_grants.sql` — schema grants for `service_role` / `authenticated`. Requires `cdl_staging` to be added to PostgREST exposed schemas (one-off project setting).
3. `20260426120000_cdl_mls_sync_control_plane.sql` — `mls_settings` / `mls_sync_jobs` / `mls_sync_state` / `mls_orchestrator_runs`, `bulk_update_property_media` (+ legacy alias), `schedule_mls_resume`, `cdl_set_updated_at` triggers, RLS on `properties_published`.
4. `20260426130000_cdl_full_reso_ingestion.sql` — Full RESO ingestion: 8 new resource tables (`members`, `offices`, `contacts`, `open_houses`, `showings` [RESO ShowingAppointment], `history_transactional`, `internet_tracking_events`, `teams`), `mls_sources` registry, `cdl_lock_field` / `cdl_unlock_field` stewardship RPCs, `property_field_overrides`. **Note:** `teams` was later DROPPED in `20260504080000` (PR1.5).
5. `20260426160000_cdl_media_staging.sql` — `cdl_staging.media_staging` table + `public.merge_media_from_staging(uuid, text)` RPC. Phase 1 Best-in-Class.
6. `20260426170000_cdl_drop_sync_mode.sql` — Drops `public.mls_settings.sync_mode` (legacy engine selector). Deployed AFTER the EF + UI rollout that no longer reads/writes the column.

## Atlas-side wiring (`matrix-atlas-mls`)

- `MLS Sync` admin page (`/mls-sync`) calls the CDL `mls-sync-orchestrator` EF directly via `useMLSSettings.invokeSync()`. The legacy "engine" dropdown and `cachedEngineFn` heuristic were removed in Phase 1 Best-in-Class.
- Admin-only actions (`get-settings`, `save-settings`, `list-jobs`, `cancel`, `lock-field`, resource CRUD, etc.) call the `mls-sync` EF via the separate `invokeMlsSyncAdmin()` helper.
- `Listings Search` page (`/listings-search`, under the `Application` sidebar group) calls the CDL `listings-search` EF.
- `useProperties` reads `public.properties_published` from the CDL anon client (no longer the SSO project).
- The cy-web-2v0 app-DB copy of `mls-sync` is retired; its `mls_settings` / `mls_sync_jobs` / `mls_sync_state` migrations are marked superseded by the CDL control-plane migration.
- Concurrent jobs are surfaced via `list-running-jobs` (both EFs) into a `runningJobs` collection in `useMLSSync`; `MLSSyncForm` shows a banner with per-job and "cancel all" controls.

## Source repos

- CDL workspace: [`matrix-platform-foundation/supabase/cdl/`](https://github.com/sharpsir-group/matrix-platform-foundation/tree/main/supabase/cdl)
  - `migrations/` — DB schema, RPCs, RLS
  - `functions/{reso-import,field-mapping-apply,listing-merge,media-import,listing-publish,mls-sync,mls-sync-orchestrator,listings-search,reso-dd-descriptions,cdl-write,cdl-contacts-read,cdl-contact-listings-read,cdl-engagement-read,cdl-read}/`
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
| `public.contacts` | Contacts | PII; `service_role`-only RLS (no anon/authenticated SELECT). FR-CON attribute columns added `20260603150000`: `company`, `lead_source`, `referred_by`, `reverse_prospecting_enabled_yn`, `notes` (all RESO DD 2.0 Contacts fields) + `x_sm_privacy_level` (extension). **`contact_type` is `text[]`** (RESO multi-value ContactType) since the same migration — was scalar `text`; the PII-scoped `v_property_contacts` view was dropped+recreated around the type change. |
| `public.open_houses` | OpenHouse | Append-only; no soft-delete sweep. |
| `public.showings` | ShowingAppointment | Service-role only. |
| `public.history_transactional` | HistoryTransactional | Append-only audit trail; bounded by `history_transactional_lookback_days`. |
| `public.internet_tracking_events` | InternetTracking | Append-only events; bounded by `tracking_lookback_days`. |
| ~~`public.teams`~~ | Teams | **DROPPED 2026-05-04 (PR1.5, `20260504080000`)** — 0 rows, 0.3% WgtOrg adoption; Cyprus market does not operate as MLS teams. Pipeline derives team identity from SSO groups (ADR-015 #5 Option B). |

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
| ~~`v_dash_members`~~ | `members` | — | **DROPPED** by the strict-RESO waves. `members` was hardened to canonical RESO and **no longer has an `is_deleted` column**, so the soft-delete-filtered dash view was removed. The Pipeline read path now uses `v_members_list` (see below). |
| ~~`v_dash_offices`~~ | `offices` | — | **DROPPED** by the strict-RESO waves. `offices` likewise has **no `is_deleted` column**; superseded by `v_offices_list` (see below). |
| ~~`v_dash_teams`~~ | `teams` | — | **DROPPED 2026-05-04 (PR1.5)** alongside `public.teams`. |
| `v_dash_property_media` | `property_media JOIN properties` | `NOT properties.is_deleted` | anon, authenticated |
| `v_dash_open_houses` | `open_houses` | `NOT is_deleted` | anon, authenticated |
| ~~`v_dash_contacts`~~ | `contacts` | — | **DROPPED** by `strict_reso_wave1` (`20260515130000`). `contacts` was hardened to a pure canonical-RESO table: `source_id` / `content_hash` / `is_deleted` / `deleted_at` were dropped, so it has **no soft-delete column** and is keyed on `(originating_system_name, originating_system_contact_key)`. PII reads go through `cdl-contacts-read`. The same hardening applies to `showings` (RESO ShowingAppointment). |

Phase-1 v_dash_properties is intentionally a minimal slice. Full Dash
field coverage (`propertyDetails.*`, `days_on_market`, `list_price_usd`,
denormalised `office.*`) is deferred to the Phase-2.5 `dash-export` EF.

### Member / office list views (`v_members_list`, `v_offices_list`)

Added by `20260603140000_member_office_list_views.sql` (matrix-pipeline Week 1
Cursor stretch #7). Denormalized, **projected** read views over `members` /
`offices` that keep RESO-native snake_case column names so app readers just
repoint their hooks. These are **regular** views, not `MATERIALIZED` —
members=129 / offices=59 make matview refresh-staleness pure cost
(`performance.md` frames matviews as a scale-beyond-Pro exit ramp). Both are
`security_invoker = true` (RLS evaluated as the caller; base tables already
grant `anon` SELECT).

| View | Backed by | Shape | Grants |
|---|---|---|---|
| `v_members_list` | `members LEFT JOIN offices` | member display/lookup columns **+ denormalized `office_name` / `office_city` / `office_country`** (join on `office_key`, fallback `office_id`). No `is_deleted` (column doesn't exist). | anon, authenticated |
| `v_offices_list` | `offices` | office display columns **+ denormalized `agent_count`** (correlated count of `members` per `office_key`). | anon, authenticated |

Supersedes the dropped `v_dash_members` / `v_dash_offices`. The Pipeline app
reads these via `useMembers` / `useOffices` ([`useMlsData.ts`]) with an explicit
`select=` projection (no `select *`); `MemberPicker` shows the denormalized
office name without a second offices fetch + client-side key join. Supporting
base-table indexes: `members(office_key)`, `members(modification_timestamp desc)`,
`members(member_status)`, `offices(modification_timestamp desc)`. Trigram GIN
search indexes were intentionally omitted (sub-ms seq-scan ILIKE at this size).

> **Data note:** only ~38/129 members currently resolve an `office_name` —
> many legacy (Qobrix-imported) `members.office_key` values have no matching
> `offices` row. This is upstream data sparsity, not a view defect; the join is
> correct where the office exists.

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

## Phase 2 expansion — Pipeline canonical RESO completeness (May 2026)

Lands the canonical RESO resources the `matrix-pipeline` 2.0 CRM consumes but
the CDL did not yet hold, plus the re-model of two live-only engagement tables.
Drivers: [ADR-015](../architecture/decisions/ADR-015.md) (EF surface request) and
[ADR-016](../architecture/decisions/ADR-016.md) (canonical-into-CDL acceleration).

### 9 new canonical resource tables

`20260529160000_pipeline_canonical_new_tables.sql`. Same hybrid pattern as the
Phase-1 tables (`id uuid pk` + `source_id` + `unique(source_id, source_*_key)` +
RESO snake_case typed columns + `raw jsonb` GIN-indexed + `content_hash` +
soft-delete + `locked_fields jsonb` + `updated_at` trigger). Canonical field
names verified against `reso-dd-kb/wiki/agent-docs/resources/*.md`.

| Table | RESO Resource | RLS read surface |
|---|---|---|
| `public.saved_search` | SavedSearch | `authenticated` SELECT (`is_deleted=false`) |
| `public.prospecting` | Prospecting | **service_role only** (PII — links Contacts) |
| `public.showing_availability` | ShowingAvailability | `authenticated` SELECT |
| `public.showing_request` | ShowingRequest | `authenticated` SELECT |
| `public.showing` | Showing (recorded fact; **distinct from `public.showings` = ShowingAppointment**) | `authenticated` SELECT |
| `public.lock_or_box` | LockOrBox | **service_role only** (access audit) |
| `public.caravan` | Caravan | `authenticated` SELECT |
| `public.caravan_stop` | CaravanStop | `authenticated` SELECT (polymorphic `stop_*` ref) |
| `public.transaction_management` | TransactionManagement | `authenticated` SELECT |

`transaction_management` carries **only the 4 canonical RESO fields**
(`transaction_key`, `transaction_id`, `transaction_type`, `modification_timestamp`).
Deal offer amount / commission / P&L stay **app-private in the CRM app DB** —
RESO has no deal-economics resource (ADR-016 escape hatch).

> **Naming caution:** `public.showings` (Phase-1) = RESO **ShowingAppointment**
> (a booked slot). `public.showing` (Phase-2) = RESO **Showing** (a recorded
> showing fact). They are different RESO resources; do not conflate.

### Re-model: `contact_listings` + `contact_listing_notes`

`20260529161000_pipeline_contact_listings_remodel.sql`. These two tables existed
**live-only** (no prior foundation migration), with a non-canonical shape and
**RLS DISABLED** (~24,979 rows exposed to the anon key — a CDL access-gate
violation per ADR-015 #4). This migration adopts them into the repo, adds the
canonical RESO envelope + engagement columns (additive), backfills canonical
keys, migrates inline `notes` text into child `contact_listing_notes` rows, and
**enables RLS service_role-only** (revoking anon/authenticated access).

> **Execution finding (ADR-016):** the live `contact_listings.relationship`
> column holds listing-side **provenance** (`Seller` 15,865 / `Developer` 9,114),
> NOT the canonical buyer-engagement `ContactListingPreference`
> (`Favorite`/`Possibility`/`Discard`). The provenance columns are retained;
> canonical engagement columns are added nullable for forward CRM use. No
> `relationship → contact_listing_preference` mapping is applied.

### Security fix: `v_property_contacts` (P0 remediation)

`20260530120000_secure_v_property_contacts.sql`. The CDL **security advisor**
flagged `public.v_property_contacts` as a **SECURITY DEFINER** view that joins
`contact_listings → contacts` and exposes contact PII
(`full_name`/`email`/`mobile_phone`/`preferred_phone`). It carried full anon
grants and bypassed the service-role-only RLS placed on `contact_listings` by
the re-model above, so anon callers could still read PII through it. The fix:
set `security_invoker = on` (so the view runs with the caller's rights and the
underlying RLS applies) and **revoke all from `anon`/`authenticated`**. The
canonical read path is now the `cdl-contact-listings-read` EF (`op=by-property`),
which resolves the same join service-role-side behind an SSO JWT scope check.

### CDL Third-Party Auth + authenticated reference reads (2026-06-01)

CDL is now registered for Supabase **Third-Party Auth** against the SSO JWKS
(see [ADR-018](../architecture/decisions/ADR-018.md)), so CDL PostgREST verifies
an SSO ES256 token directly (was `PGRST301`). The public-reference tables
`members`, `offices`, `open_houses`, `showings` were broadened from anon-only to
**`{anon, authenticated}` SELECT** (`qual = true`) — migration
`20260601190000_tpa_authed_reference_reads.sql` — mirroring the existing
`properties_published` (`pp_anon_read` / `pp_authed_read`) and
`history_transactional` split. This is additive (no new exposure: anon already
read these as public RESO reference data) and lets a logged-in caller read them
with either the anon key (`cdlAnonClient`) or the SSO JWT (`cdlAuthedClient`).
**PII tables (`contacts`, `contact_listings`) remain `service_role`-only behind
EFs** — TPA does **not** open them to the browser. Owner-clamp is still deferred
(see the Edge-functions note above).

### Broker-scope read EFs for non-anon CDL tables (2026-05-31)

Even with TPA live, two classes of data stay on EFs: **PII / service-role-only**
tables, and joins that touch them. `matrix-pipeline` reads those through the
broker-scope read EFs below (both
`verify_jwt = false`, custom SSO-JWT verification + scope check, service-role
inside; mirror `cdl-contacts-read`):

- **`cdl-engagement-read`** — PII-gated engagement reads. Ops: `prospecting-list`
  (by `contact_key` [+ optional `saved_search_key`]), `saved-search-list`
  (joins `prospecting → saved_search` for a contact), `saved-search-get`,
  **`prospecting-stale`** (FR-PROS-07 — active subscriptions with no
  `contact_listings` send in the last `days`, default 14; returns each row's
  `last_sent_timestamp`), and **`prospecting-due-events`** (recent
  `history_transactional` rows where `change_type ∈ {'Prospecting reminder due',
  'Prospecting send'}`, default `sinceDays = 30`; `field_key = prospecting_key`,
  `resource_record_key = contact_key`). `prospecting-due-events` is the signal the
  Pipeline app turns into broker touchpoint **Activities** (FR-PROS-09/11). Needed
  because `public.prospecting` is **service-role-only** (it carries recipient
  email lists = PII), so the `prospecting → saved_search` join cannot run on the
  anon/authenticated client.
- **`cdl-read`** — generic read for **authenticated-only** operational tables
  (NOT PII, NOT `lock_or_box`). Body `{ resource, filter, page, pageSize, order }`
  over a whitelist: `showing_request`, `showings`, `showing`,
  `showing_availability`, `transaction_management`, `caravan`, `caravan_stop`,
  `internet_tracking_events`. Per-resource filterable-column allow-lists; applies
  `is_deleted = false` where the column exists; estimated counts.

These complete the read side for the Pipeline canonical-process surfaces
(SavedSearch/Prospecting, Showing chain, Transactions, Caravans, Internet
tracking, and the derived 5-stage `/pipeline` projection). Writes still flow
through the single `cdl-write` dispatcher (ADR-016).

### Scheduled jobs (pg_cron) — Prospecting delivery engine (2026-06-04)

`public.cdl_prospecting_run()` is the Week-2 Prospecting **delivery/matching
engine** (FR-PROS-03) — it supersedes the reminder-only v0 `cdl_prospecting_tick()`
(now dropped). Scheduled by **`pg_cron` job `cdl-prospecting-run-hourly`**
(`0 * * * *`; the prior `cdl-prospecting-tick-hourly` job is unscheduled).
`SECURITY DEFINER`, transactional, no external I/O. Per eligible subscription
(`active_yn AND NOT is_deleted AND NOT concierge_yn AND client_activated_yn AND
contact_key IS NOT NULL`):

1. **Initialize** — sets `prospecting.next_send_timestamp = coalesce(created_at, now())`
   wherever it is `NULL` (first outreach due immediately).
2. **Match + send** — when due, reads the structured criteria persisted at
   **`saved_search.raw->'criteria'`** (written by the Pipeline app; the OData
   `$filter` in `search_query` stays the canonical contract — `raw.criteria` is
   its machine-evaluable mirror), evaluates it against **`public.properties`**
   (`standard_status`, `property_type`, `property_sub_type`, `list_price`,
   `bedrooms_total`, `bathrooms_total_integer`, `city`) restricted to rows
   `updated_at > coalesce(last_new_changed_timestamp, '-infinity')`, and inserts
   one **`contact_listings`** row per NEW match not already delivered to the
   contact (`listing_sent_timestamp = now()`, `contact_id` resolved from
   `contacts`, provenance in `raw.delivered_by/prospecting_key/saved_search_key`).
   It then advances `last_new_changed_timestamp` to the newest matched
   `updated_at` and emits a contact-scoped `'Prospecting send'`
   `history_transactional` row (`field_key = prospecting_key`, `new_value` = sent
   count).
3. **Remind** — when a due cycle yields **no new matches**, emits one
   `'Prospecting reminder due'` row per due-onset (deduped on
   `field_key + modification_timestamp >= next_send_timestamp`) so the broker
   still gets a touchpoint (FR-PROS-09).
4. **Advance cadence** — `next_send_timestamp` advances by `ScheduleType` in both
   branches: `Daily +1d`, `Weekly +7d`, `Monthly +1mo`, `ASAP`/`OnNewMatch` +1h
   (event-driven re-check), `Custom` +1d (v0). The durable broker reminder is the
   app-DB **Activity** materialized from the emitted events, so advancing the CDL
   timestamp here is safe (resolves the v0 no-advance caveat).

**Dual reminders:** the CDL `history_transactional` row is the immutable audit;
the Pipeline app reads `cdl-engagement-read` `prospecting-due-events` and
materializes an app-DB `Activity` per cycle as the broker's completable to-do
(FR-PROS-09/11). **Email dispatch is deferred** — no platform mailer yet;
delivery is in-app/portal via the `contact_listings` rows. Concierge-held and
not-client-activated subscriptions are skipped (canonical "Concierge gating").

**Divergence (recorded, escape hatch):** implemented as a SQL function + `pg_cron`
(mirroring `mls-sync-resume-watchdog`), **not** a Deno EF — v0 has no external
I/O (email deferred). `saved_search.raw.criteria` is a deliberate
structured-criteria mirror of the canonical OData `$filter` so the server engine
can evaluate matches without an OData parser. Test entry point:
`select * from public.cdl_prospecting_run();` returns
`(initialized, sent, reminders_emitted)`.

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
| 8 | `20260426160000_cdl_media_staging.sql` | `cdl_staging.media_staging` + `merge_media_from_staging` RPC (Phase 1 Best-in-Class) |
| 9 | `20260426170000_cdl_drop_sync_mode.sql` | Drop legacy `mls_settings.sync_mode` (orchestrator is sole engine) |
| … | (10–17: lifecycle, descriptions, occupant/owner, detail resources, keyset indexes, PR1 canonical renames) | see `migrations/` dir |
| 18 | `20260504080000_pr1_5_pr1_6_drop_teams_and_power_production.sql` | DROP `public.teams` + `property_power_production` (PR1.5/1.6) |
| 19 | `20260529160000_pipeline_canonical_new_tables.sql` | 9 new canonical CRM tables + RLS + grants (ADR-016) |
| 20 | `20260529161000_pipeline_contact_listings_remodel.sql` | Re-model `contact_listings` + `contact_listing_notes` + backfill + RLS (ADR-016) |
| 21 | `20260530120000_secure_v_property_contacts.sql` | Secure `v_property_contacts` (SECURITY INVOKER + revoke anon) — P0 PII leak fix (ADR-016) |
| … | (22–27: TPA authed reads, tenant label overrides, `app_ui_strings`, member/office list views, contacts FR-CON columns) | see `migrations/` dir |
| 28 | `20260604080000_cdl_prospecting_tick.sql` | `cdl_prospecting_tick()` + hourly `pg_cron` — Week-2 Prospecting reminder engine (initialize `next_send_timestamp` + emit contact-scoped reminder history). **Superseded by 29.** |
| 29 | `20260604120000_cdl_prospecting_run.sql` | `cdl_prospecting_run()` (FR-PROS-03 delivery engine) — matches `public.properties` against `saved_search.raw.criteria`, inserts `contact_listings`, advances `last_new_changed_timestamp` + `next_send_timestamp` per `ScheduleType`, emits `'Prospecting send'` / `'Prospecting reminder due'`. Drops `cdl_prospecting_tick()`, repoints cron to `cdl-prospecting-run-hourly`. |

## Cross-reference

| Topic | See |
|---|---|
| ADR — dedicated CDL project | [ADR-012](../architecture/decisions/ADR-012.md) |
| ADR — single owning repo | [ADR-013](../architecture/decisions/ADR-013.md) |
| ADR — ingestion pipeline + status note on the actual implementation | [ADR-014](../architecture/decisions/ADR-014.md) |
| ADR — Pipeline EF surface request | [ADR-015](../architecture/decisions/ADR-015.md) |
| ADR — canonical-into-CDL acceleration (Phase-2 tables, re-model, `cdl-write`) | [ADR-016](../architecture/decisions/ADR-016.md) |
| RESO canonical fields | [`reso-dd-kb/wiki/agent-docs/_index.md`](reso-dd-kb/wiki/agent-docs/_index.md) |
| Platform extensions (`x_sm_*`) | [platform-extensions.md](platform-extensions.md) |
| Read-path perf budgets | [read-path-performance.md](read-path-performance.md) |
| Dash projection map | [dash-data-model.md](dash-data-model.md) |
| Security model (JWT, RLS helpers) | [../platform/security-model.md](../platform/security-model.md) |
