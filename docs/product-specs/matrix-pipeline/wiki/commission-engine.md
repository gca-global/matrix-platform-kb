---
title: Commission Engine — CRM-internal ERP-lite for sales-broker P&L
status: stable
source: raw/context-v2.md §9.15, §11.6
last_updated: 2026-05-26
tags: [commission-engine]
---

# Commission Engine — CRM-internal ERP-lite for sales-broker P&L

> The sales broker must, at every funnel stage, (a) understand the structure of their commission payouts, (b) forecast deal-level GCI, and (c) see deal-level P&L (revenue − attributed costs) to decide "pursue / drop / escalate". This is a **CRM-internal ERP-lite subsystem**. It is an **explicit project-flavour deviation** from canonical RESO DD 2.0 ([wiki/architecture.md#escape-hatch](architecture.md#escape-hatch)). State lives in **CRM app DB** (Lovable-managed), never in CDL or SSO. Reconciliation with the external Finance ERP (legal source of truth for actual money) is via the pattern in [#reconciliation](#reconciliation).

## TOC

- [#overview](#overview)
- [#scope](#scope)
- [#data-model-stub](#data-model-stub)
- [#capabilities](#capabilities)
- [#reconciliation](#reconciliation)
- [#deviation](#deviation)

## Overview {#overview}

**Business problem.** The sales broker pursues a deal across legal support, marketing, conferences, showings, negotiation. To compensate the broker correctly the agency must (i) capture per-deal operational costs, (ii) project GCI and net margin at every funnel stage, (iii) translate that into an explainable broker compensation under published commission rules.

**Architectural positioning.** This is a CRM-internal ERP-lite subsystem inside `matrix-pipeline`. Subsystem state lives **app-private in CRM app DB** (Lovable-managed) — not in CDL, not in SSO. The subsystem **does not** duplicate:

- `matrix-fm` (the platform Financial Management) — `matrix-fm` operates at entity level (legal entity, BU, annual plan, CORE allocation), not deal level.
- The external Finance ERP ([wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission), [wiki/integration.md#finance-erp-payments](integration.md#finance-erp-payments)) — the Finance ERP is the **system of record for actual money flow** (legally significant ledger of commissions and payments). The Commission Engine is an **operational advisory tool** for the broker.
- Canonical RESO — the subsystem **does not introduce new first-class data entities** in the RESO domain; it operates on app-private state that references canonical RESO keys (`TransactionManagementKey`, `MemberKey`, `Property.ListPrice` etc.) in CDL.

Source: raw/context-v2.md §9.15.

## Scope — inside vs outside {#scope}

| Concern | Inside CRM (Commission Engine, app-private) | Outside CRM (external Finance ERP) |
|---|---|---|
| Per-deal **forecast** GCI / costs / net margin | ✓ | — |
| Per-broker **forecast** compensation via rule engine | ✓ | — |
| Per-deal **actual** GCI / commission split | — | ✓ (legal ledger) |
| Invoicing, taxes, currency conversion, bank reconciliation | — | ✓ |
| Variance computation forecast vs actual | ✓ (computed on Finance-ERP webhook) | (source of actual) |
| Rule engine + admin UI to publish commission rules | ✓ | — |
| Sales-broker advisory ("pursue / drop / escalate") | ✓ via FR-AI-MAR | — |

## Data-model stub (designed in Lovable) {#data-model-stub}

Detailed schema, formulas, and FRs are designed in Lovable during Phase 5. Conceptual app-private entities cited across the BRD:

| Entity | Role | Source-of-truth signal |
|---|---|---|
| `DealCostEvent` | A single attributed operational cost (legal hours, marketing spend, conference fee, showing logistics, negotiation effort, client-care, research, other) | Created by broker / sales manager / auto-derived from tagged `Activity` rows (see FR-ACT-10) |
| `CostRateCard` | Reference rates (hourly, fixed, per-event) applied when a `DealCostEvent` doesn't carry a custom amount | Admin UI; rights `managing_partner` / `finance_admin` |
| `CommissionRule` | Rule type definitions and parameters (PercentOfGCI / TierBased / SplitBased / BaseAndBonus / TeamOverride / Composite) | Admin UI; rights `managing_partner` / `compliance` / `finance_admin` |
| `DealPnL` (computed view) | Per-`TransactionManagement` aggregate: forecast GCI, attributed costs, net margin | Derived from `TransactionManagement.OfferAmount` (or `SavedSearch` budget mid-point per FR-FNL-12) + `DealCostEvent` rows + applied `CommissionRule` |
| `BrokerCompensation` (computed view) | Per-`Member` payout breakdown on a given deal | Derived from `DealPnL` + applied `CommissionRule` + linked `TeamMembers` |

All FK references to canonical RESO keys (`TransactionManagementKey`, `PropertyKey`, `MemberKey`) are **logical pointers across projects**, not canonical RESO relationships.

Source: raw/context-v2.md §9.15.

## High-level capabilities {#capabilities}

(Implementation details designed in Lovable during Phase 5. The BRD records the capabilities only.)

- **Capture operational deal costs** (legal / marketing / conferences / showings / negotiation / client-care / research / other) via `Activity` tagging (FR-ACT-10) and/or manual entry.
- **Forecast GCI per funnel stage** based on `ListPrice` or `OfferAmount` × commission rate × stage probability (FR-FNL-12 precedence: `OfferAmount` (a) > `SavedSearch` budget mid-point (b); switching emits `HistoryTransactional` row).
- **Configurable broker compensation rule engine** — % of GCI, tiers, split by contribution, base + bonus, team override, composite. Rule types, formulas, scope, priority defined in Lovable.
- **Per-deal P&L and forecast broker compensation** visible to the broker and the manager on the TM card (FR-TM-13).
- **Reconciliation at close**: actual GCI / payment → recompute compensation → variance alert ([#reconciliation](#reconciliation)).
- **AI Deal Margin Coach** ([wiki/ai.md#deal-margin-coach](ai.md#deal-margin-coach)) — natural-language explanation + anomaly detection + "pursue / drop / escalate" suggestions on top of the subsystem.

Source: raw/context-v2.md §9.15.

## Reconciliation with external Finance ERP {#reconciliation}

```mermaid
flowchart LR
  T["TransactionManagement.OfferAmount<br/>(or SavedSearch budget mid-point)"] --> F["Forecast GCI<br/>(CRM Commission Engine)"]
  F --> R["Apply CommissionRule<br/>→ Forecast BrokerCompensation"]
  R --> TM["Display on TM card<br/>(FR-TM-13)"]
  WH["Finance ERP webhook<br/>commission_recorded<br/>(see Integration)"] --> A[Actual GCI in CRM]
  A --> V["Compute variance<br/>(actual − forecast)"]
  V -->|"|variance| > threshold"| H["HistoryTransactional row<br/>+ Activity notification to Member / sales_manager"]
  V --> MC[AI Deal Margin Coach surfaces variance]
```

**Pattern**:

1. CRM forecasts GCI + broker compensation at each funnel stage; stores results in app-private computed views (`DealPnL`, `BrokerCompensation`).
2. On `OfferAmount` change (offer, counter-offer, amended offer), the subsystem recomputes; emits `HistoryTransactional` (`MajorChangeType = Forecast base change` per FR-FNL-12, or `MajorChangeType = Forecast recompute`).
3. At close, the external Finance ERP pushes a webhook (e.g. `commission_recorded`) with actual GCI + final split — see [wiki/integration.md#finance-erp-commission](integration.md#finance-erp-commission).
4. CRM ingests the actual into the subsystem; reruns the compensation derivation; computes variance forecast vs actual.
5. If `|variance| > threshold` (configured in admin UI), CRM emits a `HistoryTransactional` row and an `Activity` notification for the responsible `Member` / sales manager.
6. The AI Deal Margin Coach ([wiki/ai.md#deal-margin-coach](ai.md#deal-margin-coach)) surfaces the variance and proposes a root-cause analysis.

**Closed Won gating** ([wiki/overview.md#pipeline](overview.md#pipeline)): `Property.StandardStatus = Closed` + full-payment webhook from ERP ([wiki/integration.md#finance-erp-payments](integration.md#finance-erp-payments)) + an existing `TransactionManagement` row + reconciliation in this subsystem completed.

**What CRM does NOT do**:

- Maintain a legally significant ledger.
- Issue invoices.
- Pay out money.
- Generate AI-modified commission rules or cost rates (FR-AI-MAR-03).

Forecast and compensation derivation are an **operational advisory tool**, not a legal record.

Source: raw/context-v2.md §9.15, §10.9, §10.10.

## Why this is in CRM (escape hatch) {#deviation}

Canonical RESO DD 2.0 has no deal-level P&L or commission-ledger resources — the canonical [`canonical-processes/processes/transaction-lifecycle.md`](../../../business-processes/canonical-processes/processes/transaction-lifecycle.md) explicitly says under Non-goals: *"No commission ledger; project flavours encode that. No escrow milestones; project flavours encode them."*

`matrix-fm` covers entity-level (legal entity, BU, annual plan) — not deal level.

The external Finance ERP holds the legal ledger of actual money — not the operational advisory forecast a sales broker needs at every funnel stage.

Therefore the BRD accepts an **explicit project-flavour deviation**, scoped to CRM app DB, with a published escape-hatch entry — see [wiki/architecture.md#escape-hatch](architecture.md#escape-hatch).

**Deliverable**: ADR `ADR-XXX: CRM Internal Commission Engine for Sales Brokers` in `matrix-platform-kb/docs/architecture/decisions/` (status TODO).

Source: raw/context-v2.md §11.6.
