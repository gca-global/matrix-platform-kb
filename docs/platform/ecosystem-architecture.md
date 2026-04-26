# Digital Ecosystem Architecture

> Source: `vision/Sarp SIR Platform-2026-02-18-125014.mmd` (Mermaid system diagram)
> Source: `vision/Sharp-Sothebys-International-Realty.pdf` (slides 10-13)
>
> **For Lovable**: This shows the full ecosystem. For how to build apps, see [app-template.md](app-template.md).

## Sharp Matrix vs Sharp SIR — what's what

| Term | What it is |
|---|---|
| **Sharp Matrix** | The **technology platform** powering Sharp SIR. Comprises four module families that all share the CDL: **CRM** (`matrix-pipeline`, `matrix-comms`, `matrix-client-connect`), **FM / Financial Management** (financial-entries, commissions, deal closings), **HR** (`matrix-hrms`), **MLS** (`matrix-atlas-mls`, `matrix-mls-2-0`, `matrix-cy-website`). |
| **Sharp SIR** | The **brokerage business** that operates on Sharp Matrix — a Sotheby's International Realty affiliate under Anywhere Brands. Currently active in **Cyprus**, **Hungary**, and **Kazakhstan**; more markets planned. |
| **Anywhere Dash** | The **SIR network's data exchange** between affiliated SIR offices worldwide. For Sharp SIR, Dash is the **primary bidirectional data contract**. See [dash-data-model.md](../data-models/dash-data-model.md). |
| **Qobrix** | Sharp SIR's **legacy CRM for Cyprus**. Currently exposed to the CDL via the `mls.sharpsir.group` RESO Web API projection. **Being decommissioned as the MLS source once Atlas runs Cyprus listing creation.** |
| **`matrix-pipeline`** | The Sharp Matrix CRM (lead/opportunity/listing pipeline). Replaces Qobrix as the system of record for new listings. |

## Three-Platform Architecture

| Platform | Role | Key Components |
|----------|------|---------------|
| **Supabase** | CDL & system of record | SSO instance (auth/permissions) + App DB instances (per app) |
| **Databricks** | DWH & ETL engine | Bronze/Silver/Gold pipeline, CDC, analytics |
| **Lovable** | App builder | `matrix-apps-template`, builds all Matrix Apps |

## Full Platform Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        EXTERNAL CHANNELS                                │
│  ┌───────┐ ┌──────────┐ ┌──────────────┐ ┌───────┐ ┌────────────────┐ │
│  │ Email │ │ Telegram │ │ WhatsApp BSP │ │ Voice │ │ Google/Meta Ads│ │
│  └───┬───┘ └────┬─────┘ └──────┬───────┘ └───┬───┘ └───────┬────────┘ │
└──────┼──────────┼──────────────┼─────────────┼─────────────┼───────────┘
       │          │              │             │             │
┌──────┼──────────┼──────────────┼─────────────┼─────────────┼───────────┐
│      │     OWN CHANNELS        │             │             │           │
│  ┌───┴────────┐ ┌──────────────┴──┐ ┌───────┴─────────┐   │           │
│  │ Public     │ │ Client Portal   │ │ Mobile App      │   │           │
│  │ Website    │ │ (Personal       │ │                 │   │           │
│  │            │ │  Cabinet)       │ │                 │   │           │
│  └─────┬──────┘ └───────┬────────┘ └────────┬────────┘   │           │
└────────┼────────────────┼───────────────────┼─────────────┼───────────┘
         │                │                   │             │
    ┌────┴────────────────┴───────────────────┴─────────────┴──────┐
    │              API GATEWAY / ESB (Integration Layer)            │
    └──┬──────────┬──────────┬──────────────┬──────────────┬───────┘
       │          │          │              │              │
