#!/usr/bin/env python3
"""
Emit a single deterministic SQL seed file for the CDL tooltip + label
corpus, sourced from the RESO DD 2.0 mirror.

Reads:
  raw/resources.csv         (41 rows: ResourceName, Description, SourceURL, ...)
  raw/fields.csv            (1745 rows: ResourceName, StandardName, DisplayName,
                             Lookup, LookupStatus, SourceURL, ...)
  raw/field_definitions.csv (1745 rows: ResourceName, StandardName, Definition,
                             SourceURL — the verbatim RESO Definition prose
                             that lands in reso_field_descriptions.description)
  raw/lookup_values.csv     (3683 rows: LookupName, StandardValue, DisplayValue,
                             Definition, SourceURL, ...)
  _meta/manifest.json       (mirror provenance: generated_at, upstream)

Writes:
  wiki/cdl/reso_full_corpus.sql

Phase: Emit (deterministic, mechanical).
Owner: scripts/07_emit_cdl_seed.py — do NOT hand-edit the SQL output.

The generated SQL:

  1. ALTERs reso_field_descriptions to add the display_name column.
  2. CREATEs reso_lookup_value_descriptions (RLS, public read, see below).
  3. DELETEs legacy hand-written rows so the corpus is 100% RESO-sourced.
  4. INSERTs Resource.<ResourceName>, <Resource>.<StandardName>, and
     lookup-value rows with ON CONFLICT DO UPDATE.

Description-source contract (enforced by smoke-test inside this script):

  - reso_field_descriptions.description == field_definitions.csv:Definition
    (byte-for-byte, no trim, no markdown injection)
  - reso_field_descriptions.wiki_url    == fields.csv:SourceURL
  - reso_field_descriptions.lookups_url == 'https://dd.reso.org/DD2.0/lookups/<Lookup>/'
    when fields.csv:Lookup is non-empty, else NULL
  - reso_lookup_value_descriptions.definition == lookup_values.csv:Definition
  - reso_lookup_value_descriptions.wiki_url   == lookup_values.csv:SourceURL

Determinism rules:
  - stable sort by primary key
  - LF line endings
  - single-quote SQL escaping via ' -> ''
  - no now() in VALUES — let column defaults fire
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parent.parent
RAW = KB_ROOT / "raw"
META = KB_ROOT / "_meta"
OUT_DIR = KB_ROOT / "wiki" / "cdl"
OUT_FILE = OUT_DIR / "reso_full_corpus.sql"

DD_VERSION = "2.0"
RESOURCE_PLACEHOLDER = (
    "(RESO does not publish a top-level description for this resource; "
    "see field-level documentation.)"
)
LOOKUPS_URL_FMT = "https://dd.reso.org/DD2.0/lookups/{lookup}/"
RESOURCE_KEY_PREFIX = "Resource."  # e.g. Resource.Property


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sql_str(value: str | None) -> str:
    """Render a SQL string literal, NULL-aware, single-quote-escaped."""
    if value is None or value == "":
        return "NULL"
    escaped = value.replace("'", "''")
    return f"'{escaped}'"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def manifest_meta() -> tuple[str, str]:
    """Return (mirror_fetched_at, upstream)."""
    mf = META / "manifest.json"
    if not mf.exists():
        return ("(manifest.json missing)", "(unknown)")
    data = json.loads(mf.read_text(encoding="utf-8"))
    return (data.get("generated_at", "(missing)"), data.get("upstream", "(missing)"))


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def build_field_rows(
    fields: list[dict],
    field_defs: list[dict],
    resources: list[dict],
) -> list[tuple[str, str, str, str, str | None]]:
    """
    Return ordered list of tuples for reso_field_descriptions:
      (field, display_name, description, wiki_url, lookups_url|None)
    Includes 41 Resource.<X> rows + 1745 <Resource>.<StandardName> rows.
    """
    defs_by_key: dict[tuple[str, str], dict] = {
        (r["ResourceName"], r["StandardName"]): r for r in field_defs
    }
    out: list[tuple[str, str, str, str, str | None]] = []

    # Resource-level entries
    for r in resources:
        key = f"{RESOURCE_KEY_PREFIX}{r['ResourceName']}"
        desc = (r.get("Description") or "").strip() or RESOURCE_PLACEHOLDER
        out.append(
            (
                key,
                r["ResourceName"],
                desc,
                r["SourceURL"],
                None,
            )
        )

    # Field-level entries
    for f in fields:
        key = f"{f['ResourceName']}.{f['StandardName']}"
        d = defs_by_key.get((f["ResourceName"], f["StandardName"]))
        if d is None:
            raise SystemExit(
                f"[07] hard-fail: field_definitions.csv missing {key}; "
                "re-run 02_parse_mirror.py"
            )
        definition = d["Definition"]
        if not definition.strip():
            raise SystemExit(
                f"[07] hard-fail: empty Definition for {key} in field_definitions.csv"
            )
        lookup = (f.get("Lookup") or "").strip()
        lookups_url: str | None = None
        if lookup:
            lookups_url = LOOKUPS_URL_FMT.format(lookup=lookup)
        out.append(
            (
                key,
                f["DisplayName"],
                definition,
                f["SourceURL"],
                lookups_url,
            )
        )

    out.sort(key=lambda t: t[0])
    return out


def build_lookup_rows(
    lookup_values: list[dict],
) -> list[tuple[str, str, str, str, str]]:
    """
    Return ordered list of tuples for reso_lookup_value_descriptions:
      (lookup_name, standard_value, display_value, definition, wiki_url)
    """
    out: list[tuple[str, str, str, str, str]] = []
    for lv in lookup_values:
        out.append(
            (
                lv["LookupName"],
                lv["StandardValue"],
                lv["DisplayValue"],
                lv["Definition"],
                lv["SourceURL"],
            )
        )
    out.sort(key=lambda t: (t[0], t[1]))
    return out


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------


def render_header(sha256s: dict[str, str], fetched_at: str, upstream: str) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "-- ========================================================================",
        "-- CDL RESO Data Dictionary corpus (full canonical seed)",
        "-- ========================================================================",
        "-- Auto-generated: do NOT hand-edit.",
        "--",
        f"--   generated_by:        scripts/07_emit_cdl_seed.py",
        f"--   generated_at:        {generated}",
        f"--   upstream:            {upstream}",
        f"--   mirror_fetched_at:   {fetched_at}",
        f"--   dd_version:          {DD_VERSION}",
        "--",
        f"--   sha256(resources.csv):         {sha256s['resources']}",
        f"--   sha256(fields.csv):            {sha256s['fields']}",
        f"--   sha256(field_definitions.csv): {sha256s['field_definitions']}",
        f"--   sha256(lookup_values.csv):     {sha256s['lookup_values']}",
        "--",
        "-- description-source contract (enforced by 07_emit_cdl_seed.py):",
        "--   reso_field_descriptions.description == field_definitions.csv:Definition",
        "--   reso_field_descriptions.wiki_url    == fields.csv:SourceURL",
        "--   reso_field_descriptions.lookups_url == dd.reso.org/DD2.0/lookups/<Lookup>/",
        "--   reso_lookup_value_descriptions.definition == lookup_values.csv:Definition",
        "--   reso_lookup_value_descriptions.wiki_url   == lookup_values.csv:SourceURL",
        "-- ========================================================================",
        "",
        "BEGIN;",
        "",
    ]
    return "\n".join(lines)


def render_ddl() -> str:
    return """\
