#!/usr/bin/env python3
"""Scrape dd.reso.org per-LookupName pages -> raw/lookup_metadata.csv.

Source: https://dd.reso.org/DD2.0/lookups/<LookupName>/

For every distinct LookupName in raw/lookups.csv we GET the canonical
RESO DD 2.0 lookup page and capture the value count + Used By table:

    LookupName     e.g. "StandardStatus"
    ValueCount     parsed from "N values \u00b7 Used by N field" header
    UsedByCount    second number in the same header
    UsedByJson     JSON array of {Resource, Field, DisplayName, Usage}
    FetchedAt      ISO-8601 UTC instant we hit the page
    Source         constant "dd.reso.org/DD2.0"
    SourceUrl      full URL we GETd

The values themselves stay in raw/lookups.csv (parsed from the xlsx).
This file's job is just the lookup-LEVEL overview + cross-reference.

Politeness: 5 workers, 100ms launch gap, If-Modified-Since against prior
FetchedAt, exponential backoff on 429/503.

Run: python3 reso-dd-kb/scripts/fetch_lookup_metadata.py
"""
from __future__ import annotations

import csv
import datetime as dt
import json
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
LOOKUPS_CSV = RAW / "lookups.csv"
OUT_CSV = RAW / "lookup_metadata.csv"

SOURCE = "dd.reso.org/DD2.0"
URL_TMPL = "https://dd.reso.org/DD2.0/lookups/{name}/"
UA = "matrix-platform-kb/1.0 (+https://github.com/sharpsir-group/matrix-platform-kb)"
WORKERS = 5
GAP_MS = 100
TIMEOUT = 25
MAX_RETRIES = 4

COLS = ["LookupName", "ValueCount", "UsedByCount", "UsedByJson",
        "FetchedAt", "Source", "SourceUrl"]

HEADER_RE = re.compile(r"(\d+)\s*values?\s*\u00b7\s*Used by\s+(\d+)\s+field", re.I)


def load_lookup_names() -> list[str]:
    seen: list[str] = []
    with LOOKUPS_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            n = (r.get("LookupName") or "").strip()
            if n and n not in seen:
                seen.append(n)
    return sorted(seen)


def load_existing() -> dict[str, dict]:
    if not OUT_CSV.exists():
        return {}
    with OUT_CSV.open(encoding="utf-8") as f:
        return {r["LookupName"]: r for r in csv.DictReader(f)}


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


def parse_used_by(soup: BeautifulSoup) -> list[dict]:
    """Find the 'Used By' table; return [{Resource, Field, DisplayName, Usage}, ...]."""
    used: list[dict] = []
    h2 = next((h for h in soup.find_all("h2") if "used by" in h.get_text(strip=True).lower()), None)
    if not h2:
        return used
    table = h2.find_next("table")
    if not table:
        return used
    rows = table.find_all("tr")
    if len(rows) < 2:
        return used
    headers = [c.get_text(" ", strip=True).lower() for c in rows[0].find_all(["th", "td"])]
    for tr in rows[1:]:
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
        if not cells:
            continue
        rec = dict(zip(headers, cells))
        used.append({
            "Resource": rec.get("resource", ""),
            "Field": rec.get("field", ""),
            "DisplayName": rec.get("display name", ""),
            "Usage": rec.get("usage", ""),
        })
    return used


def fetch_one(session: requests.Session, name: str, prev: dict | None) -> dict:
    url = URL_TMPL.format(name=quote(name, safe=""))
    out = {c: "" for c in COLS}
    out["LookupName"] = name
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
        if r.status_code != 404:
            print(f"  WARN {name}: HTTP {r.status_code}", file=sys.stderr)
        return prev or out

    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    m = HEADER_RE.search(text)
    if m:
        out["ValueCount"] = m.group(1)
        out["UsedByCount"] = m.group(2)

    used = parse_used_by(soup)
    out["UsedByJson"] = json.dumps(used, ensure_ascii=False, separators=(",", ":"))
    out["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return out


def main() -> int:
    names = load_lookup_names()
    existing = load_existing()
    print(f"loaded {len(names)} LookupNames ({len(existing)} previously fetched)", flush=True)

    session = requests.Session()
    session.headers.update({"User-Agent": UA, "Accept": "text/html"})

    out_rows: list[dict] = []
    started = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {}
        for name in names:
            futures[ex.submit(fetch_one, session, name, existing.get(name))] = name
            time.sleep(GAP_MS / 1000.0 / WORKERS)
        done = 0
        for fut in as_completed(futures):
            name = futures[fut]
            try:
                out_rows.append(fut.result())
            except Exception as e:
                print(f"  err {name}: {e}", file=sys.stderr)
                out_rows.append({"LookupName": name, "Source": SOURCE,
                                 "SourceUrl": URL_TMPL.format(name=quote(name, safe="")),
                                 **{c: "" for c in COLS if c not in ("LookupName", "Source", "SourceUrl")}})
            done += 1
            if done % 25 == 0 or done == len(names):
                elapsed = time.time() - started
                rate = done / max(elapsed, 0.001)
                eta = (len(names) - done) / max(rate, 0.001)
                print(f"  {done}/{len(names)}  rate={rate:.1f}/s  eta={eta:.0f}s", flush=True)

    out_rows.sort(key=lambda r: r["LookupName"])
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in out_rows:
            w.writerow({c: r.get(c, "") for c in COLS})
    print(f"wrote {len(out_rows)} rows -> {OUT_CSV}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
