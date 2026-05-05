#!/usr/bin/env python3
"""
Phase 2.5 Signal C: Definition prose similarity (Jaccard).

Reads:
    raw/field_definitions.csv
    raw/_satellites_child_match.csv (Signal B output)

Writes:
    raw/_satellites_definition.csv

For every (host_resource, candidate_satellite) <-> (target_resource,
target_field) pair with a non-empty target_field, compute Jaccard
similarity over normalised token sets:

    1. Split on whitespace.
    2. Lowercase, strip outer punctuation `.,;:()"'`.
    3. Remove stopwords (the, a, of, ...).
    4. Remove role-context tokens (listing, list, buyer, co, agent,
       member, office, contact, contacts, team, teams, broker, ...).

Why role-context removal: 'Property.ListAgentFirstName' has the
definition "The first name of the listing agent."; the matching
'Member.MemberFirstName' has "The first name of the member.".
Without role-context removal the shared set is {first, name} and
jaccard = 2/5 = 0.4. With role-context removal both sides become
{first, name} and jaccard = 1.0.

Output columns:
    host_resource, host_field, candidate_satellite,
    target_resource, target_field, jaccard, host_token_count,
    target_token_count, shared_token_count,
    host_def_first120, target_def_first120

Idempotent. Determinism: rows sorted by
(host_resource, host_field, candidate_satellite).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"

IN_DEFS = RAW / "field_definitions.csv"
IN_CHILD = RAW / "_satellites_child_match.csv"
OUT = RAW / "_satellites_definition.csv"

OUT_COLUMNS = [
    "host_resource",
    "host_field",
    "candidate_satellite",
    "target_resource",
    "target_field",
    "jaccard",
    "host_token_count",
    "target_token_count",
    "shared_token_count",
    "host_def_first120",
    "target_def_first120",
]

STOPWORDS = {
    "the", "a", "an",
    "of", "to", "in", "for", "from", "on", "with", "by", "as", "at",
    "or", "and", "is", "are", "was", "were", "be", "been", "being",
    "this", "that", "these", "those", "it", "its", "their", "which",
    "may", "has", "have", "had", "if", "but", "not", "no", "all",
    "any", "some", "e.g.", "i.e.", "etc.", "e.g.,", "i.e.,", "etc.,",
    "such", "also", "only", "do", "does", "did", "can", "could",
    "should", "would", "will", "shall", "than", "then", "there",
    "here", "what", "when", "where", "who", "how", "why", "you", "your",
    "we", "our", "us", "they", "them", "he", "she", "his", "her",
    "i", "me", "my",
}

# Role-context tokens to strip before computing Jaccard. These
# typically appear in host columns to specify which side of the FK
# the column refers to ("the first name of the listing agent") but
# are absent from the target column ("the first name of the
# member"). Stripping makes equivalent definitions actually look
# equivalent.
ROLE_CONTEXT = {
    "listing", "list",
    "buyer", "buyers",
    "co-buyer", "co-buyers", "cobuyer", "cobuyers",
    "co-list", "co-listing", "colist", "colisting",
    "co",  # bare 'co' from Co-buyer/Co-list when split on whitespace
    "agent", "agents",
    "member", "members",
    "office", "offices",
    "broker", "brokers",
    "contact", "contacts",
    "team", "teams",
    "manager", "managers",
    "owner", "owners",
    "source", "originating",
    "showing", "showings",
    "main",
    "name",  # NOTE: keep 'name' - it's content not context (used in FirstName etc.)
}
# Don't actually drop 'name' - revert it.
ROLE_CONTEXT.discard("name")


_TOKEN_PUNCT = ".,;:()\"'"
_WS_RE = re.compile(r"\s+")
# Split on whitespace AND on apostrophes / hyphens so possessives
# ("buyer's") and compound role tokens ("co-agent", "co-listing")
# decompose into atoms that role-stripping can match. Without this
# the host token stays as `buyer's`/`co-agent` and never gets
# stripped, leaving the host token-set noisier than the target.
_SPLIT_RE = re.compile(r"[\s\-'\u2019]+")


def normalise(text: str) -> set[str]:
    if not text:
        return set()
    cleaned = text.replace("\u2019", "'")
    out: set[str] = set()
    for raw in _SPLIT_RE.split(cleaned):
        t = raw.lower().strip(_TOKEN_PUNCT)
        if not t:
            continue
        # Strip a trailing possessive 's' that may survive the split
        # (e.g. "buyer's" -> ["buyer", "s"], the trailing "s" is noise).
        if t == "s":
            continue
        if t in STOPWORDS:
            continue
        if t in ROLE_CONTEXT:
            continue
        out.add(t)
    return out


def main() -> int:
    if not IN_DEFS.exists() or not IN_CHILD.exists():
        print("FAIL: field_definitions.csv and _satellites_child_match.csv must both exist", file=sys.stderr)
        return 2

    defs: dict[tuple[str, str], str] = {
        (r["ResourceName"], r["StandardName"]): r["Definition"]
        for r in csv.DictReader(IN_DEFS.open())
    }

    out_rows: list[dict] = []
    for r in csv.DictReader(IN_CHILD.open()):
        target_field = r["target_field"]
        if not target_field:
            continue  # Signal B unmatched - nothing to compare.

        host_def = defs.get((r["host_resource"], r["candidate_satellite"]), "") or ""
        tgt_def = defs.get((r["target_resource"], target_field), "") or ""

        host_toks = normalise(host_def)
        tgt_toks = normalise(tgt_def)

        union = host_toks | tgt_toks
        shared = host_toks & tgt_toks
        jaccard = (len(shared) / len(union)) if union else 0.0

        out_rows.append(
            {
                "host_resource": r["host_resource"],
                "host_field": r["host_field"],
                "candidate_satellite": r["candidate_satellite"],
                "target_resource": r["target_resource"],
                "target_field": target_field,
                "jaccard": f"{jaccard:.3f}",
                "host_token_count": len(host_toks),
                "target_token_count": len(tgt_toks),
                "shared_token_count": len(shared),
                "host_def_first120": host_def[:120],
                "target_def_first120": tgt_def[:120],
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
    high = sum(1 for r in out_rows if float(r["jaccard"]) >= 0.6)
    mid = sum(1 for r in out_rows if 0.4 <= float(r["jaccard"]) < 0.6)
    low = sum(1 for r in out_rows if float(r["jaccard"]) < 0.4)
    print(f"[04c] wrote {OUT.relative_to(KB_ROOT)} ({len(out_rows)} rows)")
    print(f"      jaccard >= 0.6 (high):                {high}")
    print(f"      jaccard in [0.4, 0.6) (borderline):   {mid}")
    print(f"      jaccard < 0.4 (low):                  {low}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