-- =========================================================================
-- DDL: idempotent column add + new table for lookup-value tooltips
-- =========================================================================

ALTER TABLE public.reso_field_descriptions
  ADD COLUMN IF NOT EXISTS display_name text;

CREATE TABLE IF NOT EXISTS public.reso_lookup_value_descriptions (
  lookup_name     text        NOT NULL,
  standard_value  text        NOT NULL,
  locale          text        NOT NULL DEFAULT 'en',
  display_value   text        NOT NULL,
  definition      text,
  wiki_url        text,
  dd_version      text        NOT NULL DEFAULT '2.0',
  source          text        NOT NULL DEFAULT 'reso_official_csv',
  updated_at      timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (lookup_name, standard_value, locale)
);

COMMENT ON TABLE public.reso_lookup_value_descriptions IS
  'RESO Data Dictionary lookup values, served alongside reso_field_descriptions for dropdowns and option-level tooltips.';

CREATE INDEX IF NOT EXISTS idx_reso_lookup_value_descriptions_lookup
  ON public.reso_lookup_value_descriptions (lookup_name);

GRANT SELECT ON public.reso_lookup_value_descriptions TO anon, authenticated;
ALTER TABLE public.reso_lookup_value_descriptions ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS reso_lookup_value_descriptions_read
  ON public.reso_lookup_value_descriptions;
