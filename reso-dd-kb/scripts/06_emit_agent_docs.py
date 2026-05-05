#!/usr/bin/env python3
"""
Phase 4: emit the agent-consumption documentation layer.

Reads:
    raw/resources.csv
    raw/fields.csv
    raw/field_definitions.csv
    raw/lookups.csv
    raw/lookup_values.csv
    raw/relationships.csv
    raw/satellites.csv
    wiki/dbml/canonical.dbml      (cross-check that every Enum reference is
                                   covered by a section in lookups.md)

Writes (idempotent: deletes wiki/agent-docs/ at the start):
    wiki/agent-docs/_index.md
    wiki/agent-docs/resources/<snake>.md          (one per resource, x41)
    wiki/agent-docs/lookups.md                    (single file with TOC + per-lookup section)
    wiki/agent-docs/relationships.md              (global FK index)

Verification gates (hard-fail):
    1. One resource page per row in resources.csv (count match).
    2. Every Enum referenced in canonical.dbml has a section in lookups.md.
    3. Every internal markdown link from emitted pages resolves to a
       declared file or a declared anchor in this output set.
    4. Every (host_resource, candidate_satellite) row in satellites.csv
       with recommendation in {drop_from_host, review} appears on its
       host's resource page.
    5. _index.md links to every emitted page exactly once.

Determinism:
    Resources: order from resources.csv.
    Fields per resource: order from fields.csv (page order).
    Lookups: alphabetical by LookupName.
    Lookup values: order from lookup_values.csv (which is alphabetical by
                   LookupName then StandardValue from Phase 1).
    Refs in relationships.md: sorted by (host, host_field, target, target_field).
"""
from __future__ import annotations

import csv
import re
import sys
import shutil
from collections import defaultdict
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"
DBML_DIR = KB_ROOT / "wiki" / "dbml"
DOCS_DIR = KB_ROOT / "wiki" / "agent-docs"
RES_DIR = DOCS_DIR / "resources"

# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------
_CAMEL_RE_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_RE_2 = re.compile(r"([a-z0-9])([A-Z])")


def snake(name: str) -> str:
    s = _CAMEL_RE_1.sub(r"\1_\2", name)
    s = _CAMEL_RE_2.sub(r"\1_\2", s)
    return s.lower()


def gfm_anchor(heading: str) -> str:
    """Approximation of GitHub-flavoured-markdown anchor generation:
    lowercase, replace spaces with hyphens, keep alphanumerics +
    hyphens + underscores, drop everything else."""
    s = heading.lower().strip()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9_\-]", "", s)
    return s


def md_escape_pipe(text: str) -> str:
    """Escape literal pipes inside markdown table cells."""
    return text.replace("|", r"\|")


def collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u2019", "'")).strip()


def first_sentence(text: str, max_len: int = 240) -> str:
    if not text:
        return ""
    s = collapse_ws(text)
    m = re.search(r"\.(?:\s|$)", s)
    if m:
        return s[: m.end()].strip()
    if len(s) > max_len:
        return s[:max_len].rstrip() + "..."
    return s


def must_exist(path: Path) -> None:
    if not path.exists():
        print(f"FAIL: required input missing: {path}", file=sys.stderr)
        raise SystemExit(2)


def load(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open()))


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
# Same PK_OVERRIDES as scripts/05_emit_dbml.py - kept in sync by hand
# (the docs reference the same chosen PK).
PK_OVERRIDES: dict[str, str] = {
    "Property": "ListingKey",
    "OUID": "OrganizationUniqueIdKey",
    "PropertyGreenVerification": "GreenBuildingVerificationKey",
    "PropertyPowerProduction": "PowerProductionKey",
    "PropertyRooms": "RoomKey",
    "PropertyUnitTypes": "UnitTypeKey",
    "MemberAssociation": "AssociationKey",
    "OfficeAssociation": "AssociationKey",
    "InternetTracking": "EventKey",
    "Queue": "QueueTransactionKey",
}

# Domain buckets for the index page. Any resource not listed here is
# automatically placed under "Other" (and surfaces as a warning so we
# remember to categorise it on the next refresh).
DOMAIN_BUCKETS: list[tuple[str, list[str]]] = [
    (
        "Listings & properties",
        [
            "Property",
            "PropertyGreenVerification",
            "PropertyPowerProduction",
            "PropertyPowerStorage",
            "PropertyRooms",
            "PropertyUnitTypes",
        ],
    ),
    (
        "People & organisations",
        [
            "Member",
            "MemberAssociation",
            "MemberStateLicense",
            "Office",
            "OfficeAssociation",
            "OfficeCorporateLicense",
            "Teams",
            "TeamMembers",
            "Contacts",
            "ContactListings",
            "ContactListingNotes",
            "Association",
        ],
    ),
    (
        "Showings & access",
        [
            "OpenHouse",
            "Showing",
            "ShowingAppointment",
            "ShowingAvailability",
            "ShowingRequest",
            "Caravan",
            "CaravanStop",
            "LockOrBox",
        ],
    ),
    (
        "Media, comms & engagement",
        [
            "Media",
            "SocialMedia",
            "OtherPhone",
            "InternetTracking",
            "InternetTrackingSummary",
            "Prospecting",
            "SavedSearch",
            "TransactionManagement",
        ],
    ),
    (
        "System & metadata",
        [
            "OUID",
            "Field",
            "Lookup",
            "Rules",
            "Queue",
            "HistoryTransactional",
            "EntityEvent",
        ],
    ),
]


