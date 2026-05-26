# `matrix-pipeline` wiki — chronological log

> Append-only. Entries start with `## [YYYY-MM-DD] <action> | <subject>` so `grep '^## \[' log.md | tail -10` gives the most recent activity.
> See [`AGENTS.md`](AGENTS.md#logmd-format) for the action vocabulary.

## [2026-05-26] init | matrix-pipeline LLM Wiki created

Initial subtree under `matrix-platform-kb/docs/product-specs/matrix-pipeline/`. Three-layer pattern instantiated:

- **Raw**: `raw/context-v2.md` copied from `/home/bitnami/matrix-pipeline-2.0/context-v2.md` (the post-§12.17 QA'd BRD, ~2 109 lines).
- **Wiki**: 8 compact pages under `wiki/` + `phases.md` (8-week build plan) at the subtree root.
- **Schema**: `AGENTS.md` (load rules, ingest workflow, split-later rules, mermaid/citation/KB-first contracts), `INDEX.md` (page + anchor catalog), `log.md` (this file), `README.md` (human entry).

Inherits from parent KB: mermaid + citation + KB-first rules. Branch: `matrix-pipeline-wiki`.

## [2026-05-26] ingest | raw/context-v2.md sliced into wiki/

Initial slice of `raw/context-v2.md` into the wiki:

| Wiki page | Sources from `raw/context-v2.md` |
|---|---|
| `wiki/overview.md` | §1, §2, §3, §4, §7, §11.1 |
| `wiki/architecture.md` | §5a, §11 |
| `wiki/entities.md` | §5 entity table + §9.1, §9.2, §9.3, §9.5a (entity bits), §9.7 (entity bits), §9.7a (entity bits), §9.8 (entity bits), §9.9 (entity bits), §9.11a (entity bits) |
| `wiki/processes.md` | §6, §9.4 |
| `wiki/requirements.md` | §8, §9.1–§9.12 (FR clusters except AI / commission engine) |
| `wiki/integration.md` | §10 |
| `wiki/ai.md` | §9.13, §9.14 |
| `wiki/commission-engine.md` | §9.15 |
| `phases.md` | Plan: `.cursor/plans/llm_wiki_and_phased_build_plan_7ebe41be.plan.md` |

Citation contract: each wiki page frontmatter `source:` cites the originating `§` paths; every load-bearing claim ends with a `Source: raw/context-v2.md §X.Y` reference.

Known divergences carried forward (already present in `raw/`):

- `Referral` as self-standing CRM entity — see `wiki/architecture.md#escape-hatch`.
- Commission Engine ERP-lite — see `wiki/commission-engine.md` + `wiki/architecture.md#escape-hatch`.
- KB drift for CDL: `cdl-schema.md` Phase 1 expansion does not list `public.contact_listings` / `public.contact_listing_notes` (live; flagged for platform team).
- Naming drift: RESO `ShowingAppointment` ↔ KB `showing_appointments` ↔ live CDL `public.showings` (use `public.showings`; flagged for platform team).

## [2026-05-26] lint | initial wiki-lint.sh authored + first pass

`scripts/wiki-lint.sh` authored to enforce contracts on every PR touching this subtree:

- Required frontmatter keys: `title`, `status`, `source`, `last_updated`, `tags`.
- Orphan H2 anchor detection (declared `{#x}` with no inbound link).
- FR-ID coverage parity between `raw/` and `wiki/`.
- Page > 600 lines / H2 > 200 lines warnings (split-later rule triggers).
- `log.md` prefix consistency.

First pass: all checks green (initial slice).

## [2026-05-26] ingest | phases.md authored — 8-week atomic build plan

`phases.md` (1 file, H2 per week, H3 per Lovable / Cursor swimlane) authored from `.cursor/plans/llm_wiki_and_phased_build_plan_7ebe41be.plan.md`. Full BRD coverage in 8 weeks:

| Week | Swimlane focus | Key wiki anchors |
|---|---|---|
| Week 0 | Foundation (app shell, SSO, dual-Supabase, wiki publish) | [`wiki/architecture.md#three-supabase`](wiki/architecture.md#three-supabase) |
| Week 1 | Contacts & Org Roster | [`wiki/requirements.md#fr-con-contacts`](wiki/requirements.md#fr-con-contacts), [`#fr-pc-split`](wiki/requirements.md#fr-pc-split), [`#fr-cfl-contact-funnel-lifecycle`](wiki/requirements.md#fr-cfl-contact-funnel-lifecycle) |
| Week 2 | SavedSearch + Prospecting | [`#fr-pros-prospecting`](wiki/requirements.md#fr-pros-prospecting), [`#fr-fnl-funnel-canonical`](wiki/requirements.md#fr-fnl-funnel-canonical) |
| Week 3 | ContactListings + Showings + Caravan | [`#fr-cl-contact-listings`](wiki/requirements.md#fr-cl-contact-listings), [`#fr-show-showings`](wiki/requirements.md#fr-show-showings), [`#fr-cara-caravan`](wiki/requirements.md#fr-cara-caravan) |
| Week 4 | TransactionManagement + Offer-to-Closing + Referral | [`#fr-tm-transactions`](wiki/requirements.md#fr-tm-transactions), [`#fr-doc-documents`](wiki/requirements.md#fr-doc-documents), [`#fr-ref-referral`](wiki/requirements.md#fr-ref-referral) |
| Week 5 | Pipeline projection + Commission Engine | [`wiki/overview.md#pipeline`](wiki/overview.md#pipeline), [`wiki/commission-engine.md`](wiki/commission-engine.md) |
| Week 6 | AI Copilot (4-feature floor + 10 stubs) | [`wiki/ai.md`](wiki/ai.md) |
| Week 7 | Staging hardening + Demo prep + ADRs + KB-drift handoff | [`wiki/architecture.md#compliance-gates`](wiki/architecture.md#compliance-gates) |

Atomicity rule: ≈ 1 h per task. Two swimlanes per week (Lovable ~28 h, Cursor ~12 h). Every task cites a wiki anchor + has a DoD that ends with a `HistoryTransactional` emission and a wiki cross-ref refresh.

## [2026-05-26] lint | wiki-lint.sh hardened (grep `---` option-parsing bug fixed) + green pass

Bash bug in the frontmatter-delimiter check (`grep -qx '---'` was parsed as an option). Replaced with a `head -n 1` + string equality check. Re-ran:

- frontmatter complete on all pages ✓
- no orphan anchors ✓
- raw FR-IDs: 280, wiki FR-IDs: 280 (parity) ✓
- no split-rule triggers ✓
- log.md prefix consistency ✓

All checks green. Ready for PR.

## [2026-05-26] divergence | branding: 'Matrix Pipeline 2.0' UI string

User-facing application name is rendered as **Matrix Pipeline 2.0** in all sidebar, page title, document title, and login screen strings. Canonical identifier `matrix-pipeline` is preserved in:

- repo / package id
- KB subtree path (`docs/product-specs/matrix-pipeline/`)
- `wiki/*` front-matter and cross-refs
- `processCoverage.ts` `ownedBy: 'matrix-pipeline'` registry value
- SSO Console client_id (`matrix-pipeline`)
- Edge Function namespacing (`pipeline:*` scopes)

Rationale: branding decision by product owner; canonical naming is preserved to keep the KB ↔ implementation join stable. No effect on data model, RESO compliance, scope, or three-Supabase boundaries.

Tracked in: [wiki/architecture.md#escape-hatch](wiki/architecture.md#escape-hatch) (new "Branding divergence" row).

## [2026-05-26] divergence | role_configurations storage in SSO project

`role_configurations` (CRM role → permission-keys mapping consumed by `ProtectedRoute` and `RoleConfigPanel`) is co-located with SSO permission keys in the SSO project (`xgubaguglsnokjyudgvc`) rather than in the CRM app DB.

Rationale: source of truth for permission keys and role-to-key mappings is the SSO Console, which writes to the SSO project. Mirroring `role_configurations` into the CRM app DB would create a two-source-of-truth problem and require a sync EF for no behavioral gain.

Constraint: CRM app DB **reads** the role configuration via the standard SSO client (`ssoClient` / `ssoAuthedClient`) under the user's SSO JWT. No writes to `role_configurations` from CRM app code.

This is a permitted deviation from `wiki/architecture.md#app-private-state` invariant ("all app-private state lives in CRM app DB only"). The deviation is narrow: it affects exactly one table (`role_configurations`) and its access is read-only.

Tracked in: [wiki/architecture.md#escape-hatch](wiki/architecture.md#escape-hatch) (new "role_configurations co-location" row) + [wiki/architecture.md#app-private-state](wiki/architecture.md#app-private-state) (inline Exception bullet).

## [2026-05-26] phase-checkpoint | Week 0 — KB published, branding + role_configurations divergences accepted

KB subtree merged to `main`. Two escape-hatch divergences accepted up-front (branding, role_configurations co-location). Ready for Lovable Phase 0a (Atlas-drift cleanup + scope-boundary enforcement).