CREATE POLICY reso_lookup_value_descriptions_read
  ON public.reso_lookup_value_descriptions
  FOR SELECT
  USING (true);
"""


def render_provenance_reset() -> str:
    return """\

-- =========================================================================
-- One-time provenance reset
-- =========================================================================
-- Drop legacy hand-written rows so the corpus is 100% RESO-sourced.
-- Curated overrides return later via a separate reso_field_overrides table.

DELETE FROM public.reso_field_descriptions
 WHERE source IN ('team_override', 'atlas_custom')
    OR field NOT LIKE '%.%';
"""


def render_field_dml(rows: list[tuple[str, str, str, str, str | None]]) -> str:
    out = ["", "-- =========================================================================",
           f"-- DML: reso_field_descriptions ({len(rows)} rows: 41 resources + 1745 fields)",
           "-- =========================================================================",
           "",
           "INSERT INTO public.reso_field_descriptions",
           "  (field, locale, display_name, description, wiki_url, lookups_url, dd_version, source)",
           "VALUES"]
    body: list[str] = []
    for key, display_name, description, wiki_url, lookups_url in rows:
        body.append(
            "  ("
            + ", ".join([
                sql_str(key),
                "'en'",
                sql_str(display_name),
                sql_str(description),
                sql_str(wiki_url),
                sql_str(lookups_url) if lookups_url is not None else "NULL",
                f"'{DD_VERSION}'",
                "'reso_official_csv'",
            ])
            + ")"
        )
    out.append(",\n".join(body))
    out.append("ON CONFLICT (field, locale) DO UPDATE SET")
    out.append("  display_name = excluded.display_name,")
    out.append("  description  = excluded.description,")
    out.append("  wiki_url     = excluded.wiki_url,")
    out.append("  lookups_url  = excluded.lookups_url,")
    out.append("  dd_version   = excluded.dd_version,")
    out.append("  source       = excluded.source,")
    out.append("  updated_at   = now();")
    return "\n".join(out) + "\n"


def render_lookup_dml(rows: list[tuple[str, str, str, str, str]]) -> str:
    out = ["", "-- =========================================================================",
           f"-- DML: reso_lookup_value_descriptions ({len(rows)} rows)",
           "-- =========================================================================",
           "",
           "INSERT INTO public.reso_lookup_value_descriptions",
           "  (lookup_name, standard_value, locale, display_value, definition, wiki_url, dd_version, source)",
           "VALUES"]
    body: list[str] = []
    for lookup_name, standard_value, display_value, definition, wiki_url in rows:
        body.append(
            "  ("
            + ", ".join([
                sql_str(lookup_name),
                sql_str(standard_value),
                "'en'",
                sql_str(display_value),
                sql_str(definition),
                sql_str(wiki_url),
                f"'{DD_VERSION}'",
                "'reso_official_csv'",
            ])
            + ")"
        )
    out.append(",\n".join(body))
    out.append("ON CONFLICT (lookup_name, standard_value, locale) DO UPDATE SET")
    out.append("  display_value = excluded.display_value,")
    out.append("  definition    = excluded.definition,")
    out.append("  wiki_url      = excluded.wiki_url,")
    out.append("  dd_version    = excluded.dd_version,")
    out.append("  source        = excluded.source,")
    out.append("  updated_at    = now();")
    return "\n".join(out) + "\n"


def render_footer() -> str:
    return "\nCOMMIT;\n"


# ---------------------------------------------------------------------------
# Smoke tests (description-source contract)
# ---------------------------------------------------------------------------


def smoke_check_field_contract(
    field_rows: list[tuple[str, str, str, str, str | None]],
    fields: list[dict],
    field_defs: list[dict],
    resources: list[dict],
) -> None:
    """Spot-check a sample to confirm byte-for-byte equality."""
    fields_by_key = {(f["ResourceName"], f["StandardName"]): f for f in fields}
    defs_by_key = {(d["ResourceName"], d["StandardName"]): d for d in field_defs}
    res_names = {r["ResourceName"] for r in resources}

    sample_keys = [
        ("Property", "ListPrice"),
        ("Property", "StandardStatus"),
        ("Member", "MemberKey"),
        ("Office", "OfficeName"),
    ]
    rows_by_key = {row[0]: row for row in field_rows}
    for resource_name, standard_name in sample_keys:
        if resource_name not in res_names:
            continue
        if (resource_name, standard_name) not in fields_by_key:
            continue
        key = f"{resource_name}.{standard_name}"
        row = rows_by_key.get(key)
        assert row is not None, f"missing row for {key}"
        _, display_name, description, wiki_url, lookups_url = row

        f = fields_by_key[(resource_name, standard_name)]
        d = defs_by_key[(resource_name, standard_name)]
        assert display_name == f["DisplayName"], f"DisplayName drift for {key}"
        assert description == d["Definition"], f"Definition byte-drift for {key}"
        assert wiki_url == f["SourceURL"], f"SourceURL drift for {key}"
        lookup = (f.get("Lookup") or "").strip()
        if lookup:
            assert lookups_url == LOOKUPS_URL_FMT.format(lookup=lookup), (
                f"lookups_url drift for {key}"
            )
        else:
            assert lookups_url is None


def smoke_check_lookup_contract(
    lookup_rows: list[tuple[str, str, str, str, str]],
    lookup_values: list[dict],
) -> None:
    by_pk = {(r[0], r[1]): r for r in lookup_rows}
    sample = [
        ("StandardStatus", "Active"),
        ("StandardStatus", "Closed"),
        ("PropertyType", "Residential"),
    ]
    src_by_pk = {(lv["LookupName"], lv["StandardValue"]): lv for lv in lookup_values}
    for pk in sample:
        if pk not in src_by_pk:
            continue
        row = by_pk.get(pk)
        assert row is not None, f"missing lookup row {pk}"
        _, _, display_value, definition, wiki_url = row
        src = src_by_pk[pk]
        assert display_value == src["DisplayValue"], f"DisplayValue drift {pk}"
        assert definition == src["Definition"], f"Definition byte-drift {pk}"
        assert wiki_url == src["SourceURL"], f"SourceURL drift {pk}"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> int:
    if not RAW.is_dir():
        print(f"[07] ERROR: raw dir not found: {RAW}", file=sys.stderr)
        return 2

    resources = load_csv(RAW / "resources.csv")
    fields = load_csv(RAW / "fields.csv")
    field_defs = load_csv(RAW / "field_definitions.csv")
    lookup_values = load_csv(RAW / "lookup_values.csv")

    field_rows = build_field_rows(fields, field_defs, resources)
    lookup_rows = build_lookup_rows(lookup_values)

    smoke_check_field_contract(field_rows, fields, field_defs, resources)
    smoke_check_lookup_contract(lookup_rows, lookup_values)

    sha256s = {
        "resources": sha256(RAW / "resources.csv"),
        "fields": sha256(RAW / "fields.csv"),
        "field_definitions": sha256(RAW / "field_definitions.csv"),
        "lookup_values": sha256(RAW / "lookup_values.csv"),
    }
    fetched_at, upstream = manifest_meta()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = []
    out.append(render_header(sha256s, fetched_at, upstream))
    out.append(render_ddl())
    out.append(render_provenance_reset())
    out.append(render_field_dml(field_rows))
    out.append(render_lookup_dml(lookup_rows))
    out.append(render_footer())
    OUT_FILE.write_text("".join(out), encoding="utf-8", newline="\n")

    print(
        f"[07] emit_cdl_seed: {len(field_rows)} field rows "
        f"({len(resources)} resources + {len(fields)} fields) "
        f"+ {len(lookup_rows)} lookup-value rows -> {OUT_FILE.relative_to(KB_ROOT)} "
        f"({OUT_FILE.stat().st_size:,} bytes)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
