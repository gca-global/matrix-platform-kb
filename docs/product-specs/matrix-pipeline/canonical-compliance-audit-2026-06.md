---
title: Canonical-compliance audit — matrix-pipeline-2-0 + matrix-atlas-mls + CDL surface
status: active
last_updated: 2026-06-05
tags: [audit, reso, canonical, cdl, alignment]
instances: docs/platform/alignment-audit-playbook.md
---

# Canonical-compliance audit — matrix-pipeline-2-0 + matrix-atlas-mls + CDL surface

> An instance of the [Alignment Audit Playbook](../../platform/alignment-audit-playbook.md)
> scoped to RESO DD 2.0 canonical compliance across the two CDL-connected
> apps (`matrix-pipeline-2-0` CRM, `matrix-atlas-mls` MLS admin) and the CDL
> data model + `cdl-*` / `mls-sync` Edge Functions they touch. Every field/
> resource/lookup claim below is verified against the **live RESO corpus**
> (`public.reso_field_descriptions`, `public.reso_lookup_value_descriptions`)
> and the **live CDL schema** (`information_schema`) on project
> `ofzcokolkeejgqfjaszq`.

## Verdict — strongly canonical, with bounded drift

Both apps are well-aligned to RESO DD 2.0 and the "vanilla sales automation"
vision. Every CDL table the CRM touches (`contacts`, `contact_listings`,
`contact_listing_notes`, `showings`/`showing`/`showing_request`/
`showing_availability`, `lock_or_box`, `saved_search`, `prospecting`,
`transaction_management`, `caravan`/`caravan_stop`, `internet_tracking_events`)
uses canonical RESO snake_case column names; the only non-RESO columns are
standard CDL plumbing (`id`, `source_id`, `content_hash`,
`is_visible`/`is_deleted`/`deleted_at`, `raw`, `locked_fields`,
`created_at`/`updated_at`) and the registered `x_` extensions. Atlas writes the
MLS property/media surface only through `mls-sync` with canonical keys.

Drift is concentrated in the P0–P5 buckets below. None breaks the canonical
foundation; most are documentation accuracy, a few are enforcement/hygiene
gaps, two are genuine functional bugs in Atlas Listings Search.

## What "100% RESO compliance" means here

100% compliance is **not** "zero extensions" — RESO has real gaps (showing↔contact
linkage, contact privacy, free-text property title). It is the conjunction of
three testable conditions, each verifiable against the live corpus:

1. **Right field, right resource** — every stored/referenced field that has a
   RESO home uses the canonical resource + `PascalCase→snake_case` name.
2. **Closed-lookup values are standard** — every value written to a RESO
   closed-lookup column is a real `standard_value`; non-standard
   cadences/states are remapped or declared a registered extension.
3. **Every residual non-RESO field is a governed `x_` extension** — registered
   in [platform-extensions.md](../../data-models/platform-extensions.md) with a
   stated RESO gap; nothing non-canonical is silently passed through.

## Findings table (playbook Deliverable 1)

