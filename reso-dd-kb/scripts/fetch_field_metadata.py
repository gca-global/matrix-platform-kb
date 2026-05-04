#!/usr/bin/env python3
"""Scrape dd.reso.org per-Field pages -> raw/field_metadata.csv.

Source: https://dd.reso.org/DD2.0/<Resource>/<Field>/

For every row in raw/fields.csv we GET the field's dd.reso.org page and
parse the two structured KV tables under '## Details' plus the '## Usage'
adoption block.

Output columns (rewritten from dd.reso.org; the old DDwiki SysPct family
is gone because dd.reso.org no longer publishes a per-system breakdown):

    Resource, Field, StandardName, DisplayName, Group, DataType,
    MaxLength, MaxPrecision, Synonyms, FieldStatus, BEDES, Lookup,
    LookupStatus, PropertyTypes, Payloads, SpanishName,
    FrenchCanadianName, StatusChangeDate, RevisionDate, AddedInVersion,
    SourceResource, OrgPct, OrgAdopted, OrgTotal, SourceUrl, FetchedAt

Politeness:
  * 5 concurrent connections max (ThreadPoolExecutor)
  * 100 ms gap between launches per worker
  * If-Modified-Since header from previous FetchedAt when the row exists
  * Exponential backoff on 429 / 503

Run: python3 reso-dd-kb/scripts/fetch_field_metadata.py
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import formatdate
from pathlib import Path
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
FIELDS_CSV = RAW / "fields.csv"
OUT_CSV = RAW / "field_metadata.csv"

SOURCE = "dd.reso.org/DD2.0"
URL_TMPL = "https://dd.reso.org/DD2.0/{resource}/{field}/"
UA = "matrix-platform-kb/1.0 (+https://github.com/sharpsir-group/matrix-platform-kb)"
WORKERS = 5
GAP_MS = 100
TIMEOUT = 25
MAX_RETRIES = 4

COLS = [
    "Resource", "Field", "StandardName", "DisplayName", "Group", "DataType",
    "MaxLength", "MaxPrecision", "Synonyms", "FieldStatus", "BEDES", "Lookup",
    "LookupStatus", "PropertyTypes", "Payloads", "SpanishName",
    "FrenchCanadianName", "StatusChangeDate", "RevisionDate", "AddedInVersion",
    "SourceResource", "OrgPct", "OrgAdopted", "OrgTotal", "SourceUrl", "FetchedAt",
]

# dd.reso.org left-cell label -> output column.
# Both Detail tables on a field page render under the same key/value shape;
# we walk every <tr> across every <table> on the page and bucket by label.
LABEL_MAP: dict[str, str] = {
    "standard name": "StandardName",
    "display name": "DisplayName",
    "group": "Group",
    "simple data type": "DataType",
    "max length suggested": "MaxLength",
    "max precision suggested": "MaxPrecision",
    "synonyms": "Synonyms",
    "status": "FieldStatus",
    "bedes": "BEDES",
    "lookup status": "LookupStatus",
    "lookup": "Lookup",
    "property types": "PropertyTypes",
    "payloads": "Payloads",
    "spanish name": "SpanishName",
    "french-canadian name": "FrenchCanadianName",
    "status change date": "StatusChangeDate",
    "revised date": "RevisionDate",
    "added in version": "AddedInVersion",
    "source resource": "SourceResource",
}

USAGE_RE = re.compile(
    r"Adoption\s+(\d+)\s*%\s+(\d+)\s+of\s+(\d+)\s+Organizations?",
    re.I,
)

DASH_TOKENS = {"--", "—", "-", "N/A", "n/a", ""}


def normalize(v: str) -> str:
    s = (v or "").strip()
    if s in DASH_TOKENS:
        return ""
    return re.sub(r"\s+", " ", s)


def load_fields() -> list[dict]:
    with FIELDS_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_existing() -> dict[tuple[str, str], dict]:
    if not OUT_CSV.exists():
        return {}
    with OUT_CSV.open(encoding="utf-8") as f:
        return {(r["Resource"], r["Field"]): r for r in csv.DictReader(f)}


def http_get(session: requests.Session, url: str, prev_fetched_at: str | None) -> requests.Response | None:
    headers: dict[str, str] = {}
    if prev_fetched_at:
        try:
            d = dt.datetime.fromisoformat(prev_fetched_at.replace("Z", "+00:00"))
            headers["If-Modified-Since"] = formatdate(d.timestamp(), usegmt=True)
        except Exception:
            pass
    delay = 1.0
    for _ in range(MAX_RETRIES):
        try:
            r = session.get(url, headers=headers, timeout=TIMEOUT)
            if r.status_code in (429, 503):
                time.sleep(delay)
                delay *= 2
                continue
            return r
        except requests.RequestException:
            time.sleep(delay)
            delay *= 2
    return None


def parse_kv(soup: BeautifulSoup) -> dict[str, str]:
    """Walk every <tr> across all <table>s, bucket by left-cell label."""
    out: dict[str, str] = {}
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            cells = tr.find_all(["th", "td"])
            if len(cells) < 2:
                continue
            label = cells[0].get_text(" ", strip=True).lower()
            value = cells[1].get_text(" ", strip=True)
            col = LABEL_MAP.get(label)
            if col and col not in out:
                out[col] = value
    return out


def parse_usage(soup: BeautifulSoup) -> tuple[str, str, str]:
    text = soup.get_text(" ", strip=True)
    m = USAGE_RE.search(text)
    if not m:
        return "", "", ""
    return m.group(1), m.group(2), m.group(3)


def fetch_one(session: requests.Session,
              row: dict,
              existing: dict[tuple[str, str], dict]) -> dict:
    resource = row.get("ResourceName", "")
    field = row.get("StandardName", "")
    url = URL_TMPL.format(resource=quote(resource, safe=""),
                          field=quote(field, safe=""))
    out = {c: "" for c in COLS}
    out["Resource"] = resource
    out["Field"] = field
    out["StandardName"] = field
    out["SourceUrl"] = url

    prev = existing.get((resource, field), {})
    r = http_get(session, url, prev.get("FetchedAt"))

    if r is None:
        return prev or out
    if r.status_code == 304 and prev:
        prev = dict(prev)
        prev["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        return prev
    if r.status_code != 200:
        if r.status_code != 404:
            print(f"  WARN {resource}.{field}: HTTP {r.status_code}", file=sys.stderr)
        return prev or out

    soup = BeautifulSoup(r.text, "html.parser")
    kv = parse_kv(soup)
    for col, val in kv.items():
        out[col] = normalize(val)
    if not out["StandardName"]:
        out["StandardName"] = field

    pct, n, total = parse_usage(soup)
    out["OrgPct"], out["OrgAdopted"], out["OrgTotal"] = pct, n, total
    out["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return out


def main() -> int:
    rows = load_fields()
    existing = load_existing()
    print(f"loaded {len(rows)} fields ({len(existing)} previously fetched)", flush=True)

    session = requests.Session()
    session.headers.update({"User-Agent": UA, "Accept": "text/html"})

    out_rows: list[dict] = []
    started = time.time()

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {}
        for row in rows:
            futures[ex.submit(fetch_one, session, row, existing)] = row
            time.sleep(GAP_MS / 1000.0 / WORKERS)
        done = 0
        for fut in as_completed(futures):
            row = futures[fut]
            try:
                out_rows.append(fut.result())
            except Exception as e:
                print(f"  err {row.get('StandardName')}: {e}", file=sys.stderr)
                out_rows.append({"Resource": row.get("ResourceName", ""),
                                 "Field": row.get("StandardName", ""),
                                 "StandardName": row.get("StandardName", ""),
                                 "SourceUrl": URL_TMPL.format(
                                     resource=quote(row.get("ResourceName", ""), safe=""),
                                     field=quote(row.get("StandardName", ""), safe="")),
                                 **{c: "" for c in COLS if c not in ("Resource", "Field", "StandardName", "SourceUrl")}})
            done += 1
            if done % 50 == 0 or done == len(rows):
                elapsed = time.time() - started
                rate = done / max(elapsed, 0.001)
                eta = (len(rows) - done) / max(rate, 0.001)
                print(f"  {done}/{len(rows)}  rate={rate:.1f}/s  eta={eta:.0f}s", flush=True)

    out_rows.sort(key=lambda r: (r["Resource"], r["Field"]))

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in out_rows:
            w.writerow({c: r.get(c, "") for c in COLS})
    print(f"wrote {len(out_rows)} rows -> {OUT_CSV}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
