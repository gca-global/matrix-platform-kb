# MLS CDL Schema — Listing Management Data Model

> **Status (Apr 2026, ADR-012 / ADR-013 / ADR-014):** The Matrix CDL now
> lives on a **dedicated Supabase project** `ofzcokolkeejgqfjaszq`
> (Matrix CDL), separate from the SSO project `xgubaguglsnokjyudgvc`.
> The CDL is owned and managed exclusively by
> `matrix-platform-foundation/supabase-cdl/`. It is not linked to Lovable.
>
> Schema: 18 domain `mls_*` tables + the ingestion control plane
> (`mls_sources`, `mls_source_field_mappings`, `mls_import_runs`,
> `mls_staging_listings`, `mls_import_events`). RLS is **enabled** on
> every table from day one and policies use JWT-only helpers so the
> schema stays portable to Databricks Lakebase. Canonical column
> names follow RESO DD 2.0; Cyprus-specific fields use the `x_sm_*`
> prefix.

## Architecture Decision (updated)

The MLS CDL is a **dedicated project** — see ADR-012. It is consumed
by Broker, Marketing, Finance, Client Portal, and Portfolio apps
through a split Supabase client:

- `ssoClient` → `xgubaguglsnokjyudgvc` (identity, roles, display lookups)
- `cdlClient` → `ofzcokolkeejgqfjaszq` (listings, contacts, transactions)

**Why a dedicated project:**
- Isolates shared business data from the identity layer. An MLS
  schema incident cannot take down SSO.
- Forces JWT-only RLS helpers → Lakebase-portable.
- Single-writer via `matrix-platform-foundation` prevents Lovable
  apps from drifting the shared schema.

**CDL Connection Pattern (current):**
- **Identity:** CDL uses Supabase Third-Party Auth with the SSO JWKS
  URL + issuer. CDL PostgREST verifies SSO-issued ES256 tokens natively.
- **Reads:** apps call `cdlClient.from('mls_...')` with the SSO token
  as bearer. RLS policies call `public.get_active_scope()` /
  `public.get_crud()` / `public.get_current_tenant_id()` which read
  claims directly from `auth.jwt()`.
- **Writes:** apps call the `cdl-write` Edge Function (on the CDL
  project) which acts as a CORS proxy for authorized writes. No app
  ever holds a CDL service-role key.
- **User display:** apps never join CDL rows to `sso_users` in SQL —
  they call the `resolve-users` SSO Edge Function via the
  `useUserDisplay` React hook.

## RLS Strategy

> **Current state (Apr 2026, per ADR-012):** RLS is **enabled on every
> CDL table from day one.** The `cdl-write` Edge Function remains a
> CORS / write-authorization proxy, but it is no longer the sole gate
> — PostgREST-level RLS now enforces reads and writes using
> JWT-derived claims. Helpers live in the CDL project's `public`
> schema and never depend on Supabase-specific GUCs, so the policies
> remain valid under Databricks Lakebase.

Uses the KB's **5-level scope + CRUD model** (Patterns A-E) with CDL helper functions:

| CDL Function | Used For |
|-------------|----------|
| `get_my_tenant_id()` | Tenant isolation (4-step fallback: `uoi` → `user_metadata.tenant_id` → `auth.users` → `admin_settings`) |
| `get_active_scope()` | Scope from JWT (`self` / `team` / `global` / `org_admin` / `system_admin`) |
| `get_crud()` | CRUD permission string from JWT (e.g., `"crud"`, `"cr"`, `"r"`) |
| `get_current_user_id()` | SSO User UUID from JWT `sub` claim |
| `is_in_my_teams(user_id)` | Team-scope resolution via `sso_user_group_memberships` |
| `get_active_scope()` | Scope from JWT — used in explicit checks like `IN ('org_admin', 'system_admin')` |

**Patterns applied:**

