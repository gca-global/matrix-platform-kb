# Chapter 4: Business Processes — Index

> Operational workflows, pipelines, qualification rules, and checklists.
>
> This chapter has two layers:
>
> - **Sharp-SIR flavour** — the project-specific operational pipelines actually run at Sharp Sotheby's (the documents listed first below).
> - **Canonical baseline** — the vendor-neutral RESO DD 2.0-aligned process catalogue that Sharp-SIR (and any future affiliate brokerage) maps onto. Lives in [`canonical-processes/`](canonical-processes/USAGE.md).

## Documents

### Sharp-SIR flavour (project-specific)

| Document | What It Contains |
|----------|-----------------|
| [listing-pipeline.md](listing-pipeline.md) | Seller-side pipeline: 8 stages with tasks, artifacts, AI actions |
| [sales-pipeline.md](sales-pipeline.md) | Buyer-side pipeline: 8 stages with tasks, artifacts, AI actions |
| [lead-qualification.md](lead-qualification.md) | Raw Lead → MQL → SQL qualification path with BANT criteria |
| [follow-up-vs-active-sales.md](follow-up-vs-active-sales.md) | Boundary between nurturing and active deal management |
| [listing-checklist.md](listing-checklist.md) | Operational checklists for broker, marketing, and finance roles |

### Canonical baseline (vendor-neutral, RESO-aligned)

| Document | What It Contains |
|----------|-----------------|
| [canonical-processes/USAGE.md](canonical-processes/USAGE.md) | **Start here for canonical state-machine semantics.** Task-oriented entry points: state lookup, step implementation, cross-resource impact analysis. |
| [canonical-processes/README.md](canonical-processes/README.md) | Methodology, 2-script phase-gated pipeline (Author → Validate → Emit), boundaries with `reso-dd-kb/` and Sharp-SIR flavour. |
| [canonical-processes/AGENTS.md](canonical-processes/AGENTS.md) | Local rules: phase boundaries, citation contract, mermaid contract, 5 hard-fail gates. |
| [canonical-processes/wiki/agent-docs/_index.md](canonical-processes/wiki/agent-docs/_index.md) | Generated catalogue: 10 processes, per-resource and per-lookup coverage matrices, roll-up totals (709 RESO citations). |
| [canonical-processes/wiki/agent-docs/state_machines.md](canonical-processes/wiki/agent-docs/state_machines.md) | Generated consolidated mermaid index: every `stateDiagram-v2` block from the 10 process docs in one page. |
| [canonical-processes/processes/](canonical-processes/processes/) | The 10 hand-written process docs: Listing, Showing, OpenHouse, Lead-Contact, Transaction, Member/Office/Team onboarding, Caravan, Media. |

## Key Process Rules (Sharp-SIR flavour)

1. **Two parallel pipelines** run simultaneously: seller-side (listings) and buyer-side (sales)
2. **Matching is continuous**: every new listing triggers buyer matching; every new buyer triggers listing matching
3. **First meeting/showing** is the trigger that moves a lead from follow-up (nurturing) to active sales
4. **Long-term leads** (>12 months timeline) go to nurturing pool, not active forecast
5. **Every disqualification** must have a documented reason fed back to marketing

## Boundary with the canonical baseline

A Sharp-SIR pipeline stage like `PROSPECT → AGREEMENT SIGNED → ACTIVE` MUST map onto the canonical
[`Property.StandardStatus`](canonical-processes/processes/listing-lifecycle.md) state machine
(`Incomplete → Coming Soon | Active → ...`). When a Sharp-SIR stage cannot be expressed in canonical
RESO terms, that gap belongs in [`source-mappings/`](../data-models/source-mappings/USAGE.md) as
an `x_sm_*` extension, not as a fork of the canonical process.
