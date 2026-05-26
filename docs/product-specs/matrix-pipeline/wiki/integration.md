---
title: External integrations
status: stable
source: raw/context-v2.md §10.1, §10.2, §10.3, §10.4, §10.5, §10.6, §10.7, §10.8, §10.9, §10.10
last_updated: 2026-05-26
tags: [integration]
---

# External integrations

> CRM is not the master system for properties, contracts, or actual money. Listing Module owns properties; the external contract system owns contracts; the external Finance ERP owns the commission ledger and payment events. The CRM-internal Commission Engine ([wiki/commission-engine.md](commission-engine.md)) is a **forecast / advisory** counterpart to the Finance ERP, connected via a reconciliation pattern. This page consolidates the contracts, gates, and webhook patterns.

## TOC

- [#listing-module](#listing-module)
- [#standard-status](#standard-status)
- [#crm-to-listing-push](#crm-to-listing-push)
- [#history-emission](#history-emission)
- [#contract-system](#contract-system)
- [#finance-erp-commission](#finance-erp-commission)
- [#finance-erp-payments](#finance-erp-payments)
- [#sso](#sso)
- [#cdl](#cdl)

## Primary statement {#primary}

The Sales & Contact Management System is not the master for:

- Properties → owned by the **Listing Management Module**.
- Contracts → owned by the **external contract system** (e-signature provider).
- Commission ledger / payment events → owned by the **external Finance ERP** (1C / Xero / QuickBooks / SAP / Bitrix24 Finance / proprietary) and the connected banking channels / payment gateways.

CRM uses data from these systems via integrations for the sales process (matching, deal handling, showings, communications, offers, pipeline analytics). Contracts and payment events are **business goals**, not first-class CRM data-model entities — in canonical RESO DD 2.0, commission ledger / escrow milestones / rich contract objects are intentionally out of scope (see [`canonical-processes/processes/transaction-lifecycle.md`](../../../business-processes/canonical-processes/processes/transaction-lifecycle.md)).

**Exception — the CRM-internal ERP-lite Commission Engine** ([wiki/commission-engine.md](commission-engine.md)): for sales-broker P&L transparency CRM keeps its own forecasting / rule engine / per-deal P&L subsystem. This is an explicit project-flavour deviation from RESO ([wiki/architecture.md#escape-hatch](architecture.md#escape-hatch)) — it does not duplicate the external Finance ERP; the two are connected via the [#finance-erp-commission](#finance-erp-commission) reconciliation pattern.

**Shared principles** (apply to all of [#contract-system](#contract-system), [#finance-erp-commission](#finance-erp-commission), [#finance-erp-payments](#finance-erp-payments)):

- External systems are the **single ledger / source of truth** for contracts (parties, versions, terms, exclusivity, jurisdiction, templates), commission split (currencies, taxes, net/gross, statuses), and payment events (escrow, wire, letter of credit, deposit, notarial account).
- **Canonical RESO mirror in CRM**: `Property.StandardStatus` is the main listing/deal-lifecycle state machine (`Active Under Contract` → `Pending` → `Closed`, with rollback to `Active` / `Withdrawn` on cancel/refund); `TransactionManagement` carries `TransactionType`; `HistoryTransactional` is the append-only audit log per webhook event; `Document` stores references to signed contracts, invoices, bank docs; `Activity` carries tasks / reminders / notifications spawned by webhook events.
- **Transport**: webhook (primary) or periodic sync; CRM exposes endpoints, external systems push events.
- **Notifications** to `OwnerMemberKey`, sales manager, managing partner — in-app + email + optional WhatsApp; implemented as `Activity` rows.
- **Access control**: confidential / NDA / standard levels on related `Document` and `ContactListingNotes`; financial visibility (`ClosePrice`, commission forecast, payment timestamps) gated to finance / managing partner / responsible `Member` via RLS on canonical resources.
- **Audit / reconciliation**: reconciliation of contracts, commissions, payments happens **in external systems** as the single source of truth; CRM holds a mirror audit via `HistoryTransactional` for analytics and UI timelines.

Source: raw/context-v2.md §10.1.

## Listing Module integration {#listing-module}

CRM consumes property data from the Listing Module. CRM cannot edit property master data. The Listing Module is the single source of truth for everything the property *is*.

### Business requirements

| ID | Requirement | Priority |
|---|---|---|
| BR-LI-01 | CRM must receive up-to-date property data from the Listing Module | High |
| BR-LI-02 | Listing Module is the sole source of truth for property data | High |
| BR-LI-03 | Brokers must be able to use Listing Module properties in deals, showings, shortlists, and communications | High |
| BR-LI-04 | CRM must not allow editing property master data | High |
| BR-LI-05 | CRM must prevent use of unavailable / sold / archived / private properties without explicit rights | High |
| BR-LI-06 | CRM must allow tracking client interest in properties without modifying listings | High |
| BR-LI-07 | Leadership must see property sales analytics (showings, interest, offers, deals) | Medium |
| BR-LI-08 | CRM must support off-market / private properties subject to Listing Module access rights | High |

### Integration FRs

| ID | Requirement | Priority |
|---|---|---|
| INT-LI-01 | Fetch properties from Listing Module via API | High |
| INT-LI-02 | Scheduled or near-real-time data updates | High |
| INT-LI-03 | Webhook events on status / price / privacy-level changes | Medium/High |
| INT-LI-04 | Search and filter properties by key parameters | High |
| INT-LI-05 | Only properties the user is allowed to see may be returned | High |
| INT-LI-06 | Store the external `Property ID` (canonical `ListingKey`) for linkage | High |
| INT-LI-07 | Log integration errors | High |
| INT-LI-08 | Show last sync timestamp per property | Medium |
| INT-LI-09 | When the Listing Module is unavailable, show previously cached snapshots with a stale-data marker | Medium |
| INT-LI-10 | Support pushing back to the Listing Module: views, showings, interest, offers — when required by the business process | Medium |

### Minimum dataset CRM consumes from Listing Module

| Field | Mandatory |
|---|---|
| `ListingKey` (Property ID) | Mandatory |
| `UnparsedAddress` / `StreetName` / `City` / `StateOrProvince` / `PostalCode` / `Country` | Mandatory |
| `PropertyType` / `PropertySubType` | Mandatory |
| `ListPrice` | Mandatory |
| `StandardStatus` | Mandatory |
| `ShowingStatus` | Mandatory |
| Title / name (`PublicRemarks` / `BrokerRemarks`) | Recommended |
| `BedroomsTotal` / `BathroomsTotalInteger` / `LivingArea` / `LotSizeAcres` | Recommended |
| Media references | Recommended |

Source: raw/context-v2.md §10.2, §10.3, §10.4.

## `Property.StandardStatus` reference {#standard-status}

CRM uses the canonical RESO lookup `Property.StandardStatus` as the main lifecycle state machine. **No custom enums.** See [`canonical-processes/processes/listing-lifecycle.md`](../../../business-processes/canonical-processes/processes/listing-lifecycle.md).

| Value | Meaning |
|---|---|
| `Coming Soon` | Property being prepared for publication; no requests or showings yet |
| `Active` | Active; showings and offers accepted (per `ShowingStatus`) |
| `Hold` | Temporary pause; showings paused |
| `Active Under Contract` | Offer accepted; contract under negotiation / signing |
| `Pending` | Contract signed; awaiting closing |
| `Closed` | Transaction closed; `CloseDate`, `ClosePrice` recorded |
| `Withdrawn` | Listing withdrawn without a transaction |
| `Canceled` | Listing agreement cancelled |
| `Expired` | Listing agreement expired |

Source: raw/context-v2.md §10.5.

## CRM → Listing Module push events {#crm-to-listing-push}

| Event | CRM trigger | Effect in Listing Module |
|---|---|---|
| `OfferAccepted` | `TransactionManagement` + `HistoryTransactional` (`ChangeType=Accepted`) | `Property.StandardStatus = Active Under Contract`; emit `HistoryTransactional` on Property |
| `ContractSigned` | Webhook from external contract system ([#contract-system](#contract-system)) | `Property.StandardStatus = Pending`; emit `HistoryTransactional` |
| `FullPaymentReceived` | Webhook from Finance ERP ([#finance-erp-payments](#finance-erp-payments)) | `Property.StandardStatus = Closed`, `CloseDate`, `ClosePrice`; emit `HistoryTransactional` |
| `OfferWithdrawn` / `ContractCancelled` | `HistoryTransactional` (`ChangeType=Withdrawn` / `Cancelled`) | Roll back `Property.StandardStatus` to `Active` (or `Withdrawn` if the listing agreement is terminated too) |
| `ShowingFeedback` | `Showing` row + `ContactListingNotes` | Forward anonymized feedback to listing agent / owner (optional per policy) |

Source: raw/context-v2.md §10.6.

## `HistoryTransactional` emission contract {#history-emission}

Every state transition relevant to canonical RESO processes MUST emit a `HistoryTransactional` row. Canonical contract: [`canonical-processes/processes/history-and-audit-log.md`](../../../business-processes/canonical-processes/processes/history-and-audit-log.md).

| Field | Value |
|---|---|
| `HistoryTransactionalKey` | UUID |
| `ResourceName` | Canonical resource name: `Contacts`, `SavedSearch`, `Prospecting`, `ContactListings`, `ShowingAppointment`, `Showing`, `Caravan`, `TransactionManagement`, `Property`, `Referral` |
| `ResourceRecordKey` | Primary key of the modified record |
| `MajorChangeType` | High-level category — e.g. `ContactType change`, `Stage transition`, `Offer lifecycle`, `Status change`, `Payment event`, `Forecast base change`, `Referral created`, `Referral outcome` |
| `ChangeType` | Detail — e.g. `Lead → Prospect`, `Matching → Viewing`, `Submitted`, `Active → Pending`, `Partial Payment`, `SavedSearch budget → OfferAmount`, `Closed Won` |
| `ChangeTimestamp` | Server timestamp |
| `EntityEventSequence` | Sequence number to order events per resource |
| `ChangedByMemberKey` | `Member` (if a human initiated) or a system actor |
| `ChangeSource` | Manual / AI suggested + approved / External webhook (contract system, finance ERP) |

Emission is mandatory for:

- any `Contacts.ContactType` graduation;
- any create / close / reactivate of `SavedSearch` or `Prospecting`;
- any `ContactListings.ContactListingPreference` change or `ListingSentTimestamp` / `ListingViewedYN` transition;
- any `ShowingAppointmentStatus` transition and create of `Showing` / `LockOrBox`;
- any `CaravanStatus` transition;
- any `TransactionManagement` lifecycle event (Draft / Submitted / Countered / Accepted / Rejected / Withdrawn / Expired);
- any `Property.StandardStatus` transition (triggered by a push event or external webhook);
- any forecast-base switch in the Commission Engine ([wiki/commission-engine.md](commission-engine.md)) — `SavedSearch` budget mid-point ↔ `TransactionManagement.OfferAmount` (FR-FNL-12);
- any create / outcome update of a `Referral` row ([wiki/processes.md#referral-lifecycle](processes.md#referral-lifecycle), FR-REF-07, FR-REF-08).

Source: raw/context-v2.md §10.7.

## External contract system {#contract-system}

All contract details and versions live in the external contract system (e-signature provider) as the single source of truth; CRM reacts to webhook events and mirrors state via `Property.StandardStatus` + `HistoryTransactional`. See [#primary](#primary) for the shared principles.

- **Contract templates** (in external system): reservation agreement, sales agreement, purchase contract, rental agreement, listing agreement (sole / exclusive / open), buyer representation, NDA, commission agreement, referral agreement.
- **Webhook events** and CRM transitions:
  - `signed` → `Property.StandardStatus = Pending` + `HistoryTransactional` (`ChangeType = Pending`);
  - `cancelled` → `Property.StandardStatus = Active` (or `Withdrawn` if the listing agreement ends too) + `HistoryTransactional`;
  - `amended` / `expired` → `HistoryTransactional` with the corresponding `ChangeType`, no mandatory `Property.StandardStatus` change.
- **Reminders for key dates**: signing deadline, expiry, renewal, milestone payments — created as `Activity` rows on webhook events.
- **Versions and signed copies** — only in the external system. CRM holds only `Document` references with metadata (type, status, date, parties).

Source: raw/context-v2.md §10.8.

## Finance ERP — commission ledger (reconciliation with Commission Engine) {#finance-erp-commission}

The commission ledger lives in the **external Finance ERP** as the single source of truth for actual money flow (legally significant register of earned and paid commissions, taxes, currency conversion, invoices, bank details). CRM has its own ERP-lite subsystem ([wiki/commission-engine.md](commission-engine.md)) that holds **forecast GCI and the rule engine as an advisory tool** for the sales broker; the two systems are independent and connected via the reconciliation pattern below.

**Pattern**: the external ERP pushes a webhook (e.g. `commission_recorded`) with actual GCI and the final commission split; CRM ingests the actual into the Commission Engine, re-runs compensation derivation, computes variance (forecast vs actual), and on threshold breach emits a `HistoryTransactional` row + an `Activity` notification for the responsible `Member` / sales manager. The concrete handler (events, payload schema, thresholds, ChangeTypes) is designed in Lovable.

**Closed Won gating** ([wiki/overview.md#pipeline](overview.md#pipeline)): `Property.StandardStatus = Closed` + full-payment webhook from ERP ([#finance-erp-payments](#finance-erp-payments)) + an existing `TransactionManagement` row + reconciliation in [wiki/commission-engine.md](commission-engine.md) completed.

**What CRM does NOT do**: it does not maintain a legally significant ledger, does not issue invoices, does not pay out money. Forecast and compensation derivation in the Commission Engine are an operational advisory tool, not a legal record.

Source: raw/context-v2.md §10.9.

## Finance ERP — payment events (reconciliation with Commission Engine) {#finance-erp-payments}

Payment events (`deposit_received` / `partial_payment` / `full_payment` / `refund`) arrive in CRM via webhook from the external Finance ERP and connected banking channels. CRM reacts by transitioning `Property.StandardStatus` (Active Under Contract → Pending → Closed, or rolling back to Active / Withdrawn on refund), emits a `HistoryTransactional` row, and creates `Activity` notifications for broker / sales manager / managing partner.

`full_payment` additionally triggers **reconciliation in the Commission Engine** (update actual GCI → recompute compensation → variance). After reconciliation, the **AI Deal Margin Coach** ([wiki/ai.md#deal-margin-coach](ai.md#deal-margin-coach)) highlights variance and proposes root-cause analysis. Concrete handlers, payload schemas, and the set of `HistoryTransactional` ChangeTypes are designed in Lovable.

Source: raw/context-v2.md §10.10.

## SSO {#sso}

SSO issues all JWTs (ES256, ADR-011) and is the single source of truth for identity, roles, groups, scope claims, and permissions. CRM is an SSO **client**.

- `ssoClient` → SSO project `xgubaguglsnokjyudgvc`.
- Auth: OAuth 2.0 + PKCE via Matrix SSO Edge Functions (see `docs/platform/sso-edge-functions.md`).
- The JWT is then presented to **all three** projects (SSO + CDL + CRM app DB) — single identity chain.
- User display names: only via the SSO `resolve-users` EF + React hook `useUserDisplay`. **Never** SQL-join CDL ↔ `sso_users`.

Mapping to CDL business roster (`Member` / `Teams`): SSO `user_id` ↔ `Member.MemberKey` via canonical `Member.MemberAlternateId` or an explicit mapping in the SSO Console. See [wiki/architecture.md#identity-boundary](architecture.md#identity-boundary).

Source: raw/context-v2.md §4, §5a.2.

## CDL {#cdl}

CDL (`ofzcokolkeejgqfjaszq`) is the system-of-record for canonical RESO resources. CRM is a CDL **client**.

- `cdlClient` — CDL reads under the SSO JWT via Supabase Third-Party Auth (ADR-012) + CDL EFs for writes.
- **No direct service-role access** from CRM. CRM never holds the CDL service-role key.
- **Reads**: filtered listings via `cdlClient.functions.invoke('listings-search', …)`; anon snapshot via `.from('properties_published').select(...)` (RLS-enabled view); PII tables (`contacts`, `showings`) only through CDL EFs with scope check.
- **Writes**: through dedicated CDL EFs (`verify_jwt=false`, EF verifies SSO JWT and checks scope). CRM-specific write-EFs are added per resource as needed; a generic `cdl-write` EF is not yet built in the platform template.
- **CDL access gate**: any CDL table with RLS disabled MUST be accessed only via CDL EFs (see [wiki/architecture.md#compliance-gates](architecture.md#compliance-gates) CDL access gate).

Source: raw/context-v2.md §5a.3, §5a.4.