| Pattern | Tables | Description |
|---------|--------|-------------|
| **B (Owner-scoped)** | `mls_listings`, `mls_contacts` | 5-level CASE: self=own, team=own+teammates, global+=all tenant. DELETE: org_admin+ only |
| **A (Reference)** | `mls_checklist_templates`, `mls_document_type_config`, `mls_portal_definitions`, `mls_developments`, `mls_development_buildings` | Tenant-wide read; `org_admin`/`system_admin` write and delete |
| **Cascade** | `mls_listing_checklist_items`, `mls_listing_contact_roles`, `mls_listing_documents`, `mls_listing_media`, `mls_listing_remarks`, `mls_listing_syndications` | Inherits scope from parent `mls_listings` via `listing_id IN (SELECT id FROM mls_listings)` |
| **Cascade + Assignee** | `mls_listing_notes`, `mls_listing_tasks`, `mls_listing_approvals` | Cascade from listings OR author/assignee can see own records |
| **Append-only Cascade** | `mls_status_history`, `mls_price_history` | INSERT via cascade; no UPDATE; admin-only DELETE |

### Pattern B Example (mls_listings)

```sql
CREATE POLICY "mls_listings_select" ON mls_listings
  FOR SELECT TO authenticated
  USING (
    (SELECT get_crud()) LIKE '%r%'
    AND CASE (SELECT get_active_scope())
      WHEN 'system_admin' THEN true
      WHEN 'org_admin'    THEN tenant_id = (SELECT get_my_tenant_id())
      WHEN 'global'       THEN tenant_id = (SELECT get_my_tenant_id())
      WHEN 'team'         THEN tenant_id = (SELECT get_my_tenant_id())
                               AND (broker_id = (SELECT get_current_user_id())
                                    OR is_in_my_teams(broker_id))
      WHEN 'self'         THEN tenant_id = (SELECT get_my_tenant_id())
                               AND broker_id = (SELECT get_current_user_id())
      ELSE false
    END
  );
```

## Tables

### Core (EPIC 1 — Listing Intake)

| Table | Cols | RLS | Description |
|-------|------|-----|-------------|
| `mls_listings` | 175 | Pattern B (owner: `broker_id`) | Main listing table with full Dash field parity — RESO Property Resource alignment |
| `mls_contacts` | 30 | Pattern B (owner: `created_by`) | Shared contact registry (SIR Person form). Reusable across listings. `full_name` is a **GENERATED ALWAYS** column (`COALESCE(first_name,'') \|\| ' ' \|\| COALESCE(last_name,'')`) — do NOT include it in INSERT/UPDATE payloads |
| `mls_listing_contact_roles` | 9 | Cascade | Junction: contacts → listings with role. UNIQUE(listing_id, contact_id, role) |
| `mls_checklist_templates` | 13 | Reference | Step templates by role (BROKER/MARKETING/FINANCE). Seeded: 44 steps |
| `mls_listing_checklist_items` | 12 | Cascade | Per-listing checklist completion tracking |

### Documents & Compliance (EPIC 2)

| Table | Cols | RLS | Description |
|-------|------|-----|-------------|
| `mls_document_type_config` | 13 | Reference | Document types with conditional rules (title deed / without / land). Seeded: 9 types |
| `mls_listing_documents` | 19 | Cascade | Documents with approval workflow. Storage: `mls-documents` bucket |

### Media & Marketing (EPIC 3)

| Table | Cols | RLS | Description |
|-------|------|-----|-------------|
| `mls_listing_media` | 30 | Cascade | Photos, videos, floor plans. RESO Media Resource alignment. Storage: `mls-media` bucket |
| `mls_developments` | 14 | Reference | New development projects (admin-managed) |
| `mls_development_buildings` | 10 | Reference | Buildings within developments |
| `mls_listing_remarks` | 12 | Cascade | Multi-language descriptions. UNIQUE(listing_id, language, remark_type) |

### Workflow & Publishing (EPIC 4)

