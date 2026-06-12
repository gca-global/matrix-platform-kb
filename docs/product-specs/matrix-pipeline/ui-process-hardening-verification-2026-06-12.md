---
title: UI ↔ data core-process hardening verification — matrix-pipeline-2-0 (Week 7)
status: active
last_updated: 2026-06-12
tags: [verification, hardening, ui, cdl, history-transactional, week-7]
instances: docs/product-specs/matrix-pipeline/phases.md#week-7
---

# UI ↔ data core-process hardening verification — `matrix-pipeline-2-0`

> Week-7 staging-hardening pass. Each canonical business process was driven
> **through the production UI** (`https://intranet.sharpsir.group/pipeline/`) as
> **Sergey Seregin — System Admin**, and every side-effect was asserted against the
> live CDL (`ofzcokolkeejgqfjaszq`) and app DB (`kzvhqgpedapzqmwgikrw`) via Supabase
> MCP — row deltas, `history_transactional` emissions, and Edge-Function logs.
> Method: browser MCP for UI, Supabase MCP for data assertions.
> Full run ledger (with row keys/timestamps) and the discrepancy backlog live in the
> run artifact `~/tmp/pipeline-ui-process-verification-2026-06-12.md`.

## Verdict — core processes verified; one major gap (commission waterfall)

**8 PASS / 1 PARTIAL / 0 FAIL.** Every UI action maps to the correct canonical
process ([`wiki/processes.md`](wiki/processes.md)) and invokes the expected Edge
Function; all canonical row mutations and `history_transactional` rows were observed.
The single material gap is the **commission waterfall**, which does not compute from
the Deal P&L UI (blocks the commission-estimate / variance / finance-webhook chain).

| Process | UI surface | EF | Verdict |
|---|---|---|---|
| Contact funnel/lifecycle (`#contact-funnel`) | `/contacts` | `cdl-write` | **PASS** |
| SavedSearch + Prospecting (`#fr-pros-prospecting`) | `/saved-searches` | `cdl-write` | **PASS** |
| Property matching → ContactListings (`#property-matching`) | `/properties`, Engagement | `cdl-write` | **PASS** |
| Showing chain (`#showing-process`) | `/showings` | `cdl-write` | **PASS** |
| Caravan (`#fr-cara-caravan`) | `/caravans` | `cdl-write` | **PASS** |
| Offer-to-Closing (`#offer-to-closing`) | `/transactions` | `cdl-listing-lifecycle` | **PASS** |
| Commission P&L + Reports (`commission-engine.md`) | Deal P&L, `/reports` | (waterfall engine) | **PARTIAL** |
| Referral + Documents (`#referral-lifecycle`, `#fr-doc-documents`) | `/referrals`, Documents | `cdl-write` | **PASS** |
| `/pipeline` projection (`overview.md#pipeline`) | `/pipeline` | read-model | **PASS** |

## What works well (confirmed canonical behaviour)

- **Single-EF write discipline:** all create/modify flows route through `cdl-write`
  (or `cdl-listing-lifecycle` for status transitions) — no direct PostgREST writes
  observed. Matches [`cdl-crud-contract.md`](cdl-crud-contract.md).
- **HistoryTransactional emission (FR-CFL-14 / §10.7):** every mutating action emits
  a `history_transactional` row keyed by `resource_name` + `resource_record_key` +
  `changed_by_member_key`. The **offer-to-closing** flow is the highest-fidelity:
  rows capture `previous_value` **and** `new_value` plus a full `raw` payload.
- **ADR-029 dual vocabulary confirmed:** lifecycle `to_state`
  (`ActiveUnderContract`/`Sold`/`Active`) ↔ RESO `StandardStatus`
  (`Pending`/`Closed`/`Active`) ↔ UI labels ("Under Contract"/"Closed"/"Back On Market")
  map consistently across `property_lifecycle_events`, `properties.standard_status`,
  and `history_transactional.change_type`.
- **Showing chain auto-cascade:** recording a showing auto-creates the ContactListing
  link, writes feedback as a note, and stamps the preference (Favorite) — a coherent
  4-step cascade, all attributed to the acting admin.
- **Caravan "one showing per stop":** completing a 2-stop run records exactly one
  `showing` per stop, each `caravan_key`-linked; caravan status auto-advances Active→Ended.
- **Pipeline projection is a faithful read-model:** one card per (Contact × SavedSearch),
  correct stage, with a "Why is this here?" explainer that cites the underlying
  offer/contract signal (`overview.md#pipeline`).
- **Referral introduced-by badge** renders on the referee's contact detail, derived
  from the `referral` row (no denormalised contact column needed).

## Discrepancy backlog (severity P1 → P3)

