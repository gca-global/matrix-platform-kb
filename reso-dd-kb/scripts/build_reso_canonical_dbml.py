#!/usr/bin/env python3
"""Build the pure RESO Data Dictionary 2.0 canonical DBML for ALL 41 Resources.

Output: reso-dd-kb/wiki/dbml/reso-2.0-canonical.dbml

This is the upstream RESO 2.0 truth, with NO Atlas-specific decisions
baked in. Every canonical RESO field for every Resource is rendered as
a column; Resource-typed fields are rendered as DBML `Ref:` lines (FK
relationships); every column carries its RESO Definition + SimpleDataType
+ LookupName + adoption metrics as a DBML `Note:` annotation.

Lookups (enumerations) are materialised as **reference tables** named
`lookup_<snake_name>`, one per distinct LookupName in `raw/lookups.csv`.
Each ref table carries the canonical RESO LookupName columns:
    code, legacy_odata_value, definition, bedes, synonyms,
    spanish_value, french_value, status, record_id
Single-value lookup columns (`String List, Single`) get a DBML `Ref:`
to the corresponding `lookup_<name>.code`; multi-value lookup columns
(`String List, Multi`) stay `text` and document the lookup in a Note.

Inputs:
    raw/fields.csv         (parsed from RESO_Data_Dictionary_2.0.xlsx)
    raw/lookups.csv        (parsed from RESO_Data_Dictionary_2.0.xlsx)
    raw/field_metadata.csv (scraped from dd.reso.org/DD2.0)

Atlas adapts this canonical in `build_atlas_target_dbml.py`.
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "wiki" / "dbml" / "reso-2.0-canonical.dbml"

# RESO SimpleDataType -> DBML column type
TYPE_MAP = {
    "String": "varchar",
    "Number": "numeric",
    "Boolean": "boolean",
    "Date": "date",
    "Timestamp": "timestamp",
    "Collection": "text",
}

# PK overrides for resources where `<Resource>Key` does not exist or
# the canonical PK is named differently.
PK_OVERRIDES: Dict[str, str] = {
    "Property": "ListingKey",
    "Contacts": "ContactKey",
    "EntityEvent": "ResourceRecordKey",
    "InternetTracking": "EventKey",
    "OUID": "OrganizationUniqueIdKey",
    "PropertyGreenVerification": "GreenBuildingVerificationKey",
    "PropertyPowerProduction": "PowerProductionKey",
    "PropertyPowerStorage": "PowerStorageKey",
    "PropertyRooms": "RoomKey",
    "PropertyUnitTypes": "UnitTypeKey",
    "Queue": "QueueTransactionKey",
    "Rules": "RuleKey",
    "TeamMembers": "TeamMemberKey",
    "Teams": "TeamKey",
    "TransactionManagement": "TransactionKey",
}


def to_snake(name: str) -> str:
    """PascalCase / camelCase / acronym-runs -> snake_case."""
    if not name:
        return ""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def load_fields() -> List[Dict[str, str]]:
    with (RAW / "fields.csv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_lookup_names() -> List[str]:
    seen: List[str] = []
    with (RAW / "lookups.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            n = (r.get("LookupName") or "").strip()
            if n and n not in seen:
                seen.append(n)
    return sorted(seen)


def load_metadata() -> Dict[Tuple[str, str], Dict[str, str]]:
    out: Dict[Tuple[str, str], Dict[str, str]] = {}
    p = RAW / "field_metadata.csv"
    if not p.exists():
        return out
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[(r["Resource"], r["Field"])] = r
    return out


def map_dbml_type(reso_type: str, sug_max_length: str) -> str:
    t = (reso_type or "").strip()
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
    text = text.replace("\\", "\\\\").replace("'", "\\'")
    return f"'{text}'"


def derive_pk(resource: str, fields_for_res: List[Dict[str, str]]) -> Optional[str]:
    if resource in PK_OVERRIDES:
        return PK_OVERRIDES[resource]
    cand = f"{resource}Key"
    if any(f["StandardName"] == cand for f in fields_for_res):
        return cand
    for f in fields_for_res:
        if (f.get("Groups", "").lower() in ("identifier", "identifiers")
                and f["StandardName"].endswith("Key")):
            return f["StandardName"]
    return None


def field_note(f: Dict[str, str], meta: Dict[str, str]) -> str:
    parts = [f["StandardName"]]
    defn = (f.get("Definition") or "").strip().replace("\n", " ")
    if defn:
        parts.append(defn[:160])
    sdt = f.get("SimpleDataType") or ""
    if sdt:
        parts.append(f"type={sdt}")
    lookup = f.get("LookupName") or ""
    if lookup:
        is_multi = (f.get("SimpleDataType") or "").strip() == "String List, Multi"
        parts.append(f"lookup={lookup}" + (" (multi)" if is_multi else ""))
    for label, key in [("max_len", "SugMaxLength"), ("max_prec", "SugMaxPrecision")]:
        v = (f.get(key) or "").strip()
        if v:
            parts.append(f"{label}={v}")
    org_pct = (meta.get("OrgPct") or "").strip()
    org_n = (meta.get("OrgAdopted") or "").strip()
    org_total = (meta.get("OrgTotal") or "").strip()
    if org_pct:
        parts.append(f"adoption org={org_pct}% ({org_n}/{org_total})")
    return fmt_note(parts)


def build_table(
    resource: str,
    table_name: str,
    fields_for_res: List[Dict[str, str]],
    pk_field: Optional[str],
    meta: Dict[Tuple[str, str], Dict[str, str]],
    valid_resources: Set[str],
    lookup_names: Set[str],
    resource_to_table: Dict[str, str],
    resource_pks: Dict[str, Optional[str]],
) -> Tuple[str, List[str]]:
    """Render one Table block + collect Refs (FK lines)."""
    lines: List[str] = []
    lines.append(f"// ---- {resource} (RESO 2.0 canonical) ----")
    lines.append(f"Table {table_name} {{")

    refs: List[str] = []
    seen_cols: Set[str] = set()

    fields_sorted = sorted(
        fields_for_res,
        key=lambda f: (0 if f["StandardName"] == pk_field else 1, f["StandardName"]),
    )

    for f in fields_sorted:
        sdt = (f.get("SimpleDataType") or "").strip()

        # Resource-typed fields render as FK refs only; the scalar key column
        # they point to is materialised by another row in fields.csv (the
        # `<TargetResourceKey>` field).
        if sdt == "Resource":
            target_resource = (f.get("SourceResource") or "").strip()
            target_key_col = (f.get("TargetResourceKey") or "").strip()
            if not target_resource or not target_key_col:
                continue
            host_col = to_snake(target_key_col)
            target_table = resource_to_table.get(target_resource)
            target_pk = resource_pks.get(target_resource)
            if not target_table or not target_pk:
                continue
            target_pk_snake = to_snake(target_pk)
            refs.append(
                f"Ref: {table_name}.{host_col} > {target_table}.{target_pk_snake} "
                f"// {resource}.{f['StandardName']} -> {target_resource}"
            )
            continue

        col_name = to_snake(f["StandardName"])
        if not col_name or col_name in seen_cols:
            continue
        seen_cols.add(col_name)

        col_type = map_dbml_type(sdt, f.get("SugMaxLength") or "")

        attrs: List[str] = []
        if pk_field and f["StandardName"] == pk_field:
            attrs.append("pk")

        meta_row = meta.get((resource, f["StandardName"]), {})
        attrs.append(f"note: {field_note(f, meta_row)}")
        lines.append(f"  {col_name} {col_type} [{', '.join(attrs)}]")

        # Lookup FK ref (single-value lookups only; multi-value stays as text).
        lookup = (f.get("LookupName") or "").strip()
        if lookup and lookup in lookup_names and sdt == "String List, Single":
            refs.append(
                f"Ref: {table_name}.{col_name} > lookup_{to_snake(lookup)}.code "
                f"// {resource}.{f['StandardName']} -> {lookup}"
            )

    lines.append(f"  Note: 'RESO 2.0 canonical {resource} resource'")
    lines.append("}")
    lines.append("")
    return "\n".join(lines), refs


def build_lookup_table(name: str) -> str:
    table = f"lookup_{to_snake(name)}"
    lines = [
        f"// ---- {name} (RESO 2.0 lookup) ----",
        f"Table {table} {{",
        "  code varchar [pk, note: 'StandardLookupValue']",
        "  legacy_odata_value varchar [note: 'LegacyODataValue (PascalCase code used by older OData APIs)']",
        "  definition text",
        "  bedes text",
        "  synonyms text",
        "  spanish_value varchar",
        "  french_value varchar",
        "  status varchar [note: 'Active | Revised | Retired']",
        "  record_id varchar [note: 'RESO LookupId stable identifier']",
        f"  Note: 'RESO 2.0 lookup values for {name} (see raw/lookups.csv for the value list)'",
        "}",
        "",
    ]
    return "\n".join(lines)


def build_dbml() -> str:
    fields = load_fields()
    metadata = load_metadata()
    lookup_names = load_lookup_names()

    by_res: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for f in fields:
        by_res[f["ResourceName"]].append(f)

    resources = sorted(by_res.keys())
    resource_to_table = {r: to_snake(r) for r in resources}
    resource_pks: Dict[str, Optional[str]] = {r: derive_pk(r, by_res[r]) for r in resources}

    out: List[str] = []
    out.append("// reso-2.0-canonical.dbml")
    out.append("// Pure RESO Data Dictionary 2.0 canonical schema")
    out.append(f"// {len(resources)} Resources, {len(fields)} Fields, {len(lookup_names)} Lookups")
    out.append("//")
    out.append("// NO Atlas-specific decisions baked in. This file represents what")
    out.append("// RESO 2.0 prescribes; Atlas adapts in build_atlas_target_dbml.py.")
    out.append("//")
    out.append("// Generated by reso-dd-kb/scripts/build_reso_canonical_dbml.py")
    out.append("// Source: dd.reso.org/DD2.0 + raw/fields.csv + raw/lookups.csv + raw/field_metadata.csv")
    out.append("")
    out.append("Project reso_canonical_dd_2_0 {")
    out.append("  database_type: 'PostgreSQL'")
    out.append("  Note: '''")
    out.append(f"    Pure RESO Data Dictionary 2.0 canonical schema covering all {len(resources)} Resources,")
    out.append(f"    {len(fields)} Fields, and {len(lookup_names)} Lookups (rendered as lookup_<name> ref tables).")
    out.append("")
    out.append("    Single-value lookup columns reference the corresponding lookup_<name>.code via DBML")
    out.append("    Refs; multi-value lookup columns stay text and document the lookup in a Note.")
    out.append("")
    out.append("    No Atlas-specific decisions baked in. Atlas adapts this canonical in")
    out.append("    build_atlas_target_dbml.py (wiki/atlas/atlas-target.dbml).")
    out.append("  '''")
    out.append("}")
    out.append("")

    out.append("// ============================================================")
    out.append(f"// Resources ({len(resources)})")
    out.append("// ============================================================")
    out.append("")

    all_refs: List[str] = []
    lookup_set = set(lookup_names)
    for res in resources:
        block, refs = build_table(
            res,
            resource_to_table[res],
            by_res[res],
            resource_pks[res],
            metadata,
            valid_resources=set(resources),
            lookup_names=lookup_set,
            resource_to_table=resource_to_table,
            resource_pks=resource_pks,
        )
        out.append(block)
        all_refs.extend(refs)

    out.append("// ============================================================")
    out.append(f"// Lookup reference tables ({len(lookup_names)})")
    out.append("// ============================================================")
    out.append("")
    for n in lookup_names:
        out.append(build_lookup_table(n))

    out.append("// ============================================================")
    out.append(f"// Foreign-key relationships ({len(all_refs)})")
    out.append("// ============================================================")
    out.append("")
    for r in all_refs:
        out.append(r)

    return "\n".join(out) + "\n"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    dbml = build_dbml()
    OUT.write_text(dbml, encoding="utf-8")
    n_lines = len(dbml.splitlines())
    print(f"Wrote {OUT.relative_to(ROOT)} ({n_lines} lines, {len(dbml)} bytes)")


if __name__ == "__main__":
    main()
