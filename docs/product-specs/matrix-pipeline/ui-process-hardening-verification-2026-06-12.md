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

> **Remediation complete + P1 re-validated (2026-06-12)** — the full discrepancy backlog
> below has been remediated under plan `pipeline_compliance_remediation`, and the P1
> blocker (F-P6-1 commission waterfall) was **re-validated end-to-end through the staging
> UI** (waterfall computes + `commission_estimate` persisted, keyed by the property's
> `originating_system_key`). See [§Remediation status](#remediation-status-2026-06-12)
> for the per-finding resolution and the runtime re-validation log. Code: `tsc`+`vite build`
> clean; CDL EFs redeployed (cdl-write v9, cdl-listing-lifecycle v2); HU `commission_rule`
> de-duplicated to one published row. **Week-7 sign-off gate cleared.**

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

## Remediation status (2026-06-12)

All backlog items are resolved (code + CDL EF + one app-DB migration). Routing per
`.cursor/rules/cursor-git-handoff.mdc`: UI + app migration → `matrix-pipeline-2-0`;
CDL EFs → `matrix-platform-foundation`; this doc → `matrix-platform-kb`.

| Finding | Resolution | Where |
|---|---|---|
| **F-P6-1** waterfall never computes | `useCommissionEstimate` property lookup now also matches `originating_system_key` (the key `Transactions.tsx` passes); + persist-failure toast + split placeholder copy | `src/hooks/useCommissionEstimate.ts`, `components/commission/DealPnLTab.tsx` |
| **F-P6-2** duplicate HU rules | unpublished the two `(v2)` duplicates (identical params) via migration; deterministic `id` tie-breaker in `resolveRule` | app-DB migration `20260612143031_*`, `src/lib/commission/resolveRule.ts` |
| **F-P6-3** deal-cost attribution | `member_key` = acting member via new `useActingMemberKey`; `transaction_key` already linked when selected | `src/hooks/useActingMemberKey.ts`, `components/commission/DealCostLogCard.tsx` |
| **F-P7-1** referee LeadSource | **No change — working as designed.** `useCreateReferral` already sets `lead_source='Referral'` *only when unset* (FR-REF-02); the verification referee already had `Website`, correctly preserved | `src/hooks/useReferrals.ts` |
| **F-P1-2 / F-P3-3 / F-P4-5** field-level history | `cdl-write.emitHistory` writes `new_value`/`previous_value`; app callers pass `fieldValue`/`previousValue` | `cdl-write`, `useContactMutations`, `useContactListingsEngagement`, `useProspecting`, `useReferrals` |
| **F-P2-2 / F-P3-2 / F-P4-1 / F-P7-2** provenance | `cdl-write` defaults `originating_system_name` + `source_system_name` on source_id-envelope tables that carry them | `cdl-write` |
| **F-P2-1** prospecting schedule | `next_send_timestamp = now()` on Create & subscribe | `src/hooks/useProspecting.ts` |
| **F-P3-1 / F-P4-4** note authorship | `noted_by` + `created_by_member_key` = acting member (UI + EF belt-and-suspenders) | `useContactListingsEngagement`, `ContactListingsPanel`, `cdl-write` |
| **F-P5-1** mls_status sync | `cdl-listing-lifecycle` sets `mls_status = standard_status` on each transition | `cdl-listing-lifecycle` |
| **F-P5-2** cancelDeal UX | EF guard broadened (`TERMINAL_STATE`/`NOT_UNDER_CONTRACT` codes); UI gates the button on `Pending`, surfaces the error toast | `cdl-listing-lifecycle`, `pages/Transactions.tsx` |
| **F-P1-1** full_name | composed from first+last on write when absent | `src/lib/contactsSchema.ts` |
| **F-P4-3** listing_viewed_yn | a recorded showing marks the auto ContactListing viewed | `pages/Showings.tsx` |
| **F-P4-2** appointment terminal state | appointment advances to `Completed` on record | `pages/Showings.tsx`, `useShowingChain.ts` |
| **F-P4-6** caravan header history | header create/status-change/complete emit Caravan-scoped history rows | `src/hooks/useCaravans.ts` |
| **F-P5-3** escrow lock | **KB clarification:** escrow is enforced via the EF's `cdl_lock_field`/`cdl_unlock_field` RPCs + status gating, not a stored `x_escrow_locked` column. No schema change. | `cdl-listing-lifecycle` |
| **F-P4-7** caravan-run contact Activity | unchanged — broker-preview tours are property-only by design (not a defect) | — |

### Runtime re-validation (staging UI, post-deploy 2026-06-12)

Re-run through the production UI (`/pipeline/`, Sergey Seregin / System Admin) against
the watcher-deployed build, asserted via Supabase MCP (app DB `kzvhqgpedapzqmwgikrw`):

- **F-P6-1 — CONFIRMED FIXED end-to-end.** Selected listing **14067** (Active, list
  price EUR 1,800,000) as the Transactions subject. Deal P&L now resolves the property
  by `originating_system_key`: the Deal narrative auto-fills **country: CY** and the
  waterfall renders. With a published CY rule resolving, the full waterfall computed
  (Gross EUR 72,000 → VAT −15,307 → Net 56,693 → Royalty −4,535 → Gross profit 52,157
  → Broker fee −18,255 → PBT 33,902) and a `commission_estimate` row persisted, keyed
  by `listing_key = QOBRIX_58fb319b-…` (i.e. the property's `originating_system_key` —
  the exact key the old lookup missed) with `base_source=list_price`,
  `commission_rule_id` set, and stored totals byte-matching the UI. Pre-fix this never
  computed and wrote nothing.
- **F-P6-2 — CONFIRMED.** `commission_rule` now has exactly **one** published row
  (`HU default waterfall`); the two `(v2)` duplicates are unpublished. The new placeholder
  copy ("No published commission rule resolves for CY. Add one under Country rules.")
  rendered correctly when no CY rule was published — proving the property/country path
  resolves and only the rule was absent.
- **B5 / F-P5-2 — CONFIRMED (UI gating).** With the Active listing 14067 selected,
  **Cancel deal** is disabled and **Close deal** enabled — the status-gated
  `CancelDealAction` behaves as designed (cancel only for under-contract deals).
- Test data created during the run (one temp published CY rule + the resulting
  `commission_estimate`) was **fully removed**; post-run baseline restored
  (`commission_estimate` = 0; one published rule = HU). The pre-existing CY/KZ drafts
  were left untouched.

Remaining backlog items (field-level history detail, provenance stamping, prospecting
`next_send_timestamp`, note authorship) are code-verified and the CDL EFs are deployed
(cdl-write v9); they can be exercised in a future golden-thread UI run but are not
gating — the P1 blocker (F-P6-1) is closed.

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
