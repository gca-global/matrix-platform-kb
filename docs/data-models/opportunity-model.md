---
title: Opportunity model — App-DB-private super-resource, calculated stage
---

# Opportunity model (`opportunity` + `opportunity_link`)

> Governing decision: [ADR-035](../architecture/decisions/ADR-035.md) (supersedes
> [ADR-034](../architecture/decisions/ADR-034.md)). This is an **App-DB-private CRM
> resource** in the Pipeline App DB (`kzvhqgpedapzqmwgikrw`, Lovable-managed), in
> the same family as `activities` / `role_configurations` / the commission engine
> — **not** a CDL resource (RESO DD 2.0 has no Opportunity/Deal). It is read and
> written **directly with the `supabase` app client under SSO-claim RLS**, never
> through `cdl-write`/`cdl-read`. It is the **subject of the 5-stage pipeline**;
> the **stage itself is calculated, never stored**.

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

Stored anchor + minimal header in the **App DB**. **No `stage` column.** App-DB
Pattern B columns (mirrors `public.activities`).

| Column | Type | Notes |
|---|---|---|
| `id` | uuid PK | surrogate, `gen_random_uuid()` |
| `tenant_id` | uuid | `get_current_tenant_id()` default; RLS scope |
| `owner_id` | uuid | `get_my_record_id_v2()` (SSO `sub`) default; RLS self/team scope |
| `opportunity_key` | text UNIQUE | stable text correlation id (`gen_random_uuid()::text` default); used by links |
| `opportunity_id` | text | optional external id |
| `contact_key` | text | primary/anchor contact (loose ref → CDL `contacts.contact_key`); **nullable** to allow create-without-contact origins |
| `owner_member_key` | text | owning agent (CDL `members.member_key`) for display/assignment — NOT the RLS owner |
| `title` | text | human label |
| `origin` | text | `contact` \| `web` \| `referral` \| `import` \| … (supports "from another site") |
| `opportunity_status` | text | `open` \| `won` \| `lost` \| `archived` — **operational lifecycle of the anchor only**, NOT the funnel stage |
| `close_reason` | text | free text for won/lost |
| `modification_timestamp` / `created_at` / `updated_at` | timestamptz | trigger-maintained (`opportunity_touch_timestamps`) |

> `opportunity_status` (`open`/`won`/`lost`) is the **anchor's** operational state
> for filtering/archival. It is distinct from the **calculated funnel stage**
> (`qualification`/`matching`/`viewing`/`contract`/`closed`), which is derived and
> never stored. A `lost` anchor is hidden from the active funnel regardless of
> derived stage.

## `public.opportunity_link`

Many-to-many join from an opportunity to its CDL sub-resources. **Loose text refs,
no FK** (the sub-resources live in the CDL, resolved app-side; see
[ADR-035](../architecture/decisions/ADR-035.md) D3, carried from ADR-034 D3).

| Column | Type | Notes |
|---|---|---|
| `id` | uuid PK | surrogate |
| `tenant_id` | uuid | RLS scope |
| `owner_id` | uuid | RLS self/team scope |
| `opportunity_link_key` | text UNIQUE | deterministic `<opportunity_key>:<resource_name>:<resource_key>` (idempotent) |
| `opportunity_key` | text | parent opportunity (loose ref → `opportunity.opportunity_key`) |
| `resource_name` | text | `Contacts` \| `SavedSearch` \| `ContactListings` \| `Showing` \| `ShowingAppointment` \| `Caravan` \| `Referral` \| `TransactionManagement` |
| `resource_key` | text | the linked CDL row's canonical key |
| `role` | text | `subject` \| `buyer` \| `seller` \| `target_listing` \| `offer` \| … |
| `added_at` / `modification_timestamp` / `created_at` / `updated_at` | timestamptz | |

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

- **Read + Write**: direct `supabase` app client
  (`supabase.from('opportunity' | 'opportunity_link')`) under SSO-claim RLS
  (Pattern B, 5-level scope). **NOT** a `cdl-write`/`cdl-read` resource; never
  routed through `invokeCdl`. The app sends the SSO ES256 JWT on every App-DB
  request and holds no CDL service-role key ([ADR-013](../architecture/decisions/ADR-013.md)).
- **Sub-resource resolution**: the detail view resolves each linked CDL
  sub-resource (Contacts / SavedSearch / ContactListings / Showing / …) via its
  existing CDL read EF — there is no cross-project SQL join.
- **No stage write path.**

App schema: `matrix-pipeline-2-0/supabase/migrations/20260618120000_opportunity_appdb.sql`.
See the app-side data-model doc at `matrix-pipeline-2-0/docs/opportunity-appdb.md`.
