# reso-dd-kb

Knowledge base for the **RESO Data Dictionary 2.0**, built from a verifiable
local mirror of [`dd.reso.org/DD2.0/`](https://dd.reso.org/DD2.0/).

This directory is being rebuilt from scratch in three phases. **Phase 1
(this commit) covers the mirror and the structured extraction only.**
Correlation analysis (Phase 2) and DBML generation (Phase 3) will be
added by subsequent commits.

## Why a rebuild

The previous iteration blended xlsx-derived data with wiki scrapes and
layered an alias map over a thin upstream source. The new pipeline has a
single source of truth (`dd.reso.org/DD2.0`) and every downstream
artifact traces back to a row in the mirror.

## Layout

```
mirror/                  # verbatim HTML snapshot of dd.reso.org/DD2.0/
  DD2.0/
    index.html
    <Resource>/index.html              x 41
    <Resource>/<Field>/index.html      x 1,745
    <Lookup>/index.html                x ~222
    <Lookup>/<Value>/index.html        x ~3,500
    xref/...                           status, version-added, payloads
    about/terms/index.html

_meta/
  manifest.json          # URL list, fetch timestamps, status codes, sha256s
  robots.txt             # snapshot for record
  crawl.log              # wget log

scripts/
  01_mirror.sh           # wget mirror + sanity check
  _emit_manifest.py      # builds manifest.json
  02_parse_mirror.py     # HTML -> structured CSVs in raw/

raw/                     # structured extraction; THE inputs for Phase 2
  resources.csv          # 41 rows
  fields.csv             # 1,745 rows: every cell from the field page
  field_definitions.csv  # 1,745 rows: full Definition prose verbatim
  lookups.csv            # ~222 rows
  lookup_values.csv      # ~3,500 rows
  xref/                  # xref pages flattened
```

## Refresh workflow

```bash
cd reso-dd-kb
bash scripts/01_mirror.sh         # ~90 min at 1 req/s; respects robots.txt
python3 scripts/02_parse_mirror.py
# Verification gates run inside 02_parse_mirror.py and exit non-zero
# if anything is off (row counts, blank Definitions, broken links).
```

## Phase plan (this README will be updated as each phase lands)

| Phase | Scope | Status |
|---|---|---|
| 1 | Mirror `dd.reso.org/DD2.0` + structured extraction (this commit) | in progress |
| 2 | FK correlation analysis from Definition prose + type + name -> `raw/relationships.csv` | not started |
| 2.5 | Satellite / duplicate detection (2NF audit) -> `raw/satellites.csv` | not started |
| 3 | DBML build consuming `raw/relationships.csv` + reviewed `raw/satellites.csv` | not started |

See [`methodology.md`](methodology.md) for Phase 1 details and
[`AGENTS.md`](AGENTS.md) for the rules an LLM agent must follow when
working in this directory.
