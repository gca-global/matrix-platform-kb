#!/usr/bin/env python3
"""
Build the Atlas Target DBML — RESO canonical with all Atlas-specific
decisions from reso_canonical_gaps_atlas.plan.md applied on top.

Output: wiki/atlas/atlas-target.dbml

This is the AUTHORITATIVE BLUEPRINT every subsequent migration moves the
live Atlas DB toward. Reads the same RESO inputs as PR0 (raw/fields.csv,
raw/field_metadata.csv) and applies:

  PR1   - canonical column renames (currency_code, virtual_tour_url_unbranded,
          lot_size_area + lot_size_units, livestream_open_house_url,
          office_national_association_id) -> already canonical names; Atlas
          rename is a no-op here (target carries the canonical name only).
  PR1.5 - drop Teams resource: Teams isn't in our 12 anyway.
  PR1.6 - drop PropertyPowerProduction: not in our 12 either.
  PR2   - drop low-signal Atlas-custom (lead_source, district,
          member_photo_url, original_entry_timestamp on child tables):
          these are Atlas-custom (not canonical), so target excludes them.
  PR3   - website_listing_date -> on_market_date + on_market_timestamp:
          canonical names already in target.
  PR3.5 - drop key_holder_details + backfill list_agent_key FK: target
          carries list_agent_key with FK constraint; key_holder_details
          excluded.
  PR3.6 - drop created_by_member_key + modified_by_member_key from
          properties; backfill HistoryTransactional. Target excludes those
          columns from properties; HT keeps changed_by_member_key FK.
  PR4   - add CountyOrParish: already canonical RESO Property field, so
          present in target.
  PR5   - history_transactional `*_id` -> `*ID` (UI labels, DB stays snake).
  PR6   - property_media -> media reshape: target carries canonical media
          table (already canonical).
  PR7   - Showing vs ShowingAppointment: PICK Showing (DD 2.0). Target
          drops showing_appointment table.
  PR8   - internet_tracking_events -> internet_tracking: canonical name
          already in target.
  PR9   - top-10 missing high-adoption Property fields: all canonical RESO
          fields, already in target. The 3 ListAgent satellites
          (list_agent_first_name/_last_name/_email) carry a denormalization
          Note + [denorm: 'members via list_agent_key'].
  PR10  - atlas_custom extensions: target adds x_sm_is_sir_branded +
          x_sm_sir_office_id on properties; x_sm_sir_designation on
          members; open_houses denorm list_agent_key + list_office_key.
  PR11  - FK constraints: every Atlas-internal *_key gets the canonical
          delete action annotation in Refs.
  P9    - OUID-bound system satellites (originating_system_*, source_system_*)
          stay flat-scalar with a Note: 'OUID-bound; flat-scalar pending
          OUID resource'.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "wiki" / "atlas" / "atlas-target.dbml"

# Atlas-resident RESO Resources after PR1.5 / PR1.6 / PR7 decisions.
# (Same 12 as PR0 minus ShowingAppointment, which PR7 drops in favor of Showing.)
ATLAS_RESOURCES = [
    "Property",
    "Member",
    "Office",
    "Contacts",
    "OpenHouse",
    "Showing",  # PR7 picks Showing (DD 2.0) over ShowingAppointment (SHOW17)
    "HistoryTransactional",
    "InternetTracking",
    "Media",
    "PropertyRooms",
    "PropertyUnitTypes",
]

RESOURCE_TO_TABLE = {
    "Property": "property",
    "Member": "member",
    "Office": "office",
    "Contacts": "contacts",
    "OpenHouse": "open_house",
    "Showing": "showing",
    "HistoryTransactional": "history_transactional",
    "InternetTracking": "internet_tracking",
    "Media": "media",
    "PropertyRooms": "property_rooms",
    "PropertyUnitTypes": "property_unit_types",
}

RESOURCE_PK_FIELD = {
    "Property": "ListingKey",
    "Member": "MemberKey",
    "Office": "OfficeKey",
    "Contacts": "ContactKey",
    "OpenHouse": "OpenHouseKey",
    "Showing": "ShowingKey",
    "HistoryTransactional": "HistoryTransactionalKey",
    "InternetTracking": "EventKey",
    "Media": "MediaKey",
    "PropertyRooms": "RoomKey",
    "PropertyUnitTypes": "UnitTypeKey",
}

TYPE_MAP = {
    "String": "varchar",
    "Number": "numeric",
    "Boolean": "boolean",
    "Date": "date",
    "Timestamp": "timestamp",
    "Collection": "text",
}

# ---------------------------------------------------------------------------
# Atlas-specific overlays (all derived from reso_canonical_gaps_atlas.plan.md)
# ---------------------------------------------------------------------------

# Atlas-custom (non-RESO) extensions to add per resource (PR10).
ATLAS_CUSTOM_FIELDS: Dict[str, List[Dict[str, str]]] = {
    "Property": [
        {
            "name": "x_sm_is_sir_branded",
            "type": "boolean",
            "note": "atlas_custom — Sotheby's branded listing flag (PR10)",
        },
        {
            "name": "x_sm_sir_office_id",
            "type": "varchar(64)",
            "note": "atlas_custom — Sotheby's office identifier (PR10)",
        },
        # Atlas-only computed lifecycle chip (already documented as atlas_custom)
        {
            "name": "lifecycle_state",
            "type": "varchar(32)",
            "note": "atlas_custom — computed lifecycle chip (active/pending/sold/withdrawn); already in reso_field_descriptions source='atlas_custom'",
        },
        {
            "name": "lifecycle_state_changed_at",
            "type": "timestamptz",
            "note": "atlas_custom — last change of lifecycle_state (Postgres-set on UPDATE)",
        },
    ],
    "Member": [
        {
            "name": "x_sm_sir_designation",
            "type": "varchar(64)",
            "note": "atlas_custom — Sotheby's designation (PR10)",
        },
    ],
    "OpenHouse": [
        # PR10 + scorecard: Atlas denormalizes these from parent Property
        {
            "name": "list_agent_key",
            "type": "varchar(255)",
            "note": "atlas_custom — denormalized from parent property.list_agent_key for fast queries (PR10)",
        },
        {
            "name": "list_office_key",
            "type": "varchar(255)",
            "note": "atlas_custom — denormalized from parent property.list_office_key for fast queries (PR10)",
        },
    ],
}

# Property fields denormalized from joined satellites (PR9). The columns
# themselves ALREADY exist in the canonical Property (they are canonical
# RESO names) — we just decorate the target Note to make the
# denormalization contract explicit.
DENORMALIZED_FIELD_NOTES: Dict[Tuple[str, str], str] = {
    ("Property", "ListAgentFirstName"):
        "DENORMALIZED from member via list_agent_key (PR9; trigger-maintained)",
    ("Property", "ListAgentLastName"):
        "DENORMALIZED from member via list_agent_key (PR9; trigger-maintained)",
    ("Property", "ListAgentEmail"):
        "DENORMALIZED from member via list_agent_key (PR9; trigger-maintained)",
    ("Property", "PhotosCount"):
        "DENORMALIZED count of media rows where resource_record_key=listing_key (PR9; trigger-maintained on media insert/delete)",
}

# OUID-bound system satellites (PR0.5 task (i)): mark these flat-scalar
# columns with a Note telling readers they're OUID-bound and stay flat
# pending the OUID resource.
OUID_BOUND_FIELD_PATTERNS = [
    re.compile(r"^originating_system($|_)"),
    re.compile(r"^source_system($|_)"),
    re.compile(r"^.*_originating_system($|_)"),
    re.compile(r"^.*_source_system($|_)"),
]
OUID_BOUND_NOTE = "OUID-bound; flat-scalar pending OUID resource ingestion (out of scope)"

# FK delete actions (PR11). Map (host_table, fk_column) -> 'set null' | 'restrict' | 'cascade'.
# Default for satellite/audit FKs is 'set null'; default for hard parent-child is 'restrict'.
FK_DELETE_ACTION: Dict[Tuple[str, str], str] = {
    # Satellite / audit FKs (soft references) — set null
    ("property", "list_agent_key"): "set null",
    ("property", "list_office_key"): "set null",
    ("property", "buyer_agent_key"): "set null",
    ("property", "buyer_office_key"): "set null",
    ("property", "co_list_agent_key"): "set null",
    ("property", "co_list_office_key"): "set null",
    ("property", "co_buyer_agent_key"): "set null",
    ("property", "co_buyer_office_key"): "set null",
    ("member", "office_key"): "set null",
    ("office", "main_office_key"): "set null",
    ("office", "office_broker_key"): "set null",
    ("office", "office_manager_key"): "set null",
    ("contacts", "owner_member_key"): "set null",
    ("open_house", "showing_agent_key"): "set null",
    ("showing", "showing_agent_key"): "set null",
    ("history_transactional", "changed_by_member_key"): "set null",

    # Hard parent-child FKs (child rows orphaned without parent) — restrict
    ("open_house", "listing_key"): "restrict",
    ("showing", "listing_key"): "restrict",
    ("property_rooms", "listing_key"): "restrict",
    ("property_unit_types", "listing_key"): "restrict",
}

# ---------------------------------------------------------------------------
# Helpers (mirror PR0 builder)
# ---------------------------------------------------------------------------

def to_snake(pascal: str) -> str:
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", pascal)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def is_ouid_bound(snake_col: str) -> bool:
    return any(p.search(snake_col) for p in OUID_BOUND_FIELD_PATTERNS)


def load_fields() -> List[Dict[str, str]]:
    with (RAW / "fields.csv").open() as fh:
        return list(csv.DictReader(fh))


def load_metadata() -> Dict[Tuple[str, str], Dict[str, str]]:
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    with (RAW / "field_metadata.csv").open() as fh:
        for r in csv.DictReader(fh):
            out[(r["Resource"], r["StandardName"])] = r
    return out


def map_dbml_type(reso_type: str, sug_max_length: str) -> str:
    t = reso_type or ""
    if t.startswith("String List"):
        return "varchar"
    if t == "String":
        if sug_max_length:
            try:
                n = int(float(sug_max_length))
                return f"varchar({n})"
            except ValueError:
                pass
        return "varchar"
    if t == "Number":
        return "numeric"
    return TYPE_MAP.get(t, "text")


def fmt_note(parts: List[str]) -> str:
    text = " | ".join(p for p in parts if p)
    text = text.replace("'", "\\'")
    return f"'{text}'"


def field_note(f: Dict[str, str], meta: Dict[str, str], extras: List[str]) -> str:
    parts = [f["StandardName"]]
    defn = (f.get("Definition") or "").strip()
    if defn:
        parts.append(defn[:120].replace("\n", " "))
    sdt = f.get("SimpleDataType") or ""
    if sdt:
        parts.append(f"type={sdt}")
    lookup = f.get("LookupName") or ""
    if lookup:
        parts.append(f"lookup={lookup}")
    sml = f.get("SugMaxLength") or ""
    if sml:
        parts.append(f"max_len={sml}")
    smp = f.get("SugMaxPrecision") or ""
    if smp:
        parts.append(f"max_prec={smp}")
    sys_pct = (meta.get("SysPct") or "").strip()
    org_pct = (meta.get("OrgPct") or "").strip()
    if sys_pct or org_pct:
        parts.append(f"adoption sys={sys_pct or '-'}% org={org_pct or '-'}%")
    parts.extend(extras)
    return fmt_note(parts)


# ---------------------------------------------------------------------------
# FK target inference (Resource-typed fields)
# ---------------------------------------------------------------------------

def infer_fk_target(host: str, fk_name: str) -> Optional[str]:
    if fk_name == "MainOffice" and host == "Office":
        return "office"
    member_patterns = [
        "ListAgent", "BuyerAgent", "CoListAgent", "CoBuyerAgent",
        "OfficeBroker", "OfficeManager",
        "ChangedByMember", "OwnerMember",
        "ShowingAgent", "Actor",
    ]
    if fk_name in member_patterns:
        return "member"
    office_patterns = [
        "ListOffice", "BuyerOffice", "CoListOffice", "CoBuyerOffice", "Office",
    ]
    if fk_name in office_patterns and host in ("Property", "Member"):
        return "office"
    if fk_name in ("ListTeam", "BuyerTeam"):
        return None  # PR1.5 dropped Teams entirely
    if fk_name == "Listing":
        return "property"
    if fk_name in ("OriginatingSystem", "SourceSystem"):
        return None
    if fk_name.endswith("OriginatingSystem") or fk_name.endswith("SourceSystem"):
        return None
    return None


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_table(resource: str, all_fields: List[Dict[str, str]],
                meta: Dict[Tuple[str, str], Dict[str, str]]) -> Tuple[str, List[str]]:
    fields = [f for f in all_fields if f["ResourceName"] == resource]
    pk_field = RESOURCE_PK_FIELD.get(resource)
    table_name = RESOURCE_TO_TABLE[resource]

    lines: List[str] = []
    lines.append(f"// ---- {resource} (Atlas Target — RESO 2.0 + Atlas adaptations) ----")
    lines.append(f"Table {table_name} {{")

    refs: List[str] = []

    fields_sorted = sorted(
        fields,
        key=lambda f: (
            0 if f["StandardName"] == pk_field else 1,
            f["StandardName"],
        ),
    )

    for f in fields_sorted:
        sdt = f.get("SimpleDataType") or ""
        if sdt == "Resource":
            target = infer_fk_target(resource, f["StandardName"])
            target_key_col = f.get("TargetResourceKey") or ""
            if target and target_key_col:
                fk_col_snake = to_snake(target_key_col)
                target_resource = {
                    "member": "Member",
                    "office": "Office",
                    "property": "Property",
                    "contacts": "Contacts",
                }.get(target)
                target_pk_field = RESOURCE_PK_FIELD.get(target_resource or "")
                target_pk_snake = to_snake(target_pk_field) if target_pk_field else f"{target}_key"

                target_in_atlas = target_resource in ATLAS_RESOURCES
                if target_in_atlas:
                    delete_action = FK_DELETE_ACTION.get((table_name, fk_col_snake), "set null")
                    refs.append(
                        f"Ref: {table_name}.{fk_col_snake} > {target}.{target_pk_snake} "
                        f"[delete: {delete_action}] // {resource}.{f['StandardName']} -> {target_resource}"
                    )
                else:
                    refs.append(
                        f"// Ref: {table_name}.{fk_col_snake} > {target}.{target_pk_snake} "
                        f"// {resource}.{f['StandardName']} -> {target_resource or target.title()} (out of Atlas scope)"
                    )
            continue

        col_name = to_snake(f["StandardName"])
        col_type = map_dbml_type(sdt, f.get("SugMaxLength") or "")

        attrs: List[str] = []
        if f["StandardName"] == pk_field:
            attrs.append("pk")

        meta_row = meta.get((resource, f["StandardName"]), {})

        # Atlas-specific extras for this column's note
        extras: List[str] = []
        denorm = DENORMALIZED_FIELD_NOTES.get((resource, f["StandardName"]))
        if denorm:
            extras.append(denorm)
        if is_ouid_bound(col_name):
            extras.append(OUID_BOUND_NOTE)

        note = field_note(f, meta_row, extras)
        attrs.append(f"note: {note}")

        lines.append(f"  {col_name} {col_type} [{', '.join(attrs)}]")

    # Atlas-custom additions per resource (PR10)
    custom = ATLAS_CUSTOM_FIELDS.get(resource, [])
    if custom:
        lines.append(f"  // ---- Atlas-custom extensions (source='atlas_custom') ----")
        for c in custom:
            note_str = fmt_note([c["note"]])
            lines.append(f"  {c['name']} {c['type']} [note: {note_str}]")

    lines.append(f"  Note: 'Atlas Target — {resource} (RESO 2.0 canonical + Atlas adaptations per reso_canonical_gaps_atlas.plan.md)'")
    lines.append("}")
    lines.append("")

    return "\n".join(lines), refs


def build_dbml() -> str:
    fields = load_fields()
    meta = load_metadata()

    out: List[str] = []
    out.append("// atlas-target.dbml")
    out.append("// Atlas TARGET schema — RESO 2.0 canonical with all Atlas")
    out.append("// adaptations from reso_canonical_gaps_atlas.plan.md applied.")
    out.append("//")
    out.append("// THIS IS THE AUTHORITATIVE BLUEPRINT every subsequent migration")
    out.append("// (PRs 1 - 12) moves the live Atlas DB toward.")
    out.append("//")
    out.append("// Generated by reso-dd-kb/scripts/build_atlas_target_dbml.py")
    out.append("// Source canonical: reso-dd-kb/wiki/atlas/reso-canonical.dbml (PR0)")
    out.append("// Source data:      reso-dd-kb/raw/fields.csv + raw/field_metadata.csv")
    out.append("//")
    out.append("// Adaptations applied:")
    out.append("//   PR1.5 dropped Teams resource          (not rendered)")
    out.append("//   PR1.6 dropped PropertyPowerProduction (not rendered)")
    out.append("//   PR7   picked Showing (DD 2.0)         (ShowingAppointment not rendered)")
    out.append("//   PR9   denormalized 3 ListAgent satellites + PhotosCount on property")
    out.append("//   PR10  added 3 atlas_custom Sotheby's branding columns")
    out.append("//   PR10  added 2 denormalized columns to open_house (list_agent_key/list_office_key)")
    out.append("//   PR11  every Atlas-internal *_key has a [delete: set null|restrict] FK ref")
    out.append("//   OUID  originating_system_*/source_system_* stay flat-scalar (out of scope)")
    out.append("//")
    out.append("// Atlas-custom columns excluded from PROPERTY (dropped per plan):")
    out.append("//   key_holder_details          (PR3.5 - resolved into list_agent_key FK)")
    out.append("//   created_by_member_key       (PR3.6 - moved to history_transactional)")
    out.append("//   modified_by_member_key      (PR3.6 - dropped without backfill; sync ts)")
    out.append("//   lead_source                 (PR2   - 99.9% 'direct'; no signal)")
    out.append("//   district                    (PR2   - 1/15884 populated)")
    out.append("//   currency                    (PR1   - renamed to currency_code = canonical)")
    out.append("//   virtual_tour_url            (PR1   - renamed to virtual_tour_url_unbranded)")
    out.append("//   land_area_sqm               (PR1   - renamed to lot_size_area + units)")
    out.append("//   website_listing_date        (PR3   - renamed to on_market_date + on_market_timestamp)")
    out.append("//")
    out.append("// Atlas-custom columns excluded from MEMBER:")
    out.append("//   member_photo_url            (PR2   - 0/129 populated; canonical via Media)")
    out.append("//")
    out.append("// Atlas-custom columns excluded from PROPERTY_ROOMS / PROPERTY_UNIT_TYPES:")
    out.append("//   original_entry_timestamp    (PR2   - not on RESO child resources)")
    out.append("")
    out.append("Project atlas_target {")
    out.append("  database_type: 'PostgreSQL'")
    out.append("  Note: '''")
    out.append("    Atlas Target schema — RESO 2.0 canonical with Atlas adaptations.")
    out.append("    Authoritative blueprint for PRs 1-12 in reso_canonical_gaps_atlas.plan.md.")
    out.append("  '''")
    out.append("}")
    out.append("")

    all_refs: List[str] = []
    for res in ATLAS_RESOURCES:
        block, refs = build_table(res, fields, meta)
        out.append(block)
        all_refs.extend(refs)

    out.append("// ---- Foreign-key constraints (PR11; every Atlas-internal *_key) ----")
    out.append("")
    for r in all_refs:
        out.append(r)

    return "\n".join(out) + "\n"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    dbml = build_dbml()
    OUT.write_text(dbml)
    n_lines = len(dbml.splitlines())
    print(f"Wrote {OUT} ({n_lines} lines, {len(dbml)} bytes)")


if __name__ == "__main__":
    main()
