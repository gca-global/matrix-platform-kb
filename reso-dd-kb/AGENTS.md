# AGENTS.md - rules for LLM agents working in `reso-dd-kb/`

## Single source of truth

Every fact in this directory must trace back to a page on
`dd.reso.org/DD2.0/`. Do NOT introduce data from RESO Google Sheets,
the xlsx export, `ddwiki.reso.org` (deprecated), or any other source.
If `dd.reso.org` is silent on something, the canonical answer in this
KB is "silent" - document the gap, do not paper over it with a guess
or alias.

## Phase boundaries

This directory is built in phases. Do NOT mix phases in a single
commit:

| Phase | Reads | Writes |
|---|---|---|
| 1 | live `dd.reso.org/DD2.0/` | `mirror/`, `_meta/`, `raw/*.csv` (verbatim extraction) |
| 2 | `raw/fields.csv`, `raw/field_definitions.csv` | `raw/relationships.csv` |
| 2.5 | `raw/relationships.csv`, `raw/fields.csv`, `raw/field_definitions.csv` | `raw/satellites.csv` |
| 3 | `raw/relationships.csv`, reviewed `raw/satellites.csv`, `raw/*.csv` | `wiki/dbml/*.dbml` |
| 4 | `raw/*.csv`, `wiki/dbml/canonical.dbml` | `wiki/agent-docs/**` |

A Phase-N script must not read inputs from Phase >N (no time travel).
A Phase-N script must not modify outputs of Phase <N (no rewriting
upstream).

## File ownership

| Path | Owner | Edit by hand? |
|---|---|---|
| `mirror/**` | `scripts/01_mirror.sh` | No. Re-mirror to refresh. |
| `_meta/**` | `scripts/01_mirror.sh` + `scripts/_emit_manifest.py` | No. |
| `raw/resources.csv`, `raw/fields.csv`, `raw/field_definitions.csv`, `raw/lookups.csv`, `raw/lookup_values.csv` | `scripts/02_parse_mirror.py` | No. Re-run 02. |
| `raw/_signals_definition.csv` | `scripts/03a_extract_definition_signals.py` | No. Re-run 03a. |
| `raw/_signals_type.csv` | `scripts/03b_extract_type_signals.py` | No. Re-run 03b. |
| `raw/_signals_name.csv` | `scripts/03c_extract_name_signals.py` | No. Re-run 03c. |
| `raw/relationships.csv` | `scripts/03_merge_signals.py` | No. Re-run 03. |
| `raw/_satellites_prefix.csv` | `scripts/04a_prefix_satellites.py` | No. Re-run 04a. |
| `raw/_satellites_child_match.csv` | `scripts/04b_child_match.py` | No. Re-run 04b. |
| `raw/_satellites_definition.csv` | `scripts/04c_definition_similarity.py` | No. Re-run 04c. |
| `raw/_satellites_type.csv` | `scripts/04d_type_match.py` | No. Re-run 04d. |
| `raw/satellites.csv` | `scripts/04_merge_satellites.py` | No. Re-run 04. |
| `wiki/dbml/canonical.dbml` | `scripts/05_emit_dbml.py` | No. Re-run 05. |
| `wiki/dbml/lookups.dbml` | `scripts/05_emit_dbml.py` | No. Re-run 05. |
| `wiki/agent-docs/**` | `scripts/06_emit_agent_docs.py` | No. Re-run 06. |
| `USAGE.md` | humans + LLM agents (with review) | Yes (stable across refreshes). |
| `scripts/**` | humans + LLM agents (with review) | Yes. |
| `README.md`, `AGENTS.md`, `methodology.md` | humans + LLM agents (with review) | Yes. |

## Mirror politeness

The mirror script must:
- Respect `robots.txt` (`--execute robots=on` for wget).
- Identify itself with a real User-Agent including a contact email.
- Throttle to ~1 req/s with random jitter (`--wait=1 --random-wait`).
- Log every request to `_meta/crawl.log`.
- Snapshot `robots.txt` to `_meta/robots.txt` on every run.

## Determinism

`02_parse_mirror.py` (and every later phase script) must:
- Sort CSV rows by a stable key (typically `(Resource, StandardName)`).
- Use a stable column order.
- Quote consistently (use `csv.QUOTE_MINIMAL`).
- Not include any timestamps, hashes, or run-IDs in row content (those
  belong in `_meta/manifest.json`, not in `raw/*.csv`).

This is so each refresh produces a small, reviewable diff in git
rather than a churning byte salad.

## Verification gates

`02_parse_mirror.py` ends with hard assertions. The script must exit
non-zero on any breach. Do NOT commit a partial or inconsistent mirror.

Required gates (Phase 1):
- `resources.csv` has exactly the number of rows discovered on the
  DD 2.0 index page.
- `fields.csv` row count equals `sum(field_count)` from `resources.csv`.
- Every field row has a non-empty `Definition`.
- Every URL in `_meta/manifest.json` returned status 200.
- Every link found inside a resource page resolves to a fetched field
  page in the mirror.

If a gate breaks, fix the parser (or re-mirror the missing pages).
Do NOT relax the gate.

## Phase 2 outputs (now present)

The following files were added in Phase 2 (FK correlation analysis).
They are derived from the Phase 1 CSVs and rebuilt by re-running
`03*.py`; do not hand-edit.

