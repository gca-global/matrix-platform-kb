---
title: Requirements — BRs + FR clusters (non-AI, non-commission)
status: stable
source: raw/context-v2.md §8, §9.1, §9.2, §9.3, §9.4, §9.5, §9.5a, §9.6, §9.7, §9.7a, §9.8, §9.9, §9.10, §9.11, §9.11a, §9.12
last_updated: 2026-05-26
tags: [fr]
---

# Requirements — Business + Functional

> 24 Business Requirements (BR-01..BR-24) and 15 FR clusters covering everything except AI Copilot ([wiki/ai.md](ai.md)) and Commission Engine ([wiki/commission-engine.md](commission-engine.md)). Each FR cites its canonical RESO resource(s) and cross-links to the wiki entity / process page where applicable.

## TOC

- [#br](#br)
- [#fr-con-contacts](#fr-con-contacts)
- [#fr-pc-split](#fr-pc-split)
- [#fr-org-organizations](#fr-org-organizations)
- [#fr-cfl-contact-funnel-lifecycle](#fr-cfl-contact-funnel-lifecycle)
- [#fr-fnl-funnel-canonical](#fr-fnl-funnel-canonical)
- [#fr-pros-prospecting](#fr-pros-prospecting)
- [#fr-act-activities](#fr-act-activities)
- [#fr-show-showings](#fr-show-showings)
- [#fr-cara-caravan](#fr-cara-caravan)
- [#fr-cl-contact-listings](#fr-cl-contact-listings)
- [#fr-tm-transactions](#fr-tm-transactions)
- [#fr-cmm-communications](#fr-cmm-communications)
- [#fr-doc-documents](#fr-doc-documents)
- [#fr-ref-referral](#fr-ref-referral)
- [#fr-rep-reporting](#fr-rep-reporting)

## Business requirements (BR) {#br}

| ID | Requirement | Priority |
|---|---|---|
| BR-01 | Unified base of `Contacts`, `Member`, `Office`, `Teams`, `SavedSearch`, `Prospecting`, `ContactListings`, `TransactionManagement`, and related canonical RESO DD 2.0 resources | High |
| BR-02 | Full client lifecycle via `Contacts.ContactType` funnel (Lead → Prospect → Ready to Buy → Buyer / Seller / Past Client / …) and multiple parallel `SavedSearch` rows | High |
| BR-03 | Transparent pipeline by broker / office / region / stage ([wiki/overview.md#pipeline](overview.md#pipeline)), derived from canonical state | High |
| BR-04 | Commission income forecast = base × commission rate × probability per stage; commission ledger lives in external Finance ERP ([wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission)) | High |
| BR-05 | Help brokers not lose follow-up: auto-highlight overdue `Activity` and unanswered `ContactListings.ListingSentTimestamp` | High |
| BR-06 | Record `Contacts.LeadSource` (canonical RESO lookup) and analyze acquisition-channel effectiveness | High |
| BR-07 | Support HNWI / UHNWI clients with high confidentiality (privacy level on `Contacts`) | High |
| BR-08 | Differentiated access to VIP / private `Contacts`, `SavedSearch`, `ContactListings`, `Showing`, and related resources | High |
| BR-09 | Segmentation by budget / goal / location / type / timeline via `SavedSearch.SearchQuery` (OData filter) | High |
| BR-10 | Communication history via `Activity` and `ContactListingNotes` | High |
| BR-11 | Manage broker activities: calls, meetings, showings, tasks, follow-ups as `Activity` rows linked to canonical resources | High |
| BR-12 | Organize showings via the canonical 5-resource Showing chain integrated with the Listing Module | High |
| BR-13 | Record client interest via `ContactListings` + `ContactListingPreference` without editing property master data | High |
| BR-14 | Offers and offer history via `TransactionManagement` + `HistoryTransactional` | High |
| BR-15 | Multi-country structure: different markets, currencies, `Office`, `Teams`, `OUID` | Medium |
| BR-16 | Personal-data protection and communication-consent (`Contacts` consent fields) | High |
| BR-17 | Foundation for AI matching, funnel scoring, automated nurturing on canonical resources | Medium |
| BR-18 | One `Contacts` can have multiple parallel active `SavedSearch` + `Prospecting` + `ContactListings` + `TransactionManagement` rows — these are parallel intents; metrics aggregated by `(Contacts × SavedSearch)`, not by Contact | High |
| BR-19 | Commercial parameters of the intent live on `SavedSearch.SearchQuery` + `SearchQueryHumanReadable`, not on `Contacts` | High |
| BR-20 | Closed Won requires all three conditions simultaneously: `Property.StandardStatus = Closed` + an existing `TransactionManagement` row + a full-payment webhook from Finance ERP with `HistoryTransactional` (`ChangeType = Closed`) | High |
| BR-21 | Every CRM-side state transition MUST emit a `HistoryTransactional` row per the canonical contract ([wiki/integration.md#history-emission](integration.md#history-emission)) | High |
| BR-22 | CRM uses canonical `Member` / `Office` / `OUID` / `Teams` / `TeamMembers` as the sole roster and org-model; no parallel org-model | High |
| BR-23 | Contact ↔ Listing engagement persisted exclusively as canonical `ContactListings` + `ContactListingNotes` | High |
| BR-24 | Contracts, commissions, payments are business goals realized via canonical `Property.StandardStatus` + `HistoryTransactional` + external systems; **not** first-class CRM data entities | High |

Source: raw/context-v2.md §8.

## FR-CON — Contacts {#fr-con-contacts}

RESO: `Contacts`. Entity: [wiki/entities.md#contacts](entities.md#contacts).

| ID | Requirement | Priority |
|---|---|---|
| FR-CON-01 | Create a `Contacts` record manually | High |
| FR-CON-02 | Import `Contacts` from CSV/Excel | High |
| FR-CON-03 | Store name, surname, phone, email, country, city, language, `Contacts.LeadSource` | High |
| FR-CON-04 | `Contacts.ContactType` as a multi-value RESO lookup | High |
| FR-CON-05 | Assign responsible broker via `Contacts.OwnerMemberKey → Member` | High |
| FR-CON-06 | Communication and activity history (`Activity`, `ContactListingNotes`, `HistoryTransactional`) per contact | High |
| FR-CON-07 | Tags on contacts | Medium |
| FR-CON-08 | Detect duplicates by email / phone / name | High |
| FR-CON-09 | VIP/private flag + privacy level (Standard / Private / Ultra-confidential) | High |
| FR-CON-10 | Marketing-communication consents (`Contacts` consent fields) | High |
| FR-CON-11 | `Contacts.PreferredCommunicationMethod`: WhatsApp / phone / email / assistant / in-person | High |
| FR-CON-12 | Links between `Contacts`: spouse / assistant / advisor / lawyer / family office / company representative | Medium |
| FR-CON-13 | Lifestyle interests: golf, yachting, schools, wellness, privacy, marina, airport access, gated community, etc. | Medium |
| FR-CON-14 | Family profile: family-with-children / single / corporate buyer / etc. | Medium |
| FR-CON-15 | General decision-maker role (client / spouse / advisor / family office / assistant). Role on a specific transaction lives on `TransactionManagement`. | Medium |
| FR-CON-16 | On the `Contacts` card, show all related `SavedSearch`, `Prospecting`, `ContactListings`, `ShowingAppointment`, `Showing`, `TransactionManagement` with canonical statuses | High |
| FR-CON-17 | **Forbid** storing commercial intent parameters on `Contacts` — those belong on `SavedSearch.SearchQuery` ([#fr-pc-split](#fr-pc-split)) | High |
| FR-CON-18 | `Contacts.ContactType` lookup values: Lead / Prospect / Ready to Buy / Buyer / Seller / Landlord / Tenant / Investor / Past Client / Partner / Referral / Personal Acquaintance / Vendor / Other | High |
| FR-CON-19 | `Contacts.ContactStatus`: Active / On Vacation / Inactive / Deleted | High |
| FR-CON-20 | `Contacts.LeadSource` canonical RESO lookup (Website / Referral / Campaign / Event / Partner / Cold Outreach / Past Client / Walk-in / Other) | High |
| FR-CON-21 | Persist `OwnerMemberKey → Member`; SLA, route-to-broker and assignment rules use this link | High |
| FR-CON-22 | Start an SLA timer for first contact when `Contacts.ContactType` contains `Lead` AND no active `SavedSearch+Prospecting`; SLA stops as soon as the contact gets a first active `SavedSearch` or graduates beyond Lead | High |

Source: raw/context-v2.md §9.1.

## FR-PC — Personal vs Commercial split (canonical attribute placement) {#fr-pc-split}

Where each kind of data MUST live (no custom entities).

| Field category | Canonical resource | Canonical attribute |
|---|---|---|
| Privacy level (Standard / Private / Ultra-confidential) | `Contacts` | privacy-level extension lookup (locale) |
| Preferred communication channel | `Contacts` | `PreferredCommunicationMethod` |
| Relationships (spouse, advisor, lawyer, family office, assistant) | `Contacts` ↔ `Contacts` | canonical relationship |
| Lifestyle interests | `Contacts` | lifestyle multi-lookup |
| Family profile | `Contacts` | family-profile lookup |
| Decision-maker role (general) | `Contacts` | decision-maker-role lookup |
| Contact type (Lead / Prospect / …) | `Contacts` | `ContactType` (multi-value) |
| Contact status | `Contacts` | `ContactStatus` |
| Lead source | `Contacts` | `LeadSource` |
| Engagement preference (Favorite / Possibility / Discard) | `ContactListings` | `ContactListingPreference` |
| Showing status (Pending / Confirmed / Denied / Cancelled) | `ShowingAppointment` | `ShowingAppointmentStatus` |
| Caravan status (Active / Canceled / Ended) | `Caravan` | `CaravanStatus` |
| Listing status (Active / AUC / Pending / Closed / …) | `Property` | `StandardStatus` |
| **Budget and currency** | **`SavedSearch`** | **`SearchQuery` (OData) + `SearchQueryHumanReadable`** |
| **Purpose of purchase** (residence / investment / relocation / golden visa / lifestyle / rental income / capital preservation) | **`SavedSearch`** | `SearchQuery` parameters |
| **Target locations** | **`SavedSearch`** | `SearchQuery` parameters |
| **Property type** | **`SavedSearch`** | `SearchQuery` parameters (on `Property` resource) |
| **Bedrooms / area / view / amenities requirements** | **`SavedSearch`** | `SearchQuery` parameters |
| **Timeline / urgency** | **`SavedSearch`** | `SearchQuery` parameters + timestamp fields |
| **Decision maker / influencing parties on a specific transaction** | `TransactionManagement` | linked `Contacts` rows |
| **Investment criteria (yield, appreciation, exit horizon, risk profile)** | **`SavedSearch`** | `SearchQuery` parameters |
| **Decision criteria of the intent** | **`SavedSearch`** | `SearchQueryHumanReadable` |

Logic: one and the same `Contacts` can simultaneously look for a residence in Limassol and an investment in Budapest — these are **two distinct `SavedSearch`** rows for the same `Contacts`, with different `SearchQuery` values but shared personal preferences (`PreferredCommunicationMethod`, lifestyle, family profile).

Source: raw/context-v2.md §9.2.

## FR-ORG — Organizations: Member / Office / OUID / external counterparties {#fr-org-organizations}

RESO: `Member`, `Office`, `OUID`, `Teams`, `TeamMembers`. Entity: [wiki/entities.md#member-office-team](entities.md#member-office-team).

| ID | Requirement | Priority |
|---|---|---|
| FR-ORG-01 | Internal org-model via canonical `Member` / `Office` / `OUID` / `Teams` + `TeamMembers` | High |
| FR-ORG-02 | External counterparties (family office, developer, law firm, bank, corporate buyer, partner agency, relocation, property management) via `Contacts` with `Contacts.Company` + `Contacts.JobTitle` | High |
| FR-ORG-03 | Relationships between `Contacts` (e.g. family-office representative ↔ owner, lawyer ↔ corporate buyer) via canonical `Contacts ↔ Contacts` | High |
| FR-ORG-04 | Org ↔ transaction link via a `TransactionManagement` row + linked `Contacts` (organization representative) | Medium |
| FR-ORG-05 | External-org attributes (country, city, website, industry, comments) stored on the representative's `Contacts` (`Country`, `City`, `Website`, `Notes`) or in `ContactListingNotes` | Medium |

Source: raw/context-v2.md §9.3.

## FR-CFL — Contact funnel lifecycle (ContactType graduation) {#fr-cfl-contact-funnel-lifecycle}

RESO: `Contacts.ContactType`. Process: [wiki/processes.md#contact-funnel](processes.md#contact-funnel).

| ID | Requirement | Priority |
|---|---|---|
| FR-CFL-01 | Create `Contacts` from an inbound website inquiry with `ContactType` containing `Lead` | High |
| FR-CFL-02 | Create `Contacts` manually with any valid `ContactType` | High |
| FR-CFL-03 | Record `Contacts.LeadSource` from canonical RESO lookup | High |
| FR-CFL-04 | Assign `Contacts.OwnerMemberKey → Member` manually or via routing rules | High |
| FR-CFL-05 | Start SLA timer for first contact (Lead AND no active `SavedSearch+Prospecting`); SLA stops when contact gets a first active `SavedSearch` or graduates beyond Lead | High |
| FR-CFL-06 | Stale Leads report — filter by `ContactType` + SLA timer | High |
| FR-CFL-07 | ContactType transitions: Lead → Prospect (broker first contact), Prospect → Ready to Buy (≥1 active `SavedSearch`), Ready to Buy → Buyer / Seller / Landlord / Tenant (by transaction type when `TransactionManagement` or `Property` ownership appears), Closed → Past Client | High |
| FR-CFL-08 | On qualification create one or more `SavedSearch` (per parallel intent) with `SearchQuery` and bind to `Contacts` | High |
| FR-CFL-09 | Raw inquiry (free text) stored in `ContactListingNotes` (general note) or `SavedSearch.SearchQueryHumanReadable` | High |
| FR-CFL-10 | UTM tags / campaign data on `Contacts` (or linked campaign) and tied to `LeadSource` | Medium |
| FR-CFL-11 | Disqualification reason — emit `HistoryTransactional` (`ChangeType = Unqualified`); `Contacts.ContactType` drops `Lead`; `Contacts.ContactStatus → Inactive` | High |
| FR-CFL-12 | On inbound inquiry, dedupe by email/phone/name; reuse existing `Contacts` (add a new Lead `ContactType` entry + new `SavedSearch`); do not create a duplicate Contact | High |
| FR-CFL-13 | The funnel stage (Qualification → Matching → Viewing → Contracting → Payment → Closed Won/Lost/Nurturing) is a **UI/UX projection** of canonical state, not a stored entity. Stage derivation per [wiki/overview.md#pipeline](overview.md#pipeline). | High |
| FR-CFL-14 | Every `Contacts.ContactType` transition MUST emit a `HistoryTransactional` row (`ResourceName=Contacts`, `MajorChangeType=ContactType change`, `ChangeType=<new ContactType>`) | High |

Source: raw/context-v2.md §9.4.

## FR-FNL — Funnel canonical projection (5-stage UI/UX) {#fr-fnl-funnel-canonical}

Pipeline projection: [wiki/overview.md#pipeline](overview.md#pipeline). Stage derivation rules also live there.

| ID | Requirement | Priority |
|---|---|---|
| FR-FNL-01 | Multiple parallel commercial intents per Contact represented as multiple `SavedSearch` rows; one `(Contacts, SavedSearch)` pair = one funnel "option" | High |
| FR-FNL-02 | Transaction type stored on `TransactionManagement.TransactionType` (PurchaseOffer / LeaseOffer / ListingForSale / ListingForLease / Other); before offer appears, derived from `SavedSearch.SearchQuery` (resource Property + class) + `Contacts.ContactType` (Buyer vs Tenant vs Landlord vs Seller) | High |
| FR-FNL-03 | Budget + currency live in `SavedSearch.SearchQuery` (OData filter, e.g. `ListPrice ge 1000000 and ListPrice le 3000000 and Currency eq 'EUR'`) + duplicated to `SearchQueryHumanReadable` for UI | High |
| FR-FNL-04 | Purpose of purchase (residence / investment / relocation / holiday home / citizenship-residency / rental income / capital preservation / lifestyle) stored as a `SavedSearch.SearchQuery` parameter + `SearchQueryHumanReadable` | High |
| FR-FNL-05 | Target locations in `SavedSearch.SearchQuery` (StateOrProvince / City / SubdivisionName / PostalCode) | High |
| FR-FNL-06 | Preferred property type in `SavedSearch.SearchQuery` (PropertyType / PropertySubType) | High |
| FR-FNL-07 | Bedrooms / area / view / amenities in `SavedSearch.SearchQuery` (BedroomsTotal / LivingArea / View / Amenities) | Medium |
| FR-FNL-08 | Decision timeframe (urgent / 0–3 / 3–6 / 6+ / monitoring) in `SavedSearch` (custom timeframe attribute) or derived from `Prospecting.ScheduleType` + `NextSendTimestamp` | High |
| FR-FNL-09 | Decision maker + influencing parties on a specific transaction stored as related `Contacts` rows on `TransactionManagement` | High |
| FR-FNL-10 | Investment criteria (yield / appreciation / exit horizon / risk profile) in `SavedSearch.SearchQuery` + `SearchQueryHumanReadable` | Medium |
| FR-FNL-11 | Decision criteria in `SavedSearch.SearchQueryHumanReadable` (free text) | High |
| FR-FNL-12 | **Forecast commission** with priority rule: **(a)** if a `TransactionManagement` row exists for `(Contacts × SavedSearch)` with `OfferAmount` filled — base = `TransactionManagement.OfferAmount`; **(b)** otherwise — base = `SavedSearch` budget mid-point. In both cases: forecast commission = base × configured commission rate × stage probability. Commission ledger does NOT live in CRM (see [wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission), BR-04, BR-24). The switch (b) → (a) emits a `HistoryTransactional` row (`MajorChangeType = Forecast base change`, `ChangeType = SavedSearch budget → OfferAmount`) | High |
| FR-FNL-13 | Actual commission comes from external Finance ERP via webhook ([wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission)); CRM mirrors via `HistoryTransactional` on the related `Property` / `TransactionManagement` | Medium |
| FR-FNL-14 | Support 5-stage funnel as UI/UX projection of canonical state ([wiki/overview.md#pipeline](overview.md#pipeline)): Qualification / Matching / Viewing / Contracting / Payment + terminals Closed Won / Closed Lost / Nurturing | High |
| FR-FNL-15 | Sub-statuses derived from canonical signals; every transition recorded as `HistoryTransactional` | High |
| FR-FNL-16 | Closing probability derived from stage (preset per stage) or overridable by broker via attribute on `SavedSearch` / `TransactionManagement` | Medium |
| FR-FNL-17 | Expected closing date derived from `SavedSearch` timeframe + funnel state, or set manually on `TransactionManagement.ExpectedClosingDate` | High |
| FR-FNL-18 | Every active `(Contacts, SavedSearch)` funnel MUST have an open `Activity` (task) with `DueDate` | High |
| FR-FNL-19 | Stale Funnels report = `(Contacts, SavedSearch)` with no new `Activity` / `ContactListings` / `HistoryTransactional` rows for N days | High |
| FR-FNL-20 | Move to Nurturing = `Prospecting.ActiveYN=false` AND `Contacts.ContactStatus=Active`; return = reactivate `Prospecting` or create a new `SavedSearch` | Medium |
| FR-FNL-21 | Closed Lost recorded via `HistoryTransactional` row (`ChangeType=Closed Lost`) + reason text in `ContactListingNotes` or on `HistoryTransactional` | High |
| FR-FNL-22 | Funnel linked to one or more properties via `ContactListings` rows (per-listing engagement) and optionally `TransactionManagement` rows; primary target derived as the `Property` with highest engagement (Favorite + Showing + offer) or set explicitly on `TransactionManagement` | High |
| FR-FNL-23 | Contract via external system ([wiki/integration.md#contract-system](integration.md#contract-system)); link through `Property.StandardStatus` (AUC / Pending / Closed) + `Document` references | High |
| FR-FNL-24 | Commission / payment events — external systems; linked via `HistoryTransactional` + `Property.StandardStatus` transitions | High |
| FR-FNL-25 | Closed Won requires three canonical conditions simultaneously: `Property.StandardStatus = Closed`, existing `TransactionManagement` row, full-payment webhook received (see [wiki/overview.md#pipeline](overview.md#pipeline) and BR-20) | High |
| FR-FNL-26 | On the `Contacts` card, show a summary across all `SavedSearch`, active funnels, `ContactListings`, `ShowingAppointment`, `TransactionManagement`; commercial data is not duplicated on `Contacts` | Medium |

Source: raw/context-v2.md §9.5.

## FR-SS / FR-PROS — SavedSearch + Prospecting {#fr-pros-prospecting}

RESO: `SavedSearch`, `Prospecting`. Entity: [wiki/entities.md#saved-search](entities.md#saved-search), [wiki/entities.md#prospecting](entities.md#prospecting). Process: [wiki/processes.md#property-matching](processes.md#property-matching).

### SavedSearch (FR-SS)

| ID | Requirement | Priority |
|---|---|---|
| FR-SS-01 | Create `SavedSearch` with mandatory: `SavedSearchName`, `SavedSearchType` (Buyer / Seller / Investor / Tenant / Landlord / Past Client / Other), `MemberKey → Member`, `ResourceName`, `ClassName`, `SearchQuery` (OData filter), `SearchQueryHumanReadable` | High |
| FR-SS-02 | Bind `SavedSearch` to `Contacts` (one Contact ↔ N SavedSearch); deleting Contact MUST NOT cascade-delete SavedSearch without explicit user action | High |
| FR-SS-03 | Validate `SearchQuery` as a correct RESO OData filter; provide a UI builder for non-coding brokers | High |
| FR-SS-04 | Show list of `SavedSearch` on the `Contacts` card with status of each (active / paused / closed) — status derived from linked `Prospecting.ActiveYN` | High |
| FR-SS-05 | Allow copying a `SavedSearch` to create a new intent (e.g. broaden locations / raise budget) | Medium |

### Prospecting (FR-PROS)

| ID | Requirement | Priority |
|---|---|---|
| FR-PROS-01 | Create `Prospecting` row bound to `SavedSearchKey`, `ContactKey`, `OwnerMemberKey → Member` | High |
| FR-PROS-02 | Fields: `ActiveYN`, `ClientActivatedYN`, `ConciergeYN`, `ScheduleType` (Daily / Weekly / Monthly / OnNewMatch / Custom), `DailySchedule`, `NextSendTimestamp`, templates (`Greeting`, `Salutation`, `Signature`, `Body`), language, email lists (`EmailTo`, `EmailCc`, `EmailBcc`) | High |
| FR-PROS-03 | On every Prospecting run, execute the linked `SavedSearch.SearchQuery`, build the shortlist of new/updated properties, emit `ContactListings` rows with `ListingSentTimestamp` + channel | High |
| FR-PROS-04 | Support `ConciergeYN=true` (broker reviews before sending) and `ConciergeYN=false` (auto-send) | High |
| FR-PROS-05 | `ClientActivatedYN` flag for deliveries the client activated via portal | Medium |
| FR-PROS-06 | Emit `HistoryTransactional` on Prospecting create / activate / deactivate / send | High |
| FR-PROS-07 | Stale Prospecting report = `ActiveYN=true` without sends for N days | Medium |
| FR-PROS-08 | Stop `Prospecting` (`ActiveYN=false`) with a reason (closed / nurturing / unresponsive); this is the funnel transition to Nurturing or Closed Lost | High |
| FR-PROS-09 | On `Prospecting.NextSendTimestamp` trigger, create an `Activity` row (touchpoint reminder type `follow-up` / `task`) for `OwnerMemberKey → Member` **even if no new matched listings this cycle** — to maintain contact-rhythm with the purchaser. Activity links to `Prospecting.ProspectingKey` (see FR-ACT-11). | High |
| FR-PROS-10 | `Prospecting.ScheduleType` governs both the auto-delivery cadence to the client AND the touchpoint reminder cadence for the broker. If different cadences are needed, the broker can add a second `Prospecting` row on the same `(Contact, SavedSearch)` with a different `ScheduleType`. | Medium |
| FR-PROS-11 | When `ConciergeYN = true`, the touchpoint Activity for the broker carries a link to the assembled shortlist (if any) with actions: review and send / edit / skip / pause Prospecting. When `ConciergeYN = false`, the Activity is a post-fact notification of the delivered shortlist + reminder for a personal touchpoint. | High |
| FR-PROS-12 | Stale Prospecting report MUST also include `Prospecting` rows where the `OwnerMemberKey` has not completed a touchpoint Activity for N days (broker-side stale) | Medium |
| FR-PROS-13 | When `ContactListings.ListingSentTimestamp` appears for `(Contacts, SavedSearch)` WITHOUT an active `Prospecting` row (manual broker send — see [wiki/overview.md#pipeline](overview.md#pipeline) Matching (b)), the system MUST create an `Activity` row for `OwnerMemberKey → Member` (type `task` / `follow-up` with marker "soft prompt: activate Prospecting") — to maintain contact-rhythm. **Non-blocking**; the broker can dismiss with a reason (recorded in `Activity.Result` for analytics). The Activity links to `SavedSearch.SavedSearchKey` (since no `Prospecting` exists). | High |

Source: raw/context-v2.md §9.5a.

## FR-ACT — Activities {#fr-act-activities}

Entity: [wiki/entities.md#activity](entities.md#activity). App-private (CRM app DB, never CDL).

| ID | Requirement | Priority |
|---|---|---|
| FR-ACT-01 | Create activities: call, email, WhatsApp, meeting, viewing, task, note, follow-up | High |
| FR-ACT-02 | `Activity` linked to `Contacts`, `SavedSearch`, `Prospecting`, `ContactListings`, `ShowingAppointment`, `Showing`, `TransactionManagement`, `Caravan` and/or `Property`. For commercial context, at minimum to a `(Contacts, SavedSearch)` pair or to a `TransactionManagement` row. | High |
| FR-ACT-03 | Task reminders | High |
| FR-ACT-04 | Today-list of broker tasks | High |
| FR-ACT-05 | Overdue tasks list | High |
| FR-ACT-06 | Store activity result | High |
| FR-ACT-07 | Create follow-up after call / meeting / showing | High |
| FR-ACT-08 | Manager visibility of broker activity | High |
| FR-ACT-09 | Private vs team notes | Medium |
| FR-ACT-10 | `Activity` MAY carry cost-attribution / broker-contribution metadata (work category, broker contributor, duration, deal context) — for the Commission Engine subsystem ([wiki/commission-engine.md](commission-engine.md)). Field set, lookups, validations designed in Lovable. | Medium |
| FR-ACT-11 | `Activity` MAY be auto-generated from `Prospecting` firing (touchpoint reminder for the broker — see FR-PROS-09..12) with an explicit FK to `Prospecting.ProspectingKey` for audit, filtering, and the broker-side stale report (FR-PROS-12). Activity type: `follow-up` or `task` with touchpoint-reminder marker. | High |

Source: raw/context-v2.md §9.6.

## FR-SHA / FR-SHR / FR-SHAP / FR-SH / FR-LBX — Showing chain {#fr-show-showings}

RESO: `ShowingAvailability`, `ShowingRequest`, `ShowingAppointment`, `Showing`, `LockOrBox`. Entity: [wiki/entities.md#showing-chain](entities.md#showing-chain). Process: [wiki/processes.md#showing-process](processes.md#showing-process).

### ShowingAvailability (FR-SHA)

| ID | Requirement | Priority |
|---|---|---|
| FR-SHA-01 | Manage `ShowingAvailability` per `Property` (windows, blackout, requirements) | High |
| FR-SHA-02 | Sync posture with Listing Module (master typically on listing side) | High |
| FR-SHA-03 | Respect `Property.ShowingStatus` (Accepting Requests / On Hold / No Showings / Restricted Showings) when creating ShowingRequest | High |

### ShowingRequest (FR-SHR)

| ID | Requirement | Priority |
|---|---|---|
| FR-SHR-01 | Create `ShowingRequest` from `Member` (showing agent) or `Contacts` (via portal) | High |
| FR-SHR-02 | Must carry `ListingKey → Property`, requested timeslot, `RequesterMemberKey → Member` and/or related `Contacts` | High |
| FR-SHR-03 | Validate against `ShowingAvailability` and `Property.ShowingStatus`; denial expressed via `ShowingAppointment.ShowingAppointmentStatus = Denied` | High |
| FR-SHR-04 | Every ShowingRequest emits `HistoryTransactional` (`ResourceName=ShowingRequest`, `ChangeType=Submitted`) | High |

### ShowingAppointment (FR-SHAP)

| ID | Requirement | Priority |
|---|---|---|
| FR-SHAP-01 | Create `ShowingAppointment` with status: Pending / Confirmed / Denied / Cancelled | High |
| FR-SHAP-02 | Carry `ListingKey → Property`, `ShowingAgentKey → Member`, scheduled timeslot, optionally `ShowingRequestKey`, `Contacts`, `Caravan` | High |
| FR-SHAP-03 | Every status transition emits `HistoryTransactional` | High |
| FR-SHAP-04 | Confirmation / decline notifications to all parties (listing agent / showing agent / buyer) | High |

### Showing (FR-SH)

| ID | Requirement | Priority |
|---|---|---|
| FR-SH-01 | Create `Showing` row after the actual showing: `ListingKey`, `ShowingAgentKey → Member`, `ShowingStartTimestamp`, `ShowingEndTimestamp` | High |
| FR-SH-02 | Record client feedback in `ContactListingNotes` for the `(Contacts, Property)` pair | High |
| FR-SH-03 | Update `ContactListings.ContactListingPreference` (Favorite / Possibility / Discard) based on feedback | High |
| FR-SH-04 | Prompt for a follow-up `Activity` after showing | High |
| FR-SH-05 | History of `Showing` rows per `Contacts` (aggregated through ContactListings) | Medium |
| FR-SH-06 | History of `Showing` rows per `Property` | Medium |
| FR-SH-07 | Every created `Showing` row emits `HistoryTransactional` | High |

### LockOrBox (FR-LBX)

| ID | Requirement | Priority |
|---|---|---|
| FR-LBX-01 | Record lockbox / smart-key usage via `LockOrBox` row | Medium |
| FR-LBX-02 | `LockOrBox` carries credential identifier, time of use, `ShowingKey → Showing`, `ListingKey → Property` | Medium |
| FR-LBX-03 | LockOrBox audit access restricted to listing agent / managing partner / compliance roles | Medium |

Source: raw/context-v2.md §9.7.

## FR-CAR — Caravan + CaravanStop {#fr-cara-caravan}

RESO: `Caravan`, `CaravanStop`. Entity: [wiki/entities.md#caravan](entities.md#caravan).

| ID | Requirement | Priority |
|---|---|---|
| FR-CAR-01 | Create `Caravan` with: `CaravanName`, `CaravanDate`, `CaravanStartTime`, `CaravanEndTime`, `CaravanStatus`, `CaravanType`, `CaravanOrganizerKey → Member`, `CaravanAllowedStatuses` | High |
| FR-CAR-02 | `CaravanStatus`: Active / Canceled / Ended | High |
| FR-CAR-03 | `CaravanType`: Broker / AOR / Other (for luxury — Curated Buyer Tour / Office Sneak Peek / Private VIP Tour) | High |
| FR-CAR-04 | Add ordered `CaravanStop` rows: `StopOrder`, `Property`, `ScheduledArrival`, `ScheduledDeparture`, logistics notes | High |
| FR-CAR-05 | Validate each stop's `Property.StandardStatus` against `Caravan.CaravanAllowedStatuses` | High |
| FR-CAR-06 | Link `Contacts` (VIP client / family-office rep) as tour participant | High |
| FR-CAR-07 | Each showing in a Caravan recorded as `Showing` row with `ShowingAgentKey → Member` (organizer); optional `Showing.CaravanKey → Caravan` | High |
| FR-CAR-08 | Every `CaravanStatus` transition emits `HistoryTransactional` | High |
| FR-CAR-09 | Allow sending Caravan brief / tour digest to the client (with `ContactListings.ContactListingPreference` marks per object) | Medium |
| FR-CAR-10 | For luxury: include extras (lunch, transfer, lifestyle activities) as `CaravanStop` notes or linked `Activity` | Low |

Source: raw/context-v2.md §9.7a.

## FR-CL — ContactListings (Contact × Property engagement) {#fr-cl-contact-listings}

RESO: `ContactListings`, `ContactListingNotes`. Entity: [wiki/entities.md#contact-listings](entities.md#contact-listings). **CDL access gate applies** (RLS disabled — EF-only access).

| ID | Requirement | Priority |
|---|---|---|
| FR-CL-01 | Store `Contacts` ↔ `Property` link as a `ContactListings` row | High |
| FR-CL-02 | `ContactListings.ContactListingPreference`: Favorite / Possibility / Discard (canonical enum). No custom rich statuses; offer lifecycle is expressed via `TransactionManagement` + `HistoryTransactional`, not via ContactListings status. | High |
| FR-CL-03 | `ContactListings.ListingSentTimestamp` (date when the property was sent to the client) | High |
| FR-CL-04 | Channel of sending in `ContactListings` (Channel: email / WhatsApp / Manual / Portal / SMS) | Medium |
| FR-CL-05 | `ContactListings.ListingViewedYN` and `PortalLastVisitedTimestamp` to track whether the client opened the property | Medium |
| FR-CL-06 | Notes per `(Contacts, Property)` via `ContactListingNotes` rows (multiple; author Agent / Contact; timestamps) | High |
| FR-CL-07 | Mark a property as Discard with reason (text in `ContactListingNotes` or short reason attribute on ContactListings) | High |
| FR-CL-08 | Mark a property as Favorite (top short-list) or Possibility (considered but not confirmed) | High |
| FR-CL-09 | One `Property` can simultaneously be in `ContactListings` rows for multiple `Contacts`; preference and engagement are tracked independently per pair | High |
| FR-CL-10 | Emit `HistoryTransactional` on every `ContactListingPreference` change and every `ListingSentTimestamp` / `ListingViewedYN` transition | High |

Source: raw/context-v2.md §9.8.

## FR-TM — TransactionManagement (offers and transactions) {#fr-tm-transactions}

RESO: `TransactionManagement`. Entity: [wiki/entities.md#transaction-management](entities.md#transaction-management). Process: [wiki/processes.md#offer-to-closing](processes.md#offer-to-closing).

| ID | Requirement | Priority |
|---|---|---|
| FR-TM-01 | Create `TransactionManagement` bound to `Contacts` (buyer / seller / tenant / landlord), `Property` (via `ListingKey`), `MemberKey → Member`, with `TransactionType` (PurchaseOffer / LeaseOffer / ListingForSale / ListingForLease / Other) | High |
| FR-TM-02 | Carry `OfferAmount`, `Currency`, `OfferDate`, `ExpectedClosingDate`, terms (deposit, payment terms, contingencies, validity), `Document` references on the offer packet | High |
| FR-TM-03 | Show current `Property.ListPrice` (asking price) from the Listing Module when creating an offer | High |
| FR-TM-04 | Aggregated history of TransactionManagement rows by `Contacts`, by `Property`, by `Member` | High |
| FR-TM-05 | Warn if `Property.StandardStatus ∈ {Active Under Contract, Pending, Closed, Withdrawn, Canceled, Expired}` — new PurchaseOffer / LeaseOffer requires explicit broker confirmation | High |
| FR-TM-06 | Offer lifecycle expressed via `HistoryTransactional` rows with `ChangeType`: Draft / Submitted / Countered / Accepted / Rejected / Withdrawn / Expired. Current status = the row with the latest `EntityEventSequence`. | High |
| FR-TM-07 | Offer Accepted (`HistoryTransactional.ChangeType = Accepted`) MUST auto-push `Property.StandardStatus = Active Under Contract` to the Listing Module | High |
| FR-TM-08 | Contract-signed webhook from external contract system ([wiki/integration.md#contract-system](integration.md#contract-system)) MUST set `Property.StandardStatus = Pending` and emit `HistoryTransactional` | High |
| FR-TM-09 | TransactionManagement creation auto-advances the funnel projection (Contracting / Offer Submitted etc., per [wiki/overview.md#pipeline](overview.md#pipeline)) | Medium |
| FR-TM-10 | Link TransactionManagement ↔ `Document` (offer packet, signed contract, addenda, counter-offers) | High |
| FR-TM-11 | Mark TransactionManagement as ListingForSale / ListingForLease (sell-side rep) and link to listing agreement in the external system | High |
| FR-TM-12 | Every TM create / update emits `HistoryTransactional` | High |
| FR-TM-13 | TM card MUST show a **forecast P&L block** from the Commission Engine subsystem ([wiki/commission-engine.md](commission-engine.md)) — forecast GCI, attributed costs, net margin, per-broker compensation — and, after deal close, the **variance** (actual − forecast) from reconciliation with external Finance ERP (see [wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission), [wiki/integration.md#finance-erp-payments](integration.md#finance-erp-payments)). Specific layout, fields, recompute events, UX details designed in Lovable. Forecast GCI on the TM card uses `OfferAmount` as base (FR-FNL-12 (a)); on `OfferAmount` change (counter-offer, amended offer) the subsystem recomputes forecast and emits `HistoryTransactional`. | High |

Source: raw/context-v2.md §9.9.

## FR-COM — Communications {#fr-cmm-communications}

| ID | Requirement | Priority |
|---|---|---|
| FR-COM-01 | Store email history if email integration is configured | High |
| FR-COM-02 | Log calls | High |
| FR-COM-03 | Log WhatsApp communications manually or via integration | High |
| FR-COM-04 | Link a communication to `Contacts`, `SavedSearch`, `ContactListings`, `Property`, `TransactionManagement`, `ShowingAppointment` and/or other canonical resource. For commercial context: link to a specific `(Contacts, SavedSearch)` or `TransactionManagement` row. | High |
| FR-COM-05 | Message templates | Medium |
| FR-COM-06 | Record the fact of sending a property shortlist to the client via `ContactListings.ListingSentTimestamp` (+ channel) and `Prospecting` send history | High |
| FR-COM-07 | Visibility levels for notes: public / private / sensitive | High |

Source: raw/context-v2.md §9.10.

## FR-DOC — Documents {#fr-doc-documents}

Entity: [wiki/entities.md#document](entities.md#document). Metadata only in CRM; files in external storage.

| ID | Requirement | Priority |
|---|---|---|
| FR-DOC-01 | Attach documents to contact / organization / deal / offer | Medium |
| FR-DOC-02 | Document categories: KYC, agreement, offer, brochure, NDA, legal, financial, internal note | Medium |
| FR-DOC-03 | Store an external-storage link if files live outside CRM | Medium |
| FR-DOC-04 | Restrict access to confidential documents (NDA level / role) | High |
| FR-DOC-05 | Record upload date, author, version | Medium |

Source: raw/context-v2.md §9.11.

## FR-REF — Referral (project-flavour entity) {#fr-ref-referral}

Entity: [wiki/entities.md#referral](entities.md#referral). Process: [wiki/processes.md#referral-lifecycle](processes.md#referral-lifecycle). Escape hatch: [wiki/architecture.md#escape-hatch](architecture.md#escape-hatch).

| ID | Requirement | Priority |
|---|---|---|
| FR-REF-01 | Create `Referral` row linking referrer `Contacts` ↔ referee `Contacts`, with date and `ReferralType` (Client / Partner / Broker / Internal) | High |
| FR-REF-02 | On Referral create, auto-set `Contacts.LeadSource = Referral` on the referee if not already set | High |
| FR-REF-03 | Bind `Referral` to `OwnerMemberKey → Member` (broker who received the referral) | High |
| FR-REF-04 | Show outgoing-referrals list on the referrer's `Contacts` card (who, when, current referee `ContactType` graduation) | Medium |
| FR-REF-05 | Show source of referral on the referee's `Contacts` card (from whom, through which broker) | Medium |
| FR-REF-06 | Referral report: who brings the most referrals, conversion of referred leads into deals | Medium |
| FR-REF-07 | Every Referral create MUST emit `HistoryTransactional` row (`ResourceName = Referral`, `ResourceRecordKey = <ReferralKey>`, `MajorChangeType = Referral created`, `ChangeType = <ReferralType>`) — see [wiki/integration.md#history-emission](integration.md#history-emission) | High |
| FR-REF-08 | On `HistoryTransactional` with `MajorChangeType = Stage transition` / `ChangeType = Closed Won` for a `TransactionManagement` whose buyer/tenant `Contacts` is the referee of a `Referral`: (a) auto-update `Referral.Outcome = Closed Won` and `Referral.CloseDate`; (b) emit `HistoryTransactional` on `Referral` (`MajorChangeType = Referral outcome`, `ChangeType = Closed Won`); (c) create `Activity` notifications for the referrer-`Contacts` `OwnerMemberKey` (possible thank-you / referral-fee follow-up) and for the referee-`Contacts` `OwnerMemberKey`. Symmetric handling for `Closed Lost` (without the thank-you notification, but with recording for FR-REF-06). | Medium |

Source: raw/context-v2.md §9.11a.

## FR-REP — Reports & dashboards {#fr-rep-reporting}

| ID | Requirement | Priority |
|---|---|---|
| FR-REP-01 | Sales Pipeline by stage ([wiki/overview.md#pipeline](overview.md#pipeline)), `Member`, `Office`, region — aggregated by `(Contacts × SavedSearch)` and `TransactionManagement` rows | High |
| FR-REP-02 | Commission Forecast from forecasted commission (`SavedSearch` budget × rate × probability); actual commission comes from external Finance ERP | High |
| FR-REP-03 | Broker Activity Dashboard (`Activity`, `ShowingAppointment`, `Showing`, `TransactionManagement` rows + linked `HistoryTransactional`) per `Member` | High |
| FR-REP-04 | Lead Sources Report (`Contacts.LeadSource` aggregation) | High |
| FR-REP-05 | Lost Funnels Report (`(Contacts, SavedSearch)` with `Prospecting.ActiveYN=false` + `HistoryTransactional.ChangeType=Closed Lost` + reason) | High |
| FR-REP-06 | Stale Funnels Report (`(Contacts, SavedSearch)` with no new `Activity` / `ContactListings` / `HistoryTransactional` rows for N days) | High |
| FR-REP-07 | SLA Report on Lead reaction (`Contacts.ContactType=Lead AND no active SavedSearch+Prospecting AND SLA exceeded`) | High |
| FR-REP-08 | Property Sales Performance based on `ContactListings` (sends/views), `Showing`, `TransactionManagement` per `Property` | Medium |
| FR-REP-09 | Client Segmentation Report | Medium |
| FR-REP-10 | Export reports to Excel / CSV | Medium |

Source: raw/context-v2.md §9.12.
