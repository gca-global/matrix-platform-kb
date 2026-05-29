# `matrix-pipeline` — LLM Wiki Schema (AGENTS.md)

> Local rules for LLM agents working inside this subtree.
> Inherits the platform-kb conventions; adds Karpathy LLM-Wiki rules.
> See parent `/AGENTS.md` for KB-wide navigation.

## Purpose

This subtree is the **LLM Wiki for `matrix-pipeline`** (the Sharp Matrix CRM). It exists so Lovable (app + CRM app DB), Cursor (CDL/SSO), and any other agent can load just-the-context-needed for a single task without ingesting the full 2 100-line BRD on every query.

Three layers + a coordination surface (Karpathy pattern):

| Layer | Lives in | Mutability |
|---|---|---|
| Raw | [`raw/context-v2.md`](raw/context-v2.md) | **Immutable** — source of truth, never edited |
| Wiki | [`wiki/*.md`](wiki/) + [`phases.md`](phases.md) | LLM-maintained; kept in sync with `raw/` |
| Schema | This file (`AGENTS.md`) + [`INDEX.md`](INDEX.md) + [`log.md`](log.md) | Slowly co-evolves with the wiki |
| **Coordination surface** | [`roadmap.md`](roadmap.md) | **The durable, outcome-keyed journey view + multi-agent coordination contract.** Read + update it before any structural change (see [#coordination-through-roadmapmd](#coordination-through-roadmapmd)). |

## How to load context for a query

1. Read [`INDEX.md`](INDEX.md). It catalogs every wiki page + the important H2 anchors. (~150 lines.)
1.5. **If the task touches an outcome milestone** — i.e. any FR cluster / KPI in [`wiki/overview.md#kpis`](wiki/overview.md#kpis) — open [`roadmap.md`](roadmap.md) first to see the current `status` + `owner_agent` of the matching `O-*` row, and cite that row in your PR.
2. Drill into the wiki page that owns the anchor, e.g. `wiki/requirements.md#fr-pros-prospecting`.
3. Follow `relates_to` frontmatter and inline `[wiki/...#anchor]` links only as needed.
4. **Do not read `raw/context-v2.md` unless investigating provenance** (e.g. "is this claim in the BRD or inferred?"). The raw file is 2 100+ lines; loading it defeats the wiki.

## How to ingest a BRD change

When `raw/context-v2.md` changes (e.g. a new `§ 12.X` changelog entry is appended):

1. Identify touched `§` paths from the changelog entry.
2. For each touched `§`: update the corresponding wiki page's relevant H2 section + frontmatter `last_updated`.
3. If the change introduces a new FR-ID, a new entity, or a new external system → update [`INDEX.md`](INDEX.md) too.
4. If the change contradicts an existing wiki claim → flag inline with a `> **Divergence (vs prior wiki claim)**` callout AND append a `log.md` entry.
5. Append a `log.md` ingest entry (see format below).

## Page anatomy

Every `wiki/*.md` MUST start with frontmatter:

```yaml
---
title: <Page title>
status: draft | stable | needs-refresh
source: raw/context-v2.md §<X.Y[, §X.Z...]>
last_updated: <YYYY-MM-DD>
tags: [overview|entity|process|fr|ai|integration|architecture|commission-engine]
---
```

Body convention:

```markdown
# Title

> One-paragraph page-level synthesis.

## TOC
- [#anchor-1](#anchor-1)
- [#anchor-2](#anchor-2)

## Section title {#anchor-1}
### Summary
### Canonical RESO mapping (link to reso-dd-kb)
### Requirements (FR-IDs)
### Cross-refs
### Source: [raw/context-v2.md §X.Y](raw/context-v2.md)
```

## Stable identifiers

- **Filenames**: kebab-case, flat under `wiki/`.
- **Anchors**: explicit `{#kebab-case}` on every H2/H3 that is a stable cross-ref target.
- **FR-IDs**: the canonical token shared across raw + wiki + phases (e.g. `FR-PROS-13`).
- **Cross-link form**: `[wiki/<file>.md#<anchor>]` inside this subtree; `[../<other-kb-path>]` for KB-wide refs.

## Split-later rules

This wiki starts compact (8 files in `wiki/`). A section earns its own file **only** when one of these triggers fires:

1. Page > **600 lines** (LLM context-window pressure).
2. A single H2 section > **200 lines**.
3. ≥2 independent atomic implementation tasks in different `phases.md` weeks need only that section.
4. An ADR materially changes only one section's source-of-truth.

When a split happens: extract the section → new file in the same `wiki/` directory; update [`INDEX.md`](INDEX.md); rewrite any inbound `#anchor` links to the new file; append a `log.md` entry (action: `split`).

## `log.md` format

Append-only. Each entry starts with `## [YYYY-MM-DD] <action> | <subject>` so `grep '^## \[' log.md | tail -10` gives the latest activity.

Actions:

| Action | When |
|---|---|
| `init` | First creation of the subtree |
| `ingest` | New raw source ingested OR existing `raw/context-v2.md` changed |
| `edit` | Material wiki edit not driven by a raw change |
| `query` | A non-trivial agent query answered (optional, but recommended for compound learning) |
| `lint` | `scripts/wiki-lint.sh` ran + outcome |
| `split` | A section was promoted to its own file (per split-later rules) |
| `phase-checkpoint` | A `phases.md` week completed; demo signed off |
| `divergence` | A wiki claim was flagged as diverging from `raw/` (escape-hatch) |
| `roadmap` | An outcome milestone in [`roadmap.md`](roadmap.md) changed status / owner / scope |

## Coordination through roadmap.md {#coordination-through-roadmapmd}

[`roadmap.md`](roadmap.md) is the **single coordination surface** across all
agents (Lovable / Cursor / platform-team / business). It is **outcome-keyed**:
milestones (`O-<SLUG>`) map to the product-spec KPI groups
([`wiki/overview.md#kpis`](wiki/overview.md#kpis)) and the FR clusters that
deliver them ([`wiki/requirements.md`](wiki/requirements.md)); the calendar
quarter is only a secondary `target_horizon`.

Contract — **before** any PR that creates/modifies an FR, ADR, schema migration,
EF, or wiki page affecting an outcome:

1. Read `roadmap.md`; find the matching `O-*` row.
2. Update that row's `status` + `last_updated` + `owner_agent` + notes.
3. Append a `roadmap` entry to [`log.md`](log.md).
4. Cite the `O-*` row in the PR description.

A new milestone with **no backing FR cluster / KPI is a defect** — add the FR
first. Milestone ids never embed the quarter (`O-<OUTCOME-SLUG>`, not `O-Q3-…`).

## Lint

`scripts/wiki-lint.sh` is the contract-enforcer. It runs on every PR touching this subtree and checks:

- Orphan H2 anchors (declared `{#x}` but no inbound link).
- Missing FR cross-refs (FR-ID mentioned in `raw/` but not appearing on any wiki page).
- FR coverage parity (FR count in `raw/` ≈ FR count across `wiki/`).
- Frontmatter validity (required keys present).
- Split-rule triggers (warn-only): pages > 600 lines, H2 > 200 lines.
- `log.md` prefix consistency (`^## \[YYYY-MM-DD\] <action> \| `).

## Inherited contracts

- **Mermaid contract** — inherits from `../../business-processes/canonical-processes/AGENTS.md`: no spaces in node IDs, quoted labels with special chars, no explicit colors, no `click` events.
- **Citation contract** — every load-bearing claim cites `raw/context-v2.md §X.Y`.
- **KB-first rule** — inherits from `/.cursor/rules/kb-first.mdc`: plans and implementation must be grounded in the wiki; divergence requires written justification.

## Cross-references

| You want to… | Go to |
|---|---|
| Understand the project at a glance | [`README.md`](README.md) |
| See the long-term outcome journey + coordinate a structural change | [`roadmap.md`](roadmap.md) |
| Catalogue every wiki page + anchor | [`INDEX.md`](INDEX.md) |
| Know what was changed when | [`log.md`](log.md) |
| Read the canonical BRD | [`raw/context-v2.md`](raw/context-v2.md) |
| See the 8-week build plan | [`phases.md`](phases.md) |
| Find a specific FR | [`wiki/requirements.md`](wiki/requirements.md) |
| Understand an entity | [`wiki/entities.md`](wiki/entities.md) |
| Understand a process | [`wiki/processes.md`](wiki/processes.md) |
| Understand an integration | [`wiki/integration.md`](wiki/integration.md) |
| Understand storage / RESO compliance | [`wiki/architecture.md`](wiki/architecture.md) |
| Understand the AI Copilot | [`wiki/ai.md`](wiki/ai.md) |
| Understand the Commission Engine | [`wiki/commission-engine.md`](wiki/commission-engine.md) |
