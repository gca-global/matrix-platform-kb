# Golden Principles — Engineering Invariants

> Opinionated, mechanical rules that keep the codebase legible, consistent, and
> correct for both human and agent contributors. Violating any of these causes
> silent failures, architectural drift, or data leaks.
>
> Each principle follows the format: **Rule** / **Why it fails if violated** /
> **Enforcement mechanism**.
>
> This is the "taste document" — entropy management starts here.

---

## Agent-First Operating Principles

These define how AI agents should work within the Sharp Matrix ecosystem.

### P1. Repository knowledge is the system of record

**Rule**: If it's not in `docs/`, it doesn't exist for agents. Slack threads,
email decisions, and meeting notes must be captured in the repo to be actionable.

**Why it fails**: Agents cannot access external context. Decisions that live
outside the repo are invisible and will be contradicted or duplicated.

**Enforcement**: Doc-gardening reviews (see [kb-methodology.md](platform/kb-methodology.md)).
The `validate-kb.sh` script flags docs that haven't been updated in 90+ days.

### P2. Progressive disclosure — start small, drill down

**Rule**: Agents start with `AGENTS.md` (the map), then navigate to
`INDEX.md` → chapter index → specific doc. Never front-load an agent with the
entire KB.

**Why it fails**: Context is a scarce resource. A giant instruction dump crowds
out the task and the code. Agents pattern-match locally instead of navigating
intentionally.

**Enforcement**: `AGENTS.md` stays under ~200 lines. New docs are registered
in the tree and task-nav table, not inlined.

### P3. RESO DD is canonical for CDL-Connected apps

**Rule**: Always use RESO standard field names when building any CDL-Connected
app. Check `docs/data-models/` before writing code that touches shared data.

**Why it fails**: Inconsistent field names between apps break joins, reports,
and syndication. One field, one canonical name everywhere.

**Enforcement**: Data contracts ([data-contracts.md](data-models/data-contracts.md)).
CDL schema diff on migration PRs (planned).

### P4. Business processes define behavior

**Rule**: Pipeline stages, qualification rules, and metrics are requirements,
not suggestions. Code must match the process docs in `docs/business-processes/`.

**Why it fails**: Agents may invent plausible but incorrect business logic.
The pipeline docs are the tiebreaker.

**Enforcement**: Manual review. Business process docs are owned by CDSO
(see `CODEOWNERS`).

### P5. Vision documents define intent

**Rule**: When ambiguity arises, the digital strategy 2026-2028 and the
AI-driven sales model are the tiebreakers for product direction.

**Why it fails**: Without a north star, agents optimize locally and produce
features that contradict strategic priorities.

**Enforcement**: Vision docs are co-owned by CDSO + CDTO (`CODEOWNERS`).

### P6. Platform consistency across all apps

**Rule**: Every Matrix App uses the same field names, data types, lookup values,
auth model, and UI framework. No per-app forks of shared patterns.

**Why it fails**: Divergence creates translation layers, auth bugs, and
user-facing inconsistency across apps.

**Enforcement**: `matrix-apps-template` is the starter kit. ADRs document
decisions. Code review (agent or human) checks compliance.

---

## Token & Auth Invariants

Hard-learned lessons about the dual-Supabase token architecture. These cause
the most common silent failures.

### T1. Send the SSO JWT to CDL PostgREST (Third-Party Auth)

**Rule**: Send the SSO-issued ES256 JWT as `Authorization: Bearer …` to
CDL PostgREST. Do not juggle "Supabase native tokens" or
`localStorage.getItem('matrix_supabase_access_token')`.

**Why it works**: CDL is configured with Supabase **Third-Party Auth**
pointing at the SSO JWKS URL + issuer. PostgREST verifies the SSO token
directly. This supersedes the earlier two-token dance. See
[ADR-012](architecture/decisions/ADR-012.md).

**Enforcement**: `buildCdlClient()` in `dataLayerClient.ts` forwards the
SSO access token. Do not re-introduce native-token plumbing.

### T2. CDL RLS helpers are JWT-only (no `app_metadata` fallback)

**Rule**: CDL RLS helper functions (`public.get_active_scope`,
`public.get_crud`, `public.get_current_tenant_id`,
`public.get_current_team_ids`, …) read claims exclusively from
`auth.jwt()`. They must not depend on `auth.users.raw_app_meta_data`,
and must not use `current_setting('request.jwt.*')`.

**Why it fails (if violated)**: CDL is being designed for portability to
Databricks Lakebase. Supabase-specific GUCs and Supabase-only
`auth.users.raw_app_meta_data` columns do not exist on Lakebase. JWT-only
helpers keep the policies intact during that migration.

**Enforcement**: JWT-only RLS helpers live alongside the CDL
migrations in `matrix-platform-foundation/supabase/cdl/migrations/`.
Any CDL migration introducing a Supabase-specific helper must justify
it in ADR-form.

