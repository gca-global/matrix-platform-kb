#!/usr/bin/env python3
"""
Extract FK signals from SimpleDataType.

Reads:
    raw/fields.csv
    raw/resources.csv  (so we can flag targets that don't exist)

Writes:
    raw/_signals_type.csv

Two type-derived signal kinds:

    Resource     SimpleDataType == 'Resource'.   The host field is a
                 many-to-one FK to <SourceResource>. If SourceResource
                 is empty (12 of 89 fields), we leave target empty
                 here and let the merge step fall back to name-shape.

    Collection   SimpleDataType == 'Collection'. The host carries no
                 column; the FK lives on the child resource named in
                 SourceResource. Collection rows are informational
                 for Phase 3 (they tell us where to expect the
                 matching child-side FK).

Idempotent: deletes _signals_type.csv at the start.

Determinism: rows sorted by (host_resource, host_field).
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_RESOURCES = RAW / "resources.csv"
OUT = RAW / "_signals_type.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "signal_kind",   # resource_typed | collection_typed
    "target_resource",
    "source_resource_cell",  # raw value of SourceResource cell (for audit)
    "lookup_cell",           # raw value of Lookup cell (for audit)
    "target_resource_known",  # 1 if target exists in resources.csv, 0 if not
    "notes",
]


def main() -> int:
    if not IN_FIELDS.exists():
        print(f"FAIL: {IN_FIELDS} missing - run 02_parse_mirror.py first", file=sys.stderr)
        return 2
    if not IN_RESOURCES.exists():
        print(f"FAIL: {IN_RESOURCES} missing", file=sys.stderr)
        return 2

    known_resources: set[str] = {
        row["ResourceName"] for row in csv.DictReader(IN_RESOURCES.open())
    }

    out_rows: list[dict] = []
    with IN_FIELDS.open() as fh:
        for row in csv.DictReader(fh):
            t = row["SimpleDataType"]
            if t not in ("Resource", "Collection"):
                continue
            sr = row["SourceResource"].strip()
            target = sr if sr else ""
            kind = "resource_typed" if t == "Resource" else "collection_typed"
            target_known = 1 if (target and target in known_resources) else 0
            notes_bits: list[str] = []
            if not target:
                notes_bits.append("source_resource_missing")
            elif not target_known:
                notes_bits.append(f"target_not_in_resources_csv:{target}")
            out_rows.append(
                {
                    "host_resource": row["ResourceName"],
                    "host_field": row["StandardName"],
                    "signal_kind": kind,
                    "target_resource": target,
                    "source_resource_cell": sr,
                    "lookup_cell": row["Lookup"],
                    "target_resource_known": target_known,
                    "notes": ";".join(notes_bits) if notes_bits else "",
                }
            )

    out_rows.sort(key=lambda r: (r["host_resource"], r["host_field"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=OUT_COLUMNS, quoting=csv.QUOTE_MINIMAL, lineterminator="\n"
        )
        w.writeheader()
        for r in out_rows:
            w.writerow(r)

    # Summary
    from collections import Counter
    by_kind = Counter(r["signal_kind"] for r in out_rows)
    missing_sr = sum(1 for r in out_rows if not r["target_resource"])
    unknown_target = sum(
        1 for r in out_rows
        if r["target_resource"] and not r["target_resource_known"]
    )

    print(f"[03b] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    for k in sorted(by_kind):
        print(f"      {k}: {by_kind[k]} rows")
    print(f"      SourceResource cell empty: {missing_sr} (will fall back to name-shape)")
    print(f"      target named but not in resources.csv: {unknown_target}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
