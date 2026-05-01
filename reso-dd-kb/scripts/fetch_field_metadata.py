#!/usr/bin/env python3
"""Scrape DDwiki for per-field structured metadata + usage stats.

For every row in raw/fields.csv we GET the field's DDwiki page
(WikiPageUrl column already in fields.csv) and parse the structured
key/value block + the Usage footer ("XX% of Systems (n/N)" /
"XX% of Organizations (n/N)") into one row of
raw/field_metadata.csv.

Output columns (locked by reso-dd-kb plan):
    Resource, Field, StandardName, DisplayName, Group, DataType,
    MaxLength, MaxPrecision, Synonyms, FieldStatus, BEDES, RecordID,
    LookupStatus, Lookup, PropertyTypes, Payloads, SpanishName,
    FrenchCanadianName, StatusChangeDate, RevisionDate,
    AddedInVersion, SysPct, SysAdopted, SysTotal, OrgPct,
    OrgAdopted, OrgTotal, WikiURL, LastModified, FetchedAt

Politeness:
  * 5 concurrent connections max (ThreadPoolExecutor)
  * 100 ms gap between launches per worker
  * If-Modified-Since header from previous FetchedAt when the row exists
  * Exponential backoff on 429 / 503

Usage:
    python3 reso-dd-kb/scripts/fetch_field_metadata.py
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import formatdate, parsedate_to_datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
FIELDS_CSV = RAW / "fields.csv"
OUT_CSV = RAW / "field_metadata.csv"

UA = "matrix-platform-kb/1.0 (+https://github.com/sharpsir-group/matrix-platform-kb)"
WORKERS = 5
GAP_MS = 100
TIMEOUT = 25
MAX_RETRIES = 4

COLS = [
    "Resource", "Field", "StandardName", "DisplayName", "Group", "DataType",
    "MaxLength", "MaxPrecision", "Synonyms", "FieldStatus", "BEDES", "RecordID",
    "LookupStatus", "Lookup", "PropertyTypes", "Payloads", "SpanishName",
    "FrenchCanadianName", "StatusChangeDate", "RevisionDate", "AddedInVersion",
    "SysPct", "SysAdopted", "SysTotal", "OrgPct", "OrgAdopted", "OrgTotal",
    "WikiURL", "LastModified", "FetchedAt",
]

# canonical -> (display labels we accept on DDwiki)
LABELS = {
    "DisplayName": ["Display Name"],
    "Group": ["Group"],
    "DataType": ["Data Type"],
    "MaxLength": ["Suggested Maximum Length"],
    "MaxPrecision": ["Suggested Maximum Precision"],
    "Synonyms": ["Synonyms(s)", "Synonyms"],
    "FieldStatus": ["Field (Element) Status"],
    "BEDES": ["BEDES"],
    "RecordID": ["Record ID"],
    "LookupStatus": ["Lookup Status"],
    "Lookup": ["Lookup"],
    "PropertyTypes": ["Property Types"],
    "Payloads": ["Payloads"],
    "SpanishName": ["Spanish Name"],
    "FrenchCanadianName": ["French-Canadian Name"],
    "StatusChangeDate": ["Status Change Date"],
    "RevisionDate": ["Revision Date"],
    "AddedInVersion": ["Added in Version"],
}

H2_LABELS = {
    "StandardName": ["Standard Name"],
}

USAGE_RE = re.compile(
    r"(\d+)\s*%\s*of\s*(Systems|Organizations)\s*\((\d+)\s*/\s*(\d+)\)",
    re.IGNORECASE,
)


def load_fields() -> list[dict]:
    with FIELDS_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_existing() -> dict[tuple[str, str], dict]:
    if not OUT_CSV.exists():
        return {}
    with OUT_CSV.open(encoding="utf-8") as f:
        return {(r["Resource"], r["Field"]): r for r in csv.DictReader(f)}


def parse_kv_strong(soup: BeautifulSoup) -> dict[str, str]:
    """Pull `<strong>Key: </strong>Value` and the H2 Standard Name block."""
    out: dict[str, str] = {}
    seen: dict[str, str] = {}

    for strong in soup.select("strong"):
        label = (strong.get_text() or "").strip().rstrip(":").strip()
        if not label:
            continue
        parent = strong.parent
        if parent is None:
            continue
        text = parent.get_text(" ", strip=True)
        if ":" in text:
            value = text.split(":", 1)[1].strip()
        else:
            value = text.replace(label, "", 1).strip()
        seen.setdefault(label, value)

    for canon, aliases in LABELS.items():
        for alias in aliases:
            if alias in seen:
                out[canon] = seen[alias]
                break

    for canon, aliases in H2_LABELS.items():
        for alias in aliases:
            for h2 in soup.select("h2"):
                t = h2.get_text(" ", strip=True)
                if t.startswith(alias):
                    out[canon] = t.split(":", 1)[-1].strip() if ":" in t else t.replace(alias, "").strip()
                    break
            if canon in out:
                break

    return out


def parse_usage(soup: BeautifulSoup) -> dict[str, str]:
    out = {"SysPct": "", "SysAdopted": "", "SysTotal": "",
           "OrgPct": "", "OrgAdopted": "", "OrgTotal": ""}
    text = soup.get_text(" ", strip=True)
    for m in USAGE_RE.finditer(text):
        pct, kind, n, total = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if kind.startswith("system"):
            out["SysPct"], out["SysAdopted"], out["SysTotal"] = pct, n, total
        elif kind.startswith("organi"):
            out["OrgPct"], out["OrgAdopted"], out["OrgTotal"] = pct, n, total
    return out


def normalize_dashes(v: str) -> str:
    """DDwiki uses '--' for empty / not-applicable; normalize to ''."""
    if v is None:
        return ""
    s = v.strip()
    if s in ("--", "—", "-", "N/A", "n/a"):
        return ""
    return s


def http_get(session: requests.Session, url: str, prev_fetched_at: str | None) -> requests.Response | None:
    headers: dict[str, str] = {}
    if prev_fetched_at:
        try:
            d = dt.datetime.fromisoformat(prev_fetched_at.replace("Z", "+00:00"))
            headers["If-Modified-Since"] = formatdate(d.timestamp(), usegmt=True)
        except Exception:
            pass

    delay = 1.0
    for attempt in range(MAX_RETRIES):
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


def parse_last_modified(html: str, headers: dict) -> str:
    h = headers.get("Last-Modified") or ""
    if h:
        try:
            return parsedate_to_datetime(h).date().isoformat()
        except Exception:
            pass
    m = re.search(r"last modified on\s*<a[^>]*>([^<]+)</a>", html, re.I)
    if m:
        try:
            return dt.datetime.strptime(m.group(1).strip(), "%b %d, %Y").date().isoformat()
        except Exception:
            return m.group(1).strip()
    return ""


def fetch_one(session: requests.Session,
              row: dict,
              existing: dict[tuple[str, str], dict]) -> dict:
    resource = row.get("ResourceName", "")
    field = row.get("StandardName", "")
    url = (row.get("WikiPageUrl") or "").strip()
    out = {c: "" for c in COLS}
    out["Resource"] = resource
    out["Field"] = field
    out["WikiURL"] = url

    if not url:
        return out

    prev = existing.get((resource, field), {})
    r = http_get(session, url, prev.get("FetchedAt"))

    if r is None:
        if prev:
            return prev
        return out

    if r.status_code == 304 and prev:
        prev["FetchedAt"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        return prev

    if r.status_code != 200:
        if prev:
            return prev
        return out

    soup = BeautifulSoup(r.text, "html.parser")

    kv = parse_kv_strong(soup)
    for k, v in kv.items():
        out[k] = normalize_dashes(v)
    if not out["StandardName"]:
        out["StandardName"] = field

    out.update(parse_usage(soup))
    out["LastModified"] = parse_last_modified(r.text, r.headers)
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
        for i, row in enumerate(rows):
            futures[ex.submit(fetch_one, session, row, existing)] = (i, row)
            time.sleep(GAP_MS / 1000.0 / WORKERS)
        done = 0
        for fut in as_completed(futures):
            i, row = futures[fut]
            try:
                out_rows.append(fut.result())
            except Exception as e:
                print(f"  err {row.get('StandardName')}: {e}", flush=True)
                out_rows.append({"Resource": row.get("ResourceName", ""),
                                 "Field": row.get("StandardName", ""),
                                 "WikiURL": row.get("WikiPageUrl", ""),
                                 **{c: "" for c in COLS if c not in ("Resource", "Field", "WikiURL")}})
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
