---
title: matrix-pipeline — 8-week atomic build plan
status: stable
source: plan .cursor/plans/llm_wiki_and_phased_build_plan_7ebe41be.plan.md
last_updated: 2026-06-08
tags: [phases]
---

# `matrix-pipeline` — 8-week atomic build plan

> Eight weeks from kickoff to a staging prototype with business power users. Two swimlanes: **Lovable** (app UI + CRM app DB) and **Cursor** (CDL + SSO + wiki + Edge Functions on the platform side). Every task is atomic — about one hour of focused work — and cites the wiki anchor that backs the requirement. Implementation MUST stay grounded in the wiki; any deviation requires the [wiki/architecture.md#escape-hatch](wiki/architecture.md#escape-hatch) justification block. Cite all consulted wiki anchors in the PR description.

> **Platform pre-work landed 2026-05-29 (ADR-016 / outcome O-CDL-CANON).** The Cursor-swimlane CDL write surface is **already deployed** ahead of Week 1: the 9 canonical CRM tables exist in CDL, `contact_listings`/`contact_listing_notes` are re-modeled + RLS-enabled, and three EFs are live — `cdl-write` (generic insert/update/upsert/soft-delete + `HistoryTransactional` emit), `cdl-contacts-read`, `cdl-contact-listings-read`. Where a week task below says "build `cdl-contacts-write` EF", read it as **"wire the UI to `cdl-write` with `resource: 'contacts'`"** — the EF already exists. The per-resource write EFs (`cdl-*-write`) are superseded by the single `cdl-write` dispatcher. See [cdl-crud-contract.md](cdl-crud-contract.md) Recipe WRITE-B.

## Build status snapshot {#status}

> Reflects the deployed `matrix-pipeline-2-0` app codebase as of **2026-06-05** (Week-3 write-surface hardening + caravan timestamp fix, app `3582228`), plus **platform-side (Cursor) progress through 2026-06-08** — the Week-4 CDL surface (Referrals/Documents + the transaction-phase `cdl-listing-lifecycle` path, ADR-025/ADR-026) is deployed; the matching app UI is the pending Lovable lane. Tags: **DONE** / **MOSTLY DONE** / **PARTIAL** / **BUILT-NOT-WIRED** / **NOT STARTED**. The per-week sections below carry the same status callout.

- **Week 0 — Foundation**: **DONE**. i18n shipped ahead of plan (DB-driven, [ADR-020](../../architecture/decisions/ADR-020.md) / [ADR-021](../../architecture/decisions/ADR-021.md)). Surfaces beyond this plan are also live: Properties browse + read-only Property detail, AD Employees, Curated Lists (public share links), Settings/admin, Profile.
- **Week 1 — Contacts**: **DONE** (2026-06-03). *Lovable lane:* Activities (`activities` app-DB table, Pattern B RLS + `useActivities` + `ActivitiesCard`), the bulk CSV import wizard (commit landed 2026-06-04, see Week 2), and duplicate detection on create; earlier surfaces (list/create/detail, graduation, status, reassign, privacy) remain live. *Cursor lane:* `cdl-write`/`cdl-contacts-read` live, `contacts` RLS Pattern B confirmed, `#live-cdl-state` refreshed, the `sso-member-roster-lint` EF + daily cron shipped (risk R3), and the `Member`+`Office` materialization stretch landed.
- **Week 2 — SavedSearch + Prospecting**: **DONE — full FR-PROS parity** (2026-06-04). *Lovable lane:* `ContactSavedSearches` (fuller create modal — `PropertySubType`, budget mid-point, extended `ScheduleType` set `ASAP/Daily/Weekly/Monthly/OnNewMatch/Custom`, structured criteria persisted to `saved_search.raw.criteria`) + `ContactListingsPanel` on the Engagement tab; `/saved-searches` page with FR-PROS-13 due/upcoming cards **and** a "Needs attention" stale section (FR-PROS-07 client-side + FR-PROS-12 broker-side); dashboard reminders now read open prospecting-linked **Activities** materialized from engine events (`useProspectingActivitySync`); the Matching (b) soft-prompt can create a broker Task; CSV import **commit** + optional SavedSearch+Prospecting per contact (FR-PROS-12); Pipeline Matching signal wired (see Week 5); `role_configurations` backfill. *Cursor lane:* the **delivery/matching engine** `public.cdl_prospecting_run()` (FR-PROS-03) + hourly `pg_cron` — matches `public.properties` against `saved_search.raw.criteria`, inserts `contact_listings`, advances `last_new_changed_timestamp` + `next_send_timestamp` per `ScheduleType`, emits `'Prospecting send'` / `'Prospecting reminder due'` (supersedes the reminder-only `cdl_prospecting_tick()`); `cdl-engagement-read` gains `prospecting-stale` + `prospecting-due-events` ops; verified end-to-end via MCP. Only the **email channel** (stretch) is deferred — no platform mailer yet (same as `sso-member-roster-lint`).
- **Week 3 — ContactListings + Showings + Caravan**: **DONE — full FR parity**. Backend: the dedicated `cdl-showing-*`/`cdl-caravan-*` EFs were **superseded by the ADR-016 `cdl-read`/`cdl-write` dispatchers** (done-by-design); `lock_or_box` added to the `cdl-read` whitelist (`cdl-read` v3, 2026-06-05) for the showing-access reference. App (Lovable 10-prompt set, all run): fixed the `ContactListings` read bug (EF hook over `cdl-contact-listings-read`), role-config seed (`showings`+`caravans`), Showings Upcoming/Recent + buyer `contact_key` linkage, `ShowingAvailability` slot picker, `LockOrBox` reference card, post-showing feedback→`Activity`, Caravan create wizard + run view (emits one `showing` per stop), `/properties` send-listings wizard, and the shared cross-side `EngagementTimeline` (sent→viewed→showing→offer) on both `/contacts/:id` and `/properties/:id`. Typecheck clean; Cursor reconciled the `lock_or_box` field mapping to the canonical CDL columns.
- **Week 4 — Transactions + Referral + Documents**: **RE-SCOPED + PARTIAL** (2026-06-08). Referrals + Documents platform side **DONE** (`public.referral`/`public.document` CDL resources + `cdl-read`/`cdl-write` v7 + ADR-025). **Transaction phase un-deferred + platform side DONE (ADR-026):** Pipeline owns the `Property` *transaction phase* via the governed **`cdl-listing-lifecycle`** EF (`acceptOffer`/`closeDeal`/`cancelDeal`) + canonical `Property` close economics (migration `20260608150000`) + buyer via `ContactListings` + `HistoryTransactional` timeline (`cdl-read` v8). Only in-flight offer *negotiation* economics (amount/currency/counter lifecycle) stay deferred. App UI (`/referrals`, Documents tab, and the reworked `/transactions` accept/close/cancel + timeline) **PENDING** (Lovable).
- **Week 5 — Pipeline + Commission**: **PARTIAL**. Pipeline v0 board live (per-contact); the Matching signal is now **wired** (`usePipeline` consumes `useAllProspecting` → `prospectingActive`). Still per-Contact (not per `(Contact × SavedSearch)`); Commission Engine, forecast/variance dashboards, and `/reports` not built.
- **Week 6 — AI Copilot**: **NOT STARTED**.
- **Week 7 — Staging hardening**: **NOT STARTED**.

> **Canonical-compliance audit (2026-06-05).** A RESO DD 2.0 compliance audit of `matrix-pipeline-2-0` + `matrix-atlas-mls` + the CDL surface — verdict, findings ledger, RESO-divergence register, and corpus-verified corrections — lives at [canonical-compliance-audit-2026-06.md](canonical-compliance-audit-2026-06.md). Remediation tracked there (P0–P5).

**Immediate next** — Weeks 1-3 are closed. **Week 4 platform side is now fully DONE (Cursor):** Referrals + Documents (`referral`/`document` CDL resources + `cdl-read`/`cdl-write` v7, ADR-025) **and** the transaction phase (ADR-026) — Pipeline owns the `Property` transaction phase via the governed `cdl-listing-lifecycle` EF (`acceptOffer`/`closeDeal`/`cancelDeal`) + canonical `Property` close economics (migration `20260608150000`) + buyer via `ContactListings` + `HistoryTransactional` timeline (`cdl-read` v8). The **remaining Week-4 work is all Lovable app UI**: (1) `/referrals` page + create + history, referral surfacing with manual outcome, Documents tab on `ContactDetail`, Referrals nav + `'referrals'` page-key seed; (2) rework `/transactions` (`useTransactions.ts` + `Transactions.tsx`) to the event-sourced model — capture buyer (`ContactListings`) + property, call `cdl-listing-lifecycle` for accept/close/cancel, render the `HistoryTransactional` timeline (Lovable prompt drafted). **Still deferred (ADR-025):** in-flight offer *negotiation* economics, FR-REF-08 auto close-the-loop, forecast P&L. The only deferred Week-2 item is the Prospecting **email channel** (stretch) — blocked on a platform mailer, tracked alongside the same gap in `sso-member-roster-lint`.

## TOC

- [#governance](#governance) — atomicity rule, DoD, swimlanes, KB-first, budget
- [#mvp-scope](#mvp-scope) — what "everything" means for the staging prototype
- [#risk-register](#risk-register) — top 5 risks + mitigations
- [#week-0](#week-0) — Foundation
- [#week-1](#week-1) — Contacts & Org Roster
- [#week-2](#week-2) — SavedSearch + Prospecting
- [#week-3](#week-3) — ContactListings + Showings + Caravan
- [#week-4](#week-4) — TransactionManagement + Offer-to-Closing + Referral
- [#week-5](#week-5) — Pipeline projection + Commission Engine
- [#week-6](#week-6) — AI Copilot
- [#week-7](#week-7) — Staging hardening + Demo

## Governance — how to read and execute this plan {#governance}

### Atomicity rule

Every task is ≈ **1 hour of focused work** by a single contributor (Lovable agent or Cursor agent). A task that grows past two hours is **split** into smaller tasks in the same H3 swimlane before it is started.

### Definition of Done (DoD) — applies to every task

A task is "done" only when **all** of the following are true:

1. **UI behavior** (Lovable tasks): observable in the Lovable preview deploy; one Playwright happy-path test asserts it (added in Week 7 if not earlier).
2. **EF endpoint** (Cursor tasks): deployed to the relevant Supabase project (`verify_jwt: false`, ES256 verification, scope check), reachable from the CRM app.
3. **RLS / scope check**: a non-authorized SSO JWT returns 403; an authorized one with insufficient scope returns 403; only the correct scope returns 200. For CDL tables with RLS disabled (`contact_listings`, `contact_listing_notes`), the EF is the **only** access gate — see [wiki/architecture.md#cdl-access-pattern](wiki/architecture.md#cdl-access-pattern).
4. **`HistoryTransactional` emission**: any state transition relevant to a canonical RESO process emits a `HistoryTransactional` row with the canonical `MajorChangeType` / `ChangeType` codes. See [wiki/integration.md#history-emission](wiki/integration.md#history-emission).
5. **Wiki cross-ref refreshed**: if the task introduces a new FR or alters an existing one, the relevant `wiki/*.md` is updated in the same PR and the `last_updated` frontmatter is bumped.
6. **`log.md` entry**: the action that closes the task (or the weekly checkpoint) is appended.

### Swimlane ownership

| Swimlane | Owns | Touches |
|---|---|---|
| **Lovable** | The CRM app (`matrix-pipeline`) — UI, routes, hooks, components, queries, CRM app DB schema + RLS, app-private tables (`activities`, `documents`, `campaigns`, `referrals`, `transaction_management`, `saved_search`, `prospecting`, Commission Engine tables). | CDL only as a **client** (via `cdlClient` + dedicated CDL EFs). Never the CDL schema. Never SSO schema. |
| **Cursor** | Platform side — CDL schema + EFs on the CDL project, SSO permission keys + roles + groups, this LLM Wiki, KB drift fixes, ADRs. | The CRM app only via the wiki + (rarely) a coordinated PR if a CRM-private contract must move to CDL. |

### KB-first principle

Before starting any task: load [`INDEX.md`](INDEX.md) → the relevant wiki page → the H2 anchor. **Never** load `raw/context-v2.md` unless the task is "investigate provenance of claim X". Cite the wiki anchor(s) in the PR description.

### Weekly cadence

- **Monday** — 30-min planning sync; both swimlanes confirm the week's task list, surface blockers from the prior week.
- **Mon–Thu** — execute atomic tasks; each task closes with a small PR / Lovable preview push.
- **Friday morning** — integrate, run `scripts/wiki-lint.sh`, run Playwright smoke.
- **Friday afternoon** — demo to the business power user(s); collect feedback; append `## [<date>] phase-checkpoint | Week N` to [`log.md`](log.md). Stretch goals that did not land roll to Week 7 backlog (never to the next week's core).

### Budget recap

- 8 weeks × 5 d × 8 h ≈ **320 h** total.
- ~70 % Lovable / ~30 % Cursor → ~28 h Lovable + ~12 h Cursor per week.
- Each H3 swimlane below targets that budget; numbers in parentheses next to tasks (~1 h, ~2 h…) sum to roughly the budgeted weekly hours.

## MVP scope — what "everything" means for the staging prototype {#mvp-scope}

The 2-month staging prototype covers the **full BRD**:

- All 24 Business Requirements ([wiki/requirements.md#br](wiki/requirements.md#br)).
- All 15 functional clusters in [wiki/requirements.md](wiki/requirements.md) (`FR-CON`, `FR-PC`, `FR-COM`, `FR-CFL`, `FR-FNL`, `FR-PROS`, `FR-ACT`, `FR-SHOW`, `FR-CARA`, `FR-CL`, `FR-TM`, `FR-CMM`, `FR-DOC`, `FR-REF`, `FR-REP`).
- All 14 AI Copilot features in [wiki/ai.md](wiki/ai.md) (with the 4-feature floor in [#risk-register](#risk-register) if Week 6 slips).
- The Commission Engine ERP-lite ([wiki/commission-engine.md](wiki/commission-engine.md)) including forecast precedence rule [FR-FNL-12](wiki/requirements.md#fr-fnl-funnel-canonical) (a)/(b) and variance display [FR-TM-13](wiki/requirements.md#fr-tm-transactions).
- All six business processes ([wiki/processes.md](wiki/processes.md)) end-to-end.
- All seven external integrations ([wiki/integration.md](wiki/integration.md)) — Listing Module, Contract system, Finance ERP commission + payments, SSO, CDL, with `HistoryTransactional` emission across the board.

"Staging prototype" means: deployed to a Lovable staging URL behind SSO, with role seeded power users, on Matrix HRMS-sandbox-class Supabase projects (CRM app DB + the production SSO + CDL projects). No production traffic; no real money flows in Finance ERP.

## Risk register {#risk-register}

| ID | Risk | Mitigation | Trigger |
|---|---|---|---|
| R1 | **AI scope creep in Week 6** swallows the calendar | 4-feature **AI floor**: `FR-AI-LQ` + `FR-AI-MAT` + `FR-AI-SHOW` + `FR-AI-MAR`. The other ten features ship as stubs (UI shell + "coming soon" placeholder) and graduate during Week 7 if budget allows. | End of Week 6: if fewer than 4 AI features end-to-end → cut all stretch AI tasks. |
| R2 | **CDL RLS disabled** on `contact_listings`, `contact_listing_notes`, and most CDL tables exposes engagement data to anon | Every CRM read/write goes through a CDL EF with SSO JWT scope check (Cursor task each week). Pattern B RLS rollout is a Week 7 Cursor batch. See [wiki/architecture.md#compliance-gates](wiki/architecture.md#compliance-gates). | Production sign-off blocked until Pattern B is on the four named tables. |
| R3 | **Identity boundary drift** (SSO user ↔ CDL `Member` roster) | Week 0 Cursor task verifies `Member.MemberAlternateId = SSO user_id` for every active broker; Week 1 adds a daily lint EF (`sso-member-roster-lint`) that emails diffs. See [wiki/architecture.md#identity-boundary](wiki/architecture.md#identity-boundary). | Any mismatch surfaced by lint → block adjacent Lovable work until resolved. |
| R4 | **Stale CDL KB drift** (e.g. `cdl-schema.md` missing `public.contact_listings`, `public.showings` naming) | `wiki/architecture.md#live-cdl-state` is refreshed via MCP at the **start of every week** by a Cursor task; KB drift items handed to platform team end of Week 7. | A wiki claim contradicted by MCP → emergency `divergence` log entry. |
| R5 | **"Full BRD in 8 weeks" is tight** | Every week has a **core** task list (must ship) and a **stretch** list (ships if core wraps Thursday). Stretch slips to Week 7 backlog, never to the next week's core. The 14-feature AI catalog already uses this pattern. | End-of-week demo not passing the BR-* parity check → next Monday triage. |

## Week 0 — Foundation {#week-0}

> **Status (2026-06-03): DONE.** Auth + three Supabase clients + SidebarLayout under ProtectedRoute all shipped; i18n delivered ahead of plan (runtime DB-driven, ADR-020/021). Bonus surfaces now live beyond this plan: Properties browse + read-only Property detail, AD Employees, Curated Lists, Settings, Profile.

**Goal**: Lovable-deployed app shell that compiles, authenticates against SSO, talks to all three Supabase projects, renders `SidebarLayout` under `ProtectedRoute`. LLM Wiki published on `matrix-platform-kb` (this PR) so every subsequent task can cite an anchor.

Demo: log in as a power-user, see an empty SidebarLayout with the seven main routes (`/contacts`, `/saved-searches`, `/showings`, `/caravans`, `/transactions`, `/referrals`, `/reports`), all rendering "coming soon" placeholders.

### Lovable {#week-0-lovable}

- (~1 h) Scaffold from `matrix-apps-template-2-1` (the canonical starter kit; the old `matrix-apps-template` is obsolete); set `CLIENT_ID`, `BASE_PATH`, project name in `src/lib/matrix-sso.ts`. Cite [wiki/architecture.md#three-supabase](wiki/architecture.md#three-supabase). DoD: `npm run dev` boots in Lovable.
- (~1 h) Wire `ssoClient` + `cdlClient` + `appClient` in `src/lib/dataLayerClient.ts`. Three Supabase project IDs from [wiki/architecture.md#three-supabase](wiki/architecture.md#three-supabase). DoD: console.log of each client returns a non-null instance.
- (~1 h) Implement `ProtectedRoute` + OAuth 2.0 + PKCE callback. Cite [wiki/architecture.md#identity-boundary](wiki/architecture.md#identity-boundary). DoD: a logged-out user is redirected to SSO; a logged-in one lands on `/`.
- (~1 h) Implement `SidebarLayout` with seven empty routes; role-based section visibility wired but no permission keys yet. Cite [wiki/overview.md#personas](wiki/overview.md#personas).
- (~1 h) Add i18n scaffold (EN + RU) — load EN strings only for now. Cite the platform `app-template.md`. **Delivered 2026-06-02 at full scope**: EN + RU + **HU**, then **upgraded the same day to runtime DB-driven i18n** ([ADR-021](../../architecture/decisions/ADR-021.md)) — the app now bundles only a single English baseline and serves every other locale + per-tenant relabel from the CDL `app_ui_strings` corpus via the `app-i18n` EF (chained i18next backend). The tenant-admin Settings → "Translations & Labels" tab manages both scopes (RESO "Terminology" via [ADR-020](../../architecture/decisions/ADR-020.md) + generic "Interface text" via ADR-021) with full pagination and an add-locale picker; adding a language is data-only. Baked into `matrix-apps-template-2-1` as the platform standard. See [docs/data-models/reso-dd-descriptions.md](../../data-models/reso-dd-descriptions.md).
- (~1 h) Wire Tailwind + shadcn/ui Navy palette + Playfair Display / Inter. DoD: a placeholder page passes the Sharp visual sanity check.
- (~2 h) Implement `useUserDisplay` hook that calls SSO `resolve-users` EF for any `MemberKey` the UI renders. Cite [wiki/architecture.md#identity-boundary](wiki/architecture.md#identity-boundary).
- (~1 h) Seed CRM app DB: empty migrations folder + `001_init.sql` with `pg_*` extensions + `audit.events` table. Will be filled per-week.
- (~1 h) Push first Lovable preview deploy; share URL with Cursor for the SSO `redirect_uri` registration.
- (~1 h) Add `README.md` + `AGENTS.md` to the app repo pointing back at this wiki. DoD: a fresh contributor opens the repo and is told "read `/home/bitnami/matrix-platform-kb/docs/product-specs/matrix-pipeline/INDEX.md` first".
- (Stretch ~2 h) Add a `/dev/diagnostics` page that pings each Supabase client + the SSO `verify-jwt` EF + shows the resolved scope.

### Cursor {#week-0-cursor}

- (~1 h) Register `matrix-pipeline` in SSO Console: client_id, redirect_uri pointing at the Lovable preview URL, scopes. DoD: PKCE auth succeeds from Lovable preview.
- (~1 h) Define permission keys for every sidebar page: `pipeline:contacts:read|write`, `pipeline:saved-searches:read|write`, … Cite [wiki/overview.md#personas](wiki/overview.md#personas).
- (~1 h) Refresh `wiki/architecture.md#live-cdl-state` via MCP — confirm Phase 1 table list, row counts, RLS flags. Bump `last_updated`. (Weekly recurring Cursor task; this is the first run.)
- (~2 h) **Publish this LLM Wiki PR** — the wiki itself, `phases.md`, `scripts/wiki-lint.sh`. DoD: PR review passes, branch `matrix-pipeline-wiki` merged into `main`.
- (~1 h) Add an entry in `matrix-platform-kb/docs/index.md` (chapter row) + a row in `matrix-platform-kb/AGENTS.md` (Subsystem AGENTS.md table) pointing here.
- (~1 h) Verify SSO `Member.MemberAlternateId = sso.user_id` mapping for every active power user — manual MCP query. File mismatches into a Week 1 Cursor task.
- (~1 h) Schedule the daily MCP refresh of `wiki/architecture.md#live-cdl-state` (cron in the Cursor agent skill or simple Friday note).
- (Stretch ~2 h) Draft ADR placeholders: `ADR-XXX-crm-referral-entity.md`, `ADR-XXX-crm-commission-engine.md` — section stubs only, full bodies in Week 7.

## Week 1 — Contacts & Org Roster {#week-1}

> **Status (2026-06-03): DONE.** All Week 1 tasks shipped. Final pass added: the `activities` app-DB table (Pattern B RLS, migration `20260603115750…`) + `useActivities` + `ActivitiesCard` (open activities, complete, and a "next action" nudge) on the contact detail; the bulk CSV import wizard (`ImportWizard` — upload → map → preview, with commit deferred to Week 2 per FR-PROS-12); and duplicate detection on create (`useContactDuplicateCheck` + `DuplicateConfirmDialog`). Earlier surfaces (list/create/detail, ContactType graduation, status transition, owner reassign, privacy banner) remain live. The Engagement-tab placeholder is addressed next in Weeks 2-3.

**Goal**: a power user can create, edit, and search `Contacts`; Personal / Commercial split honored; ContactType graduation works (Lead → Buyer/Seller/Both); broker reminders surface; `HistoryTransactional` rows emitted for every transition.

Demo: create a Lead, qualify them into a Buyer, edit their personal/commercial fields, see the history log.

### Lovable {#week-1-lovable}

- (~1 h) CRM app DB: views `v_contacts_with_owner`, `v_recent_history` joining CDL `contacts` + `history_transactional` with SSO display names via `useUserDisplay`.
- (~2 h) `/contacts` list page: search by name/email/phone/`OwnerMemberKey`, filter by `ContactType`, status pill, sort by `ModificationTimestamp`. Cites [wiki/requirements.md#fr-con-contacts](wiki/requirements.md#fr-con-contacts) (FR-CON-01..04).
- (~2 h) `/contacts/new` form: required fields per [FR-CON-05..09](wiki/requirements.md#fr-con-contacts); `LeadSource` picker (Referral, Campaign, Website, Inbound, Cold, …). Call `cdl-contacts-write` EF.
- (~2 h) `/contacts/:id` detail page: tabs (Overview, Personal, Commercial, Engagement, History). Personal/Commercial split per [FR-PC](wiki/requirements.md#fr-pc-split) + [FR-COM](wiki/requirements.md#fr-pc-split). Privacy levels visible per role.
- (~1 h) ContactType graduation control on the detail page: Lead → Buyer / Seller / Both; emits `HistoryTransactional`. Cite [wiki/requirements.md#fr-cfl-contact-funnel-lifecycle](wiki/requirements.md#fr-cfl-contact-funnel-lifecycle) (FR-CFL-01..05).
- (~1 h) Activity sidebar on `/contacts/:id`: list of open `activities` (CRM-app-DB-stored); inline "next action" prompt if none open. Cite [wiki/requirements.md#fr-act-activities](wiki/requirements.md#fr-act-activities) (FR-ACT-01).
- (~2 h) CRM app DB: `activities` table + RLS by `assigned_to = sso.user_id OR scope >= team`. Cite [wiki/architecture.md#app-private-state](wiki/architecture.md#app-private-state).
- (~1 h) Owner / re-assign control: edits `OwnerMemberKey` via `cdl-contacts-write`; emits `HistoryTransactional`.
- (~1 h) Bulk import wizard stub: CSV upload → preview → no commit yet (commit lands Week 2).
- (~1 h) Privacy banner / consent flag UI per [FR-CON-15..20](wiki/requirements.md#fr-con-contacts).
- (Stretch ~2 h) Duplicate detection (fuzzy name + phone + email) on `/contacts/new` submit.

### Cursor {#week-1-cursor}

> **Status (2026-06-03): DONE (incl. stretch).** `cdl-write` (covers `cdl-contacts-write`) + `cdl-contacts-read` live; `contacts` RLS Pattern B confirmed; `#live-cdl-state` refreshed via MCP (verified 2026-06-03); `FR-CON` audit clean. The `sso-member-roster-lint` EF shipped + scheduled (see below). The stretch `Member`+`Office` view materialization also landed (`v_members_list` / `v_offices_list`, see below).

- (~2 h) **CDL EF `cdl-contacts-write`** on the CDL project, `verify_jwt: false`, ES256 verification, scope checks (`pipeline:contacts:write` for write; `pipeline:contacts:read` for read paths). Upserts `public.contacts`. Emits `HistoryTransactional`. Cite [wiki/integration.md#cdl](wiki/integration.md#cdl) + [wiki/integration.md#history-emission](wiki/integration.md#history-emission).
- (~1 h) **CDL EF `cdl-contacts-read`**: cursor pagination (per `performance.md`), HTTP cache headers, estimated counts.
- (~1 h) Live-state refresh of `wiki/architecture.md#live-cdl-state` via MCP (recurring weekly). **✅ Done 2026-06-03** (verified date bumped; deltas: `contacts` +35 → 45 108, `history_transactional` 0 → 5, `transaction_management` 0 → 1).
- (~1 h) Confirm `public.contacts` RLS Pattern B is on (it is) and verify scope mapping via test JWT.
- (~1 h) `sso-member-roster-lint` EF (daily): diff `Member` ↔ SSO users; email Cursor + Lovable leads on mismatch. **✅ Shipped 2026-06-03** — EF on SSO (`verify_jwt:false`) + `pg_cron` `sso-member-roster-lint-daily` (06:15 UTC) + `public.sso_member_roster_lint_runs` report table. **Diffs by email, not `MemberAlternateId`** (that column doesn't exist in CDL `members` — see [wiki/architecture.md#identity-boundary](wiki/architecture.md#identity-boundary) drift note). First run: 36/107 active members matched an SSO login by email; 71 active legacy members + 36 SSO users unmapped. Email is **opt-in** (no platform mailer yet → `email_status: skipped_no_provider`); wiring a provider is the only residual sub-task. See [`../../platform/sso-edge-functions.md`](../../platform/sso-edge-functions.md).
- (~1 h) Add `FR-CON-*` cross-refs to the wiki if any new FR was introduced during Lovable work — none expected, but the audit is mandatory.
- (Stretch ~2 h) `Member` + `Office` view materialization for high-load list pages, per `performance.md`. **✅ Done 2026-06-03** — CDL migration `20260603140000_member_office_list_views.sql` adds denormalized `security_invoker` views `v_members_list` (office name/city/country pre-joined onto members) + `v_offices_list` (+ `agent_count`). **Regular** views, not matviews (129/59 rows make refresh-staleness pure cost — `performance.md` exit-ramp guidance). Pipeline `useMembers`/`useOffices` repointed with explicit projections (no `select *`); `MemberPicker` shows office without a second offices fetch + client join. Also fixed KB drift: `v_dash_members`/`v_dash_offices` marked DROPPED and `members`/`offices` documented as having no `is_deleted`. See [cdl-schema.md](../../data-models/cdl-schema.md) "Member / office list views".

## Week 2 — SavedSearch + Prospecting {#week-2}

> **Status (2026-06-04): DONE — full FR-PROS parity (email stretch deferred).** Upgraded from the reminder-only v0 to the full delivery loop. *Lovable:* fuller `ContactSavedSearches` create modal (`PropertySubType`, budget mid-point, extended `ScheduleType`, structured criteria → `saved_search.raw.criteria`); `/saved-searches` due/upcoming cards **+ "Needs attention"** stale section (FR-PROS-07 + FR-PROS-12); dashboard reminders read open prospecting-linked **Activities** (`useProspectingActivitySync` materializes them from engine events via `cdl-engagement-read` `prospecting-due-events`; the `activities` link columns `related_resource`/`related_key` are **live in the app DB** via Lovable's migration `20260604164542`, so materialization is active — not deferred. The `result` disposition column for FR-PROS-13 analytics was not adopted by Lovable's schema and is deferred); Matching (b) soft-prompt can spawn a broker Task; CSV import commit **+ optional SavedSearch+Prospecting** per contact (FR-PROS-12); Pipeline Matching signal wired (see Week 5); `role_configurations` backfill. *Cursor:* the **delivery/matching engine** `public.cdl_prospecting_run()` (migration `20260604120000_cdl_prospecting_run.sql`) replaces `cdl_prospecting_tick()` — matches `public.properties` against `saved_search.raw.criteria`, inserts `contact_listings`, advances `last_new_changed_timestamp` + `next_send_timestamp` per `ScheduleType`, emits `'Prospecting send'`/`'Prospecting reminder due'`; `cdl-engagement-read` gains `prospecting-stale` + `prospecting-due-events`. **Dual reminders** (CDL history audit + app-DB Activity) per the Week-2 decision. **Note — `saved_search`/`prospecting`/`contact_listings` live in CDL, not the CRM app DB** (the per-week Lovable tasks below say "CRM app DB" — the actual surface is the CDL `cdl-engagement-read`/`cdl-write` EFs; recorded divergence, see the 2026-05-30 remediation in [log.md](log.md)). **Deferred:** the Prospecting **email channel** (stretch) — no platform mailer yet.

**Goal**: a broker can attach 1..N `SavedSearch` rows to a `Contact`, enable `Prospecting`, and the system actually pings the broker (CRM app reminder + email) for outreach. The pipeline auto-derives "Matching" from `SavedSearch + ContactListings`, including the (b) branch — manual sends without `Prospecting`.

Demo: broker creates a Buyer SavedSearch with criteria + budget, enables Prospecting, gets a reminder; manually sends two listings via WhatsApp; sees the soft prompt to create `Prospecting`.

### Lovable {#week-2-lovable}

- (~1 h) CRM app DB: `saved_search` + `prospecting` tables (CRM app DB until Phase 2+ CDL migration — see [wiki/architecture.md#phase-2-migration](wiki/architecture.md#phase-2-migration)). RLS Pattern B.
- (~2 h) `/contacts/:id/saved-searches` tab: list + create modal with all criteria fields per [FR-PROS-01..05](wiki/requirements.md#fr-pros-prospecting). Budget mid-point derived auto.
- (~2 h) `/contacts/:id/saved-searches/:sid` detail: edit, archive, see Prospecting state.
- (~1 h) Prospecting toggle: `ActiveYN`, frequency (daily/weekly), next run timestamp. Per [FR-PROS-06..09](wiki/requirements.md#fr-pros-prospecting).
- (~1 h) Broker reminder cards on the `/` dashboard: "Time to contact X about SavedSearch Y" — driven by `Prospecting.NextRun` ≤ now. Per [FR-PROS-13](wiki/requirements.md#fr-pros-prospecting).
- (~2 h) `/saved-searches` global page (broker-scoped): all open SS + Prospecting state across all my contacts.
- (~1 h) Bulk CSV import commit endpoint: now writes contacts + initial SavedSearch from CSV. Cite [FR-PROS-12](wiki/requirements.md#fr-pros-prospecting).
- (~1 h) Pipeline-derivation engine v0 (CRM app side): for each `(Contacts × SavedSearch)`, compute the canonical 5-stage projection (Qualification / Matching / Showing / Contracting / Closed). Cite [wiki/overview.md#pipeline](wiki/overview.md#pipeline) + [wiki/requirements.md#fr-fnl-funnel-canonical](wiki/requirements.md#fr-fnl-funnel-canonical) (FR-FNL-01..06).
- (~1 h) **Matching (b) soft-prompt**: if `ContactListings.ListingSentTimestamp` exists for a `(Contacts × SavedSearch)` pair WITHOUT active `Prospecting`, surface a non-blocking suggestion "Activate Prospecting?". Cites [FR-PROS-09](wiki/requirements.md#fr-pros-prospecting) + the bug-fix branch in [wiki/processes.md#contact-funnel](wiki/processes.md#contact-funnel).
- (Stretch ~2 h) Email channel for the Prospecting reminder (vs in-app only).

### Cursor {#week-2-cursor}

> **Status (2026-06-04): DONE — full delivery engine.** The reminder-only `cdl_prospecting_tick()` was upgraded to the **delivery/matching engine** `public.cdl_prospecting_run()` (FR-PROS-03, migration `20260604120000_cdl_prospecting_run.sql`): per due subscription it matches `public.properties` against `saved_search.raw.criteria`, inserts `contact_listings` for new matches, advances `last_new_changed_timestamp` + `next_send_timestamp` per `ScheduleType`, and emits `'Prospecting send'`/`'Prospecting reminder due'` history; the old function is dropped and the cron repointed to `cdl-prospecting-run-hourly`. `cdl-engagement-read` gained `prospecting-stale` (FR-PROS-07) + `prospecting-due-events` (drives app Activities). `contact_listings` write/read via `cdl-write` + `cdl-contact-listings-read` (ADR-016). End-to-end MCP smoke test passed (seed → cron run → 1 `contact_listings` + `'Prospecting send'` + cadence advance; re-run → dedup + `'Prospecting reminder due'`; cleaned up). Email channel (stretch) deferred — no platform mailer (same as `sso-member-roster-lint`).

- (~2 h) **CDL EF `cdl-prospecting-trigger`** (scheduled): every hour, scan `prospecting` rows where `next_send_timestamp ≤ now`, emit a reminder event. DoD: a single broker with active SS gets reminders. **✅ Done 2026-06-04** — shipped as **`public.cdl_prospecting_tick()` SQL function + `pg_cron` job `cdl-prospecting-tick-hourly`** (`0 * * * *`), *not* a Deno EF. **KB-divergence (escape hatch, recorded in [log.md](log.md)):** v0 has no external I/O (email deferred — no platform mailer), the work is pure CDL data manipulation, and the canonical history contract wants the `HistoryTransactional` row in-transaction → a SQL function (mirroring `mls-sync-resume-watchdog`) is the right surface; an EF wraps it when email lands. Step 1 **initializes** NULL `next_send_timestamp` (the real gap — the app inserts Prospecting rows without it, so reminders never fired); Step 2 **emits** one contact-scoped `'Prospecting reminder due'` history row per due-onset (deduped). **No cadence auto-advance** in v0 (lands with listing-dispatch/broker-ack). Concierge / not-client-activated rows skipped. Live-verified: 1 initialized, 1 reminder emitted, idempotent on re-run.
- (~2 h) **CDL EF `cdl-contact-listings-write`**: writes to `public.contact_listings`. **✅ Satisfied by `cdl-write`** (resource `contact_listings`, ADR-016 dispatcher — the per-resource write EF family is superseded, same as `cdl-contacts-write`). Scope check inside the EF is the only access control until Pattern B.
- (~1 h) **CDL EF `cdl-contact-listings-read`**: cursor paginated reads. **✅ Live** (deployed in the 2026-05-31 broker-scope read-EF batch).
- (~1 h) Live-state refresh + KB drift check. **✅ Done 2026-06-04** — targeted delta on [wiki/architecture.md#live-cdl-state](wiki/architecture.md) (`prospecting` 0 → 1, `history_transactional` 5 → 6, new scheduled-jobs table); no drift found.
- (~1 h) Verify `ContactListings` write authority claim with platform team — log any divergence. **✅ Confirmed** — Pipeline authors `contact_listings` via `cdl-write` (service-role inside, never holds the CDL key); no divergence.
- (Stretch ~2 h) `cdl-schema.md` update PR (platform-team task): add `public.contact_listings` + `public.contact_listing_notes` to Phase 1 expansion list. *(Already documented in [cdl-schema.md](../../data-models/cdl-schema.md) via the ADR-016 re-model migrations — drift item closed.)*

## Week 3 — ContactListings + Showing chain + Caravan {#week-3}

> **Status (2026-06-05): DONE — full FR parity.** All 10 Lovable prompts run + Cursor backend + reconciliation pushed (app `6aa2cb5`). Showings (5-resource chain, `useShowingChain`) and Caravans (`useCaravans`) are live; ContactListings — `ContactListingsPanel` + `useContactListingsEngagement` — is **mounted** on `ContactDetail` with the Matching (b) soft-prompt.
>
> **Write-surface hardening (2026-06-05, post live demo).** A live Weeks-0-3 demo surfaced that the *reads* were wired but several *write* paths still 400'd/401'd against the canonical schema. Fixed without changing the `cdl-write` passthrough: (1) CDL migration `20260605120000_pipeline_week3_write_fixes.sql` adds **legacy-derivation triggers** on `contact_listings`/`contact_listing_notes` (so send-listings + add-note inserts resolve the legacy NOT NULL pivots from RESO keys), the **`x_contact_key`** buyer-to-showing extension ([ADR-022](../../architecture/decisions/ADR-022.md)), and `showing_availability.listing_key`/`listing_id`. (2) App payloads corrected in `useShowingChain.ts` (canonical column names, `text[]` arrays, `timestamptz` composition, buyer via `x_contact_key`), `PropertiesExplorer` (real `listing_key`), `useCaravans` (`useCompleteCaravanRun`: drop nonexistent `showing_agent_remarks`, unique `showing_key` per stop, set `caravan_key`). (3) Activities 401 fixed by wiring the SSO ES256 JWT (`postgrestAccessToken`) into the app-DB client (`kzvhqgpedapzqmwgikrw`, TPA per [ADR-018](../../architecture/decisions/ADR-018.md)).
>
> **Caravan timestamp fix (2026-06-05, app `3582228`).** Post-deploy smoke test of the caravan path surfaced a final `cdl-write` 400: `useCreateCaravan`/`useAddCaravanStop` sent bare `"HH:MM"` strings into the `timestamptz` columns `caravan_start_time`/`caravan_end_time`/`caravan_stop.stop_start_time` (`invalid input syntax for type timestamp with time zone`). Fixed by composing `date + time` into an ISO timestamp (a local `composeTimestamp`, mirroring `useShowingChain`) and forwarding the caravan `date` into `useAddCaravanStop`. Verified end-to-end: create → run (check-in/out both stops) → complete emits 2 `showing` rows (`caravan_key` set, distinct `showing_key` per stop, `listing_key` SMOKE-001/SMOKE-002, feedback in `raw`) and flips `caravan_status='Ended'`.
>
> **Backend done-by-design (ADR-016):** the per-resource EFs listed under _Cursor_ below (`cdl-showing-write`/`-read`, `cdl-caravan-write`/`-read`) were **never built and are not needed** — the generic `cdl-read` (broker-scope read) + `cdl-write` (write/soft-delete + HistoryTransactional) dispatchers cover all five Showing-chain resources, both Caravan resources, and `contact_listings`/`contact_listing_notes`. On 2026-06-05 `lock_or_box` was added to the `cdl-read` whitelist (filterable on `listing_key`/`listing_id`/`lock_or_box_key`/`showing_agent_key`) so the showing UI can surface access info; security trade-off recorded in `cdl-schema.md`.
>
> **Remaining (Lovable, 10 atomic prompts):** (L1) fix the `ContactListingsPanel` read — it called the anon `useContactListings(contactKey)` filtered by `contact_id` against a now service-role-only table, so it returned nothing; switch to an EF hook over `cdl-contact-listings-read`. (L2) role-config seed for `showings`+`caravans`. (L3) Showings Upcoming/Recent split + buyer `contact_key` linkage. (L4) `ShowingAvailability` slot picker. (L5) `LockOrBox` reference card. (L6) post-showing feedback → `contact_listing_notes` + preference + auto-`Activity`. (L7) Caravan create wizard (≥2 stops, order, per-stop time). (L8) Caravan run view → one `showing` per stop on complete. (L9) `/properties` send-listings wizard. (L10) shared `EngagementTimeline` on both `/contacts/:id` and `/properties/:id`.

**Goal**: a broker can send a curated set of listings to a buyer, schedule a single showing or a multi-property caravan, log feedback, and see the engagement timeline on both the Contact and the Property side. Full 5-resource Showing chain wired.

Demo: send 3 listings to a Buyer; the buyer picks two; broker schedules a caravan covering both; logs feedback per stop; sees `Activity` follow-ups generated.

### Lovable {#week-3-lovable}

- (~2 h) `/contacts/:id/listings` tab: list of `ContactListings` for this contact — preference, sent / viewed / favorited timestamps, notes. Cite [wiki/requirements.md#fr-cl-contact-listings](wiki/requirements.md#fr-cl-contact-listings) (FR-CL-01..05).
- (~2 h) "Send listings" wizard from `/properties` (read-only browse via Listing Module → CDL): pick 1..N → attach to `(Contacts × SavedSearch)` → call `cdl-contact-listings-write`.
- (~1 h) Notes drawer on `ContactListings`: writes to `contact_listing_notes` via the same EF. [FR-CL-06..10](wiki/requirements.md#fr-cl-contact-listings).
- (~2 h) `/showings` page: list of upcoming + recent showings (mine + my team's by scope). Cite [wiki/requirements.md#fr-show-showings](wiki/requirements.md#fr-show-showings) (FR-SHOW-01..03).
- (~2 h) Showing creation modal — five RESO resources orchestrated:
  - `ShowingAvailability` (slots for the property — fetched from CDL),
  - `ShowingRequest` (the buyer asks),
  - `ShowingAppointment` (confirmed; stored in CDL `public.showings`),
  - `Showing` (the fact-of-happening, post hoc),
  - `LockOrBox` (access mechanism reference).
  Cite [FR-SHOW-04..09](wiki/requirements.md#fr-show-showings) + [wiki/processes.md#showing-process](wiki/processes.md#showing-process) + the naming-drift note in [wiki/architecture.md#live-cdl-state](wiki/architecture.md#live-cdl-state).
- (~1 h) Post-showing feedback form + auto-`Activity` "Follow up with buyer in 24 h". Cite [FR-SHOW-10..11](wiki/requirements.md#fr-show-showings) + [FR-ACT-05..07](wiki/requirements.md#fr-act-activities).
- (~2 h) `/caravans` page + create wizard: pick 2..N stops, set order, time per stop, route. Cite [wiki/requirements.md#fr-cara-caravan](wiki/requirements.md#fr-cara-caravan) (FR-CARA-01..06).
- (~1 h) Caravan run view: per-stop check-in + feedback; emits one `Showing` per stop on completion.
- (~1 h) Engagement timeline component (reusable) shared by `/contacts/:id` and `/properties/:id`: sent → viewed → showing → offer.

### Cursor {#week-3-cursor}

> **SUPERSEDED by ADR-016 (2026-06-05).** The four dedicated EFs below were the original Week-3 plan; they were **not built and are not needed**. The generic `cdl-read` + `cdl-write` dispatchers handle all five Showing-chain resources, both Caravan resources, and the ContactListings tables. The only Cursor build this week was adding `lock_or_box` to the `cdl-read` whitelist (deployed `cdl-read` v3, 2026-06-05) + explicit `config.toml` `verify_jwt=false` blocks for `cdl-read`/`cdl-engagement-read`. No new EFs and no CDL schema migrations were required.

- ~~(~2 h) **CDL EFs `cdl-showing-write`** (handles all five Showing-chain resources behind one router by `resource` query param). Scope: `pipeline:showings:write`. ES256 + scope check.~~ — superseded by `cdl-write`.
- ~~(~1 h) **CDL EF `cdl-showing-read`**: paginated reads + estimated counts.~~ — superseded by `cdl-read`.
- ~~(~2 h) **CDL EF `cdl-caravan-write`** + `cdl-caravan-read`: writes `Caravan` + `CaravanStop`.~~ — superseded by `cdl-write`/`cdl-read` (both resources live in CDL).
- **DONE (2026-06-05)** — `lock_or_box` added to the `cdl-read` whitelist (broker-scope read of the access-mechanism reference; security trade-off recorded in `cdl-schema.md`); `config.toml` gained explicit `[functions.cdl-read]` + `[functions.cdl-engagement-read]` `verify_jwt=false` blocks.
- (~1 h) Live-state refresh + verify `public.showings` exists with the column shape Lovable expects. **DONE** — confirmed during Week-3 exploration.
- (Stretch) `Showing` post-hoc record table (separate from `ShowingAppointment`): **DONE** — `public.showing` exists alongside `public.showings`; caravan run + post-showing feedback write to it via `cdl-write`.

## Week 4 — TransactionManagement + Offer-to-Closing + Referral {#week-4}

> **Status (2026-06-08): RE-SCOPED + PARTIAL; transaction phase un-deferred (ADR-026).** Transactions list/create/type are live (`useTransactions`). **Scope correction (2026-06-08, [ADR-026](../../architecture/decisions/ADR-026.md)):** Pipeline owns the *transaction phase* of the shared `Property` (ownership is by process, not table). The **platform write-path is now SHIPPED**: the governed **`cdl-listing-lifecycle`** EF drives `acceptOffer` (-> `Pending`), `closeDeal` (-> `Closed`), and `cancelDeal` (-> Back On Market), writing the canonical `Property` close economics (`close_price`/`close_date`/`purchase_contract_date`/`contract_status_change_date`, migration `20260608150000`), auto-(un)locking escrow fields, appending `property_lifecycle_events`, confirming the buyer `ContactListings` row, and emitting the `HistoryTransactional` event (read via `cdl-read` v8 `history_transactional`). The buyer is a `Contact` via `ContactListings`; **no link columns are added to `transaction_management`** (it stays the bare RESO 4-field header). **Still DEFERRED:** in-flight offer *negotiation* economics (amount/currency, counter/sign lifecycle), the FR-REF-08 automatic referral close-the-loop, and the forecast P&L block — these stay clean of the datamodel (no `x_` offer columns) per [ADR-025](../../architecture/decisions/ADR-025.md). **PENDING (Lovable):** rework `/transactions` to call the lifecycle EF (accept/close/cancel), capture buyer+property, and render the `HistoryTransactional` timeline.
>
> Week-4 delivers **Transaction phase (FR-TM, transaction-phase subset) + Referrals (FR-REF) + Documents (FR-DOC)**. All platform (Cursor) work is DONE; the remaining work is Lovable app UI.
> - **Platform (Cursor) — DONE (2026-06-08), Referrals + Documents:** `public.referral` + `public.document` project-flavour CDL resources (migration `20260608120000_pipeline_referral_document_tables.sql`; no RESO equivalent, no `x_`); registered in `cdl-read`/`cdl-write` (v7); ADR-025 + `cdl-schema.md`/`platform-extensions.md` updated. Authorization = `role_configurations` page-keys + CDL JWT-scope (no `sso_app_permissions` rows — see ADR-025).
> - **Platform (Cursor) — DONE (2026-06-08), Transaction phase (ADR-026):** migration `20260608150000` (canonical `Property` close economics); `cdl-listing-lifecycle` EF v1 (`acceptOffer`/`closeDeal`/`cancelDeal` — transition + scope validation, escrow auto-(un)lock via `cdl_lock_field`/`cdl_unlock_field`, `property_lifecycle_events` audit, buyer `ContactListings` confirm, `HistoryTransactional` emit); `cdl-read` v8 registers `history_transactional` as the timeline read; ADR-026 + `data-distribution-and-stewardship.md`/`cdl-schema.md`/`platform-extensions.md`/`transaction-lifecycle.md` updated.
> - **App (Lovable) — PENDING:** (Referrals/Docs) `/referrals` page + create + FR-REF-07 history; referral surfacing (LeadSource=Referral, introduced-by badge, outgoing list, **manual** outcome); Documents tab on `ContactDetail` (link-only over the CDL `document` resource); Referrals nav + `'referrals'` page-key seed. (Transactions) rework `useTransactions.ts` + `Transactions.tsx` to the event-sourced model — buyer via `ContactListings` + property subject, accept/close/cancel via `cdl-listing-lifecycle`, timeline via `cdl-read` `history_transactional` (Lovable prompt drafted).

**Goal**: (Transaction phase) a broker can pick a property + buyer (`ContactListings`), accept an offer (Property → `Pending`, escrow fields lock), and an admin can close (→ `Closed` + `close_price`/`close_date`) or cancel (→ Back On Market) — all through the governed `cdl-listing-lifecycle` EF, with the `HistoryTransactional` timeline shown. (Referrals/Docs) a broker can create a `Referral` row tying two `Contacts` + a `Member` with a manual outcome, and attach link-only `Document` rows to a Contact. (In-flight offer negotiation economics + automatic referral close-the-loop remain deferred — ADR-025.)

Demo: record a referral from a prior happy client; auto-set the referee's `LeadSource=Referral` and show the "introduced by" badge; set the referral outcome manually; attach a KYC document link to a contact.

### Lovable {#week-4-lovable}

- ✅/PENDING (~2 h) Rework `/transactions` to the event-sourced model (ADR-026): `useTransactions.ts` — drop `useRecordPropertyClose`/`useRecordBackOnMarket`; add `useAcceptOffer`/`useCloseDeal`/`useCancelDeal` (POST `cdl-listing-lifecycle`) + `useTransactionTimeline` (`cdl-read` `history_transactional`). `Transactions.tsx` — `PropertyPicker` (subject) + `ContactPicker` (buyer via `ContactListings`), accept/close/cancel actions (Close/Cancel gated org_admin/system_admin), linked `Property` economics (`list_price`+`currency_code`, `close_price`/`close_date`, `standard_status`), and the `HistoryTransactional` timeline. Lovable prompt drafted. Cite [transaction-lifecycle.md](../../business-processes/canonical-processes/processes/transaction-lifecycle.md) + [ADR-026](../../architecture/decisions/ADR-026.md).
- (~2 h) `transaction_management` create/list/type stays as-is (`useCreateTransaction`/`useSetTransactionType` over `cdl-write`) — the bare RESO 4-field header; no link columns (ADR-026). Scope-aware list + type filter.
- DEFERRED (ADR-025) — full offer lifecycle controls (Counter/Sign/Reject/Withdraw/Expire) + offer amount/currency/dates, the forecast P&L block on the TM card, and the closed-TM variance placeholder. Resume with the offer-negotiation workstream.
- (~2 h) Documents tab on `ContactDetail`: upload → CDL `document` resource row pointing at external storage (link only, file not stored); preview + version. Cite [wiki/requirements.md#fr-doc-documents](wiki/requirements.md#fr-doc-documents) (FR-DOC-01..05).
- (~2 h) `/referrals` page + creation: referrer `Contacts` + referee `Contacts` + responsible `Member` + type (Client/Partner/Broker/Internal). Cite [wiki/requirements.md#fr-ref-referral](wiki/requirements.md#fr-ref-referral) (FR-REF-01..03).
- (~1 h) Auto-set `Contacts.LeadSource = Referral` on referee creation if not set; show "introduced by X" badge on referee card. [FR-REF-02, FR-REF-05](wiki/requirements.md#fr-ref-referral).
- DEFERRED (ADR-025) — (~1 h) Referral outcome traversal (FR-REF-08): when referee's deal closes, mark `Referral.outcome` + notify referrer's broker. Resumes with the offer-negotiation workstream; outcome stays **manual** for now.
- (Stretch ~2 h) Referral leaderboard mini-report.

### Cursor {#week-4-cursor}

- ✅ DONE (2026-06-08, ADR-026) **CDL EF `cdl-listing-lifecycle`** (v1) — the governed transaction-phase write-path: `acceptOffer`/`closeDeal`/`cancelDeal` with from→to transition + scope validation, `Property` status + close-economics writes, escrow auto-(un)lock, `property_lifecycle_events` audit, buyer `ContactListings` confirm, `HistoryTransactional` emit. (Supersedes the proposed `cdl-tm-write` — the transaction acts on the canonical `Property`, not a separate TM-write surface.)
- ✅ DONE (2026-06-08) Migration `20260608150000` (canonical `Property` close economics) + `cdl-read` v8 `history_transactional` timeline read.
- DEFERRED (ADR-025) — **EF `listing-module-status-push`** / **`contract-system-push`** / **`contract-system-webhook`**: outbound webhooks to the Listing Module + e-signature provider. Not needed for the in-CDL transaction phase (status is driven canonically on `Property`); resume with the offer-negotiation + external-contract workstream.
- ✅ DONE (2026-06-08) **ADR-026** (event-sourced transaction model; Pipeline owns the `Property` transaction phase) — replaces the planned referral-entity ADR draft; ADR-025 covers the Referral/Document resources.
- (~1 h) Live-state refresh + KB drift check (post-Lovable transactions rework).

## Week 5 — Pipeline projection + Commission Engine {#week-5}

> **Status (2026-06-04): PARTIAL.** The `/pipeline` v0 board is live (`usePipeline` + `pipelineProjection.ts`). The Matching signal is now **wired** (2026-06-04): `usePipeline` consumes `useAllProspecting()` and feeds `prospectingActive` into the projection (no longer inert). Still derives one card per Contact (not per `(Contact × SavedSearch)`). NOT built: the Commission Engine (cost events / rules / deal P&L / compensation), the forecast & variance dashboards, and `/reports`.

**Goal**: a broker sees a Kanban / list view of the canonical 5-stage pipeline auto-derived from CDL + CRM-app-DB state; the Commission Engine ERP-lite forecasts GCI per deal, attributes costs, computes per-broker compensation, and reconciles against Finance ERP actuals.

Demo: open the pipeline view, see every active `(Contacts × SavedSearch)` placed in its derived stage, drill into one, see the forecast P&L + per-broker compensation; later, simulate a Finance ERP webhook (actual GCI) and see variance flow back onto the TM card.

### Lovable {#week-5-lovable}

- (~2 h) `/pipeline` Kanban view: five canonical columns (Qualification / Matching / Showing / Contracting / Closed), each card = one `(Contacts × SavedSearch)`. **No `pipeline_stages` table** — the projection is a view per [wiki/overview.md#pipeline](wiki/overview.md#pipeline) + [FR-FNL-01..06](wiki/requirements.md#fr-fnl-funnel-canonical).
- (~2 h) Card detail + stage-derivation explainer ("why is this here?"): show the inputs (e.g. "`Prospecting.ActiveYN=true` AND ≥1 `ContactListings.ListingSentTimestamp`" → Matching (a)).
- (~1 h) Pipeline filters: by broker, team, OUID, country, budget range, age in stage.
- (~2 h) CRM app DB: Commission Engine tables (per [wiki/commission-engine.md#data-model-stub](wiki/commission-engine.md#data-model-stub)) — `deal_cost_event`, `cost_rate_card`, `commission_rule`, `deal_pnl`, `broker_compensation`. Designed in Lovable from the conceptual stub.
- (~2 h) `/transactions/:id/p&l` tab: forecast P&L breakdown — list `deal_cost_event` rows, the active `commission_rule`, computed `deal_pnl`, per-broker `broker_compensation`. Cite [wiki/commission-engine.md#scope](wiki/commission-engine.md#scope).
- (~1 h) Cost-event entry: broker logs an event (e.g. "Conference Lisbon — 1 200 €") → attaches to one TM → updates `deal_pnl` forecast.
- (~1 h) `commission_rule` editor (admin-only, scope-gated): edit the firm's rule (split percentages, thresholds, role bonuses). Cite [wiki/commission-engine.md#data-model-stub](wiki/commission-engine.md#data-model-stub).
- (~1 h) Variance card on closed TM: shows `actual_gci − forecast_gci`, drilldown to which `deal_cost_event` rows reconciled. Cite [FR-TM-13](wiki/requirements.md#fr-tm-transactions) + [wiki/commission-engine.md#reconciliation](wiki/commission-engine.md#reconciliation).
- (~2 h) `/reports/forecast` dashboard: org-level forecast GCI by month, by office, by broker.
- (~1 h) `/reports/variance` dashboard: actual vs forecast across closed TMs in the period.
- (Stretch ~2 h) Per-broker P&L statement export (PDF).

### Cursor {#week-5-cursor}

- (~2 h) **EF `finance-erp-webhook`** on the CRM app DB project (or a dedicated edge project): receives actual GCI + payment confirmations from the external Finance ERP. Writes `deal_pnl.actual_gci` + emits `HistoryTransactional` (`MajorChangeType = Actual GCI received`). Cite [wiki/integration.md#finance-erp-commission](wiki/integration.md#finance-erp-commission) + [wiki/integration.md#finance-erp-payments](wiki/integration.md#finance-erp-payments).
- (~1 h) **EF `finance-erp-reconcile`** (scheduled, daily): sweeps for closed TMs with no actual GCI, flags them.
- (~1 h) SSO permission keys for the Commission Engine: `pipeline:commission:read`, `pipeline:commission:write`, `pipeline:commission:admin`. Roles: broker / sales-manager / org-admin.
- (~1 h) Live-state refresh.
- (~1 h) Verify with platform team that `deal_pnl` and friends will NOT be migrated to CDL — they are CRM-app-DB-only per [wiki/architecture.md#app-private-state](wiki/architecture.md#app-private-state) and [wiki/commission-engine.md#deviation](wiki/commission-engine.md#deviation).
- (Stretch ~2 h) ADR-XXX-crm-commission-engine.md first draft.

## Week 6 — AI Copilot {#week-6}

> **Status (2026-06-03): NOT STARTED.** No `/ai` settings page, `aiCall` hook, or LLM-wrapper EFs yet.

**Goal**: ship the **floor** of 4 AI features end-to-end (FR-AI-LQ, FR-AI-MAT, FR-AI-SHOW, FR-AI-MAR) plus stubs for the other 10. Every AI surface honors the human-approval matrix and the data-governance rules in [wiki/ai.md#governance](wiki/ai.md). All AI features run as Lovable app EFs that call an LLM provider with just-in-time context loaded from the wiki + entity rows; no AI-only fields persisted to canonical RESO resources.

Demo: paste an inbound inquiry → AI extracts `Contacts` fields + `SavedSearch.SearchQuery` → broker reviews and accepts; open a Buyer with 3 matched listings → AI explains why; open a scheduled showing → AI suggests 3 talking points; open a TM → "Deal Margin Coach" suggests cost-events to log.

### Lovable {#week-6-lovable}

- (~2 h) `/ai` settings page: provider key (env-scoped), model selection, opt-in toggle per power user. Cite [wiki/ai.md#overview](wiki/ai.md#overview).
- (~2 h) Shared `aiCall(featureKey, ctx)` hook: routes to the right app EF, loads the relevant wiki anchor at runtime (e.g. `wiki/requirements.md#fr-pros-prospecting` for the SavedSearch template generator), enforces redaction of PII per role.
- (~2 h) **FR-AI-LQ — Lead Qualification & Routing** ([wiki/ai.md#lead-qualification](wiki/ai.md#lead-qualification)): UI: paste an inbound inquiry → AI returns `Contacts` field draft + `SavedSearch.SearchQuery` draft → broker reviews → on accept, writes to CDL via `cdl-contacts-write` + CRM app DB `saved_search`. Human approval required.
- (~2 h) **FR-AI-MAT — Match Explanation** ([wiki/ai.md#match-explanation](wiki/ai.md#match-explanation)): on `/contacts/:id/listings`, button "Explain match" → AI returns 3-bullet rationale per listing based on `SavedSearch` criteria + `Property` features. Read-only.
- (~2 h) **FR-AI-SHOW — Showing Coach** ([wiki/ai.md#showing-coach](wiki/ai.md#showing-coach)): on `/showings/:id`, before-the-showing card with 3 talking points + 3 likely objections, based on the Contact's profile + Property listing. Read-only.
- (~2 h) **FR-AI-MAR — Deal Margin Coach** ([wiki/ai.md#deal-margin-coach](wiki/ai.md#deal-margin-coach)): on `/transactions/:id/p&l`, suggest cost-events the broker may have missed + flag commission-rule edge cases. Human approval required to log.
- (~1 h) UI stubs (route exists, returns "coming soon") for the remaining 10 features: FR-AI-COM / FR-AI-ACT / FR-AI-PRICE / FR-AI-SENT / FR-AI-SUM / FR-AI-DOC / FR-AI-REC / FR-AI-RISK / FR-AI-PROS-TPL. Cite the respective anchors in [wiki/ai.md](wiki/ai.md).
- (~1 h) Audit log of every AI call (CRM app DB `ai_call_log`): featureKey, input hash, output, reviewer decision, latency. Cite [wiki/ai.md#governance](wiki/ai.md#governance).
- (Stretch ~3 h) Graduate 2 stubs from above to full features (FR-AI-COM + FR-AI-SUM are the highest-leverage candidates).

### Cursor {#week-6-cursor}

- (~2 h) Four LLM-wrapper app EFs (one per AI feature shipping end-to-end): `ai-lead-qualification`, `ai-match-explanation`, `ai-showing-coach`, `ai-deal-margin-coach`. Each loads its wiki anchor at runtime + the entity rows it needs from the right Supabase project; calls the configured LLM provider; returns structured JSON.
- (~1 h) SSO permission key: `pipeline:ai:use` (gates the whole `/ai` surface).
- (~1 h) Rate limit per user (CRM-app-DB `ai_quota` table).
- (~1 h) Verify [wiki/ai.md#governance](wiki/ai.md#governance) PII redaction rules in EF code; add an EF-level test.
- (~1 h) Live-state refresh.
- (Stretch ~2 h) Two more LLM-wrapper EFs to graduate two stubs in lockstep with Lovable.

## Week 7 — Staging hardening + Demo prep {#week-7}

> **Status (2026-06-03): NOT STARTED.** No Playwright happy-path suite, seed data set, or RLS Pattern B rollout on the four critical CDL tables yet.

**Goal**: prototype is power-user-ready. RLS Pattern B is on the four critical CDL tables. Playwright E2E covers the happy paths. ADRs land. Demo script reviewed.

Demo (Friday): a 60-min end-to-end walkthrough with the business power user(s), covering a single luxury Cyprus deal from inquiry → matching → showing → caravan → offer → close → referral → variance.

### Lovable {#week-7-lovable}

- (~2 h) Playwright happy-path tests: Contacts create / edit, SavedSearch create + Prospecting toggle, ContactListings send, Showing schedule, TM lifecycle, Referral create + outcome traversal, Pipeline view derivation, Commission Engine forecast.
- (~2 h) Seed data: 30 contacts, 10 saved searches, 50 contact-listings, 8 showings, 3 caravans, 5 TMs (one in each lifecycle stage), 4 referrals. Power user can demo without manual setup.
- (~1 h) Role configuration page wired into SSO Console for the staging tenant (broker / sales-manager / org-admin scopes verified).
- (~1 h) Performance pass: `performance.md` p99 ≤ 20 ms single-property; cursor pagination on every list page; estimated counts where exact is too slow.
- (~1 h) Empty-state polish on every page; loading skeletons; error toasts.
- (~1 h) Accessibility pass: keyboard nav, focus rings, ARIA on every interactive component.
- (~1 h) Sharp visual sanity: brand check pass (Navy palette, typography, sidebar spacing).
- (~2 h) Demo script: 60-min runbook the demo presenter follows.
- (~1 h) RU strings completed (i18n parity). *(EN/RU/HU file-locale parity + the CDL terminology-override layer landed early in Week 0 — see [#week-0](#week-0) / [ADR-020](../../architecture/decisions/ADR-020.md).)*
- (Stretch ~4 h) Graduate one or two AI stubs from Week 6.

### Cursor {#week-7-cursor}

- (~2 h) **RLS Pattern B rollout** on `public.contact_listings`, `public.contact_listing_notes`, plus any other CDL tables flagged in [wiki/architecture.md#compliance-gates](wiki/architecture.md#compliance-gates). Coordinated with platform team.
- (~1 h) Daily lint EFs review: `sso-member-roster-lint`, `cdl-schema-drift-lint`. Run cleanly for two consecutive days.
- (~2 h) **ADR-XXX-crm-referral-entity.md** — finalize and merge in `matrix-platform-kb/docs/architecture/decisions/`.
- (~2 h) **ADR-XXX-crm-commission-engine.md** — finalize and merge.
- (~1 h) KB drift handoffs to platform team:
  - `cdl-schema.md` Phase 1 expansion: add `public.contact_listings` / `public.contact_listing_notes`.
  - `cdl-schema.md` rename: `public.showing_appointments` → `public.showings`.
- (~1 h) Final `wiki/architecture.md#live-cdl-state` refresh + `last_updated` bump.
- (~1 h) Append `## [<date>] phase-checkpoint | Week 7` to `log.md` with the demo outcome and a link to the demo recording.
- (Stretch ~2 h) Project-wide retro doc → seeds the next 2-month plan.

## Phases-wide artifact summary

By end of Week 7, the following exist:

- Lovable preview / staging URL behind SSO, full BRD coverage.
- 12 wiki pages (this subtree) at `status: stable`.
- Two merged ADRs in `matrix-platform-kb/docs/architecture/decisions/`.
- ~15 deployed Edge Functions across CDL + CRM-app-DB projects (each with `verify_jwt: false`, ES256 verification, scope checks).
- Playwright happy-path suite.
- Seed data + demo script.
- Two KB-drift handoffs to platform team (`cdl-schema.md` updates).
- Closing `phase-checkpoint` entries in [`log.md`](log.md).
