# AGENTS.md - rules for LLM agents working in `canonical-processes/`

## What this directory does

Documents the canonical, vendor-neutral, RESO DD 2.0-aligned MLS
business processes. Ten process docs (Listing, Showing, OpenHouse,
Lead-Contact, Transaction, Member/Office/Team onboarding, Caravan,
Media), each carrying a mermaid state machine, transition tables,
RESO field/lookup citations, and cross-resource interactions.

This is documentation, not code. Consuming applications (Atlas, CDL
ingestion, syndication adapters) reference these docs to learn the
canonical state-machine semantics RESO DD implies.

## Boundary with reso-dd-kb

[`reso-dd-kb/AGENTS.md`](../../data-models/reso-dd-kb/AGENTS.md) is "RESO DD 2.0
only". Process narratives are opinionated (which transitions are
valid, who triggers them, what fields must change), so they live
HERE. This subtree READS from
`../../data-models/reso-dd-kb/raw/{resources,fields,lookups,lookup_values}.csv` and
NEVER writes anywhere under `../../data-models/reso-dd-kb/`.

## Boundary with `docs/business-processes/`

[`docs/business-processes/`](../index.md) is
Sharp-SIR-flavoured (PROSPECT / AGREEMENT SIGNED / etc., no RESO
citations). It describes the actual operational flow at Sharp SIR.

THIS chapter describes the vendor-neutral RESO baseline. Any consumer
project (Sharp SIR, future affiliates, third-party portals) can map
its own process to the canonical baseline here. Do NOT mix the two:

- A process step expressed in terms of `Property.StandardStatus = Active`
  and `MlsStatus = Coming Soon` belongs HERE.
- A process step expressed in terms of "Anna sends the listing-doc
  email" belongs in `docs/business-processes/`.

## Phase boundaries

This directory is built in phases. Do NOT mix phases in a single
commit:

| Phase | Reads | Writes |
|---|---|---|
| Author | `../../data-models/reso-dd-kb/raw/...csv` (consult-only) | `processes/*.md` (HAND-EDITED) |
| Validate | `processes/*.md`, `../../data-models/reso-dd-kb/raw/{resources,fields,lookup_values}.csv` | `raw/citations.csv` |
| Emit | `raw/citations.csv`, `processes/*.md`, `../../data-models/reso-dd-kb/raw/...` | `wiki/agent-docs/{_index,state_machines}.md`, `raw/coverage.csv` |

A Phase-N script must not read inputs from Phase >N (no time travel).
A Phase-N script must not modify outputs of Phase <N (no rewriting
upstream).

## File ownership

| Path | Owner | Edit by hand? |
|---|---|---|
| `processes/*.md` | humans + LLM agents (with review) | **Yes.** These are the canonical process narratives. |
| `raw/citations.csv` | `scripts/01_validate_citations.py` | No. Re-run 01. |
| `raw/coverage.csv` | `scripts/02_emit_index.py` | No. Re-run 02. |
| `wiki/agent-docs/_index.md` | `scripts/02_emit_index.py` | No. Re-run 02. |
| `wiki/agent-docs/state_machines.md` | `scripts/02_emit_index.py` | No. Re-run 02. |
| `USAGE.md`, `README.md`, `AGENTS.md` | humans + LLM agents (with review) | Yes. |
| `scripts/**` | humans + LLM agents (with review) | Yes. |

## Citation contract

Every `processes/*.md` MUST end with exactly one HTML-comment
citation block of this form:

```
<!-- reso-citations
Resource: <ResourceName>
Field: <ResourceName>.<StandardName>
LookupValue: <LookupName>.<StandardValue>
-->
```

Allowed prefixes: `Resource:`, `Field:`, `LookupValue:`. Anything
else is a hard error. The validator parses ONLY this block to build
`raw/citations.csv` and to enforce the three reference gates.

In-prose markdown links to `../../data-models/reso-dd-kb/...` are encouraged for
readability but are NOT validated by `01_validate_citations.py` -
authors must keep them in sync with the citation block by hand.

## Diagram contract

Every `processes/*.md` MUST contain at least one mermaid
`stateDiagram-v2` block (heuristic: lines beginning with the literal
"```mermaid" followed by "stateDiagram-v2"). The diagram is the
canonical machine-readable state machine; tables that follow it
expand semantics row-by-row.

Use mermaid `stateDiagram-v2` (not `flowchart`) for state machines.
Use `flowchart` only for sub-process call-graphs.

## Verification gates (`01_validate_citations.py`)

Hard-fail gates (script exits non-zero on any breach):

1. Every cited `Resource: X` exists in `../../data-models/reso-dd-kb/raw/resources.csv`.
2. Every cited `Field: X.Y` exists in `../../data-models/reso-dd-kb/raw/fields.csv`
   for the matching `ResourceName=X`, `StandardName=Y`.
3. Every cited `LookupValue: L.V` exists in
   `../../data-models/reso-dd-kb/raw/lookup_values.csv` for the matching
   `LookupName=L`, `StandardValue=V`.
4. Every process file has exactly one `<!-- reso-citations -->` block.
5. Every process file has at least one `stateDiagram-v2` mermaid
   block.

Failures must print exact line numbers and unresolved citations. Do
NOT relax a gate to make the build green.

## Determinism

Generated files (`raw/citations.csv`, `raw/coverage.csv`,
`wiki/agent-docs/*.md`) must:

- Sort rows by a stable key (`process`, `citation_kind`,
  `citation_value`).
- Use a stable column order.
- Quote consistently (`csv.QUOTE_MINIMAL`).
- Not embed timestamps, hashes, or run-IDs in row content.

So each refresh produces a small, reviewable diff in git.

## What this directory does NOT contain

- No code. The processes are documentation; consuming applications
  load `raw/citations.csv` if they need a machine-readable state
  catalogue.
- No project-specific opinions for projects other than the canonical
  RESO baseline. Sharp-SIR, affiliate brokerages, etc. keep their own
  process docs that map TO this baseline.
- No alias maps for source-system field names (Dash/Qobrix/SIR). That
  belongs in [`source-mappings/`](../../data-models/source-mappings/AGENTS.md).
