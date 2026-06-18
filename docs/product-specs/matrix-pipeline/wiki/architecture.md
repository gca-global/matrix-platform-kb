---
title: Architecture — Storage, Identity, CDL access, RESO compliance
status: stable
source: raw/context-v2.md §5a, §11
last_updated: 2026-06-04
tags: [architecture]
---

# Architecture — Storage, Identity, CDL access, RESO compliance

> Three Supabase projects (SSO + CDL + CRM app DB), the identity boundary between SSO and CDL Member roster, the access pattern that makes CRM a **client** of CDL via dedicated Edge Functions, the live CDL state (MCP-verified), what's planned for Phase 2+ migration, what stays app-private forever, and the eight RESO compliance gates + escape hatch that govern every implementation decision.

## TOC

- [#three-supabase](#three-supabase)
- [#git-sync-handoff](#git-sync-handoff)
- [#identity-boundary](#identity-boundary)
- [#cdl-access-pattern](#cdl-access-pattern)
- [#live-cdl-state](#live-cdl-state)
- [#phase-2-migration](#phase-2-migration)
- [#app-private-state](#app-private-state)
- [#kb-sources-of-truth](#kb-sources-of-truth)
- [#compliance-gates](#compliance-gates)
- [#escape-hatch](#escape-hatch)
- [#resource-map](#resource-map)
- [#process-map](#process-map)
- [#crosswalk](#crosswalk)

## Three Supabase projects and ownership boundaries {#three-supabase}

| Project | ID | Owner | Managed from Lovable? | Purpose |
|---|---|---|---|---|
| **SSO** | `xgubaguglsnokjyudgvc` | `matrix-platform-foundation/supabase/` | No | Identity, JWT (ES256), roles, permissions, tenants, SSO admin EFs |
| **CDL** | `ofzcokolkeejgqfjaszq` | `matrix-platform-foundation/supabase-cdl/` | **No** | System-of-record for canonical RESO resources (shared business data) |
| **CRM app DB** | `kzvhqgpedapzqmwgikrw` | CRM team via Lovable | **Yes** | App-private state: workflow, drafts, UI cache, app-local lookups, `role_configurations`, `activities`, `notifications`. (Frontend client → `https://kzvhqgpedapzqmwgikrw.supabase.co`; the legacy v1 project `mydojctcewxrbwjckuyz` is **not** used here.) |

CDL and SSO are owned by the platform team and evolve via `matrix-platform-foundation`; CRM app DB is owned by the CRM team and evolves via Lovable. CRM **never** holds the CDL service-role key and **never** modifies the CDL schema — all CDL changes go through `matrix-platform-foundation/supabase-cdl/`.

Source: raw/context-v2.md §5a.1.

## Cursor working copy: git sync + Lovable handoff {#git-sync-handoff}

Cursor edits this ecosystem locally and **Lovable is the other author** of `matrix-pipeline-2-0`. A local `github-watcher` deploys `matrix-pipeline-2-0` to Apache `/pipeline/` on push to `main` and syncs the GitHub remote (where Lovable pushes) down to the local checkout (see [`../../platform/app-catalog.md`](../../../platform/app-catalog.md)). If the watcher isn't running, the local checkout can fall **behind** the remote — so Cursor must validate freshness before editing and hand work back cleanly so Lovable + the watcher pick it up.

### Pre-flight (before editing any ecosystem repo in Cursor)

1. `git fetch origin`.
2. If local `main` is **behind** `origin/main` → `git pull --ff-only`.
3. If the branches have **diverged** → STOP and surface to the user. Never auto-merge, rebase, or force.

### Post-work handoff (when Cursor finishes a change)

Commit + push the affected repo(s) so the watcher deploys and Lovable sees the latest. This intentionally overrides the global "only commit when asked" default **for the matrix-pipeline ecosystem repos**. Work spans **three repos** and **two Supabase projects**; route each change class to the repo that owns its Supabase project:

| Change class | Supabase project | Commit to | Lovable sees it as |
|---|---|---|---|
| CDL edge function (`cdl-write`, `cdl-read`, `cdl-engagement-read`, `cdl-contact-listings-read`, …) | CDL `ofzcokolkeejgqfjaszq` | `matrix-platform-foundation/supabase-cdl/functions/` | KB + `docs/cdl-ef-contracts/` (NOT a Lovable migration — CDL is not linked to Lovable, ADR-013) |
| CDL DB migration / schema / data | CDL `ofzcokolkeejgqfjaszq` | `matrix-platform-foundation/supabase-cdl/migrations/` | KB + `docs/cdl-ef-contracts/` |
| **App-specific edge function** (correct / modify / add) | app DB `kzvhqgpedapzqmwgikrw` | `matrix-pipeline-2-0/supabase/functions/` | **committed EF source in the app repo** |
| **App-specific Supabase schema / data** | app DB `kzvhqgpedapzqmwgikrw` | `matrix-pipeline-2-0/supabase/migrations/` | **committed migration in the app repo** |
| UI code (`src/**`) | — | `matrix-pipeline-2-0` | committed source (watcher deploys) |
| KB / docs | — | `matrix-platform-kb` | docs |

Two rules that make the handoff seamless:

- **EF deploys are not source-of-truth.** An MCP `deploy_edge_function` is invisible until the EF source (and any migration) is committed to the repo that owns that Supabase project — `matrix-platform-foundation` for CDL EFs, `matrix-pipeline-2-0/supabase/functions/` for app EFs. Deploy **and** commit.
- **App-Supabase changes must reach Lovable as migrations.** Cursor does **not** only touch CDL/foundation — it may correct or add app-specific EFs and modify the app-specific Supabase project (`kzvhqgpedapzqmwgikrw`). Every such change lands as a committed migration / EF source in `matrix-pipeline-2-0` so Lovable can see it; it is never applied out-of-band. (CDL changes, being outside the app repo and not linked to Lovable, are surfaced via this KB + `docs/cdl-ef-contracts/` instead.)

Git-safety constraints still apply (inherited from the agent system prompt): never force-push, never push to a diverged `main` without user direction, `--ff-only` only.

```mermaid
flowchart LR
  Lovable -->|push| Remote["GitHub origin/main"]
  Remote -->|"github-watcher pull"| Local["Local checkout"]
  Local -->|"github-watcher build"| Apache["/pipeline deploy"]
  Cursor -->|"pre-flight: fetch + pull --ff-only"| Local
  Cursor -->|"app EF + migration + UI: commit + push"| Remote
  Cursor -->|"CDL EF + migration: commit + push"| Foundation["matrix-platform-foundation"]
  Foundation -.->|"applies to"| CDL["CDL Supabase (ofzcokolkeejgqfjaszq)"]
  Remote -.->|"Lovable sees migrations"| AppDB["app Supabase (kzvhqgpedapzqmwgikrw)"]
```

Operative enforcement lives in [`/.cursor/rules/cursor-git-handoff.mdc`](../../../../../.cursor/rules/cursor-git-handoff.mdc); the Lovable-facing mirror is in `matrix-pipeline-2-0/.lovable/instructions.md`.

Source: [`../../platform/app-catalog.md`](../../../platform/app-catalog.md) (github-watcher); ADR-013 (CDL not linked to Lovable).

## Identity boundary {#identity-boundary}

- SSO issues all JWTs (ES256, ADR-011).
- CDL verifies SSO tokens via **Supabase Third-Party Auth** (JWKS URL + issuer from SSO; ADR-012).
- CRM app DB verifies the same SSO JWTs under ordinary RLS (`auth.jwt()` helpers).
- Single identity chain: user authenticates in SSO → gets SSO JWT → the same token is presented to all three projects.
- **Identity / permissions (SSO) vs. business roster (CDL) — two different concepts**:
  - **SSO** stores user identity (account, email, password), roles, groups, scope claims, permissions — everything that answers "can this user log in and what are they allowed to do?". CRM is an SSO client (see [wiki/overview.md#personas](overview.md#personas)).
  - **CDL** stores the canonical RESO business roster (`Member` / `Office` / `OUID` / `Teams` / `TeamMembers`) — who is a licensed broker, in which office / team / OUID — for canonical FK references (`OwnerMemberKey`, `ListAgentKey`, `BuyerAgentKey`). Answers "who is this user in the brokerage's business roster?".
  - **Mapping**: SSO `user_id` ↔ `Member.MemberKey` (either via canonical `Member.MemberAlternateId` as a mapping attribute, or an explicit mapping mechanism in the SSO Console). SSO group ↔ canonical `Teams.TeamKey` (mapping in SSO Console). No parallel org-tables (see [#compliance-gates](#compliance-gates) Roster gate).
  - CRM consumes both: SSO for permission gating and UI access control, CDL `Member` / `Teams` for canonical FK targets and business display (broker name, brokerage, team, office).

Source: raw/context-v2.md §5a.2.

## CRM as a CDL client — access pattern {#cdl-access-pattern}

CRM gets all rights and authority for CDL CRUD **as a client app** via canonical access mechanisms. CRM has no direct access to the CDL service-role key; instead:

- **`ssoClient`** (`xgubaguglsnokjyudgvc`) — auth, roles, permissions, tenants, SSO admin EFs.
- **`cdlClient`** (`ofzcokolkeejgqfjaszq`) — CDL reads under SSO JWT via Third-Party Auth; CDL writes through dedicated EFs invoked from this client.
- **`supabase`** (CRM app DB, Lovable-managed) — app-private data under ordinary RLS keyed off the SSO JWT.

**CDL reads** patterns:
- Filtered property listings → `cdlClient.functions.invoke('listings-search', …)`.
- Anonymous snapshot → `anon .from('properties_published').select(...)` under RLS.
- PII tables (`contacts`, `showings`) — only via CDL EFs with explicit scope check (service-role-only at the RLS layer).

**CDL writes** go through **dedicated EFs** deployed in `matrix-platform-foundation/supabase-cdl/functions/`. Each such EF: `verify_jwt = false`, verifies the SSO JWT itself, checks scope ∈ `SSO_ALLOWED_SCOPES`. A generic `cdl-write` EF in the platform template is not yet built; CRM-specific write-EFs are added per resource as needed.

**User display names**: only via the SSO `resolve-users` EF + React hook `useUserDisplay`. **Never** SQL-join CDL ↔ `sso_users`.

**`mls_sources.kind`** for `matrix-pipeline`: `internal` (`matrix-internal` — target state for all Sharp SIR markets).

Source: raw/context-v2.md §5a.3.

## CDL as-built (live state, MCP-verified 2026-06-03; targeted delta 2026-06-04: prospecting + history + scheduled jobs) {#live-cdl-state}

Canonical RESO resources and infrastructure tables already in CDL and available to CRM as a client.

### Canonical RESO resources (with live data)

| Canonical RESO resource | CDL table | Rows | RLS |
|---|---|---|---|
| Property | `public.properties` | 16 014 | ⚠️ disabled |
| Property media | `public.property_media` | 264 095 | ⚠️ disabled |
| Property (anon snapshot) | `public.properties_published` | 13 916 | ✓ enabled |
| PropertyRooms | `public.property_rooms` | 0 | ✓ enabled |
| PropertyUnitTypes | `public.property_unit_types` | 0 | ✓ enabled |
| Member | `public.members` | 129 | ✓ enabled |
| Office | `public.offices` | 59 | ✓ enabled |
| Contacts | `public.contacts` (PII) | 45 108 | ✓ enabled |
| ContactListings | `public.contact_listings` (junction Contacts × Property) | **24 979** | ✓ enabled (2026-05-29, service-role-only) |
| ContactListingNotes | `public.contact_listing_notes` | 0+ | ✓ enabled (2026-05-29, service-role-only) |
| HistoryTransactional | `public.history_transactional` (append-only) | 6 | ✓ enabled |
| OpenHouse | `public.open_houses` (excluded from CRM scope — see [#escape-hatch](#escape-hatch)) | 0 | ✓ enabled |
| ShowingAppointment | `public.showings` | 0 | ✓ enabled |
| InternetTracking | `public.internet_tracking_events` | 0 | ✓ enabled |
| SavedSearch | `public.saved_search` | 0 | ✓ enabled (2026-05-29) |
| Prospecting | `public.prospecting` (PII) | 1 | ✓ enabled (service-role-only) |
| ShowingAvailability | `public.showing_availability` | 0 | ✓ enabled (2026-05-29) |
| ShowingRequest | `public.showing_request` | 0 | ✓ enabled (2026-05-29) |
| Showing (recorded fact) | `public.showing` (≠ `public.showings`) | 0 | ✓ enabled (2026-05-29) |
| LockOrBox | `public.lock_or_box` | 0 | ✓ enabled (service-role-only) |
| Caravan / CaravanStop | `public.caravan` / `public.caravan_stop` | 0 | ✓ enabled (2026-05-29) |
| TransactionManagement | `public.transaction_management` (canonical 4 fields; economics app-private) | 1 | ✓ enabled (2026-05-29) |

### Projection / list views (denormalized read path)

| View | Backed by | Shape | Grants |
|---|---|---|---|
| `public.v_members_list` | `members LEFT JOIN offices` | member display/lookup columns + denormalized `office_name` / `office_city` / `office_country` (join on `office_key`, fallback `office_id`) | anon, authenticated |
| `public.v_offices_list` | `offices` | office display columns + denormalized `agent_count` (members per `office_key`) | anon, authenticated |

Added by `20260603140000_member_office_list_views.sql` (Week 1 Cursor stretch
#7). Regular `security_invoker` views — RESO-native column names preserved.
Pipeline `useMembers` / `useOffices` read these with explicit projections (no
`select *`); `MemberPicker` shows the agent's office without a second fetch +
client join. Verified live: 129 member rows, 59 office rows, `agent_count`
populated (top office = 25 agents); only 38/129 members resolve `office_name`
(legacy Qobrix `office_key` values with no matching office row — upstream data
sparsity, not a view defect). Supersede the dropped `v_dash_members` /
`v_dash_offices`.

### Scheduled jobs (pg_cron)

| Job | Schedule | Runs | Purpose |
|---|---|---|---|
| `mls-sync-resume-watchdog` | `* * * * *` | `public.mls_sync_resume_watchdog()` | Resume stale sync jobs + per-tenant scheduled syncs |
| `cdl-prospecting-tick-hourly` | `0 * * * *` | `public.cdl_prospecting_tick()` | **Week-2 Prospecting reminder engine** — initialize `prospecting.next_send_timestamp` + emit one contact-scoped `'Prospecting reminder due'` `history_transactional` row per due-onset. v0: no email, no cadence auto-advance — see [cdl-schema.md](../../../data-models/cdl-schema.md) "Scheduled jobs". First run 2026-06-04: 1 initialized, 1 reminder emitted. |

### RESO DD metadata (served to FE for tooltips/dropdowns)

| Table | Purpose | Rows |
|---|---|---|
| `public.reso_field_descriptions` | RESO DD field descriptions, served to Atlas FE for help tooltips; seeded from official RESO DD CSV | 2 010 |
| `public.reso_lookup_value_descriptions` | RESO DD lookup values, served with field_descriptions for dropdowns / option-level tooltips | 3 683 |

### Stewardship / extensions

| Table | Purpose |
|---|---|
| `public.property_extension_kv` | RESO / OData extension values without jsonb on `properties`; populated via `cdl_property_kv_sync_from_json_text()` |
| `public.entity_field_locks` | Row-level field locks (companion to `locked_fields` jsonb during migration) |
| `public.property_field_overrides` | Per-field overrides at the record level |
| `public.property_lifecycle_events` | Append-only audit of `Property` lifecycle transitions |

### Control plane / ingestion

| Table | Purpose | Rows |
|---|---|---|
| `public.mls_sources` | Source registry (`internal` / `legacy-internal` / `brand-network` / `external`) | 3 |
| `public.mls_settings` | MLS sync settings | 1 |
| `public.mls_sync_jobs` | Sync job history | 50 |
| `public.mls_sync_state` | State per source | 6 |
| `public.mls_orchestrator_runs` | Orchestrator run history | 187 |
| `public.field_mappings` | Field mappings configuration | 0 |
| `public.ingest_audit` | Ingestion audit log | 548 |
| `cdl_staging.listings_raw` | Raw staging | 490 754 |
| `cdl_staging.listings_mapped` | Mapped staging | 254 916 |
| `cdl_staging.media_staging` | Media staging | 0 |

Source: live state via `user-supabase-cdl` MCP (`list_tables` + introspection 2026-06-03; prior run 2026-05-18); `docs/data-models/cdl-schema.md`. **Deltas since 2026-05-18:** `contacts` 45 073 → 45 108 (+35); `history_transactional` 0 → 5 (Week-1 `HistoryTransactional` emission is now live); `transaction_management` 0 → 1. All other canonical/infra counts and RLS flags unchanged (`properties` RLS still ⚠️ disabled).

### KB drift (flagged for platform team)

> **Drift — `members` `member_alternate_id`** (flagged 2026-06-03; **partially resolved 2026-06-15, ADR-031**): the CDL `public.members` table historically had **no `member_alternate_id` column**, so the [#identity-boundary](#identity-boundary) mapping "SSO `user_id` ↔ `Member.MemberKey` via canonical `Member.MemberAlternateId`" was **not materialized** and the only viable SSO↔roster join was `member_email` (121/129 members have an email; 107 are `Active`). **ADR-031** added the canonical `member_alternate_id` column (migration `20260615120000`); Members provisioned from Active Directory by `matrix-pipeline` (owner picker → `cdl-write` resource `members`) now stamp the **Azure AD object id** there, materializing the mapping for newly-minted owners. **Residual:** legacy feed-sourced rows still lack it, so `sso-member-roster-lint` continues to diff on email until the existing roster is backfilled. See [cdl-schema.md](../../../data-models/cdl-schema.md) "Owner-clamp deferred".

> **Drift — Teams** ✅ RESOLVED 2026-05-29: `cdl-schema.md` now reflects the PR1.5 DROP of `public.teams`. Pipeline derives team identity from SSO groups (ADR-015 #5 Option B).

> **Drift — `v_dash_members` / `v_dash_offices` dropped, no `is_deleted`** ✅ RESOLVED 2026-06-03: the strict-RESO waves hardened `members` / `offices` to pure canonical RESO and **dropped their `is_deleted` columns**, which also removed the soft-delete-filtered `v_dash_members` / `v_dash_offices` views. `cdl-schema.md` now marks both dash views DROPPED. The Pipeline read path uses the new `v_members_list` / `v_offices_list` projection views instead (see [cdl-schema.md](../../../data-models/cdl-schema.md) "Member / office list views"). Readers MUST NOT filter `is_deleted` on members/offices.

> **Drift — contact tables** ✅ RESOLVED 2026-05-29: `public.contact_listings` + `public.contact_listing_notes` are now documented in `cdl-schema.md` (Phase-2 expansion), adopted into the foundation repo (`20260529161000`), re-modeled to canonical RESO, and **RLS-enabled** (service-role-only). The gate violation is closed.

> **Security advisory** ✅ contact-engagement tables RESOLVED 2026-05-29: `public.contact_listings` (24 979 rows) and `public.contact_listing_notes` now have RLS **enabled** service-role-only (anon/authenticated access revoked); reads go through `cdl-contact-listings-read`, writes through `cdl-write`. The broader RLS-disabled set on ingestion-side tables (`public.properties`, `public.property_media`, `public.property_field_overrides`, `public.mls_*`, `public.ingest_audit`, `cdl_staging.*`) remains a known transitional posture tracked as **S1 backlog** for the platform team (Pattern B); the CDL EF scope check is the access-control mechanism for those in the interim. The EF gate remains the canonical access path even after Pattern-B RLS lands.

> **Naming drift advisory** ✅ RESOLVED 2026-05-29: `cdl-schema.md` now names the ShowingAppointment table `public.showings` (Phase-1) and documents the separate RESO `Showing` recorded-fact table as `public.showing` (Phase-2, `20260529160000`). The two are distinct CDL tables — `public.showings` = ShowingAppointment (booked slot), `public.showing` = Showing (recorded fact). Do not conflate.

## CDL migration status (Phase 2) {#phase-2-migration}

Canonical RESO resources and their CDL landing status. **9 of these landed in CDL on 2026-05-29** (migrations `20260529160000` + `20260529161000`, ADR-016). Each now writes through `cdl-write` and reads via PostgREST/EF; the CRM app DB keeps only the `*_pending` fallback + deal economics.

| Canonical RESO resource | CDL table | Status |
|---|---|---|
| SavedSearch | `public.saved_search` | ✅ landed 2026-05-29 |
| Prospecting | `public.prospecting` | ✅ landed 2026-05-29 (PII) |
| ShowingAvailability | `public.showing_availability` | ✅ landed 2026-05-29 |
| ShowingRequest | `public.showing_request` | ✅ landed 2026-05-29 |
| Showing (separate from ShowingAppointment) | `public.showing` | ✅ landed 2026-05-29 |
| LockOrBox | `public.lock_or_box` | ✅ landed 2026-05-29 |
| Caravan, CaravanStop | `public.caravan`, `public.caravan_stop` | ✅ landed 2026-05-29 |
| TransactionManagement | `public.transaction_management` | ✅ landed 2026-05-29 (canonical 4 fields; economics app-private) |
| Teams | — | Derived from SSO groups (ADR-015 #5 Option B) — not re-introduced to CDL |
| TeamMembers | — | Derived from SSO groups (Option B) |
| OUID | — | Deferred; derive from SSO/`offices` until a canonical need arises |

Source: migrations `20260529160000` + `20260529161000`; ADR-016. As FRs build against these, they target CDL directly (no semantic change).

## App-private state (always CRM app DB, never CDL) {#app-private-state}

Not canonical RESO and not cross-app:

- `Activity` (calls, tasks, follow-ups — CRM workflow state; extended markup for cost attribution — see [wiki/requirements.md#fr-act-activities](requirements.md#fr-act-activities) FR-ACT-10).
- `Document` references (document metadata; files live in external systems).
- Pipeline-state UI cache (5-stage funnel as a **calculated** projection — see [wiki/overview.md#pipeline](overview.md#pipeline)). The Opportunity *anchor* it projects onto is stored in the **app DB** (`opportunity`/`opportunity_link`, [ADR-035](../../../architecture/decisions/ADR-035.md), supersedes ADR-034); the *stage* is never stored anywhere.
- Drafts, app-specific lookup tables.
- Any UI preferences, view configs, caches.
- **Deal Commercialization, GCI, and Commission Engine state** ([wiki/commission-engine.md](commission-engine.md)) — operational deal costs, commission rates and rules, computed per-deal P&L and broker compensation. Detailed app-private data model, formulas, and FRs. **As-built (2026-06-10, [ADR-028](../../../architecture/decisions/ADR-028.md#implementation-status-as-built)):** the shipped tables are `deal_cost_event`, `cost_rate_card`, `commission_rule` (country-scoped, date-versioned), `commission_estimate` (the conceptual `DealPnL`, generalized per listing/sales-contract), and `broker_compensation` — all real app-private tables, not computed views. The project-flavour deviation is recorded in the [#escape-hatch](#escape-hatch).
- **`Referral`** ([wiki/entities.md#referral](entities.md#referral)) — referrer ↔ referee link with type, outcome, close date. Project-flavour entity outside canonical RESO DD 2.0 (see [#escape-hatch](#escape-hatch)). Stored app-private in CRM app DB; references canonical `Contacts.ContactKey` in CDL via a CRM-app-DB → CDL FK reference (a logical pointer, not a canonical relationship).
- **`role_configurations`** (CRM role → permission-keys mapping) lives on the **CRM app DB** (matrix-pipeline's own project `kzvhqgpedapzqmwgikrw`), consistent with `#app-private-state`. Pipeline reads it via the **App DB `supabase` client** under the SSO JWT (`useRoleConfig.ts`); its SELECT policy is public/`true` and writes are admin-gated. *(Corrected 2026-06-01 — the earlier [log.md](../log.md) [2026-05-26] "SSO co-location" divergence was inaccurate; the table never lived on SSO. See log.md [2026-06-01].)*

Source: raw/context-v2.md §5a.6.

## KB sources of truth {#kb-sources-of-truth}

- CDL schema: [`../../data-models/cdl-schema.md`](../../../data-models/cdl-schema.md)
- Three-project architecture + EF contracts: [`../../platform/app-template.md`](../../../platform/app-template.md)
- RLS / identity / Third-Party Auth: [`../../platform/security-model.md`](../../../platform/security-model.md)
- ADRs: ADR-011 (ES256), ADR-012 (CDL Third-Party Auth), ADR-013 (CDL/SSO ownership; CDL not linked to Lovable), ADR-014 (CDL as-built vs original 18-table design), ADR-015 (CDL Pipeline EF surface — Proposed), ADR-016 (canonical-into-CDL acceleration — 9 tables + contact_listings re-model + `cdl-write` dispatcher — Accepted 2026-05-29).
- Stewardship / source taxonomy: [`../../architecture/data-distribution-and-stewardship.md`](../../../architecture/data-distribution-and-stewardship.md).
- Pipeline-specific CDL CRUD recipes (Lovable-facing): [`../cdl-crud-contract.md`](../cdl-crud-contract.md). Live reachability matrix iteration copy: `mem://infrastructure/cdl-coverage.md`.

Source: raw/context-v2.md §5a.7.

## RESO compliance gates {#compliance-gates}

- **Schema gate**: no CRM migration may introduce a table/field that doesn't match RESO DD 2.0 (canonical resource + canonical attribute). Any deviation requires an ADR in `matrix-platform-kb/docs/architecture/decisions/` and an explicit pin in [#escape-hatch](#escape-hatch).
- **Status gate**: no state machine in CRM may duplicate `Property.StandardStatus`, `ShowingAppointmentStatus`, `CaravanStatus`, `ContactType`, `ContactStatus`, `ContactListingPreference` with its own enum — only canonical RESO lookups.
- **Audit gate**: every state transition MUST emit a `HistoryTransactional` row (see [wiki/integration.md#history-emission](integration.md#history-emission)).
- **Roster gate**: business roster and org-model (canonical RESO `Member` / `Office` / `OUID` / `Teams` / `TeamMembers`) are sourced **only from CDL**; no parallel org-tables in CRM app DB. User identity (SSO account, roles, groups, scope claims, permissions) is a **separate domain in SSO** (`xgubaguglsnokjyudgvc`), not duplicating the canonical roster: SSO answers "can this user log in and what are they allowed to do?", CDL answers "who is this user in the brokerage's business roster?" (canonical FK targets `OwnerMemberKey` / `ListAgentKey` / `BuyerAgentKey` etc.). Mapping: SSO `user_id` ↔ `Member.MemberKey` via canonical `Member.MemberAlternateId` or an explicit mapping in the SSO Console; SSO group ↔ `Teams.TeamKey` (mapping in SSO Console). See [#identity-boundary](#identity-boundary).
- **Integration gate**: contracts and **actual** payments / commission ledger are **not** first-class CRM data entities. External systems (contract management + Finance ERP) are the sole source of truth for legally significant records; CRM observes them via webhooks and mirrors via `Property.StandardStatus` + `HistoryTransactional`. Permitted deviation: forecast GCI, commission rule engine, per-deal P&L are stored in CRM app-private tables of the [wiki/commission-engine.md](commission-engine.md) subsystem as an advisory tool for the sales broker, with an explicit reconciliation pattern against the actual ledger in external Finance ERP. See [#escape-hatch](#escape-hatch).
- **AI gate**: AI features read and update exclusively canonical resources. Introducing "AI-only" fields not mapped to RESO DD 2.0 is forbidden.
- **CDL access gate**: for any CDL table with RLS disabled, CRM **MUST** go through dedicated CDL EFs with SSO JWT scope check — not via direct anon/authenticated PostgREST. Until table-level RLS is enabled per Pattern B (`security-model.md`), the CDL EF is the only access-control mechanism. Direct PostgREST access from the CRM app layer is forbidden. **2026-05-29:** `public.contact_listings` + `public.contact_listing_notes` are now RLS-enabled (service-role-only) and reached via `cdl-contact-listings-read` / `cdl-write` — the engagement-data violation is closed. The gate still applies to the remaining RLS-disabled ingestion-side tables: `public.properties`, `public.property_media`, `public.property_field_overrides`, `public.mls_*`, `public.ingest_audit`, `cdl_staging.*` (S1 backlog, Pattern B).
- **Pipeline gate**: the pipeline **stage** is **not** stored. It is derived from canonical state ([wiki/overview.md#pipeline](overview.md#pipeline)). Any implementation that materializes `pipeline_stages` or a `stage` column violates compliance. **Refined by [ADR-034](../../../architecture/decisions/ADR-034.md), home updated by [ADR-035](../../../architecture/decisions/ADR-035.md)**: a stored `Opportunity` *anchor* (`opportunity` + `opportunity_link`, now in the **app DB**, Lovable-owned) **is** allowed — it is the explicit subject the stage projects onto — but the **stage stays calculated only** (`deriveOpportunityStage`), so the "no stored stage / no `pipeline_stages` table" rule is preserved. Storing the stage on the opportunity row is forbidden.

Source: raw/context-v2.md §11.5.

## Allowed deviations (escape hatch) {#escape-hatch}

Explicit deviations from canonical RESO DD 2.0 (structural + cosmetic + a per-tenant terminology-override layer; one earlier storage-location row was withdrawn) are accepted at this BRD release:

| Deviation | Canonical alternative | Reason | Status |
|---|---|---|---|
| **`OpenHouse` excluded from CRM scope** | Canonical `OpenHouse` (RESO DD 2.0) | Public open-house format is not used in agency practice; invitation-only showings via the Showing chain (optionally grouped in `Caravan`) | Accepted (see [wiki/entities.md#showing-chain](entities.md#showing-chain), [wiki/entities.md#caravan](entities.md#caravan)) |
| **CRM-internal ERP-lite subsystem Deal Commercialization, GCI, and Commission Engine** — app-private state in CRM app DB for forecast GCI, cost attribution, and broker compensation | Canonical `TransactionManagement` + `HistoryTransactional` + external Finance ERP ([wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission), [wiki/integration.md#finance-erp-payments](integration.md#finance-erp-payments)) | Canonical RESO has no deal-level P&L / commission ledger resources (transaction-lifecycle Non-goals); `matrix-fm` is entity-level; external Finance ERP remains system of record for actual money flow. The subsystem ([wiki/commission-engine.md](commission-engine.md)) is a forecast + rule engine advisory tool for the sales broker | Accepted. Deliverable: ADR `ADR-XXX: CRM Internal Commission Engine for Sales Brokers` (status TODO) |
| **`Referral` as a self-standing CRM entity** ([wiki/entities.md#referral](entities.md#referral)) — referrer ↔ referee `Contacts` link + `OwnerMemberKey` + referral type + outcome + close date | Canonical RESO DD 2.0 has no `Referral` resource. Alternative via `Contacts ↔ Contacts` + `Contacts.LeadSource=Referral` considered and rejected | Luxury referral economy in HNWI/UHNWI requires structured tracking (referral type, outcome, close date, commission attribution to the referrer) — impossible through only the `LeadSource` lookup or `Contacts ↔ Contacts` relationships which carry no typed fields for attribution / outcome tracking | Accepted. Deliverable: ADR `ADR-XXX: CRM Referral Entity for Luxury Segment` (status TODO); the [wiki/overview.md#reso-policy](overview.md#reso-policy) policy explicitly exempts `Referral` from the no-custom-entities rule |
| **Branding divergence: UI string "Matrix Pipeline 2.0"** | Canonical product identifier `matrix-pipeline` | Product-owner branding decision; canonical identifier preserved everywhere except user-facing UI strings (sidebar, page titles, login screen). No effect on data model, RESO compliance, scope, three-Supabase boundaries, or KB ↔ implementation joins. | Accepted ([log.md](../log.md) 2026-05-26). No ADR required (cosmetic, reversible by single PR). |
| ~~`role_configurations` co-located with SSO permission keys (SSO project)~~ | — | **Withdrawn 2026-06-01.** This divergence was inaccurate: `role_configurations` actually lives on the **CRM app DB** (`useRoleConfig.ts` reads it via the App DB `supabase` client), consistent with `#app-private-state`. No escape hatch is needed. See [log.md](../log.md) [2026-06-01]. | N/A (no deviation) |
| **Per-tenant RESO label/description/lookup-value overrides extend `reso_field_descriptions`** (CDL) via a `tenant_key` axis + curated `App.<Term>` UI-noun namespace | Canonical RESO DD 2.0 `DisplayName` / `Definition` (global rows, `tenant_key=''`) | Tenant admins must re-label and translate UI terminology (EN/RU/HU) at runtime without mutating the RESO data model, EF `resource`, `pageKey`/route identifiers, or canonical corpus keys. Overrides are `source='team_override'` rows scoped by `tenant_key`; the global RESO truth is unchanged and is the fallback. UI nouns with no RESO resource use an `App.<Term>` key (`source='vendor_extension'`). | Accepted (2026-06-02). Deliverable: [ADR-020](../../../architecture/decisions/ADR-020.md). Served via tenant-aware merge in `reso-dd-descriptions`; written via `mls-sync` resource `reso_label_override` (emits `HistoryTransactional` — see [wiki/integration.md#history-emission](integration.md#history-emission)). |

If new deviations arise later (e.g. an attribute absent from RESO DD 2.0 but critical for luxury), they must be:

1. Justified by an ADR in `matrix-platform-kb/docs/architecture/decisions/`.
2. Recorded in `matrix-platform-kb/docs/data-models/platform-extensions.md` (with `x_` prefix and reason).
3. Listed here with a reference to the ADR.
4. Accompanied by a roll-back plan (for when/if RESO DD adds the corresponding canonical attribute).

Source: raw/context-v2.md §11.6.

## Resource map — canonical RESO → wiki section {#resource-map}

| Canonical RESO resource | KB doc | Used in this wiki |
|---|---|---|
| `Contacts` | [`reso-dd-kb/.../contacts.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/contacts.md) | [wiki/entities.md#contacts](entities.md#contacts), [wiki/requirements.md#fr-con-contacts](requirements.md#fr-con-contacts), [wiki/processes.md#contact-funnel](processes.md#contact-funnel) |
| `ContactListings` | [`reso-dd-kb/.../contact_listings.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/contact_listings.md) | [wiki/entities.md#contact-listings](entities.md#contact-listings), [wiki/requirements.md#fr-cl-contact-listings](requirements.md#fr-cl-contact-listings) |
| `ContactListingNotes` | [`reso-dd-kb/.../contact_listing_notes.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/contact_listing_notes.md) | [wiki/entities.md#contact-listing-notes](entities.md#contact-listing-notes) |
| `SavedSearch` | [`reso-dd-kb/.../saved_search.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/saved_search.md) | [wiki/entities.md#saved-search](entities.md#saved-search), [wiki/requirements.md#fr-pros-prospecting](requirements.md#fr-pros-prospecting) |
| `Prospecting` | [`reso-dd-kb/.../prospecting.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/prospecting.md) | [wiki/entities.md#prospecting](entities.md#prospecting), [wiki/requirements.md#fr-pros-prospecting](requirements.md#fr-pros-prospecting) |
| `Member` / `Office` / `OUID` / `Teams` / `TeamMembers` | [`reso-dd-kb/.../`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/) | [wiki/entities.md#member-office-team](entities.md#member-office-team) |
| `ShowingAvailability` / `ShowingRequest` / `ShowingAppointment` / `Showing` / `LockOrBox` | [`reso-dd-kb/.../showing.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/showing.md) | [wiki/entities.md#showing-chain](entities.md#showing-chain), [wiki/requirements.md#fr-show-showings](requirements.md#fr-show-showings) |
| `Caravan` / `CaravanStop` | [`reso-dd-kb/.../caravan.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/caravan.md) | [wiki/entities.md#caravan](entities.md#caravan), [wiki/requirements.md#fr-cara-caravan](requirements.md#fr-cara-caravan) |
| `TransactionManagement` | [`reso-dd-kb/.../transaction_management.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/transaction_management.md) | [wiki/entities.md#transaction-management](entities.md#transaction-management), [wiki/requirements.md#fr-tm-transactions](requirements.md#fr-tm-transactions) |
| `HistoryTransactional` | [`reso-dd-kb/.../history_transactional.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/history_transactional.md) | [wiki/entities.md#history-transactional](entities.md#history-transactional), [wiki/integration.md#history-emission](integration.md#history-emission) |
| `Property` | [`reso-dd-kb/.../property.md`](../../../data-models/reso-dd-kb/wiki/agent-docs/resources/property.md) | [wiki/entities.md#property](entities.md#property), [wiki/integration.md#listing-module](integration.md#listing-module) |

Source: raw/context-v2.md §11.2.

## Process map — canonical RESO processes → wiki section {#process-map}

| Canonical process | KB doc | Used in this wiki |
|---|---|---|
| Listing lifecycle | [`canonical-processes/processes/listing-lifecycle.md`](../../../business-processes/canonical-processes/processes/listing-lifecycle.md) | [wiki/processes.md#offer-to-closing](processes.md#offer-to-closing), [wiki/overview.md#pipeline](overview.md#pipeline), [wiki/integration.md](integration.md) |
| Showing lifecycle | [`canonical-processes/processes/showing-lifecycle.md`](../../../business-processes/canonical-processes/processes/showing-lifecycle.md) | [wiki/processes.md#showing-process](processes.md#showing-process), [wiki/requirements.md#fr-show-showings](requirements.md#fr-show-showings) |
| Caravan lifecycle | [`canonical-processes/processes/caravan-lifecycle.md`](../../../business-processes/canonical-processes/processes/caravan-lifecycle.md) | [wiki/requirements.md#fr-cara-caravan](requirements.md#fr-cara-caravan) |
| Lead → Contact lifecycle | [`canonical-processes/processes/lead-contact-lifecycle.md`](../../../business-processes/canonical-processes/processes/lead-contact-lifecycle.md) | [wiki/processes.md#contact-funnel](processes.md#contact-funnel) |
| Prospecting + SavedSearch delivery | [`canonical-processes/processes/prospecting-and-saved-search-delivery.md`](../../../business-processes/canonical-processes/processes/prospecting-and-saved-search-delivery.md) | [wiki/processes.md#property-matching](processes.md#property-matching), [wiki/requirements.md#fr-pros-prospecting](requirements.md#fr-pros-prospecting) |
| Transaction lifecycle | [`canonical-processes/processes/transaction-lifecycle.md`](../../../business-processes/canonical-processes/processes/transaction-lifecycle.md) | [wiki/processes.md#offer-to-closing](processes.md#offer-to-closing), [wiki/requirements.md#fr-tm-transactions](requirements.md#fr-tm-transactions), [wiki/integration.md#contract-system](integration.md#contract-system), [wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission), [wiki/integration.md#finance-erp-payments](integration.md#finance-erp-payments) |
| History & Audit log | [`canonical-processes/processes/history-and-audit-log.md`](../../../business-processes/canonical-processes/processes/history-and-audit-log.md) | [wiki/integration.md#history-emission](integration.md#history-emission), [wiki/overview.md#pipeline](overview.md#pipeline) |

Source: raw/context-v2.md §11.3.

## Crosswalk — previous BRD model → canonical RESO {#crosswalk}

```mermaid
flowchart LR
  L[Lead BRD entity] -- ContactType funnel --> CT["Contacts.ContactType=Lead → Prospect → ..."]
  O[Opportunity BRD entity] -- stored app-DB anchor + calculated stage --> P["opportunity + opportunity_link (App DB) → Contacts + SavedSearch + Prospecting + ContactListings + Showing chain + Caravan + Referral + TransactionManagement + Property.StandardStatus (ADR-035)"]
  OPI[Opportunity Property Interest] -- engagement --> CL["ContactListings + ContactListingPreference + ContactListingNotes"]
  OFF[Offer BRD entity] -- canonical --> TM["TransactionManagement + HistoryTransactional"]
  V[Viewing BRD entity] -- 5-resource chain --> SHC["ShowingAvailability → ShowingRequest → ShowingAppointment → Showing → LockOrBox"]
  CTR[Contract BRD entity] -- observable goal --> PS["Property.StandardStatus AUC → Pending → Closed + HistoryTransactional + external contract system"]
  COM[Commission BRD entity] -- observable goal --> ERP1["External Finance ERP + forecast in CRM"]
  PAY[Payment Event BRD entity] -- observable goal --> ERP2["External Finance ERP webhook → Property.StandardStatus + HistoryTransactional"]
```

Source: raw/context-v2.md §11.4.
