#!/usr/bin/env python3
"""
Phase 2.5 Signal A: name-prefix satellite candidates.

Reads:
    raw/fields.csv
    raw/relationships.csv

Writes:
    raw/_satellites_prefix.csv

For every FK in relationships.csv with confidence in {high, medium}
and a non-empty target_resource (polymorphic FKs are skipped),
derive the FK column's stem (StandardName minus trailing Key/Id/ID),
then enumerate every other column on the same host whose
StandardName starts with that stem.

The bare `Resource`-typed companion (e.g. `Property.ListAgent` next
to `Property.ListAgentKey`) is excluded because it IS the typed
inverse of the FK, not a satellite. Other FK columns whose stem
also starts with the same prefix (rare) are excluded.

Output columns:
    host_resource, host_field (the FK), fk_stem, target_resource,
    candidate_satellite, suffix_after_stem, candidate_simple_type

Idempotent: deletes the CSV at the start.

Determinism: rows sorted by
    (host_resource, host_field, candidate_satellite).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_RELS = RAW / "relationships.csv"
OUT = RAW / "_satellites_prefix.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "fk_stem",
    "target_resource",
    "candidate_satellite",
    "suffix_after_stem",
    "candidate_simple_type",
]

KEY_SUFFIX_RE = re.compile(r"^(?P<stem>[A-Z][A-Za-z0-9]+?)(?P<suffix>Key|Id|ID)$")
ACCEPT_CONFIDENCE = {"high", "medium"}


def stem_of(field_name: str) -> str | None:
    m = KEY_SUFFIX_RE.match(field_name)
    return m.group("stem") if m else None


def main() -> int:
    if not IN_FIELDS.exists() or not IN_RELS.exists():
        print("FAIL: fields.csv and relationships.csv must both exist", file=sys.stderr)
        return 2

    fields = list(csv.DictReader(IN_FIELDS.open()))
    rels = list(csv.DictReader(IN_RELS.open()))

    # Index host fields by resource for fast lookup.
    fields_by_resource: dict[str, list[dict]] = {}
    for f in fields:
        fields_by_resource.setdefault(f["ResourceName"], []).append(f)

    # Set of every (resource, field) that is itself an FK column - so
    # we don't flag one FK as another's satellite.
    fk_columns: set[tuple[str, str]] = {
        (r["host_resource"], r["host_field"]) for r in rels
    }

    out_rows: list[dict] = []
    for r in rels:
        if r["confidence"] not in ACCEPT_CONFIDENCE:
            continue
        if not r["target_resource"]:
            # Polymorphic FKs (P5) - skip.
            continue
        host = r["host_resource"]
        fk = r["host_field"]
        target = r["target_resource"]

        stem = stem_of(fk)
        if not stem:
            # FK columns without a Key/Id suffix (e.g. Property.ListAgent
            # which is Resource-typed) don't define a usable prefix.
            continue

        # Enumerate prefix-matched columns on host.
        for cand in fields_by_resource.get(host, []):
            cand_name = cand["StandardName"]
            if cand_name == fk:
                continue
            if not cand_name.startswith(stem):
                continue
            suffix = cand_name[len(stem):]
            if not suffix:
                # Bare typed companion (e.g. ListAgent) - not a satellite.
                continue
            # Skip if the candidate is itself an FK column - we don't
            # want one FK to be flagged as another's satellite.
            if (host, cand_name) in fk_columns:
                continue
            out_rows.append(
                {
                    "host_resource": host,
                    "host_field": fk,
                    "fk_stem": stem,
                    "target_resource": target,
                    "candidate_satellite": cand_name,
                    "suffix_after_stem": suffix,
                    "candidate_simple_type": cand["SimpleDataType"],
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
    from collections import Counter
    by_host = Counter(r["host_resource"] for r in out_rows)
    print(f"[04a] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} candidate rows)")
    print(f"      across {len(by_host)} host resources")
    print(f"      top hosts by candidate count:")
    for h, c in by_host.most_common(8):
        print(f"        {h:25s} {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
