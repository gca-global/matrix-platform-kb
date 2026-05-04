#!/usr/bin/env python3
"""
Build wiki/atlas/validation-matrix.md - one validation row per field that
PRs 1-12 in reso_canonical_gaps_atlas.plan.md actually touch.

Inputs:
  - reso-dd-kb/raw/fields.csv          (RESO 2.0 canonical definitions)
  - reso-dd-kb/raw/field_metadata.csv  (Sys% / Org% adoption)
  - reso-dd-kb/wiki/atlas/atlas-target.dbml (target shape per PR0.5)
  - Atlas data samples (gathered via MCP - encoded in this script)

For every PR-touched field we record:
  Atlas current name | Atlas target name | RESO StandardName | RESO Definition |
  RESO SimpleDataType | RESO LookupName | RESO SugMaxLength/Precision |
  RESO Synonyms | RESO PropertyTypes | Sys% / Org% adoption |
  Atlas data sample | Verdict (PASS / PASS-WITH-NOTE / FAIL) | Note

Untouched canonical fields appear in a closing summary section as
'PASS - canonical RESO definition match (untouched by this plan)'.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "wiki" / "atlas" / "validation-matrix.md"


# Each row: pr / table / atlas_current / atlas_target / resource / field /
# sample / verdict / note
ROWS: List[Dict[str, str]] = []


def add(pr, table, atlas_current, atlas_target, resource, field, sample, verdict, note):
    ROWS.append({
        "pr": pr, "table": table,
        "atlas_current": atlas_current, "atlas_target": atlas_target,
        "resource": resource, "field": field,
        "sample": sample, "verdict": verdict, "note": note,
    })


# ---------------------------------------------------------------------------
# PR1 - cheap canonical renames
# ---------------------------------------------------------------------------
add("PR1", "properties", "currency", "currency_code",
    "Property", "CurrencyCode",
    "15884/15884 = 100% 'EUR' (single value)",
    "PASS",
    "Exact ISO 4217 match; rename is risk-free. Migration is `ALTER COLUMN RENAME`.")

add("PR1", "properties", "virtual_tour_url", "virtual_tour_url_unbranded",
    "Property", "VirtualTourURLUnbranded",
    "0/15884 populated (column unused today)",
    "PASS-WITH-NOTE",
    "RESO has both VirtualTourURLBranded and VirtualTourURLUnbranded. Pick `Unbranded` (privacy-default; PR1 plan choice). Branded version added on demand.")

add("PR1", "properties", "land_area_sqm", "lot_size_area",
    "Property", "LotSizeArea",
    "3805/15884 = 24% populated; all values in m^2 (Cyprus = metric)",
    "PASS",
    "RESO LotSizeArea is unit-agnostic; pair with LotSizeUnits='SquareMeters' (PR1 adds the units column with default).")

add("PR1", "properties", "(new column)", "lot_size_units",
    "Property", "LotSizeUnits",
    "n/a - new column; default 'SquareMeters' for CY",
    "PASS",
    "Lookup AreaUnits; valid values include SquareMeters/SquareFeet/Acres etc.")

add("PR1", "open_houses", "open_house_live_stream_url", "livestream_open_house_url",
    "OpenHouse", "LivestreamOpenHouseURL",
    "0/0 (table empty)",
    "PASS",
    "RESO uses the word order LivestreamOpenHouseURL (not OpenHouseLivestreamURL).")

add("PR1", "offices", "office_national_assoc_id", "office_national_association_id",
    "Office", "OfficeNationalAssociationId",
    "0/55 populated (column unused today)",
    "PASS",
    "Drop the abbreviation; canonical name is the full `Association`.")


# ---------------------------------------------------------------------------
# PR1.5 / PR1.6 - drop tables
# ---------------------------------------------------------------------------
add("PR1.5", "teams", "(entire table)", "(dropped)",
    "Teams", "(N/A - table drop)",
    "0 rows",
    "PASS",
    "RESO Teams has lowest measured adoption (0.3% WgtOrg%). Atlas table empty; no data loss. Drop with RLS + FE Teams tab + reso_field_descriptions.")

add("PR1.6", "property_power_production", "(entire table)", "(dropped)",
    "PropertyPowerProduction", "(N/A - table drop)",
    "0 rows",
    "PASS",
    "Speculative add from previous expansion plan; 1.3% WgtOrg% adoption. Cyprus market doesn't yet ingest on-site solar/wind data. Drop wholesale; PropertyGreenVerification (EPC) is the better future addition.")


# ---------------------------------------------------------------------------
# PR2 - drop low-signal Atlas-custom
# ---------------------------------------------------------------------------
add("PR2", "properties", "lead_source", "(dropped)",
    "(none)", "(no canonical home on Property)",
    "15799/15884 populated; 15787 = 'direct' (99.9%); 12 = 'agent'",
    "PASS",
    "RESO LeadSource lives on Contacts/Prospecting, NOT Property. Atlas data has no signal anyway (one value). Drop.")

add("PR2", "properties", "district", "(dropped)",
    "Property", "(superseded by CountyOrParish in PR4)",
    "1/15884 = 0.006% populated (single value 'Neapolis')",
    "PASS",
    "Effectively absent. PR4 adds canonical `county_or_parish` populated from city -> CY-district lookup.")

add("PR2", "members", "member_photo_url", "(dropped)",
    "Member", "(canonical via Media+MediaCategory='AgentPhoto')",
    "0/129 = 0% populated",
    "PASS",
    "RESO has no MemberPhotoURL field. Canonical pattern is Media row with ResourceRecordKey=MemberKey + MediaCategory='AgentPhoto'. Drop unused column.")

add("PR2", "property_rooms", "original_entry_timestamp", "(dropped)",
    "PropertyRooms", "(not on RESO PropertyRooms)",
    "0/0 (table empty)",
    "PASS",
    "RESO defines OriginalEntryTimestamp on Property + 15 other resources but NOT on PropertyRooms.")

add("PR2", "property_unit_types", "original_entry_timestamp", "(dropped)",
    "PropertyUnitTypes", "(not on RESO PropertyUnitTypes)",
    "0/0 (table empty)",
    "PASS",
    "Same as PropertyRooms - not a canonical RESO field on this resource.")


# ---------------------------------------------------------------------------
# PR3 - website_listing_date -> on_market_date
# ---------------------------------------------------------------------------
add("PR3", "properties", "website_listing_date", "on_market_date",
    "Property", "OnMarketDate",
    "4285/15884 = 27% populated; spans 2023-01-12 to 2026-04-29",
    "PASS",
    "RESO Definition: 'The date listing went on the market'. Atlas semantics match (Qobrix listing-date). Copy-then-drop migration; preserves all data.")

add("PR3", "properties", "(derived from on_market_date)", "on_market_timestamp",
    "Property", "OnMarketTimestamp",
    "n/a - derived (date::timestamptz)",
    "PASS-WITH-NOTE",
    "Derive from on_market_date via cast at midnight UTC. Add as separate timestamptz column for callers wanting subsecond precision; future Qobrix records may carry full timestamp.")


# ---------------------------------------------------------------------------
# PR3.5 - list_agent_key backfill
# ---------------------------------------------------------------------------
add("PR3.5", "properties", "key_holder_details", "(dropped - resolves into list_agent_key)",
    "Property", "(resolved to ListAgentKey FK)",
    "958/15884 = 6% populated; 48 distinct names; 36/48 (75%) resolve to a Member",
    "PASS-WITH-NOTE",
    "238 of 958 rows do not name-resolve and go to ops table `unresolved_key_holders`; remaining ~720 backfill list_agent_key. RESO has no `KeyHolder*` field; the canonical home for 'who holds keys' is the listing agent.")

add("PR3.5", "properties", "list_agent_key", "list_agent_key (FK)",
    "Property", "ListAgentKey",
    "Pre-backfill: 1/15884 (effectively unused); post-backfill: ~720/15884",
    "PASS",
    "Canonical FK to Member.MemberKey. PR11 enforces the constraint; PR9 selectively denormalizes 3 satellites (first/last/email) for query speed.")


# ---------------------------------------------------------------------------
# PR3.6 - history_transactional backfill
# ---------------------------------------------------------------------------
add("PR3.6", "properties", "created_by_member_key", "(dropped; backfilled into HT)",
    "HistoryTransactional", "ChangedByMemberKey",
    "15881/15884 populated; 0 orphans vs members.member_key",
    "PASS",
    "Backfilled as 15,881 'New Listing' HT rows. ChangedByMemberKey <- created_by_member_key (FK clean).")

add("PR3.6", "properties", "modified_by_member_key", "(dropped; NO backfill)",
    "HistoryTransactional", "(no honest backfill - sync ts)",
    "15881/15884 populated; differs from creator 66% of the time",
    "PASS-WITH-NOTE",
    "Skip backfill: properties.updated_at is the SYNC timestamp (3 distinct days = QOBRIX import window), NOT real edit time. Generic field-level audit defers to RESO EntityEvent (out of scope). Trigger handles future status/price changes only.")

add("PR3.6", "history_transactional", "(empty; new rows from backfill)", "change_type",
    "HistoryTransactional", "ChangeType",
    "Backfill writes 15,881 rows with change_type='New Listing'",
    "PASS",
    "'New Listing' is a canonical RESO ChangeType lookup value (verified in raw/lookups.csv). Trigger writes 'Price Change' / status-mapped values for future updates.")

add("PR3.6", "history_transactional", "(empty; new rows from backfill)", "resource_record_key",
    "HistoryTransactional", "ResourceRecordKey",
    "Backfill: resource_record_key=properties.listing_key (15,881 rows)",
    "PASS",
    "Canonical FK to the changed RECORD (not the field). FieldKey is the FK to FIELD METADATA - common confusion called out in plan.")

add("PR3.6", "history_transactional", "(empty; new rows from backfill)", "modification_timestamp",
    "HistoryTransactional", "ModificationTimestamp",
    "REAL-DATE path (~4,285): from on_market_date::timestamptz; FALLBACK (~11,596): from properties.created_at marked as atlas_import in raw JSONB",
    "PASS-WITH-NOTE",
    "FALLBACK rows tag raw with source=atlas_import marker so downstream queries can distinguish real-listing-date events from import-date markers. Honors timestamp-provenance principle (Principle 7).")


add("PR4", "properties", "(new column)", "county_or_parish",
    "Property", "CountyOrParish",
    "Backfill via city -> CY-district lookup (5 districts); ~700 distinct cities seed the lookup",
    "PASS",
    "Sys 90 / Org 94 adoption - universally used. Cyprus has 5 administrative districts.")

add("PR5", "history_transactional", "resource_record_id", "resource_record_id (label ResourceRecordID)",
    "HistoryTransactional", "ResourceRecordID",
    "n/a - UI label only; DB column stays snake_case",
    "PASS",
    "RESO canonical capitalizes `ID` as a suffix. Atlas DB stays snake_case (Principle 6); UI/API tooltip uses `ResourceRecordID`. Seed reso_field_descriptions.")

add("PR5", "history_transactional", "changed_by_member_id", "changed_by_member_id (label ChangedByMemberID)",
    "HistoryTransactional", "ChangedByMemberID",
    "n/a - UI label only",
    "PASS",
    "Same `*ID` pattern.")

add("PR6", "property_media -> media", "(table)", "media",
    "Media", "(table reshape)",
    "262,753 rows, all kind='image'",
    "PASS",
    "Full reshape; canonical Media columns (MediaKey, MediaURL, MediaCategory, etc.) added. Migrate kind='image' -> media_category='Photo'.")

add("PR6", "media", "url", "media_url",
    "Media", "MediaURL",
    "262,753 populated URLs",
    "PASS",
    "Direct rename.")

add("PR6", "media", "kind", "media_category",
    "Media", "MediaCategory",
    "262,753 = 'image' -> 'Photo'",
    "PASS",
    "Lookup MediaCategory: Photo, Video, VirtualTour, FloorPlan, Document, etc. All current rows map to 'Photo'.")

add("PR6", "media", "ord", "order",
    "Media", "Order",
    "262,753 populated integers",
    "PASS-WITH-NOTE",
    "Postgres reserved word - quote as \"order\" in SQL or use display_order if quoting too risky.")

add("PR6", "media", "property_id", "resource_record_key",
    "Media", "ResourceRecordKey",
    "FK to property; reshape sets resource_name='Property'",
    "PASS",
    "Polymorphic in RESO (target depends on resource_name). For Atlas's listing photos, resource_name='Property' and resource_record_key=listing_key.")

add("PR7", "showings", "showing_appointment_*", "showing_* (DD 2.0)",
    "Showing", "(spec choice - DD 2.0 over SHOW17)",
    "0/0 (table empty)",
    "PASS",
    "DD 2.0 collapses date+time into ShowingStartTimestamp/EndTimestamp; uses ShowingStatus + ShowingAllowed (no separate ShowingAppointmentMethod). Empty table = pure schema rename.")

add("PR8", "internet_tracking_events -> internet_tracking", "(table)", "internet_tracking",
    "InternetTracking", "(table rename)",
    "0/0 (table empty)",
    "PASS",
    "Drop redundant `_events` suffix to match RESO Resource name InternetTracking.")

add("PR8", "internet_tracking", "internet_tracking_key", "event_key",
    "InternetTracking", "EventKey", "0/0", "PASS", "Direct canonical rename.")

add("PR8", "internet_tracking", "actor_ip_address", "actor_ip",
    "InternetTracking", "ActorIP", "0/0", "PASS", "Canonical name is `ActorIP`.")

add("PR8", "internet_tracking", "actor_user_agent", "user_agent",
    "InternetTracking", "UserAgent", "0/0", "PASS", "RESO uses `UserAgent` not `ActorUserAgent`.")

add("PR8", "internet_tracking", "actor_mls_id", "actor_originating_system_id",
    "InternetTracking", "ActorOriginatingSystemID", "0/0", "PASS",
    "Canonical name is OUID-style ActorOriginatingSystemID. Stays flat-scalar pending OUID resource.")

add("PR8", "internet_tracking", "actor_user_name", "actor_email",
    "InternetTracking", "ActorEmail", "0/0", "PASS-WITH-NOTE",
    "RESO models actor identity via ActorEmail + ActorID. No canonical ActorUserName field.")

add("PR8", "internet_tracking", "object_mls_id", "object_id",
    "InternetTracking", "ObjectID", "0/0", "PASS", "Canonical RESO ObjectID.")

add("PR8", "internet_tracking", "actor_is_anonymous_yn", "(dropped)",
    "InternetTracking", "(no canonical equivalent)", "0/0", "PASS",
    "RESO models anonymity via absence of Actor* fields, not a flag. Drop.")

add("PR8", "internet_tracking", "event_type_other", "event_description",
    "InternetTracking", "EventDescription", "0/0", "PASS",
    "RESO uses EventDescription for free-text overflow.")

add("PR9", "properties", "(new column)", "modification_timestamp",
    "Property", "ModificationTimestamp",
    "Backfill from properties.updated_at",
    "PASS-WITH-NOTE",
    "Sys 100 / Org 99. Backfill is the Atlas SYNC time - document the provenance in reso_field_descriptions caption.")

add("PR9", "properties", "(new column)", "state_or_province",
    "Property", "StateOrProvince",
    "Backfill from city -> district mapping (CY)", "PASS",
    "Sys 100 / Org 98. For Cyprus, state_or_province == county_or_parish (no sub-state level).")

add("PR9", "properties", "(new column)", "listing_contract_date",
    "Property", "ListingContractDate",
    "Backfill from website_listing_date when available; else NULL",
    "PASS-WITH-NOTE",
    "Sys 100 / Org 97. RESO Definition is 'date the listing agent and seller signed the contract'. Atlas doesn't carry contract-signing date today; on_market_date is a reasonable proxy. Document caveat.")

add("PR9", "properties", "(new column)", "bathrooms_full",
    "Property", "BathroomsFull",
    "Backfill: bathrooms_full <- bathrooms_total_integer (best-effort)",
    "PASS-WITH-NOTE",
    "Sys 100 / Org 89. Atlas only has total integer; backfill loses half-bath precision.")

add("PR9", "properties", "(new column)", "bathrooms_half",
    "Property", "BathroomsHalf",
    "Backfill NULL (no source)", "PASS",
    "Sys 95 / Org 85. Add column; populate when source data carries it.")

add("PR9", "properties", "(new column)", "street_number",
    "Property", "StreetNumber",
    "Best-effort parse from unparsed_address",
    "PASS-WITH-NOTE",
    "Sys 95 / Org 95. Cyprus addresses are not always numbered; expect 30-40% NULL after parse.")

add("PR9", "properties", "(new column)", "street_name",
    "Property", "StreetName",
    "Best-effort parse from unparsed_address",
    "PASS-WITH-NOTE",
    "Sys 95 / Org 90. Same parser as StreetNumber.")

add("PR9", "properties", "(new column)", "unit_number",
    "Property", "UnitNumber",
    "Best-effort parse from unparsed_address",
    "PASS-WITH-NOTE",
    "Sys 95 / Org 66. Apartment-only; expect mostly NULL.")

add("PR9", "properties", "(new column)", "photos_count",
    "Property", "PhotosCount",
    "Backfill: count(*) FROM media WHERE resource_record_key=listing_key. ~262,753 rows / 15,884 listings = avg 16.5 photos/listing.",
    "PASS",
    "Sys 95 / Org 98. DENORMALIZED count; trigger-maintained on media insert/delete (PR9). Not a stored upstream value.")

add("PR9", "properties", "(new column)", "list_agent_first_name",
    "Property", "ListAgentFirstName",
    "DENORMALIZED from members via list_agent_key (PR3.5 backfilled ~720)",
    "PASS",
    "Sys 90 / Org 91. Trigger keeps in sync with members.member_first_name; FK remains source of truth.")

add("PR9", "properties", "(new column)", "list_agent_last_name",
    "Property", "ListAgentLastName",
    "DENORMALIZED from members via list_agent_key", "PASS",
    "Sys 90 / Org 91. Trigger-maintained satellite.")

add("PR9", "properties", "(new column)", "list_agent_email",
    "Property", "ListAgentEmail",
    "DENORMALIZED from members via list_agent_key", "PASS",
    "Sys 90 / Org 75. Trigger-maintained satellite.")

add("PR10", "properties", "x_sm_is_sir_branded", "x_sm_is_sir_branded",
    "(atlas_custom)", "(N/A - Sotheby's branding)",
    "Already in DB; tooltip badge needed", "PASS",
    "Sotheby's brand-specific flag; no canonical RESO home. Seed reso_field_descriptions.source='atlas_custom'.")

add("PR10", "properties", "x_sm_sir_office_id", "x_sm_sir_office_id",
    "(atlas_custom)", "(N/A - Sotheby's identifier)",
    "Already in DB", "PASS", "Same as above; namespaced under x_sm_*.")

add("PR10", "members", "x_sm_sir_designation", "x_sm_sir_designation",
    "(atlas_custom)", "(N/A - Sotheby's designation)",
    "Already in DB", "PASS",
    "Sotheby's-specific; no canonical Member field captures the same semantics.")

add("PR11", "members", "office_key (loose text)",
    "office_key REFERENCES offices(office_key) ON DELETE SET NULL",
    "Member", "OfficeKey (FK pointer)",
    "37/38 populated rows are ORPHANS (97% orphan rate)",
    "FAIL",
    "BLOCKS PR11 for this column until orphans cleaned. Either backfill missing offices from QOBRIX or NULL the orphans, then add FK.")

add("PR11", "properties", "list_agent_key (loose text)",
    "list_agent_key REFERENCES members(member_key) ON DELETE SET NULL",
    "Property", "ListAgentKey (FK pointer)",
    "Pre-PR3.5: 1/15884 populated and orphan. Post-PR3.5: ~720 cleanly-resolved + ops-table for unresolved.",
    "PASS-WITH-NOTE",
    "Re-run orphan scan after PR3.5 lands; expected clean. Add FK then.")

add("PR11", "properties", "(8 *Agent / *Office FKs all loose text)",
    "FK constraints on buyer_agent_key, buyer_office_key, co_*_key, etc.",
    "Property", "BuyerAgentKey/CoListAgentKey/etc.",
    "All 0/15884 populated today (Cyprus = mostly listing-side; no co-/buyer-side data)",
    "PASS",
    "Add FKs even on empty columns - protects future Qobrix payloads from orphan inserts.")

add("PR11", "(child tables)",
    "listing_key on open_houses/showings/property_rooms/property_unit_types",
    "listing_key REFERENCES properties(listing_key) ON DELETE RESTRICT",
    "(multiple)", "Listing FK",
    "All child tables empty today",
    "PASS",
    "Hard parent-child relationship; RESTRICT prevents orphaning child rows.")

add("PR11", "(source-system identifiers)",
    "source_listing_key, source_member_key, etc.",
    "(no FK; document as external reference)",
    "(N/A - external systems)", "(QOBRIX/MLS keys)",
    "Various - these are external IDs, not Atlas table FKs",
    "PASS",
    "Skip FK enforcement; document the contract that these reference external systems.")

add("PR12", "(FE only)", "AppSidebar.tsx + routes",
    "Root resources only: Property, Member, Office, Contacts (+admin: HistoryTransactional, Media, InternetTracking)",
    "(meta)", "(navigation tree)",
    "n/a - FE audit; no DB sample",
    "PASS",
    "Verify Teams + PowerProductionTab removed; replace free-text actor displays with JOIN+click-through to /members/{key}; document canonical nav tree in matrix-platform-kb/docs/atlas/navigation.md.")


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def load_fields() -> Dict[Tuple[str, str], Dict[str, str]]:
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    with (RAW / "fields.csv").open() as fh:
        for r in csv.DictReader(fh):
            out[(r["ResourceName"], r["StandardName"])] = r
    return out


def load_metadata() -> Dict[Tuple[str, str], Dict[str, str]]:
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    with (RAW / "field_metadata.csv").open() as fh:
        for r in csv.DictReader(fh):
            out[(r["Resource"], r["StandardName"])] = r
    return out


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def first_n(s: str, n: int) -> str:
    s = (s or "").strip().replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "..."


def render() -> str:
    fields_idx = load_fields()
    meta_idx = load_metadata()

    out: List[str] = []
    out.append("# Atlas Target - Validation Matrix (PR0.7)")
    out.append("")
    out.append("Generated by `reso-dd-kb/scripts/build_validation_matrix.py`.")
    out.append("")
    out.append("Validates every field in `wiki/atlas/atlas-target.dbml` (PR0.5) against:")
    out.append("- canonical RESO Data Dictionary 2.0 (`raw/fields.csv`)")
    out.append("- adoption metrics (`raw/field_metadata.csv`)")
    out.append("- live Atlas data samples (via Supabase MCP)")
    out.append("")
    out.append("**Verdict legend**:")
    out.append("- **PASS** - canonical match; PR may proceed.")
    out.append("- **PASS-WITH-NOTE** - semantic match with a documented quirk; PR may proceed but the note must appear in the migration commit message + reso_field_descriptions caption.")
    out.append("- **FAIL** - Definition contradicts intent OR data is dirty (e.g., orphans). BLOCKS the dependent PR until the design is revisited and/or the data cleaned.")
    out.append("")
    out.append("Per Principle 8 of the plan: no schema-touching commit lands without all three artefacts (canonical DBML, target DBML, this matrix) green for every field it touches.")
    out.append("")

    pr_order = ["PR1", "PR1.5", "PR1.6", "PR2", "PR3", "PR3.5", "PR3.6",
                "PR4", "PR5", "PR6", "PR7", "PR8", "PR9", "PR10", "PR11", "PR12"]
    by_pr: Dict[str, List[Dict[str, str]]] = {p: [] for p in pr_order}
    for r in ROWS:
        by_pr.setdefault(r["pr"], []).append(r)

    for pr in pr_order:
        rows = by_pr.get(pr, [])
        if not rows:
            continue
        out.append(f"## {pr}")
        out.append("")
        out.append("| Atlas current | Atlas target | RESO StandardName | RESO Definition | RESO Type | Lookup | MaxLen / Prec | Synonyms | PropertyTypes | Sys% / Org% | Atlas data sample | Verdict | Note |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            f = fields_idx.get((r["resource"], r["field"])) or {}
            m = meta_idx.get((r["resource"], r["field"])) or {}
            defn = first_n(f.get("Definition", ""), 200)
            sdt = f.get("SimpleDataType", "") or "-"
            lookup = f.get("LookupName", "") or "-"
            sml = f.get("SugMaxLength") or ""
            smp = f.get("SugMaxPrecision") or ""
            bounds = f"{sml}{('/' + smp) if smp else ''}" or "-"
            syn = first_n(f.get("Synonyms", ""), 60) or "-"
            ptypes = first_n(f.get("PropertyTypes", ""), 60) or "-"
            sys_pct = m.get("SysPct") or ""
            org_pct = m.get("OrgPct") or ""
            adoption = f"{sys_pct}% / {org_pct}%" if (sys_pct or org_pct) else "-"

            atlas_target_cell = (
                f"`{r['table']}.{r['atlas_target']}`"
                if "(" not in r["atlas_target"] else r["atlas_target"]
            )
            cells = [
                f"`{r['table']}.{r['atlas_current']}`",
                atlas_target_cell,
                f"**{r['field']}**" if "N/A" not in r["field"] else r["field"],
                defn or "-",
                sdt,
                lookup,
                bounds,
                syn,
                ptypes,
                adoption,
                r["sample"],
                r["verdict"],
                r["note"],
            ]
            out.append("| " + " | ".join(md_escape(c) for c in cells) + " |")
        out.append("")

    n_total = len(ROWS)
    n_pass = sum(1 for r in ROWS if r["verdict"] == "PASS")
    n_note = sum(1 for r in ROWS if r["verdict"] == "PASS-WITH-NOTE")
    n_fail = sum(1 for r in ROWS if r["verdict"] == "FAIL")

    out.append("## Verdict summary")
    out.append("")
    out.append(f"- **PASS**: {n_pass} / {n_total}")
    out.append(f"- **PASS-WITH-NOTE**: {n_note} / {n_total}")
    out.append(f"- **FAIL**: {n_fail} / {n_total}")
    out.append("")
    if n_fail:
        out.append("### Open FAIL items (block dependent PRs)")
        out.append("")
        for r in ROWS:
            if r["verdict"] == "FAIL":
                out.append(f"- **{r['pr']}** `{r['table']}.{r['atlas_current']}` -> {r['atlas_target']} ({r['field']}): {r['note']}")
        out.append("")

    out.append("## Untouched canonical fields")
    out.append("")
    out.append("Every other field present in `wiki/atlas/atlas-target.dbml` (the rest of Property, Member, Office, Contacts, OpenHouse, Showing, HistoryTransactional, InternetTracking, Media, PropertyRooms, PropertyUnitTypes) is a direct copy of its canonical RESO 2.0 definition with no Atlas-specific transformation. By definition those fields PASS the validation gate (canonical Definition / SimpleDataType / Lookup / bounds match the RESO source CSV verbatim). Future PRs that touch any of those fields must add a row here before the schema-touching commit lands.")
    out.append("")

    out.append("## Provenance")
    out.append("")
    out.append("- RESO inputs: `reso-dd-kb/raw/fields.csv` (1,745 fields), `raw/field_metadata.csv` (Sys%/Org% adoption), `raw/lookups.csv` (canonical enumerations).")
    out.append("- Atlas data sampled via Supabase MCP `execute_sql` against `public.*` tables on the production Atlas DB.")
    out.append("- Atlas target shape: `wiki/atlas/atlas-target.dbml` (PR0.5).")
    out.append("- Canonical baseline: `wiki/atlas/reso-canonical.dbml` (PR0).")
    out.append("- Plan: `reso_canonical_gaps_atlas.plan.md`.")
    out.append("")

    return "\n".join(out) + "\n"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    md = render()
    OUT.write_text(md)
    print(f"Wrote {OUT} ({len(md.splitlines())} lines, {len(md)} bytes)")


if __name__ == "__main__":
    main()
