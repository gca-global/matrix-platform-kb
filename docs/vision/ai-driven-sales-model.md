# AI-Driven Sales Management Model

> Source: AI-driven model upravleniya prodazhami (16-slide vision deck, © 2026 Sharp Sotheby's International Realty)
> Author: Sergey Seregin, Chief Digital Technology Officer

## Model Overview

The model unifies traditional sales processes with AI technologies for maximum broker effectiveness. Core principle: **the broker works with the client; the system works with the process**.

### 4 Elements of the Model

| # | Element | Purpose | Key Metrics |
|---|---------|---------|-------------|
| 1 | **Commission Funnel** | Revenue engine — tracks revenue from plan to close | Revenue (actual vs plan), # closed deals, avg commission check, cycle length, MQL→Closed Won conversion |
| 2 | **Listings** | Seller-side — inventory management & syndication | Active listings, new listings/period, Days on Market, listing→sale conversion, matching quality |
| 3 | **Appointments** | Truth point — first meeting triggers Active Sales | Meeting→deal conversion, no-show rate, days from showing to deal, # appointments/month |
| 4 | **Follow-ups** | Nurturing engine — zero follow-ups may be missed | Missed follow-ups (must be 0), response rate, avg response time, follow-up→appointment conversion |

### 2 Representations of the Process

| View | User | What They See |
|------|------|---------------|
| **matrix-pipeline CRM** (for managers) | Sales Manager | Canonical 5-stage funnel projection (Qualification → Matching → Viewing → Contracting → Payment) over `(Contacts × SavedSearch)`, Listing Module read-side, Commission Engine ERP-lite forecast, broker performance — see [`product-specs/matrix-pipeline/wiki/overview.md#pipeline`](../product-specs/matrix-pipeline/wiki/overview.md#pipeline) |
| **AI Brokerage Copilot** (for brokers) | Broker | `Contacts` card with Next Best Action, FR-AI-MX matching suggestions, stage-aware FR-AI-SC showing coach, FR-AI-DM deal margin coach — see [`product-specs/matrix-pipeline/wiki/ai.md`](../product-specs/matrix-pipeline/wiki/ai.md) |

---

## Element 1: Commission Funnel

The primary goal of the entire sales management system.

### Goals
- **Maximize revenue**: Increase closed deals count and average commission check
- **Predictability**: Accurate pipeline forecasting based on conversion rates
- **Steady growth**: Stable month-over-month and quarter-over-quarter increases

### Forecast Rule
Long-term leads (timeline >12 months) do NOT pollute the active sales forecast. They move to a separate **nurturing pool** with monthly cadence, preserving forecast accuracy and team focus on "hot" deals.

### Key Metrics
- Revenue (actual vs plan)
- Number of `TransactionManagement` rows in `Closed` status (canonical RESO terminal)
- Average commission check (forecast GCI per FR-FNL-12, see [`matrix-pipeline/wiki/commission-engine.md`](../product-specs/matrix-pipeline/wiki/commission-engine.md))
- Sales cycle length (days, Qualification → Payment)
- Funnel conversion: Qualification → Payment (full canonical 5-stage funnel)

---

## Element 2: Listings (Seller-Side)

Listings = the seller-side process. This element forms the inventory for the buyer-side.

### Seller-Side: canonical `Property.StandardStatus` lifecycle

Listing-side workflow is the canonical RESO listing lifecycle (see [`canonical-processes/processes/listing-lifecycle.md`](../business-processes/canonical-processes/processes/listing-lifecycle.md)). Stages are values of canonical `Property.StandardStatus`:

| `StandardStatus` | Tasks | Canonical Artifacts |
|---|---|---|
| `Coming Soon` | Find potential sellers, first contact, present services, professional photoshoot, legal review | `Contacts` row, signed listing agreement, `Property` + `Media` rows |
| `Active` | Organize showings, collect buyer feedback, adjust strategy | `Showing` events, `Activity` notes, `HistoryTransactional` audit |
| `Active Under Contract` / `Pending` | Negotiate final price, coordinate with lawyers | `TransactionManagement` row with `OfferAmount` |
| `Closed` | Final deal closure, commission attribution, archive | Closed `TransactionManagement`, Commission Engine `BrokerCompensation` row, full document package |
| `Withdrawn` | Remove property from sale per seller initiative, document reason | `HistoryTransactional` row with reason; reactivation via canonical re-listing |

Sharp-SIR-specific stage names (PROSPECT / CONTACTED / AGREEMENT SIGNED / SOLD / AGENT COMMISSION PAYMENT / CLOSED WON / LISTING WITHDRAWN) used in older docs are not part of the canonical model. The matrix-pipeline product spec materialises every stage transition as a `Property.StandardStatus` change emitting a `HistoryTransactional` audit row — see [`canonical-processes/processes/listing-lifecycle.md`](../business-processes/canonical-processes/processes/listing-lifecycle.md).

### Bi-Directional Matching

| Direction | How It Works |
|-----------|-------------|
| Listing → Matching Buyers | AI automatically finds clients from the database whose criteria match the new listing |
| Buyer → Matching Listings | AI generates a Curated List based on buyer's specific needs |

### Listing Integrations
- **Syndicate Dashboard**: Automated syndication to all key real estate portals
- **MLS Systems**: Integration with Multiple Listing Services for maximum reach
- **Social Media**: Auto-publish on Facebook, Instagram, LinkedIn with optimized content
- **Corporate Website**: Real-time sync with company website
- **PDF Brochures**: Auto-generation of professional property presentations
- **Email Campaigns**: Automated distribution of new listings to matching clients
- **Calendar of Showings**: Integration with calendar for viewing planning

### Listing Quality Metrics
- Days on Market (DOM)
- View → Showing conversion
- Showing → Offer conversion
- Number of active listings
- Listing → Sale conversion

---

## Element 3: Appointments

Appointments (meetings and showings) are the **truth point** where the broker directly interacts with the client and influences the purchase decision. The first meeting = the trigger for transitioning from Follow-up into Active Sales.

### Goals
- **Maximize meetings**: Increase quality appointments with qualified clients
- **High conversion**: Turn maximum meetings into closed deals
- **Effective time**: Optimize showing routes and meeting preparation

### Anatomy of an Appointment
1. **Preparation**: Study the client, select properties, plan route
2. **Questions list**: Pre-prepared questions to identify needs
3. **Fixed feedback**: Detailed notes on client reaction to each property
4. **Next step (follow-up)**: Concrete action and date for next contact

### Key Metrics
- Appointment → deal conversion
- No-show rate (missed meetings)
- Average days from showing to deal
- Appointments count per period
- Days with showings per month

---

## Element 4: Follow-ups

Follow-up = sales preparation (nurturing). Without it, there will be no closing. Missed follow-ups are the primary source of lost deals — the system must prevent every miss.

### Goals
- **Zero missed**: Not a single follow-up should be missed or forgotten
- **Timeliness**: Contact the client at the right moment with the right message
- **Lead progress**: Gradually move the client from cold to hot status

### How AI Copilot Helps with Follow-ups

| Capability | Description |
|-----------|-------------|
| Auto-scheduling | After each contact, system suggests date and time for next follow-up based on context |
| Prioritization | Surfaces urgency of contacts: missed (critical) → today → hot potentials → tomorrow → new leads |
| Reminders | Notifications about upcoming and missed follow-ups in real time |
| Content suggestions | Suggests message themes: new listings matching criteria, market updates, personal recommendations |
| Engagement tracking | Analyzes email opens, clicks, reactions and adjusts priorities |

### Key Metrics
- Missed follow-ups (target: 0)
- Response rate
- Average broker response time
- Follow-up → appointment conversion
- Touches before meeting

---

## Customer Journey: Seller (Property Owner)

Path from the decision to sell to a successful deal.

| Stage | Client Emotions & Thoughts | Client Actions | Contact Points |
|-------|---------------------------|----------------|----------------|
| 1. Awareness | "Time for a change. Want new housing. Will selling bring enough money?" | Thinks about selling, discusses with family, studies market potential | Seasonal (ads, broker content marketing) |
| 2. Decision | "How to sell correctly? Need a good broker. Where to start?" | Studies market, compares agencies, reads reviews | Web, social media, online inquiries, phone calls |
| 3. Broker Selection | "Choosing the best partner. Can I trust them? What value do they offer?" | Meets brokers, evaluates proposals, asks questions | Personal meetings, presentations, phone calls |
| 4. Preparation | "Let's start! Want the home to look ideal. Are all documents in order?" | Provides documents, prepares property for showings (cleaning, staging), participates in photoshoot | Preparation consultations, photoshoot coordination |
| 5. Active Listing | "Hope for a quick and profitable result. When will there be news?" | Maintains order in home for showings, awaits feedback | Showing reports, feedback from potential buyers |
| 6. Offers | "Received an offer! Is the price fair? Do I need to negotiate?" | Reviews proposals, discusses terms with broker, makes decision on counter-offer | Offer discussions, trade consultations |
| 7. Closing | "Finish line! Will get money soon. Will everything go smoothly?" | Signs documents, transfers keys, receives payment | Closing process coordination, legal consultations |

**Result for client**: Sale at optimal price, minimal time on market, professional support at all stages, zero stress.

---

## Customer Journey: Buyer

Path from recognizing the need to buy to the purchase.

| Stage | Client Emotions & Thoughts | Client Actions | Contact Points |
|-------|---------------------------|----------------|----------------|
| 1. Need Recognition | Initial interest, discusses with family, studies budget | Contacts broker | Seasonal (ads, content marketing) |
| 2. Ideal Search | "Want to see options matching my needs" | Describes preferences, receives personalized Curated List of 3-7 properties | Web, social media, phone |
| 3. Viewings | Visits showings, asks questions, compares properties | Gets organized showings, expert broker commentary | Personal meetings, presentations |
| 4. Selection & Discussion | Evaluates final options, discusses financing | Broker helps with negotiations, provides transparent terms | Consultations, financial calculations |
| 5. Purchase | Signs documents, pays, receives keys | Smooth process, all docs ready, no surprises | Closing coordination |
| 6. New Home | Settles in, adapts, shares impressions | Broker follows up, helps with questions, stays connected | Post-sale follow-up |

---

## AI Brokerage Copilot

The core instrument of the modern real estate broker.

### What AI Copilot Does

| Capability | Description |
|-----------|-------------|
| **Analyzes context** | Automatically determines deal stage based on actions and client data |
| **Suggests actions** | Next Best Action with success probability forecast for each step |
| **Automates routine** | Reminders, follow-ups, listing matching, document generation |
| **Learns** | Analyzes successful deals and improves recommendations over time |

### Copilot for Brokers (Client Card View)
For brokers, the Copilot acts as an assistant: registers contacts, plans follow-ups, prepares Curated Lists. The broker concentrates on conversations, showings, and closing deals.

### Example: Working with a Seller (Listing)

```
Name: Maria Ivanova | Property: Villa, Paphos | Price: €850K | Mandate: Exclusive
NEXT BEST ACTION: Organize showing and prepare professional presentation
Sale probability in 90 days: 40% → 60%

Listing pipeline: `Property.StandardStatus`: Coming Soon → Active (in progress) → Active Under Contract → Closed
```

### Example: Working with a Buyer

```
Name: Ivan Petrov | Budget: €500K | Location: Limassol | Timeline: 3-6 months
NEXT BEST ACTION: Schedule showing, from identified suitable properties (FR-AI-MX matches)
Deal probability: 15% → 35%

Funnel: Qualification (Contacts.ContactType = Prospect) → Matching (in process) → Viewing → Contracting → Payment
```

### Next Best Actions by Stage

#### Seller-Side (canonical `Property.StandardStatus`)

See [`canonical-processes/processes/listing-lifecycle.md`](../business-processes/canonical-processes/processes/listing-lifecycle.md) for the full state machine; CRM materialisation in [`product-specs/matrix-pipeline/wiki/integration.md#listing-module`](../product-specs/matrix-pipeline/wiki/integration.md#listing-module).

| `StandardStatus` | Recommended Actions | Impact |
|---|---|---|
| `Coming Soon` | Find potential sellers, sign listing agreement, photoshoot, legal review | +15-30% |
| `Active` | Organize `Showing` events, collect feedback, FR-AI-MX matching, adjust strategy | +25-40% |
| `Active Under Contract` / `Pending` | Negotiate price, finalise `TransactionManagement.OfferAmount`, coordinate lawyers | +40-50% |
| `Closed` | Commission attribution (Commission Engine), archive documents, request review | +45-50% |
| `Withdrawn` | Document reason in `HistoryTransactional`, analyse, plan reactivation | +10-20% |

#### Buyer-Side (canonical 5-stage funnel projection)

See [`product-specs/matrix-pipeline/wiki/overview.md#pipeline`](../product-specs/matrix-pipeline/wiki/overview.md#pipeline) (FR-FNL-01..06) for the canonical funnel; cards are `(Contacts × SavedSearch)` pairs.

| Stage | Recommended Actions | Impact |
|---|---|---|
| **Qualification** | FR-AI-LQ inbound enrichment, draft `Contacts` + `SavedSearch.SearchQuery`, broker confirms | +10-30% |
| **Matching** | FR-AI-MX matches `Property` → `SavedSearch`, generate Curated List + PDF brochure, share via `ContactListings` | +15-30% |
| **Viewing** | Schedule `ShowingAppointment`, FR-AI-SC showing coach, capture `ContactListingNotes` per stop | +20-35% |
| **Contracting** | Open `TransactionManagement` row, negotiate `OfferAmount`, FR-AI-DM deal margin coach, coordinate legal services | +30-45% |
| **Payment** | Coordinate financial transactions, finalise `TransactionManagement.status = Closed`, archive `Document`s | +45-50% |
| **Closed Lost** | Set `TransactionManagement.status = Withdrawn` / `Rejected`, emit `HistoryTransactional`, analyse loss, plan re-engagement | +10-20% |

---

## System Metrics Summary

### Metrics by Element

| Element | Key Metrics | Review Cadence |
|---------|------------|----------------|
| Commission Funnel | Revenue (actual vs plan), avg check, # deals, forecast | Weekly |
| Listings | Active listings, new/period, DOM, listing→sale conversion | Weekly |
| Appointments | # meetings, meeting→deal conversion, days with showings | Weekly |
| Follow-ups | Missed follow-ups (overdue), response rate, avg response time | Daily |

### Review Rhythm
- **Weekly review**: Target vs Actual on revenue & forecast, listing status (new, active, DOM), appointment count and quality
- **Daily standup**: Missed follow-ups (overdue), new leads, hot potentials, critical actions for today

### How Metrics Are Used
Metrics drive regular management reviews for analyzing team effectiveness, identifying weak points, and correcting strategies. Weekly review focuses on results and forecast; daily standup focuses on preventing losses through missed follow-ups.
