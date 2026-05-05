#!/usr/bin/env python3
"""
Extract FK signals from Definition prose.

Reads:
    raw/field_definitions.csv

Writes:
    raw/_signals_definition.csv

Each row is one (host_resource, host_field, target_resource,
target_field, pattern_id, matched_substring) hit. Multiple hits per
field are emitted as separate rows; the merge step dedups later.

Patterns (case-insensitive on cleaned single-line prose):

    P1  "foreign key relating/referring/related (to) (the) X Resource's Y"
        target=(X, Y), strong
    P2  "foreign key relating/referring/related to (the) Y of (the) X
         Resource"
        target=(X, Y), strong
    P3  "foreign key (to|from|in|of|relating to|referring to|referencing|
         related to) (the) X Resource"
        target=(X, host_field) - column inferred to the host field name,
        medium
    P4  "self-referencing foreign key relating/referring to this
         resource's Y"
        target=(host_resource, Y), strong
    P5  "foreign key from the resource selected in the <NAME> field"
        target=(<empty>, host_field) - polymorphic, medium
    P6  bare "X Resource's Y" outside any 'foreign key' clause
        target=(X, Y), strong, BUT only when the host field is the
        kind of column that typically holds an FK (its StandardName
        ends in Key/Id/ID).

Idempotent: deletes _signals_definition.csv at the start of each run.

Determinism: rows sorted by (host_resource, host_field, pattern_id,
target_resource, target_field).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_DEFS = RAW / "field_definitions.csv"
IN_FIELDS = RAW / "fields.csv"
OUT = RAW / "_signals_definition.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "pattern_id",
    "target_resource",
    "target_field",
    "matched",
    "notes",
]

# Cleaned text: collapse whitespace runs to single spaces, strip
# surrounding whitespace, normalise smart quotes (the corpus uses
# both `'` and `\u2019`).
_WS_RE = re.compile(r"\s+")


def clean(text: str) -> str:
    return _WS_RE.sub(" ", text.replace("\u2019", "'")).strip()


# Pattern 1: "...foreign key (relating|referring|related) (to)? (the)?
#             <Target> Resource's <Column>"
# Notes:
#   - We allow optional "to"/"the" between the verb and target.
#   - The verb is required so we don't match bare "X Resource's Y".
#   - <Target> = single CamelCase word (RESO resource names are single
#     CamelCase tokens by convention - Property, Member, Office, OUID,
#     Contacts, CaravanStop, etc.).
#   - <Column> must end in Key/Id/ID. Without this constraint the
#     pattern over-captures the next noun phrase, e.g.
#     "Contacts Resource's local, well-known identifier..." would
#     bind <col>=local, which is not a column.
P1 = re.compile(
    r"(?i:foreign\s+key\s+(?:relating|referring|related)"
    r"(?:\s+to)?\s+(?:the\s+)?)"
    r"(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource'?s\s+"
    r"(?P<col>[A-Z][A-Za-z]*(?:Key|Id|ID))\b",
)

# Pattern 2: "...foreign key (relating|referring|related) to (the)?
#             <Column> of (the)? <Target> Resource"
# (e.g. ShowingAppointment.ShowingAgentKey: "...foreign key relating to
#  the Member Key of the Member Resource.")
P2 = re.compile(
    r"foreign\s+key\s+(?:relating|referring|related)\s+to\s+(?:the\s+)?"
    r"(?P<col>[A-Z][A-Za-z]*(?:Key|Id|ID)|[A-Z][A-Za-z]+\s+[Kk]ey)"
    r"\s+of\s+(?:the\s+)?"
    r"(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource",
)

# Pattern 3: "...foreign key (to|from|in|of|relating to|referring to|
#             referencing|related to|related|in the|to the) (the)?
#             <Target> Resource"  (no possessive, no Y after)
P3 = re.compile(
    r"(?i:foreign\s+key\s+"
    r"(?:to|from|in|of|"
    r"relating(?:\s+to)?|referring(?:\s+to)?|referencing|related(?:\s+to)?)"
    r"\s+(?:the\s+)?)"
    r"(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource"
    r"(?!\s*'s|\s*\u2019s)",
)

# Pattern 3b: "...foreign key referencing the primary key of (the)?
#              <Target> Resource"
# (e.g. CaravanStop.CaravanKey: "foreign key referencing the primary
#  key of the Caravan Resource.")
# Treated as a P3 variant in the merge step: target=X, column=PK of X.
P3b = re.compile(
    r"(?i:foreign\s+key\s+(?:referencing|referring\s+to|relating\s+to)\s+"
    r"the\s+primary\s+key\s+of\s+(?:the\s+)?)"
    r"(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource",
)

# Pattern 7: "...foreign key (verb) (the)? <Target> Resource's primary
#             key"  (e.g. TeamMembers.TeamKey)
# Same semantics as P3b: target=X, column inferred to PK of X.
P7 = re.compile(
    r"(?i:foreign\s+key\s+"
    r"(?:to|from|in|of|"
    r"relating(?:\s+to)?|referring(?:\s+to)?|referencing|related(?:\s+to)?)"
    r"\s+(?:the\s+)?)"
    r"(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource'?s\s+primary\s+key",
)

# Pattern 4: "...self-referencing foreign key (relating|referring) to
#             this resource's <Column>"
P4 = re.compile(
    r"(?i:self-referencing\s+foreign\s+key\s+(?:relating|referring)\s+to\s+"
    r"this\s+resource'?s\s+)"
    r"(?P<col>[A-Z][A-Za-z]*(?:Key|Id|ID))\b",
)

# Pattern 5: "...foreign key from the resource selected in the <NAME>
#             field" (polymorphic via the named field, typically
#             "ResourceName")
P5 = re.compile(
    r"(?i:foreign\s+key\s+from\s+the\s+resource\s+selected\s+in\s+the\s+)"
    r"(?P<via>[A-Z][A-Za-z]+)\s+(?i:field)",
)

# Pattern 6: bare "<Target> Resource's <Column>" not inside a 'foreign
# key' clause. Captured separately and only applied when the host
# field is *Key / *Id (i.e. likely an FK-bearing column).
P6 = re.compile(
    r"\b(?P<target>[A-Z][A-Za-z]+)\s+[Rr]esource'?s\s+"
    r"(?P<col>[A-Z][A-Za-z]*(?:Key|Id|ID))\b",
)


def normalise_target_column(raw_col: str) -> str:
    """
    Pattern 2 may capture "Member Key" (two words). Collapse to
    canonical "MemberKey".
    """
    parts = raw_col.split()
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2 and parts[1].lower() == "key":
        return parts[0] + "Key"
    return "".join(p[:1].upper() + p[1:] for p in parts)


def main() -> int:
    if not IN_DEFS.exists():
        print(f"FAIL: {IN_DEFS} missing - run 02_parse_mirror.py first", file=sys.stderr)
        return 2

    fields_by_key: dict[tuple[str, str], dict] = {}
    with IN_FIELDS.open() as fh:
        for row in csv.DictReader(fh):
            fields_by_key[(row["ResourceName"], row["StandardName"])] = row

    out_rows: list[dict] = []

    with IN_DEFS.open() as fh:
        for row in csv.DictReader(fh):
            host = row["ResourceName"]
            field = row["StandardName"]
            text = clean(row["Definition"])

            # P1 - all matches (a Definition can name two FKs).
            for m in P1.finditer(text):
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P1",
                        "target_resource": m.group("target"),
                        "target_field": m.group("col"),
                        "matched": m.group(0),
                        "notes": "strong",
                    }
                )

            for m in P2.finditer(text):
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P2",
                        "target_resource": m.group("target"),
                        "target_field": normalise_target_column(m.group("col")),
                        "matched": m.group(0),
                        "notes": "strong",
                    }
                )

            # P3 emits only if no P1 match for the same target was
            # already recorded for this field (P1 supersedes P3,
            # P3 has no column).
            p1_targets = {
                r["target_resource"]
                for r in out_rows
                if r["host_resource"] == host
                and r["host_field"] == field
                and r["pattern_id"] in ("P1", "P2")
            }
            for m in P3.finditer(text):
                target = m.group("target")
                if target in p1_targets:
                    continue
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P3",
                        "target_resource": target,
                        # Column inferred to host_field for now;
                        # merge step decides the canonical column.
                        "target_field": "",
                        "matched": m.group(0),
                        "notes": "medium;column_inferred",
                    }
                )

            for m in P4.finditer(text):
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P4",
                        "target_resource": host,
                        "target_field": m.group("col"),
                        "matched": m.group(0),
                        "notes": "strong;self_referencing",
                    }
                )

            for m in P5.finditer(text):
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P5",
                        "target_resource": "",
                        "target_field": "",
                        "matched": m.group(0),
                        "notes": f"medium;polymorphic_via_{m.group('via')}",
                    }
                )

            # P3b and P7 - both add a row for an FK whose Definition
            # named the target resource via 'primary key of/for X
            # Resource' or 'X Resource's primary key'. The target
            # column is the PK of <target>; we leave target_field
            # empty here and let the merge step infer it.
            for m in P3b.finditer(text):
                target = m.group("target")
                if target == host:
                    continue
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P3b",
                        "target_resource": target,
                        "target_field": "",
                        "matched": m.group(0),
                        "notes": "medium;column_is_pk_of_target",
                    }
                )
            for m in P7.finditer(text):
                target = m.group("target")
                if target == host:
                    continue
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "pattern_id": "P7",
                        "target_resource": target,
                        "target_field": "",
                        "matched": m.group(0),
                        "notes": "medium;column_is_pk_of_target",
                    }
                )

            # P6: only consider when the host field name suggests an
            # FK column (*Key / *Id / *ID) and the matched target is
            # not already covered by P1/P2/P3 for this field.
            host_is_fk_shape = bool(re.search(r"(Key|Id|ID)$", field))
            if host_is_fk_shape:
                already = {
                    (r["target_resource"], r["target_field"])
                    for r in out_rows
                    if r["host_resource"] == host
                    and r["host_field"] == field
                    and r["pattern_id"] in ("P1", "P2")
                }
                already_p3 = {
                    r["target_resource"]
                    for r in out_rows
                    if r["host_resource"] == host
                    and r["host_field"] == field
                    and r["pattern_id"] == "P3"
                }
                for m in P6.finditer(text):
                    target = m.group("target")
                    col = m.group("col")
                    # Skip the same target+col already produced by P1/P2.
                    if (target, col) in already:
                        continue
                    # Skip non-resource possessives accidentally matched
                    # ("Standard Resource's...", "Source Resource's...").
                    # The known false-positive list is small.
                    if target in {"Source", "Standard", "Data", "This", "Related"}:
                        continue
                    # If P3 already named this target, P6 is the column
                    # disambiguator - emit it.
                    out_rows.append(
                        {
                            "host_resource": host,
                            "host_field": field,
                            "pattern_id": "P6",
                            "target_resource": target,
                            "target_field": col,
                            "matched": m.group(0),
                            "notes": "strong;possessive_no_fk_word"
                            + (";refines_P3" if target in already_p3 else ""),
                        }
                    )

    out_rows.sort(
        key=lambda r: (
            r["host_resource"],
            r["host_field"],
            r["pattern_id"],
            r["target_resource"],
            r["target_field"],
        )
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

    by_pattern = Counter(r["pattern_id"] for r in out_rows)
    print(f"[03a] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    for k in sorted(by_pattern):
        print(f"      pattern {k}: {by_pattern[k]} rows")

    # Quick sanity: no row should have target_resource == host_resource
    # except for P4 (self-FK).
    bogus = [
        r
        for r in out_rows
        if r["pattern_id"] != "P4"
        and r["target_resource"]
        and r["target_resource"] == r["host_resource"]
        and r["pattern_id"] != "P5"
    ]
    if bogus:
        print(f"[03a] WARN: {len(bogus)} non-P4 rows where target == host (review):")
        for r in bogus[:5]:
            print(f"       {r['host_resource']}.{r['host_field']} -> {r['target_resource']} [{r['pattern_id']}]")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
