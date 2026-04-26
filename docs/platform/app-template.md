# Matrix App Template — How to Build Sharp Matrix Apps

> Source: `/home/bitnami/matrix-apps-template` (starter kit)
> Examples:
> - `/home/bitnami/matrix-hrms` — Domain-Specific app (HR, 25+ tables)
> - `/home/bitnami/matrix-pipeline` — CDL-Connected app (CRM, leads, pipeline)
> - `/home/bitnami/itsm-2-1` — Domain-Specific app (IT service desk, CMDB)
> - `/home/bitnami/matrix-fm` — Domain-Specific app (financial reporting, budgeting)
>
> **For Lovable**: Read this document before building ANY Matrix App. It defines the
> exact patterns, conventions, and architecture you must follow.

## Two Types of Matrix Apps

Before building, determine which type of app you're creating:

| Type | CDL Usage | App DB Usage | Example |
|------|-----------|-------------|---------|
| **CDL-Connected** | Reads/writes shared RESO tables (Property, Member, Contacts) | May have some app-specific tables | Matrix Pipeline (`/home/bitnami/matrix-pipeline`), Broker App, Manager App |
| **Domain-Specific** | Only uses CDL for auth/permissions/tenants | Has its own Supabase instance with domain tables | HRMS (`/home/bitnami/matrix-hrms`), Matrix FM (`/home/bitnami/matrix-fm`), ITSM (`/home/bitnami/itsm-2-1`) |

**Decision rule**: If your app works with real estate listings, contacts, agents, or showings → CDL-Connected. If your app has its own domain (HR, finance, operations) → Domain-Specific.

**What stays the same in BOTH types:**
- Dual-Supabase architecture (SSO instance + App DB instance)
- SSO auth (OAuth 2.0 + PKCE + JWT)
- Permission model (5-level scope + CRUD + page/action access)
- RLS patterns (A-E)
- UI framework (shadcn/ui + Tailwind + Sharp design system)
- Data fetching (Supabase client + React Query)
- Routing (React Router v6 + ProtectedRoute)
- i18n (i18next EN/RU)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Vite + React 18 + TypeScript |
| UI | shadcn/ui (60+ Radix components) + Tailwind CSS |
| Design | Sharp design system: Navy palette, Playfair Display (headings) + Inter (body) |
| Data | `@supabase/supabase-js` v2 + TanStack Query (React Query) |
| Auth | Custom SSO (OAuth 2.0 + PKCE) via Supabase Edge Functions, ES256 JWT signing ([ADR-011](../architecture/decisions/ADR-011.md)) |
| i18n | i18next (EN/RU) |
| Routing | React Router v6 with `ProtectedRoute` guards |

## Dual-Supabase Architecture

Every Matrix App connects to **two Supabase instances**:

> **Updated Apr 2026 (ADR-012 / ADR-013):** SSO and CDL are now **two
> separate Supabase projects**, both owned by
> `matrix-platform-foundation`. Client code splits into `ssoClient`
> and `cdlClient` (exported from the same `dataLayerClient.ts` for
> migration ergonomics, but pointing at different projects).

| Instance | Project ID | Client Export | Purpose |
|----------|-----------|---------------|---------|
| **SSO** | `xgubaguglsnokjyudgvc` | `ssoClient` from `dataLayerClient.ts` | Authentication, roles, permissions, tenants, SSO admin EFs |
| **CDL** | `ofzcokolkeejgqfjaszq` | `cdlClient` from `dataLayerClient.ts` | Shared `mls_*` business data, ingestion control plane |
| **App Database** | Per-app (e.g., HRMS: `wltuhltnwhudgkkdsvsr`) | `supabase` from `client.ts` | App-specific business data with RLS |

### SSO Instance Tables

| Table | Purpose |
|-------|---------|
| `ad_users` | Azure AD user directory cache |
| `tenants` | Organization/tenant records |
| `app_settings` | Per-tenant app configuration (JSON) |
| `sso_user_groups` | Team/group memberships |
| `sso_role_configurations` | Per-role page and action access lists |

### App DB Client Setup

