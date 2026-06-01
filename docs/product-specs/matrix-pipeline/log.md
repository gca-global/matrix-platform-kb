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

## [2026-05-29] roadmap | roadmap.md created — outcome-based coordination surface

`roadmap.md` created and bootstrapped with outcome milestones (`O-*`) keyed to the product-spec KPI groups ([wiki/overview.md#kpis](wiki/overview.md#kpis)) + FR clusters ([wiki/requirements.md](wiki/requirements.md)); calendar quarter demoted to a secondary `target_horizon`. Promoted to a 4th durable artefact (coordination surface) in `AGENTS.md`; load-order step 1.5 + `roadmap` log action + `#coordination-through-roadmapmd` section added; `INDEX.md` / `README.md` updated. Bootstrap state: `O-CDL-CANON` `in-progress` (this cycle), `O-CONTACT-FOUNDATION` `in-progress`. Agent coordination protocol now active: every agent reads + updates `roadmap.md` before any structural change (FR / ADR / migration / EF / wiki page).

## [2026-05-29] phase-checkpoint | O-CDL-CANON landed — canonical CRM resources into CDL + write surface live

Closed the CDL canonical-RESO gap for matrix-pipeline 2.0 (ADR-016). Applied migrations `20260529160000_pipeline_canonical_new_tables.sql` (9 new canonical tables: `saved_search`, `prospecting`, `showing_availability`, `showing_request`, `showing`, `lock_or_box`, `caravan`, `caravan_stop`, `transaction_management`) and `20260529161000_pipeline_contact_listings_remodel.sql` (re-modeled `contact_listings` + `contact_listing_notes` to canonical RESO; 24,979 rows backfilled, 0 missing canonical key) to CDL `ofzcokolkeejgqfjaszq`. All 11 tables RLS-enabled — security advisor confirms none appear in `rls_disabled_in_public`, closing the prior `contact_listings`/`contact_listing_notes` gate violation. Deployed `cdl-write` (generic write dispatcher, v2 — fixed a `history_transactional` schema mismatch where the table has no `source_id` column), `cdl-contacts-read`, and `cdl-contact-listings-read` EFs (`verify_jwt=false`, in-code SSO-JWT verify), all `ACTIVE`. Smoke test: insert + update + `history_transactional` emit succeed; all three EFs return 401 on missing token. `transaction_management` carries only the 4 canonical RESO fields; deal economics stay app-private (ADR-016 escape hatch). Lovable repo `matrix-pipeline-2-0` rewired: `useContactsList` / `useContactDetail` → `cdl-contacts-read`; `useContactMutations` + `ContactStatusTransition` → `cdl-write`; `.lovable/instructions.md` + `docs/cdl-ef-contracts/saved-search.md` updated to the live `cdl-write` contract.

## [2026-05-29] roadmap | O-CDL-CANON → done

`O-CDL-CANON` transitioned `in-progress → done` in `roadmap.md` (migrations applied, EFs deployed + verified, gate violation closed). Closing reference: ADR-016 + migrations `20260529160000` / `20260529161000`. Backing KPI (platform data-foundation capability) observable: all canonical CRM resources now readable/writable through CDL with RLS + audit emission. `O-CONTACT-FOUNDATION` remains `in-progress` (phases.md Week 1).

## [2026-05-31] phase-checkpoint | canonical RESO process compliance remediation (P0–P3)

Closed the canonical-process gaps for `matrix-pipeline-2-0` (plan: `pipeline-reso-compliance-remediation`).

- **P0 (PII regression):** secured `public.v_property_contacts` — migration `20260530120000_secure_v_property_contacts.sql` (SECURITY INVOKER + revoke anon/authenticated). Extended `cdl-contact-listings-read` with `op=by-property` (service-role-side `contact_listings → contacts` join). Rewired `useContactListings` / `usePropertyContactListings` to the EF (no more anon view read).
- **P1 (engagement writes):** mandatory `ContactStatus → Prospecting` side-effects in `useSetContactStatus` (Active→On Vacation ⇒ `ActiveYN=false`; →Inactive ⇒ `ClientActivatedYN=false`; captures `ReasonActiveOrDisabled`) via `cdl-write` with parent-`Contacts`-scoped history override. SavedSearch + Prospecting UI (ContactDetail Engagement tab), enforcing one Prospecting row per `(SavedSearchKey, ContactKey)`. ContactListings engagement (send/view/preference) + append-only `contact_listing_notes`.
- **P2:** `/showings` (5-resource showing chain, gated on `Property.StandardStatus` + listing `Showing.ShowingStatus`); `/transactions` (canonical `transaction_management` + Property-scoped `HistoryTransactional` Closed / Back On Market rows; economics out of scope per transaction-lifecycle non-goals); read-only InternetTracking engagement counters on the property page (bot-excluded).
- **P3:** derived 5-stage `/pipeline` projection (NO stored stage; pure `pipelineProjection.ts` + unit tests) and `/caravans` (Caravan + CaravanStop).

New platform EFs (both `verify_jwt=false`, SSO-JWT broker scope, service-role inside; smoke-tested 401-on-missing-token): **`cdl-engagement-read`** (PII-gated `prospecting`/`saved_search` reads) and **`cdl-read`** (generic read for authenticated-only operational tables: showing chain, transactions, caravans, tracking). Writes continue through the single `cdl-write` dispatcher (extended with an optional `history` override for parent-scoped audit). KB updated: `cdl-schema.md` (read-EF section + migrations index + functions list), app `docs/cdl-ef-contracts/saved-search.md`. KB divergences noted: Caravan header-level history deferred to per-stop (Property-scoped) in v0; pipeline Contracting/Payment/Closed-Won linkage deferred (TransactionManagement carries no contact link; needs Finance/contract webhooks).

## [2026-05-31] edit | Cursor working-copy git-sync + Lovable-handoff contract documented

Added canonical guidance so Cursor agents (1) validate the local checkout is current with the GitHub remote before editing, and (2) commit + push the affected repo(s) on completion so the `github-watcher` deploys and Lovable can seamlessly take over. New H2 [`wiki/architecture.md#git-sync-handoff`](wiki/architecture.md#git-sync-handoff): pre-flight (`git fetch`; `pull --ff-only` if behind; STOP on divergence) + post-work commit/push, with a change-class → Supabase-project → repo mapping across **three repos and two Supabase projects**. Key clarification (per this revision): Cursor does not only touch CDL/foundation — it may correct/add **app-specific edge functions** and modify the **app-specific Supabase project** (`wckwfbbqiupvallmhqbu`); those land as committed migrations / EF source in `matrix-pipeline-2-0/supabase/` so Lovable sees them, while CDL changes (`ofzcokolkeejgqfjaszq`) live in `matrix-platform-foundation` and surface via this KB + `docs/cdl-ef-contracts/` (CDL not linked to Lovable, ADR-013). `INDEX.md` anchor + `AGENTS.md` working-copy/handoff cross-ref added. Mirrored into `matrix-pipeline-2-0/.lovable/instructions.md` (Lovable-facing) and enforced by the auto-applied rule `/.cursor/rules/cursor-git-handoff.mdc`.

## [2026-05-31] edit | Listing-side TransactionType ownership moved Pipeline → Atlas

Split `TransactionManagement.TransactionType` authoring by surface: **Pipeline (`matrix-pipeline-2-0`) keeps offer-side only** (`PurchaseOffer` / `LeaseOffer` / `Other`) — removed `Listing for Sale` / `Listing for Lease` from `TRANSACTION_TYPES` in `src/hooks/useTransactions.ts` and tweaked `src/pages/Transactions.tsx` copy. **Atlas (`matrix-atlas-mls`) now authors the listing-side** (`Listing for Sale` / `Listing for Lease`) via a new *Listing Transactions* surface: `src/hooks/useListingTransactions.ts` (`cdl-read`/`cdl-write` on `transaction_management`, client-side filtered to the two listing types, `emitHistory:false`), `src/pages/ListingTransactions.tsx` (port of pipeline `Transactions.tsx`, no close-edge dialog), `/listing-transactions` route in `App.tsx` (`ProtectedRoute requiredPage`), `AppSidebar` item + `RoleConfigPanel` `PAGE_GROUPS` key `listing-transactions`. Both apps write the **same CDL `transaction_management` table** (`ofzcokolkeejgqfjaszq`) via `cdl-write` — no per-app partition, only an authoring-surface convention. **0 listing-type rows existed in CDL**, so no data migration. KB updated in the same change: [`wiki/entities.md#transaction-management`](wiki/entities.md#transaction-management) (ownership-split note) and [`cdl-crud-contract.md`](cdl-crud-contract.md) (TransactionManagement CRUD row authoring split). The Property close-edge (`useRecordPropertyClose`/`useRecordBackOnMarket`, Property-scoped `HistoryTransactional`) stays in Pipeline — it is not a listing `TransactionType` — flagged as a possible later move.

## [2026-06-01] fix | CDL broker-scope read EFs accept self/team/global (SSO_READ_SCOPES)

After the SSO speedup patch, Pipeline CDL reads started failing for non-admin sessions. Root-caused (not a token-verification regression — current ES256 tokens verify fine against the JWKS): the four broker-scope read EFs (`cdl-contacts-read`, `cdl-contact-listings-read`, `cdl-engagement-read`, `cdl-read`) were reading the **shared, project-wide** `SSO_ALLOWED_SCOPES` (set to `system_admin,org_admin` to lock the admin EFs), so any Broker (`self`) session got `403 forbidden: scope 'self' not in [system_admin,org_admin]`. It only worked while the tester was in `system_admin` scope. Fix: each of the four read EFs now reads its **own** `SSO_READ_SCOPES` (default `self,team,global,org_admin,system_admin`), decoupled from `SSO_ALLOWED_SCOPES` (admin EFs unchanged). Deployed all four `ACTIVE` (`verify_jwt=false`); no `SSO_READ_SCOPES` secret set (broad code default). Verified with a minted `self`-scope token: `cdl-read`/`cdl-contact-listings-read`/`cdl-engagement-read` → 200; `cdl-contacts-read` passes the gate (no longer 403) but an **unfiltered** full-table list can hit a statement timeout — the Pipeline client uses pagination/filters. **Owner-clamp deferred (accepted residual risk):** no SSO-user → `member_key` mapping exists (CDL `members` keyed on legacy Cyprus emails; SSO logins are Azure AD staff; no `member_key` claim), so PII reads are currently org-wide for any allowed scope. Follow-up: build the identity mapping, then enforce per-`owner_member_key` clamp. KB updated same change: [`../../data-models/cdl-schema.md`](../../data-models/cdl-schema.md) (Edge-functions + Auth sections). No SSO or `matrix-pipeline-2-0` client change.
