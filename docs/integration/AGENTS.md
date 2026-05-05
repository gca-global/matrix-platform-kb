# AGENTS.md - rules for LLM agents working in `integration/`

## What this directory does

Emits per-resource cross-cutting integrated views that join the
canonical RESO data model (Layer 1), the source mappings (Layer 2),
and the canonical state machines (Layer 3) into a single page per
resource. This is the navigation surface for agents who want a
one-stop view of "everything about resource X".

This is generated documentation. Do NOT hand-edit anything under
`wiki/agent-docs/`. Re-run the emit pipeline.

## Boundary with other chapters

This chapter is purely DERIVATIVE:

- Reads from `../data-models/reso-dd-kb/raw/{resources,fields,
  lookup_values}.csv` (Layer 1 system of record).
- Reads from `../data-models/source-mappings/raw/alignment_*.csv`
  and `wiki/agent-docs/by_resource/*.md` (Layer 2 system of record).
- Reads from `../business-processes/canonical-processes/raw/citations.csv`
  and `processes/*.md` (Layer 3 system of record).
- Reads from `../business-processes/*.md` (Layer 4 Sharp-SIR
  flavour) for forward links.
- NEVER writes anywhere outside this chapter.

If a fact is wrong on an integration page, the fix MUST be made
in the source-of-record chapter, not here.

## Phase boundaries

| Phase | Reads | Writes |
|---|---|---|
| Emit | All four layers' CSVs and indexes | `wiki/agent-docs/by_resource/<res>.md`, `raw/integration_index.csv` |

There is no Author phase and no Validate phase: every byte of
output is mechanically derived. The "validation" is determinism
(re-runs produce zero-byte diffs) and link-resolution (every
generated cross-reference must point at a file that exists).

## File ownership

| File | Owner | Hand-edit allowed? |
|---|---|---|
| `AGENTS.md` | Subsystem authors | Yes, structural rules only |
| `USAGE.md` | Subsystem authors | Yes, task-oriented entry points |
| `README.md` | Subsystem authors | Yes, methodology |
| `scripts/01_emit_resource_views.py` | Subsystem authors | Yes, the only logic that may change emit output |
| `wiki/agent-docs/by_resource/*.md` | Generated | NO |
| `raw/integration_index.csv` | Generated | NO |

## Determinism contract

Re-running `python scripts/01_emit_resource_views.py` with no input
changes MUST produce zero-byte diffs in every file under
`wiki/agent-docs/by_resource/` and `raw/integration_index.csv`. All
iteration is over sorted collections; no timestamps appear in
generated bodies.

## Cross-chapter freshness

`scripts/validate-kb.sh` Check 8 enforces that every integration
output is at least as fresh as the source-of-record indexes it
joins. If `reso-dd-kb`, `source-mappings`, or `canonical-processes`
was regenerated, this chapter MUST be re-emitted before commit.

## When NOT to edit

- Dangling cross-link in a generated page -> fix the linker logic
  in `scripts/01_emit_resource_views.py`, not the markdown.
- Resource missing -> add it to the resource list in the script
  (or upstream).
- New layer (e.g. a "channel-distribution" view) -> add a new
  reader inside the script, not a new file under `wiki/agent-docs/`.

See [`../INTEGRATION.md`](../INTEGRATION.md) for the layered
architecture this chapter sits on top of.