**P1 — major functional gap**
- **F-P6-1 — Commission waterfall never computes** from the Deal P&L UI despite all
  stated preconditions met (Closed deal w/ list+close price, country rule resolves,
  date-of-sign + object set). No `commission_estimate` row, no error/toast. Blocks HU
  waterfall numbers, inline override, variance, and `finance-erp-webhook.actual_gci`
  (see [`wiki/commission-engine.md`](wiki/commission-engine.md)). **Needs dev
  investigation of the Deal P&L compute trigger before Week-7 sign-off.**

**P2 — correctness / integrity**
- **F-P5-2** — `cancelDeal` from a terminal Sold/Closed state is **silently rejected**
  (state-guard correct, but no UI feedback — dialog hangs, no toast).
- **F-P2-1** — `prospecting.next_send_timestamp` is **NULL** on "Create & subscribe";
  first cycle is not scheduled at write time (a backend job did later fire a reminder).
- **F-P6-2** — **3 duplicate published HU `commission_rule` rows at identical priority 100**
  → no deterministic rule-selection tie-breaker.
- **F-P6-3** — `deal_cost_event` written with `member_key=""` and `transaction_key=null`
  (cost tied only to `listing_key`).
- **F-P3-1 / F-P4-4** — note authorship: `created_by_member_key` null and `noted_by`
  is the contact **owner**, not the acting author.

**P3 — fidelity / provenance / cosmetic**
- **F-P7-1** — referral does not set referee `LeadSource=Referral` (badge is fine).
- **F-P5-1** — `properties.mls_status` not synced to lifecycle (only `standard_status` moves).
- **History field-level fidelity** (F-P1-2 / F-P3-3 / F-P4-5) — contact create/modify and
  the field-level rows carry null `field_name`/`new_value` (row-level audit met; field deltas absent).
- **Provenance stamp** (F-P2-2 / F-P3-2 / F-P4-1 / F-P7-2) — `originating_system_name`
  consistently null across saved_search/notes/showings/referral/document/lifecycle
  (though `source_system_name`/`source_id=matrix-pipeline` is set).
- **F-P4-2 / F-P4-3 / F-P4-6 / F-P4-7** — appointment stays Confirmed after record;
  auto ContactListing keeps `listing_viewed_yn=false`; no history for caravan header
  create/complete; caravan-run showings are property-only (no contact Activity).
- **F-P1-1** — `contacts.full_name` left null on create.
- **F-P5-3** — "escrow lock" is not a stored property column (implicit via status gating
  + lifecycle audit) — expectation gap vs. plan wording.

## Test data lifecycle

A single golden-thread test contact (**ZZ-UITEST Goldenthread**) and all derived
records (saved_search, prospecting, contact_listings/notes, full showing chain, a
2-stop caravan, referral, document, a `deal_cost_event`) were created during the run,
then **fully removed** afterwards. Real listings **14058 / 14067** (touched by the
offer-to-closing test) were **restored to `Active`** with contract/close fields cleared.
Post-cleanup row counts equal the pre-run baseline exactly (incl. `history_transactional`
restored to 59). The pre-existing smoke-test thread (contact `d62ea8b4`, referral
`c681ae03`, `SMOKE-001`) was left untouched.

## KB sources consulted

- [`wiki/processes.md`](wiki/processes.md) — canonical process definitions (P1–P5, referral)
- [`wiki/entities.md`](wiki/entities.md) — entity/field expectations (showing chain, caravan, referral, document)
- [`wiki/commission-engine.md`](wiki/commission-engine.md) — commission P&L model (P6)
- [`wiki/integration.md#history-emission`](wiki/integration.md) — HistoryTransactional contract
- [`cdl-crud-contract.md`](cdl-crud-contract.md) — write-path discipline
- [`overview.md#pipeline`](wiki/overview.md) — pipeline-as-projection
- [`phases.md#week-7`](phases.md) — Week-7 hardening scope
- ADR-026 / ADR-028 (TransactionManagement + app-private commission tables) and ADR-029 (deal-won vs settled labels)

## Follow-ups recommended

1. **Fix F-P6-1 (commission waterfall trigger)** — gating item for Week-7 sign-off.
2. De-duplicate the published HU `commission_rule` rows (F-P6-2) and add a deterministic priority tie-breaker.
3. Add user feedback for terminal-state `cancelDeal` (F-P5-2); initialise `prospecting.next_send_timestamp` on subscribe (F-P2-1).
4. Tighten audit attribution: stamp `created_by_member_key` on notes + `member_key`/`transaction_key` on `deal_cost_event` (F-P3-1/F-P4-4/F-P6-3).
5. Backfill `originating_system_name` provenance across all `cdl-write` paths (cross-cutting P3).