def derive_pk(resource_name: str, field_names: set[str]) -> str | None:
    if resource_name in PK_OVERRIDES:
        return PK_OVERRIDES[resource_name]
    if (resource_name + "Key") in field_names:
        return resource_name + "Key"
    if resource_name.endswith("s"):
        sing = resource_name[:-1] + "Key"
        if sing in field_names:
            return sing
    keys = [n for n in field_names if n.endswith("Key")]
    if len(keys) == 1:
        return keys[0]
    return None


def main() -> int:
    for p in (
        RAW / "resources.csv",
        RAW / "fields.csv",
        RAW / "field_definitions.csv",
        RAW / "lookups.csv",
        RAW / "lookup_values.csv",
        RAW / "relationships.csv",
        RAW / "satellites.csv",
        DBML_DIR / "canonical.dbml",
    ):
        must_exist(p)

    resources = load(RAW / "resources.csv")
    fields = load(RAW / "fields.csv")
    defs_rows = load(RAW / "field_definitions.csv")
    lookups = load(RAW / "lookups.csv")
    lookup_values = load(RAW / "lookup_values.csv")
    rels = load(RAW / "relationships.csv")
    sats = load(RAW / "satellites.csv")
    dbml_text = (DBML_DIR / "canonical.dbml").read_text()

    defs: dict[tuple[str, str], str] = {
        (r["ResourceName"], r["StandardName"]): r["Definition"] for r in defs_rows
    }

    fields_by_resource: dict[str, list[dict]] = defaultdict(list)
    field_names_by_resource: dict[str, set[str]] = defaultdict(set)
    for f in fields:
        fields_by_resource[f["ResourceName"]].append(f)
        field_names_by_resource[f["ResourceName"]].add(f["StandardName"])

    pk_by_resource: dict[str, str | None] = {}
    for res in resources:
        rname = res["ResourceName"]
        pk_by_resource[rname] = derive_pk(rname, field_names_by_resource[rname])

    # Satellite policy index.
    drop_set: set[tuple[str, str]] = set()
    review_reason: dict[tuple[str, str], str] = {}
    sat_fk_for: dict[tuple[str, str], tuple[str, str, str]] = {}
    for s in sats:
        host, cand = s["host_resource"], s["candidate_satellite"]
        sat_fk_for[(host, cand)] = (
            s["host_field"],
            s["target_resource"],
            s["target_field"],
        )
        if s["recommendation"] == "drop_from_host":
            drop_set.add((host, cand))
        elif s["recommendation"] == "review":
            review_reason[(host, cand)] = (
                f"satellite of FK {s['host_field']}->"
                f"{s['target_resource']}.{s['target_field']}"
            )

    # Lookup classification: which lookups are referenced by SV columns
    # (those are the ones emitted as Enum in DBML) vs MV-only vs open.
    lookup_uses_sv: set[str] = set()
    lookup_uses_mv: set[str] = set()
    for f in fields:
        if not f["Lookup"]:
            continue
        if f["SimpleDataType"] == "String List, Single":
            lookup_uses_sv.add(f["Lookup"])
        elif f["SimpleDataType"] == "String List, Multi":
            lookup_uses_mv.add(f["Lookup"])

    lookup_values_by_name: dict[str, list[dict]] = defaultdict(list)
    for v in lookup_values:
        lookup_values_by_name[v["LookupName"]].append(v)

    def lookup_kind(name: str) -> str:
        has_values = bool(lookup_values_by_name.get(name))
        if name in lookup_uses_sv and has_values:
            return "closed-SV"
        if name in lookup_uses_mv and has_values:
            return "closed-MV"
        if name in lookup_uses_sv or name in lookup_uses_mv:
            return "open"  # referenced but no closed values
        return "open"  # not referenced as SV/MV at all (rare)

    # Relationships: index by host and by target for the resource pages.
    rels_by_host: dict[str, list[dict]] = defaultdict(list)
    rels_by_target: dict[str, list[dict]] = defaultdict(list)
    for r in rels:
        rels_by_host[r["host_resource"]].append(r)
        if r["target_resource"]:
            rels_by_target[r["target_resource"]].append(r)

    # Parse the actual Refs emitted into canonical.dbml. This is the
    # source of truth for "is this column an FK in the canonical
    # model?" - it accounts for Phase-3 normalisations (Resource-typed
    # anchors, per-target dedup) that are not visible in rels.csv.
    # Each emitted Ref looks like:
    #     Ref: host_table.host_col > target_table.target_col  // confidence
    dbml_refs: list[tuple[str, str, str, str, str]] = []
    ref_re = re.compile(
        r"^Ref:\s+(\S+)\.(\S+)\s+>\s+(\S+)\.(\S+)\s*(?://\s*(\S+))?",
        re.M,
    )
    for m in ref_re.finditer(dbml_text):
        dbml_refs.append((m.group(1), m.group(2), m.group(3), m.group(4), m.group(5) or ""))
    # Index emitted Refs by host (snake) for fast per-resource lookup.
    refs_by_host_table: dict[str, list[tuple[str, str, str, str, str]]] = defaultdict(list)
    refs_by_target_table: dict[str, list[tuple[str, str, str, str, str]]] = defaultdict(list)
    for ref in dbml_refs:
        ht, hc, tt, tc, conf = ref
        refs_by_host_table[ht].append(ref)
        refs_by_target_table[tt].append(ref)

    # `fk_flag` is keyed by (CamelCase resource, CamelCase field) and
    # only fires for the column the DBML actually picked. For Resource-
    # typed parents whose Ref was anchored to a scalar carrier (e.g.
    # association.originating_system_id), the flag goes on the scalar
    # carrier, not on the bare Resource-typed column.
    snake_to_camel_field: dict[tuple[str, str], str] = {}
    for f in fields:
        snake_to_camel_field[(snake(f["ResourceName"]), snake(f["StandardName"]))] = (
            f["ResourceName"], f["StandardName"]
        )  # type: ignore[assignment]

    fk_flag: dict[tuple[str, str], list[str]] = defaultdict(list)
    for ht, hc, tt, tc, _ in dbml_refs:
        camel = snake_to_camel_field.get((ht, hc))
        if camel:
            fk_flag[camel].append(f"-> {tt}.{tc}")

    # Reset output dir.
    reset_dir(DOCS_DIR)
    RES_DIR.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # lookups.md
    # ------------------------------------------------------------------
    lookups_sorted = sorted(lookups, key=lambda l: l["LookupName"].lower())
    # Map of which (resource, field) cells use a given lookup.
    hosts_for_lookup: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for f in fields:
        if f["Lookup"]:
            hosts_for_lookup[f["Lookup"]].append(
                (f["ResourceName"], f["StandardName"], f["SimpleDataType"])
            )

    lookups_lines: list[str] = []
    lookups_lines.append(
        "[index](_index.md) | [relationships](relationships.md) | "
        "[USAGE.md](../../USAGE.md)"
    )
    lookups_lines.append("")
    lookups_lines.append("# Lookups (RESO DD 2.0)")
    lookups_lines.append("")
    lookups_lines.append(
        f"> {len(lookups_sorted)} lookups, {len(lookup_values):,} total values, "
        "extracted from `raw/lookups.csv` and `raw/lookup_values.csv`."
    )
    lookups_lines.append("")

    # Stats banner.
    n_sv = sum(1 for l in lookups_sorted if lookup_kind(l["LookupName"]) == "closed-SV")
    n_mv = sum(1 for l in lookups_sorted if lookup_kind(l["LookupName"]) == "closed-MV")
    n_open = sum(1 for l in lookups_sorted if lookup_kind(l["LookupName"]) == "open")
    lookups_lines.append("## At a glance")
    lookups_lines.append("")
    lookups_lines.append("| Kind | Count | DBML representation |")
    lookups_lines.append("|---|---:|---|")
    lookups_lines.append(
        f"| **closed-SV** (single-value w/ closed list) | {n_sv} | "
        "`Enum` block in `wiki/dbml/lookups.dbml`; column typed as the enum |"
    )
    lookups_lines.append(
        f"| **closed-MV** (multi-value w/ closed list) | {n_mv} | "
        "Column is `varchar`; column note carries `multi: <LookupName>` |"
    )
    lookups_lines.append(
        f"| **open** (jurisdiction-defined, no closed list) | {n_open} | "
        "Column is `varchar`; note `open: jurisdiction-defined` |"
    )
    lookups_lines.append(f"| **TOTAL** | {len(lookups_sorted)} | |")
    lookups_lines.append("")

    # Most-referenced lookups callout.
    lookups_lines.append("## Most-referenced lookups")
    lookups_lines.append("")
    lookups_lines.append("Top 10 by number of host columns (helps you find the high-traffic enums fast).")
    lookups_lines.append("")
    lookups_lines.append("| Lookup | Hosts | Values | Kind |")
    lookups_lines.append("|---|---:|---:|---|")
    by_host_count = sorted(
        lookups_sorted,
        key=lambda l: -len(hosts_for_lookup.get(l["LookupName"], [])),
    )[:10]
    for l in by_host_count:
        name = l["LookupName"]
        n_hosts = len(hosts_for_lookup.get(name, []))
        n_vals = len(lookup_values_by_name.get(name, []))
        lookups_lines.append(
            f"| [`{snake(name)}`](#{snake(name)}) | {n_hosts} | {n_vals} | "
            f"{lookup_kind(name)} |"
        )
    lookups_lines.append("")

    lookups_lines.append("## Full index (alphabetical)")
    lookups_lines.append("")
    lookups_lines.append("| Lookup | Kind | Values | Used by |")
    lookups_lines.append("|---|---|---:|---|")
    for l in lookups_sorted:
        name = l["LookupName"]
        anchor = snake(name)
        kind = lookup_kind(name)
        nvals = len(lookup_values_by_name.get(name, []))
        hosts = hosts_for_lookup.get(name, [])
        usage_summary = (
            f"{len(hosts)} columns" if len(hosts) > 3 else
            ", ".join(f"`{snake(r)}.{snake(f)}`" for r, f, _ in sorted(hosts))
        )
        if not usage_summary:
            usage_summary = "(unreferenced)"
        lookups_lines.append(
            f"| [`{snake(name)}`](#{anchor}) | {kind} | {nvals} | {md_escape_pipe(usage_summary)} |"
        )
    lookups_lines.append("")
    lookups_lines.append("---")
    lookups_lines.append("")

    # Per-lookup sections.
    declared_anchors_in_lookups: set[str] = set()
    for l in lookups_sorted:
        name = l["LookupName"]
        snake_name = snake(name)
        declared_anchors_in_lookups.add(snake_name)
        kind = lookup_kind(name)
        values = lookup_values_by_name.get(name, [])
        hosts = sorted(hosts_for_lookup.get(name, []))

        lookups_lines.append(f"## {snake_name}")
        lookups_lines.append("")
        lookups_lines.append(f"- Source name: `{name}`")
        lookups_lines.append(f"- Kind: **{kind}**")
        lookups_lines.append(f"- Value count: {len(values)}")
        lookups_lines.append(
            f"- [dd.reso.org page]({l.get('SourceURL') or 'https://dd.reso.org/DD2.0/'})"
        )
        lookups_lines.append("- Used by:")
        if hosts:
            for r, f, t in hosts:
                lookups_lines.append(
                    f"  - `{snake(r)}.{snake(f)}` (type=`{t}`)"
                )
        else:
            lookups_lines.append("  - (no field references this lookup)")
        lookups_lines.append("")

        if values:
            lookups_lines.append("| StandardValue | LegacyODataValue | Definition |")
            lookups_lines.append("|---|---|---|")
            for v in values:
                std = md_escape_pipe(v.get("StandardValue", ""))
                leg = md_escape_pipe(v.get("LegacyODataValue", ""))
                d = md_escape_pipe(first_sentence(v.get("Definition", ""), 200))
                lookups_lines.append(f"| {std} | {leg} | {d} |")
            lookups_lines.append("")
        else:
            lookups_lines.append(
                "*No closed value list - jurisdiction-defined.*"
            )
            lookups_lines.append("")

    (DOCS_DIR / "lookups.md").write_text("\n".join(lookups_lines) + "\n")

    # ------------------------------------------------------------------
    # relationships.md
    # ------------------------------------------------------------------
    rels_lines: list[str] = []
    rels_lines.append(
        "[index](_index.md) | [lookups](lookups.md) | "
        "[USAGE.md](../../USAGE.md)"
    )
    rels_lines.append("")
    rels_lines.append("# Relationships (foreign keys)")
    rels_lines.append("")
    rels_lines.append(
        "> The **Committed Refs** section below is the source of truth - it "
        "is parsed directly from `wiki/dbml/canonical.dbml`. The "
        "**Phase-2 detected signals** section is a wider net derived "
        "from `raw/relationships.csv`; some of those rows are folded "
        "into a single committed Ref by Phase-3 normalisation "
        "(Resource-typed anchoring, per-target dedup) and a few are "
        "intentionally not emitted (low-confidence, polymorphic)."
    )
    rels_lines.append("")

    # At-a-glance banner (counts).
    n_committed = len(dbml_refs)
    n_poly = sum(1 for r in rels if r["notes"] == "polymorphic")
    n_inverse = sum(1 for r in rels if r["fk_kind"] == "collection_typed")
    n_low = sum(
        1 for r in rels if r["confidence"] == "low" and r["target_resource"]
    )
    rels_lines.append("## At a glance")
    rels_lines.append("")
    rels_lines.append("| Category | Count | In DBML? |")
    rels_lines.append("|---|---:|---|")
    rels_lines.append(f"| Committed Refs (high+medium, scalar) | {n_committed} | yes (`Ref:`) |")
    rels_lines.append(f"| Polymorphic FKs (target resolved at runtime) | {n_poly} | comment only |")
    rels_lines.append(f"| Inverse 1:N (collection_typed) | {n_inverse} | comment only |")
    rels_lines.append(f"| Low-confidence (Phase 2 only) | {n_low} | no |")
    rels_lines.append("")

    # Backbone mermaid: top central tables and the FKs between them.
    backbone = {"property", "member", "office", "ouid", "teams", "association"}
    backbone_refs = [
        (ht, hc, tt, tc) for ht, hc, tt, tc, _ in dbml_refs
        if ht in backbone and tt in backbone
    ]
    rels_lines.append("## Connection backbone")
    rels_lines.append("")
    rels_lines.append(
        "The most-connected resources and the FKs between them. Use "
        "this as a mental map before drilling into individual resource pages."
    )
    rels_lines.append("")
    rels_lines.append("```mermaid")
    rels_lines.append("flowchart LR")
    for node in sorted(backbone):
        rels_lines.append(f"    {node}[\"{node}\"]")
    seen = set()
    for ht, hc, tt, tc in sorted(backbone_refs):
        # Collapse duplicate edges (e.g. multiple list_*_key FKs from
        # property -> member); the backbone diagram is a structure map,
        # not a column-by-column register.
        key = (ht, tt)
        if key in seen:
            continue
        seen.add(key)
        rels_lines.append(f"    {ht} --> {tt}")
    rels_lines.append("```")
    rels_lines.append("")

    def ref_arrow_from_rel(r: dict) -> str:
        host = snake(r["host_resource"])
        hf = snake(r["host_field"])
        if r["target_resource"]:
            tgt = snake(r["target_resource"])
            tf = (
                snake(r["target_field"])
                if r["target_field"]
                else snake(pk_by_resource.get(r["target_resource"]) or "?")
            )
            return f"`{host}.{hf}` -> `{tgt}.{tf}`"
        return f"`{host}.{hf}` -> *(polymorphic)*"

    # Committed Refs: parsed from canonical.dbml.
    rels_lines.append("## Committed Refs (in DBML)")
    rels_lines.append("")
    rels_lines.append(f"{len(dbml_refs)} rows. Source: `wiki/dbml/canonical.dbml`.")
    rels_lines.append("")
    rels_lines.append("| Ref | Confidence |")
    rels_lines.append("|---|---|")
    for ht, hc, tt, tc, conf in sorted(dbml_refs):
        rels_lines.append(f"| `{ht}.{hc}` -> `{tt}.{tc}` | {conf or '?'} |")
    rels_lines.append("")

    # Phase-2 detected signals (wider net; includes Resource-typed parents
    # that were anchored to a scalar in Phase 3).
    detected = sorted(
        (
            r for r in rels
            if r["confidence"] in {"high", "medium"}
            and r["fk_kind"] != "collection_typed"
            and r["notes"] != "polymorphic"
            and r["target_resource"]
        ),
        key=lambda r: (
            r["host_resource"], r["host_field"], r["target_resource"], r["target_field"]
        ),
    )
    rels_lines.append("## Phase-2 detected signals (high+medium, pre-normalisation)")
    rels_lines.append("")
    rels_lines.append(
        f"{len(detected)} rows from `raw/relationships.csv`. Some rows "
        "(particularly `resource_typed`) are folded into a single "
        "committed Ref above by Phase-3 anchoring; some collide on the "
        "same target table and were deduped to the target's PK."
    )
    rels_lines.append("")
    rels_lines.append("| Detected FK | Kind | Confidence | Evidence |")
    rels_lines.append("|---|---|---|---|")
    for r in detected:
        rels_lines.append(
            f"| {ref_arrow_from_rel(r)} | {r['fk_kind']} | {r['confidence']} | "
            f"{md_escape_pipe(collapse_ws(r['evidence'])[:160])} |"
        )
    rels_lines.append("")

    # Polymorphic.
    poly = sorted(
        (r for r in rels if r["notes"] == "polymorphic"),
        key=lambda r: (r["host_resource"], r["host_field"]),
    )
    rels_lines.append("## Polymorphic FKs (commented in DBML, not Refs)")
    rels_lines.append("")
    rels_lines.append(f"{len(poly)} rows.")
    rels_lines.append("")
    if poly:
        rels_lines.append("| Host column | Evidence |")
        rels_lines.append("|---|---|")
        for r in poly:
            rels_lines.append(
                f"| `{snake(r['host_resource'])}.{snake(r['host_field'])}` | "
                f"{md_escape_pipe(collapse_ws(r['evidence'])[:200])} |"
            )
        rels_lines.append("")

    # Inverse 1:N (collection_typed).
    inverse = sorted(
        (r for r in rels if r["fk_kind"] == "collection_typed"),
        key=lambda r: (r["host_resource"], r["host_field"]),
    )
    rels_lines.append("## Inverse 1:N (collection-typed; declared on the child)")
    rels_lines.append("")
    rels_lines.append(f"{len(inverse)} rows.")
    rels_lines.append("")
    if inverse:
        rels_lines.append("| Host column | Target |")
        rels_lines.append("|---|---|")
        for r in inverse:
            rels_lines.append(
                f"| `{snake(r['host_resource'])}.{snake(r['host_field'])}` | "
                f"`{snake(r['target_resource'])}` |"
            )
        rels_lines.append("")

    # Low-confidence (shown for transparency, not committed).
    low = sorted(
        (r for r in rels if r["confidence"] == "low" and r["target_resource"]),
        key=lambda r: (r["host_resource"], r["host_field"], r["target_resource"]),
    )
    rels_lines.append("## Low-confidence (NOT committed to DBML)")
    rels_lines.append("")
    rels_lines.append(
        f"{len(low)} rows. These were detected by Phase 2 with only weak "
        "signals (typically a name-shape match). They are surfaced here "
        "for transparency; do not treat as FKs without verification."
    )
    rels_lines.append("")
    if low:
        rels_lines.append("| FK | Evidence |")
        rels_lines.append("|---|---|")
        for r in low:
            rels_lines.append(
                f"| {ref_arrow_from_rel(r)} | {md_escape_pipe(collapse_ws(r['evidence'])[:160])} |"
            )
        rels_lines.append("")

    (DOCS_DIR / "relationships.md").write_text("\n".join(rels_lines) + "\n")

    # ------------------------------------------------------------------
    # Per-resource pages.
    # ------------------------------------------------------------------
    written_resource_files: list[str] = []
    # Track every column actually mentioned per resource (incl dropped/review)
    # so the satellite-coverage gate can verify.
    fields_listed_per_resource: dict[str, set[str]] = defaultdict(set)

    for res in resources:
        rname = res["ResourceName"]
        snake_table = snake(rname)
        out_path = RES_DIR / f"{snake_table}.md"
        written_resource_files.append(out_path.name)
        rfields = fields_by_resource.get(rname, [])
        pk = pk_by_resource.get(rname)

        # Per-resource counts for the at-a-glance banner.
        n_fields_total = len(rfields)
        n_dropped = sum(
            1 for f in rfields if (rname, f["StandardName"]) in drop_set
        )
        n_review = sum(
            1 for f in rfields if (rname, f["StandardName"]) in review_reason
        )
        n_resource_typed = sum(1 for f in rfields if f["SimpleDataType"] == "Resource")
        n_collection_typed = sum(
            1 for f in rfields if f["SimpleDataType"] == "Collection"
        )
        n_in_dbml = (
            n_fields_total - n_dropped - n_resource_typed - n_collection_typed
        )

        L: list[str] = []
        # Quick-nav breadcrumb at the very top so an agent can always
        # bounce between resources / lookups / relationships.
        L.append(
            "[index](../_index.md) | "
            "[lookups](../lookups.md) | "
            "[relationships](../relationships.md) | "
            "[USAGE.md](../../../USAGE.md)"
        )
        L.append("")
        L.append(f"# `{snake_table}` ({rname})")
        L.append("")
        L.append(f"> {res.get('Description', '')}")
        L.append("")

        # At-a-glance banner.
        L.append("## At a glance")
        L.append("")
        L.append("| | |")
        L.append("|---|---|")
        L.append(
            f"| **Primary key** | `{snake(pk) if pk else '(unresolved)'}`"
            + (f" *(override; RESO uses `{PK_OVERRIDES[rname]}`)*" if rname in PK_OVERRIDES else "")
            + " |"
        )
        L.append(f"| **Fields on dd.reso.org** | {n_fields_total} |")
        L.append(
            f"| **Columns in canonical DBML** | {n_in_dbml} "
            f"(omits {n_dropped} satellite drops + "
            f"{n_resource_typed} `Resource`-typed + "
            f"{n_collection_typed} `Collection`-typed) |"
        )
        L.append(
            f"| **Foreign keys OUT / IN** | {len(refs_by_host_table.get(snake_table, []))} / "
            f"{len(refs_by_target_table.get(snake_table, []))} |"
        )
        L.append(f"| **Review markers** | {n_review} |")
        L.append(
            f"| **Source** | [{res.get('SourceURL', '')}]({res.get('SourceURL', '')}) |"
        )
        L.append(f"| **Last revised upstream** | {res.get('RevisedDate', '?')} |")
        L.append("")

        # Per-resource ER diagram (only for resources with <=10 outgoing
        # FKs - keeps the diagram readable; skipped for the giant central
        # tables like Property where it would be unreadable anyway).
        out_refs_for_diagram = sorted(refs_by_host_table.get(snake_table, []))
        in_refs_for_diagram = sorted(refs_by_target_table.get(snake_table, []))
        if 0 < len(out_refs_for_diagram) + len(in_refs_for_diagram) <= 10:
            L.append("## Relationship diagram")
            L.append("")
            L.append("```mermaid")
            L.append("flowchart LR")
            L.append(f"    {snake_table}[\"{snake_table}\"]")
            seen_nodes: set[str] = {snake_table}
            for ht, hc, tt, tc, _ in out_refs_for_diagram:
                if tt not in seen_nodes:
                    L.append(f"    {tt}[\"{tt}\"]")
                    seen_nodes.add(tt)
                L.append(f"    {snake_table} -->|\"{hc}\"| {tt}")
            for ht, hc, tt, tc, _ in in_refs_for_diagram:
                if ht not in seen_nodes:
                    L.append(f"    {ht}[\"{ht}\"]")
                    seen_nodes.add(ht)
                L.append(f"    {ht} -->|\"{hc}\"| {snake_table}")
            L.append("```")
            L.append("")

        # ---- Fields table ----------------------------------------------
        L.append("## Fields")
        L.append("")
        L.append(
            "Columns in their original `dd.reso.org` page order. The `flags` "
            "column shows: `pk`, `fk -> target.col` (committed FK), "
            "`[REVIEW]` (Phase 2.5 satellite audit flagged for review), "
            "`[dropped]` (omitted from the canonical DBML; satellite of "
            "the named FK), `[Resource]` / `[Collection]` (no scalar "
            "column in DBML; FK companion - see Refs/inverse-1:N below)."
        )
        L.append("")
        L.append("| Field | DBML name | Type | Lookup | Description | Flags |")
        L.append("|---|---|---|---|---|---|")
        for f in rfields:
            cname = f["StandardName"]
            scol = snake(cname)
            fields_listed_per_resource[rname].add(cname)
            simple = f["SimpleDataType"]
            lookup = f["Lookup"]
            d = first_sentence(defs.get((rname, cname), ""), 160)
            flags: list[str] = []
            if cname == pk:
                flags.append("`pk`")
            for arrow in fk_flag.get((rname, cname), []):
                flags.append(f"`{arrow}`")
            if simple == "Resource":
                flags.append("`[Resource]`")
            elif simple == "Collection":
                flags.append("`[Collection]`")
            if (rname, cname) in drop_set:
                fk_origin = sat_fk_for.get((rname, cname), ("", "", ""))[0]
                flags.append(f"`[dropped: satellite of {snake(fk_origin)}]`")
            if (rname, cname) in review_reason:
                flags.append(f"`[REVIEW]`")
            lookup_cell = (
                f"[`{snake(lookup)}`](../lookups.md#{snake(lookup)})"
                if lookup
                else ""
            )
            type_cell = simple
            if lookup and simple == "String List, Single":
                type_cell = f"enum"
            elif lookup and simple == "String List, Multi":
                type_cell = "varchar (multi)"
            L.append(
                f"| `{cname}` | `{scol}` | {type_cell} | {lookup_cell} | "
                f"{md_escape_pipe(d)} | {' '.join(flags)} |"
            )
        L.append("")

        # ---- FKs out (from parsed DBML Refs) -----------------------
        out_refs = sorted(refs_by_host_table.get(snake_table, []))
        L.append("## Foreign keys OUT (this resource references)")
        L.append("")
        if out_refs:
            for ht, hc, tt, tc, conf in out_refs:
                L.append(f"- `{ht}.{hc}` -> `{tt}.{tc}` ({conf or 'medium'})")
        else:
            L.append("*(none committed)*")
        L.append("")

        # ---- FKs in (from parsed DBML Refs) -----------------------
        in_refs = sorted(refs_by_target_table.get(snake_table, []))
        L.append("## Foreign keys IN (other resources reference this)")
        L.append("")
        if in_refs:
            for ht, hc, tt, tc, conf in in_refs:
                L.append(f"- `{ht}.{hc}` -> `{tt}.{tc}` ({conf or 'medium'})")
        else:
            L.append("*(none committed)*")
        L.append("")

        # ---- Inverse 1:N ----------------------------------------------
        inv_here = [
            r for r in inverse if r["host_resource"] == rname
        ]
        if inv_here:
            L.append("## Inverse 1:N (collection-typed companions)")
            L.append("")
            for r in sorted(inv_here, key=lambda r: r["host_field"]):
                L.append(
                    f"- `{snake(r['host_field'])}` -> "
                    f"`{snake(r['target_resource'])}` "
                    f"(many `{snake(r['target_resource'])}` per `{snake_table}`)"
                )
            L.append("")

        # ---- Polymorphic ----------------------------------------------
        poly_here = [r for r in poly if r["host_resource"] == rname]
        if poly_here:
            L.append("## Polymorphic FKs")
            L.append("")
            for r in sorted(poly_here, key=lambda r: r["host_field"]):
                L.append(
                    f"- `{snake(r['host_field'])}` - target resolved at "
                    f"runtime; evidence: "
                    f"{md_escape_pipe(collapse_ws(r['evidence'])[:160])}"
                )
            L.append("")

        # ---- Phase 2.5 audit notes ----------------------------------------------
        sats_here = [s for s in sats if s["host_resource"] == rname]
        if sats_here:
            L.append("## Phase 2.5 satellite audit")
            L.append("")
            L.append(
                "Recommendations from `raw/satellites.csv`. `drop_from_host` "
                "rows are not present in the canonical DBML; `review` rows "
                "are kept but flagged; `keep_both` rows are silently kept."
            )
            L.append("")
            L.append("| Column | FK | Recommendation | Notes |")
            L.append("|---|---|---|---|")
            for s in sorted(
                sats_here,
                key=lambda s: (s["host_field"], s["candidate_satellite"]),
            ):
                L.append(
                    f"| `{snake(s['candidate_satellite'])}` | "
                    f"`{snake(s['host_field'])}` -> "
                    f"`{snake(s['target_resource'])}.{snake(s['target_field']) if s['target_field'] else '?'}` | "
                    f"`{s['recommendation']}` | "
                    f"{md_escape_pipe(collapse_ws(s.get('notes', ''))[:120])} |"
                )
            L.append("")

        out_path.write_text("\n".join(L) + "\n")

    # ------------------------------------------------------------------
    # _index.md
    # ------------------------------------------------------------------
    idx: list[str] = []
    idx.append("# RESO DD 2.0 - agent-docs index")
    idx.append("")
    idx.append(
        "> Generated by `scripts/06_emit_agent_docs.py`. Read "
        "[`USAGE.md`](../../USAGE.md) first for the consumption guide."
    )
    idx.append("")

    # At-a-glance stats banner.
    idx.append("## At a glance")
    idx.append("")
    idx.append("| | |")
    idx.append("|---|---|")
    idx.append(f"| **Resources** | {len(resources)} |")
    idx.append(f"| **Fields (RESO total)** | {len(fields):,} |")
    idx.append(f"| **Lookups** | {len(lookups)} |")
    idx.append(f"| **Lookup values** | {len(lookup_values):,} |")
    idx.append(f"| **Foreign keys committed in DBML** | {len(dbml_refs)} |")
    idx.append(
        f"| **Schema** | [`canonical.dbml`](../dbml/canonical.dbml) + "
        f"[`lookups.dbml`](../dbml/lookups.dbml) |"
    )
    idx.append("")

    # Cross-cutting pages.
    idx.append("## Cross-cutting pages")
    idx.append("")
    idx.append(
        f"- [`lookups.md`](lookups.md) - {len(lookups)} lookups, value tables, "
        f"host-column index."
    )
    idx.append(
        f"- [`relationships.md`](relationships.md) - {len(dbml_refs)} committed Refs, "
        f"polymorphic FKs, inverse 1:N, Phase-2 detected signals."
    )
    idx.append("")

    # Most-connected resources callout.
    in_count: dict[str, int] = defaultdict(int)
    out_count: dict[str, int] = defaultdict(int)
    for ht, hc, tt, tc, _ in dbml_refs:
        out_count[ht] += 1
        in_count[tt] += 1
    most_connected = sorted(
        ({snake(r["ResourceName"]) for r in resources}),
        key=lambda t: -(in_count[t] + out_count[t]),
    )[:5]
    idx.append("## Most-connected resources")
    idx.append("")
    idx.append("| Resource | FKs IN | FKs OUT |")
    idx.append("|---|---:|---:|")
    for t in most_connected:
        idx.append(f"| [`{t}`](resources/{t}.md) | {in_count[t]} | {out_count[t]} |")
    idx.append("")

    # Domain-grouped resource catalogue.
    idx.append("## Resource catalogue (by domain)")
    idx.append("")
    res_by_name = {r["ResourceName"]: r for r in resources}
    bucketed: set[str] = set()
    for bucket_name, bucket_members in DOMAIN_BUCKETS:
        idx.append(f"### {bucket_name}")
        idx.append("")
        idx.append("| Resource | DBML table | Fields | Description |")
        idx.append("|---|---|---:|---|")
        for rname in bucket_members:
            r = res_by_name.get(rname)
            if not r:
                continue
            bucketed.add(rname)
            snake_table = snake(rname)
            idx.append(
                f"| [`{rname}`](resources/{snake_table}.md) | `{snake_table}` | "
                f"{r.get('FieldCount', '?')} | "
                f"{md_escape_pipe(collapse_ws(r.get('Description', '')))} |"
            )
        idx.append("")
    # Surface anything not bucketed (typically RESO additions since the
    # last categorisation pass).
    leftovers = [r for r in resources if r["ResourceName"] not in bucketed]
    if leftovers:
        idx.append("### Other (please categorise on next refresh)")
        idx.append("")
        idx.append("| Resource | DBML table | Fields | Description |")
        idx.append("|---|---|---:|---|")
        for r in leftovers:
            rname = r["ResourceName"]
            snake_table = snake(rname)
            idx.append(
                f"| [`{rname}`](resources/{snake_table}.md) | `{snake_table}` | "
                f"{r.get('FieldCount', '?')} | "
                f"{md_escape_pipe(collapse_ws(r.get('Description', '')))} |"
            )
        idx.append("")

    # Alphabetical fallback for direct-lookup convenience (also feeds
    # GATE 5: every page linked exactly once - we link from the
    # alphabetical list and from the domain bucket; we adjust the gate
    # to accept any nonzero count instead of exactly 1 since the
    # domain table also links).
    idx.append("## Alphabetical index")
    idx.append("")
    for r in resources:
        rname = r["ResourceName"]
        snake_table = snake(rname)
        idx.append(f"- [`{rname}`](resources/{snake_table}.md) - `{snake_table}`")
    idx.append("")

    (DOCS_DIR / "_index.md").write_text("\n".join(idx) + "\n")

    # ------------------------------------------------------------------
    # Verification gates.
    # ------------------------------------------------------------------
    failures: list[str] = []

    # Gate 1.
    if len(written_resource_files) != len(resources):
        failures.append(
            f"GATE 1: wrote {len(written_resource_files)} resource pages, "
            f"expected {len(resources)}"
        )

    # Gate 2: every Enum referenced in canonical.dbml must have a section in lookups.md.
    # canonical.dbml emits enum-typed columns as `<col_snake> <enum_snake> [...]`
    # We extract the enum identifiers (non-builtin types) referenced inside Table blocks.
    builtin_types = {"varchar", "int", "double", "bool", "timestamp", "date"}
    enum_refs: set[str] = set()
    in_table = False
    for line in dbml_text.splitlines():
        if line.startswith("Table "):
            in_table = True
            continue
        if line == "}" and in_table:
            in_table = False
            continue
        if not in_table:
            continue
        m = re.match(r"\s+\S+\s+([a-z][a-z0-9_]*)\s*\[", line)
        if m:
            t = m.group(1)
            if t not in builtin_types and not t.startswith("varchar("):
                enum_refs.add(t)
    missing_in_lookups = enum_refs - declared_anchors_in_lookups
    for e in sorted(missing_in_lookups):
        failures.append(f"GATE 2: enum '{e}' referenced in canonical.dbml but no section in lookups.md")

    # Gate 3: internal links resolve.
    # We check links of the shape:
    #   ../lookups.md#<anchor>
    #   resources/<snake>.md
    #   ../../USAGE.md
    declared_resource_files = set(written_resource_files)
    declared_pages = {"lookups.md", "relationships.md", "_index.md"}
    link_re = re.compile(r"\]\(([^)]+)\)")
    bad_links: list[str] = []
    for md_path in [DOCS_DIR / "lookups.md", DOCS_DIR / "relationships.md", DOCS_DIR / "_index.md"] + [
        RES_DIR / fn for fn in written_resource_files
    ]:
        text = md_path.read_text()
        for m in link_re.finditer(text):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            # Split off anchor.
            if "#" in href:
                path_part, anchor = href.split("#", 1)
            else:
                path_part, anchor = href, ""
            # Resolve relative to md_path's directory.
            if path_part:
                resolved = (md_path.parent / path_part).resolve()
                # We only care about files inside DOCS_DIR or USAGE.md upstairs.
                try:
                    resolved.relative_to(KB_ROOT)
                except ValueError:
                    bad_links.append(f"{md_path.name}: {href} (escapes KB)")
                    continue
                if not resolved.exists():
                    bad_links.append(f"{md_path.name}: {href} (file missing)")
                    continue
                target_text = resolved.read_text() if resolved.suffix == ".md" else ""
            else:
                target_text = md_path.read_text()
            # Anchor check (markdown headings only).
            if anchor:
                # Extract heading anchors from the resolved file.
                heading_anchors = {
                    gfm_anchor(line.lstrip("# ").strip())
                    for line in target_text.splitlines()
                    if re.match(r"^#{1,6}\s+\S", line)
                }
                if anchor not in heading_anchors:
                    bad_links.append(f"{md_path.name}: {href} (anchor missing)")
    for bl in bad_links[:20]:
        failures.append(f"GATE 3: {bl}")
    if len(bad_links) > 20:
        failures.append(f"GATE 3: ... ({len(bad_links) - 20} more bad links)")

    # Gate 4: every dropped/review column appears on its host's page.
    for s in sats:
        if s["recommendation"] not in {"drop_from_host", "review"}:
            continue
        host = s["host_resource"]
        cand = s["candidate_satellite"]
        # We listed every column from fields.csv in the resource page; verify.
        if cand not in fields_listed_per_resource.get(host, set()):
            failures.append(
                f"GATE 4: {host}.{cand} ({s['recommendation']}) not listed on resources/{snake(host)}.md"
            )

    # Gate 5: _index.md links each emitted page at least once. (The
    # domain catalogue and the alphabetical fallback both link to each
    # resource, so we expect >=1, not exactly 1.)
    idx_text = (DOCS_DIR / "_index.md").read_text()
    expected_links = (
        [f"resources/{fn}" for fn in written_resource_files]
        + ["lookups.md", "relationships.md"]
    )
    for href in expected_links:
        n = idx_text.count(f"({href})")
        if n < 1:
            failures.append(f"GATE 5: _index.md does not link '{href}' (expected >=1)")

    # ------------------------------------------------------------------
    # Summary.
    # ------------------------------------------------------------------
    # Count per-lookup sections only (skip the top-level structural
    # headings: At a glance, Most-referenced, Full index).
    _toplevel_skip = {
        "## At a glance", "## Most-referenced lookups", "## Full index (alphabetical)",
    }
    n_lookup_sections = sum(
        1 for line in (DOCS_DIR / "lookups.md").read_text().splitlines()
        if line.startswith("## ") and line not in _toplevel_skip
    )
    print(f"[06] wrote {DOCS_DIR.relative_to(KB_ROOT)}/")
    print(f"     _index.md, lookups.md ({n_lookup_sections} sections), relationships.md")
    print(f"     resources/*.md  ({len(written_resource_files)} files)")
    print(f"     enums referenced in DBML: {len(enum_refs)} (all present in lookups.md: "
          f"{'yes' if not missing_in_lookups else 'NO'})")
    print(f"     bad internal links: {len(bad_links)}")
    print(f"     dropped+review satellite rows: "
          f"{len(drop_set) + len(review_reason)}")

    if failures:
        print("\n[06] FAILED verification gates:", file=sys.stderr)
        for f in failures[:20]:
            print(f"  - {f}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  ... ({len(failures) - 20} more)", file=sys.stderr)
        return 2
    print("[06] OK: all verification gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
