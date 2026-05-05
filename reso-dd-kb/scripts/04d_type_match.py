#!/usr/bin/env python3
"""
Phase 2.5 Signal D: SimpleDataType + Lookup match.

Reads:
    raw/fields.csv
    raw/_satellites_child_match.csv (Signal B output, for the
        candidate <-> target_field pairs)

Writes:
    raw/_satellites_type.csv

For each (host_resource, candidate_satellite) <-> (target_resource,
target_field) pair:

    - SimpleDataType match: 1 if both cells are equal, 0 otherwise.
    - Lookup match: 1 if both cells are equal (including both empty),
                    0 otherwise. The "both empty" case is the most
                    common - it just means neither column is enum-
                    typed - and counts as a match for our purposes.

`type_match` final score:
    1.0  - both SimpleDataType AND Lookup match
    0.5  - SimpleDataType matches, Lookup differs
    0.0  - SimpleDataType differs (Lookup is then irrelevant)

Output columns:
    host_resource, host_field, candidate_satellite,
    target_resource, target_field, host_simple_type, target_simple_type,
    host_lookup, target_lookup, type_match, simple_type_match,
    lookup_match
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_CHILD = RAW / "_satellites_child_match.csv"
OUT = RAW / "_satellites_type.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "candidate_satellite",
    "target_resource",
    "target_field",
    "host_simple_type",
    "target_simple_type",
    "host_lookup",
    "target_lookup",
    "type_match",
    "simple_type_match",
    "lookup_match",
]


def main() -> int:
    if not IN_FIELDS.exists() or not IN_CHILD.exists():
        print("FAIL: fields.csv and _satellites_child_match.csv must both exist", file=sys.stderr)
        return 2

    field_index: dict[tuple[str, str], dict] = {
        (r["ResourceName"], r["StandardName"]): r
        for r in csv.DictReader(IN_FIELDS.open())
    }

    out_rows: list[dict] = []
    for r in csv.DictReader(IN_CHILD.open()):
        target_field = r["target_field"]
        if not target_field:
            continue
        host_row = field_index.get((r["host_resource"], r["candidate_satellite"]))
        tgt_row = field_index.get((r["target_resource"], target_field))
        if not host_row or not tgt_row:
            # Should never happen because Signal B already validated
            # both ends; if it does, skip rather than crash.
            continue

        h_type = host_row["SimpleDataType"]
        t_type = tgt_row["SimpleDataType"]
        h_lookup = host_row["Lookup"]
        t_lookup = tgt_row["Lookup"]

        type_eq = 1 if h_type == t_type else 0
        lookup_eq = 1 if h_lookup == t_lookup else 0
        if type_eq and lookup_eq:
            score = 1.0
        elif type_eq:
            score = 0.5
        else:
            score = 0.0

        out_rows.append(
            {
                "host_resource": r["host_resource"],
                "host_field": r["host_field"],
                "candidate_satellite": r["candidate_satellite"],
                "target_resource": r["target_resource"],
                "target_field": target_field,
                "host_simple_type": h_type,
                "target_simple_type": t_type,
                "host_lookup": h_lookup,
                "target_lookup": t_lookup,
                "type_match": f"{score:.1f}",
                "simple_type_match": type_eq,
                "lookup_match": lookup_eq,
            }
        )

    out_rows.sort(
        key=lambda r: (r["host_resource"], r["host_field"], r["candidate_satellite"])
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=OUT_COLUMNS, quoting=csv.QUOTE_MINIMAL, lineterminator="\n"
        )
        w.writeheader()
        for r in out_rows:
            w.writerow(r)

    # Summary
    full = sum(1 for r in out_rows if float(r["type_match"]) == 1.0)
    half = sum(1 for r in out_rows if float(r["type_match"]) == 0.5)
    none = sum(1 for r in out_rows if float(r["type_match"]) == 0.0)
    print(f"[04d] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    print(f"      type+lookup match (1.0): {full}")
    print(f"      type only      (0.5): {half}")
    print(f"      no match       (0.0): {none}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
