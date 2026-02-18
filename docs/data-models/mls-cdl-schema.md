# MLS CDL Schema — Listing Management Data Model

> 18 tables, 422 columns, 72 RLS policies deployed to `supabase-matrix-data-layer` (CDL instance `xgubaguglsnokjyudgvc`).
> All tables use the `mls_` prefix. Column names follow Dash conventions; Cyprus-specific fields use `x_sm_*`.

## Architecture Decision

The MLS Listing Management tables are deployed to the **shared CDL instance**, not a separate app database. This makes listing data a canonical, cross-app asset — consumed by Broker, Marketing, Finance, and Client Portal apps through the same Supabase client.

**Why CDL, not a separate app DB:**
- Listings are shared data (like Property in RESO) — multiple apps need read/write access
- Avoids cross-instance joins or data duplication
- RLS policies use existing CDL helper functions
- Consistent with the "CDL = system of record" principle

## RLS Strategy

Uses **existing CDL functions** (not the KB's Pattern A-E `get_active_scope()`/`get_crud()` model):

| CDL Function | Used For |
|-------------|----------|
| `get_my_tenant_id()` | Tenant isolation on every policy |
| `auth.uid()` | Broker/creator ownership checks |
| `is_admin()` | Admin-only write on reference tables |
| `can_access_all_tenant_data()` | Org-wide read for managers |
| `is_manager_or_above()` | Manager-level access |

**Why the deviation:** The CDL instance does not have `001_sso_helper_functions.sql` deployed (no `get_active_scope()`, `get_crud()`, `get_current_tenant_id()`). Rather than deploying new SECURITY DEFINER functions to the shared CDL, we use the existing 3-level permission model.

**Patterns applied:**

| Pattern | Tables | Description |
|---------|--------|-------------|
| **Reference** | `mls_checklist_templates`, `mls_document_type_config`, `mls_portal_definitions`, `mls_developments`, `mls_development_buildings` | All tenant users read; admin-only write |
| **Broker-owned** | `mls_listings` | Broker sees own listings; managers/admins see all |
| **Creator-owned** | `mls_contacts` | Creator sees own contacts; managers/admins see all |
| **Cascade** | `mls_listing_*` child tables | Inherits access from parent `mls_listings` via `listing_id IN (SELECT id FROM mls_listings)` |
| **Append-only** | `mls_status_history`, `mls_price_history` | INSERT via cascade; no UPDATE; admin-only DELETE |
| **Author-owned** | `mls_listing_notes` | Author writes; tenant-wide read |

## Tables

### Core (EPIC 1 — Listing Intake)

| Table | Cols | RLS | Description |
|-------|------|-----|-------------|
| `mls_listings` | 175 | Broker-owned | Main listing table with full Dash field parity — RESO Property Resource alignment |
| `mls_contacts` | 30 | Creator-owned | Shared contact registry (SIR Person form). Reusable across listings |
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
| `mls_listing_notes` | 9 | Author-owned | Internal notes by type (GENERAL, DUE_DILIGENCE, MARKETING, FINANCE, VIEWING_FEEDBACK) |

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

Every table has `idx_mls_{table}_tenant` on `tenant_id`. Key additional indexes:

| Table | Index | Columns |
|-------|-------|---------|
| `mls_listings` | `idx_mls_listings_broker` | `broker_id` |
| `mls_listings` | `idx_mls_listings_status` | `tenant_id, status` |
| `mls_listings` | `idx_mls_listings_city` | `tenant_id, city` |
| `mls_listings` | `idx_mls_listings_market` | `tenant_id, market` |
| `mls_listings` | `idx_mls_listings_property_type` | `tenant_id, property_type` |
| `mls_listings` | `mls_listings_ref_key` | `ref` (UNIQUE) |
| `mls_contacts` | `idx_mls_contacts_email` | `tenant_id, email` |
| `mls_contacts` | `idx_mls_contacts_name` | `tenant_id, last_name, first_name` |
| `mls_listing_media` | `idx_mls_listing_media_order` | `listing_id, display_order` |
| `mls_listing_tasks` | `idx_mls_tasks_assigned` | `assigned_to` |

## Seed Data

Seeded per active tenant on deployment:

| Table | Records | Source |
|-------|---------|--------|
| `mls_document_type_config` | 9 types | SIR document requirements |
| `mls_portal_definitions` | 6 portals | SIR Global, Cyprus Website, MLS Feed, Facebook, Instagram, LinkedIn |
| `mls_checklist_templates` | 44 steps | `listing-checklist.md` (29 Broker, 10 Marketing, 5 Finance) |

## Compliance Notes

**Supabase best practice (known issues to fix):**
- 8 RLS policies use bare `auth.uid()` instead of `(SELECT auth.uid())` — causes per-row re-evaluation at scale
- 4 foreign keys missing covering indexes: `template_id`, `document_type_id`, `building_id`, `development_id`

**KB deviation (documented, intentional):**
- Uses CDL 3-level permission model instead of KB 5-level scope (Pattern A-E)
- `tenant_id` has no DEFAULT (Postgres disallows subquery defaults; app must supply)
- Append-only tables correctly omit `updated_at` triggers

## Source

- App repo: `/home/bitnami/matrix-mls`
- CDL instance: `xgubaguglsnokjyudgvc` (supabase-matrix-data-layer)
- Migrations: 004–011 (mls_lookup_tables through mls_seed_data)
- TypeScript types: `src/integrations/supabase/dataLayerTypes.ts`
