#!/usr/bin/env python3
"""
Join the three inventories with the curated mapping CSV and the
canonical RESO DD 2.0 fields/lookups, emitting one alignment CSV per
in-scope RESO resource.

Reads:
  raw/dash_inventory.csv
  raw/qobrix_inventory.csv
  raw/cbp_inventory.csv
  raw/mapping_curated.csv             (HAND-EDITED - the human judgement layer)
  ../reso-dd-kb/raw/fields.csv
  ../reso-dd-kb/raw/field_definitions.csv
  ../reso-dd-kb/raw/lookup_values.csv

Writes:
  raw/alignment_property.csv
  raw/alignment_member.csv
  raw/alignment_office.csv
  raw/alignment_contacts.csv
  raw/alignment_teams.csv
  raw/alignment_media.csv

Hard-fail gates (exit non-zero on breach; do NOT relax):

  1. Every mapping_curated.csv row's reso_field exists in
     reso-dd-kb/raw/fields.csv for the matching reso_resource, OR
     is_extension=true AND reso_field starts with 'x_sm_'.
  2. Every non-empty dash_label cited in mapping_curated.csv exists
     in dash_inventory.csv.
  3. Every non-empty (qobrix_schema, qobrix_path) pair cited in
     mapping_curated.csv exists in qobrix_inventory.csv.
  4. Every non-empty sir_label cited in mapping_curated.csv exists
     in cbp_inventory.csv.
  5. Every value_mapping_json mapping target value exists in the
     corresponding RESO lookup (lookup_values.csv) when the field
     has a closed Lookup.

Phase: Join (mechanical, deterministic).
Owner: scripts/04_join_alignment.py - do NOT hand-edit raw/alignment_*.csv.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RESO_RAW = KB_ROOT.parent / "reso-dd-kb" / "raw"
RAW = KB_ROOT / "raw"

IN_SCOPE_RESOURCES = ["Property", "Member", "Office", "Contacts", "Teams", "Media"]

ALIGN_COLUMNS = [
    "reso_field",
    "reso_definition",
    "reso_lookup",
    "reso_data_type",
    "is_extension",
    "dash_form",
    "dash_label",
    "qobrix_schema",
    "qobrix_path",
    "sir_label",
    "value_mapping_json",
    "confidence",
    "has_dash",
    "has_qobrix",
    "has_sir",
    "notes",
]


def load_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    # Load inventories
    dash_rows = load_csv(RAW / "dash_inventory.csv")
    qobrix_rows = load_csv(RAW / "qobrix_inventory.csv")
    cbp_rows = load_csv(RAW / "cbp_inventory.csv")
    curated = load_csv(RAW / "mapping_curated.csv")

    # Load reso-dd-kb refs
    reso_fields_raw = load_csv(RESO_RAW / "fields.csv")
    reso_field_defs = load_csv(RESO_RAW / "field_definitions.csv")
    reso_lookup_values = load_csv(RESO_RAW / "lookup_values.csv")

    # Index RESO fields by (Resource, StandardName)
    reso_fields: dict[tuple[str, str], dict] = {}
    for fr in reso_fields_raw:
        reso_fields[(fr["ResourceName"], fr["StandardName"])] = fr
    # Definitions
    reso_defs: dict[tuple[str, str], str] = {}
    for fd in reso_field_defs:
        reso_defs[(fd["ResourceName"], fd["StandardName"])] = fd.get("Definition", "")
    # Lookup values: Lookup -> set of standard values
    reso_lookup_set: dict[str, set[str]] = {}
    for lv in reso_lookup_values:
        reso_lookup_set.setdefault(lv["LookupName"], set()).add(lv["StandardValue"])

    # Inventory indexes for fast existence checks
    dash_label_set: set[str] = {
        r["field_label"] for r in dash_rows if r["kind"] == "field"
    }
    qobrix_path_set: set[tuple[str, str]] = {
        (r["schema"], r["property_path"]) for r in qobrix_rows
    }
    sir_label_set: set[str] = {
        r["step_label"] for r in cbp_rows if r["kind"] in ("field", "step")
    }

    # ====== HARD-FAIL GATES ======
    errors: list[str] = []

    for i, c in enumerate(curated, start=2):  # +2 for header + 1-based
        res = c["reso_resource"]
        fld = c["reso_field"]
        is_ext = c["is_extension"].strip().lower() == "true"

        # Gate 1: reso_field exists OR is x_sm_ extension
        if is_ext:
            if not fld.startswith("x_sm_"):
                errors.append(
                    f"GATE 1 line {i}: extension reso_field {fld!r} must start with 'x_sm_' (resource={res})"
                )
        else:
            if (res, fld) not in reso_fields:
                errors.append(
                    f"GATE 1 line {i}: reso_field {res}.{fld} not in reso-dd-kb/raw/fields.csv"
                )

        # Gate 2: dash_label exists
        if c["dash_label"] and c["dash_label"] not in dash_label_set:
            errors.append(
                f"GATE 2 line {i}: dash_label {c['dash_label']!r} not in dash_inventory.csv (form column {c['dash_form']!r})"
            )

        # Gate 3: (qobrix_schema, qobrix_path) exists
        if c["qobrix_path"]:
            schema = c["qobrix_schema"] or ""
            path = c["qobrix_path"]
            if (schema, path) not in qobrix_path_set:
                errors.append(
                    f"GATE 3 line {i}: qobrix {schema}/{path} not in qobrix_inventory.csv"
                )

        # Gate 4: sir_label exists
        if c["sir_label"] and c["sir_label"] not in sir_label_set:
            errors.append(
                f"GATE 4 line {i}: sir_label {c['sir_label']!r} not in cbp_inventory.csv"
            )

        # Gate 5: value_mapping_json targets exist in the RESO lookup
        if c["value_mapping_json"] and not is_ext:
            try:
                vmap = json.loads(c["value_mapping_json"])
            except json.JSONDecodeError as exc:
                errors.append(
                    f"GATE 5 line {i}: value_mapping_json invalid JSON for {res}.{fld}: {exc}"
                )
                continue
            field_meta = reso_fields.get((res, fld))
            lookup_name = (field_meta or {}).get("Lookup", "")
            if lookup_name and lookup_name in reso_lookup_set:
                for src_val, target_val in vmap.items():
                    if target_val not in reso_lookup_set[lookup_name]:
                        errors.append(
                            f"GATE 5 line {i}: {res}.{fld} value_mapping target "
                            f"{target_val!r} (from {src_val!r}) is not a "
                            f"StandardValue in lookup {lookup_name!r}"
                        )

    if errors:
        print(
            f"04_join_alignment.py: {len(errors)} hard-fail gate violation(s):",
            file=sys.stderr,
        )
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        print(
            "\nFix the rows above in raw/mapping_curated.csv (or rerun the "
            "01..03 inventory scripts if upstream sources changed) and try "
            "again. Do NOT relax the gates.",
            file=sys.stderr,
        )
        return 1

    # ====== Emit per-resource alignment CSVs ======
    grouped: dict[str, list[dict]] = {res: [] for res in IN_SCOPE_RESOURCES}
    for c in curated:
        res = c["reso_resource"]
        if res not in grouped:
            print(
                f"WARN: curated row references out-of-scope resource {res!r}; "
                f"add it to IN_SCOPE_RESOURCES if intentional.",
                file=sys.stderr,
            )
            continue

        is_ext = c["is_extension"].strip().lower() == "true"
        fld = c["reso_field"]
        field_meta = reso_fields.get((res, fld), {})

        out_row = {
            "reso_field": fld,
            "reso_definition": "" if is_ext else reso_defs.get((res, fld), ""),
            "reso_lookup": "" if is_ext else field_meta.get("Lookup", ""),
            "reso_data_type": "" if is_ext else field_meta.get("SimpleDataType", ""),
            "is_extension": "true" if is_ext else "false",
            "dash_form": c["dash_form"],
            "dash_label": c["dash_label"],
            "qobrix_schema": c["qobrix_schema"],
            "qobrix_path": c["qobrix_path"],
            "sir_label": c["sir_label"],
            "value_mapping_json": c["value_mapping_json"],
            "confidence": c["confidence"],
            "has_dash": "yes" if c["dash_label"] else "no",
            "has_qobrix": "yes" if c["qobrix_path"] else "no",
            "has_sir": "yes" if c["sir_label"] else "no",
            "notes": c["notes"],
        }
        grouped[res].append(out_row)

    summary: list[tuple[str, int, int]] = []
    for res, rows in grouped.items():
        rows.sort(key=lambda r: (r["is_extension"], r["reso_field"]))
        out_path = RAW / f"alignment_{res.lower()}.csv"
        with out_path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=ALIGN_COLUMNS, quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            writer.writerows(rows)
        ext_count = sum(1 for r in rows if r["is_extension"] == "true")
        summary.append((res, len(rows), ext_count))

    print("[04] join_alignment: 5/5 hard-fail gates passed.")
    for res, total, exts in summary:
        print(f"     {res}: {total} rows ({exts} extensions) -> raw/alignment_{res.lower()}.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
