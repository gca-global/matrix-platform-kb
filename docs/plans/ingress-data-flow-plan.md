# Ingress Data Flow Plan — Load, Modify, Distribute

> **Status**: Draft plan for review — no implementation changes yet
> **Date**: 2026-02-22
> **Branch**: `cursor/ingress-data-flow-plan-a541`
>
> **Core idea**: External source data arrives via Databricks into Supabase CDL,
> where the MLS app enriches and controls it, then distributes outward to all channels.

## Problem Statement

Today three external sources feed data **inbound** through Databricks into the CDL:

```
Qobrix API (Cyprus) ──┐
DASH API (Kazakhstan) ─┼──→ Databricks Bronze → Silver → Gold ──→ Supabase CDL (RESO tables)
DASH FILE (Hungary) ───┘
```

The existing docs describe a future where Matrix Apps become the **sole origin** of data
(Phase 3 — Qobrix gone). But there is an important intermediate phase: the MLS app is
being built *now*, and external sources will continue feeding data for some time.

**The opportunity**: use the MLS app as a **modification and enrichment layer** sitting on
CDL, so that data loaded from existing sources can be claimed, enriched with Sharp-specific
fields and workflow, and then pushed outward to all channels with those modifications.

## Current Architecture (As-Is)

### Data Path

```
External Sources
    │
    ▼
Databricks (Bronze → Silver → Gold)
    │
    ▼ Gold → CDL sync
Supabase CDL
    ├── reso_gold.property  →  CDL: property table (RESO names)
    ├── reso_gold.member    →  CDL: member table
    ├── reso_gold.media     →  CDL: media table
    ├── reso_gold.contacts  →  CDL: contacts table
    └── ...
    │
    ▼
Matrix Apps (read-only consumers today)
```

### Two Table Families on CDL

| Family | Tables | Naming | Source | Status |
|--------|--------|--------|--------|--------|
| **RESO tables** | `property`, `member`, `contacts`, `media` | RESO DD names | Databricks Gold sync | Data present |
| **MLS tables** | `mls_listings`, `mls_contacts`, `mls_listing_media`, ... (18 tables) | Dash conventions | MLS app (manual entry) | Schema deployed, empty |

These two families currently live side-by-side on the same CDL instance (`xgubaguglsnokjyudgvc`)
but are not connected — there is no link between a `property` row ingested from Databricks
and an `mls_listings` row created by a broker in the MLS app.

## Proposed Architecture (To-Be)

### Core Concept

```
External Sources (Qobrix, Dash API, Dash FILE)
    │
    ▼
Databricks (Bronze → Silver → Gold)
    │
    ▼ Ingress Sync
┌────────────────────────────────────────────────────────┐
│  Supabase CDL — mls_listings (single canonical table)  │
│                                                        │
│  ┌─────────────────┐     ┌─────────────────────────┐  │
│  │ Ingested records │────▶│ MLS App (Modify/Enrich) │  │
│  │ origin = 'DASH'  │     │ • Add x_sm_* fields     │  │
│  │ origin = 'QOBRIX'│     │ • Advance status        │  │
│  │ status = INGESTED│     │ • Attach documents      │  │
│  └─────────────────┘     │ • Assign broker         │  │
│                          │ • Manage media          │  │
│                          │ • Control syndication   │  │
│                          └────────┬────────────────┘  │
│                                   │                    │
│                          ┌────────▼────────────────┐  │
│                          │ Modified records         │  │
│                          │ status = PUBLISHED / etc │  │
│                          │ origin preserved         │  │
│                          └─────────────────────────┘  │
└───────────┬───────────────────────────────────────────┘
            │
            ▼ Egress (push to channels)
    ┌───────┼───────────────────────┐
    │       │                       │
    ▼       ▼                       ▼
  Dash    RESO Web API         Portal Exports
  (push)  (3rd parties)        (HomeOverseas, etc.)
```

