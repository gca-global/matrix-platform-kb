# Execution Plans

> Execution plans are first-class artifacts in this repository. They capture
> complex, multi-step work with enough detail for an agent to pick up, continue,
> or verify progress without external context.

## Why Execution Plans

In an agent-first workflow, knowledge that lives only in chat threads or people's
heads is invisible to agents. Execution plans solve this by making intent,
progress, and decisions discoverable in the repository.

## Directory Structure

```
docs/exec-plans/
├── index.md                 ← this file
├── tech-debt-tracker.md     ← known technical debt by domain
├── active/                  ← plans currently being executed
│   └── <plan-name>.md
└── completed/               ← archived finished plans
    └── <plan-name>.md
```

## Plan Format

Every execution plan follows this template:

```markdown
# <Plan Title>

| Field       | Value                    |
|-------------|--------------------------|
| Status      | active / completed / abandoned |
| Created     | YYYY-MM-DD               |
| Owner       | name or role             |
| Related ADR | ADR-NNN (if applicable)  |

## Goal

One paragraph describing the desired end state.

## Context

Why this work is needed. Link to relevant KB docs, ADRs, or issues.

## Steps

- [ ] Step 1 — description
- [ ] Step 2 — description
- [x] Step 3 — completed description

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| YYYY-MM-DD | Chose approach X over Y | Because Z |

## Verification

How to confirm the plan is complete (tests, manual checks, metrics).
```

## Lifecycle

| Phase | Action |
|-------|--------|
| **Create** | Write plan in `active/`, link from relevant docs |
| **Execute** | Check off steps, record decisions in the log |
| **Complete** | Move from `active/` to `completed/`, update `tech-debt-tracker.md` if debt was resolved |
| **Abandon** | Set status to `abandoned`, document why, move to `completed/` |

## Relationship to Lovable Prompts

For Lovable-managed apps, the Lovable prompt *is* the execution plan for that
change. Prompts stored in `matrix-testing-suite/hrms-uat/prompts/` follow the
same principle: structured intent that an agent (Lovable) can execute without
external context.

## Cross-Reference

| For | See |
|-----|-----|
| Known technical debt | [tech-debt-tracker.md](tech-debt-tracker.md) |
| Architecture decisions | [ADR index](../architecture/decisions/index.md) |
| KB methodology | [kb-methodology.md](../platform/kb-methodology.md) |
| Quality grades by domain | [QUALITY_SCORE.md](../QUALITY_SCORE.md) |