### T3. `oauth-token` MUST include scope / crud / team_ids in the JWT payload

**Rule**: The `oauth-token` Edge Function must embed the resolved
`scope`, `crud`, `team_ids`, `uoi` (tenant), and `active_app` claims
into the JWT payload it issues.

**Why it fails**: CDL RLS helpers read these from `auth.jwt()` directly
(T2). Missing claims → policies default to `'self'` / no CRUD → empty
query results.

**Enforcement**: Edge Function tests in `matrix-platform-foundation`.
`auth.users.raw_app_meta_data` may still be populated for convenience
on the SSO project, but it is no longer the fallback path for CDL RLS.

### T4. CDL writes go through Edge Functions on the CDL project

**Rule**: Browser code must not call CDL PostgREST directly for writes,
and apps must never hold a CDL service-role key. Route writes through
the EFs deployed on the CDL project itself (`ofzcokolkeejgqfjaszq`).
Today that means:

- **Ingestion / MLS Sync admin** → `mls-sync` or `mls-sync-orchestrator` EF (action surface: `start`, `cancel`, `save-settings`, …).
- **Programmatic listing reads (filtered)** → `listings-search` EF.
- **Anon listing reads (public snapshot)** → direct PostgREST against `public.properties_published` with the CDL anon key (RLS gates `is_visible AND NOT is_deleted`).

If a future app needs a generic CRUD proxy, add a new dedicated EF on
the CDL project (the previously-planned `cdl-write` proxy was never
built; ingestion-only flows did not need it).

**Why it fails**: CORS blocks cross-origin browser writes; service-role
distribution across Lovable apps is a credential-leak vector.

**Enforcement**: All CDL EFs live under
`matrix-platform-foundation/supabase/cdl/functions/` and run with
`verify_jwt = false`, performing custom SSO-JWT verification + scope
checks themselves.

---

## Scope & Permission Invariants

### S1. Don't conflate scope with admin privileges

**Rule**: `global` scope = data visibility (see all records in tenant).
`org_admin` / `system_admin` = administrative control. Admin operations
(permissions, tenant config, system settings) require `org_admin` or
`system_admin`, never just `global`.

**Why it fails**: A Sales Director with `global` scope should NOT be able to
modify checklist templates, manage roles, or administer tenants.

**Enforcement**: RLS policies on config tables use
`(SELECT get_active_scope()) IN ('org_admin', 'system_admin')`. Frontend
gates admin UI behind `isAdmin` (which excludes `global`).

| Scope | Data Access | Admin Functions |
|-------|-------------|-----------------|
| `self` | Own records | None |
| `team` | Team + own | None |
| `global` | All records in tenant | **None** |
| `org_admin` | All records + admin | **Yes** |
| `system_admin` | Cross-tenant + admin | **Yes** |

