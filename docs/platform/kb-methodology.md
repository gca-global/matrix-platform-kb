# KB Methodology — Design Principles, Versioning, and Contribution

> This document explains how the Sharp Matrix Knowledge Base itself is designed,
> maintained, and versioned. It serves as both a competitive advantage and an
> operational guide for contributors.

---

## Design Principles

| Principle | Implementation |
|-----------|----------------|
| **LLM-first** | Structured for AI agent consumption, not just human reading |
| **Progressive disclosure** | AGENTS.md → INDEX.md → chapter indexes → individual docs |
| **Task-based navigation** | "If you need to…" table in [AGENTS.md](../../AGENTS.md) |
| **Explicit reading order** | Numbered steps for Lovable in "For Lovable — Start Here" |
| **Self-contained chapters** | Each chapter works independently with cross-references |

## Why This Matters

No PropTech leader (Zillow, Compass, Redfin, CoStar) has published an LLM-readable KB designed as an executable specification for AI-powered app builders. This is a genuine competitive advantage.

## Semantic Versioning for the KB

| Version | When to Bump |
|---------|--------------|
| **Major** | Breaking structure changes (renaming AGENTS.md, reorganizing chapters) |
| **Minor** | New files (adding a new doc) |
| **Patch** | Content updates (fixing, expanding existing docs) |

Changelog maintained in repo; tag releases when shipping major/minor bumps.

## Breaking Change Detection

Checklist for changes that could affect Lovable:

- [ ] Renaming files referenced in AGENTS.md
- [ ] Changing table/column names in data model docs
- [ ] Altering auth flow patterns in app-template.md
- [ ] Modifying RLS patterns in security-model.md
- [ ] Changing Supabase project IDs or Edge Function names

## Contribution Guidelines

**Adding a new doc:**

1. Create file (kebab-case.md)
2. Add to chapter index (e.g. `docs/product-specs/index.md`)
3. Add to AGENTS.md tree
4. Add to INDEX.md table
5. Add task nav entry in AGENTS.md if applicable

**Naming**: Use kebab-case for all doc filenames. **Cross-references**: Every new doc must link to related docs at the bottom.

## Validation Process

### Automated Validation (`scripts/validate-kb.sh`)

The KB includes a mechanical validation script that checks:

| Check | What It Validates |
|-------|-------------------|
| File references | All paths in `AGENTS.md` tree resolve to actual files |
| Cross-links | All `[text](path.md)` links in every doc resolve |
| Project IDs | Supabase project IDs in docs match known instances |
| Staleness | Flags docs not updated via git in 90+ days |

Run: `bash scripts/validate-kb.sh` from the repo root.

Exit code 0 = all checks pass. Exit code 1 = errors found (broken links, missing files).

### When to Run Validation

- Before major Lovable builds
- After adding new data model docs
- After changing AGENTS.md structure
- After adding/renaming any KB file
- Weekly as part of doc-gardening (see below)

### Manual Validation (supplemental)

Checks that require human or database access:

- Table names in data model docs vs live Supabase schema
- Edge Function names vs deployed functions (via `supabase functions list`)
- Content accuracy of business process docs

## Entropy Management & Doc Gardening

Inspired by [OpenAI's harness engineering approach](https://openai.com/index/harness-engineering/),
the KB treats documentation entropy like technical debt: pay it down continuously
in small increments rather than letting it compound.

### The Problem

Agents replicate patterns that already exist in the repository — even stale or
incorrect ones. Over time this leads to drift. Without active maintenance:

- Stale rules quietly become "attractive nuisances" (agents follow them faithfully)
- Cross-references rot as files are renamed or restructured
- Golden principles diverge from actual codebase behavior

### Doc-Gardening Process

| Cadence | Activity | Tooling |
|---------|----------|---------|
| **Weekly** | Run `scripts/validate-kb.sh`, fix broken links and missing refs | Automated script |
| **Monthly** | Review stale docs flagged by the script (90+ day threshold) | Git history + manual review |
| **Per-sprint** | Update [QUALITY_SCORE.md](../QUALITY_SCORE.md) grades if domains improved or regressed | Manual assessment |
| **Per-sprint** | Update [tech-debt-tracker.md](../exec-plans/tech-debt-tracker.md) — resolve or add items | Manual assessment |
| **On-change** | When a decision contradicts an existing doc, update the doc immediately | Human or agent |

### Agent-Driven Gardening

Use this prompt template to have an AI agent perform a gardening pass:

> Run `scripts/validate-kb.sh` and fix all errors. Then review docs flagged as
> stale. For each stale doc, either update it to reflect current codebase state
> or add a note explaining why the content is still accurate. Update the
> `QUALITY_SCORE.md` grades and `tech-debt-tracker.md` based on your findings.

### Taste Feedback Loop

When a human reviews agent output and finds a pattern violation:

1. Identify which golden principle was violated (see [GOLDEN_PRINCIPLES.md](../GOLDEN_PRINCIPLES.md))
2. If the principle exists but was ignored → check if the principle is discoverable (is it linked from relevant docs?)
3. If no principle covers the case → add a new principle to `GOLDEN_PRINCIPLES.md`
4. If the principle should be mechanically enforced → add a check to `validate-kb.sh` or app linters

This loop ensures human taste is captured once and applied continuously.

## Document Conventions

- **Tables over prose**: Prefer structured tables for specifications; easier for LLM parsing.
- **Cross-reference section**: Every doc ends with a "Cross-Reference" table linking to related docs.
- **For Lovable callouts**: Use blockquote `> **For Lovable**:` when content directly affects app-building.
- **Source attribution**: When a doc derives from external sources (PDFs, Mermaid diagrams), cite them at the top.

## Cross-Reference

| For | See |
|-----|-----|
| Master navigation | [AGENTS.md](../../AGENTS.md) |
| Chapter index and summaries | [INDEX.md](../INDEX.md) |
| App template (Lovable entry point) | [app-template.md](app-template.md) |
| Platform chapter index | [platform/index.md](index.md) |
| Golden principles (engineering invariants) | [GOLDEN_PRINCIPLES.md](../GOLDEN_PRINCIPLES.md) |
| Quality grades by domain | [QUALITY_SCORE.md](../QUALITY_SCORE.md) |
| Execution plans | [exec-plans/index.md](../exec-plans/index.md) |
| Technical debt tracker | [exec-plans/tech-debt-tracker.md](../exec-plans/tech-debt-tracker.md) |
| KB validation script | `scripts/validate-kb.sh` |
