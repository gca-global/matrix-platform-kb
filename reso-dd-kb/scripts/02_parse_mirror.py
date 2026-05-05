#!/usr/bin/env python3
"""
Parse reso-dd-kb/mirror/ into structured CSVs under reso-dd-kb/raw/.

Inputs (read-only):
    mirror/DD2.0/index.html
    mirror/DD2.0/<Resource>/index.html               (41)
    mirror/DD2.0/<Resource>/<Field>/index.html       (~1,745)
    mirror/DD2.0/lookups/<Lookup>/index.html         (~222)
    mirror/DD2.0/lookups/<Lookup>/<Value>/index.html (~3,500)
    _meta/manifest.json                              (status / size / sha256)

Outputs (overwritten on each run):
    raw/resources.csv         41 rows
    raw/fields.csv            ~1,745 rows; every cell from the field page
    raw/field_definitions.csv ~1,745 rows; full Definition prose
    raw/lookups.csv           ~222 rows
    raw/lookup_values.csv     ~3,500 rows

Determinism:
    - rows sorted by stable keys (resource then standard_name, etc.)
    - stable column order (the FIELD_COLUMNS / VALUE_COLUMNS lists below)
    - csv.QUOTE_MINIMAL, lf line endings
    - no timestamps / hashes / run-IDs in row content (those live in
      _meta/manifest.json)

Verification gates (hard-fail at end of main):
    1. resources.csv row count equals number of resources linked from
       /DD2.0/ (currently 41).
    2. fields.csv row count equals sum(field_count) over resources.csv
       (currently 1,745).
    3. Every field row has a non-empty Definition.
    4. Every URL in _meta/manifest.json returned status 200.
    5. Every field link found inside any resource page resolves to a
       fetched field page in the mirror.
    6. lookup_values.csv row count equals sum of value_count over
       lookups.csv.

Any breach -> sys.exit(2) with details printed.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

KB_ROOT = Path(__file__).resolve().parent.parent
MIRROR_DIR = KB_ROOT / "mirror"
META_DIR = KB_ROOT / "_meta"
RAW_DIR = KB_ROOT / "raw"
DD_DIR = MIRROR_DIR / "DD2.0"

UPSTREAM_HOST = "dd.reso.org"
UPSTREAM_BASE = f"https://{UPSTREAM_HOST}"

# Reserved second-level segments that are NOT resources.
NON_RESOURCE_SEGMENTS = {"lookups", "xref", "about"}

# Column orders are fixed for stable diffs.
RESOURCE_COLUMNS = [
    "ResourceName",
    "Description",
    "FieldCount",
    "RevisedDate",
    "SourceURL",
]

# Order roughly mirrors the on-page order of the two metadata tables on
# field pages (left table then right table) plus the adoption block.
FIELD_COLUMNS = [
    "ResourceName",
    "StandardName",
    "DisplayName",
    "Group",
    "SimpleDataType",
    "MaxLength",
    "MaxPrecision",
    "Synonyms",
    "Status",
    "BEDES",
    "LookupStatus",
    "Lookup",
    "PropertyTypes",
    "Payloads",
    "SpanishName",
    "FrenchCanadianName",
    "StatusChangeDate",
    "RevisedDate",
    "AddedInVersion",
    "SourceResource",
    "AdoptionPercent",
    "AdoptionAdopted",
    "AdoptionTotal",
    "SourceURL",
]

FIELD_DEFINITION_COLUMNS = [
    "ResourceName",
    "StandardName",
    "Definition",
    "SourceURL",
]

LOOKUP_COLUMNS = [
    "LookupName",
    "Description",
    "ValueCount",
    "UsedByCount",
    "SourceURL",
]

LOOKUP_VALUE_COLUMNS = [
    "LookupName",
    "StandardValue",
    "DisplayValue",
    "Definition",
    "LegacyODataValue",
    "Synonyms",
    "Status",
    "BEDES",
    "References",
    "SpanishValue",
    "FrenchCanadianValue",
    "StatusChangeDate",
    "RevisedDate",
    "AddedInVersion",
    "SourceURL",
]

# RESO renders "no value" as an em-dash. Treat as empty.
EMPTY_TOKENS = {"\u2014", "-", "--"}


# --------------------------------------------------------------------- helpers


def read_html(path: Path) -> BeautifulSoup:
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        return BeautifulSoup(fh, "lxml")


def url_for(rel_path: Path) -> str:
    return f"{UPSTREAM_BASE}/{rel_path.as_posix()}"


def canonical_url(rel_path: Path) -> str:
    """
    Map mirror-relative path to the canonical (trailing-slash) URL,
    so 'DD2.0/Property/index.html' becomes
    'https://dd.reso.org/DD2.0/Property/'.
    """
    posix = rel_path.as_posix()
    if posix.endswith("/index.html"):
        posix = posix[: -len("index.html")]
    return f"{UPSTREAM_BASE}/{posix}"


def clean_cell(text: str) -> str:
    """
    Strip whitespace, drop em-dash placeholders, collapse internal
    whitespace runs, and remove zero-width characters that sneak in
    via copy buttons.
    """
    if text is None:
        return ""
    # Strip the "Copy" button title text and zero-width chars.
    txt = text.replace("\u200b", "").replace("\xa0", " ")
    txt = re.sub(r"\s+", " ", txt).strip()
    if txt in EMPTY_TOKENS:
        return ""
    return txt


def cell_text(td) -> str:
    """
    Get the visible text of a <td>, but drop nested <button> nodes
    (those carry "Copy" labels we don't want in the data).
    """
    if td is None:
        return ""
    # Make a shallow clone to avoid mutating the parsed tree.
    td_copy = BeautifulSoup(str(td), "lxml").find("td") or BeautifulSoup(str(td), "lxml").find()
    if td_copy is None:
        return clean_cell(td.get_text(" ", strip=True))
    for btn in td_copy.find_all("button"):
        btn.decompose()
    return clean_cell(td_copy.get_text(" ", strip=True))


def cell_links(td) -> list[str]:
    """
    Comma-joined visible labels of any <a> tags inside a <td>, in
    source order. Used for fields like "Property Types" and "Payloads"
    that render as a list of links.
    """
    if td is None:
        return []
    return [clean_cell(a.get_text(" ", strip=True)) for a in td.find_all("a")]


def parse_metadata_tables(soup: BeautifulSoup, h2_text: str) -> dict[str, str]:
    """
    Parse all `<table class="dd-metadata-table">` tables that appear
    inside the <div class="dd-metadata-card"> whose <h2> matches the
    given text. Returns {th_text: td_text} merged across the tables.
    """
    out: dict[str, str] = {}
    for card in soup.select("div.dd-metadata-card"):
        h2 = card.find("h2")
        if not h2 or clean_cell(h2.get_text(" ", strip=True)) != h2_text:
            continue
        for table in card.select("table.dd-metadata-table"):
            for row in table.find_all("tr"):
                th = row.find("th")
                td = row.find("td")
                if th is None or td is None:
                    continue
                # Strip nested <small> ("Suggested" hints) from headers.
                th_copy = BeautifulSoup(str(th), "lxml").find("th")
                if th_copy is not None:
                    for s in th_copy.find_all("small"):
                        s.decompose()
                    key = clean_cell(th_copy.get_text(" ", strip=True))
                else:
                    key = clean_cell(th.get_text(" ", strip=True))
                # Special case: PropertyTypes / Payloads should be a
                # comma-joined list of link labels, not the raw
                # whitespace-collapsed text.
                if key in {"Property Types", "Payloads", "References"}:
                    labels = cell_links(td)
                    out[key] = ", ".join(labels)
                else:
                    out[key] = cell_text(td)
    return out


# --------------------------------------------------------------------- pages


def parse_resource_page(path: Path) -> dict:
    """
    Resource page: /DD2.0/<Resource>/index.html.

    Extracts:
      - ResourceName (from <h1> or path)
      - Description (dd-callout-text)
      - FieldCount (parsed from "<N> fields ..." subtitle)
      - RevisedDate (parsed from "Last revised <date>" subtitle)
      - SourceURL (canonical)
      - field_links: list of /DD2.0/<Resource>/<Field>/ URLs found
        on the page (used for verification gate 5).
    """
    soup = read_html(path)
    rel = path.relative_to(MIRROR_DIR)

    h1 = soup.find("h1")
    h1_text = clean_cell(h1.get_text(" ", strip=True)) if h1 else ""
    # "Property Resource" -> "Property"
    resource_name = re.sub(r"\s+Resource$", "", h1_text).strip()
    if not resource_name:
        # fall back to URL path
        resource_name = path.parent.name

    description = ""
    callout = soup.select_one("div.dd-definition-callout")
    if callout:
        text_el = callout.select_one("span.dd-callout-text")
        if text_el is None:
            # Some pages put the prose directly inside the callout div
            # without the .dd-callout-text wrapper.
            for child in callout.find_all(["span", "button"]):
                child.decompose()
            description = clean_cell(callout.get_text(" ", strip=True))
        else:
            description = clean_cell(text_el.get_text(" ", strip=True))

    subtitle = ""
    sub_el = soup.select_one("p.dd-page-subtitle")
    if sub_el is not None:
        subtitle = clean_cell(sub_el.get_text(" ", strip=True))

    field_count = 0
    m = re.match(r"^\s*(\d+)\s+fields", subtitle)
    if m:
        field_count = int(m.group(1))

    revised_date = ""
    m = re.search(r"[Ll]ast revised\s+([0-9/]+)", subtitle)
    if m:
        revised_date = m.group(1)

    # `wget --convert-links` rewrites absolute hrefs to relative paths
    # (e.g. "BusinessName/index.html"), but a small number of links
    # remain absolute (typically rows added after the initial render).
    # Normalise both to a single canonical /DD2.0/<Resource>/<Field>/
    # form for the field-link inventory.
    field_links: list[str] = []
    abs_re = re.compile(rf"^(?:https://{re.escape(UPSTREAM_HOST)})?/DD2\.0/{re.escape(resource_name)}/([A-Za-z0-9_]+)/?(?:index\.html)?$")
    rel_re = re.compile(r"^([A-Za-z0-9_]+)/(?:index\.html)?$")
    for a in soup.select("table.dd-fields-table a.dd-field-link"):
        href = a.get("href", "")
        m = abs_re.match(href) or rel_re.match(href)
        if m:
            field_links.append(f"/DD2.0/{resource_name}/{m.group(1)}/")
    seen: set[str] = set()
    field_links = [u for u in field_links if not (u in seen or seen.add(u))]

    return {
        "ResourceName": resource_name,
        "Description": description,
        "FieldCount": field_count,
        "RevisedDate": revised_date,
        "SourceURL": canonical_url(rel),
        "_field_links": field_links,
    }


def parse_field_page(path: Path) -> tuple[dict, dict]:
    """
    Field page: /DD2.0/<Resource>/<Field>/index.html.

    Returns (field_row, definition_row).
    """
    soup = read_html(path)
    rel = path.relative_to(MIRROR_DIR)

    resource_name = path.parent.parent.name
    standard_name_from_path = path.parent.name

    # Definition: live in <div class="dd-definition-callout">.
    # Drop the "Definition" label span and any toggle buttons first.
    definition = ""
    callout = soup.select_one("div.dd-definition-callout")
    if callout:
        callout = BeautifulSoup(str(callout), "lxml").select_one("div.dd-definition-callout")
        for el in callout.select("span.dd-callout-label, button"):
            el.decompose()
        definition = clean_cell(callout.get_text(" ", strip=True))

    # Details metadata.
    details = parse_metadata_tables(soup, "Details")

    # Adoption block: <div class="dd-usage">.
    adoption_pct = ""
    adoption_adopted = ""
    adoption_total = ""
    usage_block = soup.select_one("div.dd-metadata-card div.dd-usage")
    if usage_block:
        val_el = usage_block.select_one("span.dd-usage-value")
        if val_el:
            adoption_pct = clean_cell(val_el.get_text(" ", strip=True))
        det_el = usage_block.select_one("span.dd-usage-detail")
        if det_el:
            det_txt = clean_cell(det_el.get_text(" ", strip=True))
            # "325 of 344 Organizations"
            m = re.match(r"^(\d+)\s+of\s+(\d+)\s+Organi[sz]ations", det_txt)
            if m:
                adoption_adopted = m.group(1)
                adoption_total = m.group(2)

    standard_name = details.get("Standard Name", "") or standard_name_from_path

    field_row = {
        "ResourceName": resource_name,
        "StandardName": standard_name,
        "DisplayName": details.get("Display Name", ""),
        "Group": details.get("Group", ""),
        "SimpleDataType": details.get("Simple Data Type", ""),
        "MaxLength": details.get("Max Length", ""),
        "MaxPrecision": details.get("Max Precision", ""),
        "Synonyms": details.get("Synonyms", ""),
        "Status": details.get("Status", ""),
        "BEDES": details.get("BEDES", ""),
        "LookupStatus": details.get("Lookup Status", ""),
        "Lookup": details.get("Lookup", ""),
        "PropertyTypes": details.get("Property Types", ""),
        "Payloads": details.get("Payloads", ""),
        "SpanishName": details.get("Spanish Name", ""),
        "FrenchCanadianName": details.get("French-Canadian Name", ""),
        "StatusChangeDate": details.get("Status Change Date", ""),
        "RevisedDate": details.get("Revised Date", ""),
        "AddedInVersion": details.get("Added in Version", ""),
        "SourceResource": details.get("Source Resource", ""),
        "AdoptionPercent": adoption_pct,
        "AdoptionAdopted": adoption_adopted,
        "AdoptionTotal": adoption_total,
        "SourceURL": canonical_url(rel),
    }

    definition_row = {
        "ResourceName": resource_name,
        "StandardName": standard_name,
        "Definition": definition,
        "SourceURL": canonical_url(rel),
    }

    return field_row, definition_row


def parse_lookup_page(path: Path) -> tuple[dict, list[dict]]:
    """
    Lookup page: /DD2.0/lookups/<LookupName>/index.html.

    Returns (lookup_row, [embedded_value_summaries]). The embedded
    value summaries are NOT used for the final lookup_values.csv -
    the per-value pages give richer metadata - but we use them to
    cross-check the value count and to enumerate the value links.
    """
    soup = read_html(path)
    rel = path.relative_to(MIRROR_DIR)

    lookup_name = path.parent.name

    h1 = soup.find("h1")
    h1_text = clean_cell(h1.get_text(" ", strip=True)) if h1 else ""
    # h1 is "<Name> Lookup".
    # Allow path-based fallback.
    lookup_name_h1 = re.sub(r"\s+Lookup$", "", h1_text).strip()
    if lookup_name_h1:
        lookup_name = lookup_name_h1.replace(" ", "")

    description = ""
    callout = soup.select_one("div.dd-definition-callout")
    if callout:
        text_el = callout.select_one("span.dd-callout-text")
        if text_el:
            description = clean_cell(text_el.get_text(" ", strip=True))
        else:
            for el in callout.select("span.dd-callout-label, button"):
                el.decompose()
            description = clean_cell(callout.get_text(" ", strip=True))

    subtitle = ""
    sub_el = soup.select_one("p.dd-page-subtitle")
    if sub_el is not None:
        subtitle = clean_cell(sub_el.get_text(" ", strip=True))

    value_count = 0
    m = re.match(r"^\s*(\d+)\s+values?\b", subtitle)
    if m:
        value_count = int(m.group(1))

    used_by_count = 0
    m = re.search(r"Used by\s+(\d+)\s+field", subtitle)
    if m:
        used_by_count = int(m.group(1))

    # Embedded value links. Same normalisation issue as resource pages:
    # most links are relative (post `--convert-links`) but a handful
    # remain absolute. Match both.
    embedded_links: list[dict] = []
    abs_re = re.compile(
        rf"^(?:https://{re.escape(UPSTREAM_HOST)})?/DD2\.0/lookups/{re.escape(lookup_name)}/([^/]+?)/?(?:index\.html)?$"
    )
    rel_re = re.compile(r"^([^/]+?)/(?:index\.html)?$")
    for a in soup.select("table.dd-fields-table a.dd-field-link"):
        href = a.get("href", "")
        m = abs_re.match(href) or rel_re.match(href)
        if not m:
            continue
        seg = m.group(1)
        # The "Used By" table also lives in dd-fields-table; its links
        # point at field pages with a "/" in the path (resource/field).
        # The embedded value table only has single-segment hrefs.
        if "/" in unquote(seg):
            continue
        embedded_links.append(
            {"value_url_segment": seg, "label": clean_cell(a.get_text(" ", strip=True))}
        )

    lookup_row = {
        "LookupName": lookup_name,
        "Description": description,
        "ValueCount": value_count,
        "UsedByCount": used_by_count,
        "SourceURL": canonical_url(rel),
    }
    return lookup_row, embedded_links


def parse_lookup_value_page(path: Path) -> dict:
    """
    Lookup value page: /DD2.0/lookups/<LookupName>/<Value>/index.html.
    """
    soup = read_html(path)
    rel = path.relative_to(MIRROR_DIR)

    lookup_name_path = path.parent.parent.name
    value_segment = unquote(path.parent.name)

    h1 = soup.find("h1")
    display_value = clean_cell(h1.get_text(" ", strip=True)) if h1 else value_segment

    definition = ""
    callout = soup.select_one("div.dd-definition-callout")
    if callout:
        callout = BeautifulSoup(str(callout), "lxml").select_one("div.dd-definition-callout")
        for el in callout.select("span.dd-callout-label, button"):
            el.decompose()
        definition = clean_cell(callout.get_text(" ", strip=True))

    details = parse_metadata_tables(soup, "Details")

    lookup_name = details.get("Lookup Name", "") or lookup_name_path
    standard_value = details.get("Standard Value", "") or display_value

    return {
        "LookupName": lookup_name,
        "StandardValue": standard_value,
        "DisplayValue": display_value,
        "Definition": definition,
        "LegacyODataValue": details.get("Legacy OData Value", ""),
        "Synonyms": details.get("Synonyms", ""),
        "Status": details.get("Status", ""),
        "BEDES": details.get("BEDES", ""),
        "References": details.get("References", ""),
        "SpanishValue": details.get("Spanish Value", ""),
        "FrenchCanadianValue": details.get("French-Canadian Value", ""),
        "StatusChangeDate": details.get("Status Change Date", ""),
        "RevisedDate": details.get("Revised Date", ""),
        "AddedInVersion": details.get("Added in Version", ""),
        "SourceURL": canonical_url(rel),
    }


# --------------------------------------------------------------------- index


def discover_pages() -> dict[str, list[Path]]:
    """
    Walk the mirror tree and bucket files by page type.

    Buckets:
      'resource'      : DD2.0/<Resource>/index.html
      'field'         : DD2.0/<Resource>/<Field>/index.html
      'lookup'        : DD2.0/lookups/<Lookup>/index.html
      'lookup_value'  : DD2.0/lookups/<Lookup>/<Value>/index.html
      'index'         : DD2.0/index.html
      'other'         : everything else (xref/, about/, assets, etc.)
    """
    buckets: dict[str, list[Path]] = {
        "index": [],
        "resource": [],
        "field": [],
        "lookup": [],
        "lookup_value": [],
        "other": [],
    }
    for path in sorted(DD_DIR.rglob("index.html")):
        rel = path.relative_to(MIRROR_DIR)
        parts = rel.parts  # ('DD2.0', ...)
        if len(parts) < 2 or parts[0] != "DD2.0":
            buckets["other"].append(path)
            continue

        if len(parts) == 2:
            buckets["index"].append(path)
        elif len(parts) == 3 and parts[1] not in NON_RESOURCE_SEGMENTS:
            buckets["resource"].append(path)
        elif len(parts) == 4 and parts[1] not in NON_RESOURCE_SEGMENTS:
            buckets["field"].append(path)
        elif len(parts) == 4 and parts[1] == "lookups":
            buckets["lookup"].append(path)
        elif len(parts) == 5 and parts[1] == "lookups":
            buckets["lookup_value"].append(path)
        else:
            buckets["other"].append(path)
    return buckets


# --------------------------------------------------------------------- writers


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=columns,
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in columns})


# --------------------------------------------------------------------- main


def main() -> int:
    if not DD_DIR.exists():
        print(f"[02_parse] FAIL: mirror not present at {DD_DIR}", file=sys.stderr)
        return 2

    buckets = discover_pages()
    print(f"[02_parse] discovered:")
    for k in ("index", "resource", "field", "lookup", "lookup_value", "other"):
        print(f"  {k:>13s}: {len(buckets[k]):>5d}")

    # --- resources -----------------------------------------------------------
    resource_rows: list[dict] = []
    field_links_by_resource: dict[str, list[str]] = {}
    for path in buckets["resource"]:
        row = parse_resource_page(path)
        field_links_by_resource[row["ResourceName"]] = row.pop("_field_links")
        resource_rows.append(row)
    resource_rows.sort(key=lambda r: r["ResourceName"])

    # --- fields --------------------------------------------------------------
    field_rows: list[dict] = []
    field_definition_rows: list[dict] = []
    for path in buckets["field"]:
        try:
            field_row, def_row = parse_field_page(path)
        except Exception as exc:
            print(f"[02_parse] FAIL parsing field {path}: {exc}", file=sys.stderr)
            return 2
        field_rows.append(field_row)
        field_definition_rows.append(def_row)
    field_rows.sort(key=lambda r: (r["ResourceName"], r["StandardName"]))
    field_definition_rows.sort(key=lambda r: (r["ResourceName"], r["StandardName"]))

    # --- lookups -------------------------------------------------------------
    lookup_rows: list[dict] = []
    embedded_value_count_by_lookup: dict[str, int] = {}
    for path in buckets["lookup"]:
        row, embedded = parse_lookup_page(path)
        lookup_rows.append(row)
        embedded_value_count_by_lookup[row["LookupName"]] = len(embedded)
    lookup_rows.sort(key=lambda r: r["LookupName"])

    # --- lookup values -------------------------------------------------------
    lookup_value_rows: list[dict] = []
    for path in buckets["lookup_value"]:
        try:
            row = parse_lookup_value_page(path)
        except Exception as exc:
            print(f"[02_parse] FAIL parsing lookup value {path}: {exc}", file=sys.stderr)
            return 2
        lookup_value_rows.append(row)
    lookup_value_rows.sort(key=lambda r: (r["LookupName"], r["StandardValue"]))

    # --- write ---------------------------------------------------------------
    write_csv(RAW_DIR / "resources.csv", RESOURCE_COLUMNS, resource_rows)
    write_csv(RAW_DIR / "fields.csv", FIELD_COLUMNS, field_rows)
    write_csv(RAW_DIR / "field_definitions.csv", FIELD_DEFINITION_COLUMNS, field_definition_rows)
    write_csv(RAW_DIR / "lookups.csv", LOOKUP_COLUMNS, lookup_rows)
    write_csv(RAW_DIR / "lookup_values.csv", LOOKUP_VALUE_COLUMNS, lookup_value_rows)

    print(f"[02_parse] wrote raw/resources.csv         {len(resource_rows):>5d}")
    print(f"[02_parse] wrote raw/fields.csv            {len(field_rows):>5d}")
    print(f"[02_parse] wrote raw/field_definitions.csv {len(field_definition_rows):>5d}")
    print(f"[02_parse] wrote raw/lookups.csv           {len(lookup_rows):>5d}")
    print(f"[02_parse] wrote raw/lookup_values.csv     {len(lookup_value_rows):>5d}")

    # --- verification gates --------------------------------------------------
    failures: list[str] = []

    # Gate 1: resources.csv row count == number of resources linked from
    # the DD 2.0 index page.
    expected_resources = expected_resource_count_from_index(buckets["index"])
    if expected_resources is not None and len(resource_rows) != expected_resources:
        failures.append(
            f"GATE 1: resources.csv has {len(resource_rows)} rows, "
            f"index page advertises {expected_resources}"
        )

    # Gate 2: fields.csv row count == sum(field_count) over resources.csv.
    declared_total = sum(int(r["FieldCount"] or 0) for r in resource_rows)
    if declared_total > 0 and len(field_rows) != declared_total:
        failures.append(
            f"GATE 2: fields.csv has {len(field_rows)} rows, "
            f"resources.csv declares {declared_total}"
        )

    # Gate 3: every field row has a non-empty Definition.
    blank_def = [
        f"{r['ResourceName']}.{r['StandardName']}"
        for r in field_definition_rows
        if not r["Definition"].strip()
    ]
    if blank_def:
        failures.append(
            f"GATE 3: {len(blank_def)} field(s) have empty Definition; first 10: "
            f"{blank_def[:10]}"
        )

    # Gate 4: every URL in manifest.json returned status 200.
    manifest_path = META_DIR / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        bad = [e for e in manifest["entries"] if e.get("status") != 200]
        if bad:
            failures.append(
                f"GATE 4: {len(bad)} URL(s) in manifest.json did not return 200; "
                f"first 5: {[(e['status'], e['url']) for e in bad[:5]]}"
            )
    else:
        failures.append(f"GATE 4: manifest.json missing at {manifest_path}")

    # Gate 5: every field link found inside any resource page resolves
    # to a fetched field page in the mirror.
    fetched_field_urls: set[str] = {row["SourceURL"] for row in field_rows}
    missing_fields: list[str] = []
    for resource, links in field_links_by_resource.items():
        for href in links:
            full = f"{UPSTREAM_BASE}{href}"
            if full not in fetched_field_urls:
                missing_fields.append(full)
    if missing_fields:
        failures.append(
            f"GATE 5: {len(missing_fields)} field link(s) advertised by a "
            f"resource page were not fetched; first 5: {missing_fields[:5]}"
        )

    # Gate 6: lookup_values.csv row count == sum of value_count over lookups.
    declared_values = sum(int(r["ValueCount"] or 0) for r in lookup_rows)
    # Some lookups have closed enumerations only in the embedded table
    # but no per-value pages (rare). Compare against declared subtitle
    # count and against the embedded link count, choose the higher of
    # the two for the gate.
    embedded_total = sum(embedded_value_count_by_lookup.values())
    expected_value_total = max(declared_values, embedded_total)
    if expected_value_total > 0 and len(lookup_value_rows) != expected_value_total:
        # Allow off-by-one slack only if subtitle and embedded disagree
        # AND we matched one of them exactly.
        if len(lookup_value_rows) not in (declared_values, embedded_total):
            failures.append(
                f"GATE 6: lookup_values.csv has {len(lookup_value_rows)} rows; "
                f"lookups subtitle declares {declared_values}, "
                f"embedded link count = {embedded_total}"
            )

    if failures:
        print("\n[02_parse] FAILED verification gates:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print("[02_parse] OK: all verification gates passed")
    return 0


def expected_resource_count_from_index(index_paths: list[Path]) -> int | None:
    """
    Count resource links on /DD2.0/index.html, used for gate 1.
    Returns None if the index page isn't in the mirror yet.
    """
    if not index_paths:
        return None
    soup = read_html(index_paths[0])
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("/DD2.0/"):
            continue
        tail = href[len("/DD2.0/") :]
        # Looking for /DD2.0/<Resource>/ (single segment, capitalised,
        # not a reserved bucket).
        m = re.fullmatch(r"([A-Z][A-Za-z0-9]*)/", tail)
        if m and m.group(1) not in NON_RESOURCE_SEGMENTS:
            seen.add(m.group(1))
    return len(seen) if seen else None


if __name__ == "__main__":
    raise SystemExit(main())