### Key Design Decisions

#### 1. `mls_listings` Is the Single Canonical Table

Instead of maintaining two parallel table families (RESO `property` *and* `mls_listings`),
`mls_listings` becomes the single truth for all listing data — whether it arrived from
an external source or was created manually by a broker.

**Why**: `mls_listings` already has 175 columns covering Dash field parity plus all
`x_sm_*` extensions. It has the richer schema. The RESO `property` table has ~125 columns
and lacks the workflow fields (status pipeline, checklists, syndication tracking, documents).

The RESO `property` table either:
- **(Option A)** Becomes a **view** or **materialized view** over `mls_listings` that
  exposes RESO-named columns for backward compatibility with the RESO Web API
- **(Option B)** Is populated by a **CDL-side trigger/function** that mirrors published
  `mls_listings` records into RESO-named columns for the API layer

Recommended: **Option A** — a Postgres view is simpler, always consistent, zero sync lag.

#### 2. Ingress Creates `mls_listings` Records Directly

The Databricks Gold → CDL sync target changes from the RESO `property` table to
`mls_listings`. Each ingested record gets:

| Field | Value | Purpose |
|-------|-------|---------|
| `origin_system` | `'QOBRIX'`, `'DASH_API'`, `'DASH_FILE'` | Track where record came from |
| `origin_key` | Source system ID (e.g., `QOBRIX_1234`, `DASH_abc-def`) | Deduplication and back-reference |
| `origin_sync_ts` | Timestamp of last ingress sync | Conflict detection |
| `status` | `'INGESTED'` | New status before the existing pipeline |
| `is_externally_managed` | `true` / `false` | Whether source system is still authoritative |

These are **new columns** added to `mls_listings` (5 columns).

#### 3. Status Pipeline Gains an INGESTED Stage

Current pipeline:
```
DRAFT → PENDING_DUE_DILIGENCE → AGREEMENT_PENDING → PHOTOS_PENDING → MARKETING_REVIEW → PUBLISHED → UNDER_OFFER → SOLD
```

Extended pipeline:
```
INGESTED → DRAFT → PENDING_DUE_DILIGENCE → ... → PUBLISHED → UNDER_OFFER → SOLD
  │
  └──(auto-publish path for already-active listings from Dash)──→ PUBLISHED
```

- **INGESTED**: Record loaded from external source, not yet claimed/reviewed by a broker
- Records that arrive with `StandardStatus = Active` from Dash can optionally be
  auto-advanced to `PUBLISHED` (configurable per tenant/market)
- Records in `INGESTED` are visible to brokers/managers but flagged as "awaiting review"

#### 4. Conflict Resolution — Source Updates vs MLS Modifications

When a record exists in both the external source and `mls_listings`, the sync must
handle conflicts:

| Scenario | Resolution |
|----------|-----------|
| Record exists in source, not in CDL | **INSERT** into `mls_listings` with status `INGESTED` |
| Record exists in both, CDL status is `INGESTED` (unclaimed) | **UPDATE** from source — source wins for all source-mapped fields |
| Record exists in both, CDL status is `DRAFT` or later (claimed) | **Selective merge** — source updates only price/status/coordinates if changed; MLS modifications to enrichment fields preserved |
| Record exists in both, `is_externally_managed = false` | **Skip** — MLS app has full ownership, no source updates |
| Record deleted in source, exists in CDL | **Flag** `origin_deleted = true`, do not delete. MLS app decides |

The MERGE logic runs as a **Supabase Edge Function** or **database function** invoked
by the Databricks sync, not as a blind UPSERT.

#### 5. Field Mapping: Gold → mls_listings

The Gold layer outputs RESO DD names. `mls_listings` uses Dash names. A mapping layer
translates during ingress:

