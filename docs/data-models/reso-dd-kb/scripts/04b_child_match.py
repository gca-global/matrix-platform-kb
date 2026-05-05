#!/usr/bin/env python3
"""
Phase 2.5 Signal B: child-side column match.

Reads:
    raw/fields.csv
    raw/_satellites_prefix.csv (Signal A output)

Writes:
    raw/_satellites_child_match.csv

For each candidate from Signal A, look for a column on
target_resource named (priority order):

    1. <target><suffix>          score 1.0  (e.g. MemberFirstName)
    2. <target_singular><suffix> score 1.0  (TeamMembers -> TeamMember,
                                              Contacts   -> Contact)
    3. <suffix>                  score 0.9  (bare; rare in DD 2.0)
    4. case-folded variants of any of the above  score 0.8
    5. underscore-stripped match of any of the above  score 0.7

The first non-zero score wins. Rows with no match are still emitted
so the merge step can see Signal B = 0; they're useful for the
"keep_both" / "review" decisions.

Output columns:
    host_resource, host_field, target_resource, candidate_satellite,
    suffix_after_stem, target_field, name_match_score, match_kind

Idempotent. Determinism: rows sorted by
(host_resource, host_field, candidate_satellite).
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_PREFIX = RAW / "_satellites_prefix.csv"
OUT = RAW / "_satellites_child_match.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "target_resource",
    "candidate_satellite",
    "suffix_after_stem",
    "target_field",
    "name_match_score",
    "match_kind",
]


def main() -> int:
    if not IN_FIELDS.exists() or not IN_PREFIX.exists():
        print("FAIL: fields.csv and _satellites_prefix.csv must both exist", file=sys.stderr)
        return 2

    fields = list(csv.DictReader(IN_FIELDS.open()))
    target_fields_by_res: dict[str, set[str]] = {}
    target_fields_lower: dict[str, dict[str, str]] = {}
    for f in fields:
        target_fields_by_res.setdefault(f["ResourceName"], set()).add(f["StandardName"])
    for res, names in target_fields_by_res.items():
        target_fields_lower[res] = {n.lower(): n for n in names}

    out_rows: list[dict] = []
    for r in csv.DictReader(IN_PREFIX.open()):
        target = r["target_resource"]
        suffix = r["suffix_after_stem"]
        names = target_fields_by_res.get(target, set())

        target_singular = target[:-1] if target.endswith("s") else target

        # Build candidate target-field names in priority order.
        attempts: list[tuple[str, float, str]] = [
            (target + suffix, 1.0, "target_prefix"),
            (target_singular + suffix, 1.0, "target_singular_prefix"),
            (suffix, 0.9, "bare_suffix"),
        ]

        target_field = ""
        score = 0.0
        match_kind = ""
        for cand, base_score, kind in attempts:
            if cand in names:
                target_field, score, match_kind = cand, base_score, kind
                break
            cf = target_fields_lower.get(target, {}).get(cand.lower())
            if cf:
                target_field, score, match_kind = cf, base_score - 0.2, kind + "_casefold"
                break
            cand_strip = cand.replace("_", "")
            for n in names:
                if n.replace("_", "").lower() == cand_strip.lower():
                    target_field, score, match_kind = n, base_score - 0.3, kind + "_underscore"
                    break
            if target_field:
                break

        out_rows.append(
            {
                "host_resource": r["host_resource"],
                "host_field": r["host_field"],
                "target_resource": target,
                "candidate_satellite": r["candidate_satellite"],
                "suffix_after_stem": suffix,
                "target_field": target_field,
                "name_match_score": f"{score:.2f}",
                "match_kind": match_kind or "no_match",
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
    matched = sum(1 for r in out_rows if r["match_kind"] != "no_match")
    by_kind = Counter(r["match_kind"] for r in out_rows)
    print(f"[04b] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows; {matched} matched)")
    for k in sorted(by_kind):
        print(f"      {k}: {by_kind[k]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