The app database client injects the SSO JWT for RLS:

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  global: {
    headers: { 'x-sso-email': userEmail },
  },
  accessToken: async () => ssoAccessToken,
});
```

The `accessToken` hook injects the SSO JWT into every request. RLS policies read claims from `current_setting('request.jwt.claims')`.

### CDL Client Setup (for CDL-Connected Apps)

CDL-Connected apps read the shared CDL tables through the `cdlClient`
exported from `dataLayerClient.ts`. The CDL project is configured with
**Supabase Third-Party Auth** pointing at the SSO JWKS URL + issuer,
so PostgREST verifies SSO-issued ES256 tokens directly. Apps forward
the SSO access token as the bearer — no Supabase-native token juggling.

```typescript
// dataLayerClient.ts — split SSO and CDL clients
export const SSO_SUPABASE_URL = 'https://xgubaguglsnokjyudgvc.supabase.co';
export const CDL_SUPABASE_URL = 'https://ofzcokolkeejgqfjaszq.supabase.co';

export function buildSsoClient() { /* …SSO anon key… */ }
export function buildCdlClient() { /* …CDL anon key… */ }

export const ssoClient = buildSsoClient();
export const cdlClient = buildCdlClient();
```

**How RLS claims reach CDL PostgREST**: the CDL RLS helpers
(`public.get_active_scope`, `public.get_crud`,
`public.get_current_tenant_id`, …) read claims directly from
`auth.jwt()`. There is no `app_metadata` fallback on the CDL project
— the helpers are JWT-only so the policies remain portable to
Databricks Lakebase. See [security-model.md](security-model.md) and
ADR-012.

### Resolving user display names across projects

Because `mls_*` rows live on a different Supabase project than
`auth.users`, apps must NOT try to SQL-join listings to SSO users.
Use the `useUserDisplay` React hook (from `matrix-apps-template`),
which batches IDs and calls the `resolve-users` SSO Edge Function.

### CDL Read & Write Patterns (current)

CDL-Connected apps reach the CDL project (`ofzcokolkeejgqfjaszq`) via
EFs deployed on that project, never via direct PostgREST writes:

```
App UI → cdlClient.functions.invoke('listings-search', body)            ← filtered listing reads
App UI → cdlAnonClient.from('properties_published').select(...)         ← simple anon snapshot reads (RLS gated)
App UI → cdlClient.functions.invoke('mls-sync' | 'mls-sync-orchestrator', { action, ... })
                                                                         ← MLS Sync admin (start/cancel/save-settings/...)
```

Each CDL EF runs with `verify_jwt = false` and verifies the SSO JWT
itself (HS256 / JWKS fallback) and checks `scope` ∈
`SSO_ALLOWED_SCOPES`. The previously-planned generic `cdl-write` proxy
was never built; if a future app needs generic CRUD, add a dedicated
EF to `matrix-platform-foundation/supabase/cdl/functions/`.

## SSO Auth Flow

1. App redirects to `https://intranet.sharpsir.group/sso-login/` with PKCE code challenge
2. User authenticates via Azure AD
3. Callback at `/auth/callback` exchanges authorization code for JWT via `oauth-token` Edge Function
4. Tokens stored in `localStorage`:
   - `matrix_sso_access_token` — SSO JWT (custom claims: scope, crud, team_ids, uoi)
   - `matrix_sso_refresh_token` — for token renewal
   - `matrix_supabase_access_token` — Supabase native token (for CDL PostgREST calls)
5. `oauth-token` also persists `active_scope`, `active_crud`, `active_team_ids` to user's `app_metadata` (enables RLS for native token)
6. SSO JWT injected into App DB client via `accessToken` hook; native token used for CDL client
7. Proactive token refresh at 80% of expiry time (also refreshes `app_metadata`)

### JWT Claims Structure

```typescript
{
  sub: string;                     // User UUID (permanent ID across all apps)
  email: string;                   // User email
  sso_role: { id: string; name: string };   // Active role (object, not string)
  scope: { id: string; name: string };      // Access scope (object, not string)
  crud: string;                    // "crud" | "cr" | "r" | "ru" | etc. (c/r/u/d letters)
  uoi: string;                     // Tenant UUID (organization ID)
  teams: Array<{ id: string; name: string }>;  // Team memberships
  team_ids: string[];              // Team UUIDs (flat array for RLS)
  allowed_apps: Array<{ id: string; name: string }>;  // Apps user can access
}
```