┌──────┴──────────┴──────────┴──────────────┴──────────────┴───────────┐
│              MATRIX APPS (Built by Lovable from App Builder Template) │
│                                                                       │
│  Live:                                                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────┐ │
│  │ Agency       │ │ Client       │ │ Meeting Hub  │ │ Matrix      │ │
│  │ Portal       │ │ Connect      │ │              │ │ Comms       │ │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ └──────┬──────┘ │
│         │                │                │                │         │
│  In Progress (CDL-Connected):                                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                  │
│  │ Pipeline     │ │ Contact      │ │ Integration  │                  │
│  │ Management   │ │ Management   │ │ Management   │                  │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘                  │
│                                                                       │
│  In Progress (Domain-Specific):                                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────┐ │
│  │ HRMS         │ │ Matrix FM    │ │ ITSM         │ │ Notification│ │
│  │ (own DB)     │ │ (Financial)  │ │ (IT Service) │ │ Management  │ │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ └──────┬──────┘ │
│         │                │                │                │         │
│  Platform Services:                                                   │
│  ┌──────┴────────────────┴────────────────┴──────────────────────┐   │
│  │ SSO Console │ Website CMS │ AI Web Asst │ Zoe AI │ Blog AI    │   │
│  └───────────────────────────────────────────────────────────────┘   │
└──────────┬───────────────┬────────────────┬──────────────────────────┘
           │               │                │
┌──────────┴───────────────┴────────────────┴──────────────────────────┐
│  SUPABASE (Identity + Common Data Layer + Per-App Databases)          │
│                                                                       │
│  ┌────────────────────────┐ ┌────────────────────────┐ ┌──────────┐  │
│  │ SSO                     │ │ Matrix CDL              │ │ App DBs  │  │
│  │ xgubaguglsnokjyudgvc   │ │ ofzcokolkeejgqfjaszq    │ │ per app  │  │
│  │ Auth, Tenants,          │ │ Shared mls_* + ingestion│ │ Domain + │  │
│  │   Permissions, OAuth,   │ │ pipeline (ADR-014);     │ │ app-     │  │
│  │   ES256 JWTs (ADR-011)  │ │ JWKS-verified SSO JWTs  │ │ specific │  │
│  │                         │ │ (ADR-012 Third-Party)   │ │ tables   │  │
│  └────────────────────────┘ └────────────────────────┘ └──────────┘  │
│        SSO and CDL both owned by matrix-platform-foundation (ADR-013).│
└──────────┬───────────────────────────────────────────────────────────┘
           │
┌──────────┴───────────────────────────────────────────────────────────┐
│  DATABRICKS (DWH & ETL Engine)                                        │
│                                                                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                  │
│  │ Bronze       │ │ Silver       │ │ Gold (RESO)  │                  │
│  │ (raw strings)│→│ (normalized) │→│ (unified)    │→ RESO Web API    │
│  └──────────────┘ └──────────────┘ └──────────────┘                  │
│  CDC every 15 min. CDL pulls Gold via reso-import EF (ADR-014).      │
└──────────────────────────────────────────────────────────────────────┘
           │
┌──────────┴───────────────────────────────────────────────────────────┐
│  EXTERNAL SOURCES & SYNDICATION                                       │
│                                                                       │
│  Inbound (current, being phased out):                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                  │
│  │ Qobrix API   │ │ DASH API     │ │ DASH FILE    │                  │
│  │ (Cyprus)     │ │ (Kazakhstan) │ │ (Hungary)    │                  │
│  │ ⚠ replacing  │ │ ⚠ flipping   │ │ ⚠ flipping   │                  │
│  └──────────────┘ └──────────────┘ └──────────────┘                  │
│                                                                       │
│  Outbound (target state):                                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                  │
│  │ RESO Web API │ │ Dash/SIR     │ │ Portal       │                  │
│  │ (OData 4.0)  │ │ (push sync)  │ │ Exports      │                  │
│  └──────────────┘ └──────────────┘ └──────────────┘                  │
└──────────────────────────────────────────────────────────────────────┘
           │
