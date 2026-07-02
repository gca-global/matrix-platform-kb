# Sharp Matrix × 23 Deal Tasks — Value Map

> Maps the Alloy Advisors "23 Tasks of a Deal" framework to Sharp Matrix apps, delivery status, and value levers.
> Source: Alloy Advisors — *The Home Sale Transaction, Reconsidered* (June 2026) + Sharp Matrix Platform KB (June 2026).
> Last updated: June 2026

## Purpose

Executive and product teams use this doc to explain **how Sharp Matrix generates additional value** at each step of a real estate transaction. It bridges an external deal-workflow taxonomy (Alloy Advisors) with the platform's own CRM model (6 processes, 5-stage funnel, 25 apps on one CDL).

**Core thesis** ([core-beliefs.md](core-beliefs.md)):

> *The broker works with the client. The system works with the process.*

## Value model

| Lever | Mechanism | Scale benchmark (50 agents) |
|---|---|---|
| **Lever 1 — Cost stripped** | Automate commodity admin, coordination, documentation (~7% of GCI friction) | +€0.57M/yr on ~180 deals |
| **Lever 2 — Hours reinvested** | Free ~15 hrs/deal (~40% of 30–50 agent hours) → capacity for +1 deal/agent/yr | +€2.28M/yr at €45.6K avg commission |

Combined: **~€8.2M GCI baseline → ~€11.0M** (~35% lift), before full conversion gains.

On a single **$400K deal**, ~**$39,660** of friction cost can become brokerage margin when the 10 AI-WIN tasks are automated.

## Alloy classification legend

| Class | Count | Meaning for Sharp Matrix |
|---|---|---|
| **AI WIN** | 10 | Platform automates or will automate; primary Lever 1 target |
| **PARITY** | 10 | Broker + platform together; Matrix augments speed, data, coordination |
| **HUMAN WIN** | 3 | Broker-only; Matrix returns time via Lever 2 |

## Platform enablers (all stages)

| Enabler | Role |
|---|---|
| **SSO Console** | One identity across 25 apps |
| **CDL (Common Data Layer)** | One RESO-canonical data truth; enter once, syndicate everywhere |
| **Agency Portal** | Orchestration hub, KPIs, app launcher, AI advisor |
| **EDW + MLS Pipelines** | 3-market ingest every 15 min (CY, HU, KZ) |

## Task map

### Pre-Listing (4 tasks — all AI WIN)

| # | Task | Sharp Matrix apps | Value | Status | Lever |
|---|---|---|---|---|---|
| 1 | Pricing analysis | Matrix Analytics (Auto Forecast), Matrix Pipeline Commission Engine + Reports, CDL comparables via EDW | Data-grounded CMA in minutes, not days | IN PROGRESS | L1 + L2 |
| 2 | Listing description | Matrix Atlas MLS → Website CMS; AI Blog Generator; Pipeline FR-AI-PROP (planned) | Luxury-tone drafts from verified property data | PARTIAL LIVE | L1 |
| 3 | Photo brief | Atlas Media lifecycle (`property_media`); Matrix Stardom prompt templates | Structured shoot brief from listing attributes | PARTIAL | L1 |
| 4 | MLS entry | Matrix Atlas MLS + `mls-sync` → CDL → portals/website | Enter once, syndicate everywhere (RESO-canonical) | **LIVE** | L1 |

### Marketing (6 tasks — 5 AI WIN, 1 PARITY)

| # | Task | Sharp Matrix apps | Value | Status | Lever |
|---|---|---|---|---|---|
| 5 | Marketing plan | Agency Portal KPIs, Matrix Analytics; Marketing App (planned) | Plan from live pipeline/listing data, not spreadsheets | PLANNED-HEAVY | L1 + L2 |
| 6 | Digital ads | Website CMS, AI Web Assistant lead capture; CDL `InternetTracking` | Leads in 30 min not 4 hrs; measurable CTR | PARTIAL LIVE | L1 + L2 |
| 7 | Social posts | AI Blog Generator, listing syndication to web/social | Always-current inventory posts | PARTIAL LIVE | L1 |
| 8 | Buyer outreach | Pipeline Prospecting cron + Curated Lists; Matrix Comms campaigns + AI replies | Personalized outreach at scale | **LIVE** | L1 + L2 |
| 9 | Showings scheduling | Pipeline Showing chain + O365 calendar-sync; Meeting Hub | Zero double-booking; calendar = CRM truth | **LIVE** | L1 |
| 10 | Tour conducting | Pipeline Caravan/Curated Lists; FR-AI-VIEW prep (planned) | Broker arrives prepared; human conducts tour | PARITY | L2 |

### Engagement (4 tasks — all PARITY)

| # | Task | Sharp Matrix apps | Value | Status | Lever |
|---|---|---|---|---|---|
| 11 | Open houses | CDL `OpenHouse`, Pipeline showings; Meeting Hub analytics | Attendance → CRM engagement automatically | LIVE | L2 |
| 12 | Buyer Q&A | AI Web Assistant (public); Zoe + Portal AI Advisor; Comms AI replies | Instant answers, qualified handoff to broker | **LIVE** | L1 + L2 |
| 13 | Lead nurture | Prospecting engine + `ContactListings` engagement; Comms; FR-AI-COM (planned) | Zero missed follow-ups (platform target) | PARTIAL LIVE | L1 + L2 |
| 14 | Offer drafting | Pipeline `TransactionManagement`; external e-sign; FR-AI-NEG (planned) | Offer history + audit trail; faster first draft | IN PROGRESS | L1 |