| # | Dim. | Severity | Finding | Evidence | Remediation (tier) |
|---|------|----------|---------|----------|--------------------|
| 1 | D2 | High | `x_property_name` materialized on `properties`, used by both apps + `listings-search`, but unregistered; absent from `properties_published` while the EF free-text-searches it there | corpus `Property.X_PropertyName` (`source=vendor_extension`); `listings-search/index.ts` ~L253 | P0 |
| 2 | D1 | High | `cdl-schema.md` L335-338 documents `x_is_sir_branded`/`x_sir_office_id`/`x_sir_designation` (+`v_dash_*`) as materialized; not present in live `properties`/`members` | `information_schema.columns` (CDL) | P0 |
| 3 | D2 | Med | `contact_listings.relationship` (`Seller`/`Developer`, Qobrix) is not a RESO `ContactListings` field but is in the `cdl-contact-listings-read` FILTERABLE set | `cdl-contact-listings-read/index.ts`; corpus (no such field) | P0 |
| 4 | D5 | High | `cdl-write` is a full record passthrough with no column-name validation | `cdl-write/index.ts` | P1 |
| 5 | D5 | Med | `cdl-read` accepts unvalidated `order.column` | `cdl-read/index.ts` ~L162 | P1 |
| 6 | D7 | Med | `ShowingStatus` attributed to `Property`; corpus has it only on `Showing` | `listing-lifecycle.md` L273, `showing-lifecycle.md` L172-174 | P2 |
| 7 | D7 | Med | `OrganizationUniqueId` / `OfficeCorporateLicenseState`/`...ExpirationDate` attributed to `Office` | `office-onboarding.md` L62; corpus `OUID.*` / `OfficeCorporateLicense.*` | P2 |
| 8 | D7 | Med | `Property.ClassName` referenced; no such field (ClassName is metadata/history only) | `caravan-lifecycle.md` L145 | P2 |
| 9 | D7 | Med | `Media.DocumentStatus` + `x_doc_status`; corpus has `Property.DocumentStatus` | `listing-lifecycle.md` L246-247 | P2 |
| 10 | D7 | Med | `HistoryTransactional.ChangeType='Object Modified'` — not a ChangeType value; it's an `EventType` (`InternetTracking`) value | `history-and-audit-log.md` L77; corpus | P2 |
| 11 | D7 | Med | `HistoryTransactional.ResourceName=Field/Lookup` invalid (closed lookup = Association/Contacts/Member/Office/Property); team-audit Member-vs-Office disagreement | `field-and-lookup-metadata-publication.md`, `team-lifecycle.md` L133 | P2 |
| 12 | D2 | Med | `x_commission_pct` referenced unregistered; canonical comp fields exist | `listing-lifecycle.md` L303, `member-onboarding.md` L204; corpus `Property.BuyerBrokerageCompensation*` | P2 |
| 13 | D7 | Med | `ScheduleType` extension values `Weekly`/`OnNewMatch`/`Custom`; corpus lookup = ASAP/Daily/Monthly on `Prospecting` | `prospecting-and-saved-search-delivery.md` L224-227 | P2 |
| 14 | D6 | Low | Stale catalogue: process counts ("Ten" vs 15), USAGE refresh path, prospecting provisioning contradiction, PropertyPowerProduction, early-vs-canonical property columns, empty reso-canonical-schema stub | `canonical-processes/AGENTS.md`, `cdl-schema.md` L83-95/455-463/666 | P3 |
| 15 | D5 | High | **CRM calls Atlas's `mls-sync` EF** — thin-client boundary violation (6 call sites) | `pipeline LabelOverridesPanel.tsx` L133/142/255/262/284/288 | P4 |
| 16 | D5 | Med | App copy references non-existent `cdl-contacts-write` EF; direct anon reads of `history_transactional`; dead direct-access hooks | `ContactDetail.tsx`, `useContactHistory.ts`, `useMlsData.ts` | P4 |
| 17 | D7 | High | **Atlas BUG**: `applyListingKind` filters spaced strings not RESO tokens — chips never match | `atlas useListingsSearch.ts` L83-87 | P5 |
| 18 | D3 | High | **Atlas BUG**: dead `includeMedia` param; UI reads `images`/`cover_image_url` never populated | `atlas ListingsSearch.tsx` L49, `useListingsSearch.ts` | P5 |
| 19 | D2 | Med | Atlas legacy media `order` column on CDL reads; `media-upload` payload `kind`/`order_index` | `atlas useCuratedList.ts` L83-85/156-158, `useMlsData.ts` L592-621 | P5 |
| 20 | D2 | Med | Atlas `district` — non-RESO/non-`x_` column on CDL reads + silently-ignored filter key | `atlas useCuratedList.ts`, `useListingsSearch.ts` L27/128 | P5 |
| 21 | D5 | Med | Atlas direct anon reads of `contacts` + `contact_listings` (PII) bypass EF gate | `atlas RecordEditDialog.tsx` L492-496, `useMlsData.ts` L285-291 | P5 |
| 22 | D3 | Low | Atlas `DataModelPanel.tsx` PascalCase/legacy `dbColumn`s; `PropertyPicker` bind mismatch; `MLS_STATUS_VALUES` internal/draft; dead `mls_listings_cache` type | `atlas DataModelPanel.tsx`, `PropertyPicker.tsx` L19, `types.ts` | P5 |

