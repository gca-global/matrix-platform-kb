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

A Phase-N script must not read inputs from Phase >N (no time travel).
A Phase-N script must not modify outputs of Phase <N (no rewriting
upstream).

## File ownership

| Path | Owner | Edit by hand? |
|---|---|---|
| `mirror/**` | `scripts/01_mirror.sh` | No. Re-mirror to refresh. |
| `_meta/**` | `scripts/01_mirror.sh` + `scripts/_emit_manifest.py` | No. |
| `raw/**` | `scripts/02_parse_mirror.py` (Phase 1) and the Phase 2 / 2.5 scripts | No. Re-run the owning script. |
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

## What this directory does NOT contain (yet)

- No `wiki/dbml/*.dbml` (Phase 3 output).
- No `raw/relationships.csv` (Phase 2 output).
- No `raw/satellites.csv` (Phase 2.5 output).
- No alias map of any kind. The `RESOURCE_ALIASES` map from the
  previous iteration is intentionally not carried over.
- No xlsx file. If a cross-check is needed later, re-download from
  RESO and put it under a clearly-labelled `_xchk/` folder, never
  `raw/`.
