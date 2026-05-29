---
title: Business entities — canonical RESO + project-flavour Referral
status: stable
source: raw/context-v2.md §5, §9.1, §9.2, §9.3, §9.5a, §9.7, §9.7a, §9.8, §9.9, §9.11a
last_updated: 2026-05-26
tags: [entity]
---

# Business entities — canonical RESO + project-flavour Referral

> Fifteen canonical RESO entities + one project-flavour entity (`Referral`). For each: definition, where it is mastered (write authority vs physical store), key attributes, and what concepts (Lead / Opportunity / Offer / Contract / Commission / Payment Event) are realized **without** their own entity. Column-semantics note at the bottom.

## TOC

- [#contacts](#contacts)
- [#contact-listings](#contact-listings)
- [#contact-listing-notes](#contact-listing-notes)
- [#saved-search](#saved-search)
- [#prospecting](#prospecting)
- [#showing-chain](#showing-chain)
- [#caravan](#caravan)
- [#transaction-management](#transaction-management)
- [#history-transactional](#history-transactional)
- [#referral](#referral)
- [#property](#property)
- [#activity](#activity)
- [#document](#document)
- [#campaign](#campaign)
- [#member-office-team](#member-office-team)
- [#realized-without-entity](#realized-without-entity)
- [#column-semantics-note](#column-semantics-note)

## Data-model logic

- **Contact** — a natural person + personal preferences (language, channel, lifestyle, family profile, privacy level). Does **not** store commercial parameters.
- **SavedSearch** — canonical store of the client's commercial intent (budget, goal, target locations, property type, timeline) as a RESO OData filter + human-readable form. One Contact can have multiple parallel SavedSearch rows — these are the "multiple parallel intents" (residence vs investment vs relocation).
- **Prospecting** — canonical schedule of outreach over `(Contact, SavedSearch, Member)`. Drives **two simultaneous scenarios**: (a) auto-delivery of new/updated listings to the client via email/WhatsApp; (b) reminder-`Activity` rows for the broker to maintain regular contact-rhythm even when no new matches exist.
- **ContactListings** — per-listing engagement: what was sent, what was viewed, what is in Favorite / Possibility / Discard.
- **Showing chain** (5 resources) — full lifecycle of a property showing.
- **TransactionManagement** — canonical offer/transaction entity (`TransactionType`: PurchaseOffer / LeaseOffer / ListingForSale / ListingForLease / Other).
- **Property** — the listing object from the Listing Module; `Property.StandardStatus` is the main state machine of the listing lifecycle (Active → Active Under Contract → Pending → Closed).
- **HistoryTransactional** — universal append-only audit log of all state transitions.

Source: raw/context-v2.md §5 (logic preamble).

## Contacts {#contacts}

**RESO resource**: `Contacts`. **Write authority**: CRM. **Physical store**: CDL (`public.contacts`, RLS enabled, 45 073 live rows). See [wiki/architecture.md#live-cdl-state](architecture.md#live-cdl-state).

A natural person: client, representative, partner, lawyer, family-office representative. Stores identity and personal preferences (language, preferred channel, lifestyle, family profile, privacy level, decision-maker role, tags, relationships); `ContactType` (multi-value RESO lookup: Lead / Prospect / Ready to Buy / Buyer / Seller / Landlord / Tenant / Investor / Past Client / Partner / Referral / Personal Acquaintance / Vendor / Other); `ContactStatus` (Active / On Vacation / Inactive / Deleted); `LeadSource`; `OwnerMemberKey → Member`.

Commercial parameters of the intent (budget, goal, locations, type, timeline, decision criteria) are **NOT** stored on `Contacts` — they belong on `SavedSearch.SearchQuery` (see [#saved-search](#saved-search)).

FRs: [wiki/requirements.md#fr-con-contacts](requirements.md#fr-con-contacts).

Source: raw/context-v2.md §5, §9.1, §9.4.

## ContactListings {#contact-listings}

**RESO resource**: `ContactListings` (junction Contacts × Property). **Write authority**: CRM via `cdl-write` (`resource: 'contact_listings'`). **Physical store**: CDL (`public.contact_listings`, **RLS enabled service-role-only since 2026-05-29** — 24 979 live rows re-modeled to canonical RESO; read via `cdl-contact-listings-read`, write via `cdl-write` — see [wiki/architecture.md#compliance-gates](architecture.md#compliance-gates) CDL access gate). Note: live `relationship` column holds listing provenance (`Seller`/`Developer`), not buyer-engagement preference (ADR-016).

Per-listing engagement Contact ↔ property: `ContactListingPreference` (Favorite / Possibility / Discard), `ListingViewedYN`, `ListingSentTimestamp`, `PortalLastVisitedTimestamp`, unread flags, channel (email / WhatsApp / Manual / Portal / SMS). Multiple `ContactListings` for one Contact = interactions across different properties, possibly in the context of parallel intents (different SavedSearches).

`ContactListings ↔ SavedSearch` link (for stage derivation, see [wiki/overview.md#pipeline](overview.md#pipeline) Matching condition (b)):
- (i) **preferred**: explicit `SavedSearchKey` attribute on `ContactListings` (records the intent context in which the property was sent);
- (ii) **fallback**: heuristic match — `ContactListings.Property` falls inside `SavedSearch.SearchQuery` filter at `ListingSentTimestamp`.

FRs: [wiki/requirements.md#fr-cl-contact-listings](requirements.md#fr-cl-contact-listings).

Source: raw/context-v2.md §5, §9.8.

## ContactListingNotes {#contact-listing-notes}

**RESO resource**: `ContactListingNotes`. **Write authority**: CRM via `cdl-write` (`resource: 'contact_listing_notes'`). **Physical store**: CDL (`public.contact_listing_notes`, **RLS enabled service-role-only since 2026-05-29**; canonical RESO shape; read via `cdl-contact-listings-read` op `notes`; same EF-only gate as ContactListings).

Notes on a Contact × Property pair: content, author (Agent / Contact), timestamps. Used for broker observations, client feedback after a showing, decision reasons (incl. Discard reason and Closed Lost reason).

FRs: [wiki/requirements.md#fr-cl-contact-listings](requirements.md#fr-cl-contact-listings) (FR-CL-06, FR-CL-07).

Source: raw/context-v2.md §5, §9.8.

## SavedSearch {#saved-search}

**RESO resource**: `SavedSearch`. **Write authority**: CRM. **Physical store**: CRM app DB (Lovable-managed) — Phase 2+ migration to CDL planned (see [wiki/architecture.md#phase-2-migration](architecture.md#phase-2-migration)).

Canonical store of commercial intent: `SearchQuery` (OData filter), `SearchQueryHumanReadable`, `ResourceName` (Property / Caravan / …), `ClassName`, `MemberKey` (owning broker), `SavedSearchType`. **One Contact → N SavedSearch** (multiple parallel intents — residence / investment / relocation, each with its own projected funnel stage).

Commercial parameters of the buyer's intent (budget, goal, target locations, type, timeline, decision criteria) live here, not on `Contacts`.

FRs: [wiki/requirements.md#fr-pros-prospecting](requirements.md#fr-pros-prospecting) (FR-SS-01..08 mixed in).

Source: raw/context-v2.md §5, §9.5, §9.5a.

## Prospecting {#prospecting}

**RESO resource**: `Prospecting`. **Write authority**: CRM. **Physical store**: CRM app DB — Phase 2+ migration to CDL planned.

Canonical outreach schedule over `(Contact, SavedSearch, Member)`. Fields: `ActiveYN`, `ClientActivatedYN`, `ConciergeYN`, `ScheduleType` (Daily / Weekly / Monthly / OnNewMatch / Custom), `DailySchedule`, `NextSendTimestamp`, message templates, language, email lists (`EmailTo`, `EmailCc`, `EmailBcc`). Bindings: `ContactKey → Contacts`, `SavedSearchKey → SavedSearch`, `OwnerMemberKey → Member`.

**Drives two simultaneous scenarios in Sharp SIR**:
1. **Client auto-delivery** of new/updated listings via email / WhatsApp (canonical SavedSearch delivery).
2. **Broker reminder Activity** rows — touchpoint reminders for the broker (see [wiki/entities.md#activity](#activity), FR-ACT-11 in [wiki/requirements.md#fr-act-activities](requirements.md#fr-act-activities)) to maintain regular contact-rhythm with the purchaser even when no new matches exist. The broker must respond to the reminder (call / meeting / WhatsApp / note) or explicitly deactivate Prospecting.

FRs: [wiki/requirements.md#fr-pros-prospecting](requirements.md#fr-pros-prospecting).

Source: raw/context-v2.md §5, §9.5a.

## Showing chain (5-resource) {#showing-chain}

**RESO resources**: `ShowingAvailability` → `ShowingRequest` → `ShowingAppointment` → `Showing` → `LockOrBox`. **Write authority**: CRM (CRM app DB for Availability/Request/Showing/LockOrBox; Appointment lives in CDL as `public.showings` — see [wiki/architecture.md#live-cdl-state](architecture.md#live-cdl-state) naming-drift advisory).

1. **ShowingAvailability** — listing-side posture: the owner / listing agent publishes available slots and rules.
2. **ShowingRequest** — buyer-side request: a `Member` (showing agent) or `Contacts` requests a showing.
3. **ShowingAppointment** — scheduled meeting; `ShowingAppointmentStatus` (Pending / Confirmed / Denied / Cancelled); `ShowingAgentKey → Member`.
4. **Showing** — recorded actual showing event after the meeting. `ShowingStartTimestamp`, `ShowingEndTimestamp`, `ShowingAgentKey`, `ListingKey → Property`.
5. **LockOrBox** — credential audit: lockbox / smart-key usage at the showing.

Gating: `Property.ShowingStatus` (Accepting Requests / On Hold / No Showings / Restricted Showings) and `Property.StandardStatus` (showing typically allowed only when Active / Active Under Contract, per policy).

Optional grouping: showings can be part of a `Caravan` (see [#caravan](#caravan)).

After the showing, client feedback goes into `ContactListingNotes` for the relevant Contact × Listing pair; preference is updated (Favorite / Possibility / Discard). If interest is high, a `TransactionManagement` row is created (PurchaseOffer / LeaseOffer).

FRs: [wiki/requirements.md#fr-show-showings](requirements.md#fr-show-showings).

Source: raw/context-v2.md §5, §6.4, §9.7.

## Caravan {#caravan}

**RESO resources**: `Caravan` + `CaravanStop`. **Write authority**: CRM. **Physical store**: CRM app DB — Phase 2+ migration to CDL planned.

A curated multi-property tour: `CaravanStatus` (Active / Canceled / Ended), `CaravanType` (Broker / AOR / Other), `CaravanOrganizerKey`, `CaravanAllowedStatuses`. `CaravanStop` rows are ordered stops linked to a `Property`.

Typical luxury scenario: an assistant / GR-consultant takes a UHNWI client / family-office representative through 3–7 properties in one city in a single day. `Caravan` is a first-class canonical entity for these invitation-only tours.

`OpenHouse` (public open houses) is excluded from CRM scope; invitation-only showings via the Showing chain, optionally grouped in a Caravan. See [wiki/architecture.md#escape-hatch](architecture.md#escape-hatch).

FRs: [wiki/requirements.md#fr-cara-caravan](requirements.md#fr-cara-caravan).

Source: raw/context-v2.md §5, §9.7a.

## TransactionManagement {#transaction-management}

**RESO resource**: `TransactionManagement`. **Write authority**: CRM. **Physical store**: CRM app DB — Phase 2+ migration to CDL planned.

Canonical resource for offers and transactions: `TransactionType` (PurchaseOffer / LeaseOffer / ListingForSale / ListingForLease / Other). Lifecycle (Draft → Submitted → Countered → Accepted → Rejected / Withdrawn / Expired) is expressed through `HistoryTransactional` rows + `Property.StandardStatus` transitions.

The TM card carries the **forecast P&L block** from the Commission Engine subsystem ([wiki/commission-engine.md](commission-engine.md)) — forecast GCI, attributed costs, net margin, per-broker compensation; after deal close, the **variance** (actual − forecast) computed from reconciliation with the external Finance ERP (FR-TM-13).

`OfferAmount` is the **preferred forecast base** when populated (FR-FNL-12 precedence (a)): switching from `SavedSearch` budget mid-point (b) → `OfferAmount` (a) emits `HistoryTransactional` row (`MajorChangeType = Forecast base change`, `ChangeType = SavedSearch budget → OfferAmount`).

FRs: [wiki/requirements.md#fr-tm-transactions](requirements.md#fr-tm-transactions).

Source: raw/context-v2.md §5, §9.9.

## HistoryTransactional {#history-transactional}

**RESO resource**: `HistoryTransactional`. **Write authority**: CRM. **Physical store**: CDL (`public.history_transactional`, RLS enabled, append-only, 0 live rows on 2026-05-18 — initial state).

Universal append-only audit log of all state transitions: `ResourceName` + `ResourceRecordKey` + `MajorChangeType` + `ChangeType` + `EntityEventSequence`. Emitted on every funnel stage transition, every offer state change, every `Property.StandardStatus` transition, events from external systems (contracts, payments).

Full emission contract (when emission is mandatory, payload fields) — see [wiki/integration.md#history-emission](integration.md#history-emission).

Source: raw/context-v2.md §5, §10.7.

## Referral {#referral}

**Project-flavour entity** (NOT canonical RESO; see [wiki/architecture.md#escape-hatch](architecture.md#escape-hatch)). **Write authority**: CRM. **Physical store**: CRM app DB (Lovable-managed); **never** planned for CDL migration.

Records the act of recommending a client / partner / broker / other agent. Links two `Contacts` (referrer ↔ referee) and optionally a `Member` (responsible broker who received the referral). The source of the referral is reflected in `Contacts.LeadSource = Referral` for the referee.

Conceptual fields (designed in Lovable): referrer `ContactKey`, referee `ContactKey`, `OwnerMemberKey → Member`, `ReferralType` (Client / Partner / Broker / Internal), `Outcome` (open / Closed Won / Closed Lost), `CloseDate`, `CreatedAt`.

FK pattern: references canonical `Contacts.ContactKey` in CDL through CRM-app-DB → CDL logical FK (not a canonical RESO relationship).

Deliverable: `ADR-XXX: CRM Referral Entity for Luxury Segment` in `matrix-platform-kb/docs/architecture/decisions/`.

FRs: [wiki/requirements.md#fr-ref-referral](requirements.md#fr-ref-referral).

Source: raw/context-v2.md §5, §9.11a, §11.6.

## Property {#property}

**RESO resource**: `Property`. **Write authority**: Listing Module (out of CRM scope). **Physical store**: CDL (`public.properties`, **RLS disabled** — EF-only access for CRM; 16 014 live rows). Anonymous snapshot via `public.properties_published` (RLS enabled, 13 916 rows).

CRM uses `Property` via integration only (see [wiki/integration.md#listing-module](integration.md#listing-module)); the key state machine is `Property.StandardStatus` (Coming Soon / Active / Hold / Active Under Contract / Pending / Closed / Withdrawn / Canceled / Expired).

CRM never edits property master data. CRM-side observation only: the linkage `ContactListings.ListingKey → Property` and the `Property.StandardStatus` transitions pushed by CRM via Listing Module integration.

Source: raw/context-v2.md §5, §10.

## Activity {#activity}

**App-private**. **Write authority**: CRM. **Physical store**: CRM app DB. Never CDL.

Call, task, meeting, letter, WhatsApp, follow-up. Linked to `Contacts`, `SavedSearch`, `Prospecting`, `ContactListings`, `ShowingAppointment`, `Showing`, `TransactionManagement`, `Caravan` and/or `Property`. For commercial context, an Activity is at minimum linked to a `(Contacts, SavedSearch)` pair or to a `TransactionManagement` row.

Carries extended markup for **cost attribution** to the Commission Engine subsystem (see FR-ACT-10 in [wiki/requirements.md#fr-act-activities](requirements.md#fr-act-activities), and [wiki/commission-engine.md](commission-engine.md)).

Used as the **touchpoint reminder** mechanism for Prospecting (broker side) — see [#prospecting](#prospecting) and FR-PROS-09 / FR-PROS-13.

FRs: [wiki/requirements.md#fr-act-activities](requirements.md#fr-act-activities).

Source: raw/context-v2.md §5, §9.6.

## Document {#document}

**App-private (metadata only)**. **Write authority**: CRM. **Physical store**: CRM app DB for metadata; file blobs in external systems / blob storage.

A document linked to `Contacts`, `TransactionManagement`, the Showing chain, or an Activity. Contracts are stored in the external contract management system (see [wiki/integration.md#contract-system](integration.md#contract-system)); CRM holds references only. NDA level can be applied to a Document for restricted access (BR-07).

FRs: [wiki/requirements.md#fr-doc-documents](requirements.md#fr-doc-documents).

Source: raw/context-v2.md §5, §9.11.

## Campaign {#campaign}

**Marketing system / CRM (metadata only)**. **Write authority**: marketing system (campaign definition) / CRM (linking to `Contacts.LeadSource`). **Physical store**: CRM app DB for CRM-side bookkeeping.

A campaign or source of a marketing inquiry. Linked via `Contacts.LeadSource`.

Source: raw/context-v2.md §5.

## Member / Office / OUID / Teams / TeamMembers {#member-office-team}

**RESO business roster** — canonical org-model. **Write authority**: CDL (target state for all). **Physical store**:
- `Member`, `Office` — CDL (`public.members` 129 rows, `public.offices` 59 rows, RLS enabled). Phase 1 live.
- `OUID`, `Teams`, `TeamMembers` — CDL is the target write authority **but** not yet physically in live CDL on 2026-05-18; until Phase 2+ migration `Teams` and `TeamMembers` live in CRM app DB (Lovable-managed); `OUID` is TBD.

The **Roster gate** (see [wiki/architecture.md#compliance-gates](architecture.md#compliance-gates)) applies to the target state, not the current physical placement.

User identity (SSO account, roles, groups, scope claims, permissions) is **separate from CDL Member**, in the SSO project (`xgubaguglsnokjyudgvc`). Mapping: SSO `user_id` ↔ `Member.MemberKey` via canonical `Member.MemberAlternateId` or an explicit mapping in the SSO Console. See [wiki/architecture.md#identity-boundary](architecture.md#identity-boundary).

FRs: [wiki/requirements.md#fr-con-contacts](requirements.md#fr-con-contacts) (FR-ORG-01..04) — yes, organizational FRs are grouped near Contacts because of `OwnerMemberKey` etc.

Source: raw/context-v2.md §5, §9.3.

## Concepts realized without their own entity {#realized-without-entity}

| Concept | Where it is realized instead of being a standalone entity |
|---|---|
| `Lead` | `Contacts.ContactType = Lead` (ContactType funnel: Lead → Prospect → Ready to Buy → Buyer / Seller / …). |
| `Opportunity` | Projection over `(Contacts.ContactType + N×SavedSearch + N×Prospecting + N×ContactListings + optional TransactionManagement + Property.StandardStatus)`. The 5-stage pipeline persists as a UI/UX projection (see [wiki/overview.md#pipeline](overview.md#pipeline)), not as a stored entity. |
| `Opportunity Property Interest` | `ContactListings` + `ContactListingPreference` (Favorite / Possibility / Discard) + Showing chain rows + `TransactionManagement` rows. |
| `Offer` | `TransactionManagement` (TransactionType: PurchaseOffer / LeaseOffer) + `HistoryTransactional` for lifecycle statuses + push of `Property.StandardStatus`. |
| `Viewing` (as a single entity) | Canonical 5-resource Showing chain. |
| `Contract` | Business goal: `Property.StandardStatus` transitions (`Active Under Contract` → `Pending` → `Closed`) + `HistoryTransactional` + external contract system (e-sign, versions, documents). |
| `Commission` | Business goal: forecast lives in CRM ([wiki/commission-engine.md](commission-engine.md)); the actual ledger lives in external Finance ERP. CRM does not store a commission ledger. |
| `Payment Event` | Business goal: webhook from Finance ERP → `Property.StandardStatus` transitions + `HistoryTransactional`. |
| `Organization` (as a standalone entity) | Canonical `Office` / `OUID` (for brokerages and MLS-organizations) + `Contacts.Company` / `Contacts.JobTitle` (for family offices, banks, developers, law firms as counterparties). |

Source: raw/context-v2.md §5 (table at the bottom of the section).

## Note (column semantics) {#column-semantics-note}

The "Where it is mastered" column in raw/context-v2.md §5 reflects **write authority** (which app initiates CRUD operations), not necessarily the physical store. Concretely:

- **CRM is write authority, CDL is physical store** (CRM writes via dedicated CDL EFs under SSO JWT scope): `Contacts`, `ContactListings`, `ContactListingNotes`, `HistoryTransactional`, `ShowingAppointment` (table `public.showings`).
- **CRM is write authority AND physical store** in CRM app DB (Lovable-managed) until Phase 2+ migration to CDL: `SavedSearch`, `Prospecting`, `Caravan`, `CaravanStop`, `ShowingAvailability`, `ShowingRequest`, `Showing` (separate resource), `LockOrBox`, `TransactionManagement`.
- **CDL is both write authority and physical store** (Phase 1 live): `Member`, `Office`.
- **CDL is target write authority** but currently absent in live CDL (Phase 2+ migration; today data in CRM app DB or TBD): `OUID`, `Teams`, `TeamMembers`. Roster gate applies to the target state.
- **Listing Module is write authority**, CDL is physical store: `Property`. CRM uses via integration only ([wiki/integration.md#listing-module](integration.md#listing-module)).
- **CRM is write authority AND physical store; never CDL** (project-flavour app-private / non-canonical): `Activity`, `Document` (metadata; files in external storage), `Campaign` (CRM-side bookkeeping), `Referral`.

Source: raw/context-v2.md §5 column-semantics note.