┌──────────┴───────────────────────────────────────────────────────────┐
│  AI/ML & ANALYTICS                                                    │
│                                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────┐                    │
│  │ GenAI &     │  │ Scoring     │  │ AI Agents │                    │
│  │ Embedding   │  │ Models      │  │ (Copilot) │                    │
│  └─────────────┘  └─────────────┘  └───────────┘                    │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────┐                    │
│  │ RAG         │  │ Semantic    │  │ Recomm.   │                    │
│  │             │  │ Search      │  │ Engine    │                    │
│  └─────────────┘  └─────────────┘  └───────────┘                    │
└──────────────────────────────────────────────────────────────────────┘
```

## Layer Descriptions

### External Channels
Inbound communication touchpoints managed through the API Gateway.

| Channel | Purpose | Integration |
|---------|---------|-------------|
| Email | Client correspondence, marketing campaigns, opportunity context | SMTP/IMAP via API Gateway; Exchange Online via Microsoft Graph API (delegated, for broker mailbox read + attach to opportunity) |
| Telegram | Instant messaging (high priority: Cyprus, Kazakhstan) | Bot API via Gateway |
| WhatsApp BSP | Business messaging (high priority: all markets) | BSP API via Gateway |
| Voice | Phone calls, contact center | VoIP/SIP via Gateway |
| Google/Meta Ads | Lead generation, remarketing | Ads API via Gateway |

### Own Channels
Company-controlled digital properties.

| Channel | Purpose |
|---------|---------|
| Public Website | Property listings, brand, SEO, lead capture |
| Client Portal (Personal Cabinet) | Authenticated client area: Curated Lists, documents, communication |
| Mobile App | On-the-go access for brokers and clients |

### Integration Layer
**API Gateway / ESB** — central hub connecting all channels to application systems. Every request flows through this layer for consistent authentication (Matrix SSO), logging, and rate limiting.

**Ingress/Egress Channel Manager** (CDL MLS 2.1) — orchestration layer that manages data flow between external sources, the CDL, and syndication targets. Handles channel configuration, deduplication, filtering, and routing. See [mls-datamart.md](mls-datamart.md) for channel taxonomy.

### Matrix Apps (Application Layer)

All apps are built by **Lovable** from the **App Builder Template** (`matrix-apps-template`). Two categories:

| Type | Live | In Progress | Planned | Supabase Tables |
|------|------|-------------|---------|----------------|
| **CDL-Connected** | Agency Portal, Client Connect, Meeting Hub, Matrix Comms, Website CMS | Matrix Pipeline, Contact Mgmt, Integration Mgmt | Broker App, Manager App, Client Portal, Marketing App | Shared RESO tables: `property`, `member`, `contacts`, `media` |
| **Domain-Specific** | SSO Console | HRMS, Matrix FM, ITSM, Notification Mgmt | Admin Console, BI Dashboard | Own tables: `employees`, `vacations`, `financial_entries`, `service_desk_tickets`, etc. |

All apps share: SSO auth, dual-Supabase architecture, 5-level scope, CRUD permissions, shadcn/ui.

### Supabase (Identity + CDL + Per-App)

**Three project roles (ADR-012 / ADR-013):**
- **SSO project** (`xgubaguglsnokjyudgvc`) — identity only (auth, permissions, tenants, AD users, SSO EFs).
- **Matrix CDL project** (`ofzcokolkeejgqfjaszq`) — canonical listing tables (`public.properties`, `public.properties_published`, `public.property_media`), the **8 RESO resource tables** (`members`, `offices`, `contacts`, `open_houses`, `showings`, `history_transactional`, `internet_tracking_events`, `teams`), `cdl_staging.*` raw/mapped, the MLS Sync control plane (`mls_settings`, `mls_sync_jobs`, `mls_sync_state`, `mls_orchestrator_runs`), the source-of-record taxonomy (`mls_sources.kind`), the stewardship layer (`locked_fields` + `cdl_lock_field` / `cdl_unlock_field` RPCs), the lifecycle audit (`property_lifecycle_events`), the **7 `v_dash_*` Anywhere Dash projection views**, and **Phase-2 pgvector placeholders** (`embedding`, `feature_vector`, `marketing_metadata`). Eight EFs: 5-stage pipeline (`reso-import` / `field-mapping-apply` / `listing-merge` / `media-import` / `listing-publish`), admin (`mls-sync` + `mls-sync-orchestrator`), and read (`listings-search` — keyset pagination + ETag/Cache-Control + estimated counts; see [`read-path-performance.md`](../data-models/read-path-performance.md)). Uses Supabase Third-Party Auth against SSO JWKS so SSO-issued ES256 JWTs verify directly.
- **App DB projects** (per app) — app-specific tables with RLS.

CDL-Connected apps read shared listing data via the CDL anon client
(`public.properties_published`) or the `listings-search` EF; ingestion
and admin go through the `mls-sync` / `mls-sync-orchestrator` EFs on
the CDL project. Domain-Specific apps define their own schemas in
their own project.

### Databricks (DWH & ETL)

MLS 2.0 pipeline (`/home/bitnami/mls_2_0`):
- Ingests from Qobrix API (Cyprus), DASH API (Kazakhstan), DASH FILE (Hungary)
- Transforms through Bronze → Silver → Gold (RESO DD 2.0)
- Syncs gold layer to Supabase CDL
- Runs CDC every 15 minutes for incremental updates

See [mls-datamart.md](mls-datamart.md) for details.

### Data Sources & Syndication

**Sharp Matrix is the platform; Sharp SIR is the brokerage operating in Cyprus, Hungary, and Kazakhstan.** Most current inbound is either our own data (legacy CRMs being decommissioned) or sister-SIR-office data via the Anywhere brand network. We additionally support `external` feeds from third parties (developers, partner brokerages).

**Source-of-record taxonomy** (`mls_sources.kind`):

| Kind | Sources | Notes |
|---|---|---|
| `internal` | `matrix-internal` | Target state. Listings authored in Atlas / `matrix-pipeline` CRM / future broker apps. |
| `legacy-internal` | `qobrix` (Cyprus legacy CRM) | Sharp SIR's own data in a legacy CRM being decommissioned as Atlas takes over Cyprus listing creation. Marked `is_sunsetting = true`. HU + KZ have no legacy seed — those offices author directly in Anywhere Dash, so they're covered by the `dash` brand-network source. |
| **`brand-network`** | **`dash`** (Anywhere Dash) | **Primary BIDIRECTIONAL channel** — SIR affiliate contract. Phase-2.5 `dash-import` / `dash-export` EFs. |
| `external` | (added per onboarding) | Third-party feeds we ingest from organizations outside Sharp SIR — real estate **developers** (new-build / off-plan inventory), **partner brokerages** (referrals, co-broke), future industry MLS exchanges. Inbound only; onward syndication restricted by per-partner terms-of-use. |

**Anywhere Dash (SIR network) — primary BIDIRECTIONAL channel.** Sharp Matrix powers an SIR affiliate under Anywhere Brands; Dash is therefore not a generic syndication target but a contractual two-way contract surface. Phase-1 lands the schema hooks (`mls_sources.kind = 'brand-network'`, `dash` source seed row, SIR brand markers, `v_dash_*` projection views). Phase-2.5 lands the EFs (`dash-import` for sister-SIR-office listings; `dash-export` for our internally-sourced `Active` listings).

**Current state (Cyprus, today):**
- Qobrix legacy CRM → exposed as `mls.sharpsir.group` (RESO Web API projection over our own data) → CDL `mls-sync` EF. **This is a self-loop during the migration period.** `qobrix` source is `kind = 'legacy-internal'`, `is_sunsetting = true`.
- Anywhere Dash → Databricks bronze (via `mls_2_0` ETL); flipping to direct CDL bidirectional in Phase-2.5.

**Target state (per market, as Atlas covers listing creation):**
- Brokers author listings in `matrix-pipeline` CRM / Atlas → direct CDL writes (`source_id = matrix-internal`).
- Legacy CRM (Qobrix CY) gets `sunset_at` set; `mls-sync` stops scheduling against it.
- **Anywhere Dash ↔ CDL (bidirectional, primary contract)** — sister-SIR-office listings inbound, our `Active` SIR-branded listings outbound; both via `v_dash_*` views.
- RESO Web API → 3rd-party integrations (outbound, secondary).
- Portal exports → HomeOverseas.ru, Zillow, partner portals (outbound, secondary).

### AI/ML & Analytics Layer

| Component | Function |
|-----------|----------|
| GenAI & Embedding Providers | LLM services, text embedding for semantic capabilities |
| Scoring Models | Lead scoring, deal probability, property valuation |
| AI Agents (Copilot) | AI Brokerage Copilot: Next Best Action, forecasting, automation |
| RAG | Knowledge-grounded AI responses |
| Semantic Search | Natural language property and client search |
| Recommendation Engine | Property matching, Curated List generation |
| Personalization Engine | Visitor profiling, semantic ranking, personalized listing order |
| Visitor Profiling | Anonymous + authenticated user behavior tracking for recommendation input |

## Data Flow Patterns

### Listing Ingress Flow (CDL MLS 2.1)
```
Direct CDL write (Matrix Apps) → Supabase CDL → Realtime → all apps
API ingress (new constructions)  → Edge Function → Supabase CDL → Realtime
Legacy pipeline (Databricks)     → Gold sync → Supabase CDL (being phased out)
```

### Listing Creation Flow (Target State)
```
Broker (Broker App / matrix-pipeline CRM)
    → cdl-write EF → Supabase CDL (source_id=matrix-internal, lifecycle_state=Draft)
    → cdl-listing-lifecycle EF (submitForReview → approve → publish)
    → Realtime → Manager App, Client Portal see updates instantly
    → Sync → Databricks (analytics/BI)
    → dash-export EF (bidirectional) → Anywhere Dash via v_dash_properties (SIR-affiliate primary contract)
    → Push (secondary) → RESO Web API (3rd parties), Zillow, partner portals
    → AI Copilot monitors: DOM, viewings, conversions
