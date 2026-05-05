#!/usr/bin/env python3
"""
Inventory the 6 Dash DOCX listing-form templates.

Reads:
  ../../../../raw/dash/BlankForm_*.docx

Writes:
  raw/dash_inventory.csv

Phase: Inventory (mechanical, deterministic).
Owner: scripts/01_inventory_dash.py - do NOT hand-edit raw/dash_inventory.csv.

Determinism:
  - Sorted by (form, table_index, row_index, cell_index, field_label).
  - csv.QUOTE_MINIMAL.
  - No timestamps/hashes/run-IDs in row content.

Heuristic for field-label detection:
  - Cell text ending with ':' (with optional trailing required marker
    such as 'V', '*', '√') is a field LABEL.
  - First-row cell text in a table is the section HEADER (de-duplicated
    when the row uses merged cells repeated across columns).
  - Other non-empty cells are ENUM_VALUE candidates (lookup options).

This is intentionally conservative; the curated mapping CSV references
labels by text, so capturing the full inventory matters more than
classification accuracy.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import docx

KB_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = KB_ROOT.parent.parent.parent
DASH_DIR = REPO_ROOT / "raw" / "dash"
OUT_CSV = KB_ROOT / "raw" / "dash_inventory.csv"

FORM_NAME_MAP = {
    "BlankForm_Residential Sale Listing_SIR.docx": "Residential_Sale",
    "BlankForm_Residential Rental Listing_SIR.docx": "Residential_Rental",
    "BlankForm_Commercial Sale Listing_SIR.docx": "Commercial_Sale",
    "BlankForm_Commercial Lease Listing_SIR.docx": "Commercial_Lease",
    "BlankForm_Person_SIR.docx": "Person",
    "BlankForm_Team_SIR.docx": "Team",
}

# Trailing "required" markers stripped before classifying a label.
REQUIRED_MARKERS = {"√", "v", "V", "*", "✓", "✔"}

LABEL_RE = re.compile(r":\s*[√v*✓✔]?\s*$")
SECTION_HEADER_RE = re.compile(r"^[A-Za-z][A-Za-z &/]+$")  # rough: words only


def normalize_cell(text: str) -> str:
    """Collapse whitespace; trim."""
    return " ".join(text.split())


def is_field_label(text: str) -> bool:
    return bool(LABEL_RE.search(text))


def has_required_marker(text: str) -> bool:
    stripped = text.rstrip()
    return any(stripped.endswith(m) for m in REQUIRED_MARKERS)


def field_type_hint(text: str) -> str:
    lower = text.lower()
    if any(k in lower for k in ("date", "year", "year built", "year of")):
        return "date"
    if any(
        k in lower
        for k in ("price", "amount", "fee", "rate", "%", "sq.m", "sq.ft", "size", "count", "number of", "no. of", "n. of", "no of")
    ):
        return "number"
    if any(k in lower for k in ("yes/no", "(yes/no)", "y/n")):
        return "boolean"
    if "(choose one)" in lower or "(select one)" in lower:
        return "enum_single"
    if "(choose all that apply)" in lower or "(select all)" in lower or "(multi)" in lower:
        return "enum_multi"
    return "text"


def iter_cells_unique(form: str, document) -> list[dict]:
    """
    Walk every cell in every table; return a list of cell records with
    deduplication of the same text within a row (DOCX merged-cell trick
    repeats text across columns).
    """
    rows: list[dict] = []
    for ti, table in enumerate(document.tables):
        # Section header is the first row's first non-empty distinct cell text.
        section: str = ""
        for ri, row in enumerate(table.rows):
            seen_in_row: set[str] = set()
            for ci, cell in enumerate(row.cells):
                text = normalize_cell(cell.text)
                if not text:
                    continue
                if text in seen_in_row:
                    continue
                seen_in_row.add(text)

                # First-row, first-distinct-text -> section header.
                if ri == 0 and not section:
                    section = text

                rows.append(
                    {
                        "form": form,
                        "table_index": ti,
                        "row_index": ri,
                        "cell_index": ci,
                        "section": section,
                        "raw_text": text,
                    }
                )
    return rows


def classify(record: dict) -> dict | None:
    text = record["raw_text"]
    section = record["section"]

    # Skip the literal section-header row (it is metadata, not a field).
    if record["row_index"] == 0 and text == section:
        return None

    if is_field_label(text):
        # Strip trailing colon and any required marker.
        label = re.sub(r":\s*[√v*✓✔]?\s*$", "", text).strip()
        return {
            "form": record["form"],
            "section": section,
            "kind": "field",
            "field_label": label,
            "field_type_hint": field_type_hint(label),
            "required_yn": "yes" if has_required_marker(text) else "no",
            "table_index": record["table_index"],
            "row_index": record["row_index"],
            "cell_index": record["cell_index"],
        }

    # Enum value candidate (a lookup option on a "(choose one)" table).
    return {
        "form": record["form"],
        "section": section,
        "kind": "enum_value",
        "field_label": text,
        "field_type_hint": "",
        "required_yn": "",
        "table_index": record["table_index"],
        "row_index": record["row_index"],
        "cell_index": record["cell_index"],
    }


def main() -> int:
    if not DASH_DIR.is_dir():
        print(f"ERROR: Dash source dir not found: {DASH_DIR}", file=sys.stderr)
        return 2

    rows: list[dict] = []
    seen_keys: set[tuple] = set()
    for filename, form_name in sorted(FORM_NAME_MAP.items()):
        path = DASH_DIR / filename
        if not path.is_file():
            print(f"ERROR: missing form: {path}", file=sys.stderr)
            return 2
        document = docx.Document(str(path))
        cells = iter_cells_unique(form_name, document)
        for cell in cells:
            classified = classify(cell)
            if classified is None:
                continue
            # Deduplicate identical (form, section, kind, field_label) tuples;
            # keep the earliest position for stability.
            key = (
                classified["form"],
                classified["section"],
                classified["kind"],
                classified["field_label"],
            )
            if key in seen_keys:
                continue
            seen_keys.add(key)
            rows.append(classified)

    rows.sort(
        key=lambda r: (
            r["form"],
            r["section"],
            r["kind"],
            r["table_index"],
            r["row_index"],
            r["cell_index"],
            r["field_label"],
        )
    )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "form",
                "section",
                "kind",
                "field_label",
                "field_type_hint",
                "required_yn",
                "table_index",
                "row_index",
                "cell_index",
            ],
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(rows)

    field_count = sum(1 for r in rows if r["kind"] == "field")
    enum_count = sum(1 for r in rows if r["kind"] == "enum_value")
    forms = sorted({r["form"] for r in rows})
    print(
        f"[01] wrote {OUT_CSV.relative_to(KB_ROOT)}: "
        f"{len(rows)} rows ({field_count} fields, {enum_count} enum values) across {len(forms)} forms"
    )
    print(f"     forms: {', '.join(forms)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
