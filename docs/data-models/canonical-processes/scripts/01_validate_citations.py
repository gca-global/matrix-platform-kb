#!/usr/bin/env python3
"""
Validate RESO citations and mermaid state diagrams in every
processes/*.md file.

Reads:
  processes/*.md
  ../reso-dd-kb/raw/resources.csv
  ../reso-dd-kb/raw/fields.csv
  ../reso-dd-kb/raw/lookup_values.csv

Writes:
  raw/citations.csv

Phase: Validate (mechanical, deterministic).
Owner: scripts/01_validate_citations.py - do NOT hand-edit raw/citations.csv.

Hard-fail gates (script exits non-zero on any breach):

  1. Every cited `Resource: X` exists in resources.csv.
  2. Every cited `Field: X.Y` exists in fields.csv with ResourceName=X
     and StandardName=Y.
  3. Every cited `LookupValue: L.V` exists in lookup_values.csv with
     LookupName=L and StandardValue=V.
  4. Every process file has exactly one `<!-- reso-citations ... -->`
     block.
  5. Every process file has at least one ```mermaid stateDiagram-v2
     block.

Failures print exact line numbers and unresolved citations. Do NOT
relax a gate to make the build green.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RESO_RAW = KB_ROOT.parent / "reso-dd-kb" / "raw"
PROCESSES_DIR = KB_ROOT / "processes"
OUT_CSV = KB_ROOT / "raw" / "citations.csv"

CITATION_BLOCK_RE = re.compile(
    r"<!--\s*reso-citations\s*\n(?P<body>.*?)\n\s*-->",
    re.DOTALL,
)
MERMAID_STATE_RE = re.compile(
    r"```mermaid\s*\n\s*stateDiagram-v2\b",
)
ALLOWED_PREFIXES = ("Resource:", "Field:", "LookupValue:")


def load_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def parse_citation_block(text: str, file_offset_line: int) -> list[tuple[int, str, str]]:
    """Return list of (line_no_in_file, prefix, value) tuples."""
    out: list[tuple[int, str, str]] = []
    for i, raw in enumerate(text.splitlines()):
        line_no = file_offset_line + i
        line = raw.strip()
        if not line:
            continue
        if not any(line.startswith(p) for p in ALLOWED_PREFIXES):
            out.append((line_no, "INVALID", raw))
            continue
        prefix, _, value = line.partition(":")
        out.append((line_no, prefix.strip(), value.strip()))
    return out


def main() -> int:
    if not PROCESSES_DIR.is_dir():
        print(f"ERROR: processes dir not found: {PROCESSES_DIR}", file=sys.stderr)
        return 2
    if not RESO_RAW.is_dir():
        print(f"ERROR: reso-dd-kb raw dir not found: {RESO_RAW}", file=sys.stderr)
        return 2

    # Build RESO lookup indexes.
    resources = {r["ResourceName"] for r in load_csv(RESO_RAW / "resources.csv")}
    fields_by_resource: dict[str, set[str]] = {}
    for fr in load_csv(RESO_RAW / "fields.csv"):
        fields_by_resource.setdefault(fr["ResourceName"], set()).add(fr["StandardName"])
    lookups: dict[str, set[str]] = {}
    for lv in load_csv(RESO_RAW / "lookup_values.csv"):
        lookups.setdefault(lv["LookupName"], set()).add(lv["StandardValue"])

    process_files = sorted(PROCESSES_DIR.glob("*.md"))
    if not process_files:
        print(f"ERROR: no processes/*.md files found in {PROCESSES_DIR}", file=sys.stderr)
        return 2

    errors: list[str] = []
    citations: list[dict] = []

    for path in process_files:
        rel = path.relative_to(KB_ROOT)
        text = path.read_text(encoding="utf-8")

        # Gate 4: exactly one citation block.
        matches = list(CITATION_BLOCK_RE.finditer(text))
        if len(matches) == 0:
            errors.append(
                f"GATE 4 {rel}: no `<!-- reso-citations ... -->` block found"
            )
            continue
        if len(matches) > 1:
            errors.append(
                f"GATE 4 {rel}: {len(matches)} `<!-- reso-citations ... -->` blocks "
                f"found (must be exactly one)"
            )
            continue

        # Gate 5: at least one mermaid stateDiagram-v2.
        if not MERMAID_STATE_RE.search(text):
            errors.append(
                f"GATE 5 {rel}: no ```mermaid stateDiagram-v2 block found"
            )

        # Parse the (single) citation block.
        m = matches[0]
        body = m.group("body")
        block_start = text[: m.start("body")].count("\n") + 1
        for line_no, kind, value in parse_citation_block(body, block_start):
            if kind == "INVALID":
                errors.append(
                    f"{rel}:{line_no}: invalid citation prefix in line {value!r}; "
                    f"allowed prefixes: {', '.join(ALLOWED_PREFIXES)}"
                )
                continue

            citations.append(
                {
                    "process": rel.name,
                    "citation_kind": kind,
                    "citation_value": value,
                    "line_no": line_no,
                }
            )

            # Gate 1/2/3: citation resolves.
            if kind == "Resource":
                if value not in resources:
                    errors.append(
                        f"GATE 1 {rel}:{line_no}: Resource {value!r} not in "
                        f"reso-dd-kb/raw/resources.csv"
                    )
            elif kind == "Field":
                if "." not in value:
                    errors.append(
                        f"GATE 2 {rel}:{line_no}: Field must be of form "
                        f"`<Resource>.<Field>`; got {value!r}"
                    )
                    continue
                res, fld = value.split(".", 1)
                if res not in fields_by_resource:
                    errors.append(
                        f"GATE 2 {rel}:{line_no}: Field {value!r}: resource "
                        f"{res!r} not in fields.csv"
                    )
                elif fld not in fields_by_resource[res]:
                    errors.append(
                        f"GATE 2 {rel}:{line_no}: Field {value!r}: "
                        f"{res}.{fld} not in fields.csv"
                    )
            elif kind == "LookupValue":
                if "." not in value:
                    errors.append(
                        f"GATE 3 {rel}:{line_no}: LookupValue must be of form "
                        f"`<Lookup>.<StandardValue>`; got {value!r}"
                    )
                    continue
                lk, val = value.split(".", 1)
                if lk not in lookups:
                    errors.append(
                        f"GATE 3 {rel}:{line_no}: LookupValue {value!r}: "
                        f"lookup {lk!r} not in lookup_values.csv"
                    )
                elif val not in lookups[lk]:
                    errors.append(
                        f"GATE 3 {rel}:{line_no}: LookupValue {value!r}: "
                        f"{lk}.{val} not in lookup_values.csv"
                    )

    if errors:
        print(
            f"01_validate_citations.py: {len(errors)} hard-fail gate violation(s):",
            file=sys.stderr,
        )
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        print(
            "\nFix the rows above in processes/*.md (or update reso-dd-kb if "
            "RESO has changed) and try again. Do NOT relax the gates.",
            file=sys.stderr,
        )
        return 1

    citations.sort(
        key=lambda r: (r["process"], r["citation_kind"], r["citation_value"], r["line_no"])
    )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["process", "citation_kind", "citation_value", "line_no"],
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(citations)

    by_kind: dict[str, int] = {}
    for c in citations:
        by_kind[c["citation_kind"]] = by_kind.get(c["citation_kind"], 0) + 1
    parts = ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items()))
    print(
        f"[01] validate_citations: 5/5 hard-fail gates passed across "
        f"{len(process_files)} process file(s); {len(citations)} citations "
        f"({parts}) -> raw/citations.csv"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
