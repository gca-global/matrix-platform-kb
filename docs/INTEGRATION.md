# How the KB layers compose — integrated stack

> A single integrated KB. This page explains how the four
> RESO-aligned chapters fit together into one stack, so an LLM
> agent can pick the right layer for the task at hand.

This is a navigation aid, not a system-of-record. The
system of record for each layer is its own chapter.

## The four layers

```mermaid
flowchart TB
    subgraph L1["Layer 1: Canonical data model"]
        L1A["data-models/reso-dd-kb/<br/>RESO DD 2.0 — 41 resources, 1,745 fields, 222 lookups<br/>(canonical, RESO-only, mirror-faithful)"]
    end
    subgraph L2["Layer 2: Source mappings"]
        L2A["data-models/source-mappings/<br/>Dash / Qobrix / SIR -> RESO DD<br/>(96 curated rows, 6 resources, x_sm_* extensions for gaps)"]
    end
    subgraph L3["Layer 3: Canonical state machines"]
        L3A["business-processes/canonical-processes/<br/>Vendor-neutral RESO state machines<br/>(10 processes, 709 RESO citations, mermaid diagrams)"]
    end
    subgraph L4["Layer 4: Project flavour"]
        L4A["business-processes/*.md (Sharp-SIR)<br/>Operational pipelines, lead qualification,<br/>checklists — opinionated, project-specific"]
    end
    subgraph L5["Layer 5: Cross-cutting view"]
        L5A["integration/wiki/agent-docs/by_resource/<br/>Per-resource one-stop view joining all layers above<br/>(generated, do NOT hand-edit)"]
    end
    L1A --> L2A
    L1A --> L3A
    L2A --> L3A
    L3A --> L4A
    L1A --> L5A
    L2A --> L5A
    L3A --> L5A
    L4A --> L5A
```

## What each layer answers

| Layer | Answers the question | System of record |
|---|---|---|
| 1. Canonical data model | "What does RESO say about `Property.StandardStatus`?" | [`data-models/reso-dd-kb/`](data-models/reso-dd-kb/USAGE.md) |
| 2. Source mappings | "Which Dash / Qobrix / SIR field IS `Property.StandardStatus`?" | [`data-models/source-mappings/`](data-models/source-mappings/USAGE.md) |
| 3. Canonical state machines | "What transitions in or out of `StandardStatus = Pending`?" | [`business-processes/canonical-processes/`](business-processes/canonical-processes/USAGE.md) |
| 4. Project flavour | "How does Sharp-SIR's `AGREEMENT SIGNED` stage map to RESO?" | [`business-processes/`](business-processes/index.md) (the five `*.md` siblings) |
| 5. Cross-cutting view | "Show me everything about `Property` across all four layers." | [`integration/`](integration/USAGE.md) |

## Picking the right layer

Use this decision table when navigating the KB:

| Task | Start at |
|---|---|
| Looking up a RESO field name / lookup value | Layer 1 — `data-models/reso-dd-kb/USAGE.md` |
| Finding which Dash field becomes which RESO field | Layer 2 — `data-models/source-mappings/USAGE.md` |
| Designing an `x_sm_*` extension | Layer 2 — `data-models/source-mappings/USAGE.md` + [`platform-extensions.md`](data-models/platform-extensions.md) |
| Implementing state-machine logic in Atlas / CDL | Layer 3 — `business-processes/canonical-processes/USAGE.md` |
| Writing a Sharp-SIR operational SOP | Layer 4 — `business-processes/index.md` |
| One-stop "everything about resource X" lookup | Layer 5 — `integration/USAGE.md` |

## Example: tracing one fact across all layers

Take the fact "the listing went under contract".

- **Layer 1** says the canonical state is
  `Property.StandardStatus = "Pending"` (with `MlsStatus` mirroring,
  `PendingTimestamp` / `PurchaseContractDate` /
  `ContractStatusChangeDate` / `StatusChangeTimestamp` updated).
- **Layer 2** says the Dash field that drives this is
  `propertyStatus = "PEND"` (or its equivalent) and the Qobrix path
  is `Property.transaction_state`. Mismatches go to `x_sm_*`.
- **Layer 3** says the transition is
  `Active -> Pending` (or `Active -> Active Under Contract ->
  Pending`), driven by an "offer accepted" trigger, and emits a
  `HistoryTransactional` row with `ChangeType = Pending`. See
  [`canonical-processes/processes/listing-lifecycle.md`](business-processes/canonical-processes/processes/listing-lifecycle.md).
- **Layer 4** says Sharp-SIR's pipeline calls this stage `SOLD` and
  the broker has a checklist of follow-up tasks. See
  [`business-processes/listing-pipeline.md`](business-processes/listing-pipeline.md).
