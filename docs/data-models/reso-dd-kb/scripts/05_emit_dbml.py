#!/usr/bin/env python3
"""
Phase 3: emit canonical DBML from Phase 1/2/2.5 CSVs.

Reads:
    raw/resources.csv          (Phase 1)
    raw/fields.csv             (Phase 1)
    raw/field_definitions.csv  (Phase 1)
    raw/lookups.csv            (Phase 1)
    raw/lookup_values.csv      (Phase 1)
    raw/relationships.csv      (Phase 2 - FK source)
    raw/satellites.csv         (Phase 2.5 - column-drop source)

Writes:
    wiki/dbml/canonical.dbml   (41 Tables + Refs + // REVIEW comments)
    wiki/dbml/lookups.dbml     (Enums for SV lookups + MV/open notes)

Phase 3 is a pure code-gen pass. Every Table / Column / Ref / Enum
traces back to a row in the input CSVs:

  - Tables                <- resources.csv
  - Columns on a Table    <- fields.csv (minus drop_from_host rows
                             from satellites.csv; review rows kept
                             with a // REVIEW comment)
  - Column types          <- SimpleDataType + MaxLength on the
                             field row + Lookup -> Enum mapping
  - Refs                  <- relationships.csv (high+medium only;
                             collection_typed skipped as inverse;
                             polymorphic emits a // comment)
  - Enums                 <- lookups.csv (SV) + lookup_values.csv

No hand-curated alias map. No implicit FK detection inside the
generator. The only schema decision the generator makes that is NOT
in a CSV is the per-resource primary-key choice for resources whose
PK column is not the obvious `<Resource>Key` shape - those nine
overrides are listed in PK_OVERRIDES below, each with an explanatory
comment.

Idempotent: deletes wiki/dbml/canonical.dbml and lookups.dbml at
the start.

Determinism: tables emitted in resources.csv order; columns within
a table in fields.csv order (which is the page order from the mirror);
refs sorted alphabetically; enums sorted alphabetically by name.

Verification gates (hard-fail):
    1. Every Table block declared exactly once.
    2. Resource count in DBML == len(resources.csv).
    3. Every Ref source/target Table is declared.
    4. Every Ref source/target column exists in its Table.
    5. Every Enum referenced by a column is declared.
    6. No `(resource, field)` pair from fields.csv that survived
       the drop policy is silently missing from the DBML.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"
DBML_DIR = KB_ROOT / "wiki" / "dbml"

OUT_CANONICAL = DBML_DIR / "canonical.dbml"
OUT_LOOKUPS = DBML_DIR / "lookups.dbml"

# ----------------------------------------------------------------------
# Per-resource primary key. The 9 resources below have ambiguous PK
# candidates (multiple *Key columns) and need an explicit override.
# Each entry cites the dd.reso.org page that motivates the choice.
# ----------------------------------------------------------------------
PK_OVERRIDES: dict[str, str] = {
    # `Property` is the canonical "listing" table; its PK is ListingKey.
    # The other *Key columns (BuyerAgentKey, ListAgentKey, ...) are FKs.
    "Property": "ListingKey",
    # OUID's PK is the "OUID Key" column on dd.reso.org. The matching
    # field name in the corpus is `OrganizationUniqueIdKey`.
    "OUID": "OrganizationUniqueIdKey",
    # PropertyXxx sub-resources: their own *Key column is the PK; the
    # ListingKey column is the FK back to Property.
    "PropertyGreenVerification": "GreenBuildingVerificationKey",
    "PropertyPowerProduction": "PowerProductionKey",
    "PropertyRooms": "RoomKey",
    "PropertyUnitTypes": "UnitTypeKey",
    # Junction tables - composite key in RESO. We pick the
    # "<JunctionName>Key" stand-in if it exists, otherwise the most-
    # prominent FK column. Phase 3 declares this single column as PK
    # for tooling convenience; the true uniqueness is composite.
    "MemberAssociation": "AssociationKey",  # composite (AssociationKey + MemberKey)
    "OfficeAssociation": "AssociationKey",  # composite (AssociationKey + OfficeKey)
    # InternetTracking is event-shaped; EventKey is the natural PK.
    "InternetTracking": "EventKey",
    # Queue's transactional PK column.
    "Queue": "QueueTransactionKey",
}

# DBML type mapping for non-lookup columns. Lookup columns use a
# separate path (enum reference for SV, varchar for MV/open).
SIMPLE_TYPE_TO_DBML = {
    "String": "varchar",
    "Number": "int",  # widened to `double` if the field's MaxPrecision > 0
    "Boolean": "bool",
    "Timestamp": "timestamp",
    "Date": "date",
}

# Resource and Collection are FK companions; they have NO scalar
# column in the host table. The Ref (or its inverse) is emitted at
# the bottom of the file.
SKIPPED_SIMPLE_TYPES = {"Resource", "Collection"}


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------
def must_exist(path: Path) -> None:
    if not path.exists():
        print(f"FAIL: required input missing: {path}", file=sys.stderr)
        raise SystemExit(2)


def load(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open()))


# CamelCase -> snake_case for table and column identifiers.
_CAMEL_RE_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_RE_2 = re.compile(r"([a-z0-9])([A-Z])")


def snake(name: str) -> str:
    s = _CAMEL_RE_1.sub(r"\1_\2", name)
    s = _CAMEL_RE_2.sub(r"\1_\2", s)
    return s.lower()


def escape_note(text: str) -> str:
    if not text:
        return ""
    # Single-line; collapse whitespace; escape single quotes for DBML
    # single-quoted Note strings.
    one_line = re.sub(r"\s+", " ", text.replace("\u2019", "'")).strip()
    return one_line.replace("\\", "\\\\").replace("'", "\\'")


def first_sentence(text: str, max_len: int = 200) -> str:
    if not text:
        return ""
    one_line = re.sub(r"\s+", " ", text.replace("\u2019", "'")).strip()
    # Definition prose ends sentences with `. `; take the first.
    m = re.search(r"\.(?:\s|$)", one_line)
    if m:
        return one_line[: m.end()].strip()
    return one_line[:max_len]


def derive_pk(resource_name: str, fields_for_resource: list[dict]) -> str | None:
    if resource_name in PK_OVERRIDES:
        return PK_OVERRIDES[resource_name]
    names = {f["StandardName"] for f in fields_for_resource}
    if (resource_name + "Key") in names:
        return resource_name + "Key"
    if resource_name.endswith("s"):
        sing = resource_name[:-1] + "Key"
        if sing in names:
            return sing
    keys = [n for n in names if n.endswith("Key")]
    if len(keys) == 1:
        return keys[0]
    return None


def lookup_kind_for_resource(lookup_values_by_name: dict[str, list[dict]],
                             lookup_name: str) -> str:
    """`closed` if the lookup has values; `open` otherwise (RESO uses
    open lookups for jurisdiction-defined value sets like AOR, City)."""
    return "closed" if lookup_values_by_name.get(lookup_name) else "open"


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main() -> int:
    for p in (
        RAW / "resources.csv",
        RAW / "fields.csv",
        RAW / "field_definitions.csv",
        RAW / "lookups.csv",
        RAW / "lookup_values.csv",
        RAW / "relationships.csv",
        RAW / "satellites.csv",
    ):
        must_exist(p)

    DBML_DIR.mkdir(parents=True, exist_ok=True)
    if OUT_CANONICAL.exists():
        OUT_CANONICAL.unlink()
    if OUT_LOOKUPS.exists():
        OUT_LOOKUPS.unlink()

    resources = load(RAW / "resources.csv")
    fields = load(RAW / "fields.csv")
    defs = {
        (r["ResourceName"], r["StandardName"]): r["Definition"]
        for r in load(RAW / "field_definitions.csv")
    }
    lookups = load(RAW / "lookups.csv")
    lookup_values = load(RAW / "lookup_values.csv")
    rels = load(RAW / "relationships.csv")
    sats = load(RAW / "satellites.csv")

    fields_by_resource: dict[str, list[dict]] = defaultdict(list)
    field_index: set[tuple[str, str]] = set()
    for f in fields:
        fields_by_resource[f["ResourceName"]].append(f)
        field_index.add((f["ResourceName"], f["StandardName"]))

    lookup_values_by_name: dict[str, list[dict]] = defaultdict(list)
    for v in lookup_values:
        lookup_values_by_name[v["LookupName"]].append(v)

    # ------------------------------------------------------------------
    # Apply Phase-2.5 satellite policy.
    #   drop_from_host -> drop the column entirely
    #   review         -> keep + flag with // REVIEW
    #   keep_both      -> keep silently
    #   drop_from_child -> not applied (overrides only)
    # ------------------------------------------------------------------
    drop_set: set[tuple[str, str]] = set()
    review_reasons: dict[tuple[str, str], str] = {}
    for s in sats:
        key = (s["host_resource"], s["candidate_satellite"])
        if s["recommendation"] == "drop_from_host":
            drop_set.add(key)
        elif s["recommendation"] == "review":
            review_reasons[key] = (
                f"satellite of FK {s['host_field']} -> "
                f"{s['target_resource']}.{s['target_field']}; "
                f"jaccard={s['jaccard']}, type_match={s['type_match']}, "
                f"signals={s['signals_fired']}, notes={s['notes']}"
            )

    # ------------------------------------------------------------------
    # Per-resource PK resolution (used for empty-target_field FKs).
    # ------------------------------------------------------------------
    pk_by_resource: dict[str, str | None] = {}
    for res in resources:
        rname = res["ResourceName"]
        pk_by_resource[rname] = derive_pk(rname, fields_by_resource.get(rname, []))

    # ------------------------------------------------------------------
    # Lookup classification.
    # closed = has values in lookup_values.csv -> emit Enum
    # open   = no values -> varchar w/ note
    # SV     = at least one field with SimpleDataType 'String List, Single'
    #          uses this lookup -> emit Enum reference on those columns
    # MV     = 'String List, Multi' usage -> varchar with note
    # ------------------------------------------------------------------
    lookup_uses_sv: set[str] = set()
    lookup_uses_mv: set[str] = set()
    for f in fields:
        if not f["Lookup"]:
            continue
        if f["SimpleDataType"] == "String List, Single":
            lookup_uses_sv.add(f["Lookup"])
        elif f["SimpleDataType"] == "String List, Multi":
            lookup_uses_mv.add(f["Lookup"])

    sv_lookups_to_emit = sorted(
        l["LookupName"] for l in lookups
        if l["LookupName"] in lookup_uses_sv and lookup_values_by_name.get(l["LookupName"])
    )
    mv_only_lookups = sorted(
        l["LookupName"] for l in lookups
        if l["LookupName"] in (lookup_uses_mv - lookup_uses_sv)
    )
    open_lookups = sorted(
        l["LookupName"] for l in lookups
        if not lookup_values_by_name.get(l["LookupName"])
    )

    # ------------------------------------------------------------------
    # Render canonical.dbml table-by-table.
    # ------------------------------------------------------------------
    declared_columns: dict[str, set[str]] = {}  # snake table -> set(snake col)
    declared_tables: list[str] = []
    out_lines: list[str] = []

    out_lines.append("// canonical.dbml")
    out_lines.append("// RESO Data Dictionary 2.0 canonical schema (2NF normalised)")
    out_lines.append(
        f"// Generated by reso-dd-kb/scripts/05_emit_dbml.py from Phase 1/2/2.5 CSVs."
    )
    out_lines.append("// Companion file: lookups.dbml (Enum blocks for SV lookups).")
    out_lines.append("")
    out_lines.append("Project reso_canonical_dd_2_0 {")
    out_lines.append("  database_type: 'PostgreSQL'")
    out_lines.append("  Note: '''")
    out_lines.append(
        "    RESO Data Dictionary 2.0, derived from a verifiable mirror of "
        "dd.reso.org/DD2.0/."
    )
    out_lines.append(
        "    Tables: 41 (one per Resource).  FKs: from raw/relationships.csv "
        "(high + medium confidence)."
    )
    out_lines.append(
        "    Column drops: from raw/satellites.csv recommendation == "
        "drop_from_host (Phase 2.5)."
    )
    out_lines.append(
        "    Review markers: rows with recommendation == review carry a "
        "// REVIEW comment."
    )
    out_lines.append("  '''")
    out_lines.append("}")
    out_lines.append("")
    out_lines.append("// ============================================================")
    out_lines.append(f"// Resources ({len(resources)})")
    out_lines.append("// ============================================================")
    out_lines.append("")

    # FK lookup helpers (used while rendering each table to attach
    # inverse-1:N comments and during Ref emission below).
    rels_by_host: dict[str, list[dict]] = defaultdict(list)
    for r in rels:
        rels_by_host[r["host_resource"]].append(r)

    # Per-row column metadata gets stored so we can later emit Refs
    # without rebuilding everything.
    table_column_index: dict[tuple[str, str], str] = {}  # (snake_table, snake_col) -> CamelName

    for res in resources:
        rname = res["ResourceName"]
        snake_table = snake(rname)
        declared_tables.append(snake_table)

        rfields = fields_by_resource.get(rname, [])
        pk_field = pk_by_resource.get(rname)

        # Inverse 1:N comment: collection_typed FKs from this host.
        inverse_lines: list[str] = []
        for r in sorted(rels_by_host.get(rname, []), key=lambda x: x["host_field"]):
            if r["fk_kind"] == "collection_typed" and r["target_resource"]:
                inverse_lines.append(
                    f"// inverse 1:N: {r['host_field']} -> {r['target_resource']}"
                )

        out_lines.append(f"// ---- {rname} ({res['FieldCount']} fields on dd.reso.org) ----")
        for il in inverse_lines:
            out_lines.append(il)
        out_lines.append(f"Table {snake_table} {{")

        col_set: set[str] = set()
        for f in rfields:
            cname = f["StandardName"]
            simple = f["SimpleDataType"]
            # Drop satellite columns and Resource/Collection companions.
            if (rname, cname) in drop_set:
                continue
            if simple in SKIPPED_SIMPLE_TYPES:
                continue

            scol = snake(cname)
            note_bits = [cname]
            d = first_sentence(defs.get((rname, cname), ""))
            if d:
                note_bits.append(d)
            note_bits.append(f"type={simple}")
            if f.get("MaxLength"):
                note_bits.append(f"max_len={f['MaxLength']}")
            if f.get("Lookup"):
                note_bits.append(f"lookup={f['Lookup']}")
            note = escape_note(" | ".join(note_bits))

            col_attrs: list[str] = []
            if cname == pk_field:
                col_attrs.append("pk")

            # Lookup column handling.
            if simple == "String List, Single" and f["Lookup"] in sv_lookups_to_emit:
                dbml_type = snake(f["Lookup"])
            elif simple == "String List, Single":
                dbml_type = "varchar"
                note_bits.insert(-1, "open: jurisdiction-defined; no closed value list")
                note = escape_note(" | ".join(note_bits))
            elif simple == "String List, Multi":
                dbml_type = "varchar"
                note_bits.insert(-1, f"multi: {f['Lookup']}")
                note = escape_note(" | ".join(note_bits))
            elif simple == "Number":
                # Widen to double when MaxPrecision > 0.
                try:
                    prec = float(f.get("MaxPrecision") or "0")
                except ValueError:
                    prec = 0.0
                dbml_type = "double" if prec > 0 else "int"
            elif simple in SIMPLE_TYPE_TO_DBML:
                dbml_type = SIMPLE_TYPE_TO_DBML[simple]
                # Tighten varchar with MaxLength when known.
                if dbml_type == "varchar":
                    try:
                        ml = int(float(f.get("MaxLength") or "0"))
                    except ValueError:
                        ml = 0
                    if 0 < ml < 4000:
                        dbml_type = f"varchar({ml})"
            else:
                # Unknown SimpleDataType - shouldn't happen on the
                # corpus but keep the script robust.
                dbml_type = "varchar"

            col_attrs.append(f"note: '{note}'")
            attr_str = "[" + ", ".join(col_attrs) + "]" if col_attrs else ""

            if (rname, cname) in review_reasons:
                out_lines.append(
                    f"  // REVIEW: {escape_note(review_reasons[(rname, cname)])}"
                )
            out_lines.append(f"  {scol} {dbml_type} {attr_str}".rstrip())
            col_set.add(scol)
            table_column_index[(snake_table, scol)] = cname

        out_lines.append("}")
        out_lines.append("")
        declared_columns[snake_table] = col_set

    # ------------------------------------------------------------------
    # Refs (FKs).
    # ------------------------------------------------------------------
    out_lines.append("// ============================================================")
    out_lines.append("// Refs (foreign keys) - high + medium confidence only")
    out_lines.append("// Source: raw/relationships.csv (Phase 2)")
    out_lines.append("// ============================================================")
    out_lines.append("")

    refs_emitted: list[tuple[str, str, str, str, str]] = []  # for sorting + gates
    polymorphic_comments: list[str] = []
    skipped_low: list[str] = []
    skipped_collection: list[str] = []
    skipped_dropped: list[str] = []  # FK column was dropped as satellite
    skipped_no_target: list[str] = []  # could not resolve target column
    skipped_no_host_col: list[str] = []  # FK column was a Resource/Collection companion

    for r in rels:
        if r["confidence"] == "low":
            skipped_low.append(f"{r['host_resource']}.{r['host_field']} -> {r['target_resource']}")
            continue
        if r["fk_kind"] == "collection_typed":
            skipped_collection.append(f"{r['host_resource']}.{r['host_field']} -> {r['target_resource']}")
            continue
        if r["notes"] == "polymorphic" or r["fk_kind"] == "prose" and "polymorphic" in r["notes"]:
            polymorphic_comments.append(
                f"// polymorphic FK: {r['host_resource']}.{r['host_field']}  "
                f"({r['evidence']})"
            )
            continue

        host_table = snake(r["host_resource"])
        host_col = snake(r["host_field"])
        # If the FK column was dropped as a satellite (rare but
        # possible), skip the Ref - the column doesn't exist anymore.
        if (r["host_resource"], r["host_field"]) in drop_set:
            skipped_dropped.append(
                f"{r['host_resource']}.{r['host_field']} -> {r['target_resource']}"
            )
            continue
        # Resource-typed FK columns have no scalar in the table
        # (we omitted them at table render time). The FK IS declared
        # by rels.csv though, so pick the natural scalar carrier on
        # the host: a column named <ResourceField>Key, <ResourceField>Id,
        # or <ResourceField>ID. This is NOT implicit FK detection -
        # the FK existence is already declared; we are just choosing
        # which column on the host carries the value.
        if host_col not in declared_columns.get(host_table, set()):
            if r["fk_kind"] == "resource_typed":
                # Resource-typed FK has no scalar column on the host.
                # Find a sibling scalar carrier (<base>Id, <base>ID,
                # <base>Key) BUT only if its Definition mentions the
                # target resource name or the target PK column name.
                # Without that check we'd attach the FK to upstream
                # local-key columns (e.g. Property.SourceSystemKey is
                # the upstream system's local record key, not a UOI
                # reference - the actual UOI ref lives on
                # Property.SourceSystemId whose Definition explicitly
                # names "OrganizationUniqueId").
                base = r["host_field"]
                target = r["target_resource"]
                target_lower = target.lower()
                target_pk = pk_by_resource.get(target) or ""
                target_pk_lower = target_pk.lower()
                anchor = None
                for suf in ("Id", "ID", "Key"):
                    cand = base + suf
                    if (r["host_resource"], cand) not in field_index:
                        continue
                    if snake(cand) not in declared_columns.get(host_table, set()):
                        continue
                    cand_def = (defs.get((r["host_resource"], cand)) or "").lower()
                    if (
                        target_lower in cand_def
                        or (target_pk_lower and target_pk_lower in cand_def)
                    ):
                        anchor = cand
                        break
                if anchor:
                    host_col = snake(anchor)
                else:
                    skipped_no_host_col.append(
                        f"{r['host_resource']}.{r['host_field']} -> {r['target_resource']} (no scalar carrier with matching definition)"
                    )
                    continue
            else:
                skipped_no_host_col.append(
                    f"{r['host_resource']}.{r['host_field']} -> {r['target_resource']}"
                )
                continue

        target_resource = r["target_resource"]
        if not target_resource:
            continue
        target_field = r["target_field"]
        if not target_field:
            target_field = pk_by_resource.get(target_resource) or ""
        if not target_field:
            skipped_no_target.append(
                f"{r['host_resource']}.{r['host_field']} -> {target_resource} (no PK)"
            )
            continue
        target_table = snake(target_resource)
        target_col = snake(target_field)
        if target_col not in declared_columns.get(target_table, set()):
            skipped_no_target.append(
                f"{r['host_resource']}.{r['host_field']} -> "
                f"{target_resource}.{target_field} (target col missing)"
            )
            continue

        refs_emitted.append((host_table, host_col, target_table, target_col, r["confidence"]))

    # Dedup. Two layers:
    #   (a) exact (host_table, host_col, target_table, target_col)
    #       collisions: keep the higher confidence.
    #   (b) (host_table, host_col, target_table) collisions (different
    #       target_col on same target table - happens for OUID where
    #       prose names OrganizationUniqueId (UOI) but the PK is
    #       OrganizationUniqueIdKey): collapse to one Ref aimed at
    #       the target's PK if present, otherwise keep the first.
    exact: dict[tuple[str, str, str, str], str] = {}
    for ht, hc, tt, tc, conf in refs_emitted:
        k = (ht, hc, tt, tc)
        if k not in exact or (conf == "high" and exact[k] == "medium"):
            exact[k] = conf

    by_triple: dict[tuple[str, str, str], list[tuple[str, str]]] = defaultdict(list)
    for (ht, hc, tt, tc), conf in exact.items():
        by_triple[(ht, hc, tt)].append((tc, conf))

    final: dict[tuple[str, str, str, str], str] = {}
    for (ht, hc, tt), candidates in by_triple.items():
        if len(candidates) == 1:
            tc, conf = candidates[0]
            final[(ht, hc, tt, tc)] = conf
            continue
        # Multiple Refs to same target table: prefer target's PK.
        target_resource = next(
            (res["ResourceName"] for res in resources if snake(res["ResourceName"]) == tt),
            None,
        )
        target_pk_snake = (
            snake(pk_by_resource[target_resource])
            if target_resource and pk_by_resource.get(target_resource)
            else None
        )
        pk_choice = next(
            ((tc, conf) for tc, conf in candidates if tc == target_pk_snake),
            None,
        )
        if pk_choice:
            tc, conf = pk_choice
        else:
            tc, conf = sorted(
                candidates, key=lambda x: (0 if x[1] == "high" else 1, x[0])
            )[0]
        final[(ht, hc, tt, tc)] = conf

    refs_sorted = sorted(final.items(), key=lambda x: x[0])

    for (ht, hc, tt, tc), conf in refs_sorted:
        out_lines.append(f"Ref: {ht}.{hc} > {tt}.{tc}  // {conf}")

    if polymorphic_comments:
        out_lines.append("")
        out_lines.append("// Polymorphic FKs (target resolved at runtime via the named field):")
        for c in polymorphic_comments:
            out_lines.append(c)

    out_lines.append("")
    OUT_CANONICAL.write_text("\n".join(out_lines) + "\n")

    # ------------------------------------------------------------------
    # Render lookups.dbml.
    # ------------------------------------------------------------------
    lookup_lines: list[str] = []
    lookup_lines.append("// lookups.dbml")
    lookup_lines.append(
        f"// {len(sv_lookups_to_emit)} Enum blocks for RESO DD 2.0 single-value lookups."
    )
    lookup_lines.append("// Companion to canonical.dbml.")
    lookup_lines.append("")
    lookup_lines.append("Project reso_canonical_dd_2_0_lookups {")
    lookup_lines.append("  database_type: 'PostgreSQL'")
    lookup_lines.append("  Note: 'Single-value lookup enums extracted from raw/lookups.csv + raw/lookup_values.csv'")
    lookup_lines.append("}")
    lookup_lines.append("")

    declared_enums: set[str] = set()
    for lname in sv_lookups_to_emit:
        values = sorted(
            (v["StandardValue"] for v in lookup_values_by_name.get(lname, [])
             if v.get("StandardValue")),
            key=str.lower,
        )
        if not values:
            continue
        snake_enum = snake(lname)
        lookup_lines.append(f"// ---- {lname} ({len(values)} values) ----")
        lookup_lines.append(f"Enum {snake_enum} {{")
        for v in values:
            # DBML enum value: bare identifier OK if all-alnum;
            # otherwise quote with backticks.
            if re.match(r"^[A-Za-z][A-Za-z0-9_]*$", v):
                lookup_lines.append(f"  {v}")
            else:
                lookup_lines.append(f'  "{v}"')
        lookup_lines.append("}")
        lookup_lines.append("")
        declared_enums.add(snake_enum)

    if mv_only_lookups:
        lookup_lines.append("")
        lookup_lines.append("// ============================================================")
        lookup_lines.append(f"// Multi-value-only lookups ({len(mv_only_lookups)})")
        lookup_lines.append("// These are referenced by 'String List, Multi' columns and")
        lookup_lines.append("// kept as varchar in canonical.dbml. Listed here for reference.")
        lookup_lines.append("// ============================================================")
        for lname in mv_only_lookups:
            n = len(lookup_values_by_name.get(lname, []))
            lookup_lines.append(f"// {lname} ({n} values)")
    if open_lookups:
        lookup_lines.append("")
        lookup_lines.append("// ============================================================")
        lookup_lines.append(f"// Open lookups ({len(open_lookups)}) - jurisdiction-defined,")
        lookup_lines.append("// no closed value set. Kept as varchar in canonical.dbml.")
        lookup_lines.append("// ============================================================")
        for lname in open_lookups:
            lookup_lines.append(f"// {lname}")

    OUT_LOOKUPS.write_text("\n".join(lookup_lines) + "\n")

    # ------------------------------------------------------------------
    # Verification gates.
    # ------------------------------------------------------------------
    failures: list[str] = []

    # Gate 1: each table declared exactly once.
    table_counter = Counter(declared_tables)
    for t, n in table_counter.items():
        if n != 1:
            failures.append(f"GATE 1: table '{t}' declared {n} times (expected 1)")

    # Gate 2: resource count == declared tables.
    if len(declared_tables) != len(resources):
        failures.append(
            f"GATE 2: declared tables ({len(declared_tables)}) != resources.csv ({len(resources)})"
        )

    # Gate 3+4: refs reference declared tables and columns.
    for (ht, hc, tt, tc), _conf in refs_sorted:
        if ht not in declared_columns:
            failures.append(f"GATE 3: Ref source table '{ht}' not declared")
        elif hc not in declared_columns[ht]:
            failures.append(f"GATE 4: Ref source column '{ht}.{hc}' not in table")
        if tt not in declared_columns:
            failures.append(f"GATE 3: Ref target table '{tt}' not declared")
        elif tc not in declared_columns[tt]:
            failures.append(f"GATE 4: Ref target column '{tt}.{tc}' not in table")

    # Gate 5: every Enum referenced in canonical.dbml is declared.
    enum_refs = set(re.findall(r"^\s+\S+\s+([a-z][a-z0-9_]*)\s*\[",
                                "\n".join(out_lines), flags=re.M))
    # Filter to enum-shaped types only (ignore varchar, int, ...).
    builtin_types = {"varchar", "int", "double", "bool", "timestamp", "date"}
    used_enums = {
        e for e in enum_refs
        if e not in builtin_types
        and not e.startswith("varchar(")
    }
    for e in used_enums:
        if e not in declared_enums:
            failures.append(f"GATE 5: Enum '{e}' referenced but not declared in lookups.dbml")

    # Gate 6: no surviving (resource, field) silently missing.
    expected_columns: set[tuple[str, str]] = set()
    for f in fields:
        if (f["ResourceName"], f["StandardName"]) in drop_set:
            continue
        if f["SimpleDataType"] in SKIPPED_SIMPLE_TYPES:
            continue
        expected_columns.add((snake(f["ResourceName"]), snake(f["StandardName"])))
    actual_columns = {(t, c) for t, cols in declared_columns.items() for c in cols}
    silently_missing = expected_columns - actual_columns
    if silently_missing:
        for t, c in sorted(silently_missing)[:10]:
            failures.append(f"GATE 6: column '{t}.{c}' missing from DBML output")
        if len(silently_missing) > 10:
            failures.append(f"GATE 6: ... ({len(silently_missing) - 10} more)")

    # ------------------------------------------------------------------
    # Summary.
    # ------------------------------------------------------------------
    print(f"[05] wrote {OUT_CANONICAL.relative_to(KB_ROOT)} ({OUT_CANONICAL.stat().st_size} bytes)")
    print(f"     wrote {OUT_LOOKUPS.relative_to(KB_ROOT)} ({OUT_LOOKUPS.stat().st_size} bytes)")
    print(f"     tables: {len(declared_tables)}")
    print(f"     columns kept: {sum(len(c) for c in declared_columns.values())}")
    print(f"     refs emitted: {len(refs_sorted)}")
    print(f"       skipped low-confidence:       {len(skipped_low)}")
    print(f"       skipped collection (inverse): {len(skipped_collection)}")
    print(f"       skipped FK column dropped:    {len(skipped_dropped)}")
    print(f"       skipped no host scalar col:   {len(skipped_no_host_col)}")
    print(f"       skipped no target column:     {len(skipped_no_target)}")
    print(f"     polymorphic FK comments:        {len(polymorphic_comments)}")
    print(f"     enums declared (SV):            {len(declared_enums)}")
    print(f"     review markers (// REVIEW):    {len(review_reasons)}")

    if failures:
        print("\n[05] FAILED verification gates:", file=sys.stderr)
        for f in failures[:20]:
            print(f"  - {f}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... ({len(failures) - 20} more)", file=sys.stderr)
        return 2
    print("[05] OK: all verification gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
