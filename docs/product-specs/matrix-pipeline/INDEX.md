# `matrix-pipeline` wiki — Index

> Content-oriented catalog. Read this first when answering a query — drill into the wiki page that owns the relevant anchor.
> See [`AGENTS.md`](AGENTS.md#how-to-load-context-for-a-query) for the load order.

## Pages

| Page | Purpose | Sources from `raw/context-v2.md` |
|---|---|---|
| [`wiki/overview.md`](wiki/overview.md) | Scope, design principles, personas, KPIs, pipeline-as-UI-projection, RESO policy | §1, §2, §3, §4, §7, §11.1 |
| [`wiki/architecture.md`](wiki/architecture.md) | Three-Supabase, CDL access pattern, identity boundary, live CDL state, Phase 2+ migration, RESO compliance gates, escape hatch | §5a, §11 |
| [`wiki/entities.md`](wiki/entities.md) | Business entities (15 canonical RESO + Referral) | §5, §9.1, §9.2, §9.3, §9.5a, §9.7, §9.7a, §9.8, §9.9, §9.11a |
| [`wiki/processes.md`](wiki/processes.md) | End-to-end business processes (6) | §6, §9.4 |
| [`wiki/requirements.md`](wiki/requirements.md) | Business requirements + Functional requirements (non-AI, non-commission) | §8, §9.1–§9.12 |
| [`wiki/ai.md`](wiki/ai.md) | AI Copilot — 14 features + implementation plan | §9.13, §9.14 |
| [`wiki/integration.md`](wiki/integration.md) | External integrations: Listing Module, Contract system, Finance ERP, SSO, CDL | §10 |
| [`wiki/commission-engine.md`](wiki/commission-engine.md) | CRM-internal ERP-lite for sales-broker P&L + reconciliation | §9.15 |
| [`cdl-crud-contract.md`](cdl-crud-contract.md) | Lovable CDL CRUD contract — 5 recipe shapes + 6 commandments. Canonical copy synced from `mem://infrastructure/lovable-cdl-crud-contract.md` | (operational) |
| [`phases.md`](phases.md) | 8-week atomic build plan (Lovable + Cursor swimlanes) | (plan) |
| [`raw/context-v2.md`](raw/context-v2.md) | Immutable BRD (read for provenance only) | — |
| [`log.md`](log.md) | Chronological append-only log | — |
| [`AGENTS.md`](AGENTS.md) | LLM schema layer | — |

## Anchors by topic

### Overview ([`wiki/overview.md`](wiki/overview.md))

- `#scope` — In/Out scope, CRM↔Listing Module boundary
- `#principles` — Design principles
- `#personas` — Users and roles
- `#kpis` — Measurable outcomes
- `#pipeline` — Pipeline as canonical-state projection (5 stages)
- `#reso-policy` — Strict RESO DD 2.0 compliance policy

### Architecture ([`wiki/architecture.md`](wiki/architecture.md))

- `#three-supabase` — SSO + CDL + CRM app DB
- `#identity-boundary` — SSO vs CDL Member roster
- `#cdl-access-pattern` — CRM as CDL client (EFs, never direct PostgREST)
- `#live-cdl-state` — As-built CDL state (MCP-refreshed)
- `#phase-2-migration` — Tables planned for CDL migration
- `#app-private-state` — Always-app-private (never CDL)
- `#kb-sources-of-truth` — Where to look for canonical KB docs
- `#compliance-gates` — Schema / Status / Audit / Roster / Integration / AI / CDL access / Pipeline gates
- `#escape-hatch` — Allowed deviations from canonical RESO (Referral, Commission Engine, OpenHouse-removed)
- `#resource-map` — RESO resource → wiki / phase mapping
- `#process-map` — Canonical RESO process → wiki section
- `#crosswalk` — Previous BRD model → canonical RESO

### Entities ([`wiki/entities.md`](wiki/entities.md))

- `#contacts` — Person record (canonical Contacts; ContactType graduation)
- `#contact-listings` — Engagement junction (Contact × Property)
- `#contact-listing-notes` — Notes on a Contact × Property pair
- `#saved-search` — Buyer search criteria
- `#prospecting` — Outreach schedule + broker reminder driver
- `#showing-chain` — 5-resource Showing chain (Availability → Request → Appointment → Showing → LockOrBox)
- `#caravan` — Curated multi-property tour
- `#transaction-management` — Offer + lifecycle (Purchase/Lease offer)
- `#history-transactional` — Audit event log
- `#referral` — Project-flavour entity (escape hatch)
- `#property` — Read-only canonical (mastered by Listing Module)
- `#activity` — Tasks, follow-ups, broker touchpoint reminders
- `#document` — Document references (files in external storage)
- `#campaign` — Marketing campaign (LeadSource link)
- `#member-office-team` — Canonical RESO business roster (CDL-mastered)

### Processes ([`wiki/processes.md`](wiki/processes.md))

- `#contact-funnel` — Lead → Buyer/Seller graduation (§6.1, §9.4)
- `#contact-relationship` — Long-term engagement (§6.2)
- `#property-matching` — Buyer ↔ Listing alignment (§6.3)
- `#showing-process` — 5-resource chain (§6.4)
- `#offer-to-closing` — TM lifecycle to deal close (§6.5)
- `#referral-lifecycle` — Inbound + outbound referral outcomes

### Requirements ([`wiki/requirements.md`](wiki/requirements.md))

- `#br` — Business Requirements (§8)
- `#fr-con-contacts` — Contacts (FR-CON-01..20)
- `#fr-pc-split` — Personal/Commercial split (FR-PC-01..05, FR-COM-01..03)
- `#fr-cfl-contact-funnel-lifecycle` — Funnel graduation (FR-CFL-01..05)
- `#fr-fnl-funnel-canonical` — Funnel canonical projection (FR-FNL-01..26)
- `#fr-pros-prospecting` — SavedSearch + Prospecting (FR-PROS-01..13)
- `#fr-act-activities` — Activities (FR-ACT-01..11)
- `#fr-show-showings` — Showing chain (FR-SHOW-01..11)
- `#fr-cara-caravan` — Caravan (FR-CARA-01..06)
- `#fr-cl-contact-listings` — ContactListings (FR-CL-01..10)
- `#fr-tm-transactions` — TransactionManagement (FR-TM-01..14)
- `#fr-cmm-communications` — Communications (FR-CMM-01..05)
- `#fr-doc-documents` — Documents (FR-DOC-01..05)
- `#fr-ref-referral` — Referral (FR-REF-01..08)
- `#fr-rep-reporting` — Reports & dashboards (FR-REP-01..05)

### AI ([`wiki/ai.md`](wiki/ai.md))

- `#overview` — AI Copilot purpose + cross-feature contracts
- `#lead-qualification` — FR-AI-LQ
- `#match-explanation` — FR-AI-MAT
- `#showing-coach` — FR-AI-SHOW
- `#communication-drafting` — FR-AI-COM
- `#deal-margin-coach` — FR-AI-MAR (§9.13.9a)
- `#activity-prioritization` — FR-AI-ACT
- `#price-positioning` — FR-AI-PRICE
- `#client-sentiment` — FR-AI-SENT
- `#deal-summarization` — FR-AI-SUM
- `#document-drafting` — FR-AI-DOC
- `#recommendation-engine` — FR-AI-REC
- `#transaction-risk` — FR-AI-RISK
- `#prospecting-template-gen` — FR-AI-PROS
- `#implementation-plan` — §9.14 rollout plan

### Integration ([`wiki/integration.md`](wiki/integration.md))

- `#listing-module` — Property feed + StandardStatus push (§10.1–10.6)
- `#history-emission` — HistoryTransactional contract (§10.7)
- `#contract-system` — External e-signature provider (§10.8)
- `#finance-erp-commission` — Commission ledger reconciliation (§10.9)
- `#finance-erp-payments` — Payment events reconciliation (§10.10)
- `#sso` — Identity, roles, groups, scope claims
- `#cdl` — CRM-as-CDL-client pattern + dedicated EFs

### CDL CRUD contract ([`cdl-crud-contract.md`](cdl-crud-contract.md))

- `#two-clients` — `ssoClient` / `cdlClient` / `appClient` setup
- `#read-a` — direct PostgREST on CDL (anon SELECT `qual=true` tables)
- `#read-b` — `listings-search` EF (broker-scope, properties)
- `#read-c` — per-resource Pipeline read EFs (planned, placeholder)
- `#write-a` — CRM app DB writes (default for everything today)
- `#write-b` — per-resource Pipeline write EFs (planned, placeholder)
- `#commandments` — the six rules Lovable always applies
- `#quick-reference` — recipe per RESO resource
- `#ef-ship-checklist` — what to update when a platform EF lands
- `#anti-patterns` — code patterns Lovable refuses to generate

### Commission Engine ([`wiki/commission-engine.md`](wiki/commission-engine.md))

- `#overview` — Business goal (sales-broker P&L visibility)
- `#scope` — Inside CRM (forecast + rule) vs outside (Finance ERP for actuals)
- `#data-model-stub` — Conceptual entities (DealCostEvent, CostRateCard, CommissionRule, DealPnL, BrokerCompensation) — design completed during Phase 5 in Lovable
- `#reconciliation` — Variance vs external Finance ERP
- `#deviation` — Why this is in CRM (escape hatch reference)

### Phases ([`phases.md`](phases.md))

- `#governance` — Atomicity rule + DoD
- `#week-0` — Phase 0: Foundation
- `#week-1` — Phase 1: Contacts & Org Roster
- `#week-2` — Phase 2: SavedSearch + Prospecting
- `#week-3` — Phase 3: ContactListings + Showings + Caravan
- `#week-4` — Phase 4: TransactionManagement + Offer-to-Closing + Referral
- `#week-5` — Phase 5: Pipeline projection + Commission Engine
- `#week-6` — Phase 6: AI Copilot
- `#week-7` — Phase 7: Staging hardening + Demo

## Quick reference — by RESO resource

| Resource | Wiki anchor | KB doc |
|---|---|---|
| `Contacts` | `wiki/entities.md#contacts` | [`reso-dd-kb/wiki/agent-docs/resources/contacts.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/contacts.md) |
| `ContactListings` | `wiki/entities.md#contact-listings` | [`reso-dd-kb/.../contact_listings.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/contact_listings.md) |
| `ContactListingNotes` | `wiki/entities.md#contact-listing-notes` | [`reso-dd-kb/.../contact_listing_notes.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/contact_listing_notes.md) |
| `SavedSearch` | `wiki/entities.md#saved-search` | [`reso-dd-kb/.../saved_search.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/saved_search.md) |
| `Prospecting` | `wiki/entities.md#prospecting` | [`reso-dd-kb/.../prospecting.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/prospecting.md) |
| `Member`, `Office`, `OUID`, `Teams`, `TeamMembers` | `wiki/entities.md#member-office-team` | [`reso-dd-kb/.../`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/) |
| `ShowingAvailability/Request/Appointment/Showing/LockOrBox` | `wiki/entities.md#showing-chain` | [`reso-dd-kb/.../showing.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/showing.md) |
| `Caravan`, `CaravanStop` | `wiki/entities.md#caravan` | [`reso-dd-kb/.../caravan.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/caravan.md) |
| `TransactionManagement` | `wiki/entities.md#transaction-management` | [`reso-dd-kb/.../transaction_management.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/transaction_management.md) |
| `HistoryTransactional` | `wiki/entities.md#history-transactional` | [`reso-dd-kb/.../history_transactional.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/history_transactional.md) |
| `Property` | `wiki/entities.md#property` | [`reso-dd-kb/.../property.md`](../../data-models/reso-dd-kb/wiki/agent-docs/resources/property.md) |
