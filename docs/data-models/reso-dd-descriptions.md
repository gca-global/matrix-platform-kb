# RESO DD descriptions corpus (`reso_field_descriptions` + tenant overrides)

**Project**: Matrix CDL (`ofzcokolkeejgqfjaszq`) — owned by `matrix-platform-foundation/supabase/cdl/`. **Not** SSO.
**Served by**: the public `reso-dd-descriptions` Edge Function (read) + the `mls-sync` resource `reso_label_override` (write).
**Consumed by**: `<ResoFieldLabel>` / `<ResoLookupValue>` (RESO keys) and `Term`/`useTerm` (curated `App.*` UI nouns) in CDL-connected apps (matrix-pipeline-2-0 today).
**Related**: [ADR-020](../architecture/decisions/ADR-020.md), [reso-dd-overview.md](reso-dd-overview.md), [reso-canonical-schema.md](reso-canonical-schema.md), the FE→CDL contract `matrix-pipeline-2-0/docs/cdl-ef-contracts/reso-label-overrides.md`.

## Purpose

A single CDL store that serves three purposes at once:

1. the **official RESO DD 2.0 corpus** — `DisplayName` + verbatim `Definition`
   for every Resource / Field, plus lookup-value `DisplayValue` / `Definition`;
2. **additional UI translations** (locale rows beyond `en`);
3. **per-tenant terminology/label overrides** edited by tenant admins at runtime.

The corpus `DisplayName` is the canonical default label the FE prefers over any
static fallback. Renaming/translating a label never touches the data model, EF
`resource` names, `pageKey`/route identifiers, or the canonical corpus keys.

## Tables & keys

| Table | Key shape | Notes |
|---|---|---|
| `public.reso_field_descriptions` | PK `(field, locale, tenant_key)` | `field` is the corpus key; `display_name`, `description`, `wiki_url`, `lookups_url`, `dd_version`, `source`. |
| `public.reso_lookup_value_descriptions` | PK `(lookup_name, standard_value, locale, tenant_key)` | per-lookup-value `display_value` + `definition`. |

- `tenant_key text NOT NULL DEFAULT ''`. **`''` = global RESO truth**; a non-empty
  value scopes the row to one tenant. Partial index covers `WHERE tenant_key <> ''`.
- `source ∈ { 'reso_official_csv', 'team_override', 'atlas_custom', 'vendor_extension' }`.
  Tenant overrides are always `source='team_override'`.

### Corpus key namespaces

| Prefix | Meaning | Example | `source` (global seed) |
|---|---|---|---|
| `Resource.<X>` | a RESO Resource label | `Resource.Property` | `reso_official_csv` |
| `<Resource>.<Field>` | a RESO Field label | `Property.ListingAgreement` | `reso_official_csv` |
| `Lookup.<X>` | a RESO lookup category label | `Lookup.ContactType` | `reso_official_csv` |
| `App.<Term>` | a curated UI noun with **no** RESO resource | `App.Pipeline`, `App.Transaction`, `App.Settings`, `App.SectionSales` | `vendor_extension` |

The `App.*` namespace covers app-level nouns (sidebar items, section headings,
page titles) that the platform UI labels but RESO does not model. They are seeded
globally for `en` + `ru` + `hu` and are re-labelable per tenant like any other key.

## Read merge (`reso-dd-descriptions` EF)

Request: `GET ?locale=<lng>&v=<corpus-version>[&tenant=<tenant_key>]`.

Resolution is a three-layer overlay per `(field, locale)`:

1. **global `en`** baseline (always),
2. **global `<locale>`** overlay (the requested locale's official/translated row),
3. **tenant `<locale>`** overlay (`tenant_key=<tenant>`), if `tenant` is supplied.

Empty override strings are treated as "no override" and fall back to the layer
below, so a tenant can override `display_name` without wiping `description`, and
a missing `hu` row falls back to `en`. Lookup values merge by `standard_value`.

**Caching**: global responses (no `tenant`) are CDN-cacheable
(`public, s-maxage`); tenant responses are `private, no-store` so a relabel is
visible immediately. The FE keys React Query on `(locale, tenant, corpus
version)` and bumps `RESO_DD_CORPUS_VERSION` whenever a migration adds global
rows.

## Write (`mls-sync` resource `reso_label_override`)

Admin-gated by the **SSO scope claim** (`global` / `org_admin` / `system_admin`),
re-checked inside the CDL EF (`verify_jwt:false` + ES256/JWKS). Actions:

- `list-resource` — global value + this tenant's override, side by side, with
  `locale` / `category` (`app|resource|lookup|field|all`) / `q` / pagination.
- `upsert-resource` — single-locale (`locale` + `display_name`/`description`) or
  **multi-locale** (`locales: { en, ru, hu }`). Empty `display_name`+`description`
  for a locale clears that locale's override. `Lookup.*` keys may carry
  `lookup_values[]`.
- `delete-resource` — reset a field's overrides (one or all locales).

The EF force-injects `tenant_key = caller.tenantId` + `source='team_override'`,
rejects keys/values not present in the global corpus, and emits a
`HistoryTransactional` row (`ResourceName=ResoLabelOverride`, `ChangeType ∈
{Created, Updated, Deleted}`) — see
[wiki/integration.md#history-emission](../product-specs/matrix-pipeline/wiki/integration.md#history-emission).

## FE resolution chain (unchanged shape)

`<ResoFieldLabel>`: `children` → i18n `reso.fields.*` → corpus `displayName` →
static `RESO_DISPLAY_NAMES` → raw key. `Term`/`useTerm`: corpus `displayName` for
the `App.*` / `Resource.*` key → i18n `term.*` fallback → raw key. Tenant
overrides win because the EF merges them in before the FE sees the map; saving an
override invalidates `['reso-dd-descriptions', …]` so labels flip live.
