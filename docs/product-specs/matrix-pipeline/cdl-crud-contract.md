---
title: Lovable CDL CRUD contract
status: draft
source: mem://infrastructure/lovable-cdl-crud-contract.md (iteration copy)
last_synced: 2026-05-28
last_updated: 2026-05-28
tags: [infrastructure, lovable, crud, cdl, contract]
---

# Lovable CDL CRUD contract — Matrix Pipeline

> **For Lovable**: Read this before generating ANY code that touches the CDL Supabase project (`ofzcokolkeejgqfjaszq`). The companion reachability matrix lives in the iteration copy at `mem://infrastructure/cdl-coverage.md` (Pipeline-team operational doc). This doc tells you HOW to write code; the coverage doc tells you WHAT is reachable.
>
> The CRM app DB is the default write target for everything except the three resources that already have a live CDL home (`members`/`offices` are read-only consumer paths anyway; `showings` is read-only from Pipeline today).
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
- **Never** read an **RLS-disabled** table directly (e.g. `contact_listings` today) — Supabase warns such tables are "accessible to the public using the anon role"; that is a CDL access-gate violation. Use the EF. And **never** use the CDL service-role key in app code.

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

### Recipe READ-C — per-resource Pipeline EF (planned, not yet built) {#read-c}

For resources that direct PostgREST cannot reach safely:
- `contacts` (PII, service-role-only RLS) → `cdl-contacts-read`
- `contact_listings`, `contact_listing_notes` (RLS disabled, gate violation if read directly) → `cdl-contact-listings-read`

```typescript
const { data, error } = await cdlClient.functions.invoke('cdl-contacts-read', {
  body: {
    filter: { owner_member_key: currentMemberKey, contact_type: 'Lead' },
    page: 0, pageSize: 25,
  },
});
if (error?.message === 'EF_NOT_AVAILABLE') {
  return { data: [], total: 0, pending: true };
}
```

**Today these EFs return `501 EF_NOT_AVAILABLE`**. Lovable generates the hook with the correct invoke shape so day-one wiring is right; the UI shows a pending banner until the platform team ships the EF (see [`../../architecture/decisions/ADR-015.md`](../../architecture/decisions/ADR-015.md)).

### Recipe WRITE-A — `appClient.from(...).insert(...)` on the CRM app DB {#write-a}

Default write path for every Pipeline-owned resource today:

- Already app-private forever: `Activity`, `Document`, `Campaign`, `Referral`.
- App-private until CDL migration (Phase 2+): `SavedSearch`, `Prospecting`, `ShowingAvailability`, `ShowingRequest`, `Showing` (recorded fact), `LockOrBox`, `Caravan`, `CaravanStop`, `TransactionManagement`, plus the queue tables `history_pending`, `showing_drafts`, `contacts_pending`.

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

### Recipe WRITE-B — per-resource Pipeline EF (planned, not yet built) {#write-b}

For canonical resources that have a CDL table today but cannot be written from a broker scope:

| Resource | Planned EF | Today |
|---|---|---|
| `contacts` | `cdl-contacts-write` | queue in `contacts_pending` (app DB) |
| `contact_listings` / `contact_listing_notes` | `cdl-contact-listings-write` | queue in `contact_listings_pending` (app DB) |
| `showings` (ShowingAppointment) | `cdl-showings-write` | queue in `showing_drafts` (app DB) |
| `history_transactional` | `cdl-history-emit` | queue in `history_pending` (app DB) — **critical, every state transition emits** |
| `transaction_management` (Phase 4) | `cdl-tm-write` | write to app DB `transaction_management` (already in WRITE-A) |

```typescript
async function emitHistory(row: HistoryTransactionalRow) {
  const { error } = await cdlClient.functions.invoke('cdl-history-emit', { body: row });
  if (error?.message === 'EF_NOT_AVAILABLE') {
    await appClient.from('history_pending').insert({
      payload: row,
      created_at: new Date().toISOString(),
    });
    return { queued: true };
  }
  if (error) throw error;
  return { queued: false };
}
```

The reconciler (Phase 7 task in [`phases.md`](phases.md)) drains `*_pending` tables into CDL when the EFs ship. The queue rows store the full RESO record so no information is lost in transit.

## The six commandments {#commandments}

A short checklist Lovable applies at the top of every relevant prompt:

1. **Two databases, never three.** SSO (`ssoClient`), CDL (`cdlClient`), App DB (`appClient`). Never a fourth Supabase. Never the CDL service-role key in app code.
2. **RESO names only.** Tables in the CRM app DB use canonical PascalCase → snake_case. Never `customerId`, `dealAmount`, `leadStage` — always `contact_key`, `offer_amount`, `contact_type`. FK columns to CDL canonical resources are `text` typed using the RESO `*Key` field, not `uuid`.
3. **Reads go through Recipe READ-A / READ-B / READ-C in that order.** Use direct PostgREST only on tables listed in the coverage matrix as "direct anon `select` ✓". Use `listings-search` for everything property-shaped that needs filters or pagination. Use the placeholder Pipeline EFs (READ-C) for `contacts`, `contact_listings`, `contact_listing_notes`.
4. **Writes default to the CRM app DB (WRITE-A).** Use WRITE-B only when the resource is canonical RESO + lives in CDL today + has a Pipeline-scoped write EF. **Today zero WRITE-B EFs exist** → every Pipeline write today is WRITE-A.
5. **Every state transition emits a `HistoryTransactional`.** Until `cdl-history-emit` ships, queue the emission in `history_pending`. Never write `public.history_transactional` directly from anon (RLS blocks it) and never write to RLS-disabled tables to bypass the gate.
6. **No SSO ↔ CDL SQL joins.** Display names always go through `resolve-users` EF + `useUserDisplay` hook. Member roster lookups go through `cdlClient.from('members')`. Never `select … join sso_users …` anywhere.

## Quick reference — which recipe for which resource? {#quick-reference}

| Resource | Read | Write |
|---|---|---|
| `Property` (`properties_published`) | READ-A or READ-B | n/a (Atlas-owned) |
| `Property` (raw `properties`) | use READ-B only | n/a |
| `Media` | use READ-B `includeMedia: true` | n/a |
| `PropertyRooms` / `PropertyUnitTypes` | READ-A | n/a |
| `Member` | READ-A | n/a (read-only consumer) |
| `Office` | READ-A | n/a |
| `Contacts` | READ-C (`cdl-contacts-read`, placeholder) | WRITE-B `cdl-contacts-write` (placeholder → queue) |
| `ContactListings` | READ-C (`cdl-contact-listings-read`, placeholder) | WRITE-B (placeholder → queue) |
| `ContactListingNotes` | READ-C | WRITE-B (placeholder → queue) |
| `ShowingAppointment` (`showings`) | READ-A | WRITE-B `cdl-showings-write` (placeholder → `showing_drafts`) |
| `SavedSearch` | n/a (CRM app DB) | WRITE-A |
| `Prospecting` | n/a (CRM app DB) | WRITE-A |
| `ShowingAvailability` / `ShowingRequest` / `Showing` (recorded) / `LockOrBox` / `Caravan` / `CaravanStop` | n/a (CRM app DB) | WRITE-A |
| `TransactionManagement` | n/a (CRM app DB until Phase-4 CDL migration) | WRITE-A |
| `HistoryTransactional` | READ-A | WRITE-B `cdl-history-emit` (placeholder → `history_pending`) |
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
- "Write to `public.contact_listings` directly because RLS is disabled and it works" — No. [CDL access gate](wiki/architecture.md#compliance-gates) forbids it. Use the `cdl-contact-listings-write` EF (placeholder → queue).
- "Pick a more convenient column name like `dealValue` for offer amount" — No. Always RESO snake_case (`offer_amount`).
- "Use `mls-sync` from the broker UI to upsert a showing" — No. `mls-sync` is `system_admin`/`org_admin` scope only; broker calls get 403.

## Cross-references

- [`wiki/architecture.md#cdl-access-pattern`](wiki/architecture.md#cdl-access-pattern) — the Pipeline-specific instantiation of the general CRM-as-CDL-client pattern.
- [`wiki/integration.md#cdl`](wiki/integration.md#cdl) — outer integration view.
- [`../../data-models/cdl-schema.md`](../../data-models/cdl-schema.md) — full CDL schema (subject to drift; see coverage doc).
- [`../../architecture/decisions/ADR-012.md`](../../architecture/decisions/ADR-012.md) — Third-Party Auth contract.
- [`../../architecture/decisions/ADR-015.md`](../../architecture/decisions/ADR-015.md) — the platform-team decision request bundling the six EFs/decisions Pipeline needs.