| Gold (RESO) | mls_listings (Dash) | Notes |
|-------------|-------------------|-------|
| `ListingKey` | `origin_key` | Stored as origin reference |
| `ListPrice` | `list_price` | Direct map |
| `StandardStatus` | `status` | Mapped: Active→PUBLISHED, Pending→UNDER_OFFER, Closed→SOLD |
| `PropertyType` | `property_type` | Reverse RESO→Dash type mapping |
| `BedroomsTotal` | `bedrooms` | Direct map |
| `City` | `city` | Direct map |
| `Latitude` | `latitude` | Direct map |
| `Longitude` | `longitude` | Direct map |
| `ListAgentKey` | `broker_id` | Requires agent→user lookup |
| `OriginatingSystemOfficeKey` | → `tenant_id` lookup | Maps office key to tenant |
| ... | ... | Full mapping covers 100+ fields |

This mapping already exists conceptually in the ETL pipeline (Silver→Gold does the
reverse). It can be codified as a Postgres function or a thin mapping table.

#### 6. Media and Contacts Follow the Same Pattern

| Resource | Source Gold Table | CDL Target Table | Link |
|----------|-----------------|-----------------|------|
| Listings | `reso_gold.property` | `mls_listings` | `origin_key` |
| Media | `reso_gold.media` | `mls_listing_media` | `listing_id` + `origin_media_key` |
| Contacts | `reso_gold.contacts` | `mls_contacts` | `origin_contact_key` |
| Members | `reso_gold.member` | (SSO users / `member` table) | `origin_member_key` |

Each child table gets an `origin_*_key` column for dedup.

#### 7. Egress: MLS App Controls What Gets Distributed

The MLS app already has syndication infrastructure:
- `mls_portal_definitions` — 6 portals defined (SIR Global, Cyprus Website, MLS Feed, Facebook, Instagram, LinkedIn)
- `mls_listing_syndications` — per-portal publishing status per listing
- Status pipeline — only `PUBLISHED`, `UNDER_OFFER`, `SOLD`, `WITHDRAWN` are syndicated

Egress paths:

| Channel | Mechanism | Trigger |
|---------|-----------|---------|
| Dash / SIR Global | Databricks push job or Edge Function calling Dash API | `mls_listing_syndications` row with `portal = 'SIR_GLOBAL'` and `status = 'ACTIVE'` |
| RESO Web API | Postgres view over `mls_listings` with RESO column aliases | Always available for published listings |
| Portal Exports (HomeOverseas) | Databricks export job reads from CDL `mls_listings` | Listing is published + portal syndication active |
| Website | Direct Supabase query from website app | Published listings in tenant scope |
| Social Media | Marketing app triggers | Manual or rule-based |

**Key change for Dash**: Dash flips from being a **source** to being a **destination**.
Listings modified in the MLS app push back to Dash with Sharp's enrichments. This is
the "Dash flip" described in the platform strategy.

## Implementation Phases

### Phase A: Schema Preparation (no data flow changes)

1. Add 5 new columns to `mls_listings`:
   - `origin_system TEXT` — `'QOBRIX'` | `'DASH_API'` | `'DASH_FILE'` | `'MANUAL'` | NULL
   - `origin_key TEXT` — source system primary key
   - `origin_sync_ts TIMESTAMPTZ` — last sync timestamp from source
   - `is_externally_managed BOOLEAN DEFAULT false` — source still authoritative
   - `origin_deleted BOOLEAN DEFAULT false` — source record was deleted
2. Add `INGESTED` to the status enum
3. Add `origin_media_key TEXT` to `mls_listing_media`
4. Add `origin_contact_key TEXT` to `mls_contacts`
5. Create unique index: `UNIQUE(tenant_id, origin_system, origin_key)` on `mls_listings`
6. Create RESO view: `CREATE VIEW property_reso AS SELECT ... FROM mls_listings` with RESO column aliases

### Phase B: Ingress Pipeline — Databricks → mls_listings

