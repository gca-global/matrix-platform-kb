---
title: Lovable CDL CRUD contract
status: active
source: mem://infrastructure/lovable-cdl-crud-contract.md (iteration copy)
last_synced: 2026-05-29
last_updated: 2026-05-29
tags: [infrastructure, lovable, crud, cdl, contract]
---

# Lovable CDL CRUD contract — Matrix Pipeline

> **For Lovable**: Read this before generating ANY code that touches the CDL Supabase project (`ofzcokolkeejgqfjaszq`). The companion reachability matrix lives in the iteration copy at `mem://infrastructure/cdl-coverage.md` (Pipeline-team operational doc). This doc tells you HOW to write code; the coverage doc tells you WHAT is reachable.
>
> **2026-05-29 update (ADR-016 landed):** the canonical CRM resources now have a **live CDL home**. The generic `cdl-write` dispatcher EF + `cdl-contacts-read` + `cdl-contact-listings-read` are **deployed**. `contact_listings` + `contact_listing_notes` are now **RLS-enabled** (the prior gate violation is closed). The CRM app DB remains the write target only for app-private resources (`Activity`, `Document`, `Campaign`, `Referral`) and for deal economics (offer amount / commission / P&L) that have no RESO resource. Everything canonical-RESO now writes through `cdl-write`.
>
> **Sync contract**: this file is the canonical copy. The iteration copy lives at `mem://infrastructure/lovable-cdl-crud-contract.md` in the matrix-pipeline Lovable repo. Divergence between the two is treated as a defect — sync on every meaningful change.

## TOC