> See [security-model.md](security-model.md) for the full JWT claims structure with all fields.

### JWT Signing Algorithm

SSO JWTs are signed with **ES256 (ECDSA P-256)** — Supabase's default asymmetric algorithm. During migration, apps with their own Supabase project may receive **HS256** tokens signed with an app-specific secret. See [ADR-011](../architecture/decisions/ADR-011.md) for the full migration plan and [security-model.md](security-model.md#jwt-signing--es256-target--hs256-legacy) for implementation details.

**For app developers**: The signing algorithm is transparent. The Supabase JS client passes the token string; PostgREST validates it against registered keys. No app code changes are needed.

### SSO Edge Functions Called

| Function | When Called |
|----------|-----------|
| `oauth-authorize` | Initiating login redirect |
| `oauth-token` | Exchanging auth code for JWT (signs ES256 or HS256 per app config) |
| `oauth-userinfo` | Fetching user info with claims |
| `switch-role` | User switches active role → re-issues JWT (signs ES256 or HS256 per app config) |
| `switch-tenant` | System admin switches active tenant → re-issues JWT with new org context |
| `admin-ad-users` | Querying Azure AD user directory |

### Lovable Environment Detection

```typescript
function isLovableEnvironment(): boolean {
  const host = window.location.hostname;
  return host.includes('lovable.dev')
      || host.includes('lovable.app')
      || host.includes('lovableproject.com');
}
```

In Lovable dev mode: uses in-app login (bypasses external SSO redirect).
In production: redirects to external SSO login page.

## Permission Model

### 5-Level Scope Hierarchy

```
self → team → global → org_admin → system_admin
```

| Scope | Sees |
|-------|------|
| `self` | Own records only |
| `team` | Own records + team members' records |
| `global` | All records in tenant |
| `org_admin` | Full tenant access + admin functions |
| `system_admin` | Cross-tenant access + tenant switching via `switch-tenant` |

### CRUD Permission String

Format: any combination of `c`, `r`, `u`, `d`.

| Value | Meaning |
|-------|---------|
| `r` | Read only |
| `cr` | Create + Read |
| `crud` | Full access |
| `ru` | Read + Update (no create, no delete) |

### Auth Hooks

| Hook | Returns | Usage |
|------|---------|-------|
| `useAuth()` | `user`, `roles`, `tenant`, `scope`, `crud`, `teams`, `isLoading` | Global auth state |
| `useActiveRole()` | `canCreate`, `canRead`, `canUpdate`, `canDelete`, `scope` | Per-action permission checks |
| `useRoleConfig()` | `canAccessPage(pageKey)`, `canPerformAction(actionKey)` | Page/route/action guards |

### Usage Patterns

```typescript
// Check if user can create records
const { canCreate, scope } = useActiveRole();
if (!canCreate) return <AccessDenied />;

// Check if user can access a page
const { canAccessPage } = useRoleConfig();
if (!canAccessPage('hr-dashboard')) return <NotFound />;

// Scope-aware data filtering (automatic via RLS, but useful for UI)
if (scope === 'self') showOnlyMyRecords();
if (scope === 'team') showTeamRecords();
if (scope === 'global') showAllRecords();
```

## Data Fetching Pattern

All data queries use Supabase client + TanStack React Query:

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { supabase } from '@/integrations/supabase/client';

// READ
const { data, isLoading, error } = useQuery({
  queryKey: ['employees'],
  queryFn: async () => {
    const { data, error } = await supabase
      .from('employees')
      .select('*')
      .order('last_name');
    if (error) throw error;
    return data;
  },
});

