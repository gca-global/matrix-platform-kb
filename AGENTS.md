# Sharp Matrix Platform — Agent Knowledge Map

> This file is the **table of contents** for the Sharp Matrix Platform knowledge base.
> It is deliberately short. Each pointer leads to a deeper source of truth in `docs/`.
> When working in this repository, read this file first, then navigate to the relevant chapter.

## For LLMs — Start Here

Before building or modifying ANY Matrix App:

### Step 1: Read the App Template (mandatory)
→ `docs/platform/app-template.md` — dual-Supabase, SSO auth, permissions, RLS, UI patterns, token architecture

### Step 2: Determine App Type

| Question | → App Type | Example Repos | Read Next |
|----------|-----------|--------------|-----------|
| Does the app work with listings, contacts, agents, showings? | **CDL-Connected** | `/home/bitnami/matrix-pipeline`, `/home/bitnami/matrix-mls` | Steps 3a-3c below |
| Does the app have its own domain (HR, finance, IT ops)? | **Domain-Specific** | `/home/bitnami/matrix-hrms`, `/home/bitnami/matrix-fm`, `/home/bitnami/itsm-2-1` | Step 3d below |

### Step 3a (CDL-Connected): Read the CDL Schema
→ `docs/data-models/cdl-schema.md` — actual CDL tables (`properties`, `properties_published`, `property_media`, `cdl_staging.*`, MLS Sync control plane), 5-stage pipeline, EF contracts
→ `docs/data-models/dash-data-model.md` — Dash field names used as column names

### Step 3b (CDL-Connected): Understand Token Architecture (critical)

> **Updated Apr 2026 (ADR-012 / ADR-013):** SSO and CDL are **two
> separate Supabase projects**. CDL is configured with Supabase
> **Third-Party Auth** pointing at the SSO JWKS URL + issuer, so CDL
> PostgREST verifies SSO-issued ES256 tokens directly. There is no
> "Supabase native token" dance for the CDL anymore, and no
> `app_metadata` fallback on the CDL RLS helpers.

CDL-Connected apps hold a single token: the **SSO JWT** (custom claims,
ES256-signed). They send it as `Authorization: Bearer …` to:

- **SSO PostgREST** (`xgubaguglsnokjyudgvc`) — for roles, permissions, display names.
- **CDL PostgREST** (`ofzcokolkeejgqfjaszq`) — for direct anon reads of `public.properties_published` and the EFs (`mls-sync`, `mls-sync-orchestrator`, `listings-search`, the 5 pipeline stages).
- **SSO / CDL Edge Functions** — all `verify_jwt: false`; each function verifies the JWT against the SSO JWKS itself.
- **App DB PostgREST** (per-app) — unchanged.

**JWT signing**: SSO issues ES256 tokens. See `docs/architecture/decisions/ADR-011.md` (ES256 migration) and ADR-012 (Third-Party Auth boundary between SSO and CDL).

→ `docs/platform/security-model.md` — RLS helpers (JWT-only on CDL), claims, ES256 signing
→ `docs/architecture/decisions/ADR-012.md` — dedicated CDL project + Third-Party Auth

