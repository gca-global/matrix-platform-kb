#!/usr/bin/env python3
"""
Emit reso-dd-kb/_meta/manifest.json from the wget mirror tree and crawl log.

For each fetched URL we record:
  - url            (absolute https://dd.reso.org/...)
  - path           (path relative to mirror/)
  - status         (HTTP status from crawl.log; defaults to 200 for files
                    present on disk that wget reported no error for)
  - bytes          (size of the on-disk file)
  - sha256         (sha256 of the on-disk file)

The manifest is the contract between Phase 1 (this script) and every
later phase. If a URL isn't here, it isn't in the canonical KB.

Deterministic: entries are sorted by URL.

Re-runnable: overwrites manifest.json each run.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
MIRROR_DIR = KB_ROOT / "mirror"
META_DIR = KB_ROOT / "_meta"
CRAWL_LOG = META_DIR / "crawl.log"
MANIFEST = META_DIR / "manifest.json"

UPSTREAM_HOST = "dd.reso.org"
UPSTREAM_BASE = f"https://{UPSTREAM_HOST}"


def parse_crawl_log(log_path: Path) -> dict[str, int]:
    """
    Map URL -> last seen HTTP status code from a wget --output-file log.

    wget log lines we care about look like:

        --2026-05-04 19:30:01--  https://dd.reso.org/DD2.0/Property/StandardStatus/
        HTTP request sent, awaiting response... 200 OK

    We pair each "--<timestamp>--  <url>" line with the next
    "HTTP request sent, awaiting response... <code>" line. If a URL
    appears multiple times (retries), the last status wins.
    """
    if not log_path.exists():
        return {}
    url_re = re.compile(r"^--\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}--\s+(\S+)")
    status_re = re.compile(r"HTTP request sent, awaiting response\.\.\. (\d{3})")

    statuses: dict[str, int] = {}
    pending_url: str | None = None
    with log_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            m = url_re.match(line)
            if m:
                pending_url = m.group(1)
                continue
            m = status_re.search(line)
            if m and pending_url:
                statuses[pending_url] = int(m.group(1))
                pending_url = None
    return statuses


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def url_for(rel_path: Path) -> str:
    """
    Map a mirror-relative path back to its source URL.

    With wget's `--no-host-directories` the mirror tree is rooted at
    <host root>, so `mirror/DD2.0/Property/index.html` came from
    `https://dd.reso.org/DD2.0/Property/index.html` (the trailing
    /index.html is wget's `--adjust-extension` rendering of the
    canonical `/DD2.0/Property/`).
    """
    return f"{UPSTREAM_BASE}/{rel_path.as_posix()}"


def main() -> int:
    if not MIRROR_DIR.exists():
        raise SystemExit(f"mirror dir does not exist: {MIRROR_DIR}")

    log_statuses = parse_crawl_log(CRAWL_LOG)

    entries: list[dict] = []
    for path in sorted(MIRROR_DIR.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(MIRROR_DIR)
        if rel.name.startswith(".listing") or rel.name == ".gitkeep":
            continue
        url = url_for(rel)
        # Match either the .html-suffixed URL (what wget records) or the
        # canonical trailing-slash URL (what users type).
        log_status = log_statuses.get(url)
        if log_status is None and url.endswith("/index.html"):
            log_status = log_statuses.get(url[: -len("index.html")])
        size = path.stat().st_size
        # Source-of-truth for 'do we have the bytes': the file on disk.
        # If the file is present and non-empty, the URL fetched
        # successfully at some point (either during the original wget
        # crawl or via a subsequent manual gap-fill curl) - so we
        # record status=200. A non-2xx in the crawl log for a file
        # that is now present means 'transient error during the crawl,
        # subsequently re-fetched'; we keep the historical status code
        # in `crawl_log_status` so reviewers can see it.
        status = 200 if size > 0 else (int(log_status) if log_status is not None else 0)
        entry = {
            "url": url,
            "path": rel.as_posix(),
            "status": status,
            "bytes": size,
            "sha256": sha256_of(path),
        }
        if log_status is not None and int(log_status) != status:
            entry["crawl_log_status"] = int(log_status)
        entries.append(entry)

    entries.sort(key=lambda e: e["url"])

    META_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "upstream": UPSTREAM_BASE,
        "entries": entries,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=False) + "\n")

    by_status: dict[int, int] = {}
    for e in entries:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(by_status.items()))
    print(f"[_emit_manifest] {len(entries)} files; status counts: {summary}")
    print(f"[_emit_manifest] wrote {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