| Table | Cols | RLS | Description |
|-------|------|-----|-------------|
| `mls_status_history` | 11 | Append-only | Immutable status change log |
| `mls_price_history` | 13 | Append-only | Immutable price change log with approval support |
| `mls_listing_approvals` | 13 | Cascade | Approval records (DUE_DILIGENCE, MARKETING, MANAGEMENT, PRICE_CHANGE) |
| `mls_listing_tasks` | 14 | Cascade | Workflow tasks — assignable with priority and due date |
| `mls_portal_definitions` | 12 | Reference | Portal/channel definitions. Seeded: 6 portals |
| `mls_listing_syndications` | 13 | Cascade | Per-portal publishing tracking |
| `mls_listing_notes` | 9 | Cascade + Assignee (`author_id`) | Internal notes by type (GENERAL, DUE_DILIGENCE, MARKETING, FINANCE, VIEWING_FEEDBACK) |

## Status Pipeline

```
DRAFT → PENDING_DUE_DILIGENCE → AGREEMENT_PENDING → PHOTOS_PENDING → MARKETING_REVIEW → PUBLISHED → UNDER_OFFER → SOLD
                                                                                          ↘ WITHDRAWN
```

| Status | Dash Code | Syndicated |
|--------|-----------|-----------|
| DRAFT | — | No |
| PENDING_DUE_DILIGENCE | — | No |
| AGREEMENT_PENDING | — | No |
| PHOTOS_PENDING | — | No |
| MARKETING_REVIEW | — | No |
| PUBLISHED | AC (Active) | Yes |
| UNDER_OFFER | PS (Pending) | Yes |
| SOLD | CL (Closed) | Yes |
| WITHDRAWN | WD (Withdrawn) | Yes |

## RESO DD Alignment

`mls_listings` maps 100+ columns to RESO Property Resource fields:

| Category | Example DB Columns | RESO Properties |
|----------|-------------------|----------------|
| Identification | `ref`, `status`, `property_type` | ListingKey, StandardStatus, PropertyType |
| Pricing | `list_price`, `original_list_price`, `currency_code` | ListPrice, OriginalListPrice, CurrencyCode |
| Location | `city`, `country`, `latitude`, `longitude` | City, Country, Latitude, Longitude |
| Structure | `bedrooms`, `bathrooms`, `living_area`, `year_built` | BedroomsTotal, BathroomsTotalInteger, LivingArea, YearBuilt |
| Features | `pool_type`, `parking_covered`, `view`, `flooring` | PoolPrivateYN, ParkingTotal, View, Flooring |
| Commercial | `net_operating_income`, `capitalization_rate` | NetOperatingIncome, CapRate |
| Rental | `monthly_rent`, `lease_term`, `lease_type` | ListPrice, LeaseTerm, LeaseAmountFrequency |

`mls_listing_media` maps to RESO Media Resource. `mls_contacts` maps to RESO Contacts Resource.

## Platform Extensions Used

19 property `x_sm_*` fields (all registered in `platform-extensions.md`):

| Extension | Type | Purpose |
|-----------|------|---------|
| `x_sm_vat_applicable` | Boolean | Cyprus VAT on property |
| `x_sm_vat_expiration_date` | Date | VAT exemption expiration |
| `x_sm_introducer_fee` | Numeric | Fee paid to introducer |
| `x_sm_crypto_payment` | Boolean | Cryptocurrency accepted |
| `x_sm_excluded_from_marketing` | Boolean | Seller excludes from marketing |
| `x_sm_title_deeds` | Boolean | Title deeds availability |
| `x_sm_suitable_for_pr` | Boolean | Qualifies for Permanent Residency |
| `x_sm_uncovered_verandas` | Numeric | Uncovered veranda area |
| `x_sm_roof_garden` | Numeric | Roof garden area |
| `x_sm_elevator` | Boolean | Building has elevator |
| `x_sm_maids_room` | Boolean | Maid's/service room |
| `x_sm_separate_laundry` | Boolean | Separate laundry room |
| `x_sm_smart_home` | Boolean | Smart home features |
| `x_sm_year_renovated` | Integer | Year of last renovation |
| `x_sm_heating_medium` | Text | Specific heating medium |
| `x_sm_extras` | Text | Free-text additional features |
| `x_sm_building_density` | Numeric | Building density % (zoning) |
| `x_sm_coverage` | Numeric | Coverage % (zoning) |
| `x_sm_floors_allowed` | Integer | Max floors allowed |
| `x_sm_height_allowed` | Numeric | Max building height (m) |

