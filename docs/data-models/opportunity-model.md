---
title: Opportunity model — stored CDL super-resource, calculated stage
---

# Opportunity model (`opportunity` + `opportunity_link`)

> Governing decision: [ADR-034](../architecture/decisions/ADR-034.md). This is a
> **project-flavour CDL resource** (no RESO DD 2.0 equivalent), in the same family
> as `referral` / `document` / `showing_participation` ([ADR-025](../architecture/decisions/ADR-025.md),
> [ADR-033](../architecture/decisions/ADR-033.md)). It is the **subject of the
> 5-stage pipeline**; the **stage itself is calculated, never stored**.

## Purpose

An **Opportunity** is the explicit, stable anchor for one client sales intent. It
aggregates every CRM sub-resource bound to that intent and is the unit the pipeline
projects a stage onto. It replaces the implicit `(Contacts × SavedSearch)` pair as
the pipeline subject while preserving the rule that the **stage is never
materialized** (Pipeline gate, [architecture.md](../product-specs/matrix-pipeline/wiki/architecture.md)).

- Created **from a contact** or **without a contract** (e.g. originated from
  another site / inbound web lead).
- Links 0..N of each sub-resource: `saved_search`, `contact_listings`,
  `showing`/`showings`, `caravan`, `referral`, `transaction_management`.
- Stage is derived on read from the linked sub-resources' lifecycles.

## `public.opportunity`

Stored anchor + minimal header. **No `stage` column.** Source envelope mirrors
`referral`/`document`.

| Column | Type | Notes |
|---|---|---|
| `id` | uuid PK | surrogate, `gen_random_uuid()` |
| `source_id` | text | envelope; defaulted to `matrix-pipeline` by `cdl-write` |
| `source_opportunity_key` | text | natural key with `source_id` (`unique`) |
| `content_hash` | text | envelope |
| `is_visible` / `is_deleted` / `deleted_at` | bool/bool/timestamptz | soft-delete |
| `opportunity_key` | text | canonical key (auto-minted by `cdl-write`) |
| `opportunity_id` | text | optional external id |
| `contact_key` | text | primary/anchor contact (loose ref → `contacts.contact_key`); **nullable** to allow create-without-contact origins |
| `owner_member_key` | text | owning agent (loose ref → `members.member_key`) |
| `title` | text | human label |
| `origin` | text | `contact` \| `web` \| `referral` \| `import` \| … (supports "from another site") |
| `opportunity_status` | text | `open` \| `won` \| `lost` \| `archived` — **operational lifecycle of the anchor only**, NOT the funnel stage |
| `close_reason` | text | free text for won/lost |
| `tenant_id` | text | tenant scoping |
| `modification_timestamp` / `original_entry_timestamp` | timestamptz | |
| `originating_system_*` / `source_system_*` | text | provenance triple |
| `locked_fields` / `raw` | jsonb | stewardship + envelope |
| `created_at` / `updated_at` | timestamptz | `cdl_set_updated_at` trigger |

> `opportunity_status` (`open`/`won`/`lost`) is the **anchor's** operational state
> for filtering/archival. It is distinct from the **calculated funnel stage**
> (`qualification`/`matching`/`viewing`/`contract`/`closed`), which is derived and
> never stored. A `lost` anchor is hidden from the active funnel regardless of
> derived stage.

## `public.opportunity_link`

Many-to-many join from an opportunity to its sub-resources. **Loose text refs, no
FK** (consistent with the CDL envelope; see [ADR-034](../architecture/decisions/ADR-034.md) D3).

| Column | Type | Notes |
|---|---|---|
| `id` | uuid PK | surrogate |
| `source_id` | text | envelope |
| `source_opportunity_link_key` | text | natural key with `source_id` (`unique`) |
| `is_visible` / `is_deleted` / `deleted_at` | | soft-delete |
| `opportunity_link_key` | text | canonical key |
| `opportunity_key` | text | parent opportunity (loose ref → `opportunity.opportunity_key`) |
| `resource_name` | text | `Contacts` \| `SavedSearch` \| `ContactListings` \| `Showing` \| `ShowingAppointment` \| `Caravan` \| `Referral` \| `TransactionManagement` |
| `resource_key` | text | the linked row's canonical key |
| `role` | text | `subject` \| `buyer` \| `seller` \| `target_listing` \| `offer` \| … |
| `added_at` | timestamptz | |
| provenance + `raw` + timestamps | | same envelope |

A deterministic source key `<opportunity_key>:<resource_name>:<resource_key>` makes
linking idempotent.

## Calculated stage

`deriveOpportunityStage(signals)` (app: `src/lib/opportunityStage.ts`) maps the
union of the linked sub-resources' lifecycles to the 5 funnel stages, reusing the
ADR-029 derivation:

| Stage | Derivation (most-advanced-first) |
|---|---|
| `closed` | any linked `Property.StandardStatus = Closed`/`Pending`, or a linked accepted/closed `TransactionManagement` (deal-won vs settled sub-state per ADR-029) |
| `contract` | a linked `TransactionManagement` offer exists, or target property `Active Under Contract` |
| `viewing` | ≥1 linked showing/appointment |
| `matching` | ≥1 linked `SavedSearch`, or ≥1 `ContactListings.ListingSentTimestamp` |
| `qualification` | default — anchor + contact only, no advanced signal yet |

`opportunity_status = lost` ⇒ off-funnel (Closed Lost); `won` with settlement ⇒
Closed (settled). Nothing here is persisted on the opportunity row.

## Access path

- **Write**: `cdl-write` dispatcher (`resource: 'opportunity' | 'opportunity_link'`),
  insert/update/upsert/delete; envelope + `HistoryTransactional` auto-emitted. No
  app service-role key ([ADR-012](../architecture/decisions/ADR-012.md)).
- **Read**: `cdl-read` (`resource: 'opportunity' | 'opportunity_link'`), filterable
  by `opportunity_key` / `contact_key` / `owner_member_key` / `resource_name` /
  `resource_key`. Service-role-only at the table (PII-adjacent — links Contacts).
- **No stage write path.**

See the app-side EF contract mirror at
`matrix-pipeline-2-0/docs/cdl-ef-contracts/opportunity.md`.