// CREATE
const queryClient = useQueryClient();
const createMutation = useMutation({
  mutationFn: async (newEmployee: EmployeeInsert) => {
    const { data, error } = await supabase
      .from('employees')
      .insert(newEmployee)
      .select()
      .single();
    if (error) throw error;
    return data;
  },
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['employees'] });
  },
});
```

## RLS Migration Patterns

From `supabase/migrations/003_data_model_template.sql` — choose the pattern that matches the table's **use case**, not just a scope level. Each pattern uses `get_active_scope()` internally to apply the full 5-level hierarchy.

> **Authoritative reference**: [security-model.md — RLS Policy Patterns](security-model.md#rls-policy-patterns) has the full SQL for each pattern.

| Pattern | Use Case | When to Use | Logic Summary |
|---------|----------|-------------|---------------|
| **A** | Reference tables (lookups, types) | Tenant-isolated read for all; admin-only write | Tenant isolation + CRUD check; `org_admin`/`system_admin` for INSERT/UPDATE/DELETE |
| **B** | User-owned records (listings, contacts, deals) | Record ownership matters | Scope-aware CASE: self→own, team→own+reports, global+→all in tenant |
| **C** | Tenant-wide records (config, announcements) | Everyone in tenant reads all | All records in tenant for anyone with read access |
| **D** | Admin-only tables (audit, configuration) | Only admins write | Full CRUD restricted to `org_admin` / `system_admin` |
| **E** | System tables (cross-tenant) | Platform-wide data | Cross-tenant access for `system_admin` only |

RLS helper functions (available on both App DB and CDL projects — all read from `auth.jwt()` only):
- `get_current_tenant_id()` — extracts tenant UUID from JWT `uoi` claim
- `get_active_scope()` — extracts scope from JWT (`self` / `team` / `global` / `org_admin` / `system_admin`)
- `get_crud()` — extracts CRUD string from JWT
- `get_current_user_id()` — extracts SSO user UUID from JWT `sub` claim
- `get_current_team_ids()` — extracts team UUID array from JWT
- `is_sso_admin_v2()` / `is_admin_scope()` — returns true if scope is `org_admin` or `system_admin`

> **CDL Token Architecture (Apr 2026, ADR-012):** CDL PostgREST uses
> **Supabase Third-Party Auth** against the SSO JWKS URL + issuer. Apps
> send the SSO-issued ES256 JWT directly to CDL. There is **no**
> Supabase-native-token path and **no** `app_metadata` fallback on CDL
> RLS helpers — `oauth-token` embeds `scope`, `crud`, `team_ids`, and
> `uoi` in the JWT payload itself. Keeping the helpers JWT-only is what
> makes the CDL portable to Databricks Lakebase.

## UI Conventions

### Layout

Every page uses `SidebarLayout`:

```tsx
import SidebarLayout from '@/layouts/SidebarLayout';

export default function MyPage() {
  return (
    <SidebarLayout>
      <div className="p-6">
        {/* Page content */}
      </div>
    </SidebarLayout>
  );
}
```

### Route Protection

Every route uses `ProtectedRoute` with a `requiredPage` key:

```tsx
<Route
  path="/hr-dashboard"
  element={
    <ProtectedRoute requiredPage="hr-dashboard">
      <HRDashboard />
    </ProtectedRoute>
  }