```

### Lead Processing Flow
```
Ads/Website/Referral → API Gateway → Marketing Platform → Contact Center
    → Supabase CDL (RESO Contacts table)
    → AI/ML (scoring, qualification, Next Best Action)
    → Assignment to broker via Manager App
```

### O365 Integration Flows

**Email (read + attach to opportunity):**
```
Broker App → email-messages Edge Function → Microsoft Graph API (/me/messages)
    → Exchange Online (broker's mailbox, delegated access)
    → Broker selects email → email-attach Edge Function
    → Snapshot stored in Supabase CDL (opportunity_emails table)
```

**Calendar (CRM ↔ Outlook sync):**
```
Broker creates viewing/meeting in CRM → calendar-events Edge Function
    → Microsoft Graph API (POST /me/calendar/events)
    → Outlook event created with attendees (client, seller/keyholder)
    → outlook_event_id stored back in CRM (showing_appointment / broker_meetings)

Broker views calendar in CRM → calendar-events Edge Function
    → Microsoft Graph API (GET /me/calendarView)
    → Merged view: CRM-linked events + Outlook-only events
```

See [o365-exchange-integration.md](o365-exchange-integration.md) for full architecture, data model, and security details.

### Analytics Flow
```
All Matrix Apps → Supabase CDL → Sync → Databricks DWH
    → BI dashboards → Scoring models → RAG knowledge base
    → Semantic Search → Recommendation Engine
```