1. Write a new Gold → CDL sync notebook (or modify `04_*` export layer) that:
   - Reads from `reso_gold.property`
   - Maps RESO field names → Dash field names (reverse of the Silver→Gold transform)
   - Calls a Supabase RPC function `ingest_listing(...)` that handles MERGE logic
2. Implement `ingest_listing()` as a Postgres function on CDL:
   - INSERT if no matching `(tenant_id, origin_system, origin_key)` exists
   - UPDATE if match exists AND status is `INGESTED` (source wins)
   - Selective merge if match exists AND status > `INGESTED` (preserve enrichments)
   - Skip if `is_externally_managed = false`
3. Same pattern for media: `ingest_listing_media(...)` links to parent via `origin_key`
4. Same pattern for contacts: `ingest_contact(...)` with dedup on email + name
5. CDC variant: incremental ingress using existing `cdc_metadata` timestamps

### Phase C: MLS App — Claim and Modify Workflow

1. Add "Ingested Listings" view in MLS app UI — shows records with `status = 'INGESTED'`
2. Broker can **claim** a listing → advances to `DRAFT`, assigns `broker_id`
3. Broker enriches: adds `x_sm_*` fields, documents, remarks, contacts
4. Workflow continues through existing status pipeline
5. Manager bulk-review: auto-advance ingested listings that meet criteria
6. Dashboard shows ingress metrics: how many ingested, claimed, enriched, published

### Phase D: Egress — Push Modified Data to Channels

1. **Dash push**: New Databricks notebook or Edge Function reads published `mls_listings`
   and PUSHes to Dash API (reverse of current pull)
2. **RESO Web API**: Point API queries at the `property_reso` view instead of Gold tables
3. **Portal exports**: Modify `04a_export_homesoverseas_etl.py` to read from CDL
   `mls_listings` instead of `reso_gold.property`
4. **Realtime**: Supabase Realtime broadcasts listing changes to connected apps
   (Broker, Manager, Client Portal, Website)

### Phase E: Deprecate Direct RESO Table Population

1. Stop Gold → RESO `property` table sync (replaced by Gold → `mls_listings` sync)
2. RESO `property` table becomes a view over `mls_listings`
3. Archive Gold tables in Databricks for analytics/BI only
4. Eventually (Phase 3 of platform migration): stop Qobrix ingress entirely

## Per-Market Rollout Strategy

| Market | Current Source | Phase B Ingress | Phase D Egress | Notes |
|--------|---------------|-----------------|----------------|-------|
| **Cyprus** | Qobrix API | Qobrix → Gold → `mls_listings` | MLS → Dash (push), MLS → portals | Highest priority: replace Qobrix |
| **Hungary** | Dash FILE | Dash FILE → Gold → `mls_listings` | MLS → Dash (push back) | Dash becomes bidirectional |
| **Kazakhstan** | Dash API | Dash API → Gold → `mls_listings` | MLS → Dash (push back) | Dash becomes bidirectional |

For Hungary and Kazakhstan, the "Dash flip" means:
- **Before**: Dash → Databricks → CDL (pull)
- **Transition**: Dash → Databricks → CDL → MLS enrichment → Dash (round-trip)
- **After**: MLS app → CDL → Dash (push only, Dash ingress stopped)

## Schema Impact Summary

### New Columns on Existing Tables

| Table | New Column | Type | Purpose |
|-------|-----------|------|---------|
| `mls_listings` | `origin_system` | `TEXT` | Source identifier |
| `mls_listings` | `origin_key` | `TEXT` | Source primary key |
| `mls_listings` | `origin_sync_ts` | `TIMESTAMPTZ` | Last sync from source |
| `mls_listings` | `is_externally_managed` | `BOOLEAN` | Source still authoritative |
| `mls_listings` | `origin_deleted` | `BOOLEAN` | Source record deleted |
| `mls_listing_media` | `origin_media_key` | `TEXT` | Source media ID |
| `mls_contacts` | `origin_contact_key` | `TEXT` | Source contact ID |

