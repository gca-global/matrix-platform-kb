# Sharp Matrix Platform — App Catalog

> All applications and platform components in the Sharp Matrix ecosystem, with current delivery status.
> Last updated: March 2026

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
| 19 | Broker Daily Dashboard & AI Copilot | **Broker App** | App (CDL-Connected) | Brokers, Agents |
| 20 | Manager Kanban & Analytics | **Manager App** | App (CDL-Connected) | Sales Managers, Team Leads |
| 21 | Buyer/Seller Self-Service | **Client Portal** | App (CDL-Connected) | Buyers, Sellers |
| 22 | Campaign & Marketing Automation | **Marketing App** | App (CDL-Connected) | Marketing Team |
| 23 | Leadership KPI Dashboards | **BI Dashboard** | App | Leadership (CDSO, CDTO) |
| 24 | Platform Configuration | **Admin Console** | App | System Admins |

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
**Repo**: `/home/bitnami/matrix-apps-template`
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
**Status**: In Progress
**Users**: Brokers, Sales Managers, Call Center Staff, Listing Coordinators, Marketing, Finance
**RESO Resources**: Property, Media, Contacts, Member, Office
**App Type**: CDL-Connected
**Supabase Instance**: `tiuansahlsgautkjsajk`
**Repo**: `/home/bitnami/matrix-pipeline`
**Key Features** (target):
- Lead capture and management with webhook ingestion from external sources
- Sales pipeline with Kanban board and drag-and-drop stage management
- Opportunity detail with contacts, properties, tasks, timeline, and email linking
- Opportunity review workflow for manager oversight
- Comprehensive contact management with relationship tracking
- Microsoft 365 email integration (read inbox, link emails to deals)
- Microsoft 365 calendar integration (events linked to opportunities)
- MLS property data browsing and linking to pipeline opportunities
- Call center module with contact verification and MLS duplicate checking
- Shared property lists via public token links for client sharing
- AI-powered data entry: voice transcription and opportunity info parsing
- Semantic search and Humatic AI matching
- Date-based reminders for contact follow-ups
- Notification system with real-time updates
- CDL write proxy for app settings and role configurations
- Role-based permissions via `role_configurations` (app_id: `smpipeline`)
- Revenue forecasting with probability-weighted calculations

### Contact Management
**Status**: In Progress
**Users**: Brokers, Sales Managers, Contact Center, Welcome Team
**RESO Resources**: Contacts, Member
**App Type**: CDL-Connected
**Key Features** (target):
- Comprehensive contact lifecycle management
- Omnichannel inbox (Email, Telegram, WhatsApp, Voice)
- Lead qualification (Raw → MQL → SQL)
- Automated routing and assignment
- Communication logging and history
- Contact deduplication across sources
- Segmentation and tagging

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

### Integration Management (External MLS and Portals)
**Status**: In Progress
**Users**: Data Engineers, Admins, Listing Coordinators
**Key Features** (target):
- Ingress channel configuration (which external sources feed into CDL)
- Egress syndication controls (per-listing toggle for target channels)
- External MLS feed management
- Portal export configuration (SIR Global, HomeOverseas, etc.)
- Channel health monitoring and error reporting
- Deduplication and conflict resolution rules

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

### Broker App
**Users**: Brokers and agents
**RESO Resources**: Property, Contacts, Member, ShowingAppointment, Media
**O365 Dependency**: Exchange Online (Mail.Read, Calendars.ReadWrite via Microsoft Graph API)
**Key Features**:
- Personal daily dashboard with auto-prioritized actions
- AI Copilot with Next Best Action per client
- Client cards with activity history
- Follow-up management (zero tolerance for missed)
- Property matching and Curated List generation
- Document generation (PDF brochures)
- Exchange email integration: read inbox, attach emails to opportunities
- Outlook calendar sync with free/busy conflict detection

### Manager App
**Users**: Sales managers, team leads
**RESO Resources**: Property, Contacts, Member, Office, Teams
**O365 Dependency**: Exchange Online (Calendars.ReadWrite, Mail.Read via Microsoft Graph API)
**Key Features**:
- Dual Kanban: seller-side (listings) + buyer-side (sales) pipelines
- Revenue forecast with probability-weighted calculations
- Team productivity metrics and broker comparisons
- Intervention tools: reassign, add tasks, comment
- Real-time pipeline monitoring with trouble spot detection
- Team calendar overview and email audit on opportunities

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

| RESO Resource | Pipeline Mgmt | Contact Mgmt | Broker App | Manager App | Client Portal | Marketing | Finance | AI Services |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Property | R/W | — | R/W | R | R | R | R | R |
| Contacts | R | R/W | R/W | R | R (own) | R/W | R | R |
| Member | R | R | R | R/W | — | R | R | R |
| Office | R | — | R | R/W | — | R | R | R |
| Teams | — | — | R | R/W | — | — | — | R |
| Media | R/W | — | R/W | R | R | R/W | — | R |
| ShowingAppointment | R | — | R/W | R | R/W | — | — | R |
| OpenHouse | R/W | — | R | R | R | R/W | — | R |
| HistoryTransactional | R | — | R | R | — | R | R | R |
| Prospecting | — | R/W | R/W | R | — | R/W | — | R |

R = Read, W = Write, R/W = Read and Write

## O365 Integration Matrix

| Capability | Broker App | Manager App | Other Apps |
|-----------|:---:|:---:|:---:|
| Exchange email read (own mailbox) | ✓ | — | — |
| Attach email to opportunity | ✓ | — | — |
| View attached emails (team) | ✓ (own) | ✓ (team) | — |
| Outlook calendar sync (own) | ✓ | — | — |
| Team calendar view | — | ✓ | — |
| Free/busy conflict detection | ✓ | ✓ | — |

See [o365-exchange-integration.md](o365-exchange-integration.md) for full technical details.
