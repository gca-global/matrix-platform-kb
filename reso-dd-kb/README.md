# reso-dd-kb

Knowledge base for the **RESO Data Dictionary 2.0**, built from a verifiable
local mirror of [`dd.reso.org/DD2.0/`](https://dd.reso.org/DD2.0/).

This directory is being rebuilt from scratch in three phases.
**Phase 1 (mirror + structured extraction), Phase 2 (FK correlation
analysis) and Phase 2.5 (satellite / 2NF audit) are complete.**
Phase 3 (DBML generation) will be added by a subsequent commit.

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
  01_mirror.sh                       # Phase 1: wget mirror + sanity check
  _emit_manifest.py                  # Phase 1: builds manifest.json
  02_parse_mirror.py                 # Phase 1: HTML -> raw/*.csv

  03a_extract_definition_signals.py  # Phase 2: prose -> _signals_definition.csv
  03b_extract_type_signals.py        # Phase 2: type -> _signals_type.csv
  03c_extract_name_signals.py        # Phase 2: name -> _signals_name.csv
  03_merge_signals.py                # Phase 2: merge -> relationships.csv

  04a_prefix_satellites.py           # Phase 2.5: prefix candidates
  04b_child_match.py                 # Phase 2.5: child column match
  04c_definition_similarity.py       # Phase 2.5: Jaccard on prose
  04d_type_match.py                  # Phase 2.5: type + lookup match
  04_merge_satellites.py             # Phase 2.5: merge -> satellites.csv

raw/                     # structured extraction
  # Phase 1 outputs
  resources.csv          # 41 rows
  fields.csv             # 1,745 rows: every cell from the field page
  field_definitions.csv  # 1,745 rows: full Definition prose verbatim
  lookups.csv            # 222 rows
  lookup_values.csv      # 3,683 rows
  # Phase 2 outputs (derived from the above)
  _signals_definition.csv
  _signals_type.csv
  _signals_name.csv
  relationships.csv      # 226 rows: FK inventory with per-row evidence
  # Phase 2.5 outputs (derived from Phase 1 + Phase 2)
  _satellites_prefix.csv
  _satellites_child_match.csv
  _satellites_definition.csv
  _satellites_type.csv
  satellites.csv         # 208 rows: 2NF audit with drop/review/keep
```

## Refresh workflow

```bash
cd reso-dd-kb
bash scripts/01_mirror.sh         # ~90 min at 1 req/s; respects robots.txt
python3 scripts/02_parse_mirror.py
# Verification gates run inside 02_parse_mirror.py and exit non-zero
# if anything is off (row counts, blank Definitions, broken links).

# Phase 2: FK correlation (cheap; <1s).
python3 scripts/03a_extract_definition_signals.py
python3 scripts/03b_extract_type_signals.py
python3 scripts/03c_extract_name_signals.py
python3 scripts/03_merge_signals.py
# 03_merge_signals.py runs verification gates and prints a
# fk_kind x confidence histogram.

# Phase 2.5: satellite / 2NF audit (cheap; <1s).
python3 scripts/04a_prefix_satellites.py
python3 scripts/04b_child_match.py
python3 scripts/04c_definition_similarity.py
python3 scripts/04d_type_match.py
python3 scripts/04_merge_satellites.py
# 04_merge_satellites.py runs verification gates and prints a
# recommendation histogram.
```

## Phase plan (this README will be updated as each phase lands)

| Phase | Scope | Status |
|---|---|---|
| 1 | Mirror `dd.reso.org/DD2.0` + structured extraction | done |
| 2 | FK correlation analysis from Definition prose + type + name -> `raw/relationships.csv` | done |
| 2.5 | Satellite / duplicate detection (2NF audit) -> `raw/satellites.csv` | done |
| 3 | DBML build consuming `raw/relationships.csv` + reviewed `raw/satellites.csv` | not started |

See [`methodology.md`](methodology.md) for the per-phase methodology
and [`AGENTS.md`](AGENTS.md) for the rules an LLM agent must follow
when working in this directory.