## RESO-divergence register (governed extensions — compliant end-state)

These have no RESO canonical home and remain **registered** `x_` extensions
(or `raw`-scoped structures). They are the residual, justified divergence:

| Field / structure | RESO gap | Disposition |
|---|---|---|
| `x_contact_key` (showings/showing/showing_request) | RESO has no buyer↔showing FK | Registered extension (ADR-022) |
| `x_privacy_level` (contacts) | RESO has no contact-privacy enum | Registered extension |
| `x_property_name` | No free-text marketing-title field (building/development names → `BuildingName`) | Register where free-text; migrate to `Property.BuildingName` where it is a building name (P0) |
| `x_commission_pct` (member split) | RESO models listing *compensation*, not agent comp split | Registered extension / HRMS (P2) |
| `saved_search.raw->criteria` camelCase keys | Structured search mirror | Documented `raw` escape hatch (ADR-016) |
| `x_` prefix itself | No RESO basis | ADR-023 |

### Data-layer lookup-casing divergence (P6 — ingestion fix, NOT a frontend fix)

The live `properties_published` (and `properties`) store enumerated lookup
values in **PascalCase, space-stripped** form — `FullService`,
`ResidentialLease`, `CommercialLease`, `Residential` — whereas the canonical
RESO `ListingService` / `PropertyType` corpus values are **space-separated**
(`Full Service`, `Residential Lease`, `Commercial Lease`). This is a genuine
RESO-compliance gap **at the data/ingestion layer**, not in the apps:

- It is corpus-verified: `reso_lookup_value_descriptions` lists the spaced
  forms; `select distinct listing_service/property_type from properties_published`
  returns the PascalCase forms.
- The Atlas FE type model (`PROPERTY_TYPE_VALUES`, `LISTING_SERVICE_VALUES`)
  and both the chip filter (`useListingsSearch.ts#applyListingKind`) and the
  inverse classifier (`propertyTypes.ts#listingKind`) were brought into
  lock-step on the **stored PascalCase tokens** (2026-06 audit), which fixed a
  live bug where the filter used spaced tokens and returned zero rows. The FE
  must match the data; it cannot unilaterally switch to spaced values without
  re-ingestion.
- **Disposition (P6):** normalise the ingestion mapping (`reso-import` /
  `csv-import` / `crm-import` → `listing-merge`) to emit canonical
  space-separated RESO lookup values, backfill `properties` +
  `properties_published`, then flip the Atlas enums/tokens to the spaced
  canonical forms in the same change. Until then the PascalCase tokens are the
  de-facto contract and the FE follows them.

## Corpus-verified corrections (the canonical targets)

