#!/usr/bin/env python3
"""Build the pure RESO Data Dictionary 2.0 canonical DBML for ALL 41 Resources.

Outputs:
    wiki/dbml/reso-2.0-canonical.dbml   - 41 Resource tables + cross-resource Refs
    wiki/dbml/reso-2.0-lookups.dbml     - 99 Enum blocks for SV lookups (companion)
    wiki/dbml/2nf-satellite-drops.md    - human-readable satellite drop list
    wiki/dbml/extra-fks.md              - human-readable extra-FK list

The canonical DBML is **2NF normalized** with FKs surfaced from four
detection passes (Resource-typed siblings, Definition prose x2,
name-shape). Single-value lookup columns are typed as the snake_case
LookupName (e.g. `standard_status`). The actual `Enum standard_status
{ ... values ... }` blocks live in the companion `reso-2.0-lookups.dbml`
- this split keeps the main schema small enough for any DBML viewer
while preserving full enum value sets in a co-locatable companion file.

Multi-value lookup columns (`String List, Multi`) stay `varchar`
because DBML's single-column FK / type system can't model array
membership; their LookupName is documented in the column Note. Open
lookups (LookupName declared by RESO but with no closed value list,
e.g. `City`, `MlsStatus`, `AOR`) are also `varchar` and tagged
explicitly in the Note.

Inputs:
    raw/fields.csv         (parsed from RESO_Data_Dictionary_2.0.xlsx)
    raw/lookups.csv        (parsed from RESO_Data_Dictionary_2.0.xlsx)
    raw/field_metadata.csv (scraped from dd.reso.org/DD2.0)

Atlas adapts this canonical in `build_atlas_target_dbml.py`.
"""
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "wiki" / "dbml" / "reso-2.0-canonical.dbml"
OUT_LOOKUPS = ROOT / "wiki" / "dbml" / "reso-2.0-lookups.dbml"
OUT_DROPS = ROOT / "wiki" / "dbml" / "2nf-satellite-drops.md"
OUT_EXTRAS = ROOT / "wiki" / "dbml" / "extra-fks.md"

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


def field_note(
    f: Dict[str, str],
    meta: Dict[str, str],
    lookup_names: Optional[Set[str]] = None,
) -> str:
    parts = [f["StandardName"]]
    defn = (f.get("Definition") or "").strip().replace("\n", " ")
    if defn:
        parts.append(defn[:160])
    sdt = f.get("SimpleDataType") or ""
    if sdt:
        parts.append(f"type={sdt}")
    lookup = (f.get("LookupName") or "").strip()
    if lookup:
        sdt_clean = (f.get("SimpleDataType") or "").strip()
        is_multi = sdt_clean == "String List, Multi"
        is_open = lookup_names is not None and lookup not in lookup_names
        suffix = ""
        if is_open:
            suffix = " (open: jurisdiction-defined; no closed value list)"
        elif is_multi:
            suffix = " (multi-value; column stores comma-separated codes)"
        parts.append(f"lookup={lookup}{suffix}")
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

        # Single-value lookup columns get the snake_case LookupName as their
        # type. The actual `Enum <name> { ... }` block lives in the companion
        # reso-2.0-lookups.dbml. DBML viewers rendering the canonical file
        # standalone will treat the type as an opaque custom type (the
        # enum-name still serves as documentation); loaded together with
        # the lookups file, the type becomes a real validated enum.
        lookup = (f.get("LookupName") or "").strip()
        if (
            lookup
            and lookup in lookup_names
            and sdt == "String List, Single"
        ):
            col_type = to_snake(lookup)
        else:
            col_type = map_dbml_type(sdt, f.get("SugMaxLength") or "")

        attrs: List[str] = []
        if pk_field and f["StandardName"] == pk_field:
            attrs.append("pk")

        meta_row = meta.get((resource, f["StandardName"]), {})
        attrs.append(f"note: {field_note(f, meta_row, lookup_names)}")
        lines.append(f"  {col_name} {col_type} [{', '.join(attrs)}]")

    lines.append(f"  Note: 'RESO 2.0 canonical {resource} resource'")
    lines.append("}")
    lines.append("")
    return "\n".join(lines), refs


