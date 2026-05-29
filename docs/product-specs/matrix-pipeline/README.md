# `matrix-pipeline` — CRM for Sharp SIR (Sharp Matrix Platform)

> Single canonical source-of-truth for the **Sales Pipeline CRM**: requirements, architecture, AI Copilot, integrations, and the 8-week build plan that takes it from kickoff to a power-user staging prototype.

## What this is

The Sharp Matrix CRM (`matrix-pipeline`) is the luxury-real-estate sales pipeline app for Sharp SIR brokers in Cyprus, Hungary, and Kazakhstan. It is built strictly on canonical RESO DD 2.0 (no `x_sm_*` extensions) with two explicit project-flavour exceptions documented in [`wiki/architecture.md#escape-hatch`](wiki/architecture.md#escape-hatch):

1. **`Referral`** as a self-standing CRM entity (luxury referral economy in HNWI/UHNWI).
2. **Commission Engine** — CRM-internal ERP-lite for sales-broker P&L forecasting + reconciliation with external Finance ERP.

## Where to start

| Audience | Start here |
|---|---|
| LLM agent (Lovable, Cursor, etc.) | [`AGENTS.md`](AGENTS.md) → [`INDEX.md`](INDEX.md) → [`roadmap.md`](roadmap.md) (coordination) |
| Anyone asking "where are we / where are we going" | [`roadmap.md`](roadmap.md) — outcome-based journey + per-milestone status |
| New human reader | this `README.md` → [`wiki/overview.md`](wiki/overview.md) → [`roadmap.md`](roadmap.md) → [`phases.md`](phases.md) |
| Implementer (a single feature) | [`phases.md`](phases.md) → relevant week → relevant task → wiki anchor cited in the task |
| Looking for the canonical BRD | [`raw/context-v2.md`](raw/context-v2.md) (immutable — read the wiki first; only open this for provenance) |

## Layout

```text
matrix-pipeline/
├── AGENTS.md            # LLM schema layer — how to read/write this wiki
├── INDEX.md             # Catalog of every wiki page + anchor
├── README.md            # You are here
├── roadmap.md           # Outcome-based roadmap + agent coordination surface
├── log.md               # Chronological append-only log
├── phases.md            # 8-week build plan
├── raw/
│   └── context-v2.md    # Immutable BRD
├── scripts/
│   └── wiki-lint.sh     # PR-time contract checks
└── wiki/
    ├── overview.md           # Scope, personas, pipeline, RESO policy
    ├── entities.md           # Business entities (canonical RESO + Referral)
    ├── processes.md          # End-to-end business processes
    ├── requirements.md       # All FRs and BRs
    ├── ai.md                 # AI Copilot features + plan
    ├── integration.md        # External systems (Listing Module, Finance ERP, …)
    ├── architecture.md       # Three-Supabase, CDL, RESO compliance gates
    └── commission-engine.md  # ERP-lite forecast + reconciliation
```

## How this wiki is maintained

LLM agents do all the bookkeeping. Humans curate sources (the BRD updates), ask questions, and review.

- **Source of truth**: `raw/context-v2.md` is immutable. The wiki is derived; it is **not** edited by hand against the wishes of the raw.
- **Ingest a BRD change**: the LLM identifies touched `§` paths and updates the corresponding wiki sections, frontmatter, INDEX, and `log.md` in a single PR. Rules in [`AGENTS.md`](AGENTS.md).
- **Lint**: [`scripts/wiki-lint.sh`](scripts/wiki-lint.sh) catches orphan anchors, missing FR cross-refs, broken citation contracts.
- **Split**: pages stay compact (~12 files total) and only fan out when triggers in [`AGENTS.md`](AGENTS.md#split-later-rules) fire.

## Provenance

This wiki was generated from `matrix-pipeline-2.0/context-v2.md` (the post-§12.17 QA'd BRD, ~2 100 lines, 312 KB). Initial slice is logged in [`log.md`](log.md#init).

## Cross-references to the broader KB

- **App template + dual-Supabase + SSO + RLS**: [`../../platform/app-template.md`](../../platform/app-template.md) — required reading before building.
- **Canonical RESO DD 2.0**: [`../../data-models/reso-dd-kb/USAGE.md`](../../data-models/reso-dd-kb/USAGE.md) — start here for any RESO field / lookup question.
- **CDL schema**: [`../../data-models/cdl-schema.md`](../../data-models/cdl-schema.md) — Common Data Layer (cross-app shared tables).
- **Security model**: [`../../platform/security-model.md`](../../platform/security-model.md) — 5-level scope, JWT claims, RLS Patterns A-E.
- **Canonical RESO processes**: [`../../business-processes/canonical-processes/`](../../business-processes/canonical-processes/) — vendor-neutral state machines.