- `raw/_signals_definition.csv` - one row per Definition-prose FK
  pattern hit (P1 / P2 / P3 / P3b / P4 / P5 / P6 / P7).
- `raw/_signals_type.csv` - one row per `Resource`- or
  `Collection`-typed field, with the `SourceResource` cell.
- `raw/_signals_name.csv` - one row per `*Key` / `*Id` field whose
  stem matches a known resource (with PK-collision and
  `OriginatingSystem<X>Key` host-pattern suppression applied).
- `raw/relationships.csv` - the merged, scored deliverable. One row
  per `(host_resource, host_field, target_resource)` triple, with
  evidence verbatim and a `confidence in {high, medium, low}`.

See `methodology.md` -> "Methodology - Phase 2" for the patterns,
scoring rules, and spot-check results.

Phase 3 (DBML build) is the only consumer permitted to read
`raw/relationships.csv` (FK source) and `raw/satellites.csv`
(column-drop source).

## Phase 2.5 outputs (now present)

The following files were added in Phase 2.5 (satellite / 2NF audit).
They are derived from Phase 1 + Phase 2 outputs and rebuilt by
re-running `04*.py`; do not hand-edit.

- `raw/_satellites_prefix.csv` - one row per (FK, candidate) pair
  whose StandardName starts with the FK column's stem.
- `raw/_satellites_child_match.csv` - candidate -> target column
  match (target_prefix / target_singular_prefix / bare_suffix /
  case-folded / underscore-stripped variants).
- `raw/_satellites_definition.csv` - Jaccard similarity over
  role-context-stripped Definition tokens.
- `raw/_satellites_type.csv` - SimpleDataType + Lookup match.
- `raw/satellites.csv` - the merged, scored deliverable. One row
  per (host_resource, host_field, candidate_satellite) triple, with
  a `recommendation in {drop_from_host, drop_from_child, keep_both,
  review}`.

See `methodology.md` -> "Methodology - Phase 2.5" for the four
signals, scoring, and spot-check results.

## Phase 3 outputs (now present)

The following files were added in Phase 3 (DBML build). They are
derived from Phase 1 + Phase 2 + Phase 2.5 outputs and rebuilt by
re-running `05_emit_dbml.py`; do not hand-edit.

- `wiki/dbml/canonical.dbml` - one `Table` per resource (snake_case),
  columns in original page order, PK marker on the chosen key, lookup
  columns typed as Enum references when the lookup is single-value
  with a closed value list. Includes inline `// REVIEW:` comments for
  rows the Phase-2.5 audit flagged for human inspection. Ends with a
  block of `Ref:` lines (one per high/medium-confidence FK from
  `relationships.csv`) and `// polymorphic FK` comments.
- `wiki/dbml/lookups.dbml` - one `Enum` block per single-value
  lookup with values from `lookup_values.csv`. Multi-value-only and
  open lookups are listed as comments at the bottom (their host
  columns stay `varchar` in `canonical.dbml`).

The generator's only schema decision NOT carried in a CSV is the
`PK_OVERRIDES` table (9 resources whose PK is not the obvious
`<Resource>Key` shape - each with an explanatory comment in the
script).

See `methodology.md` -> "Methodology - Phase 3" for the type-mapping
table, FK / column-drop / review policies, and the regression diff
against the previous iteration.

## Phase 4 outputs (now present)

The following files were added in Phase 4 (agent-consumption docs).
They are derived from Phase 1 + Phase 2 + Phase 2.5 + Phase 3 outputs
and rebuilt by re-running `06_emit_agent_docs.py`; do not hand-edit.

- `wiki/agent-docs/_index.md` - top-level index with the 41 resources
  table and pointers to `lookups.md` / `relationships.md`.
- `wiki/agent-docs/resources/<snake>.md` - one per resource: header,
  PK, fields table (with `pk`/`fk -> ...`/`[REVIEW]`/`[dropped]`/
  `[Resource]`/`[Collection]` flags), FKs OUT, FKs IN, inverse 1:N,
  polymorphic FKs, Phase-2.5 satellite audit table.
- `wiki/agent-docs/lookups.md` - 222 lookups in one file, alphabetical
  TOC + per-lookup section with kind (closed-SV / closed-MV / open),
  host columns, and value table.
- `wiki/agent-docs/relationships.md` - committed Refs (parsed from
  `wiki/dbml/canonical.dbml` - source of truth), Phase-2 detected
  signals (wider net), polymorphic FKs, inverse 1:N, low-confidence.

`USAGE.md` (at the root of `reso-dd-kb/`) is the human-curated narrative
entry point that orients a consuming agent before it dives into
`wiki/agent-docs/**`. It is stable across refreshes.

See `methodology.md` -> "Methodology - Phase 4" for the page templates,
verification gates, and refresh workflow.

## What this directory does NOT contain

- No alias map of any kind. The `RESOURCE_ALIASES` map from the
  previous iteration is intentionally not carried over - role
  aliases (`ListAgent -> Member`, `OriginatingSystem -> OUID`,
  etc.) are surfaced through the Definition-prose signal and the
  `SourceResource` cell instead.
- No xlsx file. If a cross-check is needed later, re-download from
  RESO and put it under a clearly-labelled `_xchk/` folder, never
  `raw/`.
- No project-specific opinions. `reso-dd-kb/` is RESO DD 2.0 only;
  consumer-project rules ("we always use ListAgentKey for the
  showing agent", etc.) live in the consuming project's docs.
