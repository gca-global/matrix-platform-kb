#!/usr/bin/env python3
"""
Phase 2.5: merge the four signal CSVs into raw/satellites.csv.

Reads:
    raw/fields.csv
    raw/relationships.csv
    raw/_satellites_prefix.csv      (Signal A)
    raw/_satellites_child_match.csv (Signal B)
    raw/_satellites_definition.csv  (Signal C)
    raw/_satellites_type.csv        (Signal D)

Writes:
    raw/satellites.csv

One row per (host_resource, host_field, candidate_satellite) triple
that survived Signal A. Recommendation rules:

    drop_from_host
        Signal A fires (always; A is the gate)
        AND Signal B name_match_score >= 0.7
        AND Signal C jaccard >= jaccard_threshold (0.7 for *Id /
            *Key / *NationalAssociationId / *LoginId / *MlsId
            identifier columns; 0.6 for everything else)
        AND Signal D type_match >= 0.5

    review
        Either:
          - Signal B + C + D fire but jaccard in [0.4, jaccard_threshold), OR
          - Signal B fires AND C >= 0.6 AND D = 0.5 (lookup
            differs)
        i.e. the candidate clearly relates to the target column but
        one of the strong signals is weak.

    keep_both
        Anything else (Signal B unmatched, or jaccard < 0.4, or
        type mismatch).

    drop_from_child
        NOT auto-emitted; reserved for human override (left for a
        future overrides file).

Verification gates (hard-fail):
    1. (host_resource, host_field) in fields.csv
    2. (host_resource, candidate_satellite) in fields.csv
    3. (target_resource, target_field) in fields.csv (when target
       fields are non-empty)
    4. (host_resource, host_field=fk, target_resource) is in
       relationships.csv with confidence in {high, medium}
    5. recommendation in {drop_from_host, drop_from_child,
       keep_both, review}

Determinism: rows sorted by
    (host_resource, host_field, candidate_satellite).
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_RELS = RAW / "relationships.csv"
IN_PREFIX = RAW / "_satellites_prefix.csv"
IN_CHILD = RAW / "_satellites_child_match.csv"
IN_DEF = RAW / "_satellites_definition.csv"
IN_TYPE = RAW / "_satellites_type.csv"
OUT = RAW / "satellites.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "fk_stem",
    "candidate_satellite",
    "candidate_simple_type",
    "target_resource",
    "target_field",
    "name_match_score",
    "name_match_kind",
    "jaccard",
    "type_match",
    "lookup_match",
    "signals_fired",
    "recommendation",
    "notes",
]

VALID_RECOMMENDATIONS = {"drop_from_host", "drop_from_child", "keep_both", "review"}
ACCEPT_FK_CONFIDENCE = {"high", "medium"}

# Identifier-style suffixes use a tighter Jaccard threshold to limit
# false positives where the host intentionally denormalises an
# identifier (e.g. ListAgentMlsId) with a definition that happens to
# look generic.
ID_SUFFIXES = ("Key", "Id", "ID", "MlsId", "LoginId", "NationalAssociationId")


def must_exist(p: Path) -> None:
    if not p.exists():
        print(f"FAIL: required input missing: {p}", file=sys.stderr)
        raise SystemExit(2)


def load_csv(p: Path) -> list[dict]:
    return list(csv.DictReader(p.open()))


def jaccard_threshold_for(suffix: str) -> float:
    return 0.7 if suffix in ID_SUFFIXES else 0.6


def main() -> int:
    for p in (IN_FIELDS, IN_RELS, IN_PREFIX, IN_CHILD, IN_DEF, IN_TYPE):
        must_exist(p)

    fields = load_csv(IN_FIELDS)
    rels = load_csv(IN_RELS)
    prefix = load_csv(IN_PREFIX)
    child = load_csv(IN_CHILD)
    defs = load_csv(IN_DEF)
    typm = load_csv(IN_TYPE)

    field_set: set[tuple[str, str]] = {(f["ResourceName"], f["StandardName"]) for f in fields}

    # FKs in relationships.csv keyed by (host, field, target), filtered
    # to the confidences we accept.
    accepted_fks: set[tuple[str, str, str]] = set()
    for r in rels:
        if r["confidence"] in ACCEPT_FK_CONFIDENCE and r["target_resource"]:
            accepted_fks.add((r["host_resource"], r["host_field"], r["target_resource"]))

    # Index intermediate signals by (host, host_field, candidate_satellite).
    def by_key(rows: list[dict]) -> dict[tuple[str, str, str], dict]:
        return {
            (r["host_resource"], r["host_field"], r["candidate_satellite"]): r
            for r in rows
        }

    child_idx = by_key(child)
    def_idx = by_key(defs)
    type_idx = by_key(typm)

    out_rows: list[dict] = []
    for p in prefix:
        key = (p["host_resource"], p["host_field"], p["candidate_satellite"])
        c = child_idx.get(key, {})
        d = def_idx.get(key, {})
        t = type_idx.get(key, {})

        target_resource = p["target_resource"]
        target_field = c.get("target_field", "") or ""
        name_score = float(c.get("name_match_score") or 0.0)
        name_kind = c.get("match_kind", "") or ""
        jaccard = float(d.get("jaccard") or 0.0) if target_field else 0.0
        type_match = float(t.get("type_match") or 0.0) if target_field else 0.0
        lookup_match = int(t.get("lookup_match") or 0) if target_field else 0

        # Signals fired:
        signals: list[str] = []
        if True:
            signals.append("A")  # prefix shape - always present (this is the gate).
        if name_score >= 0.7:
            signals.append("B")
        if jaccard >= 0.6:
            signals.append("C")
        if type_match >= 0.5:
            signals.append("D")

        suffix = p["suffix_after_stem"]
        jthresh = jaccard_threshold_for(suffix)

        notes_bits: list[str] = []
        if not target_field:
            recommendation = "keep_both"
            notes_bits.append("no_child_match")
        elif "B" in signals and "C" in signals and "D" in signals:
            if jaccard >= jthresh and type_match >= 0.5:
                recommendation = "drop_from_host"
                if jthresh > 0.6:
                    notes_bits.append(f"id_suffix_threshold_{jthresh}")
            else:
                recommendation = "review"
                notes_bits.append(f"jaccard_{jaccard:.2f}_below_id_threshold_{jthresh}")
        elif "B" in signals and "C" in signals and type_match == 0.5:
            recommendation = "review"
            notes_bits.append("lookup_differs")
        elif "B" in signals and 0.4 <= jaccard < 0.6:
            recommendation = "review"
            notes_bits.append("borderline_jaccard")
        elif "B" in signals and "D" in signals and jaccard < 0.4:
            # Names match exactly + types match, but Definition prose
            # diverges enough that we cannot auto-trust drop. The
            # canonical case is OfficeBrokerMlsId on Office: the
            # column literally IS Member.MemberMlsId per the Office
            # row's prose ("The MemberMlsId of the responsible /
            # owning broker"), but the target's prose is the full
            # MlsId boilerplate. Flag for human review.
            recommendation = "review"
            notes_bits.append("name_type_match_but_definitions_differ")
        else:
            recommendation = "keep_both"
            if not signals or signals == ["A"]:
                notes_bits.append("only_prefix_signal")

        out_rows.append(
            {
                "host_resource": p["host_resource"],
                "host_field": p["host_field"],
                "fk_stem": p["fk_stem"],
                "candidate_satellite": p["candidate_satellite"],
                "candidate_simple_type": p["candidate_simple_type"],
                "target_resource": target_resource,
                "target_field": target_field,
                "name_match_score": f"{name_score:.2f}",
                "name_match_kind": name_kind,
                "jaccard": f"{jaccard:.3f}",
                "type_match": f"{type_match:.1f}",
                "lookup_match": lookup_match,
                "signals_fired": "|".join(signals),
                "recommendation": recommendation,
                "notes": ";".join(notes_bits),
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

    # ---- verification gates ------------------------------------------------
    failures: list[str] = []
    for r in out_rows:
        host = r["host_resource"]
        if (host, r["host_field"]) not in field_set:
            failures.append(f"GATE 1: host_field {host}.{r['host_field']} not in fields.csv")
        if (host, r["candidate_satellite"]) not in field_set:
            failures.append(f"GATE 2: candidate {host}.{r['candidate_satellite']} not in fields.csv")
        if r["target_field"] and (r["target_resource"], r["target_field"]) not in field_set:
            failures.append(
                f"GATE 3: target {r['target_resource']}.{r['target_field']} not in fields.csv"
            )
        if (host, r["host_field"], r["target_resource"]) not in accepted_fks:
            failures.append(
                f"GATE 4: FK {host}.{r['host_field']} -> {r['target_resource']} "
                f"not in relationships.csv with confidence in {sorted(ACCEPT_FK_CONFIDENCE)}"
            )
        if r["recommendation"] not in VALID_RECOMMENDATIONS:
            failures.append(
                f"GATE 5: recommendation '{r['recommendation']}' not in "
                f"{sorted(VALID_RECOMMENDATIONS)}"
            )

    # ---- summary -----------------------------------------------------------
    print(f"[04_merge] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    print(f"[04_merge] recommendation histogram:")
    for rec, n in Counter(r["recommendation"] for r in out_rows).most_common():
        print(f"           {rec:<20s} {n}")

    # Distinct hosts/FKs touched.
    distinct_hosts = {r["host_resource"] for r in out_rows}
    distinct_fks = {(r["host_resource"], r["host_field"]) for r in out_rows}
    print(f"[04_merge] distinct host resources: {len(distinct_hosts)}")
    print(f"[04_merge] distinct FK (host, host_field): {len(distinct_fks)}")
    drops = sum(1 for r in out_rows if r["recommendation"] == "drop_from_host")
    reviews = sum(1 for r in out_rows if r["recommendation"] == "review")
    print(f"[04_merge] -> Phase 3 will drop {drops} columns once human signs off")
    print(f"[04_merge] -> {reviews} additional rows need human review")

    if failures:
        print("\n[04_merge] FAILED verification gates:", file=sys.stderr)
        for f in failures[:20]:
            print(f"  - {f}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... ({len(failures) - 20} more)", file=sys.stderr)
        return 2
    print("[04_merge] OK: all verification gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