## Storage Buckets

| Bucket | Max File Size | Content | RLS |
|--------|--------------|---------|-----|
| `mls-documents` | 50 MB | PDFs, scanned documents | Auth read/write; admin-only delete |
| `mls-media` | 100 MB | Photos, videos, floor plans | Auth read/write; admin-only delete |

## Indexes

Every table has `idx_mls_{table}_tenant` on `tenant_id`. Every child table has `idx_mls_{table}_listing` on `listing_id`. Key additional indexes:

| Table | Index | Columns | Notes |
|-------|-------|---------|-------|
| `mls_listings` | `idx_mls_listings_broker` | `broker_id` | |
| `mls_listings` | `idx_mls_listings_co_broker` | `co_broker_id` | Partial: `WHERE co_broker_id IS NOT NULL` |
| `mls_listings` | `idx_mls_listings_status` | `tenant_id, status` | |
| `mls_listings` | `idx_mls_listings_city` | `tenant_id, city` | |
| `mls_listings` | `idx_mls_listings_market` | `tenant_id, market` | |
| `mls_listings` | `idx_mls_listings_property_type` | `tenant_id, property_type` | |
| `mls_listings` | `mls_listings_ref_key` | `ref` | UNIQUE |
| `mls_contacts` | `idx_mls_contacts_created_by` | `created_by` | For RLS owner-scope |
| `mls_contacts` | `idx_mls_contacts_email` | `tenant_id, email` | |
| `mls_contacts` | `idx_mls_contacts_name` | `tenant_id, last_name, first_name` | |
| `mls_checklist_templates` | `idx_mls_checklist_tmpl_role` | `tenant_id, role` | |
| `mls_listing_contact_roles` | `idx_mls_contact_roles_contact` | `contact_id` | |
| `mls_listing_documents` | `idx_mls_listing_docs_status` | `listing_id, status` | |
| `mls_listing_media` | `idx_mls_listing_media_order` | `listing_id, display_order` | |
| `mls_listing_notes` | `idx_mls_notes_author` | `author_id` | |
| `mls_listing_syndications` | `idx_mls_syndications_portal` | `portal_id` | |
| `mls_listing_tasks` | `idx_mls_tasks_assigned` | `assigned_to` | Partial: `WHERE assigned_to IS NOT NULL` |
| `mls_listing_tasks` | `idx_mls_tasks_status` | `tenant_id, status` | |
| `mls_listing_approvals` | `idx_mls_approvals_status` | `tenant_id, status` | |
| `mls_development_buildings` | `idx_mls_dev_buildings_dev` | `development_id` | |

## Seed Data

Seeded per active tenant on deployment:

| Table | Records | Source |
|-------|---------|--------|
| `mls_document_type_config` | 9 types | SIR document requirements |
| `mls_portal_definitions` | 6 portals | SIR Global, Cyprus Website, MLS Feed, Facebook, Instagram, LinkedIn |
| `mls_checklist_templates` | 44 steps | `listing-checklist.md` (29 Broker, 10 Marketing, 5 Finance) |

## Compliance Notes

**Supabase best practice (known issues to fix):**
- 4 foreign keys missing covering indexes: `template_id`, `document_type_id`, `building_id`, `development_id`

**Generated columns (cannot be set in INSERT/UPDATE):**
- `mls_contacts.full_name` — `GENERATED ALWAYS AS (COALESCE(first_name, '') || ' ' || COALESCE(last_name, ''))` — auto-computed, omit from write payloads

