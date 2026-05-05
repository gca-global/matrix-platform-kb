#!/usr/bin/env python3
"""
Emit per-resource integrated views joining Layers 1-4.

Reads:
  ../data-models/reso-dd-kb/raw/resources.csv
  ../data-models/reso-dd-kb/raw/fields.csv
  ../data-models/source-mappings/raw/alignment_*.csv
  ../business-processes/canonical-processes/raw/citations.csv
  ../business-processes/canonical-processes/processes/*.md (for titles)

Writes:
  wiki/agent-docs/by_resource/<resource_lower>.md
  wiki/agent-docs/_index.md
  raw/integration_index.csv

Phase: Emit (deterministic, no hand-edits to outputs).
Owner: scripts/01_emit_resource_views.py - do NOT hand-edit any of
the files listed under "Writes".

Determinism contract:
  - Re-running this script with no input changes MUST produce
    zero-byte diffs in every output file.
  - All iteration is over sorted collections.
  - All paths are relative; no timestamps appear in output bodies.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = KB_ROOT.parent

RESO_RAW = DOCS_ROOT / "data-models" / "reso-dd-kb" / "raw"
RESO_RES_DOCS = DOCS_ROOT / "data-models" / "reso-dd-kb" / "wiki" / "agent-docs" / "resources"
SM_RAW = DOCS_ROOT / "data-models" / "source-mappings" / "raw"
SM_BY_RES = DOCS_ROOT / "data-models" / "source-mappings" / "wiki" / "agent-docs" / "by_resource"
CP_RAW = DOCS_ROOT / "business-processes" / "canonical-processes" / "raw"
CP_PROCESSES = DOCS_ROOT / "business-processes" / "canonical-processes" / "processes"

OUT_BY_RES = KB_ROOT / "wiki" / "agent-docs" / "by_resource"
OUT_INDEX = KB_ROOT / "wiki" / "agent-docs" / "_index.md"
OUT_INTEGRATION_CSV = KB_ROOT / "raw" / "integration_index.csv"

# Hand-encoded Sharp-SIR (Layer 4) flavour mapping. Resource ->
# list of (relative-from-by_resource/, label) tuples.
FLAVOUR_LINKS: dict[str, list[tuple[str, str]]] = {
    "Property": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (seller-side Kanban)"),
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (buyer-side Kanban)"),
        ("../../../../business-processes/listing-checklist.md", "listing-checklist.md (broker / marketing / finance checklists)"),
    ],
    "Contacts": [
        ("../../../../business-processes/lead-qualification.md", "lead-qualification.md (MQL -> SQL)"),
        ("../../../../business-processes/follow-up-vs-active-sales.md", "follow-up-vs-active-sales.md (Follow-up vs Active boundary)"),
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (buyer-side Kanban)"),
    ],
    "Showing": [
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (Solution / Viewing stage)"),
        ("../../../../business-processes/follow-up-vs-active-sales.md", "follow-up-vs-active-sales.md (first-showing trigger)"),
    ],
    "ShowingRequest": [
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (Solution / Viewing stage)"),
    ],
    "ShowingAppointment": [
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (Solution / Viewing stage)"),
    ],
    "ShowingAvailability": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (Active Listing stage)"),
    ],
    "LockOrBox": [
        ("../../../../business-processes/listing-checklist.md", "listing-checklist.md (broker access / lockbox steps)"),
    ],
    "OpenHouse": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (Active Listing stage marketing tasks)"),
    ],
    "Caravan": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (Active Listing stage marketing tasks)"),
    ],
    "CaravanStop": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (Active Listing stage marketing tasks)"),
    ],
    "Media": [
        ("../../../../business-processes/listing-checklist.md", "listing-checklist.md (marketing checklist)"),
    ],
    "TransactionManagement": [
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (Deal Signing / Payment / Closed)"),
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (SOLD / AGENT COMMISSION / CLOSED)"),
    ],
    "HistoryTransactional": [
        ("../../../../business-processes/listing-pipeline.md", "listing-pipeline.md (every stage transition writes history)"),
        ("../../../../business-processes/sales-pipeline.md", "sales-pipeline.md (every stage transition writes history)"),
    ],
}

# Resources that Layer 2 (source-mappings) covers. Used to compute
# the Layer-2 link / row-count.
SM_RESOURCES = ["Property", "Member", "Office", "Contacts", "Teams", "Media"]


def load_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def reso_resource_index() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in load_csv(RESO_RAW / "resources.csv"):
        out[r["ResourceName"]] = r
    return out


def reso_field_count() -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    for r in load_csv(RESO_RAW / "fields.csv"):
        out[r["ResourceName"]] += 1
    return out


def sm_alignment_counts() -> dict[str, int]:
    out: dict[str, int] = {}
    for res in SM_RESOURCES:
        path = SM_RAW / f"alignment_{res.lower()}.csv"
        rows = load_csv(path)
        if rows:
            out[res] = len(rows)
    return out


def cp_resource_to_processes() -> dict[str, list[str]]:
    """Read citations.csv; map ResourceName -> sorted list of process file names."""
    out: dict[str, set[str]] = defaultdict(set)
    for c in load_csv(CP_RAW / "citations.csv"):
        if c["citation_kind"] == "Resource":
            out[c["citation_value"]].add(c["process"])
        elif c["citation_kind"] == "Field":
            res = c["citation_value"].split(".", 1)[0]
            out[res].add(c["process"])
    return {k: sorted(v) for k, v in out.items()}


def process_titles() -> dict[str, str]:
    out: dict[str, str] = {}
    if not CP_PROCESSES.is_dir():
        return out
    H1 = re.compile(r"^#\s+(?P<title>.+)$", re.MULTILINE)
    for p in sorted(CP_PROCESSES.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        m = H1.search(text)
        out[p.name] = m.group("title").strip() if m else p.name
    return out


def reso_resource_doc_path(resource: str) -> str:
    """Compute relative path from by_resource/<res>.md to reso-dd-kb resource doc."""
    snake = resource.lower()
    candidate = RESO_RES_DOCS / f"{snake}.md"
    if candidate.is_file():
        return f"../../../../data-models/reso-dd-kb/wiki/agent-docs/resources/{snake}.md"
    return ""


def sm_by_resource_path(resource: str) -> str:
    snake = resource.lower()
    if (SM_BY_RES / f"{snake}.md").is_file():
        return f"../../../../data-models/source-mappings/wiki/agent-docs/by_resource/{snake}.md"
    return ""


def cp_process_path(process_filename: str) -> str:
    return f"../../../../business-processes/canonical-processes/processes/{process_filename}"


def emit_resource_page(
    resource: str,
    reso_meta: dict,
    field_count: int,
    sm_count: int | None,
    sm_link: str,
    processes: list[str],
    titles: dict[str, str],
    flavour_links: list[tuple[str, str]],
    reso_doc_link: str,
) -> str:
    layers_present: list[int] = [1]
    if sm_count is not None:
        layers_present.append(2)
    if processes:
        layers_present.append(3)
    if flavour_links:
        layers_present.append(4)
    layer_summary = ", ".join(f"L{i}" for i in layers_present)

    lines: list[str] = []
    lines.append(f"# Integrated view: `{resource}`\n")
    lines.append(
        "Generated by "
        "`docs/integration/scripts/01_emit_resource_views.py`. Do NOT "
        "hand-edit. Re-run after changing any source-of-record "
        "chapter (`reso-dd-kb`, `source-mappings`, "
        "`canonical-processes`) or any Sharp-SIR flavour mapping in "
        "the script's `FLAVOUR_LINKS`.\n"
    )

    lines.append("## Summary\n")
    lines.append("| Property | Value |")
    lines.append("|---|---|")
    lines.append(f"| Resource | `{resource}` |")
    lines.append(f"| Layers covering this resource | {layer_summary} |")
    lines.append(f"| RESO field count | {field_count} |")
    if sm_count is not None:
        lines.append(f"| Source-mapping rows (Layer 2) | {sm_count} |")
    if processes:
        lines.append(f"| Canonical processes citing this (Layer 3) | {len(processes)} |")
    if flavour_links:
        lines.append(f"| Sharp-SIR flavour docs (Layer 4) | {len(flavour_links)} |")
    lines.append("")

    # Layer 1 - Canonical RESO definition
    lines.append("## Layer 1 - Canonical RESO definition\n")
    desc = (reso_meta.get("Description") or "").strip()
    if desc:
        lines.append(f"> {desc}\n")
    if reso_doc_link:
        lines.append(
            f"Full per-resource agent doc (resources, fields, lookups): "
            f"[`reso-dd-kb/wiki/agent-docs/resources/{resource.lower()}.md`]"
            f"({reso_doc_link})."
        )
    else:
        lines.append(
            "_(no per-resource agent doc emitted by `reso-dd-kb`; "
            "consult the raw CSVs at "
            "`data-models/reso-dd-kb/raw/{resources,fields,"
            "lookup_values}.csv`.)_"
        )
    lines.append("")

    # Layer 2 - Source mappings
    lines.append("## Layer 2 - Source mappings\n")
    if sm_count is not None and sm_link:
        lines.append(
            f"Curated mappings: **{sm_count}** rows in "
            f"`alignment_{resource.lower()}.csv`. Per-resource doc: "
            f"[`source-mappings/wiki/agent-docs/by_resource/"
            f"{resource.lower()}.md`]({sm_link})."
        )
    else:
        lines.append(
            "_Not yet in scope of the 6-resource Layer-2 curated "
            "set. Promote by adding rows to "
            "`data-models/source-mappings/raw/mapping_curated.csv` "
            "and re-running its emit pipeline._"
        )
    lines.append("")

    # Layer 3 - Canonical state machines
    lines.append("## Layer 3 - Canonical state machines\n")
    if processes:
        lines.append("Canonical processes citing this resource:\n")
        for p in processes:
            title = titles.get(p, p)
            lines.append(f"- [{title}]({cp_process_path(p)}) (`{p}`)")
        lines.append("")
    else:
        lines.append(
            "_No canonical process currently cites this resource. "
            "Add one under "
            "`business-processes/canonical-processes/processes/` "
            "if a state machine is needed._\n"
        )

    # Layer 4 - Sharp-SIR flavour
    lines.append("## Layer 4 - Sharp-SIR flavour\n")
    if flavour_links:
        lines.append("Project-flavour pipelines / checklists touching this resource:\n")
        for href, label in flavour_links:
            lines.append(f"- [{label}]({href})")
        lines.append("")
    else:
        lines.append(
            "_No project-flavour SOP yet for this resource. The "
            "canonical baseline (Layer 3) is currently the SOP. "
            "Promote a `docs/business-processes/<flavour>.md` doc "
            "when Sharp-SIR codifies its operational flow and add "
            "the link to `FLAVOUR_LINKS` in "
            "`scripts/01_emit_resource_views.py`._\n"
        )

    lines.append("## Determinism\n")
    lines.append(
        "This page is mechanically derived from the four source-of-"
        "record chapters. Edits MUST happen in those chapters; this "
        "page is regenerated by re-running the emit script."
    )

    return "\n".join(lines) + "\n"


def emit_index_page(
    rows: list[dict],
    titles_by_proc: dict[str, str],
    reso_meta: dict[str, dict],
) -> str:
    lines: list[str] = []
    lines.append("# Integrated views - agent index\n")
    lines.append(
        "Generated by "
        "`docs/integration/scripts/01_emit_resource_views.py`. "
        "Do NOT hand-edit.\n"
    )
    lines.append(
        "Per-resource one-stop pages joining Layer 1 (canonical RESO "
        "data model), Layer 2 (source mappings), Layer 3 (canonical "
        "state machines), and Layer 4 (Sharp-SIR flavour). See "
        "[`../../../INTEGRATION.md`](../../../INTEGRATION.md) for the "
        "layered architecture.\n"
    )
    lines.append("## Resource catalogue\n")
    lines.append("| Resource | Layers | RESO fields | Source-mapping rows | Canonical processes | Sharp-SIR docs | Page |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows:
        page = f"by_resource/{r['resource'].lower()}.md"
        lines.append(
            f"| `{r['resource']}` "
            f"| {r['layers']} "
            f"| {r['reso_field_count']} "
            f"| {r['sm_row_count'] or '-'} "
            f"| {r['cp_process_count']} "
            f"| {r['flavour_link_count']} "
            f"| [{r['resource'].lower()}.md]({page}) |"
        )
    lines.append("")
    lines.append("## Roll-up totals\n")
    lines.append(f"- Resources with integrated views: **{len(rows)}**")
    lines.append(
        f"- Resources covered by Layer 2 (source mappings): "
        f"**{sum(1 for r in rows if r['sm_row_count'])}**"
    )
    lines.append(
        f"- Resources covered by Layer 3 (canonical processes): "
        f"**{sum(1 for r in rows if r['cp_process_count'])}**"
    )
    lines.append(
        f"- Resources covered by Layer 4 (Sharp-SIR flavour): "
        f"**{sum(1 for r in rows if r['flavour_link_count'])}**"
    )
    lines.append(
        f"- Resources covered by all four layers: "
        f"**{sum(1 for r in rows if r['layers'] == 'L1, L2, L3, L4')}**"
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    if not RESO_RAW.is_dir():
        print(f"ERROR: missing {RESO_RAW}", file=sys.stderr)
        return 2
    if not CP_RAW.is_dir():
        print(f"ERROR: missing {CP_RAW}", file=sys.stderr)
        return 2

    reso_meta = reso_resource_index()
    field_counts = reso_field_count()
    sm_counts = sm_alignment_counts()
    cp_map = cp_resource_to_processes()
    titles = process_titles()

    # Resource set: Layer-2 + Layer-3 union, restricted to RESO-known
    # resources only (so we never emit a page for an unknown name).
    resource_set: set[str] = set()
    resource_set.update(sm_counts.keys())
    resource_set.update(cp_map.keys())
    resource_set &= set(reso_meta.keys())

    OUT_BY_RES.mkdir(parents=True, exist_ok=True)
    OUT_INTEGRATION_CSV.parent.mkdir(parents=True, exist_ok=True)

    # Track files we should keep this run; everything else under
    # by_resource/ that we previously emitted but no longer should is
    # removed for cleanliness.
    kept: set[str] = set()

    rows_for_index: list[dict] = []

    for resource in sorted(resource_set):
        sm_count = sm_counts.get(resource)
        sm_link = sm_by_resource_path(resource) if resource in sm_counts else ""
        processes = cp_map.get(resource, [])
        flavour_links = FLAVOUR_LINKS.get(resource, [])
        reso_doc_link = reso_resource_doc_path(resource)

        page = emit_resource_page(
            resource=resource,
            reso_meta=reso_meta[resource],
            field_count=field_counts.get(resource, 0),
            sm_count=sm_count,
            sm_link=sm_link,
            processes=processes,
            titles=titles,
            flavour_links=flavour_links,
            reso_doc_link=reso_doc_link,
        )
        out = OUT_BY_RES / f"{resource.lower()}.md"
        out.write_text(page, encoding="utf-8")
        kept.add(out.name)

        layers = ["L1"]
        if sm_count is not None:
            layers.append("L2")
        if processes:
            layers.append("L3")
        if flavour_links:
            layers.append("L4")
        rows_for_index.append(
            {
                "resource": resource,
                "layers": ", ".join(layers),
                "reso_field_count": field_counts.get(resource, 0),
                "sm_row_count": sm_count or 0,
                "cp_process_count": len(processes),
                "flavour_link_count": len(flavour_links),
            }
        )

    # Cleanliness: remove any stale by_resource/*.md files no longer
    # in the kept set. This keeps re-runs deterministic when the
    # upstream resource set shrinks.
    for existing in OUT_BY_RES.glob("*.md"):
        if existing.name not in kept:
            existing.unlink()

    rows_for_index.sort(key=lambda r: r["resource"])

    OUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    OUT_INDEX.write_text(
        emit_index_page(rows_for_index, titles, reso_meta),
        encoding="utf-8",
    )

    with OUT_INTEGRATION_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "resource",
                "layers",
                "reso_field_count",
                "sm_row_count",
                "cp_process_count",
                "flavour_link_count",
            ],
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(rows_for_index)

    print(
        f"[01] emit_resource_views: emitted "
        f"{len(rows_for_index)} resource page(s) -> wiki/agent-docs/by_resource/, "
        f"_index.md ({OUT_INDEX.stat().st_size}B), "
        f"raw/integration_index.csv ({len(rows_for_index)} rows)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
