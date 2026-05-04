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

# RESO SimpleDataType -> DBML column type. `Resource` and `Collection` are
# intentionally absent: Resource fields render as forward FK Refs (-> 2NF),
# Collection fields render as inverse 1:N comments (the FK lives on the
# child resource, not on the host).
TYPE_MAP = {
    "String": "varchar",
    "Number": "numeric",
    "Boolean": "boolean",
    "Date": "date",
    "Timestamp": "timestamp",
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


def _fk_prefix(target_key_col: str) -> str:
    """Strip trailing Key/ID/Id from a TargetResourceKey to get the FK prefix
    that satellite columns share (e.g. ListAgentKey -> ListAgent,
    OriginatingSystemID -> OriginatingSystem)."""
    for sfx in ("Key", "ID", "Id"):
        if target_key_col.endswith(sfx) and len(target_key_col) > len(sfx):
            return target_key_col[: -len(sfx)]
    return ""


def compute_satellites(
    by_res: Dict[str, List[Dict[str, str]]],
    resource_pks: Dict[str, Optional[str]],
) -> Tuple[Dict[str, Set[str]], List[Tuple[str, str, str, str]]]:
    """Identify satellite fields per host for 2NF normalization.

    A *satellite* is a non-Resource scalar field on host H whose name shares
    the prefix of a Resource-typed FK on H (e.g. Property.ListAgentEmail
    shares prefix `ListAgent` with the FK Property.ListAgent -> Member, so
    its value is functionally dependent on Property.ListAgentKey rather than
    Property.ListingKey -> 2NF/3NF violation).

    Excluded from the satellite set:
      - the host's own primary key
      - any FK column on the host (TargetResourceKey of another Resource-typed
        field)
      - Resource-typed fields themselves (already rendered as Refs only)

    Two flavours of satellite are dropped uniformly:
      1. True denormalizations - the column also exists on the target
         (e.g. Property.ListAgentEmail mirrors Member.MemberEmail).
      2. Auxiliary identifiers / relationship attributes - the column does
         not exist on the target and would belong in a junction/link table
         in a fully normalized model (e.g. Property.OriginatingSystemKey =
         "this listing's identifier in the originating system").

    Both flavours violate 2NF on the host; both are removed from the
    canonical model. Operational/denormalized stores (Atlas) may re-add a
    chosen subset for query performance via build_atlas_target_dbml.py.

    Returns:
        (satellites_by_host, report_rows)
        satellites_by_host: {host_resource: {satellite_field_name, ...}}
        report_rows: [(host, satellite_field, target_resource, fk_field, target_key_col), ...]
    """
    satellites: Dict[str, Set[str]] = defaultdict(set)
    report: List[Tuple[str, str, str, str, str]] = []
    for res in sorted(by_res):
        pk = resource_pks.get(res)
        rt_fields = [
            f for f in by_res[res]
            if (f.get("SimpleDataType") or "").strip() == "Resource"
        ]
        fk_cols: Set[str] = {
            (f.get("TargetResourceKey") or "").strip()
            for f in rt_fields
            if (f.get("TargetResourceKey") or "").strip()
        }
        excluded: Set[str] = set(fk_cols) | ({pk} if pk else set())
        for f in rt_fields:
            target = (f.get("SourceResource") or "").strip()
            tkey = (f.get("TargetResourceKey") or "").strip()
            fk_field = f["StandardName"]
            if not target or not tkey:
                continue
            pfx = _fk_prefix(tkey)
            if not pfx:
                continue
            for g in by_res[res]:
                n = g["StandardName"]
                if n in excluded:
                    continue
                if (g.get("SimpleDataType") or "").strip() == "Resource":
                    continue
                if not n.startswith(pfx):
                    continue
                rest = n[len(pfx):]
                # Require a word boundary after the prefix so e.g. prefix
                # "Contact" doesn't match "ContactListingsKey" (the host PK
                # is already excluded, but this guards future PKs too).
                if rest and not rest[0].isupper():
                    continue
                if n in satellites[res]:
                    continue
                satellites[res].add(n)
                report.append((res, n, target, fk_field, tkey))
    return satellites, report


# Definition-prose patterns RESO uses to call out implicit FKs.
_PROSE_FK_RELATING = re.compile(
    r"(?:foreign key (?:relating|related) to|relates to|relating to|references?)"
    r"\s+(?:the\s+)?(\w+)\s+[Rr]esource",
    re.IGNORECASE,
)
_PROSE_FK_RESOURCES = re.compile(
    r"(\w+)\s+[Rr]esource['\u2019]s\s+(\w+)",
    re.IGNORECASE,
)


def _name_shape_target(field_name: str, resource_names: Set[str]) -> Optional[str]:
    """`<Word>Key` -> Resource named `<Word>` or its simple plural (Contacts,
    Teams, Rules, etc.). Returns the canonical Resource name or None."""
    if not field_name.endswith("Key") or len(field_name) <= 3:
        return None
    prefix = field_name[:-3]
    if prefix in resource_names:
        return prefix
    for r in resource_names:
        if r.endswith("s") and r[:-1] == prefix:
            return r
    return None


def compute_extra_fks(
    by_res: Dict[str, List[Dict[str, str]]],
    resource_pks: Dict[str, Optional[str]],
    satellites_by_host: Dict[str, Set[str]],
) -> List[Tuple[str, str, str, str, str]]:
    """Detect FK columns that are NOT already a TargetResourceKey of an
    existing Resource-typed sibling on the same host.

    Three signals, in priority order:
      1. `prose-foreign-key`  - Definition contains "foreign key relating
         to the <X> Resource".
      2. `prose-resources`    - Definition contains "<X> Resource's <Y>".
      3. `name-shape`         - field name `<Word>Key` where `<Word>`
         names a Resource (or its singular form for plural Resources).

    Filters:
      - Skip the host's own PK (it's a key, not a FK).
      - Skip fields already covered (they're a TargetResourceKey of a
        Resource-typed sibling - the existing FK pass handles them).
      - Skip fields dropped as satellites (no point Ref-ing a column we
        won't render).

    Returns: [(host, field_name, target_resource, target_pk, signal), ...]
    """
    resource_names = set(by_res)
    covered: Set[Tuple[str, str]] = set()
    for res, fs in by_res.items():
        for f in fs:
            if (f.get("SimpleDataType") or "").strip() == "Resource":
                tkey = (f.get("TargetResourceKey") or "").strip()
                if tkey:
                    covered.add((res, tkey))

    priority = {"prose-foreign-key": 0, "prose-resources": 1, "name-shape": 2}
    best: Dict[Tuple[str, str], Tuple[str, str, str, str, str]] = {}

    for res in sorted(by_res):
        host_satellites = satellites_by_host.get(res, set())
        for f in by_res[res]:
            sdt = (f.get("SimpleDataType") or "").strip()
            if sdt in ("Resource", "Collection"):
                continue
            name = f["StandardName"]
            if not name.endswith(("Key", "ID", "Id")):
                continue
            if (res, name) in covered:
                continue
            if resource_pks.get(res) == name:
                continue
            if name in host_satellites:
                continue

            defn = (f.get("Definition") or "").strip()
            target: Optional[str] = None
            signal: Optional[str] = None

            m = _PROSE_FK_RELATING.search(defn)
            if m and m.group(1) in resource_names:
                target, signal = m.group(1), "prose-foreign-key"
            if not target:
                m = _PROSE_FK_RESOURCES.search(defn)
                if m and m.group(1) in resource_names:
                    target, signal = m.group(1), "prose-resources"
            if not target:
                cand = _name_shape_target(name, resource_names)
                if cand:
                    target, signal = cand, "name-shape"

            if not target:
                continue
            tpk = resource_pks.get(target)
            if not tpk:
                continue

            row = (res, name, target, tpk, signal)
            key = (res, name)
            if key not in best or priority[signal] < priority[best[key][-1]]:
                best[key] = row

    return sorted(best.values())


def collection_inverse_targets(
    fields_for_res: List[Dict[str, str]],
    resource_names: Set[str],
) -> List[Tuple[str, str]]:
    """For each Collection-typed field on the host, resolve the child
    Resource it inverse-references. Returns [(field_name, child_resource), ...]
    skipping any that cannot be resolved."""
    out: List[Tuple[str, str]] = []
    for f in fields_for_res:
        if (f.get("SimpleDataType") or "").strip() != "Collection":
            continue
        target = (f.get("SourceResource") or "").strip()
        if not target:
            # Fall back to StandardName matching a known Resource
            cand = f["StandardName"]
            if cand in resource_names:
                target = cand
        if target and target in resource_names:
            out.append((f["StandardName"], target))
    return out


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
    satellite_fields: Set[str],
    inverse_collections: List[Tuple[str, str]],
) -> Tuple[str, List[str]]:
    """Render one Table block + collect Refs (FK lines)."""
    lines: List[str] = []
    lines.append(f"// ---- {resource} (RESO 2.0 canonical) ----")
    if satellite_fields:
        lines.append(
            f"// 2NF: {len(satellite_fields)} satellite field(s) dropped "
            f"(reachable via FK joins). See header for full list."
        )
    if inverse_collections:
        lines.append(
            f"// Inverse 1:N (Collection-typed in RESO; FK lives on child): "
            + ", ".join(f"{name} -> {target}" for name, target in inverse_collections)
        )
    lines.append(f"Table {table_name} {{")

    refs: List[str] = []
    seen_cols: Set[str] = set()

    fields_sorted = sorted(
        fields_for_res,
        key=lambda f: (0 if f["StandardName"] == pk_field else 1, f["StandardName"]),
    )

    for f in fields_sorted:
        sdt = (f.get("SimpleDataType") or "").strip()

        # Collection-typed fields are inverse 1:N relationships in RESO -
        # the FK lives on the child resource, not on the host. Don't emit
        # a column; the per-host inverse list is summarised in the table
        # header comment above.
        if sdt == "Collection":
            continue

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

        # 2NF: skip satellite fields (functionally dependent on an FK,
        # not on the host PK). They remain reachable via the FK join.
        if f["StandardName"] in satellite_fields:
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

    satellites_by_host, satellite_report = compute_satellites(by_res, resource_pks)
    n_sat = sum(len(s) for s in satellites_by_host.values())
    n_collection = sum(
        1 for f in fields if (f.get("SimpleDataType") or "").strip() == "Collection"
    )
    n_kept = len(fields) - n_sat - n_collection
    extra_fks = compute_extra_fks(by_res, resource_pks, satellites_by_host)
    inverse_by_host: Dict[str, List[Tuple[str, str]]] = {
        r: collection_inverse_targets(by_res[r], set(resources)) for r in resources
    }
    n_inverse = sum(len(v) for v in inverse_by_host.values())

    out: List[str] = []
    out.append("// reso-2.0-canonical.dbml")
    out.append("// Pure RESO Data Dictionary 2.0 canonical schema (2NF normalized)")
    out.append(
        f"// {len(resources)} Resources, {n_kept} Fields kept "
        f"({len(fields)} total - {n_sat} satellites - {n_collection} Collection inverses), "
        f"{len(lookup_names)} Lookups"
    )
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
    out.append(f"    {n_kept} Fields kept ({len(fields)} total minus {n_sat} satellite fields and")
    out.append(f"    {n_collection} Collection-typed inverse references), and {len(lookup_names)} Lookups.")
    out.append("")
    out.append("    Three FK detection passes feed the relationship graph:")
    out.append("      1. Resource-typed siblings  -> emit Ref host.<TargetResourceKey> > target.PK")
    out.append("      2. Definition prose         -> 'foreign key relating to the X Resource' or")
    out.append("                                     \"X Resource's YKey\" -> emit Ref")
    out.append("      3. Name-shape `<Word>Key`   -> Word matches a Resource (or its plural)")
    out.append("                                     -> emit Ref (lowest priority)")
    out.append("    Single-value lookup columns get a 4th Ref to lookup_<name>.code.")
    out.append("")
    out.append("    2NF normalization: satellite fields (scalar columns whose name shares the")
    out.append("    prefix of a Resource-typed FK on the same host, e.g. Property.ListAgentEmail")
    out.append("    next to Property.ListAgent -> Member) are removed from the canonical model")
    out.append("    because their value is functionally dependent on the FK column rather than")
    out.append("    the host PK. They remain reachable via the FK join (or, in the case of")
    out.append("    auxiliary IDs / relationship attributes, would belong in a junction table).")
    out.append("    See the `// 2NF: dropped satellite fields` section below for the full list.")
    out.append("")
    out.append("    Collection-typed RESO fields (e.g. Property.Media, Property.OpenHouse) are")
    out.append("    inverse 1:N references - the FK column lives on the child resource, not on")
    out.append("    the host - so they are NOT rendered as host columns. Each host table has a")
    out.append("    `// Inverse 1:N` comment listing them so the relationship is documented.")
    out.append("")
    out.append("    Single-value lookup columns reference the corresponding lookup_<name>.code via DBML")
    out.append("    Refs; multi-value lookup columns stay text and document the lookup in a Note.")
    out.append("")
    out.append("    No Atlas-specific decisions baked in. Atlas adapts this canonical in")
    out.append("    build_atlas_target_dbml.py (wiki/atlas/atlas-target.dbml), where a chosen")
    out.append("    subset of satellites may be re-added for query performance.")
    out.append("  '''")
    out.append("}")
    out.append("")

    out.append("// ============================================================")
    out.append(f"// 2NF: dropped satellite fields ({n_sat} across {len(satellites_by_host)} hosts)")
    out.append("// ============================================================")
    out.append("//")
    out.append("// Reachable via the FK column shown in [brackets]. Re-derive any value")
    out.append("// from the target resource via that FK in your query layer.")
    out.append("//")
    by_host_fk: Dict[Tuple[str, str, str, str], List[str]] = defaultdict(list)
    for host, sat, target, fk, tkey in satellite_report:
        by_host_fk[(host, target, fk, tkey)].append(sat)
    for (host, target, fk, tkey) in sorted(by_host_fk):
        sats = sorted(by_host_fk[(host, target, fk, tkey)])
        out.append(
            f"// {host}: drop {len(sats)} via {host}.{fk} -> {target} "
            f"[FK column: {to_snake(host)}.{to_snake(tkey)}]"
        )
        for s in sats:
            out.append(f"//   - {s}")
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
            satellite_fields=satellites_by_host.get(res, set()),
            inverse_collections=inverse_by_host.get(res, []),
        )
        out.append(block)
        all_refs.extend(refs)

    # Extra FK Refs detected via prose / name-shape (signals beyond the
    # Resource-typed sibling pass). Tagged with the signal in the comment
    # so reviewers can verify the heuristic.
    extra_ref_lines: List[str] = []
    for host, name, target, tpk, signal in extra_fks:
        host_table = resource_to_table[host]
        target_table = resource_to_table[target]
        extra_ref_lines.append(
            f"Ref: {host_table}.{to_snake(name)} > {target_table}.{to_snake(tpk)} "
            f"// {host}.{name} -> {target} [{signal}]"
        )

    out.append("// ============================================================")
    out.append(f"// Lookup reference tables ({len(lookup_names)})")
    out.append("// ============================================================")
    out.append("")
    for n in lookup_names:
        out.append(build_lookup_table(n))

    out.append("// ============================================================")
    out.append(
        f"// Foreign-key relationships ({len(all_refs) + len(extra_ref_lines)} "
        f"= {len(all_refs)} primary + {len(extra_ref_lines)} extra)"
    )
    out.append("// Primary: emitted from Resource-typed siblings (pass 1) and")
    out.append("//          single-value lookup columns (pass 4).")
    out.append("// Extra:   emitted from Definition prose (passes 2-3) and")
    out.append("//          name-shape heuristics (pass 4) for FK columns that")
    out.append("//          have no Resource-typed sibling on the host.")
    out.append("// ============================================================")
    out.append("")
    for r in all_refs:
        out.append(r)
    if extra_ref_lines:
        out.append("")
        out.append(f"// ---- Extra FKs ({len(extra_ref_lines)}) ----")
        for r in extra_ref_lines:
            out.append(r)

    return "\n".join(out) + "\n"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    dbml = build_dbml()
    OUT.write_text(dbml, encoding="utf-8")
    n_lines = len(dbml.splitlines())
    n_tables = sum(1 for ln in dbml.splitlines() if ln.startswith("Table "))
    n_refs = sum(1 for ln in dbml.splitlines() if ln.startswith("Ref:"))
    print(
        f"Wrote {OUT.relative_to(ROOT)} ({n_lines} lines, {len(dbml)} bytes, "
        f"{n_tables} tables, {n_refs} refs)"
    )


if __name__ == "__main__":
    main()
