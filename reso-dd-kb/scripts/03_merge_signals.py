#!/usr/bin/env python3
"""
Merge the three Phase-2 signal CSVs into raw/relationships.csv.

Reads:
    raw/fields.csv             (host_field validation)
    raw/resources.csv          (target validation)
    raw/_signals_definition.csv  (P1..P7 + P3b)
    raw/_signals_type.csv        (resource_typed | collection_typed)
    raw/_signals_name.csv        (exact_stem | tail_stem | self_stem)

Writes:
    raw/relationships.csv

One row per (host_resource, host_field, target_resource) triple. The
target_field is filled in the priority order:
    1. definition prose strong patterns (P1, P2, P4, P6) - they
       capture the column verbatim;
    2. type signal: target's PK column (canonical: <Target>Key);
    3. name signal: target_pk_column (<Target>Key);
    4. polymorphic (P5): empty.

fk_kind is the strongest contributor in priority order:
    resource_typed > collection_typed > prose > name_shape

confidence is set per the rules in methodology.md.

Verification gates (hard-fail at the end):
    1. target_resource (when non-empty) must exist in resources.csv.
    2. (host_resource, host_field) must exist in fields.csv.
    3. fk_kind must be one of the four enums.
    4. confidence must be high|medium|low.
    5. All three intermediate _signals_*.csv files must exist.

Determinism:
    Rows sorted by (host_resource, host_field, target_resource).
    Stable column order. csv.QUOTE_MINIMAL, lf line endings.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_RESOURCES = RAW / "resources.csv"
IN_SIG_DEF = RAW / "_signals_definition.csv"
IN_SIG_TYPE = RAW / "_signals_type.csv"
IN_SIG_NAME = RAW / "_signals_name.csv"
OUT = RAW / "relationships.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "host_field_type",
    "target_resource",
    "target_field",
    "fk_kind",
    "confidence",
    "evidence",
    "notes",
]

VALID_FK_KIND = {"resource_typed", "collection_typed", "prose", "name_shape"}
VALID_CONFIDENCE = {"high", "medium", "low"}

# Strong prose patterns name both target and column.
STRONG_PROSE_PATTERNS = {"P1", "P2", "P4", "P6"}
# Medium prose patterns name target only or are polymorphic.
MEDIUM_PROSE_PATTERNS = {"P3", "P3b", "P7", "P5"}
# P5b is a polymorphic marker (not an FK on its own; it demotes any
# other FK we found for the same field to a polymorphic comment).
POLY_MARKER_PATTERN = "P5b"


def must_exist(path: Path) -> None:
    if not path.exists():
        print(f"FAIL: required input missing: {path}", file=sys.stderr)
        raise SystemExit(2)


def load_csv(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    for p in (IN_FIELDS, IN_RESOURCES, IN_SIG_DEF, IN_SIG_TYPE, IN_SIG_NAME):
        must_exist(p)

    fields = load_csv(IN_FIELDS)
    resources_set: set[str] = {r["ResourceName"] for r in load_csv(IN_RESOURCES)}
    sig_def = load_csv(IN_SIG_DEF)
    sig_type = load_csv(IN_SIG_TYPE)
    sig_name = load_csv(IN_SIG_NAME)

    # Index host fields for type lookup.
    host_field_index: dict[tuple[str, str], dict] = {
        (f["ResourceName"], f["StandardName"]): f for f in fields
    }
    # Set of every (resource, field) pair, used to validate that an
    # inferred target_field actually exists on its target resource.
    field_set: set[tuple[str, str]] = set(host_field_index.keys())

    def target_field_exists(target_resource: str, target_field: str) -> bool:
        if not target_resource or not target_field:
            return False
        return (target_resource, target_field) in field_set

    # Group all signals by (host_resource, host_field).
    grouped: dict[tuple[str, str], dict] = defaultdict(
        lambda: {
            "prose_strong": [],   # list of (target_res, target_col, pattern, matched)
            "prose_medium": [],   # list of (target_res, target_col, pattern, matched)
            "prose_poly": [],     # list of (matched,)
            "poly_marker": [],    # list of (matched,) - P5b
            "type": [],           # list of (kind, target_res)
            "name": [],           # list of (target_res, target_col, match_kind, stem)
        }
    )

    for r in sig_def:
        key = (r["host_resource"], r["host_field"])
        bucket = grouped[key]
        pid = r["pattern_id"]
        target = r["target_resource"]
        col = r["target_field"]
        if pid in STRONG_PROSE_PATTERNS:
            bucket["prose_strong"].append((target, col, pid, r["matched"]))
        elif pid == "P5":
            bucket["prose_poly"].append((r["matched"],))
        elif pid == POLY_MARKER_PATTERN:
            bucket["poly_marker"].append((r["matched"],))
        elif pid in MEDIUM_PROSE_PATTERNS:
            bucket["prose_medium"].append((target, col, pid, r["matched"]))

    for r in sig_type:
        key = (r["host_resource"], r["host_field"])
        grouped[key]["type"].append((r["signal_kind"], r["target_resource"]))

    for r in sig_name:
        key = (r["host_resource"], r["host_field"])
        grouped[key]["name"].append(
            (
                r["target_resource"],
                r["target_pk_column"],
                r["match_kind"],
                r["stem"],
            )
        )

    out_rows: list[dict] = []

    # Iterate every host (host_resource, host_field) that produced any
    # signal. For each, emit one or more (target_resource) rows.
    for (host, field), b in sorted(grouped.items()):
        host_field_row = host_field_index.get((host, field))
        host_field_type = host_field_row["SimpleDataType"] if host_field_row else ""

        # If the field is flagged as polymorphic by P5b, demote every
        # concrete FK we found for it to a single polymorphic comment.
        # (We still want the comment for reviewers; we just don't want
        # to emit a wrong-looking concrete Ref in the DBML.)
        if b["poly_marker"]:
            for (matched,) in b["poly_marker"]:
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "host_field_type": host_field_type,
                        "target_resource": "",
                        "target_field": "",
                        "fk_kind": "prose",
                        "confidence": "medium",
                        "evidence": f'prose:P5b:"{matched}"',
                        "notes": "polymorphic",
                    }
                )
            # Skip the per-target emission for this field; we still
            # process polymorphic P5 hits below for record-keeping.
            for (matched,) in b["prose_poly"]:
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "host_field_type": host_field_type,
                        "target_resource": "",
                        "target_field": "",
                        "fk_kind": "prose",
                        "confidence": "medium",
                        "evidence": f'prose:P5:"{matched}"',
                        "notes": "polymorphic",
                    }
                )
            continue

        # Bucket by target_resource. Collect every signal contributing
        # to that target.
        per_target: dict[str, dict] = defaultdict(
            lambda: {
                "fk_kinds": set(),
                "evidence": [],
                "target_field_candidates": [],
                "is_collection": False,
                "is_self_pk": False,
                "name_match_kinds": set(),
                "prose_strong_seen": False,
                "prose_medium_seen": False,
            }
        )

        # Definition prose, strong patterns: name target+column.
        for tgt, col, pid, matched in b["prose_strong"]:
            t = per_target[tgt]
            t["fk_kinds"].add("prose")
            t["prose_strong_seen"] = True
            t["evidence"].append(f'prose:{pid}:"{matched}"')
            if col:
                t["target_field_candidates"].append((col, "prose_strong"))

        # Definition prose, medium patterns: name target only.
        for tgt, col, pid, matched in b["prose_medium"]:
            if not tgt:
                continue
            t = per_target[tgt]
            t["fk_kinds"].add("prose")
            t["prose_medium_seen"] = True
            t["evidence"].append(f'prose:{pid}:"{matched}"')
            # P3/P3b/P7 don't carry a column; merge step infers later.

        # Type signal.
        for kind, tgt in b["type"]:
            if not tgt:
                continue  # type-only with empty SourceResource - falls to name signal
            t = per_target[tgt]
            t["fk_kinds"].add(kind)  # 'resource_typed' or 'collection_typed'
            t["evidence"].append(f"type:{kind}:SourceResource={tgt}")
            if kind == "collection_typed":
                t["is_collection"] = True

        # Name signal.
        for tgt, pk_col, match_kind, stem in b["name"]:
            t = per_target[tgt]
            t["fk_kinds"].add("name_shape")
            t["evidence"].append(f"name:{match_kind}:{stem}->{tgt}")
            t["name_match_kinds"].add(match_kind)
            if pk_col:
                t["target_field_candidates"].append((pk_col, "name"))
            # Mark exact_stem with target == host as a primary-key
            # candidate (not a real FK).
            if match_kind == "exact_stem" and tgt == host:
                t["is_self_pk"] = True

        # Note: per_target may be empty if the only signal for this
        # field was a polymorphic P5 hit. The polymorphic branch
        # below handles that case. We do NOT `continue` here.

        # Materialise per-target rows.
        for tgt in sorted(per_target):
            t = per_target[tgt]

            # PK self-row: a *Key field whose stem == its own host
            # resource, with no other signals. This is the host's PK,
            # not an FK; drop it from relationships.csv.
            if (
                t["is_self_pk"]
                and t["fk_kinds"] == {"name_shape"}
                and not t["prose_strong_seen"]
                and not t["prose_medium_seen"]
            ):
                continue

            # fk_kind: strongest contributor.
            if "resource_typed" in t["fk_kinds"]:
                fk_kind = "resource_typed"
            elif "collection_typed" in t["fk_kinds"]:
                fk_kind = "collection_typed"
            elif "prose" in t["fk_kinds"]:
                fk_kind = "prose"
            else:
                fk_kind = "name_shape"

            # confidence:
            # - high: 2+ independent signal *categories* agree
            #   (prose / type / name_shape are the three categories).
            # - medium: exactly one strong signal (resource_typed,
            #   collection_typed, or strong prose pattern).
            # - low: only weak signals.
            categories = set()
            if "resource_typed" in t["fk_kinds"] or "collection_typed" in t["fk_kinds"]:
                categories.add("type")
            if "prose" in t["fk_kinds"]:
                categories.add("prose")
            if "name_shape" in t["fk_kinds"]:
                categories.add("name")

            if len(categories) >= 2:
                confidence = "high"
            elif categories == {"type"} or (
                categories == {"prose"} and t["prose_strong_seen"]
            ):
                confidence = "medium"
            elif categories == {"prose"} and t["prose_medium_seen"]:
                confidence = "medium"  # explicit prose target named
            else:
                confidence = "low"

            # target_field: prefer prose-strong candidate (verbatim
            # from the Definition), then a name-signal PK column,
            # then a type-signal heuristic <Target>Key. Each candidate
            # is validated against the target resource's actual
            # field set; if the candidate doesn't exist as a real
            # field on target, fall through. Final fallback is "".
            #
            # Special case (highest priority): if the host_field is a
            # *Key/*Id column and a column with the same name exists
            # on the target resource, prefer it. RESO often expresses
            # FKs as same-named columns (PropertyXxx.ListingKey ->
            # Property.ListingKey, MemberAssociation.AssociationKey ->
            # Association.AssociationKey, etc.). When the prose says
            # "X Resource's <SomeOtherKey>" but the host column shares
            # a name with a column on X, the same-named column is the
            # actual join column - the prose is naming a co-FK.
            target_field = ""
            seen_candidates: list[tuple[str, str]] = []
            host_is_keyish = bool(field.endswith("Key") or field.endswith("Id") or field.endswith("ID"))
            # Skip the same-name rule for self-FKs: the host column
            # exists on the target trivially (same table) so we'd
            # produce a Ref pointing at itself instead of at the
            # actual PK (e.g. Office.MainOfficeKey -> Office.OfficeKey,
            # not Office.MainOfficeKey -> Office.MainOfficeKey).
            if host_is_keyish and tgt != host and target_field_exists(tgt, field):
                target_field = field
            # Strong prose first (verbatim from the page).
            if not target_field:
                for cand, src in t["target_field_candidates"]:
                    if src == "prose_strong" and target_field_exists(tgt, cand):
                        target_field = cand
                        break
                    if src == "prose_strong":
                        seen_candidates.append((cand, "prose_strong:not_in_schema"))
            # Name-signal PK column second (validated).
            if not target_field:
                for cand, src in t["target_field_candidates"]:
                    if src == "name" and target_field_exists(tgt, cand):
                        target_field = cand
                        break
                    if src == "name":
                        seen_candidates.append((cand, "name:not_in_schema"))
            # Type-signal heuristic third: <Target>Key, validated.
            if not target_field and "type" in categories:
                if target_field_exists(tgt, tgt + "Key"):
                    target_field = tgt + "Key"
                else:
                    seen_candidates.append((tgt + "Key", "type:heuristic_not_in_schema"))
            # If nothing validated, surface the first prose-strong
            # candidate verbatim as a hint (Phase 3 / reviewer can
            # reconcile - e.g. OUID FKs point at OrganizationUniqueId
            # which is the alt-key, not the PK).
            if not target_field:
                for cand, src in t["target_field_candidates"]:
                    if src == "prose_strong":
                        target_field = cand
                        break

            notes_bits: list[str] = []
            if t["is_collection"]:
                notes_bits.append("inverse_one_to_many")
            if "self_stem" in t["name_match_kinds"]:
                notes_bits.append("self_referencing")
            if t["is_self_pk"] and "prose" in categories:
                notes_bits.append("name_overlaps_pk")
            # If we ended up using a target_field that doesn't exist
            # in the target schema (final-fallback verbatim prose),
            # tag it so the reviewer knows.
            if target_field and not target_field_exists(tgt, target_field):
                notes_bits.append("target_field_not_in_target_schema")

            out_rows.append(
                {
                    "host_resource": host,
                    "host_field": field,
                    "host_field_type": host_field_type,
                    "target_resource": tgt,
                    "target_field": target_field,
                    "fk_kind": fk_kind,
                    "confidence": confidence,
                    "evidence": " | ".join(t["evidence"]),
                    "notes": ";".join(notes_bits),
                }
            )

        # Polymorphic rows (P5): always emit one polymorphic row per
        # P5 hit, regardless of whether other targets exist for this
        # field. Reviewers need to see the polymorphic marker so the
        # downstream DBML build knows to skip a single Ref and add a
        # comment instead.
        for (matched,) in b["prose_poly"]:
            out_rows.append(
                {
                    "host_resource": host,
                    "host_field": field,
                    "host_field_type": host_field_type,
                    "target_resource": "",
                    "target_field": "",
                    "fk_kind": "prose",
                    "confidence": "medium",
                    "evidence": f'prose:P5:"{matched}"',
                    "notes": "polymorphic",
                }
            )

    out_rows.sort(
        key=lambda r: (r["host_resource"], r["host_field"], r["target_resource"])
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
    valid_host_keys = {(f["ResourceName"], f["StandardName"]) for f in fields}

    for r in out_rows:
        if (r["host_resource"], r["host_field"]) not in valid_host_keys:
            failures.append(
                f"GATE 2: row {r['host_resource']}.{r['host_field']} not in fields.csv"
            )
        if r["target_resource"] and r["target_resource"] not in resources_set:
            failures.append(
                f"GATE 1: target_resource '{r['target_resource']}' not in "
                f"resources.csv (row: {r['host_resource']}.{r['host_field']})"
            )
        if r["fk_kind"] not in VALID_FK_KIND:
            failures.append(
                f"GATE 3: fk_kind '{r['fk_kind']}' not in {sorted(VALID_FK_KIND)}"
            )
        if r["confidence"] not in VALID_CONFIDENCE:
            failures.append(
                f"GATE 4: confidence '{r['confidence']}' not in {sorted(VALID_CONFIDENCE)}"
            )

    # ---- summary -----------------------------------------------------------
    print(f"[03_merge] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    histogram: dict[tuple[str, str], int] = Counter(
        (r["fk_kind"], r["confidence"]) for r in out_rows
    )
    print("[03_merge] fk_kind x confidence histogram:")
    print(f"           {'fk_kind':<20s}{'high':>6s}{'medium':>8s}{'low':>6s}")
    for kind in ("resource_typed", "collection_typed", "prose", "name_shape"):
        h = histogram.get((kind, "high"), 0)
        m = histogram.get((kind, "medium"), 0)
        lo = histogram.get((kind, "low"), 0)
        print(f"           {kind:<20s}{h:>6d}{m:>8d}{lo:>6d}")

    poly = sum(1 for r in out_rows if r["notes"] == "polymorphic")
    inverse = sum(1 for r in out_rows if r["fk_kind"] == "collection_typed")
    print(f"[03_merge] polymorphic rows: {poly}")
    print(f"[03_merge] inverse 1:N (Collection) rows: {inverse}")
    print(f"[03_merge] distinct (host_resource, host_field) covered: "
          f"{len({(r['host_resource'], r['host_field']) for r in out_rows})}")

    if failures:
        print("\n[03_merge] FAILED verification gates:", file=sys.stderr)
        for f in failures[:20]:
            print(f"  - {f}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... ({len(failures) - 20} more)", file=sys.stderr)
        return 2
    print("[03_merge] OK: all verification gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