**Design decisions (documented, intentional):**
- `tenant_id` has no DEFAULT (Postgres disallows subquery defaults; app must supply)
- Append-only tables (`mls_status_history`, `mls_price_history`) correctly omit UPDATE policies and `updated_at` triggers
- Uses `get_my_tenant_id()` (with 4-step fallback) instead of `get_current_tenant_id()` for backward compatibility with legacy JWT models
- RLS disabled for dev (Feb 2026) — 70 policies preserved, will be re-enabled post-stabilization

## Key Files

| File | Purpose |
|------|---------|
| `src/lib/cdlWrite.ts` | CDL write helper — invokes `cdl-write` Edge Function with native token |
| `src/integrations/supabase/dataLayerClient.ts` | CDL read client — prioritizes Supabase native token for PostgREST |
| `supabase/functions/cdl-write/index.ts` | Edge Function proxy — forwards CRUD operations to CDL PostgREST |
| `src/integrations/supabase/dataLayerTypes.ts` | Auto-generated CDL TypeScript types |
| `src/components/settings/DevToolsPanel.tsx` | Test data seeder — seeds 18 tables with SEED-prefixed records |

## Ingestion control plane (ADR-014)

On top of the 18 domain tables, the CDL hosts a unified ingestion
control plane that every data feed funnels through. Complete design
and rationale live in ADR-014; summary below.

| Table | Role |
|---|---|
| `mls_sources` | Registry of data feeds (reso_web_api, databricks_gold, csv_upload, crm_webhook, manual_entry). Per-tenant, unique on `(tenant_id, slug)`. |
| `mls_source_field_mappings` | Per-source mapping from `source_field` → `canonical_field` (RESO DD 2.0 column name on `mls_listings`). Supports lightweight `transform` (trim/upper/lower/cast/enum_map). |
| `mls_import_runs` | One row per sync execution. Tracks `status`, counters, `cursor`, and `error_summary`. |
| `mls_staging_listings` | Landing zone. Holds `raw_payload` + `mapped_payload` + provenance; `validation_status` enum: `staged`, `validated`, `promoted`, `rejected`, `superseded`. |
| `mls_import_events` | Append-only audit log of every ingestion decision. |

Every promoted row in `public.mls_listings` carries the provenance
columns `x_sm_source_id`, `x_sm_source_record_id`, `x_sm_ingested_at`,
`x_sm_ingested_by_run_id`, `x_sm_last_source_sync_at`. A unique
partial index on `(x_sm_source_id, x_sm_source_record_id)` keeps
dedup deterministic across retries.

**Flow:** ingest EF → `mls_staging_listings` → `listing-merge` EF →
`public.mls_listings`.

**Edge functions** (all on CDL project, `verify_jwt: false`):

- `reso-import` — OData 4.01 incremental pagination with OAuth2
  `client_credentials`. Seeded to pull from the `mls_2_0` RESO API.
- `csv-import` — direct CSV payload ingestion from the admin UI.
- `crm-import` — webhook ingestion with optional HMAC verification.
- `listing-merge` — staging → canonical promotion with three
  resolution strategies: `prefer_incoming`, `prefer_existing`,
  `reject`.

**Admin UI:** `matrix-mls/src/pages/admin/mls/*` (Sources, Field
Mappings, Import Runs, Staging Review, Manual Entry, CSV Import,
CRM Import, Merge, Audit), gated by the `data_ops` SSO role.

## Source

- CDL project: `ofzcokolkeejgqfjaszq` (Matrix CDL)
- Owning repo: `/home/bitnami/matrix-platform-foundation/supabase-cdl/`
- Migrations: `supabase-cdl/migrations/20260420000000_infra_schema.sql`
  through `20260420001100_seed_mls_sources_reso_api.sql`
- Edge functions: `supabase-cdl/functions/{cdl-write, reso-import, csv-import, crm-import, listing-merge}/`
- Consumer app (admin UI): `/home/bitnami/matrix-mls`
- Retired writer app: `/home/bitnami/matrix-cdl-studio` (see `RETIREMENT.md`)