### Step 3c (CDL-Connected): CDL Write & Read Pattern
Writes to CDL go through Edge Functions deployed on the CDL project
itself (not the app's Supabase instance). Apps never hold a CDL
service-role key.

- **Listing reads (anon)**: `cdlAnonClient` → `public.properties_published` (RLS-gated: `is_visible AND NOT is_deleted`).
- **Filtered listing reads**: `cdlClient` → `listings-search` EF (POST with `q`, `filters`, `page`, `pageSize`, `sort`, `includeMedia`).
- **MLS Sync admin (per tenant)**: app → `mls-sync` *or* `mls-sync-orchestrator` EF (chosen by `mls_settings.sync_mode`). Same action surface (`get-settings`, `save-settings`, `list-jobs`, `start`, `cancel`, `test`, …).

### Step 3c′ (CDL-Connected): MLS Ingestion Pattern
All MLS data ingestion (external RESO Web API, our own `mls_2_0`
RESO API) funnels through the **5-stage pipeline** on the CDL project:

```
reso-import → field-mapping-apply → listing-merge → media-import → listing-publish
   ↓                ↓                     ↓               ↓                ↓
cdl_staging.    cdl_staging.        public.         public.          public.
listings_raw    listings_mapped     properties      property_media   properties_published
```

Each stage writes one row to `public.ingest_audit`. The orchestration
itself is owned by `mls-sync-orchestrator` (or by the lifted
`mls-sync` monolith for the cy-web-2v0-style direct-write path). See
[`docs/data-models/cdl-schema.md`](docs/data-models/cdl-schema.md)
and the implementation-status note in
[ADR-014](docs/architecture/decisions/ADR-014.md). CSV / CRM webhook
ingestion remains on the roadmap.

### Step 3c″ (CDL-Connected): Cross-project user display
Apps must NOT SQL-join CDL rows to `auth.users` or `sso_users`. Use the
`useUserDisplay` React hook from `matrix-apps-template`, which batches
IDs through the `resolve-users` SSO Edge Function.

### Step 3d (Domain-Specific): Read Domain-Specific Examples
→ `/home/bitnami/matrix-hrms` — HRMS: 25+ domain tables, 30+ hooks, multi-step vacation approval
→ `/home/bitnami/matrix-fm` — Financial Management: reporting, planning, Edge Function-backed reads/writes
→ `/home/bitnami/itsm-2-1` — ITSM: service desk tickets, CMDB, software assets, webhook ingestion

### Step 4: Read Relevant Business Processes
→ `docs/business-processes/listing-pipeline.md` — seller-side (8 stages)
→ `docs/business-processes/sales-pipeline.md` — buyer-side (8 stages)
→ `docs/business-processes/listing-checklist.md` — operational checklists

### Step 5 (as needed)
- Syndication/exports: `docs/data-models/dash-data-model.md` (RESO mapping column)
- Security deep-dive: `docs/platform/security-model.md`
- Deployment: `docs/platform/operations.md`
- GDPR/compliance: `docs/platform/compliance.md`
- **New app can't auth?**: `docs/platform/new-app-auth-troubleshooting.md` — 401/400/403 flowchart, stale sessions, Lovable preview issues

## Platform Identity

**Sharp Matrix** is the **technology platform** powering **Sharp SIR** (Sharp Sotheby's International Realty), a luxury real estate brokerage and SIR-network affiliate currently operating in **Cyprus**, **Hungary**, and **Kazakhstan** (more markets planned). Sharp Matrix comprises four module families that all share the CDL:

- **CRM** — `matrix-pipeline` (lead/opportunity/listing pipeline), `matrix-comms`, `matrix-client-connect`
- **FM** (Financial Management) — financial-entries, commissions, deal closings
- **HR** — `matrix-hrms`
- **MLS** — `matrix-atlas-mls`, `matrix-mls-2-0`, `matrix-cy-website`

**Source-of-record taxonomy** (`mls_sources.kind`):
- `internal` — `matrix-internal` (Atlas / `matrix-pipeline` / future broker apps); target state for all Sharp SIR markets.
- `legacy-internal` — `qobrix` (Cyprus legacy CRM, currently exposed as `mls.sharpsir.group` RESO Web API; **being decommissioned once Atlas runs CY listing creation**). Marked `is_sunsetting = true`. HU + KZ have no Phase-1 legacy seed — those Sharp SIR offices author directly in Anywhere Dash today (covered by the `dash` brand-network source).
- `brand-network` — `dash` (Anywhere Dash). **Primary bidirectional contract** as an SIR affiliate.
- `external` — third-party feeds (real estate developers, partner brokerages, future MLS exchanges); inbound only with restricted onward syndication per the partner's terms-of-use.

**Built with**: Lovable (app builder) + Supabase (CDL / system of record) + Databricks (DWH / ETL).
**Practical data model**: RESO DD 2.0 in storage (snake_case canonical names); Dash names projected via `v_dash_*` views (Phase-1 contract surface for the SIR network).
**App template**: `matrix-apps-template` — defines stack, auth, permissions, UI patterns.
**Strategic goal**: Matrix Apps (`matrix-pipeline` CRM + Atlas) replace Qobrix for Cyprus listing creation; Dash flips from inbound-only to bidirectional via `dash-import` / `dash-export` EFs (HU + KZ already author in Dash today).

## Knowledge Base Structure

```
docs/
├── GOLDEN_PRINCIPLES.md              ← Engineering invariants & taste rules (prevents entropy)
├── QUALITY_SCORE.md                  ← Domain quality grades (where to focus improvement)
├── INDEX.md                          ← Master index with chapter summaries
├── ARCHITECTURE.md                   ← System architecture & technology map
├── platform/
│   ├── index.md                      ← Platform overview & three-platform architecture
│   ├── app-template.md              ← How to build Matrix Apps (Lovable must read first)
│   ├── security-model.md            ← Auth, roles, permissions, RLS patterns, JWT claims
│   ├── sso-edge-functions.md        ← SSO Edge Function API contracts (38 functions)
│   ├── operations.md                ← CI/CD, deployment, monitoring, DR/backup
│   ├── compliance.md                ← GDPR, data protection, retention, DSAR procedures
│   ├── mls-datamart.md              ← MLS 2.0 data pipeline & phased migration roadmap
│   ├── new-app-auth-troubleshooting.md ← Troubleshooting new app auth (401/400/403)
│   ├── alignment-audit-playbook.md   ← Harness-style audit: kill schema↔code↔UI drift
│   ├── ecosystem-architecture.md     ← Full ecosystem: channels, apps, data, AI/ML
│   ├── app-catalog.md               ← All platform apps (11 live, 7 in progress, 6 planned)
│   ├── performance.md              ← Latency targets (p99 ≤ 20ms property read), index strategy, capacity planning
│   ├── mobile-strategy.md           ← PWA, responsive design, offline requirements
│   └── kb-methodology.md            ← KB design, versioning, entropy management, doc gardening
├── architecture/
│   ├── intelligence-layer.md        ← Phase-2 roadmap: semantic + algebraic search, recsys, MCP, syndication
│   ├── data-distribution-and-stewardship.md  ← Phase-2.5 roadmap: source-of-record & listing lifecycle, channel distribution rules, multi-source merge precedence, field-level overrides (locked_fields)
│   └── decisions/                   ← ADRs (numbered, immutable)
├── exec-plans/
│   ├── index.md                      ← Execution plan format, lifecycle, usage guide
│   ├── tech-debt-tracker.md          ← Known technical debt by domain with severity
│   ├── active/                       ← Currently in-progress execution plans
│   └── completed/                    ← Archived finished plans
├── vision/
│   ├── index.md                      ← Vision chapter index
│   ├── digital-strategy-2026-2028.md ← Digital strategy: 3 markets, 7 phases, KPIs
│   ├── ai-driven-sales-model.md      ← AI-driven sales management model (16 elements)
│   └── core-beliefs.md              ← Operating principles & design philosophy
├── data-models/
│   ├── index.md                      ← Data models chapter index (Dash-first hierarchy)
│   ├── dash-data-model.md           ← Dash/Anywhere.com practical data model (START HERE)
│   ├── reso-dd-overview.md           ← RESO DD 2.0 — interop standard for syndication
│   ├── reso-canonical-schema.md      ← Which RESO resources/fields map to Dash
│   ├── platform-extensions.md        ← All x_sm_* fields not in Dash or RESO DD
│   ├── cdl-schema.md            ← Common Data Layer for Sharp Matrix apps (cross-app data; today: listings + ingestion + MLS Sync control plane)
│   ├── etl-pipeline.md              ← Bronze/Silver/Gold ETL pipeline architecture
│   ├── data-quality.md              ← Data quality verification, validation, reporting
│   ├── reso-web-api.md              ← RESO Web API (OData 4.0) endpoint reference
│   ├── qobrix-data-model.md          ← Qobrix CRM reference & migration source
│   └── property-field-mapping.md     ← Field mapping: Dash ↔ RESO ↔ Qobrix ↔ SIR
├── business-processes/
│   ├── index.md                      ← Business processes chapter index
│   ├── listing-pipeline.md           ← Seller-side pipeline (8 stages)
│   ├── sales-pipeline.md             ← Buyer-side pipeline (8 stages)
│   ├── lead-qualification.md         ← MQL → SQL qualification with BANT
│   ├── follow-up-vs-active-sales.md  ← Nurturing vs active deal boundary
│   └── listing-checklist.md          ← Operational checklists (broker/marketing/finance)
├── product-specs/
│   ├── index.md                      ← Product specs chapter index
│   ├── sir-listing-forms.md          ← SIR/Anywhere.com form field specifications
│   ├── broker-dashboard.md           ← AI-powered broker dashboard design
│   ├── manager-kanban.md             ← Manager pipeline & Kanban views
│   ├── personalization.md            ← Personalization & recommendation engine (Phase 4)
│   ├── client-portal.md              ← Buyer/seller self-service portal
│   ├── contact-center.md             ← Lead processing and routing system
│   ├── marketing-platform.md        ← Campaign management and marketing automation
│   └── personas.md                   ← User personas for UX decisions
├── references/
│   ├── index.md                      ← References chapter index
│   ├── qobrix-api-summary.md         ← Qobrix OpenAPI resource catalog
│   └── reso-dd-fields-summary.md     ← RESO DD 2.0 field & lookup summary
scripts/
└── validate-kb.sh                    ← Mechanical KB validation (links, refs, IDs, staleness)
```

## For Zoe AI Assistant (1st & 2nd Line Support)

If you are the Zoe AI assistant providing end-user or 2nd-line support, read:

→ `docs/zoe-ai-assistant-kb/index.md` — KB index and usage guide
→ `docs/zoe-ai-assistant-kb/platform-overview.md` — Start here for general questions

**1st Line (end-user facing):** Navigate to the relevant app article:
- `docs/zoe-ai-assistant-kb/portal.md` — Agency Portal
- `docs/zoe-ai-assistant-kb/client-connect.md` — Client Connect
- `docs/zoe-ai-assistant-kb/meeting-hub.md` — Meeting Hub
- `docs/zoe-ai-assistant-kb/comms.md` — Matrix Comms (WhatsApp)
- `docs/zoe-ai-assistant-kb/pipeline.md` — Matrix Pipeline (CRM, leads, deals, contacts)
- `docs/zoe-ai-assistant-kb/hrms.md` — Matrix HR Management (employees, vacations, onboarding)
- `docs/zoe-ai-assistant-kb/itsm.md` — ITSM (IT service desk, assets, licenses)
- `docs/zoe-ai-assistant-kb/financial-management.md` — Matrix Financial Management (reporting, budgets, planning)
- `docs/zoe-ai-assistant-kb/platform-sso-auth.md` — SSO, Login, Roles, Permissions

**2nd Line (technical):**
- `docs/zoe-ai-assistant-kb/second-line-tech-reference.md` — Architecture, tech stack, and links to deep-dive docs

**Generating new KB articles:**
- `docs/zoe-ai-assistant-kb/kb-generation-guide.md` — How to create a support KB article for any new app

## Quick Navigation by Task

| If you need to…                              | Read this                                         |
|----------------------------------------------|---------------------------------------------------|
| Build a new Matrix App (start here)          | `docs/platform/app-template.md`                   |
| Understand the Sharp Matrix platform          | `docs/platform/index.md`                          |
| See the full ecosystem architecture           | `docs/platform/ecosystem-architecture.md`         |
| Understand the data pipeline (MLS 2.0)        | `docs/platform/mls-datamart.md`                   |
| Know which apps exist and their status        | `docs/platform/app-catalog.md`                    |
| Understand the 2026-2028 strategy & roadmap   | `docs/vision/digital-strategy-2026-2028.md`       |
| Understand the AI-driven sales model          | `docs/vision/ai-driven-sales-model.md`            |
| Know the design philosophy                    | `docs/vision/core-beliefs.md`                     |
| See how systems connect                       | `docs/ARCHITECTURE.md`                            |
| See Dash field names for app development       | `docs/data-models/dash-data-model.md`             |
| Map a property field across systems            | `docs/data-models/property-field-mapping.md`      |
| See which RESO fields map to Dash              | `docs/data-models/reso-canonical-schema.md`       |
| Find or add a platform extension (x_sm_*)     | `docs/data-models/platform-extensions.md`         |
| See the CDL schema (cross-app data layer; properties + ingestion + MLS Sync) | `docs/data-models/cdl-schema.md`              |
| Understand the ETL pipeline (Bronze→Gold)     | `docs/data-models/etl-pipeline.md`                |
| Use the RESO Web API (OData)                  | `docs/data-models/reso-web-api.md`                |
| Understand Qobrix entities & migration        | `docs/data-models/qobrix-data-model.md`           |
| Understand RESO DD 2.0 (interop standard)      | `docs/data-models/reso-dd-overview.md`            |
| Understand auth, roles, permissions, RLS       | `docs/platform/security-model.md`                 |
| Understand ES256 JWT migration from HS256      | `docs/architecture/decisions/ADR-011.md`          |
| See SSO Edge Function API contracts            | `docs/platform/sso-edge-functions.md`             |
| Deploy an app or Edge Function                | `docs/platform/operations.md`                     |
| Performance targets, capacity planning        | `docs/platform/performance.md`                   |
| Plan Phase-2 AI / semantic search / recsys / MCP | `docs/architecture/intelligence-layer.md`     |
| Plan Phase-2.5 source-of-record / listing lifecycle / channel distribution / field overrides / multi-source merge | `docs/architecture/data-distribution-and-stewardship.md` |
| Mobile strategy (PWA, offline)                | `docs/platform/mobile-strategy.md`                |
| Test Matrix Apps (unit, E2E, contract)         | `docs/platform/testing-strategy.md`               |
| Run an alignment / drift audit on an app       | `docs/platform/alignment-audit-playbook.md`       |
| Edge Function API contracts                   | `docs/platform/api-contracts.md`                  |
| Handle GDPR, data retention, DSARs            | `docs/platform/compliance.md`                     |
| Understand KB methodology and contribution   | `docs/platform/kb-methodology.md`                 |
| See engineering invariants & taste rules      | `docs/GOLDEN_PRINCIPLES.md`                       |
| See quality grades by domain                  | `docs/QUALITY_SCORE.md`                           |
| See execution plans (active, completed)       | `docs/exec-plans/index.md`                        |
| See known technical debt                      | `docs/exec-plans/tech-debt-tracker.md`            |
| Validate KB structure and links               | `scripts/validate-kb.sh`                          |
| Verify data quality in the pipeline           | `docs/data-models/data-quality.md`                |
| Build a listing workflow                      | `docs/business-processes/listing-pipeline.md`     |
| Build a buyer/sales workflow                  | `docs/business-processes/sales-pipeline.md`       |
| Implement lead scoring / qualification        | `docs/business-processes/lead-qualification.md`   |
| Design the broker dashboard UI                | `docs/product-specs/broker-dashboard.md`          |
| Design listing input forms                    | `docs/product-specs/sir-listing-forms.md`         |
| Build Client Portal, Contact Center, Marketing | `docs/product-specs/client-portal.md`, etc.      |
| Use user personas for UX                     | `docs/product-specs/personas.md`                  |
| Look up Qobrix API endpoints                  | `docs/references/qobrix-api-summary.md`           |
| Look up RESO standard field names             | `docs/references/reso-dd-fields-summary.md`       |

## Source Repos & Files

| Repo / File | Format | Contents |
|------------|--------|---------|
| `/home/bitnami/matrix-apps-template` | React/TS | App template: dual-Supabase, SSO, permissions, RLS, UI |
| `/home/bitnami/matrix-hrms` | React/TS | HRMS app (Domain-Specific, 25+ tables, vacations, onboarding, performance) |
| `/home/bitnami/matrix-pipeline` | React/TS | Pipeline CRM app (CDL-Connected, leads, opportunities, contacts, M365) |
| `/home/bitnami/itsm-2-1` | React/TS | ITSM app (Domain-Specific, service desk, CMDB, software assets, vendors) |
| `/home/bitnami/matrix-fm` | React/TS | Financial Management app (Domain-Specific, reporting, budgets, planning, CORE) |
| `/home/bitnami/matrix-mls` | React/TS | MLS Listing Management app (CDL-Connected via the `properties_published` snapshot + `listings-search` EF; per-broker tables on the matrix-mls app DB). **Cursor-managed, not Lovable-linked** — see ADR-013. |
| `/home/bitnami/matrix-atlas-mls` | React/TS | Atlas — MLS Sync admin & Listings Search consumer (CDL-Connected). Calls `mls-sync` / `mls-sync-orchestrator` and `listings-search` EFs on the CDL project. |
| `/home/bitnami/mls_2_0` | Python/FastAPI | MLS 2.0 pipeline: Databricks ETL + RESO Web API |
| `vision/Sharp-Sothebys-International-Realty.pdf` | PDF | Full 28-slide digital strategy 2026-2028 |
| `vision/Sarp SIR Platform-2026-02-18-125014.mmd` | Mermaid | Platform ecosystem architecture diagram |
| `vision/AI-driven-model-upravleniya-prodazhami.pdf` | PDF | 16-slide AI-driven sales model |
| `qobrix/qobrix_openapi.yaml` | YAML | Full Qobrix OpenAPI 3.0 spec (68K lines) |
| `reso dd/RESO_Data_Dictionary_2.0.xlsx` | XLSX | RESO DD 2.0 (Fields + Lookups) |
| `reso dd/RESO_Data_Dictionary_1.7.xlsx` | XLSX | RESO DD 1.7 (historical reference) |
| `dash/BlankForm_*.docx` | DOCX | SIR/Anywhere.com listing forms (6 types) |
| `current busienss practice/*.xlsx` | XLSX | Listing checklists 2024–2026 |