**Ref**: [app-template.md § Pitfall 5](platform/app-template.md#5-dont-conflate-scope-with-admin-privileges),
[security-model.md](platform/security-model.md)

### S2. Use `get_my_tenant_id()` on CDL, not `get_current_tenant_id()`

**Rule**: CDL RLS must use `get_my_tenant_id()` which has a 4-step fallback:
`uoi` → `user_metadata.tenant_id` → `auth.users` → `admin_settings`.

**Why it fails**: `get_current_tenant_id()` only reads the JWT `uoi` claim.
Legacy apps and some token types lack this claim → tenant isolation breaks.

**Enforcement**: RLS migration template.

**Ref**: [app-template.md § Pitfall 6](platform/app-template.md#6-use-get_my_tenant_id-not-get_current_tenant_id-on-cdl)

---

## Client Usage Invariants

### C1. Use the correct Supabase client for each table

**Rule**: Not all tables are accessible with all client types. The SSO JWT is
not recognized by CDL PostgREST (causes `PGRST301`), so tables with
auth-dependent RLS need the authenticated client while tables with anon policies
can use the anon client.

| Table | Client | Reason |
|-------|--------|--------|
| `sso_tenants` | `createAnonDataLayerClient()` | Has anon SELECT policy for active tenants |
| `sso_roles` | `createDataLayerClient()` | RLS requires `authenticated` role |
| `sso_role_configurations` | `createDataLayerClient()` | RLS requires auth for SELECT |
| `app_settings` | `createAnonDataLayerClient()` | Has anon SELECT policy |
| App-specific tables | `supabase` (app client) | App DB with RLS via SSO JWT or native token |

**Why it fails**: Using the wrong client causes `PGRST301` errors or empty
results depending on the RLS policy.

**Enforcement**: Code review. Documented per-table in Lovable prompts.

---

## Lovable App Maintenance Invariants

### L1. Changes to Lovable-managed apps go through prompts

**Rule**: All Matrix business apps are built and maintained in Lovable. Changes
are made via structured markdown prompts, not direct code edits.

**Why it fails**: Direct edits to Lovable-managed code will be overwritten on
the next Lovable publish. Prompts create a versioned audit trail.

**Enforcement**: Prompts stored in project prompt archives
(e.g., `matrix-testing-suite/hrms-uat/prompts/`).

**Ref**: [operations.md § Lovable App Maintenance](platform/operations.md),
[app-template.md § Lovable-Managed Apps](platform/app-template.md)

### L2. Direct edits are reserved for infrastructure

**Rule**: Only SSO/CDL Edge Functions, database migrations, RLS policies, and
infrastructure config are edited directly. Everything else goes through Lovable.

**Why it fails**: Mixing direct edits with Lovable-managed code creates merge
conflicts and makes the Lovable history unreliable.

**Enforcement**: Repository ownership (Edge Functions in `matrix-platform-foundation`,
apps in Lovable).

### P7. SSO and CDL are separate Supabase projects, both owned by `matrix-platform-foundation`

**Rule**: The SSO project (`xgubaguglsnokjyudgvc`) and the CDL project
(`ofzcokolkeejgqfjaszq`) are the two highest-blast-radius Supabase
projects in the platform. Both are managed **exclusively** via
`matrix-platform-foundation` (`supabase/sso/` for SSO,
`supabase/cdl/` for CDL — sibling workspaces in one repo). Neither is
linked to Lovable. No Matrix app may own CDL schema.

**Why it fails**: Allowing a Lovable-linked app (including
`matrix-cdl-studio`) to own CDL schema caused unpredictable drift that
cascaded across every app reading shared data. Co-locating MLS tables
with SSO auth created a shared-outage risk for identity and business data.

**Enforcement**: Lovable is not linked to these projects. Schema
changes must land as PRs against `matrix-platform-foundation` and be
pushed via `supabase db push --project-ref …` by the platform team.
See ADR-012 and ADR-013. `matrix-cdl-studio` is retired as a write
surface (see its `RETIREMENT.md`).

### P8. CDL is JWT-only and Lakebase-portable

**Rule**: CDL RLS helpers and migrations must not depend on
Supabase-native constructs in `public` (no FKs to `auth.users`, no
`current_setting('request.jwt.*')` required). All context comes from
`auth.jwt()`. Supabase-only needs live in the quarantined `_infra`
schema.

**Why it fails**: We expect to migrate CDL to Databricks Lakebase
within 12–18 months. Each Supabase-specific touch in the shared
schema becomes an unplanned rewrite. Cross-project joins to SSO users
are also impossible once CDL moves off Supabase — apps must not
assume they exist.

**Enforcement**: CDL migrations land through
`matrix-platform-foundation/supabase/cdl/`. User display name
lookups go through `resolve-users` (SSO EF) + `useUserDisplay` React
hook, never SQL joins. See ADR-012 and
[cdl-schema.md](data-models/cdl-schema.md).

### P9. Ingestion always flows: source → staging → merge → published

**Rule**: All MLS data ingestion (RESO endpoints, `mls_2_0` RESO API)
must go through the unified pipeline on the CDL project:
`reso-import` → `cdl_staging.listings_raw` → `field-mapping-apply` →
`cdl_staging.listings_mapped` → `listing-merge` → `public.properties`
→ `media-import` → `public.property_media` → `listing-publish` →
`public.properties_published`. Per-source identity is tracked by the
`(source_id, source_listing_key)` natural key plus per-row
`content_hash` for dedup. Every stage writes one row to
`public.ingest_audit`, and orchestrator runs additionally record
per-stage state in `public.mls_orchestrator_runs`.

**Why it fails**: Bespoke ingestion EFs drift in error handling,
dedup, and audit. Skipping staging makes manual review impossible.
Skipping the natural key collides external records on retries.
Skipping the audit log destroys regulatory traceability.

**Enforcement**: ADR-014 (with the 2026-04-26 implementation status
note). The ingestion EFs on the CDL project are the 5 pipeline stages
above plus the two admin/orchestration EFs (`mls-sync` lifted
monolith, `mls-sync-orchestrator` chaining the 5 stages). New tenants
are onboarded by adding a row in `public.mls_settings` (per-tenant
RESO creds + `source_id`) and field mappings in
`public.field_mappings` — never by writing a bespoke EF. CSV / CRM
ingestion is on the roadmap; when added it should write to
`cdl_staging.listings_raw` so the rest of the pipeline is reused.

---

## Cross-Reference

| For | See |
|-----|-----|
| Quality grades by domain | [QUALITY_SCORE.md](QUALITY_SCORE.md) |
| Technical debt tracker | [exec-plans/tech-debt-tracker.md](exec-plans/tech-debt-tracker.md) |
| Security model details | [platform/security-model.md](platform/security-model.md) |
| App template & pitfalls | [platform/app-template.md](platform/app-template.md) |
| Core beliefs (business) | [vision/core-beliefs.md](vision/core-beliefs.md) |
| KB methodology | [platform/kb-methodology.md](platform/kb-methodology.md) |