### Negotiation (5 tasks — 1 AI WIN, 1 PARITY, 3 HUMAN WIN)

| # | Task | Sharp Matrix apps | Value | Status | Lever |
|---|---|---|---|---|---|
| 15 | Counter-offers | TM + `HistoryTransactional` audit; FR-AI-NEG brief (planned) | Full offer lineage, no lost context | IN PROGRESS | L1 |
| 16 | Negotiation execution | Pipeline deal brief + margin coach (planned); broker executes | ~15 hrs/deal returned for high-stakes negotiation | HUMAN WIN | L2 |
| 17 | Emotional support | No automation — time freed from commodity tasks | Client relationship funded by Lever 2 | HUMAN WIN | L2 |
| 18 | Hyperlocal judgment | FR-AI-MKT market notes (planned); broker decides | AI cites sources; broker applies local expertise | HUMAN WIN | L2 |
| 19 | Doc prep | Pipeline `Document` refs; O365 email-attach; external contract (FR-FNL-23) | Docs linked to deal, not email threads | IN PROGRESS | L1 |

### Closing (4 tasks — all PARITY)

| # | Task | Sharp Matrix apps | Value | Status | Lever |
|---|---|---|---|---|---|
| 20 | Transaction coord | Pipeline TM lifecycle + status webhooks; Commission Engine; Matrix FM | Single deal timeline, manager visibility | IN PROGRESS | L1 |
| 21 | Inspection coord | Pipeline `Activity` tasks on transaction timeline | Coordinated milestones, reminders | IN PROGRESS | L1 |
| 22 | Title / escrow | Finance ERP webhook → `Property.StandardStatus`; Matrix FM reconciliation | CRM reflects legal/financial reality automatically | IN PROGRESS | L1 |
| 23 | Closing logistics | Closed Won = Closed + TM + payment webhook; Commission Engine → FM | Faster close, accurate commission forecast | IN PROGRESS | L1 + L2 |

## Delivery status summary

| Status | Task count | Examples |
|---|---|---|
| **LIVE** | 6 | MLS entry, buyer outreach, showings scheduling, buyer Q&A, open houses |
| **PARTIAL LIVE** | 5 | Listing description, digital ads, social posts, lead nurture, doc prep |
| **IN PROGRESS** | 9 | Pricing analysis, offer drafting, counter-offers, transaction coord, closing |
| **PLANNED-HEAVY** | 1 | Marketing plan (Marketing App) |
| **HUMAN WIN** | 3 | Negotiation execution, emotional support, hyperlocal judgment |

## AI honesty note

Pipeline **AI Broker Co-Pilot** features (FR-AI-LQ, FR-AI-MX, FR-AI-SC, FR-AI-DM, FR-AI-NEG, FR-AI-MKT, etc.) are extensively specified in [`product-specs/matrix-pipeline/wiki/ai.md`](../product-specs/matrix-pipeline/wiki/ai.md) but **most are not yet shipped**. Live AI today:

- Matrix Comms — AI reply suggestions (HumaticAI)
- Agency Portal — AI Advisor (`portal-agent-chat`)
- Zoe AI Assistant — internal RAG support
- AI Web Assistant — public website lead capture
- AI Blog Generator — SEO content
- Matrix Stardom — shared AI workspace + scheduled prompts
- Pipeline Prospecting cron — automated property matching (non-LLM)

Do not present planned Copilot features as live in executive materials.

## Mapping to platform CRM model

The platform's canonical buyer funnel ([`product-specs/matrix-pipeline/wiki/overview.md#pipeline`](../product-specs/matrix-pipeline/wiki/overview.md#pipeline)) projects over `(Contacts × SavedSearch)`:

| Funnel stage | 23-task stages covered |
|---|---|
| Qualification | Pre-listing (seller), marketing (lead capture), engagement (nurture) |
| Matching | Marketing (buyer outreach), pre-listing (pricing) |
| Viewing | Marketing (showings, tours), engagement (open houses, Q&A) |
| Contracting | Engagement (offer drafting), negotiation (counter-offers, doc prep) |
| Payment / Closed | Negotiation (execution), closing (coord, inspection, title, logistics) |

## Related docs

- [core-beliefs.md](core-beliefs.md) — operating philosophy
- [ai-driven-sales-model.md](ai-driven-sales-model.md) — 4 value engines (Funnel, Listings, Appointments, Follow-ups)
- [digital-strategy-2026-2028.md](digital-strategy-2026-2028.md) — KPI targets (90%+ automation, 50–60 day cycle)
- [app-catalog.md](../platform/app-catalog.md) — full app inventory and delivery status
- [ecosystem-architecture.md](../platform/ecosystem-architecture.md) — platform layer stack

## KB sources consulted

- `docs/vision/core-beliefs.md`
- `docs/vision/ai-driven-sales-model.md`
- `docs/vision/digital-strategy-2026-2028.md`
- `docs/platform/app-catalog.md`
- `docs/platform/ecosystem-architecture.md`
- `docs/product-specs/matrix-pipeline/wiki/ai.md`
- `docs/product-specs/matrix-pipeline/wiki/processes.md`