def _load_lookup_values() -> Dict[str, List[Tuple[str, str]]]:
    """Return {LookupName: [(StandardLookupValue, LegacyODataValue), ...]}
    preserving raw/lookups.csv ordering and de-duplicating on the standard
    code (some lookups have repeated rows for legacy variants)."""
    out: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    seen: Dict[str, Set[str]] = defaultdict(set)
    with (RAW / "lookups.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            n = (r.get("LookupName") or "").strip()
            v = (r.get("StandardLookupValue") or "").strip()
            legacy = (r.get("LegacyODataValue") or "").strip()
            if not n or not v:
                continue
            if v in seen[n]:
                continue
            seen[n].add(v)
            out[n].append((v, legacy))
    return out


_DBML_ENUM_VALUE_OK = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _enum_value(code: str) -> str:
    """DBML enum values that contain spaces, slashes, hyphens, or other
    non-identifier characters must be wrapped in double quotes. Returns
    the value as a DBML-safe token."""
    if _DBML_ENUM_VALUE_OK.match(code):
        return code
    # Escape any embedded double-quotes (unlikely in RESO codes but safe).
    return '"' + code.replace('"', '\\"') + '"'


def build_lookups_dbml(
    fields: List[Dict[str, str]],
    lookup_names: List[str],
) -> str:
    """Render the companion `reso-2.0-lookups.dbml` containing one DBML
    `Enum` block per single-value-targeted RESO LookupName, plus a
    documentation block listing the multi-only and open lookups (which
    cannot be modelled as enums)."""
    values = _load_lookup_values()

    # Categorise lookups by usage in fields.csv
    lookup_users: Dict[str, Counter] = defaultdict(Counter)
    for f in fields:
        ln = (f.get("LookupName") or "").strip()
        if not ln:
            continue
        sdt = (f.get("SimpleDataType") or "").strip()
        lookup_users[ln][sdt] += 1

    sv_lookups = sorted(
        n for n in lookup_names
        if "String List, Single" in lookup_users.get(n, {})
    )
    mv_only_lookups = sorted(
        n for n in lookup_names
        if lookup_users.get(n)
        and "String List, Single" not in lookup_users[n]
    )
    open_lookups = sorted(
        n for n in lookup_users
        if n not in set(lookup_names)
    )

    out: List[str] = []
    out.append("// reso-2.0-lookups.dbml")
    out.append(
        f"// {len(sv_lookups)} Enum blocks for RESO DD 2.0 single-value lookups"
    )
    out.append("// Companion to wiki/dbml/reso-2.0-canonical.dbml.")
    out.append("//")
    out.append("// Generated by reso-dd-kb/scripts/build_reso_canonical_dbml.py")
    out.append("// Source: raw/lookups.csv + raw/fields.csv")
    out.append("")
    out.append("Project reso_canonical_dd_2_0_lookups {")
    out.append("  database_type: 'PostgreSQL'")
    out.append("  Note: '''")
    out.append(
        f"    Enum value sets for the {len(sv_lookups)} RESO 2.0 lookups that are referenced"
    )
    out.append(
        "    by at least one `String List, Single` column in the canonical schema."
    )
    out.append(
        "    Single-value lookup columns in `reso-2.0-canonical.dbml` are typed as the"
    )
    out.append(
        "    snake_case LookupName (e.g. `standard_status`); DBML viewers that load both"
    )
    out.append(
        "    files together resolve the column type to a real validated enum."
    )
    out.append("")
    out.append(
        f"    {len(mv_only_lookups)} multi-value-only lookups and {len(open_lookups)} open"
    )
    out.append(
        "    (jurisdiction-defined, no closed value list) lookups are NOT emitted as"
    )
    out.append(
        "    enums - DBML's type system can't model array membership for the former,"
    )
    out.append(
        "    and there is no closed value set to enumerate for the latter. Both groups"
    )
    out.append(
        "    are listed at the bottom of this file as comments for reference."
    )
    out.append("  '''")
    out.append("}")
    out.append("")
    out.append("// ============================================================")
    out.append(f"// Single-value lookup enums ({len(sv_lookups)})")
    out.append("// ============================================================")
    out.append("")

    for name in sv_lookups:
        snake = to_snake(name)
        vs = values.get(name, [])
        n_users = sum(lookup_users[name].values())
        out.append(f"// ---- {name} ({len(vs)} values, {n_users} field user(s)) ----")
        out.append(f"Enum {snake} {{")
        for code, legacy in vs:
            tok = _enum_value(code)
            note_bits = []
            if legacy and legacy != code:
                note_bits.append(f"legacy={legacy}")
            if note_bits:
                out.append(f"  {tok} [note: '{' | '.join(note_bits)}']")
            else:
                out.append(f"  {tok}")
        out.append("}")
        out.append("")

    out.append("// ============================================================")
    out.append(
        f"// Multi-value lookups - NOT emitted as enums ({len(mv_only_lookups)})"
    )
    out.append("// ============================================================")
    out.append("// These LookupNames are referenced only by `String List, Multi` columns,")
    out.append("// which store comma-separated codes. DBML's single-column type system")
    out.append("// can't model array membership; the host column stays `varchar` and tags")
    out.append("// the LookupName in its Note. See raw/lookups.csv for value sets.")
    out.append("//")
    for n in mv_only_lookups:
        n_values = len(values.get(n, []))
        n_users = sum(lookup_users[n].values())
        out.append(f"//   {n}  ({n_values} values, {n_users} multi-value column user(s))")
    out.append("")

    out.append("// ============================================================")
    out.append(
        f"// Open lookups - NOT emitted as enums ({len(open_lookups)})"
    )
    out.append("// ============================================================")
    out.append("// These LookupNames are declared by RESO but ship no closed value list")
    out.append("// (jurisdiction-defined: each MLS sets its own values). Columns that")
    out.append("// reference them stay `varchar` and tag `(open: jurisdiction-defined;")
    out.append("// no closed value list)` in their Note.")
    out.append("//")
    for n in open_lookups:
        n_users = sum(lookup_users[n].values())
        out.append(f"//   {n}  ({n_users} field user(s))")
    out.append("")
    return "\n".join(out) + "\n"


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
        f"({len(fields)} total - {n_sat} satellites - {n_collection} Collection inverses)"
    )
    out.append("// Lookup enums live in the companion file `reso-2.0-lookups.dbml`.")
    out.append("//")
    out.append("// Generated by reso-dd-kb/scripts/build_reso_canonical_dbml.py")
    out.append("// Source: dd.reso.org/DD2.0 + raw/fields.csv + raw/lookups.csv + raw/field_metadata.csv")
    out.append("//")
    out.append("// Companion files:")
    out.append("//   - wiki/dbml/reso-2.0-lookups.dbml    99 Enum blocks for SV lookups")
    out.append(f"//   - wiki/dbml/2nf-satellite-drops.md   {n_sat} dropped satellites by host+FK+target")
    out.append("//   - wiki/dbml/extra-fks.md             FKs detected via prose / name-shape")
    out.append("")
    out.append("Project reso_canonical_dd_2_0 {")
    out.append("  database_type: 'PostgreSQL'")
    out.append("  Note: '''")
    out.append(f"    Pure RESO Data Dictionary 2.0 canonical schema: {len(resources)} Resources,")
    out.append(f"    {n_kept} Fields kept (= {len(fields)} total - {n_sat} satellites - {n_collection} Collection inverses).")
    out.append("")
    out.append("    FK detection (4 passes, full algorithm in methodology.md Step 3):")
    out.append("      1. Resource-typed siblings  -> Ref host.<TargetResourceKey> > target.PK")
    out.append("      2. Definition prose         -> 'foreign key relating to the X Resource'")
    out.append("      3. Definition prose         -> \"X Resource's YKey\"")
    out.append("      4. Name-shape `<Word>Key`   -> Word names a Resource")
    out.append("    Lookup constraints are expressed as enum types defined in the companion")
    out.append("    file `reso-2.0-lookups.dbml`; no Ref: lines are emitted for lookups.")
    out.append("")
    out.append("    Single-value (String List, Single) lookup columns are typed as the snake_case")
    out.append("    LookupName (e.g. `standard_status`); the matching `Enum standard_status { ... }`")
    out.append("    block lives in the companion file. Multi-value (String List, Multi) lookup")
    out.append("    columns stay `varchar` - DBML's type system can't model array membership -")
    out.append("    and tag their LookupName in the column Note. Open lookups (LookupName")
    out.append("    declared by RESO but with no closed value list, e.g. City, MlsStatus, AOR)")
    out.append("    are also `varchar` and tagged `(open: jurisdiction-defined)` in the Note.")
    out.append("")
    out.append(f"    2NF normalization drops {n_sat} satellite fields (full per-host list in")
    out.append("    `wiki/dbml/2nf-satellite-drops.md`). Collection-typed inverse references")
    out.append(f"    ({n_collection}) live as `// Inverse 1:N` comments on each host table; the")
    out.append("    forward FK is emitted on the child resource by the four FK passes.")
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
    out.append(
        f"// Cross-resource FK relationships "
        f"({len(all_refs) + len(extra_ref_lines)} = {len(all_refs)} primary "
        f"+ {len(extra_ref_lines)} extra)"
    )
    out.append("// Primary: from Resource-typed siblings (pass 1).")
    out.append("// Extra:   from Definition prose (passes 2-3) and name-shape")
    out.append("//          heuristics (pass 4) for FK columns with no sibling.")
    out.append("// Lookup constraints: see reso-2.0-lookups.dbml (enum types).")
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


