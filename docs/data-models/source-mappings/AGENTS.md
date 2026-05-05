# AGENTS.md - rules for LLM agents working in `source-mappings/`

## What this directory does

Maps real-world Sharp Matrix source systems (Dash DOCX forms, Qobrix
OpenAPI, SIR business-practice XLSX checklists) to the canonical RESO
DD 2.0 model in [`../reso-dd-kb/`](../reso-dd-kb/AGENTS.md). CDL/Atlas
storage stays canonical RESO; this directory is the bridge for
ingestion (inbound) and syndication (outbound).

## Boundary with reso-dd-kb

`reso-dd-kb/` is RESO DD 2.0 only. Project-specific opinions ("we use
ListAgentKey for the showing agent") MUST live here, never there. This
directory READS from `../reso-dd-kb/raw/{fields,field_definitions,
lookups,lookup_values}.csv` and NEVER writes anywhere under
`../reso-dd-kb/`.

## Phase boundaries

This directory is built in phases. Do NOT mix phases in a single
commit:

| Phase | Reads | Writes |
|---|---|---|
| Inventory | `../../../raw/dash/*.docx`, `../../../raw/qobrix/qobrix_openapi.yaml`, `../../../raw/current-business-practice/*.xlsx` | `raw/dash_inventory.csv`, `raw/qobrix_inventory.csv`, `raw/cbp_inventory.csv` |
| Curate | `raw/*_inventory.csv`, `../reso-dd-kb/raw/fields.csv` | `raw/mapping_curated.csv` (HAND-EDITED) |
| Join | `raw/*_inventory.csv`, `raw/mapping_curated.csv`, `../reso-dd-kb/raw/{fields,lookups,lookup_values}.csv` | `raw/alignment_<resource>.csv` (one per resource) |
| Emit | `raw/alignment_*.csv`, `raw/mapping_curated.csv`, `../reso-dd-kb/raw/field_definitions.csv` | `wiki/agent-docs/**` |

A Phase-N script must not read inputs from Phase >N (no time travel).
A Phase-N script must not modify outputs of Phase <N (no rewriting
upstream).

## File ownership

| Path | Owner | Edit by hand? |
|---|---|---|
| `raw/dash_inventory.csv` | `scripts/01_inventory_dash.py` | No. Re-run 01. |
| `raw/qobrix_inventory.csv` | `scripts/02_inventory_qobrix.py` | No. Re-run 02. |
| `raw/cbp_inventory.csv` | `scripts/03_inventory_cbp.py` | No. Re-run 03. |
| `raw/mapping_curated.csv` | humans + LLM agents (with review) | **Yes.** This is the only hand-edited CSV. |
| `raw/alignment_*.csv` | `scripts/04_join_alignment.py` | No. Re-run 04. |
| `wiki/agent-docs/**` | `scripts/05_emit_mapping_docs.py` | No. Re-run 05. |
| `USAGE.md`, `README.md`, `AGENTS.md` | humans + LLM agents (with review) | Yes. |
| `scripts/**` | humans + LLM agents (with review) | Yes. |

## In-scope resources

The 6 RESO resources all three sources (Dash, Qobrix, SIR) collectively
touch: `Property`, `Member`, `Office`, `Contacts`, `Teams`, `Media`.

`ShowingAppointment`, `OpenHouse`, `HistoryTransactional`, `Prospecting`
are out of scope here - they belong in a follow-up plan.

## Determinism

Every script must:
- Sort CSV rows by a stable key.
- Use a stable column order.
- Quote consistently (`csv.QUOTE_MINIMAL`).
- Not include any timestamps, hashes, or run-IDs in row content.
- Use `KB_ROOT = Path(__file__).resolve().parent.parent` for the
  source-mappings root, and `REPO_ROOT = KB_ROOT.parent.parent.parent`
  for the matrix-platform-kb repo root (where `raw/` lives).

This is so each refresh produces a small, reviewable diff in git.

## Verification gates

`04_join_alignment.py` ends with hard assertions. The script must exit
non-zero on any breach. Do NOT commit a partial join.

Required gates:

1. Every `mapping_curated.csv` row's `reso_field` exists in
   `../reso-dd-kb/raw/fields.csv` for the matching `reso_resource`,
   OR `is_extension=true` AND `reso_field` starts with `x_sm_`.
2. Every non-empty `dash_label` cited in `mapping_curated.csv` exists
   in `dash_inventory.csv`.
3. Every non-empty `qobrix_path` cited in `mapping_curated.csv` exists
   in `qobrix_inventory.csv`.
4. Every non-empty `sir_label` cited in `mapping_curated.csv` exists
   in `cbp_inventory.csv`.
5. Every `value_mapping_json` mapping target value exists in the
   corresponding RESO lookup (`../reso-dd-kb/raw/lookup_values.csv`)
   when the field has a closed lookup.

Gate failures must print exact source rows and the mismatch reason.
Do NOT relax a gate to make the build green.

## What this directory does NOT contain

- No alias map of any kind. Every fact traces back to a row in
  `dash_inventory.csv`, `qobrix_inventory.csv`, `cbp_inventory.csv`,
  or `mapping_curated.csv`.
- No code. The mapping is documentation; consuming code (CDL ingestion
  EFs, syndication adapters) reads `raw/alignment_*.csv` directly or
  via its own typed adapter.
- No project-specific RESO opinions for projects other than Sharp
  Matrix. Other consuming projects must keep their own mapping table.
