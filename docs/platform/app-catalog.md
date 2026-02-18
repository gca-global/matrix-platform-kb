# Sharp Matrix Platform — App Catalog

> All applications in the Sharp Matrix ecosystem and their relationship to the RESO DD common data layer

## App Overview

| App | Primary Users | Purpose | Status |
|-----|--------------|---------|--------|
| **Broker App** | Brokers/Agents | Daily dashboard, AI Copilot, client management | Planned |
| **Manager App** | Sales Managers | Kanban pipelines, analytics, team management | Planned |
| **Client Portal** | Buyers, Sellers | Property search, Curated Lists, documents, communication | Planned |
| **Marketing App** | Marketing Team | Campaigns, automation, lead capture, analytics | Planned |
| **Listings Management (MLS)** | Brokers, Listing Coordinators, Marketing, Finance | Listing lifecycle, syndication, media management | CDL Deployed |
| **Contact Center** | Welcome Team | Omnichannel communication, lead qualification | Planned |
| **Finance App** | Finance Team | Commissions, invoicing, payment tracking | Planned |
| **AI Copilot** | All internal users | Next Best Action, matching, forecasting, automation | Planned |
| **BI Dashboard** | Leadership (CDSO, CDTO) | KPI tracking, management reporting | Planned |
| **SSO Console** | Admins | Authentication, authorization, RBAC | Active |
| **Admin Console** | System Admins | Platform configuration, user management | Planned |
| **Website CMS** | Content Managers | Public website content, SEO, property pages | Active |

## App Details

### Broker App
**Users**: Brokers and agents
**RESO Resources**: Property, Contacts, Member, ShowingAppointment, Media
**Key Features**:
- Personal daily dashboard with auto-prioritized actions
- AI Copilot with Next Best Action per client
- Client cards with activity history
- Follow-up management (zero tolerance for missed)
- Property matching and Curated List generation
- Document generation (PDF brochures)

### Manager App
**Users**: Sales managers, team leads
**RESO Resources**: Property, Contacts, Member, Office, Teams
**Key Features**:
- Dual Kanban: seller-side (listings) + buyer-side (sales) pipelines
- Revenue forecast with probability-weighted calculations
- Team productivity metrics and broker comparisons
- Intervention tools: reassign, add tasks, comment
- Real-time pipeline monitoring with trouble spot detection

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
- Marketing funnel analytics (CTR, opens, conversions)
- Syndication management to portals

### Listings Management (Matrix MLS)
**Users**: Brokers, listing coordinators, marketing, finance
**RESO Resources**: Property, Media, Contacts, Member, Office
**App Type**: CDL-Connected (18 `mls_*` tables on shared CDL instance)
**Repo**: `/home/bitnami/matrix-mls`
**CDL Schema**: `docs/data-models/mls-cdl-schema.md`
**Status**: Data model deployed, app under development
**Key Features**:
- Multi-step conditional listing form replacing Excel checklists (Apartment/House/Land/Development)
- Shared contact registry with role-based linking (seller, introducer, keyholder, lawyer)
- Document compliance with conditional mandatory rules (with/without title deed, land)
- Media management with Dash category alignment and development inheritance
- 9-stage status pipeline (DRAFT → PUBLISHED → SOLD) with immutable audit trail
- Multi-language marketing descriptions (EN/RU/HU) with approval workflow
- Portal syndication tracking (SIR Global, Cyprus Website, MLS Feed, social media)
- Role-based checklists (29 Broker, 10 Marketing, 5 Finance steps)
- Price history with approval workflow for large changes
- Task assignment system (photoshoot, marketing review, portal upload, finance filing)

### Contact Center
**Users**: Welcome Team, call center
**RESO Resources**: Contacts
**Key Features**:
- Omnichannel inbox (Email, Telegram, WhatsApp, Voice)
- Lead qualification (Raw → MQL)
- Automated routing and assignment
- Communication logging

### Finance App
**Users**: Finance team
**RESO Resources**: Property (transaction data), Member
**Key Features**:
- Commission calculation and tracking
- Invoice generation
- Payment follow-up
- Agreement registry
- Financial reporting

### AI Copilot (Cross-Cutting Service)
**Users**: All internal users (embedded in other apps)
**RESO Resources**: All
**Key Features**:
- Context analysis and automatic stage determination
- Next Best Action with probability scoring
- Bidirectional matching (listings ↔ buyers)
- Lead scoring and deal probability
- Follow-up auto-scheduling
- Content suggestions for communication
- Engagement tracking and priority adjustment
- RAG-powered knowledge retrieval
- Semantic property search

### BI Dashboard
**Users**: Leadership (CDSO, CDTO), managers
**Key Features**:
- KPI tracking against targets
- Revenue vs forecast
- Marketing funnel visualization
- Sales pipeline health
- Regional comparisons (Cyprus, Hungary, Kazakhstan)

### SSO Console (Active)
**Users**: System administrators
**Key Features**:
- OAuth/JWT authentication
- RBAC (role-based access control)
- User and group management
- App registration and permissions

## RESO Resource Usage Matrix

| RESO Resource | Broker | Manager | Client | Marketing | Listings | Contact | Finance | AI |
|--------------|--------|---------|--------|-----------|----------|---------|---------|-----|
| Property | R/W | R | R | R | R/W | — | R | R |
| Contacts | R/W | R | R (own) | R/W | R | R/W | R | R |
| Member | R | R/W | — | R | R | R | R | R |
| Office | R | R/W | — | R | R | — | R | R |
| Teams | R | R/W | — | — | — | — | — | R |
| Media | R/W | R | R | R/W | R/W | — | — | R |
| ShowingAppointment | R/W | R | R/W | — | R | — | — | R |
| OpenHouse | R | R | R | R/W | R/W | — | — | R |
| HistoryTransactional | R | R | — | R | R | — | R | R |
| Prospecting | R/W | R | — | R/W | — | R/W | — | R |

R = Read, W = Write, R/W = Read and Write
