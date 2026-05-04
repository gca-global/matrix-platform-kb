#!/usr/bin/env python3
"""Render reso-dd-kb/wiki/resources/<Resource>.md from raw/*.csv.

Idempotent rebuild step of the RESO DD LLM KB. Inputs in raw/:
    fields.csv               (parsed from RESO_Data_Dictionary_2.0.xlsx)
    lookups.csv              (parsed from RESO_Data_Dictionary_2.0.xlsx)
    field_descriptions.csv   (dumped from public.reso_field_descriptions)
    field_metadata.csv       (scraped via fetch_field_metadata.py from dd.reso.org)
    resource_metadata.csv    (scraped via fetch_resource_metadata.py)
    lookup_metadata.csv      (scraped via fetch_lookup_metadata.py)
    field_usage.csv          (RESO certification stats, fallback Org%)
    resource_usage.csv       (per-resource adoption summary)

Output: wiki/resources/<Resource>.md (one file per RESO Resource).

The page anatomy follows AGENTS.md:
    Overview line  ->  Groups section  ->  Fields table
    (Field | Type | Group | Lookup | Org% | Description | Source)  ->  Lookups section.

Source links go to dd.reso.org (DDwiki was retired in favour of dd.reso.org).

Run: `python3 reso-dd-kb/scripts/refresh.py`
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT_DIR = ROOT / "wiki" / "resources"


def load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def first_nonempty(*vals: str) -> str:
    for v in vals:
        if v:
            s = str(v).strip()
            if s and s not in ("--", "—"):
                return s
    return ""


def md_escape(s: str) -> str:
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def first_sentence(text: str, max_len: int = 200) -> str:
    if not text:
        return ""
    s = text.strip()
    for i, ch in enumerate(s):
        if ch in ".!?" and i + 1 < len(s) and s[i + 1] in (" ", "\n"):
            return s[: i + 1].strip()
    return (s[:max_len] + ("…" if len(s) > max_len else "")).strip()


def load_all():
    fields = load_csv(RAW / "fields.csv")
    lookups = load_csv(RAW / "lookups.csv")
    descriptions = {r["field"]: r for r in load_csv(RAW / "field_descriptions.csv")}
    metadata = {(r["Resource"], r["Field"]): r for r in load_csv(RAW / "field_metadata.csv")}
    usage = {(r["Resource"], r["Field"]): r for r in load_csv(RAW / "field_usage.csv")}
    resource_usage = {r["Resource"]: r for r in load_csv(RAW / "resource_usage.csv")}
    resource_metadata = {r["Resource"]: r for r in load_csv(RAW / "resource_metadata.csv")}
    lookup_metadata = {r["LookupName"]: r for r in load_csv(RAW / "lookup_metadata.csv")}
    return (fields, lookups, descriptions, metadata, usage, resource_usage,
            resource_metadata, lookup_metadata)


def lookups_for(lookup_name: str, lookups: list[dict]) -> list[dict]:
    if not lookup_name:
        return []
    return [r for r in lookups if r.get("LookupName") == lookup_name]


def render_resource(
    resource: str,
    rows: list[dict],
    lookups: list[dict],
    descriptions: dict,
    metadata: dict,
    usage: dict,
    resource_usage: dict,
    resource_metadata: dict,
    lookup_metadata: dict,
) -> str:
    out: list[str] = []
    out.append(f"# {resource}")
    out.append("")

    res_meta = resource_metadata.get(resource, {})
    overview = first_nonempty(
        res_meta.get("Definition"),
        descriptions.get(resource, {}).get("description"),
    )
    if overview:
        out.append(overview)
    else:
        out.append(f"_RESO Data Dictionary 2.0 resource — {len(rows)} fields. See "
                   f"[dd.reso.org]({_resource_source_url(resource)}) for the canonical page._")
    out.append("")

    if res_meta.get("FieldCount") or res_meta.get("LastRevised"):
        bits = []
        fc = res_meta.get("FieldCount") or ""
        lr = res_meta.get("LastRevised") or ""
        if fc:
            bits.append(f"{fc} fields")
        if lr:
            bits.append(f"last revised {lr}")
        bits.append(f"[dd.reso.org]({_resource_source_url(resource)})")
        out.append("**RESO DD 2.0** — " + " · ".join(bits))
        out.append("")

    ru = resource_usage.get(resource)
    if ru:
        out.append(
            f"**Adoption** — weighted Org%: **{round(float(ru.get('WeightedOrgPct') or 0))}%** "
            f"across {ru.get('FieldsWithUsage')} measured fields "
            f"(median {round(float(ru.get('MedianOrgPct') or 0))}%, "
            f"avg {round(float(ru.get('AvgOrgPct') or 0))}%)."
        )
        out.append("")

    by_group: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        g = first_nonempty(r.get("Groups"), "Other")
        by_group[g].append(r)

    out.append("## Groups")
    out.append("")
    for g in sorted(by_group):
        out.append(f"- **{g}** — {len(by_group[g])} fields")
    out.append("")

    out.append("## Fields")
    out.append("")
    out.append("| Field | Type | Group | Lookup | Org% | Description | Source |")
    out.append("|---|---|---|---|---|---|---|")

    for r in sorted(rows, key=lambda x: x.get("StandardName", "")):
        field = r.get("StandardName", "")
        meta = metadata.get((resource, field), {})
        usg = usage.get((resource, field), {})
        desc = descriptions.get(field, {}).get("description", "")
        source_url = first_nonempty(
            meta.get("SourceUrl"),
            _field_source_url(resource, field),
        )

        org_pct = first_nonempty(meta.get("OrgPct"), usg.get("OrgPct"))
        org_pct = f"{org_pct}%" if org_pct else ""

        lookup_name = first_nonempty(r.get("LookupName"), meta.get("Lookup"))
        lookup_md = f"[{lookup_name}](#{_anchor(lookup_name)})" if lookup_name and lookups_for(lookup_name, lookups) else (lookup_name or "")

        source_md = f"[link]({source_url})" if source_url else ""

        out.append(
            "| "
            + " | ".join([
                md_escape(f"`{field}`"),
                md_escape(first_nonempty(meta.get("DataType"), r.get("SimpleDataType"))),
                md_escape(first_nonempty(meta.get("Group"), r.get("Groups"))),
                lookup_md,
                org_pct,
                md_escape(first_sentence(desc) or first_sentence(r.get("Definition", ""))),
                source_md,
            ])
            + " |"
        )

    out.append("")

    field_details_rows = [r for r in rows
                          if any(metadata.get((resource, r.get("StandardName", "")), {}).get(k)
                                 for k in ("BEDES", "PropertyTypes", "SpanishName",
                                           "FrenchCanadianName", "StatusChangeDate", "RevisionDate"))]
    if field_details_rows:
        out.append("## Field details")
        out.append("")
        out.append("Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type"
                   " applicability, Spanish / French-Canadian display names, change-history dates).")
        out.append("")
        for r in sorted(field_details_rows, key=lambda x: x.get("StandardName", "")):
            field = r.get("StandardName", "")
            meta = metadata.get((resource, field), {})
            extras: list[str] = []
            for label, key in [
                ("BEDES", "BEDES"),
                ("Property Types", "PropertyTypes"),
                ("Status", "FieldStatus"),
                ("Spanish Name", "SpanishName"),
                ("French-Canadian Name", "FrenchCanadianName"),
                ("Status Change Date", "StatusChangeDate"),
                ("Revision Date", "RevisionDate"),
                ("Added in Version", "AddedInVersion"),
            ]:
                v = meta.get(key)
                if v:
                    extras.append(f"  - **{label}:** {v}")
            if extras:
                out.append(f"<details><summary><code>{field}</code></summary>")
                out.append("")
                out.extend(extras)
                out.append("")
                out.append("</details>")
                out.append("")

    used_lookup_names = sorted({first_nonempty(r.get("LookupName")) for r in rows
                                if first_nonempty(r.get("LookupName"))})
    rendered_lookups = [n for n in used_lookup_names if lookups_for(n, lookups)]
    if rendered_lookups:
        out.append("## Lookups")
        out.append("")
        for name in rendered_lookups:
            out.append(f"### {name}")
            out.append("")
            lk_meta = lookup_metadata.get(name, {})
            if lk_meta.get("ValueCount") or lk_meta.get("UsedByCount") or lk_meta.get("SourceUrl"):
                bits = []
                if lk_meta.get("ValueCount"):
                    bits.append(f"{lk_meta['ValueCount']} values")
                if lk_meta.get("UsedByCount"):
                    bits.append(f"used by {lk_meta['UsedByCount']} field(s)")
                if lk_meta.get("SourceUrl"):
                    bits.append(f"[dd.reso.org]({lk_meta['SourceUrl']})")
                out.append(" · ".join(bits))
                out.append("")
            out.append("| Value | Definition |")
            out.append("|---|---|")
            for lr in lookups_for(name, lookups):
                val = first_nonempty(lr.get("StandardLookupValue"), lr.get("LegacyODataValue"))
                out.append(f"| `{md_escape(val)}` | {md_escape(first_sentence(lr.get('Definition', '')))} |")
            out.append("")

    out.append("---")
    out.append(f"_Generated by `reso-dd-kb/scripts/refresh.py` on {dt.date.today().isoformat()} "
               f"from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._")
    out.append("")

    return "\n".join(out)


def _anchor(name: str) -> str:
    return name.lower()


def _resource_source_url(resource: str) -> str:
    return f"https://dd.reso.org/DD2.0/{resource}/"


def _field_source_url(resource: str, field: str) -> str:
    return f"https://dd.reso.org/DD2.0/{resource}/{field}/"


def main() -> int:
    (fields, lookups, descriptions, metadata, usage, resource_usage,
     resource_metadata, lookup_metadata) = load_all()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    by_resource: dict[str, list[dict]] = defaultdict(list)
    for r in fields:
        by_resource[r["ResourceName"]].append(r)

    for resource, rows in sorted(by_resource.items()):
        md = render_resource(resource, rows, lookups, descriptions, metadata,
                             usage, resource_usage, resource_metadata, lookup_metadata)
        out_path = OUT_DIR / f"{resource}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"  wrote {out_path.relative_to(ROOT)}  ({len(rows)} fields)")

    print(f"done. {len(by_resource)} resource files in {OUT_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