- [#two-clients](#two-clients)
- [#read-a](#read-a)
- [#read-b](#read-b)
- [#read-c](#read-c)
- [#write-a](#write-a)
- [#write-b](#write-b)
- [#commandments](#commandments)
- [#quick-reference](#quick-reference)
- [#ef-ship-checklist](#ef-ship-checklist)
- [#anti-patterns](#anti-patterns)

## Two clients, two scopes, one JWT {#two-clients}

Pipeline talks to three Supabase projects. The client setup is canonical and mandatory:

```typescript
import { ssoClient, cdlClient } from '@/lib/dataLayerClient';
import { supabase as appClient } from '@/lib/client';
const ssoJwt = await getSsoAccessToken();
```

| Client | Project | Use for |
|---|---|---|
| `ssoClient` | `xgubaguglsnokjyudgvc` (SSO) | identity, roles, permissions, `useUserDisplay`, `resolve-users` EF |
| `cdlClient` | `ofzcokolkeejgqfjaszq` (CDL) | **reads** of allow-listed public canonical resources via direct PostgREST (anon SELECT policy, `qual = true`); **scoped/PII reads + all writes** via dedicated Pipeline EFs (SSO JWT auto-injected by `invokeCdl`) |
| `appClient` | per-app DB (Lovable-managed) | every CRM app-private resource + every Phase-1-4 write that does not yet have a Pipeline EF |

The **same SSO JWT** is the bearer for SSO and for every CDL **EF** call. CDL verifies it via Supabase Third-Party Auth ([`../../architecture/decisions/ADR-012.md`](../../architecture/decisions/ADR-012.md)). Pipeline **never** holds the CDL service-role key.

## Access-mechanism decision rule (Supabase-grounded) {#access-rule}

This is the one rule that decides *how* any given CDL resource is reached. It is grounded in Supabase's own guidance, not invented here:

- **Supabase Data API + RLS is the default for reads.** Per [Securing your API](https://supabase.com/docs/guides/api/securing-your-api): "The data APIs are designed to work with Postgres Row Level Security… Any table you create in the `public` schema will be accessible via the Supabase Data API. To restrict access, enable RLS." So **public, non-sensitive** canonical tables that carry an anon `SELECT` policy (`qual = true`) are read **directly via PostgREST** on `cdlClient` (the anon key is sufficient — no identity needed for global reference data). This is the READ-A allow-list.
- **Send the JWT (or use an EF) the moment a read is identity-scoped.** Cross-project identity is carried by the **SSO JWT via Third-Party Auth** ([Third-party auth](https://supabase.com/docs/guides/auth/third-party/overview): the API "will trust JWTs issued by the provider"; requires asymmetric signing — our SSO ES256). In this architecture, identity-scoped and **PII** reads (`contacts`, `contact_listings`, `contact_listing_notes`) do **not** use JWT-scoped PostgREST — they go through a **Pipeline EF** (READ-C), because Supabase's [*"Enforce additional rules on each request"*](https://supabase.com/docs/guides/api/securing-your-api) guidance applies: "Using Row Level Security policies may not always be adequate" (PII, service-role-only RLS, server-side checks) → put it behind an Edge Function.
- **All canonical writes go through an EF.** Browsers never write CDL PostgREST directly; writes use `invokeCdl` (service-role inside the EF, SSO-JWT-scoped authz, emits `HistoryTransactional`). This is WRITE-B; until the EF ships, queue in the app-DB `*_pending` table (WRITE-A fallback).
- **Never** read an **RLS-disabled** table directly (e.g. `contact_listings` today) — Supabase warns such tables are "accessible to the public using the anon role"; that is a CDL access-gate violation. Use the EF. And **never** use the CDL service-role key in app code. (RLS-disabled here is a **temporary dev-phase condition**, not the target — target is RLS enabled per Pattern B before production sign-off; see [`wiki/architecture.md` Security advisory](wiki/architecture.md). The EF access gate is the rule during dev **and** stays the canonical write path after RLS lands, so building against it now is correct either way.)

Decision in one line: **public reference data → anon PostgREST; identity-scoped or PII → Pipeline EF; any write → Pipeline EF.** When in doubt, use the EF.

## Per-resource recipes — five shapes, no others

The matrix in [`mem://infrastructure/cdl-coverage.md` §A2](#) tells you which shape applies per resource. There are exactly five recipe shapes; Lovable must not invent a sixth.

### Recipe READ-A — direct PostgREST on the CDL client {#read-a}

For tables with RLS enabled + an anon SELECT policy with `qual = true`. Today: `members`, `offices`, `properties_published`, `property_rooms`, `property_unit_types`, `showings`, `history_transactional`, `internet_tracking_events`, `open_houses`, `mls_sources`, `reso_field_descriptions`, `reso_lookup_value_descriptions`.

```typescript
const { data, error } = await cdlClient
  .from('properties_published')
  .select('id, source_listing_key, title_en, price, currency, city, country, status, published_at')
  .eq('source_id', sourceId)
  .order('published_at', { ascending: false })
  .limit(50);
```

When to use: simple list/detail pages where server-side filtering is light and no PII is involved.

### Recipe READ-B — `listings-search` EF on the CDL client {#read-b}

For property reads that need server-side filtering, keyset pagination, media joins, or HTTP caching. `listings-search` allows `self,team,global,org_admin,system_admin` per [cdl-schema.md](../../data-models/cdl-schema.md) §Read EF.

```typescript
const { data, error } = await cdlClient.functions.invoke('listings-search', {
  body: {
    q: 'sea view',
    filters: { city: 'Limassol', minPrice: 1_000_000, status: 'Active', sourceId },
    page: 0, pageSize: 25,
    sort: { field: 'price', direction: 'desc' },
    includeMedia: true,
  },
});
```

Response shape: `{ data, total, page, pageSize }`. Sortable fields: `published_at, price, bedrooms, bathrooms, area_sqm, year_built, city, country, status, property_type`.

### Recipe READ-C — per-resource Pipeline EF (LIVE) {#read-c}

For resources that direct PostgREST cannot reach safely:
- `contacts` (PII, service-role-only RLS) → `cdl-contacts-read` ✅ **live**
- `contact_listings`, `contact_listing_notes` (RLS service-role-only since 2026-05-29) → `cdl-contact-listings-read` ✅ **live**

```typescript
const { data, error } = await cdlClient.functions.invoke('cdl-contacts-read', {
  body: {
    op: 'list',
    filter: { owner_member_key: currentMemberKey, contact_type: 'Lead' },
    scopeToOwner: true,
    page: 0, pageSize: 25,
  },
});
// Response: { data: [...], total, page, pageSize }
```

`cdl-contact-listings-read` supports `op: 'list' | 'get' | 'notes'` (the `notes`
op returns the child `contact_listing_notes` for a given `contact_listings_key`).
Both EFs are deployed (ADR-016). Hooks should still keep the `EF_NOT_AVAILABLE`
fallback branch for resilience, but it is no longer the expected path.

### Recipe WRITE-A — `appClient.from(...).insert(...)` on the CRM app DB {#write-a}

Default write path for app-private resources only:

- Already app-private forever: `Activity`, `Document`, `Campaign`, `Referral`.
- Deal economics with no RESO resource (stay app-private): offer amount, commission, deal P&L (the canonical `transaction_management` envelope itself lives in CDL — only its economics stay app-private; ADR-016 escape hatch).
- ~~App-private until CDL migration~~: `SavedSearch`, `Prospecting`, `ShowingAvailability`, `ShowingRequest`, `Showing` (recorded fact), `LockOrBox`, `Caravan`, `CaravanStop`, `TransactionManagement` — **these now have a live CDL table + write via `cdl-write` (WRITE-B). Migrated 2026-05-29 (ADR-016).** The `*_pending` queue tables remain only as the `EF_NOT_AVAILABLE` fallback.

Column names use **RESO DD 2.0 PascalCase → snake_case** so the future CDL migration is a 1:1 mirror (zero column-rename PRs):

```sql
create table public.transaction_management (
  id uuid primary key default gen_random_uuid(),
  transaction_management_key text unique,        -- RESO TransactionManagementKey
  transaction_type text not null,                -- RESO TransactionType
  offer_amount numeric,                          -- RESO OfferAmount
  currency text,
  contact_key text not null,                     -- RESO ContactKey (logical FK to CDL contacts.contact_key)
  listing_key text,                              -- RESO ListingKey (logical FK to CDL properties.source_listing_key)
  owner_member_key text,                         -- RESO OwnerMemberKey (logical FK to CDL members.member_key)
  valid_from timestamptz,
  valid_until timestamptz,
  deposit_amount numeric,
  payment_terms text,
  contingencies text,
  status text default 'Draft',                   -- Draft / Submitted / Countered / Accepted / Rejected / Withdrawn / Expired
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```

**Naming rules** (Lovable: enforce these in every generated schema and TypeScript model):
- Table names: snake_case singular for app-private, snake_case plural for canonical-RESO-mirror.
- Column names: RESO PascalCase mechanically lower-cased + underscore-joined. `OwnerMemberKey` → `owner_member_key`. `OfferAmount` → `offer_amount`. `ContactType` → `contact_type`.
- FK shape: foreign keys to CDL canonical resources use the RESO `*Key` text type (`text`, not `uuid`). When the row migrates into CDL it joins via the canonical key, not a synthetic Lovable UUID.
- Never invent column names: `customerId`, `dealAmount`, `leadStage`, `nextActionAt`, `salesRep` — all violations of the [Schema gate](wiki/architecture.md#compliance-gates).

### Recipe WRITE-B — the generic `cdl-write` dispatcher EF (LIVE) {#write-b}

One EF (`cdl-write`) handles **every** canonical-RESO write — insert / update /
upsert / soft-delete — and emits a `HistoryTransactional` row on every mutating
op. This replaces the per-resource `cdl-<resource>-write` family that ADR-015 #6
proposed (decision recorded in ADR-016: one dispatcher is cheaper to ship and
maintain; the redaction/scope contract is uniform).

Writable `resource` values: `contacts`, `members` (AD-provisioned — ADR-031),
`contact_listings`, `contact_listing_notes`, `showings` (ShowingAppointment),
`showing` (recorded), `showing_request`, `showing_availability`, `saved_search`,
`prospecting`, `lock_or_box`, `caravan`, `caravan_stop`,
`transaction_management`, `referral`, `document`,
`history_transactional` (insert-only).

```typescript
// insert / update / upsert / delete a canonical resource
const { data, error } = await cdlClient.functions.invoke('cdl-write', {
  body: {
    resource: 'contacts',
    op: 'insert',                         // insert | update | upsert | delete
    record: { contact_type: 'Lead', email: 'x@y.com', owner_member_key: memberKey },
    emitHistory: true,                    // default true
  },
});
// Response: { success: true, data: <row>, history: 'emitted' }

// History emission is automatic on every write. To emit a standalone history row:
async function emitHistory(row: HistoryTransactionalRow) {
  const { error } = await cdlClient.functions.invoke('cdl-write', {
    body: { resource: 'history_transactional', op: 'insert', record: row, emitHistory: false },
  });
  if (error?.message === 'EF_NOT_AVAILABLE') {
    await appClient.from('history_pending').insert({ payload: row, created_at: new Date().toISOString() });
    return { queued: true };
  }
  if (error) throw error;
  return { queued: false };
}
```

`update` / `delete` require `key: { column, value }` (e.g.
`{ column: 'contact_key', value: '...' }`). `delete` is a soft-delete
(`is_deleted = true`) **only on the Pipeline-authored tables** that carry the
soft-delete bookkeeping. The `*_pending` queue tables remain only as the
`EF_NOT_AVAILABLE` resilience fallback; the Phase-7 reconciler drains them.

**Two source envelopes (important for writes).** `cdl-write` keys each resource
off one of two envelopes, selected by `systemColumn`:

| Envelope | `systemColumn` | natural key | soft-delete | resources |
|---|---|---|---|---|
| Pipeline-authored | `source_id` | `(source_id, source_<resource>_key)` | yes (`is_deleted`/`deleted_at`) | `contact_listings`, `contact_listing_notes`, `showing`, `showing_request`, `showing_availability`, `saved_search`, `prospecting`, `lock_or_box`, `caravan`, `caravan_stop`, `transaction_management` |
| Strict-RESO | `originating_system_name` | `(originating_system_name, originating_system_<resource>_key)` | **no column** | `contacts`, `members`, `showings` (ShowingAppointment) |

The strict-RESO tables were hardened by the `strict_reso_wave` migrations
(`20260515130000+`), which **dropped** `source_id` / `content_hash` /
`is_deleted` / `deleted_at`. So for `contacts`, `members`, and `showings`:
upserts conflict on `(originating_system_name, originating_system_<resource>_key)`,
`cdl-write` defaults `originating_system_name` to the Pipeline source slug, mints
the canonical key (`member_key` / `contact_key` / `showing_appointment_key`) as a
UUID when absent, and **`delete` is rejected** (no soft-delete column —
hard-deleting PII is a stewardship decision, not a default). Callers must never
send `source_id`/`is_deleted` for these resources. For `members` specifically,
the Pipeline only **inserts** (provisioning a new owner from Active Directory);
the canonical roster remains master-sourced by `mls-sync` (ADR-031).

## The six commandments {#commandments}

A short checklist Lovable applies at the top of every relevant prompt:

1. **Two databases, never three.** SSO (`ssoClient`), CDL (`cdlClient`), App DB (`appClient`). Never a fourth Supabase. Never the CDL service-role key in app code.
2. **RESO names only.** Tables in the CRM app DB use canonical PascalCase → snake_case. Never `customerId`, `dealAmount`, `leadStage` — always `contact_key`, `offer_amount`, `contact_type`. FK columns to CDL canonical resources are `text` typed using the RESO `*Key` field, not `uuid`.
3. **Reads go through Recipe READ-A / READ-B / READ-C in that order.** Use direct PostgREST only on tables listed in the coverage matrix as "direct anon `select` ✓". Use `listings-search` for everything property-shaped that needs filters or pagination. Use the placeholder Pipeline EFs (READ-C) for `contacts`, `contact_listings`, `contact_listing_notes`.
4. **Canonical-RESO writes go through `cdl-write` (WRITE-B); app-private writes go to the CRM app DB (WRITE-A).** WRITE-B is now live for every canonical resource. WRITE-A is reserved for `Activity`/`Document`/`Campaign`/`Referral` and deal economics.
5. **Every state transition emits a `HistoryTransactional`.** `cdl-write` emits one automatically on every mutating op. For standalone emissions use `cdl-write` with `resource: 'history_transactional'`. Never write `public.history_transactional` directly from anon (RLS blocks it) and never write to a service-role-only table to bypass the gate.
6. **No SSO ↔ CDL SQL joins.** Display names always go through `resolve-users` EF + `useUserDisplay` hook. Member roster lookups go through `cdlClient.from('members')`. Never `select … join sso_users …` anywhere.

## Quick reference — which recipe for which resource? {#quick-reference}

| Resource | Read | Write |
|---|---|---|
| `Property` (`properties_published`) | READ-A or READ-B | n/a (Atlas-owned) |
| `Property` (raw `properties`) | use READ-B only | n/a |
| `Media` | use READ-B `includeMedia: true` | n/a |
| `PropertyRooms` / `PropertyUnitTypes` | READ-A | n/a |
| `Member` | READ-A | WRITE-B `cdl-write` resource `members` ✅ (insert = AD-provisioning of new owners; **`update` of AD-sourced fields only** — `job_title` / `x_company` — when the owner picker reconciles a drifted roster row; ADR-031). Roster is otherwise master-sourced by `mls-sync`. |
| `Office` | READ-A | n/a |
| `Contacts` | READ-C (`cdl-contacts-read`, ✅ live) | WRITE-B `cdl-write` resource `contacts` ✅ |
| `ContactListings` | READ-C (`cdl-contact-listings-read`, ✅ live) | WRITE-B `cdl-write` resource `contact_listings` ✅ |
| `ContactListingNotes` | READ-C (`cdl-contact-listings-read` op `notes`) | WRITE-B `cdl-write` resource `contact_listing_notes` ✅ |
| `ShowingAppointment` (`showings`) | READ-A | WRITE-B `cdl-write` resource `showings` ✅ |
| `SavedSearch` | READ-A (`saved_search`) | WRITE-B `cdl-write` resource `saved_search` ✅ |
| `Prospecting` | READ-C (PII, via `cdl-write`-paired read TBD) | WRITE-B `cdl-write` resource `prospecting` ✅ |
| `ShowingAvailability` / `ShowingRequest` / `Showing` (recorded) / `Caravan` / `CaravanStop` | READ-A | WRITE-B `cdl-write` (matching resource) ✅ |
| `LockOrBox` | service-role-only (access audit) | WRITE-B `cdl-write` resource `lock_or_box` ✅ |
| `TransactionManagement` | READ-A (`transaction_management`) | WRITE-B `cdl-write` resource `transaction_management` ✅ (economics stay app-private). **Authoring split:** offer-side types (`PurchaseOffer`/`LeaseOffer`/`Other`) authored by Pipeline; listing-side types (`ListingForSale`/`ListingForLease`) authored by Atlas (`matrix-atlas-mls` *Listing Transactions*). Same table, no per-app partition. |
| `HistoryTransactional` | READ-A | WRITE-B `cdl-write` resource `history_transactional` (insert-only) ✅ |
| `InternetTracking` | READ-A | WRITE-B (queue if needed) |
| `Activity` / `Document` / `Campaign` / `Referral` | n/a (CRM app DB only forever) | WRITE-A |
| `OUID` / `Teams` / `TeamMembers` | derive from SSO groups ([`../../architecture/decisions/ADR-015.md`](../../architecture/decisions/ADR-015.md) item #5 Option B) | n/a |

## When the platform team ships an EF {#ef-ship-checklist}

For each new EF ship event:

1. Update the coverage matrix in `mem://infrastructure/cdl-coverage.md` §A2 — flip "blocked"/"placeholder" → "✓".
2. Update this contract — flip the relevant table row in the quick-reference above.
3. Sync the iteration copy at `mem://infrastructure/lovable-cdl-crud-contract.md` to match.
4. Update [`phases.md`](phases.md) Phase 7 reconciler task — add a drain step for the matching `*_pending` table.
5. Bump `last_verified` in `mem://` and `last_synced` here.

## Anti-patterns Lovable must refuse to generate {#anti-patterns}

If a prompt asks Lovable to do any of the following, Lovable should push back and cite this section:

- "Just use the CDL service-role key to write directly to `public.contacts`" — No. Service-role key never leaves the platform-foundation EFs.
- "Insert into `public.history_transactional` from the React Query mutation" — No. Anon writes are blocked; use the `cdl-history-emit` EF (placeholder today) and queue in `history_pending` on `EF_NOT_AVAILABLE`.
- "Mirror `members` into the CRM app DB so we can join cheaply" — No. [Roster gate](wiki/architecture.md#compliance-gates) forbids parallel org tables. Read from `cdlClient.from('members')` and cache with React Query.
- "Write to `public.contact_listings` directly because RLS is disabled and it works" — No (and as of 2026-05-29 RLS is **enabled** service-role-only, so direct anon access fails anyway). [CDL access gate](wiki/architecture.md#compliance-gates) forbids it. Use `cdl-write` with `resource: 'contact_listings'`.
- "Pick a more convenient column name like `dealValue` for offer amount" — No. Always RESO snake_case (`offer_amount`).
- "Use `mls-sync` from the broker UI to upsert a showing" — No. `mls-sync` is `system_admin`/`org_admin` scope only; broker calls get 403.

## Cross-references

- [`wiki/architecture.md#cdl-access-pattern`](wiki/architecture.md#cdl-access-pattern) — the Pipeline-specific instantiation of the general CRM-as-CDL-client pattern.
- [`wiki/integration.md#cdl`](wiki/integration.md#cdl) — outer integration view.
- [`../../data-models/cdl-schema.md`](../../data-models/cdl-schema.md) — full CDL schema (subject to drift; see coverage doc).
- [`../../architecture/decisions/ADR-012.md`](../../architecture/decisions/ADR-012.md) — Third-Party Auth contract.
- [`../../architecture/decisions/ADR-015.md`](../../architecture/decisions/ADR-015.md) — the platform-team decision request bundling the six EFs/decisions Pipeline needs.