/>
```

The `requiredPage` key is checked against `role_configurations.pages` for the user's role.

### Sidebar Structure

The sidebar is defined in `AppSidebar.tsx` as an array of sections. Each item has a `pageKey` for permission-based visibility:

```typescript
const sidebarSections = [
  {
    title: 'Employee',
    items: [
      { title: 'My Dashboard', url: '/', icon: Home, pageKey: 'home' },
      { title: 'My Vacations', url: '/my-vacations', icon: Calendar, pageKey: 'my-vacations', countKey: 'myVacations' },
    ],
  },
  {
    title: 'Human Resources',
    requiredScope: 'global', // Section only visible to global+ scope
    items: [
      { title: 'Personnel', url: '/personnel', icon: Users, pageKey: 'personnel' },
    ],
  },
];
```

### Sharp Design System

| Element | Value |
|---------|-------|
| Primary color | Navy/Blue (HSL variables in `index.css`) |
| Heading font | Playfair Display |
| Body font | Inter |
| Sidebar | Dark navy background |
| Components | shadcn/ui with Radix primitives |

## i18n Pattern

```tsx
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t } = useTranslation();
  return <h1>{t('settings.title')}</h1>;
}
```

Supported languages: English (`en`), Russian (`ru`).
Language detected from `localStorage` or browser `navigator.language`.

## Lovable-Managed Apps — Development & Maintenance Model

All Matrix business apps (HRMS, Pipeline, ITSM, Financial Management, Client Connect, Meeting Hub, MLS, etc.) are **Lovable-managed projects**. This means:

### Change Management via Lovable Prompts

The primary mechanism for modifying, fixing, or extending these apps is through **Lovable prompts** — structured instructions provided to the Lovable AI builder. Direct code edits outside Lovable are avoided because Lovable maintains its own state and may overwrite external changes on next publish.

**Best practices**:

| Practice | Detail |
|----------|--------|
| **Write prompts, not code** | Describe the desired change in a Lovable prompt; Lovable generates and applies the code |
| **Prompt files** | Store prompts as markdown files in the testing suite or project repo (e.g., `hrms-uat/prompts/`) for traceability |
| **One concern per prompt** | Each prompt should address a single feature, fix, or refactor for clarity |
| **Include file paths** | Reference exact file paths and existing code patterns so Lovable targets the right locations |
| **Specify what NOT to change** | Explicitly list files or patterns that must remain untouched to prevent regressions |
| **Test instructions** | Include testing steps in the prompt so the change can be verified after Lovable applies it |

**What CAN be changed directly (outside Lovable)**:
- SSO Edge Functions on the CDL/SSO instance (`switch-role`, `switch-tenant`, `admin-*`, etc.)
- Database migrations and RLS policies (via Supabase dashboard or CLI)
- CDL Edge Functions (`update-tenant-settings`, etc.)
- Apache deployment configuration

**What MUST go through Lovable prompts**:
- React component changes (pages, hooks, UI)
- `matrix-sso.ts` modifications (auth flow, token handling)
- Routing changes (`App.tsx`)
- State management (`AuthContext.tsx`, custom contexts)
- App-specific Edge Functions deployed from Lovable (e.g., `hrms-sync-permissions`)

### Prompt Archive

Lovable prompts for each app are stored alongside UAT materials:

| App | Prompt Location |
|-----|-----------------|
| HRMS | `/home/bitnami/matrix-testing-suite/hrms-uat/prompts/` |

## Lovable-Specific Rules

| Rule | Detail |
|------|--------|
| No `.env` files | All configuration hardcoded in `matrix-sso.ts` (Lovable doesn't support `.env`) |
| Environment detection | `isLovableEnvironment()` for dev vs production behavior |
| Component tagger | `lovable-tagger` Vite plugin in dev mode for AI component understanding |
| TypeScript strictness | Relaxed for Lovable compatibility |
| `CLIENT_ID` | Must be updated in `matrix-sso.ts` after app registration in SSO Console |
| `BASE_PATH` | Set in `matrix-sso.ts` for production subdirectory routing |

## Real App Example: Matrix HRMS

Source: `/home/bitnami/matrix-hrms` — a Domain-Specific app built from the template.

### What HRMS Added Beyond the Template

| Category | Template | HRMS |
|----------|----------|------|
| Database tables | 2 (`notifications`, `role_configurations`) | 25+ domain tables |
| Custom hooks | ~5 | 30+ |
| Pages | 4 (home, auth, callback, settings) | 20+ organized by role |
| Sidebar sections | 1 | 4 (Employee, Organization, Manager, HR Admin) |

### HRMS Domain Tables

**Employee management**: `employees`, `departments`, `locations`, `employee_managers`, `employee_ad_links`

**Leave management**: `vacations`, `vacation_balances`, `leave_policies`, `public_holidays`

**Performance**: `review_cycles`, `review_participants`, `goals`

**Onboarding/Offboarding**: `onboarding_templates`, `onboarding_template_tasks`, `onboarding_checklists`, `onboarding_tasks`, `offboarding_templates`, `offboarding_template_tasks`, `offboarding_checklists`, `offboarding_tasks`

**Compensation**: `compensation_history`, `payroll_records`

**Documents**: `document_templates`, `document_distributions`, `employee_documents`

**Other**: `internal_changes`, `social_posts`, `social_comments`, `social_reactions`, `employee_agreements`, `employee_edit_requests`

### Key Patterns from HRMS

**Approval workflow** (`internal_changes`):
- Status flow: `pending` → `approved` → `applied` (or `rejected`)
- Manager approves, HR applies changes to employee record
- IF status = 'approved' AND role = 'hr_admin' THEN apply changes to `employees` table

**Template-based processes** (onboarding):
- `onboarding_templates` → defines reusable task lists
- `onboarding_checklists` → instance of a template for a specific employee
- `onboarding_tasks` → individual tasks within a checklist, tracked to completion

**Role-based sidebar sections**:
- Employee section: visible to all (scope = self+)
- Manager section: visible when user has direct reports (scope = team+)
- HR Admin section: visible to global+ scope with HR role

**Directory view with privacy** (`employee_directory`):
- Database VIEW that masks sensitive columns (salary, personal phone, etc.)
- Public queries use the view; admin queries use the full `employees` table

### HRMS Supabase Instance

| Instance | Project ID | Purpose |
|----------|-----------|---------|
| SSO | `xgubaguglsnokjyudgvc` | Auth, permissions, AD users, tenants |
| HRMS App DB | `wltuhltnwhudgkkdsvsr` | All HR tables, RLS enforced via SSO JWT |

## Key Files Reference

### In `matrix-apps-template`

| File | Purpose |
|------|---------|
| `src/App.tsx` | Root component, route definitions |
| `src/main.tsx` | Entry point, QueryClient + i18n setup |
| `src/index.css` | Sharp design system CSS variables |
| `src/lib/matrix-sso.ts` | SSO client (1000+ lines): OAuth, JWT, refresh, config |
| `src/contexts/AuthContext.tsx` | React auth context provider |
| `src/components/ProtectedRoute.tsx` | Route guard with permission checks |
| `src/integrations/supabase/client.ts` | App DB Supabase client |
| `src/integrations/supabase/dataLayerClient.ts` | SSO/CDL Supabase client |
| `src/integrations/supabase/types.ts` | App DB TypeScript types (auto-generated) |
| `src/integrations/supabase/dataLayerTypes.ts` | SSO/CDL TypeScript types |
| `src/hooks/useActiveRole.ts` | CRUD permission helpers |
| `src/hooks/useRoleConfig.ts` | Page/action permission checks |
| `src/components/AppSidebar.tsx` | Main sidebar with role-based sections |
| `src/layouts/SidebarLayout.tsx` | Layout wrapper (sidebar + content) |
| `supabase/migrations/001_sso_helper_functions.sql` | RLS helper functions |
| `supabase/migrations/003_data_model_template.sql` | 5 RLS patterns (A-E) |

### In `matrix-hrms` (Domain-Specific example)

| File | What It Shows |
|------|--------------|
| `src/hooks/useEmployees.ts` | Querying employee directory with scope-aware filtering |
| `src/hooks/useVacations.ts` | CRUD operations with approval workflow |
| `src/hooks/useOnboarding.ts` | Template-based process management |
| `src/hooks/useInternalChanges.ts` | Change request workflow (create, approve, apply) |
| `src/hooks/useRoleConfig.ts` | Extended page/action permissions |
| `src/components/AppSidebar.tsx` | 4-section sidebar with badge counts and role-based visibility |

### In `matrix-atlas-mls` (CDL-Connected example)

| File | What It Shows |
|------|--------------|
| `src/integrations/supabase/cdlClient.ts` | CDL anon client (project `ofzcokolkeejgqfjaszq`) — separate from the SSO `dataLayerClient.ts` |
| `src/lib/cdl-edge-function-client.ts` | `invokeWithAuthCdl` helper — sends the SSO JWT to CDL EFs |
| `src/hooks/useMLSSync.ts` / `useMLSSettings.ts` | Calls `mls-sync` or `mls-sync-orchestrator` based on `mls_settings.sync_mode` |
| `src/hooks/useListingsSearch.ts` | Calls the `listings-search` EF (filters / pagination / sort) |
| `src/hooks/useMlsData.ts` (`useProperties`) | Reads `public.properties_published` via the CDL anon client |
| `src/components/AppSidebar.tsx` | Sidebar groups: `Overview` / `Application` / `MLS Sync` / `Administration` |
| `src/pages/AuthCallback.tsx` | OAuth2 + PKCE callback handler |

## Common Pitfalls (LLM Guidance)

These are hard-learned lessons. Violating any of them will cause silent failures.

### 1. Do NOT reintroduce "Supabase native tokens" for CDL

**Wrong**: Juggling `localStorage.getItem('matrix_supabase_access_token')`
for CDL PostgREST calls.
**Why it's stale**: That path existed when CDL lived on the SSO project
and PostgREST validated tokens against the local project key. The
Matrix CDL is now a **separate project** (`ofzcokolkeejgqfjaszq`)
configured with **Supabase Third-Party Auth** against the SSO JWKS
URL + issuer.
**Correct**: Send the SSO-issued ES256 JWT directly as
`Authorization: Bearer …`. `buildCdlClient()` does this automatically.
See ADR-012.

### 2. CDL RLS helpers are JWT-only — no `app_metadata` fallback

**Wrong**: Copy-pasting the old CDL helper definitions that read
`auth.users.raw_app_meta_data`.
**Why it's stale**: The CDL project now verifies SSO tokens natively
via Third-Party Auth; `scope`, `crud`, `team_ids`, and `uoi` are in
the JWT payload itself. Keeping the helpers JWT-only is what makes
the CDL portable to Databricks Lakebase.
**Correct**: Use the JWT-only helpers in
`matrix-platform-foundation/supabase/cdl/migrations/` (JWT-only RLS helpers).

### 3. `oauth-token` embeds claims in the JWT payload

**Wrong**: Treating `app_metadata` as the source of truth for scope /
crud / team claims.
**Why it fails**: CDL RLS reads from `auth.jwt()` only. If the claims
are not in the payload, CDL policies silently default to `'self'` /
no CRUD and queries return empty results.
**Correct**: `oauth-token` must add `scope`, `crud`, `team_ids`,
`uoi`, and `active_app` to the JWT payload it signs. Populating
`auth.users.raw_app_meta_data` is still allowed for SSO-side
conveniences but is not the CDL fallback.

### 4. CDL writes go through CDL-project EFs (never the app's project)

**Wrong**: Calling CDL PostgREST directly for INSERT/UPDATE/DELETE
from the browser, or proxying through an EF on the app's own Supabase
project.
**Why it fails**: CORS blocks direct writes; putting a write proxy on
each app's project fragments the write boundary and requires
distributing the CDL service-role key to every app.
**Correct**: Invoke an Edge Function on the **CDL project**
(`ofzcokolkeejgqfjaszq`). Today the deployed write paths are
`mls-sync` / `mls-sync-orchestrator` for MLS ingestion and admin, and
the 5 pipeline-stage EFs for orchestrated runs. If a future feature
needs a generic CRUD proxy, add a new EF to
`matrix-platform-foundation/supabase/cdl/functions/` rather than
distributing service-role keys.

### 5. Do NOT SQL-join CDL rows to `auth.users` / `sso_users`

**Wrong**: `select properties.*, auth.users.email from properties join …`.
**Why it fails**: `auth.users` is on the SSO project, not the CDL. The
join is impossible across projects and breaks again when CDL moves to
Lakebase.
**Correct**: Resolve display names client-side with the `useUserDisplay`
React hook (from `matrix-apps-template`), which batches IDs through the
`resolve-users` SSO Edge Function.

### 6. Don't conflate scope with admin privileges

**Wrong**: Treating `global` scope as admin for write operations on
config tables.
**Why it fails**: `global` means visibility (see all records in
tenant), not admin privileges. A Sales Director with `global` scope
should NOT be able to modify checklist templates or document type
configs.
**Correct**: Restrict config table writes to
`(SELECT get_active_scope()) IN ('org_admin', 'system_admin')`.

### 7. Ingestion into CDL goes through the unified pipeline

**Wrong**: Writing a bespoke EF that inserts directly into
`public.properties` or `public.properties_published`.
**Why it fails**: Skips staging (`cdl_staging.listings_raw` /
`listings_mapped`), the merge step's dedup-by-`(source_id,
source_listing_key)`, and the per-stage `public.ingest_audit` log.
**Correct**: Add a row in `public.mls_settings` (per tenant, with
`source_id`, RESO creds, schedule), then trigger the pipeline by
calling `mls-sync-orchestrator` (`action: 'start'`) or — if the lifted
monolith is required — `mls-sync`. The orchestrator chains
`reso-import → field-mapping-apply → listing-merge → media-import →
listing-publish` and records per-stage state in
`public.mls_orchestrator_runs`. See `docs/data-models/cdl-schema.md`
and ADR-014's Implementation Status note.