### New Database Objects

| Object | Type | Purpose |
|--------|------|---------|
| `ingest_listing()` | Function | MERGE logic for listing ingress |
| `ingest_listing_media()` | Function | MERGE logic for media ingress |
| `ingest_contact()` | Function | MERGE logic for contact ingress |
| `property_reso` | View | RESO-named columns over `mls_listings` |
| `idx_mls_listings_origin` | Index | `UNIQUE(tenant_id, origin_system, origin_key)` |

### New Pipeline Notebooks

| Notebook | Layer | Purpose |
|----------|-------|---------|
| `05_sync_gold_to_cdl_listings.py` | Sync | Gold → `mls_listings` ingress |
| `05a_sync_gold_to_cdl_media.py` | Sync | Gold → `mls_listing_media` ingress |
| `05b_sync_gold_to_cdl_contacts.py` | Sync | Gold → `mls_contacts` ingress |
| `06_push_cdl_to_dash.py` | Egress | `mls_listings` → Dash API push |

### Status Enum Change

```
Current:  DRAFT | PENDING_DUE_DILIGENCE | AGREEMENT_PENDING | PHOTOS_PENDING | MARKETING_REVIEW | PUBLISHED | UNDER_OFFER | SOLD | WITHDRAWN
Proposed: INGESTED | DRAFT | PENDING_DUE_DILIGENCE | AGREEMENT_PENDING | PHOTOS_PENDING | MARKETING_REVIEW | PUBLISHED | UNDER_OFFER | SOLD | WITHDRAWN
```

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Dual-write conflicts (source and MLS both update) | Data inconsistency | `is_externally_managed` flag + selective merge function with field-level precedence |
| Field mapping errors (RESO → Dash) | Wrong data in listings | Reuse existing ETL mapping logic (already tested in Silver→Gold); add integrity checks |
| Performance: large ingress batches | CDL overload | Batch ingress via RPC with configurable batch size; run during off-peak |
| Broker confusion: which listings are "mine" | UX friction | Clear "Ingested" badge + separate view in MLS app; auto-assign by market/office |
| Dash push failures | Syndication gap | Retry queue in `mls_listing_syndications` with status tracking |
| RESO Web API backward compatibility | API consumers break | `property_reso` view maintains exact same column names and types |

## Success Criteria

1. All existing Qobrix/Dash listings appear in `mls_listings` with `status = INGESTED`
2. Brokers can claim, enrich, and publish ingested listings through the MLS app
3. Published listings with modifications appear in Dash (push) and RESO Web API
4. No data loss during the transition — all source data preserved via `origin_*` columns
5. CDC continues to work — incremental updates flow from source through to CDL
6. The RESO Web API returns identical results (served from view instead of Gold table)

## Dependencies

| Dependency | Owner | Needed By |
|-----------|-------|-----------|
| MLS app UI (listing form, status pipeline) | Lovable / MLS team | Phase C |
| Databricks sync notebook updates | Data Engineering | Phase B |
| Supabase migration (new columns, functions, view) | Data Engineering | Phase A |
| Dash API push credentials and endpoint access | SIR / Dash team | Phase D |
| RESO Web API query target change | Data Engineering | Phase D |

## Cross-Reference

| For | See |
|-----|-----|
| Current ETL pipeline | `docs/data-models/etl-pipeline.md` |
| MLS CDL schema (18 tables) | `docs/data-models/mls-cdl-schema.md` |
| Dash field names | `docs/data-models/dash-data-model.md` |
| RESO ↔ Dash field mapping | `docs/data-models/property-field-mapping.md` |
| Platform extensions (x_sm_*) | `docs/data-models/platform-extensions.md` |
| Phased migration roadmap | `docs/platform/mls-datamart.md` |
| Full ecosystem architecture | `docs/platform/ecosystem-architecture.md` |