- **Layer 5** is the integrated per-resource page that surfaces
  all of the above on one screen. See
  [`integration/wiki/agent-docs/by_resource/property.md`](integration/wiki/agent-docs/by_resource/property.md).

## Boundaries the layers MUST respect

These are the harness-engineering invariants that keep the layers
composable:

- **Layer 1 is RESO-only.** It NEVER imports Dash, Qobrix, or
  SIR concepts. Mirror is regenerated, never hand-edited.
- **Layer 2 NEVER writes back into Layer 1.** It consults the RESO
  CSVs and curates a mapping side-by-side.
- **Layer 3 NEVER writes back into Layer 1 or Layer 2.** It
  consults the RESO CSVs to validate citations and pins state
  transitions to canonical names.
- **Layer 4 NEVER edits the canonical layer.** Project flavours map
  ONTO the canonical states; they do not invent new ones in the
  RESO vocabulary. New states / transitions specific to the project
  go through `x_sm_*` extensions in Layer 2.
- **Layer 5 is purely derived.** Every byte is generated from
  Layers 1–4; the chapter has no hand-edited content under
  `wiki/agent-docs/`. Re-runs produce zero-byte diffs.

## Phase-gated pipelines per layer

Each generative chapter follows the same Author -> Validate -> Emit
pipeline pattern:

| Layer | Phase 1 (Mirror / Author) | Phase 2 (Validate / Curate) | Phase 3 (Emit) |
|---|---|---|---|
| 1. reso-dd-kb | Mirror RESO XML → CSVs | (built-in to Phase 1) | DBML + per-resource markdown + `_index.md` |
| 2. source-mappings | Inventory Dash / Qobrix / SIR | Curate `mapping_curated.csv` + join with RESO + 5 hard-fail gates | per-source + per-resource markdown + `_index.md` |
| 3. canonical-processes | Hand-write `processes/*.md` | Validate citations + mermaid (5 hard-fail gates) | `wiki/agent-docs/_index.md` + `state_machines.md` + `coverage.csv` |
| 5. integration | (no author phase) | (no validate phase) | `wiki/agent-docs/by_resource/<res>.md` joining all layers |

Layer 4 (Sharp-SIR flavour) is hand-edited operational documentation
and does not have a generative pipeline; it consumes Layer 3 by
linking out, never by transforming.

## Mechanical enforcement

[`scripts/validate-kb.sh`](../scripts/validate-kb.sh) enforces the
following cross-chapter invariants in addition to per-chapter
freshness:

- Check 1 — every `AGENTS.md` file reference resolves
- Check 2 — every markdown cross-link resolves (chapter to chapter)
- Check 5 — `reso-dd-kb` generated artifacts at least as fresh as
  raw CSVs
- Check 6 — `source-mappings` generated artifacts at least as fresh
  as inventories and curated rows
- Check 7 — `canonical-processes` generated artifacts at least as
  fresh as `processes/*.md`
- Check 8 — `integration/` generated artifacts at least as fresh as
  every layer 1–3 `_index.md` (cross-chapter freshness)

A green `validate-kb.sh` is therefore a guarantee that the four
layers are mutually consistent.

## Where to add new content

| New content | Add it to |
|---|---|
| A new RESO resource that RESO has now standardised | Re-mirror Layer 1 (`reso-dd-kb`); do NOT hand-edit |
| A new `x_sm_*` field Sharp-SIR needs | Layer 2 (`source-mappings/raw/mapping_curated.csv` + `platform-extensions.md`) |
| A new RESO-aligned business process not in the 10 canonical ones | Layer 3 (`canonical-processes/processes/<new>.md`) — also bump README's in-scope table and re-run pipeline |
| A new Sharp-SIR operational pipeline | Layer 4 (`business-processes/<new>.md`) — link forward to its canonical baseline |
| A new cross-cutting per-resource summary | NEVER hand-edit Layer 5 — extend `integration/scripts/01_emit_resource_views.py` instead |

## Anchored in harness engineering

This entire stack mirrors the OpenAI harness-engineering principles
the project follows:

- **Repository as system of record.** Every fact is anchored in a
  CSV, a markdown file, or a generated artifact under git.
- **Progressive disclosure.** `AGENTS.md` is short; deep documents
  are linked from per-chapter `USAGE.md` and consumed only when
  needed.
- **Mechanical enforcement.** `validate-kb.sh` is the single point
  of "is the KB self-consistent?" — green means the layers compose.
- **Phase-gated pipelines.** Each generative chapter has the same
  Author / Validate / Emit shape; later phases never write to
  earlier-phase outputs.
- **Generated outputs are zero-byte-diff.** Re-running any emit
  script with no input changes produces identical bytes.
