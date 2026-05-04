#!/usr/bin/env python3
"""
Build the pure RESO DD Canonical DBML for the 12 Resources Atlas uses.

Output: wiki/atlas/reso-canonical.dbml

This is the upstream RESO 2.0 truth, with NO Atlas-specific decisions baked in.
Every canonical RESO field for each Atlas-used Resource is rendered as a column;
Resource-typed fields are rendered as DBML `Ref:` lines (FK relationships); every
column carries its RESO Definition + SimpleDataType + LookupName + adoption metrics
as a DBML `Note:` annotation.

Atlas adapts this canonical in PR0.5 (atlas-target.dbml).
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "wiki" / "atlas" / "reso-canonical.dbml"

# The 12 RESO Resources Atlas uses today
ATLAS_RESOURCES = [
    "Property",
    "Member",
    "Office",
    "Contacts",
    "OpenHouse",
    "Showing",
    "ShowingAppointment",
    "HistoryTransactional",
    "InternetTracking",
    "Media",
    "PropertyRooms",
    "PropertyUnitTypes",
]

# RESO Resource -> snake_case Atlas table name (canonical mapping; identifier per Principle 6)
RESOURCE_TO_TABLE = {
    "Property": "property",
    "Member": "member",
    "Office": "office",
    "Contacts": "contacts",
    "OpenHouse": "open_house",
    "Showing": "showing",
    "ShowingAppointment": "showing_appointment",
    "HistoryTransactional": "history_transactional",
    "InternetTracking": "internet_tracking",
    "Media": "media",
    "PropertyRooms": "property_rooms",
    "PropertyUnitTypes": "property_unit_types",
}

# Each resource's primary key field (the *Key column we mark [pk])
RESOURCE_PK_FIELD = {
    "Property": "ListingKey",
    "Member": "MemberKey",
    "Office": "OfficeKey",
    "Contacts": "ContactKey",
    "OpenHouse": "OpenHouseKey",
    "Showing": "ShowingKey",
    "ShowingAppointment": "ShowingAppointmentKey",
    "HistoryTransactional": "HistoryTransactionalKey",
    "InternetTracking": "EventKey",
    "Media": "MediaKey",
    "PropertyRooms": "RoomKey",
    "PropertyUnitTypes": "UnitTypeKey",
}

# RESO SimpleDataType -> DBML column type
TYPE_MAP = {
    "String": "varchar",
    "Number": "numeric",
    "Boolean": "boolean",
    "Date": "date",
    "Timestamp": "timestamp",
    "Collection": "text",  # rare; collection-typed fields
}


def to_snake(pascal: str) -> str:
    """Convert PascalCase / camelCase to snake_case.

    Preserves contiguous capital runs at boundaries (e.g. ListAgentURL -> list_agent_url).
    """
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", pascal)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def load_fields() -> List[Dict[str, str]]:
    with (RAW / "fields.csv").open() as fh:
        return list(csv.DictReader(fh))


def load_metadata() -> Dict[Tuple[str, str], Dict[str, str]]:
    """Index field_metadata by (Resource, StandardName) -> row."""
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    with (RAW / "field_metadata.csv").open() as fh:
        for r in csv.DictReader(fh):
            key = (r["Resource"], r["StandardName"])
            out[key] = r
    return out


def map_dbml_type(reso_type: str, sug_max_length: str) -> str:
    """Map RESO SimpleDataType to a DBML type."""
    t = reso_type or ""
    if t.startswith("String List"):
        return "varchar"  # lookups stored as string code(s)
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


# Manual FK target table inference (Resource-typed fields -> target table name)
# Keyed on (host_resource, fk_expansion_field_name) -> target_table or None (skip)
def infer_fk_target(host: str, fk_name: str) -> Optional[str]:
    """Return the target Atlas table for a Resource-typed FK, or None to skip.

    Skip = the target is OUID or some other resource Atlas doesn't ingest.
    """
    # Self-referential (Office.MainOffice -> Office)
    if fk_name == "MainOffice" and host == "Office":
        return "office"

    # Member-pointing groups (the Resource-typed expansion)
    member_patterns = [
        "ListAgent", "BuyerAgent", "CoListAgent", "CoBuyerAgent",
        "OfficeBroker", "OfficeManager",
        "ChangedByMember", "OwnerMember",
        "ShowingAgent", "Actor",
    ]
    for p in member_patterns:
        if fk_name == p:
            return "member"

    # Office-pointing groups
    office_patterns = [
        "ListOffice", "BuyerOffice", "CoListOffice", "CoBuyerOffice", "Office",
    ]
    for p in office_patterns:
        if fk_name == p and host in ("Property", "Member"):
            return "office"

    # Team-pointing
    if fk_name in ("ListTeam", "BuyerTeam"):
        return "teams"  # Atlas may drop this; canonical RESO still defines it

    # Listing-pointing (child resources)
    if fk_name == "Listing":
        return "property"

    # OUID-bound system satellites: out of scope; skip the FK
    if fk_name in ("OriginatingSystem", "SourceSystem"):
        return None
    if fk_name.endswith("OriginatingSystem") or fk_name.endswith("SourceSystem"):
        return None

    # Polymorphic / explicitly skipped
    if fk_name in ("ChangedByMember",):  # already handled
        return "member"

    return None  # unknown -> skip (will appear as plain column)


def fmt_note(parts: List[str]) -> str:
    """Format a DBML Note string. Escape single quotes."""
    text = " | ".join(p for p in parts if p)
    text = text.replace("'", "\\'")
    # DBML supports single-quoted notes; multi-line uses triple single quotes
    return f"'{text}'"


def field_note(f: Dict[str, str], meta: Dict[str, str]) -> str:
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
    return fmt_note(parts)


def build_table(resource: str, all_fields: List[Dict[str, str]],
                meta: Dict[Tuple[str, str], Dict[str, str]]) -> Tuple[str, List[str]]:
    """Build a DBML Table block for one resource.

    Returns (table_dbml_str, list_of_ref_lines).
    """
    fields = [f for f in all_fields if f["ResourceName"] == resource]
    pk_field = RESOURCE_PK_FIELD.get(resource)
    table_name = RESOURCE_TO_TABLE[resource]

    lines: List[str] = []
    lines.append(f"// ---- {resource} (RESO 2.0 canonical) ----")
    lines.append(f"Table {table_name} {{")

    refs: List[str] = []

    # Sort: PK first, then alphabetical
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
            # FK pointer; emit a Ref: line if we can infer the target
            target = infer_fk_target(resource, f["StandardName"])
            target_key_col = f.get("TargetResourceKey") or ""  # e.g. ListAgentKey
            if target and target_key_col:
                fk_col_snake = to_snake(target_key_col)
                # Map snake target table -> RESO Resource name -> canonical PK
                target_resource = {
                    "member": "Member",
                    "office": "Office",
                    "property": "Property",
                    "contacts": "Contacts",
                    "teams": "Teams",
                }.get(target)
                target_pk_field = RESOURCE_PK_FIELD.get(target_resource or "")
                if not target_pk_field:
                    # Canonical RESO PK fallbacks for resources NOT rendered as Atlas tables
                    target_pk_field = {"Teams": "TeamKey"}.get(target_resource or "")
                target_pk_snake = to_snake(target_pk_field) if target_pk_field else f"{target}_key"

                # If target table is not in ATLAS_RESOURCES, comment the ref out
                # so the canonical DBML still documents the relationship without
                # producing a dangling reference to a non-rendered table.
                target_in_atlas = target_resource in ATLAS_RESOURCES if target_resource else False
                prefix = "Ref:" if target_in_atlas else "// Ref:"
                trailing_note = (
                    f"{resource}.{f['StandardName']} -> {target_resource or target.title()}"
                )
                if not target_in_atlas:
                    trailing_note += " (out of Atlas scope: target table not rendered)"
                refs.append(
                    f"{prefix} {table_name}.{fk_col_snake} > {target}.{target_pk_snake} "
                    f"// {trailing_note}"
                )
            continue

        col_name = to_snake(f["StandardName"])
        col_type = map_dbml_type(sdt, f.get("SugMaxLength") or "")

        attrs: List[str] = []
        if f["StandardName"] == pk_field:
            attrs.append("pk")

        meta_row = meta.get((resource, f["StandardName"]), {})
        note = field_note(f, meta_row)
        attrs.append(f"note: {note}")

        attrs_str = ", ".join(attrs)
        lines.append(f"  {col_name} {col_type} [{attrs_str}]")

    # Table-level note
    lines.append(f"  Note: 'RESO 2.0 canonical {resource} resource'")
    lines.append("}")
    lines.append("")

    return "\n".join(lines), refs


def build_dbml() -> str:
    fields = load_fields()
    meta = load_metadata()

    out_lines: List[str] = []

    # Project header
    out_lines.append("// reso-canonical.dbml")
    out_lines.append("// Pure RESO Data Dictionary 2.0 canonical schema")
    out_lines.append("// for the 12 Resources Atlas uses.")
    out_lines.append("//")
    out_lines.append("// NO Atlas-specific decisions are baked in. This file")
    out_lines.append("// represents what RESO 2.0 prescribes; Atlas adapts in PR0.5.")
    out_lines.append("//")
    out_lines.append("// Generated by reso-dd-kb/scripts/build_reso_canonical_dbml.py")
    out_lines.append("// Source: reso-dd-kb/raw/fields.csv (RESO 2.0)")
    out_lines.append("//         reso-dd-kb/raw/field_metadata.csv (Sys% / Org% adoption)")
    out_lines.append("")
    out_lines.append("Project reso_canonical {")
    out_lines.append("  database_type: 'PostgreSQL'")
    out_lines.append("  Note: '''")
    out_lines.append("    Pure RESO Data Dictionary 2.0 canonical schema for the 12 Resources Atlas uses:")
    out_lines.append("    Property, Member, Office, Contacts, OpenHouse, Showing, ShowingAppointment,")
    out_lines.append("    HistoryTransactional, InternetTracking, Media, PropertyRooms, PropertyUnitTypes.")
    out_lines.append("")
    out_lines.append("    No Atlas-specific decisions baked in. Atlas adapts this canonical in PR0.5.")
    out_lines.append("  '''")
    out_lines.append("}")
    out_lines.append("")

    all_refs: List[str] = []
    for res in ATLAS_RESOURCES:
        table_block, refs = build_table(res, fields, meta)
        out_lines.append(table_block)
        all_refs.extend(refs)

    out_lines.append("// ---- Foreign-key relationships (Resource-typed fields) ----")
    out_lines.append("")
    for r in all_refs:
        out_lines.append(r)

    return "\n".join(out_lines) + "\n"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    dbml = build_dbml()
    OUT.write_text(dbml)
    n_lines = len(dbml.splitlines())
    print(f"Wrote {OUT} ({n_lines} lines, {len(dbml)} bytes)")


if __name__ == "__main__":
    main()
