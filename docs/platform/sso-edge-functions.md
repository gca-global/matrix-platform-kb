# SSO Edge Functions — API Contracts

> Source: SSO instance `xgubaguglsnokjyudgvc` — Supabase Edge Functions (Deno runtime)
> Implementation: `matrix-platform-foundation/supabase/functions/`
>
> **For Lovable**: These are the Edge Functions your app calls for authentication, role management, and admin operations. All are deployed with `verify_jwt: false` unless noted — your code handles JWT verification.

## OAuth Flow Functions

These implement the OAuth 2.0 + PKCE flow used by all Matrix Apps.

### `oauth-authorize`

| Field | Value |
|-------|-------|
| Method | `GET` |
| Auth | None (initiates flow) |
| `verify_jwt` | `false` |
| Purpose | Starts OAuth flow — validates `client_id`, `redirect_uri`, `code_challenge`, generates authorization code |

**Query Parameters**: `client_id`, `redirect_uri`, `response_type=code`, `code_challenge`, `code_challenge_method=S256`, `state`, `scope`

**Response**: Redirects to SSO login page with session context.

### `oauth-token`

| Field | Value |
|-------|-------|
| Method | `POST` |
| Auth | None (exchanges code/refresh token) |
| `verify_jwt` | `false` |
| Purpose | Exchanges authorization code or refresh token for JWT. Signs ES256 or HS256 per app config ([ADR-011](../architecture/decisions/ADR-011.md)). |

**Grant Types**:
- `authorization_code` — exchanges code + PKCE verifier for access token + refresh token
- `refresh_token` — exchanges refresh token for new access token

**Request Body** (`application/json`):
```json
{
  "grant_type": "authorization_code",
  "code": "<authorization_code>",
  "redirect_uri": "<app_callback_url>",
  "client_id": "<client_id>",
  "code_verifier": "<pkce_verifier>"
}
```

**Server-managed PKCE (per-app opt-in)** — for public clients flagged
`sso_applications.server_managed_pkce = true`, `code_verifier` is **optional**:
the gate requires it only when `!app.server_managed_pkce`. Such clients send no
`code_challenge` (so the conditional challenge-validation is skipped) and exchange
on the code alone; authorization rests on the single-use, short-TTL code bound to
`redirect_uri` + `client_id` + an authenticated SSO session. This makes fresh
logins survive storage-stripping embedded browsers (Cursor in-IDE webview). The
flag defaults `false`; only Matrix Pipeline 2.0 is enabled so far. Backward
compatible — a client still sending challenge+verifier validates as before. See
[ADR-019](../architecture/decisions/ADR-019.md).

**Response** (`200`):
```json
{
  "access_token": "<JWT>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "<opaque_token>",
  "supabase_access_token": "<native_token>",
  "sso_role": { "id": "<uuid>", "name": "Sales Manager" },
  "scope": { "id": "team", "name": "Team" },
  "crud": "crud"
}
```

