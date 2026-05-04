#!/usr/bin/env python3
"""Scrape dd.reso.org per-Resource pages -> raw/resource_metadata.csv.

Source: https://dd.reso.org/DD2.0/<Resource>/

For every distinct ResourceName in raw/fields.csv we GET the canonical
RESO DD 2.0 resource page and capture:

    Resource       e.g. "Property"
    EntityName     e.g. "property" (lowercase identifier rendered under H1)
    FieldCount     parsed from "N fields ..." header line
    Definition     prose paragraph rendered after "Definition" label
    LastRevised    date rendered after "... \u00b7 Last revised <date>"
    FetchedAt      ISO-8601 UTC instant we hit the page
    Source         constant "dd.reso.org/DD2.0"
    SourceUrl      full URL we GETd

Politeness: serial GETs (only ~41 pages); 250ms gap; If-Modified-Since
honoured against prior FetchedAt; exponential backoff on 429/503.

Run: python3 reso-dd-kb/scripts/fetch_resource_metadata.py
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
import time
from email.utils import formatdate
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
FIELDS_CSV = RAW / "fields.csv"
OUT_CSV = RAW / "resource_metadata.csv"

SOURCE = "dd.reso.org/DD2.0"
URL_TMPL = "https://dd.reso.org/DD2.0/{resource}/"
UA = "matrix-platform-kb/1.0 (+https://github.com/sharpsir-group/matrix-platform-kb)"
TIMEOUT = 25
GAP_MS = 250
MAX_RETRIES = 4

COLS = [
    "Resource", "EntityName", "FieldCount", "Definition",
    "LastRevised", "FetchedAt", "Source", "SourceUrl",
]

HEADER_RE = re.compile(r"(\d+)\s*fields?\s*\u00b7\s*Last revised\s*([\w/-]+)", re.I)
DEF_RE = re.compile(r"Definition\s+([^\n]+?)(?:\.{3,}|$)", re.S)


def load_resources() -> list[str]:
    seen: list[str] = []
    with FIELDS_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            name = (r.get("ResourceName") or "").strip()
            if name and name not in seen:
                seen.append(name)
    return sorted(seen)


def load_existing() -> dict[str, dict]:
    if not OUT_CSV.exists():
        return {}
    with OUT_CSV.open(encoding="utf-8") as f:
        return {r["Resource"]: r for r in csv.DictReader(f)}


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


def parse_entity_name(soup: BeautifulSoup) -> str:
    """The lowercase entity-name string rendered immediately after the H1."""
    h1 = soup.find("h1")
    if not h1:
        return ""
    sib = h1.find_next_sibling()
    if sib and sib.name in ("p", "div", "span"):
        t = sib.get_text(" ", strip=True)
        if t and t.lower() == t and " " not in t:
            return t
    parent_text = h1.parent.get_text(" ", strip=True) if h1.parent else ""
    h1_text = h1.get_text(" ", strip=True)
    after = parent_text.split(h1_text, 1)[-1].strip()
    parts = after.split()
    return parts[0] if parts and parts[0].islower() else ""


def parse_definition(soup: BeautifulSoup) -> str:
    """Capture the prose after the literal label 'Definition'."""
    text = soup.get_text(" ", strip=True)
    m = DEF_RE.search(text)
    if not m:
        return ""
    candidate = m.group(1).strip()
    candidate = re.split(r"\s+(?:Sort by|Show Groups|##)\b", candidate)[0].strip()
    return candidate


def fetch_one(session: requests.Session, resource: str, prev: dict | None) -> dict:
    url = URL_TMPL.format(resource=resource)
    out = {c: "" for c in COLS}
    out["Resource"] = resource
    out["Source"] = SOURCE
    out["SourceUrl"] = url

    r = http_get(session, url, (prev or {}).get("FetchedAt"))
    if r is None:
        return prev or out
    if r.status_code == 304 and prev:
        prev = dict(prev)
        prev["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        return prev
    if r.status_code != 200:
        print(f"  WARN {resource}: HTTP {r.status_code}", file=sys.stderr)
        return prev or out

    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    out["EntityName"] = parse_entity_name(soup)

    m = HEADER_RE.search(text)
    if m:
        out["FieldCount"] = m.group(1)
        out["LastRevised"] = m.group(2)

    out["Definition"] = parse_definition(soup)
    out["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return out


def main() -> int:
    resources = load_resources()
    existing = load_existing()
    print(f"loaded {len(resources)} resources ({len(existing)} previously fetched)", flush=True)

    session = requests.Session()
    session.headers.update({"User-Agent": UA, "Accept": "text/html"})

    rows: list[dict] = []
    started = time.time()
    for i, res in enumerate(resources, 1):
        row = fetch_one(session, res, existing.get(res))
        rows.append(row)
        if i % 5 == 0 or i == len(resources):
            print(f"  {i}/{len(resources)}  ({time.time()-started:.1f}s)", flush=True)
        time.sleep(GAP_MS / 1000.0)

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})
    print(f"wrote {len(rows)} rows -> {OUT_CSV}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
