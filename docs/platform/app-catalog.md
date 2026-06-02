# Sharp Matrix Platform — App Catalog

> All applications and platform components in the Sharp Matrix ecosystem, with current delivery status.
> Last updated: April 2026
>
> **Development model**: Most Matrix business apps are **Lovable-managed projects** — changes flow through structured Lovable prompts, not direct code edits. SSO/CDL Edge Functions and database migrations are managed directly. See [app-template.md — Lovable-Managed Apps](app-template.md#lovable-managed-apps--development--maintenance-model) for details.
>
> **Exceptions (Cursor-managed, not Lovable-linked):**
> - `matrix-mls` (app DB `wckwfbbqiupvallmhqbu`) — detached from Lovable after the CDL cutover (ADR-013/014). Changes go through Cursor + git directly.
> - `matrix-cdl-studio` — **retired** as a write surface (see `matrix-cdl-studio/RETIREMENT.md`). Any future CDL inspector must be read-only with the CDL anon key.

## Delivery Status Summary

### Done (Live)

| # | Component | KB Name | Type | Primary Users |
|---|-----------|---------|------|---------------|
| 1 | Identity & Access Management | **SSO Console** | Platform | Admins |
| 2 | Home Dashboard & App Launcher | **Agency Portal** | App | Everyone |
| 3 | App Builder Starter Kit | **App Builder Template** | Infrastructure | Developers (Lovable) |
| 4 | Contact Registration | **Client Connect** | App | Brokers, Contact Center, Sales Managers |
| 5 | Meeting Registration | **Meeting Hub** | App | Brokers, Sales Managers |
| 6 | WhatsApp & Messaging | **Matrix Comms** | App | Brokers, Marketing, Sales |
| 7 | Data Warehouse & MLS Pipelines | **EDW + MLS Pipelines** | Infrastructure | Data Engineers, BI |
| 8 | Public Website & CMS | **Website CMS** | App | Content Managers |
| 9 | AI Assistant for Web Channel | **AI Web Assistant** | AI Service | Website visitors |
| 10 | AI Assistant for Internal Support | **Zoe AI Assistant** | AI Service | All internal users (multi-role) |
| 11 | AI Assistant for Blog Generation | **AI Blog Generator** | AI Service | Marketing, Content Managers |
| 11a | MLS Data Studio (CDL admin) | **Matrix Atlas (`matrix-atlas-mls`)** | App (CDL admin, served at `/mls`) | Data ops, system_admin / org_admin |

> **Atlas** is the Lovable-managed CDL admin SPA that drives `mls-sync` / `mls-sync-orchestrator` / `listings-search`. It's the operator UI for the 5-stage ingestion pipeline + the 8 RESO resource toggles + the source-of-record / lifecycle taxonomy + the data-stewardship `locked_fields` surface. See [`cdl-schema.md`](../data-models/cdl-schema.md) and the matrix-atlas-mls repo. Production path: `https://intranet.sharpsir.group/mls/`.

### In Progress

| # | Component | KB Name | Type | Primary Users |
|---|-----------|---------|------|---------------|
| 12 | Pipeline Management | **Matrix Pipeline** | App (CDL-Connected) | Brokers, Sales Managers, Call Center Staff |
| 13 | Contact Management | **Contact Management** | App (CDL-Connected) | Brokers, Sales Managers, Contact Center |
| 14 | IT Service & Asset Management | **ITSM** | App (Domain-Specific) | IT Staff, All internal users |
| 15 | Human Resources Management | **HRMS** | App (Domain-Specific) | All Employees, HR, Managers, Finance |
| 16 | Financial Management | **Matrix FM** | App (Domain-Specific) | Finance Team, Entity Managers, Senior Mgmt |
| 17 | Integration Management for External MLS and Portals | **Integration Management** | App / Service | Data Engineers, Admins |
| 18 | Notification Management | **Notification Management** | App / Service | All internal users, Admins |

### Planned

| # | Component | KB Name | Type | Primary Users |
|---|-----------|---------|------|---------------|
| 19 | Buyer/Seller Self-Service | **Client Portal** | App (CDL-Connected) | Buyers, Sellers |
| 20 | Campaign & Marketing Automation | **Marketing App** | App (CDL-Connected) | Marketing Team |
| 21 | Leadership KPI Dashboards | **BI Dashboard** | App | Leadership (CDSO, CDTO) |
| 22 | Platform Configuration | **Admin Console** | App | System Admins |

> **Consolidation note**: the previously-planned **Broker App** (daily dashboard + AI copilot) and **Manager App** (Kanban + analytics) are **consolidated into matrix-pipeline 2.0** as a single CRM serving both broker and manager personas (see [`product-specs/matrix-pipeline/wiki/personas`](../product-specs/matrix-pipeline/wiki/overview.md#personas) and [`phases.md`](../product-specs/matrix-pipeline/phases.md)). The canonical 5-stage funnel projection (Qualification → Matching → Viewing → Contracting → Payment) replaces both the old broker daily-dashboard view and the old manager Kanban as a single funnel-state UI projection.

---

## App Details — Done (Live)

### SSO Console (Identity & Access Management)
**Status**: Done
**Users**: System administrators
**URL**: `/sso-console/`
**Key Features**:
- OAuth 2.0 + PKCE authentication with custom JWT
- RBAC (role-based access control) with 5-level scope
- User and group management
- App registration and permissions
- AD user synchronization
- "Act As" role switching for testing

### Agency Portal
**Status**: Done
**Users**: All Sharp Sotheby's staff
**URL**: `/agency-portal/`
**Key Features**:
- Central dashboard with KPI widgets (pipeline value, clients, meetings)
- App launcher with role-based visibility
- AI Advisor chat (powered by Zoe)
- Quick Access navigation bar
- Stats aggregation from Client Connect, Meeting Hub, and other apps
- Multi-language support (EN/RU)

### App Builder Template
**Status**: Done
**Repo**: `/home/bitnami/matrix-apps-template-2-1` (canonical; the prior `/home/bitnami/matrix-apps-template` is obsolete — do not use or update)
**Key Features**:
- Vite + React 18 + TypeScript + shadcn/ui starter kit
- Dual-Supabase architecture (SSO + App DB)
- OAuth 2.0 + PKCE authentication flow
- 5-level scope permissions with CRUD strings
- ProtectedRoute with `requiredPage` checks
- SidebarLayout, i18n (EN/RU), Sharp design system (Navy palette, Playfair Display + Inter)
- TanStack React Query data fetching patterns

### Client Connect (Contact Registration)
**Status**: Done
**Users**: Brokers, Contact Center (MLS Staff), Sales Managers
**URL**: `/client-connect/`
**Key Features**:
- Register new buyer, seller, tenant, and landlord leads
- Multi-step registration with role-specific forms
- MLS duplicate detection and deduplication
- Client verification and approval pipeline (Draft → Verified → Approved)
- RFI (Request for Information) workflow
- Role-based data visibility (self → team → global)

### Meeting Hub (Meeting Registration)
**Status**: Done
**Users**: Brokers, Sales Managers
**URL**: `/meeting-hub/`
**Key Features**:
- Record and manage appointments (buyer, seller, tenant, landlord)
- Four meeting types with dedicated forms
- Meeting analytics and reporting
- Calendar integration
- Role-based data visibility

### Matrix Comms (WhatsApp & Messaging)
**Status**: Done
**Users**: Brokers, Marketing, Sales
**URL**: `/comms/`
**Powered by**: Twilio + Meta WhatsApp Business API
**Key Features**:
- WhatsApp Business messaging (1:1 conversations)
- Pre-approved message templates with variable substitution
- Bulk campaigns to contact segments
- AI-powered reply suggestions
- Quick replies and snippets
- Conversation history and context
- Webhook-based real-time message delivery

### EDW + MLS Pipelines (Databricks)
**Status**: Done
**Repo**: `/home/bitnami/mls_2_0`
**Key Features**:
- Medallion architecture: Bronze → Silver → Gold (RESO DD 2.0)
- Ingests from Qobrix API (Cyprus), DASH API (Kazakhstan), DASH FILE (Hungary)
- CDC every 15 minutes for incremental updates
- Gold layer sync to Supabase CDL
- Data quality verification and validation reporting
- RESO Web API (OData 4.0) exposure for external consumers

### Website CMS
**Status**: Done
**Users**: Content managers
**Supabase Instance**: `yugymdytplmalumtmyct` (CY Web Site)
**Key Features**:
- Public website content management and SEO optimization
- Property listing pages synced from CDL
- Lead capture integration with AI Web Assistant
- Multi-language content (EN/RU)

### AI Web Assistant
**Status**: Done
**Users**: Website visitors (anonymous and authenticated)
**Powered by**: RagChat / Humatic AI
**Key Features**:
- Conversational AI embedded on public website
- Property search assistance and recommendations
- Lead capture via webhook (name, email, phone, notes, transcript)
- Visitor context: IP geolocation, device, language, referrer
- Automatic lead routing to Client Connect / Contact Management

### Zoe AI Assistant (Internal Multi-Role Support)
**Status**: Done
**Users**: All internal users (brokers, managers, admins, support staff)
**Key Features**:
- 1st line support: how-to guidance, troubleshooting, incident triage
- 2nd line support: architecture context, deep-dive doc pointers, incident qualification
- RAG-powered knowledge retrieval from platform KB
- Multi-role awareness (adapts responses to broker vs. manager vs. admin)
- Cross-app workflow guidance
- Incident reporting assistance

### AI Blog Generator
**Status**: Done
**Users**: Marketing team, Content Managers
**Key Features**:
- AI-powered blog article generation for real estate content
- SEO-optimized output
- Multi-language generation (EN/RU)
- Integration with Website CMS publishing workflow

---

## App Details — In Progress

### Pipeline Management (Matrix Pipeline)
**Status**: In Progress (rebuild on the matrix-pipeline 2.0 spec)
**Spec (single source of truth)**: [`product-specs/matrix-pipeline/`](../product-specs/matrix-pipeline/INDEX.md) — wiki + phases + cdl-crud-contract
**Users**: Brokers, Sales Managers, Call Center Staff, Listing Coordinators, Marketing, Finance
**RESO Resources** (canonical, strict DD 2.0): `Property`, `Media`, `Contacts`, `Member`, `Office`, `OUID`, `Teams`, `TeamMembers`, `SavedSearch`, `Prospecting`, `Activity`, `ContactListings`, `ContactListingPreference`, `ContactListingNotes`, `ShowingAvailability`, `ShowingRequest`, `ShowingAppointment`, `Showing`, `LockOrBox`, `Caravan`, `CaravanStop`, `TransactionManagement`, `HistoryTransactional`, `Document`, `Field`, `Lookup`, `OpenHouse`, `InternetTracking`, `PropertyDetailAttachment`, plus a documented project-flavour `Referral` entity (one of two escape hatches).
**App Type**: CDL-Connected (canonical reads + writes via dedicated CDL EFs under SSO JWT)
**Supabase Instance**: `mydojctcewxrbwjckuyz` (CRM app DB — app-private state only: drafts, workflow cache, Commission Engine ERP-lite tables)
**Repo**: `sharpsir-group/matrix-pipeline-2-0` (GitHub, Lovable-managed) — local checkout `/home/bitnami/matrix-pipeline-2-0`. Supersedes the retired `sharpsir-group/smpipeline` repo (old local checkout `/home/bitnami/matrix-pipeline` has been removed).
**Production path**: `https://intranet.sharpsir.group/pipeline/` (Apache htdocs `/opt/bitnami/apache/htdocs/pipeline`).
**Deploy**: auto-deployed by `github-watcher` on push to `main` (config key `sharpsir-group/matrix-pipeline-2-0`, secret `WEBHOOK_SECRET_PIPELINE`, base path patched to `/pipeline/`).
**Key Features** (target — see [`wiki/requirements.md`](../product-specs/matrix-pipeline/wiki/requirements.md) FR-CON / PC / COM / CFL / FNL / PROS / ACT / SHOW / CARA / CL / TM / CMM / DOC / REF / REP and [`phases.md`](../product-specs/matrix-pipeline/phases.md)):
- Canonical `Contacts` lifecycle with `ContactType` graduation (Lead → Prospect → Ready-to-Buy → Buyer/Seller) — FR-CON
- Multiple parallel commercial intents per contact via canonical `SavedSearch` + `Prospecting` — FR-PC
- Canonical 5-stage funnel projection over `(Contacts × SavedSearch)` (Qualification / Matching / Viewing / Contracting / Payment) — FR-FNL-01..06; **no `pipeline_stages` table**, the projection is a view over canonical CDL state
- Activity / task / follow-up management — FR-ACT
- Canonical 5-resource `Showing` chain (`ShowingAvailability` → `ShowingRequest` → `ShowingAppointment` → `Showing` → `LockOrBox`) — FR-SHOW
- Curated luxury tours via `Caravan` + `CaravanStop` — FR-CARA
- Client engagement via `ContactListings` + `ContactListingPreference` + `ContactListingNotes` — FR-CL
- Offers and transactions via canonical `TransactionManagement` + `HistoryTransactional` audit — FR-TM
- **Commission Engine ERP-lite** (second project-flavour escape hatch, app-private only): per-deal cost attribution via `Activity` tagging, GCI forecasting per FR-FNL-12 precedence (`OfferAmount` (a) > `SavedSearch` budget mid-point (b)), broker compensation rule engine, reconciliation against external Finance ERP — see [`wiki/commission-engine.md`](../product-specs/matrix-pipeline/wiki/commission-engine.md)
- AI Brokerage Copilot — FR-AI-LQ Lead Qualification, FR-AI-MX Match Explanation, FR-AI-SC Showing Coach, FR-AI-DM Deal Margin Coach (each shipped as a small LLM-wrapper EF; see [`wiki/ai.md`](../product-specs/matrix-pipeline/wiki/ai.md))
- O365 email + calendar integration linked to `Activity` and `ShowingAppointment` rows
- Listing Module integration via canonical `Property` + `Property.StandardStatus` push events — see [`wiki/integration.md#listing-module`](../product-specs/matrix-pipeline/wiki/integration.md#listing-module)
- Role-based permissions via SSO `role_configurations` (app_id: `smpipeline`)

### Contact Management → consolidated into matrix-pipeline 2.0
**Status**: target-state contact management folds into matrix-pipeline 2.0 (FR-CON cluster). The deployed `Contact Management` app remains a transitional surface; new development goes into matrix-pipeline.
**Spec**: see [`product-specs/matrix-pipeline/wiki/requirements.md#fr-con-contacts`](../product-specs/matrix-pipeline/wiki/requirements.md#fr-con-contacts).
**RESO Resources** (canonical): `Contacts`, `Member`, `OUID`, plus AI-driven enrichment via FR-AI-LQ.
**Key target capabilities** (post-consolidation):
- Canonical `Contacts` lifecycle with `ContactType` graduation (Lead → Prospect → Ready-to-Buy → Buyer/Seller); no MQL/SQL labels
- FR-AI-LQ inbound qualification + routing (broker confirms, writes via `cdl-contacts-write`)
- Communication logging in `Activity` (canonical resource)
- Canonical contact deduplication via `Contacts.MatchKey` heuristics + admin merge tools
- Segmentation via canonical `ContactType` + `SavedSearch` parameters (no app-private tags layer)

### ITSM (IT Service & Asset Management)
**Status**: In Progress
**Users**: IT staff, IT Admins, All internal users (ticket submitters)
**App Type**: Domain-Specific (own Supabase instance)
**Supabase Instance**: `irjrcskfcyierdbefrpk`
**Repo**: `/home/bitnami/itsm-2-1`
**Key Features** (target):
- Service desk with ticket lifecycle (Incident, Service Request, Change, Problem)
- SLA tracking with priority-based breach time
- Multi-level agent assignment (L1/L2/L3 escalation)
- CMDB: hardware/software asset registry with classification tree and bill of materials
- Software asset and license management with seat allocation
- Vendor and IT project management
- IT budget management with categories
- Analytics dashboards (service desk + IT operations)
- IT architecture documentation
- Microsoft 365 integration (Graph API)
- Active Directory employee sync
- External incident ingestion via webhook
- MLS integration settings (inherited from template)
- Role-based permissions via `app_permissions` (app_id: `itsm`)

### HRMS (Human Resources Management)
**Status**: In Progress
**Users**: All employees, Managers, HR team, Finance team, Admins
**App Type**: Domain-Specific (own Supabase instance)
**Supabase Instance**: `wltuhltnwhudgkkdsvsr`
**Repo**: `/home/bitnami/matrix-hrms`
**Key Features** (target):
- Employee directory with public profiles and search
- Interactive organizational structure chart
- Multi-step vacation approval workflow (Employee → Manager → HR → Finance)
- Leave balance tracking and policy management
- Onboarding and offboarding checklists with templates
- Internal change requests (transfers, promotions) with approval
- Performance review cycles with goals and participant assignment
- Compensation history tracking
- Document management with templates, distribution, and signing
- Employee profile edit requests with HR approval
- Internal social feed (posts, comments, reactions, holiday auto-posts)
- Active Directory sync and employee linking
- Excel bulk upload for employee data
- Public holiday management by country
- HR reports (headcount, turnover, leave statistics)
- Finance module for vacation payroll processing
- Role-based permissions via `sso_role_configurations` (app_id: `hrms`)
- 25+ domain tables, 30+ hooks

### Financial Management (Matrix FM)
**Status**: In Progress
**Users**: Finance team, Entity Managers, Country Managers, Senior Management, CFO/Board
**App Type**: Domain-Specific (own Supabase instance)
**Supabase Instance**: `retujkznogwplfrbniet`
**Repo**: `/home/bitnami/matrix-fm`
**Key Features** (target):
- Monthly financial reporting (P&L, Cash Flow, Balance Sheet, Working Capital)
- Annual reporting with full-year actuals
- Multi-year annual planning (Y-1 Actual, Y Budget, Y+1/Y+2/Y+3 Budget)
- CORE cost allocation by entity and year
- Submission workflow (Draft → Submitted → Withdrawn)
- Submission deadline management and tracking
- Data entry progress monitoring across entities
- Financial analytics and variance analysis
- Clipboard paste from Excel into financial grids
- Audit log with export capability
- Built-in bilingual documentation (EN/RU)
- Test data generation for development
- Edge Function-backed reads/writes with SSO JWT validation
- Role-based permissions via `app_permissions` (app_id: `matrix-financial-management`)

### Integration Management (Sources and Channels)
**Status**: In Progress
**Users**: Data Engineers, Admins, Listing Coordinators
**Key Features** (target):
- Ingress source configuration — manages all four `mls_sources.kind` types: `internal` (matrix-internal), `legacy-internal` (Qobrix CY — sunsetting), `brand-network` (Anywhere Dash — bidirectional; covers HU + KZ inbound today), `external` (developer / partner-brokerage feeds)
- Per-source onboarding wizard (RESO Web API creds, scheduling, field mapping, locked-field defaults, sunset markers)
- Egress syndication controls (per-listing toggle for target channels; channel-distribution rules per source kind)
- Portal export configuration (SIR Global / Anywhere Dash, HomeOverseas, Zillow, etc.)
- Channel health monitoring and error reporting
- Deduplication and multi-source merge precedence (`source_field_priority`)

### Notification Management
**Status**: In Progress
**Users**: All internal users (recipients), Admins (configuration)
**Key Features** (target):
- Centralized notification engine for all Matrix apps
- Multi-channel delivery (in-app, email, push, WhatsApp)
- Notification templates and rules configuration
- User preference management (opt-in/opt-out per channel)
- Delivery tracking and retry logic

---

## App Details — Planned

### Broker App and Manager App → consolidated into matrix-pipeline 2.0

The previously-planned **Broker App** (broker daily dashboard + AI copilot) and **Manager App** (manager Kanban + analytics) are **superseded by the matrix-pipeline 2.0 product spec**, which consolidates broker, manager, contact-center, and listing-coordinator workflows into one CRM with role-based views over the same canonical 5-stage funnel projection (Qualification → Matching → Viewing → Contracting → Payment).

**Single source of truth**: [`product-specs/matrix-pipeline/`](../product-specs/matrix-pipeline/INDEX.md) (wiki + phases + cdl-crud-contract).

Capabilities previously listed under Broker App (personal dashboard, Next Best Action, Curated List generation, follow-up management, O365 integration) are realised in matrix-pipeline as:
- Broker home view = role-filtered canonical 5-stage funnel projection per `Member` ([`wiki/overview.md#pipeline`](../product-specs/matrix-pipeline/wiki/overview.md#pipeline))
- AI Copilot = FR-AI-LQ / MX / SC / DM clusters in [`wiki/ai.md`](../product-specs/matrix-pipeline/wiki/ai.md)
- Curated Lists = canonical `Caravan` + `CaravanStop` + `ContactListings` ([`wiki/requirements.md#fr-cara`](../product-specs/matrix-pipeline/wiki/requirements.md#fr-cara-caravans), [`wiki/requirements.md#fr-cl`](../product-specs/matrix-pipeline/wiki/requirements.md#fr-cl-contact-listings))
- Follow-up management = canonical `Activity` + reminders ([`wiki/requirements.md#fr-act`](../product-specs/matrix-pipeline/wiki/requirements.md#fr-act-activities))
- O365 integration = matrix-pipeline integration cluster ([`wiki/integration.md#o365`](../product-specs/matrix-pipeline/wiki/integration.md))

Capabilities previously listed under Manager App (revenue forecast, team productivity, intervention tools, pipeline monitoring) are realised in matrix-pipeline as:
- Revenue forecast = Commission Engine ERP-lite forecast precedence (FR-FNL-12 + FR-TM-13) — see [`wiki/commission-engine.md`](../product-specs/matrix-pipeline/wiki/commission-engine.md)
- Team productivity / broker comparisons = canonical reports over `Member` × `TransactionManagement` × `Activity` (FR-REP cluster)
- Intervention tools = canonical `Member` reassignment on `Contacts.OwnerMemberKey`, `Activity` creation, `HistoryTransactional` audit
- Real-time monitoring = view over canonical funnel state; no separate Kanban materialisation

### Client Portal
**Users**: Buyers and sellers (authenticated)
**RESO Resources**: Property, Media, ShowingAppointment, OpenHouse
**Key Features**:
- Personalized Curated Lists of properties
- Showing scheduling and confirmation
- Document exchange (contracts, title deeds)
- Communication with assigned broker
- Transaction status tracking

### Marketing App
**Users**: Marketing team
**RESO Resources**: Property, Contacts, Media
**Key Features**:
- Campaign management (email, SMS, social)
- Lead capture and auto-qualification
- Segmentation and triggers
- A/B testing
- Marketing funnel analytics

### BI Dashboard
**Users**: Leadership (CDSO, CDTO), managers
**Key Features**:
- KPI tracking against targets
- Revenue vs forecast
- Marketing funnel visualization
- Sales pipeline health
- Regional comparisons (Cyprus, Hungary, Kazakhstan)

### Admin Console
**Users**: System admins
**Key Features**:
- Platform configuration
- User management (bulk operations)
- System health monitoring

---

## RESO Resource Usage Matrix

> Matrix Pipeline = matrix-pipeline 2.0 (consolidates broker, manager, contact-center, and listing-coordinator workflows). Authoritative resource matrix in [`product-specs/matrix-pipeline/cdl-crud-contract.md`](../product-specs/matrix-pipeline/cdl-crud-contract.md).

| RESO Resource | Matrix Pipeline | Client Portal | Marketing | Finance | AI Services |
|---|:---:|:---:|:---:|:---:|:---:|
| `Property` | R/W (via Listing Module push) | R | R | R | R |
| `Contacts` | R/W | R (own) | R/W | R | R |
| `Member` | R/W | — | R | R | R |
| `Office`, `OUID` | R/W | — | R | R | R |
| `Teams`, `TeamMembers` | R/W | — | — | — | R |
| `Media` | R/W | R | R/W | — | R |
| `ShowingAvailability` / `Request` / `Appointment` / `Showing` / `LockOrBox` | R/W | R/W (own) | — | — | R |
| `Caravan`, `CaravanStop` | R/W | R (own) | — | — | R |
| `ContactListings`, `ContactListingPreference`, `ContactListingNotes` | R/W | R (own) | R | — | R |
| `SavedSearch`, `Prospecting` | R/W | R (own) | R/W | — | R |
| `Activity` | R/W | — | R | — | R |
| `OpenHouse` | R/W | R | R/W | — | R |
| `TransactionManagement` | R/W | R (own) | — | R | R |
| `HistoryTransactional` | R/W (emit) | — | R | R | R |
| `Document` | R/W | R (own) | — | R | R |
| `InternetTracking` | R | — | R/W | — | R |
| `PropertyDetailAttachment` | R | R | R/W | — | R |
| `Field`, `Lookup` (metadata) | R | R | R | R | R |
| `Referral` (project-flavour escape hatch) | R/W | — | — | R | R |

R = Read, W = Write, R/W = Read and Write

## O365 Integration Matrix

> O365 integration is a matrix-pipeline 2.0 capability cluster ([`wiki/integration.md#o365`](../product-specs/matrix-pipeline/wiki/integration.md)). All capabilities below are role-filtered inside the same matrix-pipeline app — there is no separate Broker / Manager app surface.

| Capability | Matrix Pipeline (broker role) | Matrix Pipeline (manager role) | Other Apps |
|---|:---:|:---:|:---:|
| Exchange email read (own mailbox) | ✓ | — | — |
| Attach email to `Activity` / `TransactionManagement` row | ✓ | — | — |
| View attached emails (team) | ✓ (own) | ✓ (team) | — |
| Outlook calendar sync (own) → `ShowingAppointment` / `Activity` | ✓ | — | — |
| Team calendar view | — | ✓ | — |
| Free/busy conflict detection | ✓ | ✓ | — |

See [o365-exchange-integration.md](o365-exchange-integration.md) for full technical details.