**Embedded JWT claims (2026 — login round-trip elimination)**: the minted access token now carries the **full consumed profile** so first-party apps can hydrate the user from the signed JWT without a second `oauth-userinfo` call. In addition to the role/scope/org claims it already carried (`sso_role`, `scope`, `crud`, `active_scope`, `organization`, `teams`, `allowed_apps`, `uoi`, `org_name`, `team_ids`, `groups`, `permissions`, `member_type`, `act_as_roles`, `attrs`), it now also includes: `email`, `email_verified`, `name`, `picture`, `available_roles`, and `tenant_id`. These are ES256-signed (equivalent trust to the userinfo response). The shared `matrix-apps-template` decodes them via `decodeUserFromToken` on login. Apps that have not synced the template keep calling `oauth-userinfo` and keep working. (See [performance.md](performance.md#sso-login-latency-auth-critical-path).)

**Side effects** (all **deferred** off the synchronous mint path via `EdgeRuntime.waitUntil` — they do not block the token response):
- Persists `active_scope`, `active_crud`, `active_team_ids` to `auth.users.raw_app_meta_data`. This is now a **fallback only**: the SSO-DB RLS helpers (`sso_get_active_scope`, `sso_get_crud`, `sso_get_current_team_ids`) read `request.jwt.claims` **first** and only consult `raw_app_meta_data` when the claim is absent — and the minted JWT always carries those claims, so deferring this write does not affect RLS for freshly-minted tokens.
- Backfills `tenant_id` / `azure_object_id` into `user_metadata` when missing.
- Stores token in `sso_access_tokens` table (synchronous; not deferred). ⚠️ The enriched JWT (~3.4 KB) exceeds the btree row-size limit (2704 bytes), so `sso_access_tokens.token` is indexed with a **hash** index (`idx_access_tokens_token_hash`, equality lookups only) plus a `md5(token)` **unique** guard — NOT a plain/unique btree on the raw token. Re-adding a btree index on the raw `token` column will break every login/refresh. (migration `20260601143000_fix_sso_access_tokens_token_index_for_enriched_jwt`.)

**Token-mint performance**: `getUserById` and `loadDefaultSettings` are fetched **once** per request and the independent reads (permissions, groups, roles, teams, attributes) run in `Promise.all` (previously serial, with a duplicate `getUserById`). See [performance.md](performance.md#sso-login-latency-auth-critical-path).

**Signing reliability (ES256-or-fail-closed)** — applies to all JWT-minting functions (`oauth-token`, `switch-role`, `switch-tenant`):
- The ES256 signing key (`get_vault_secret('sso_es256_signing_key')`) is **cached in module scope** (10 min TTL + in-flight de-dup) and fetched with a short retry. One successful vault load serves the warm instance, so a transient vault blip no longer forces a downgrade. The TTL lets a future key rotation propagate.
- For apps **without** `jwt_secret_name` (ES256 apps — their DB trusts only the SSO ES256 JWKS, kid via `sso-jwks`), if the ES256 key still cannot be resolved the function **fails closed with HTTP `503 temporarily_unavailable`** instead of silently minting an HS256 token. A downgraded HS256 token would be rejected by the app DB at the PostgREST auth layer (401), producing a confusing post-login 401 storm; a retryable 503 at mint time is the correct failure.
- For apps **with** `jwt_secret_name` (e.g. `jwt_secret_sso_console` → Sharp Matrix Portal, Appointment Reports/meeting-hub, New Client Registration/client-connect; per-app HRMS/ITSM secrets), behavior is unchanged: they always sign HS256 with their app secret and never touch the ES256 path or the 503 fail-closed branch.

**Issuer (`iss`) — 2026-05-31**: all minted tokens set `iss = https://xgubaguglsnokjyudgvc.supabase.co/auth/v1` (the SSO project's GoTrue issuer URL; was `"matrix-sso"`). This lets own-DB app projects verify SSO ES256 tokens via **Supabase Third-Party Auth** (which matches the token `iss` against a registered URL issuer + JWKS). The MLS app DB (`wckwfbbqiupvallmhqbu`, used by Pipeline / Atlas / Matrix MLS) has this TPA registered. Nothing verifies the old `"matrix-sso"` value — see [ADR-018](../architecture/decisions/ADR-018.md).

### `oauth-userinfo`

| Field | Value |
|-------|-------|
| Method | `GET` |
| Auth | `Bearer <SSO JWT>` |
| `verify_jwt` | `false` |
| Purpose | Returns current user info and role claims |

**Optional on the login path (2026)**: because `oauth-token` now embeds the full
profile in the JWT, first-party apps no longer call this on login — the shared
template hydrates from claims and calls `oauth-userinfo` only in the **background**
(freshness refresh) and for not-yet-migrated apps. **The response shape below is
frozen** — existing apps hydrate their entire user (incl. `act_as_roles`,
`member_type`, `permissions`, `groups`, `tenant_id`) from it. New JWT claims are
additive; userinfo fields are never renamed or removed.

**Token verification order** (incoming bearer): ES256 (cached vault key) → HS256
(`JWT_SECRET` / app secret) → opaque-token lookup (`sso_access_tokens`). The ES256
signature is now verified (previously an ES256 token fell through to the opaque DB
lookup with no signature check — KB gap H4, closed).

**Response** (`200`):
```json
{
  "sub": "<user_uuid>",
  "email": "user@sharpsir.group",
  "email_verified": true,
  "sso_role": { "id": "<uuid>", "name": "Sales Manager" },
  "scope": { "id": "team", "name": "Team" },
  "crud": "crud",
  "organization": { "id": "<tenant_uuid>", "name": "Sharp Sotheby's" },
  "teams": [{ "id": "<uuid>", "name": "Dubai Sales" }],
  "allowed_apps": [{ "id": "client_id", "name": "Pipeline Management" }],
  "available_roles": [{ "uuid": "<uuid>", "name": "Sales Manager", "scope": "team", "is_primary": true }],
  "tenant_id": "<tenant_uuid>",
  "member_type": "Broker",
  "act_as_roles": []
}
```

### `oauth-login`

| Field | Value |
|-------|-------|
| Method | `POST` |
| Auth | None |
| `verify_jwt` | `false` |
| Purpose | In-app login (email + password) — used by Lovable preview environment |

### `oauth-callback`

| Field | Value |
|-------|-------|
| Method | `GET` |
| Auth | None |
| `verify_jwt` | `false` |
| Purpose | Handles Azure AD redirect after authentication |

### `oauth-revoke`

| Field | Value |
|-------|-------|
| Method | `POST` |
| Auth | `client_id` + the refresh token itself (RFC 7009) |
| `verify_jwt` | `false` |
| Purpose | Revokes a refresh token. Authenticated by `client_id` (+ `client_secret` for confidential clients) and the token value — no SSO/Supabase JWT required. |

> **2026 fix**: `oauth-revoke` was previously `verify_jwt: true`, which forced the
> caller to hold a live Supabase session token just to log out. Per RFC 7009 and
> the rest of the OAuth surface it now runs `verify_jwt: false` and validates the
> client + token internally. Resolves the documented contradiction in this doc.

## Role Management

### `switch-role`

| Field | Value |
|-------|-------|
| Method | `POST` |
| Auth | `Bearer <SSO JWT>` |
| `verify_jwt` | `false` |
| Purpose | Re-issues JWT with a different active role. Signs ES256 or HS256 per app config. |

**Request Body**:
```json
{
  "role": "<role_uuid>",
  "client_id": "<client_id>",
  "client_secret": "<optional_for_public_clients>"
}
```

**Response** (`200`):
```json
{
  "access_token": "<new_JWT>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "<new_refresh_token>",
  "sso_role": { "id": "<uuid>", "name": "HR Manager" },
  "scope": { "id": "global", "name": "Global" },
  "crud": "crud"
}
```

**Token verification order** (incoming bearer):
1. ES256 (vault key)
2. App-specific HS256 (vault secret via `jwt_secret_name`)
3. SSO HS256 (`JWT_SECRET` env)
4. Opaque token lookup (`sso_access_tokens`)

**Side effects**: Persists `active_role_id` to `user_metadata`.

### `switch-tenant`

| Field | Value |
|-------|-------|
| Method | `POST` |
| Auth | `Bearer <SSO JWT>` |
| `verify_jwt` | `false` |
| Purpose | Re-issues JWT with a different active tenant/organization. Only `system_admin` scope. |

**Request Body**:
```json
{
  "tenant_id": "<tenant_uuid>",
  "client_id": "<client_id>"
}
```

**Response** (`200`):
```json
{
  "access_token": "<new_JWT>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "<new_refresh_token>",
  "organization": { "id": "<tenant_uuid>", "name": "Acme Corporation" }
}
```

**Error responses**:
- `403` `insufficient_scope` — caller does not have `system_admin` scope
- `404` `invalid_tenant` — tenant not found or inactive

**Token verification order**: Same as `switch-role` (ES256 → app HS256 → SSO HS256 → opaque lookup).

**Side effects**: Persists `tenant_id` to `user_metadata`. JWT `organization`, `uoi`, and `org_name` claims reflect the new tenant. Role/scope/CRUD remain unchanged.

**Relationship to `switch-role`**: Role switching changes *what you can do* (scope + CRUD). Tenant switching changes *which organization's data you see* (cross-tenant context for platform admins).

## Admin Functions

All admin functions require `org_admin` or `system_admin` scope.

**Token verification (`_shared/admin.ts` — `requireAdmin` / `requireAdminOrOrgAdmin` / `requireUserManagement`)**: ES256 (public vault key) → HS256 (app-specific via `jwt_secret_name`, else `JWT_SECRET`) → Supabase-native (`auth.getUser`) fallback. There is **no** opaque-token DB fallback here (unlike `oauth-userinfo`), so the signature path must actually verify.

> **2026-06-01 fix — admin EFs 401'd for ES256 apps (e.g. Matrix Pipeline 2.0).** The shared admin helper previously ran an **HS256-only** `jwtVerify`. ES256 SSO tokens (apps with no `jwt_secret_name`) failed it, fell through to `auth.getUser()` (which rejects custom tokens), and returned **401** — most visibly on the Pipeline **AD Employees** page (`admin-ad-users`). HRMS was unaffected because it uses an HS256 app secret (`jwt_secret_smhrms`). Fix: add ES256-first verification mirroring `oauth-userinfo`, **deriving the PUBLIC JWK (drop `d`)** before `importJWK`. Importing the stored *private* JWK as-is yields a sign-only key that `jwtVerify` cannot use (it would throw and silently downgrade to HS256). All 9 admin EFs that import `_shared/admin.ts` (`admin-ad-users`, `admin-users`, `admin-roles`, `admin-apps`, `admin-groups`, `admin-permissions`, `admin-privileges`, `admin-dashboard`, `admin-microsoft-auth`) were redeployed (`verify_jwt=false`). Verified: a minted `rw_global`/`global`-scope ES256 token → `admin-ad-users` 200 (was 401). Note `admin-dashboard` also had a stale `./_shared` import path corrected to `../_shared`. **Related latent issue (not fixed here):** `oauth-userinfo`'s ES256 path imports the private JWK too, so it is effectively inert and only succeeds via its opaque-token DB fallback — it should adopt the same public-key derivation (follow-up).

| Function | Method | Purpose |
|----------|--------|---------|
| `admin-users` | `GET/POST/PATCH/DELETE` | CRUD for SSO users (list, create, update, delete, reset password) |
| `admin-roles` | `GET/POST/PATCH/DELETE` | CRUD for `sso_roles` (list, create, update CRUD flags, delete) |
| `admin-apps` | `GET/POST/PATCH/DELETE` | CRUD for `sso_applications` (register, update, deactivate) |
| `admin-groups` | `GET/POST/PATCH/DELETE` | CRUD for `sso_user_groups` and memberships |
| `admin-permissions` | `GET/POST/DELETE` | CRUD for `sso_user_permissions` |
| `admin-tenants` | `GET/POST/PATCH` | CRUD for `tenants` |
| `admin-dashboard` | `GET` | Dashboard statistics (user counts, role distribution, login activity) |
| `admin-privileges` | `GET/POST/PATCH` | Manage privilege escalation and delegation |
| `check-permissions` | `POST` | Check if a user has a specific permission for an app |

## Identity & Directory

| Function | Method | Purpose |
|----------|--------|---------|
| `sync-azure-profile` | `POST` | Syncs user profile from Azure AD (photo, job title, department) |
| `sync-ad-users` | `POST` | Bulk syncs Azure AD user directory to `ad_users` table |
| `sync-ad-photos` | `POST` | Syncs Azure AD profile photos to storage |
| `admin-ad-users` | `GET` | Queries Azure AD directory with filtering |
| `admin-microsoft-auth` | `POST` | Manages Microsoft Graph API tokens for AD integration |
| `sso-token-exchange` | `POST` | Exchanges external tokens for SSO tokens |

## AI & Utility

| Function | Method | Purpose |
|----------|--------|---------|
| `portal-agent-chat` | `POST` | AI chat for the portal (RAG-powered) |
| `rag-search` | `POST` | Semantic search over KB embeddings |
| `parse-meeting-info` | `POST` | AI extraction of meeting details from text |
| `parse-client-info` | `POST` | AI extraction of client details from text |
| `parse-advisor-command` | `POST` | AI parsing of natural language commands |
| `transcribe-audio` | `POST` | Speech-to-text transcription |
| `text-to-speech` | `POST` | Text-to-speech synthesis |
| `generate-summary` | `POST` | AI text summarization |
| `batch-generate-summaries` | `POST` | Batch AI summarization |

## CDL Data Functions

| Function | Method | Purpose |
|----------|--------|---------|
| `check-mls-duplicate` | `POST` | Checks for duplicate MLS listings before import |
| `fetch-mls-contacts` | `POST` | Fetches MLS contact data for matching |

## Utility

| Function | Method | Purpose |
|----------|--------|---------|
| `upload-app-icon` | `POST` | Uploads application icon to storage |
| `get-users-with-emails` | `GET` | Resolves user UUIDs to email addresses |
| `admin-set-password` | `POST` | Admin resets user password |
| `validate-sso-token` | `POST` | Validates an SSO token and returns claims |
| `generate-sso-token` | `POST` | Generates an SSO token for service-to-service calls |

## `verify_jwt` Configuration

All SSO-facing functions use `verify_jwt: false` with custom JWT verification in code. This is required because:

1. Custom SSO tokens (ES256/HS256) are not Supabase Auth tokens
2. `verify_jwt: true` causes Supabase to reject the request **before** your code runs if the JWT isn't a valid Supabase native token
3. Functions need to accept tokens from multiple sources (ES256, app HS256, SSO HS256, opaque)

**Exceptions** (`verify_jwt: true` — accept Supabase native tokens only): `admin-set-password`, `generate-sso-token`, `validate-sso-token`, `get-users-with-emails`.

> **2026 fix**: `oauth-revoke`, `resolve-users`, and `check-privileges` were moved to `verify_jwt: false` (added explicitly to `config.toml`). They accept **custom SSO tokens** (or, for revoke, client-credentials + token) and verify internally, so gating them with the platform JWT check was incorrect — it rejected valid ES256 SSO tokens / forced a live Supabase session for logout. This closes the documented `verify_jwt` contradiction.

See [ADR-007](../architecture/decisions/ADR-007.md) for the Edge Function architecture decision.

## Cross-Reference

| For | See |
|-----|-----|
| JWT claims structure | [security-model.md](security-model.md#jwt-claims-structure) |
| ES256 signing logic | [security-model.md](security-model.md#jwt-signing--es256-target--hs256-legacy) |
| ES256 migration plan | [ADR-011](../architecture/decisions/ADR-011.md) |
| App-side auth hooks | [app-template.md](app-template.md#auth-hooks) |
| Full app auth flow | [app-template.md](app-template.md#sso-auth-flow) |
