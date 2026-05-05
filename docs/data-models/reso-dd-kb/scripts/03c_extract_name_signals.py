#!/usr/bin/env python3
"""
Extract FK signals from field name shape.

Reads:
    raw/fields.csv
    raw/resources.csv

Writes:
    raw/_signals_name.csv

For every field whose StandardName ends in 'Key' or 'Id' (case-
sensitive; 'ID' suffix counts too), derive
    Stem = StandardName[:-3]   for *Key
    Stem = StandardName[:-2]   for *Id / *ID

Search resources.csv for a target by:
    1) exact match: Stem == ResourceName.   match_kind=exact_stem
    2) tail match:  Stem ends in ResourceName, with a CamelCase
                    boundary (so 'OwnerMember'.endswith('Member') ->
                    Member, but 'AssociationFee'.endswith('Fee')
                    won't match because there's no resource named
                    'Fee'). match_kind=tail_stem
    3) host match:  Stem == host_resource (self-FK candidate).
                    match_kind=self_stem
A field can produce multiple rows if the stem matches multiple
resources; the merge step decides which one Phase 2.5 / Phase 3
trusts.

Idempotent: deletes _signals_name.csv at the start.

Determinism: rows sorted by (host_resource, host_field,
target_resource).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_FIELDS = RAW / "fields.csv"
IN_RESOURCES = RAW / "resources.csv"
OUT = RAW / "_signals_name.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "stem",
    "suffix",     # Key | Id | ID
    "target_resource",
    "match_kind",  # exact_stem | tail_stem | self_stem
    "target_pk_column",  # what the canonical PK column on target is
                          # likely to be (Target+Key); merge step
                          # uses this to fill target_field
    "notes",
]

KEY_SUFFIX_RE = re.compile(r"^(?P<stem>[A-Z][A-Za-z0-9]+?)(?P<suffix>Key|Id|ID)$")


def main() -> int:
    if not IN_FIELDS.exists():
        print(f"FAIL: {IN_FIELDS} missing", file=sys.stderr)
        return 2
    if not IN_RESOURCES.exists():
        print(f"FAIL: {IN_RESOURCES} missing", file=sys.stderr)
        return 2

    resources: list[str] = sorted(
        row["ResourceName"] for row in csv.DictReader(IN_RESOURCES.open())
    )
    resources_set: set[str] = set(resources)

    out_rows: list[dict] = []

    with IN_FIELDS.open() as fh:
        for row in csv.DictReader(fh):
            host = row["ResourceName"]
            field = row["StandardName"]
            m = KEY_SUFFIX_RE.match(field)
            if not m:
                continue
            stem = m.group("stem")
            suffix = m.group("suffix")
            seen_targets: set[str] = set()

            # The host resource depluralised. RESO sometimes pluralises
            # resource names (TeamMembers, Contacts, Teams) but their
            # PK column drops the trailing `s` (TeamMemberKey,
            # ContactKey, TeamKey). Detecting "this is a PK" needs to
            # compare against both spellings.
            host_singular = host[:-1] if host.endswith("s") else host
            is_host_pk = stem == host or stem == host_singular

            # 1. Exact stem match.
            if stem in resources_set:
                seen_targets.add(stem)
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "stem": stem,
                        "suffix": suffix,
                        "target_resource": stem,
                        "match_kind": "exact_stem",
                        "target_pk_column": stem + "Key",
                        "notes": "self_referencing" if stem == host else "",
                    }
                )

            # 2. Self-FK: stem == host_resource. Only emit if NOT
            #    already added by exact_stem (the typical case).
            if stem == host and host not in seen_targets:
                seen_targets.add(host)
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "stem": stem,
                        "suffix": suffix,
                        "target_resource": host,
                        "match_kind": "self_stem",
                        "target_pk_column": host + "Key",
                        "notes": "self_referencing",
                    }
                )

            # If the stem IS the host's PK (TeamMemberKey on
            # TeamMembers, SocialMediaKey on SocialMedia), do NOT
            # produce tail_stem matches - those would falsely flag
            # the host's own PK as an FK to a substring resource
            # ("SocialMedia" tail-matching "Media").
            if is_host_pk:
                continue

            # 3. Tail stem match (CamelCase boundary).
            #    Iterate over resources in descending name length so
            #    the longest tail wins.
            for r in sorted(resources, key=len, reverse=True):
                if r in seen_targets:
                    continue
                if not stem.endswith(r):
                    continue
                if r == stem:
                    continue  # exact match was already handled
                head = stem[: -len(r)]
                # Require head to end in a CamelCase boundary.
                if not head:
                    continue
                if not (head[-1].islower() or head[-1].isdigit()):
                    continue
                # Suppress the "OriginatingSystem<X>Key" /
                # "SourceSystem<X>Key" pattern when X is the host's
                # own resource. RESO uses these to mean "the host's
                # own key, as it appears on the originating / source
                # system" - they are NOT FKs to <X>.
                if r == host and head in ("OriginatingSystem", "SourceSystem"):
                    continue
                # Same idea but for plurals: TeamMember on TeamMembers,
                # Contact on Contacts.
                if r == host_singular and head in ("OriginatingSystem", "SourceSystem"):
                    continue
                seen_targets.add(r)
                out_rows.append(
                    {
                        "host_resource": host,
                        "host_field": field,
                        "stem": stem,
                        "suffix": suffix,
                        "target_resource": r,
                        "match_kind": "tail_stem",
                        "target_pk_column": r + "Key",
                        "notes": f"head={head}",
                    }
                )
                # Tail-stem is weak; once the longest valid tail is
                # found we stop - shorter tails would create noise.
                break

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

    # Summary
    from collections import Counter
    by_kind = Counter(r["match_kind"] for r in out_rows)
    by_suffix = Counter(r["suffix"] for r in out_rows)
    print(f"[03c] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    for k in sorted(by_kind):
        print(f"      {k}: {by_kind[k]} rows")
    for s in sorted(by_suffix):
        print(f"      suffix {s!r}: {by_suffix[s]} rows")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