- `ShowingStatus` → **`Showing.ShowingStatus`** (values: `Accepting Requests`, `On Hold`, `No Showings`, `Restricted Showings`).
- `OrganizationUniqueId` → **`OUID.OrganizationUniqueId`**. `OfficeCorporateLicenseState`/`ExpirationDate`/`Type` → **`OfficeCorporateLicense`** resource. Keep `Office.OfficeCorporateLicense` (license number) on `Office`.
- `Property.ClassName` → **`Property.PropertyType`** (+ `PropertySubType`). `ClassName` exists only on metadata/history resources.
- `Media.DocumentStatus`/`x_doc_status` → **`Property.DocumentStatus`** (values incl. `Published`, `Submitted`, `Signed`, `Received`, `Required`, `Archived`, `Deleted`).
- `HistoryTransactional.ChangeType='Object Modified'` → split: listing field-change history uses `ChangeType` (lifecycle values: `New Listing`, `Price Change`, `Active`, `Pending`, `Closed`, `Withdrawn`, `Deleted`…; note `Property.MajorChangeType`); generic object/engagement events use **`InternetTracking.EventType`** (`Object Modified`, `Detailed View`, `Favorited`…).
- `HistoryTransactional.ResourceName` closed lookup = **{`Association`, `Contacts`, `Member`, `Office`, `Property`}**. `Field`/`Lookup` invalid → metadata changes tracked via the `Field`/`Lookup` resources' own `ModificationTimestamp`. Team-audit rule: roster change → `Member`; office-composition → `Office`.
- `x_commission_pct` (listing) → **`Property.BuyerBrokerageCompensation`** + **`BuyerBrokerageCompensationType`** (`CompensationType`: `%`, `$`, `Other`, `See Remarks`).
- `ScheduleType` → **`Prospecting.ScheduleType`** standard values `ASAP`/`Daily`/`Monthly` (`OnNewMatch`→`ASAP`; `Weekly`/`Custom` drop or register tenant lookup extension).

## Staged remediation plan (playbook Deliverable 2)

Ordered additive → consolidation → deletion → rename, routed per the
[cursor-git-handoff](../../../.cursor/rules/cursor-git-handoff.mdc) rule.

| Tier | Stage | Repo(s) | Invariant established |
|---|---|---|---|
| P0 | Register `x_property_name`; fix `properties_published` mirror; correct SIR markers + `relationship` classification | KB + foundation (CDL) | Every materialized non-RESO column is a registered extension or documented removal |
| P1 | `cdl-write` per-resource writable-column allow-list; `cdl-read` order-column allow-list | foundation (CDL) | No non-canonical column can persist or sort silently |
| P2 | Corpus-verified process corrections + extension canonicalization | KB | Process docs cite only real RESO resources/values |
| P3 | Catalogue/contradiction cleanup | KB | Cross-doc counts/paths consistent |
| P4 | Decouple CRM from `mls-sync` (→ `app-i18n`); EF discipline | pipeline + foundation + KB | CRM is `mls-sync`-free; one responsibility per EF |
| P5 | Atlas: fix listing_kind + media bugs, district, PII gate, doc drift | atlas | Listings Search filters/media work; canonical names only |

### P4 implementation note (2026-06-05) — i18n admin EF home

The initial P4 sketch routed `app_ui_string` through `app-i18n` and
`reso_label_override` **writes** through `cdl-write`. Implementation routes
**both** i18n resources through the dedicated **`app-i18n`** EF (one new POST
admin surface alongside the existing public GET bundle), and `cdl-write` was
**not** extended for them. Rationale (KB-first escape hatch):

- `cdl-write` is the canonical-**CRM** write path. Its P1 boundary validator now
  rejects any non-RESO-snake_case / unregistered column. The label-override
  tables (`reso_field_descriptions`, `reso_lookup_value_descriptions`,
  `app_ui_strings`) are **i18n control-plane** tables with columns like `field`,
  `display_name`, `tenant_key`, `string_key` — not canonical CRM resources.
  Forcing them into `cdl-write` would mean carving permanent non-canonical
  exceptions into the exact guard P1 exists to enforce.
- `app-i18n` already owns the i18n read surface (ADR-021). Co-locating the
  admin CRUD there yields **one responsibility per EF** (all app-i18n concerns
  in one place) and keeps `cdl-write` purely canonical. Handlers were ported
  verbatim from `mls-sync` (behaviour-preserving); writes are forced to
  `tenant_key = caller JWT tenant` + `source='team_override'`; SSO JWT verified
  in-function (admin scopes only). Contract: `docs/cdl-ef-contracts/reso-label-overrides.md`.