def build_satellite_drops_md(
    by_res: Dict[str, List[Dict[str, str]]],
    resource_pks: Dict[str, Optional[str]],
) -> str:
    """Render a human-readable companion to the canonical DBML enumerating
    every satellite field dropped during 2NF normalization, grouped by host
    + FK + target Resource."""
    _, report = compute_satellites(by_res, resource_pks)
    grouped: Dict[str, Dict[Tuple[str, str, str], List[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for host, sat, target, fk, tkey in report:
        grouped[host][(target, fk, tkey)].append(sat)
    n_total = sum(
        len(sats) for host_g in grouped.values() for sats in host_g.values()
    )

    lines: List[str] = []
    lines.append("# 2NF satellite-field drops (canonical RESO DD 2.0)")
    lines.append("")
    lines.append(
        f"This is the human-readable companion to "
        f"[`reso-2.0-canonical.dbml`](./reso-2.0-canonical.dbml). It enumerates "
        f"every RESO 2.0 field that was removed during 2NF normalization "
        f"because its value is functionally dependent on a foreign key on the "
        f"same host rather than on the host's primary key."
    )
    lines.append("")
    lines.append(
        f"**{n_total} satellites** dropped across **{len(grouped)} host "
        f"resources**. For every drop, the FK column shown below is the only "
        f"thing the canonical model retains; re-derive the satellite value at "
        f"read time by JOINing through that FK to the target resource."
    )
    lines.append("")
    lines.append(
        "Generated by [`scripts/build_reso_canonical_dbml.py`](../../scripts/build_reso_canonical_dbml.py). "
        "Do not edit by hand — regenerate after refreshing `raw/fields.csv`."
    )
    lines.append("")

    lines.append("## Summary by host")
    lines.append("")
    lines.append("| Host resource | Satellites dropped | Distinct FKs |")
    lines.append("|---|---:|---:|")
    for host in sorted(grouped, key=lambda h: -sum(len(v) for v in grouped[h].values())):
        host_total = sum(len(v) for v in grouped[host].values())
        n_fks = len(grouped[host])
        lines.append(f"| `{host}` | {host_total} | {n_fks} |")
    lines.append(f"| **Total** | **{n_total}** | |")
    lines.append("")

    lines.append("## Detailed list")
    lines.append("")
    for host in sorted(grouped):
        host_total = sum(len(v) for v in grouped[host].values())
        lines.append(f"### {host}  ({host_total} satellites dropped)")
        lines.append("")
        for (target, fk, tkey) in sorted(grouped[host]):
            sats = sorted(grouped[host][(target, fk, tkey)])
            host_table = to_snake(host)
            fk_col = to_snake(tkey)
            target_table = to_snake(target)
            target_pk_snake = to_snake(resource_pks.get(target) or "")
            lines.append(
                f"**via FK `{host}.{fk}` -> `{target}` "
                f"(`{host_table}.{fk_col}` -> `{target_table}.{target_pk_snake}`)** "
                f"- {len(sats)} field(s)"
            )
            lines.append("")
            for s in sats:
                lines.append(f"- `{s}`")
            lines.append("")
    return "\n".join(lines) + "\n"


def build_extra_fks_md(
    by_res: Dict[str, List[Dict[str, str]]],
    resource_pks: Dict[str, Optional[str]],
    satellites_by_host: Dict[str, Set[str]],
) -> str:
    """Render a human-readable companion enumerating every FK detected via
    Definition prose or name-shape (i.e. NOT via a Resource-typed sibling)."""
    extras = compute_extra_fks(by_res, resource_pks, satellites_by_host)

    lines: List[str] = []
    lines.append("# Extra FKs (prose + name-shape detection)")
    lines.append("")
    lines.append(
        "This is the human-readable companion to "
        "[`reso-2.0-canonical.dbml`](./reso-2.0-canonical.dbml). It enumerates "
        "every foreign-key relationship in the canonical schema that was "
        "discovered by something other than a Resource-typed sibling row in "
        "`raw/fields.csv` (the primary FK signal)."
    )
    lines.append("")
    lines.append("Three signals (in priority order):")
    lines.append("")
    lines.append(
        "1. **`prose-foreign-key`** - Definition contains "
        "*\"foreign key relating to the X Resource\"*."
    )
    lines.append(
        "2. **`prose-resources`** - Definition contains *\"X Resource's YKey\"*."
    )
    lines.append(
        "3. **`name-shape`** - Field name `<Word>Key` where `<Word>` is itself "
        "a Resource name (or its singular form for plural Resources like "
        "`Contacts`/`Teams`/`Rules`)."
    )
    lines.append("")
    lines.append(
        f"**{len(extras)} extra FKs** are emitted from these signals (after "
        "filtering hits that match satellite-dropped columns)."
    )
    lines.append("")
    lines.append(
        "Generated by [`scripts/build_reso_canonical_dbml.py`](../../scripts/build_reso_canonical_dbml.py). "
        "Do not edit by hand."
    )
    lines.append("")
    lines.append("## Detected FKs")
    lines.append("")
    lines.append("| Host | Field | Target | Target PK | Signal |")
    lines.append("|---|---|---|---|---|")
    for host, name, target, tpk, signal in extras:
        host_table = to_snake(host)
        target_table = to_snake(target)
        col = to_snake(name)
        tpk_col = to_snake(tpk)
        lines.append(
            f"| `{host}` (`{host_table}`) | `{name}` (`{col}`) | "
            f"`{target}` (`{target_table}`) | `{tpk}` (`{tpk_col}`) | `{signal}` |"
        )
    return "\n".join(lines) + "\n"


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

    # Re-derive the inputs once for the .md companions (cheap; deterministic).
    fields = load_fields()
    by_res: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for f in fields:
        by_res[f["ResourceName"]].append(f)
    resources = sorted(by_res)
    resource_pks: Dict[str, Optional[str]] = {
        r: derive_pk(r, by_res[r]) for r in resources
    }
    satellites_by_host, _ = compute_satellites(by_res, resource_pks)

    drops_md = build_satellite_drops_md(by_res, resource_pks)
    OUT_DROPS.write_text(drops_md, encoding="utf-8")
    print(
        f"Wrote {OUT_DROPS.relative_to(ROOT)} "
        f"({len(drops_md.splitlines())} lines, {len(drops_md)} bytes)"
    )

    extras_md = build_extra_fks_md(by_res, resource_pks, satellites_by_host)
    OUT_EXTRAS.write_text(extras_md, encoding="utf-8")
    print(
        f"Wrote {OUT_EXTRAS.relative_to(ROOT)} "
        f"({len(extras_md.splitlines())} lines, {len(extras_md)} bytes)"
    )

    lookup_names = load_lookup_names()
    lookups_dbml = build_lookups_dbml(fields, lookup_names)
    OUT_LOOKUPS.write_text(lookups_dbml, encoding="utf-8")
    n_enums = sum(1 for ln in lookups_dbml.splitlines() if ln.startswith("Enum "))
    print(
        f"Wrote {OUT_LOOKUPS.relative_to(ROOT)} "
        f"({len(lookups_dbml.splitlines())} lines, {len(lookups_dbml)} bytes, "
        f"{n_enums} enums)"
    )


if __name__ == "__main__":
    main()