### P5 implementation note (2026-06-05) — Atlas canonical fixes shipped

All P5 Atlas (`matrix-atlas-mls`) findings (#17–22) are implemented; `npm run
typecheck` is green. Summary of the disposition per finding:

- **#17 `applyListingKind` (D7) + #18 `includeMedia` (D3):** the chip filter and
  the inverse classifier (`propertyTypes.ts#listingKind`) were brought into
  lock-step on the **stored PascalCase** lookup tokens (`FullService`,
  `ResidentialLease`, `CommercialLease`), which fixed the zero-rows bug. The FE
  must follow the data; the spaced-vs-PascalCase mismatch is the **data-layer**
  gap tracked under P6 below (ingestion fix), not a frontend fix. `includeMedia`
  now fetches cover images from `property_media` (`cover_image_url`).
- **#19 media legacy `order` (D2):** `useCuratedList`/`PropertyMediaManager` use
  canonical `listing_key` + `media_order` + `media_url`/`media_category`; the
  `url`/`kind`/`order_index`/`caption` legacy fallbacks were dropped.
- **#20 `district` (D2):** renamed to the canonical RESO **`city_region`** across
  `useCuratedList`, `CuratedList`, `CuratedListPropertyDetail`; the silently
  ignored `district` filter key in `useListingsSearch` was replaced by a working
  canonical `city_region` ilike filter (it is a real `properties_published`
  column).
- **#21 PII gate (D5):** the direct anon reads of `contacts` / `contact_listings`
  were re-routed through the scoped CDL EFs — `usePropertyContactListings` →
  `cdl-contact-listings-read` `op=by-property` (replaces the retired
  `v_property_contacts`); `useContactListings` → `op=list` (then enriches listing
  name/address from anon-readable, non-PII `properties_published`); the member
  "contacts owned" count → `cdl-contacts-read` `op=list` (`total`). No PII table
  is read via the anon client any more.
- **#22 doc drift (D3):** `DataModelPanel.tsx` now lists canonical snake_case
  `dbColumn`s for **every** resource block (Property/Member/Office/Contacts/
  Media/Showing/OpenHouse/History/InternetTracking) — `source_listing_key →
  listing_key`, `district → city_region`, `MediaURL → media_url`, `Order →
  media_order`, `MemberKey → member_key`, etc.; `PropertyPicker` `bind:'listing_key'`
  now returns `listing_key` (was `originating_system_key`); `MLS_STATUS_VALUES`
  is canonical RESO `StandardStatus` only (the non-RESO `internal`/`draft` were
  dropped — drafts are the canonical `Incomplete`, internal-only is the
  `is_visible` flag); the dead `mls_listings_cache` generated type was removed.

## Recommendation (playbook Deliverable 3)

Ship **P1 (cdl-write allow-list)** and **P5 listing_kind/media bugs** first:
the former is the single mechanical guard that keeps the whole surface canonical
forever after (drift becomes a rejected write, not a silent column); the latter
are user-facing Listings-Search bugs with self-contained fixes. P0/P2/P3 are
documentation-and-registry safe to batch into one KB + one CDL commit.

## KB sources consulted

- [alignment-audit-playbook.md](../../platform/alignment-audit-playbook.md),
  [cdl-schema.md](../../data-models/cdl-schema.md),
  [platform-extensions.md](../../data-models/platform-extensions.md),
  [reso-canonical-schema.md](../../data-models/reso-canonical-schema.md),
  `business-processes/canonical-processes/**`,
  ADR-016 / ADR-022 / ADR-023.
- Live CDL `information_schema` + RESO corpus
  (`public.reso_field_descriptions`, `public.reso_lookup_value_descriptions`)
  via the CDL `execute_sql` MCP — every P2 correction is corpus-verified.
- Code: `matrix-pipeline-2-0/src/**`, `matrix-atlas-mls/src/**`,
  `matrix-platform-foundation/supabase/cdl/functions/**`.
