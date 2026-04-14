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

**Side effects**:
- Persists `active_scope`, `active_crud`, `active_team_ids` to `auth.users.raw_app_meta_data` (enables CDL RLS fallback)
- Stores token in `sso_access_tokens` table

### `oauth-userinfo`

| Field | Value |
|-------|-------|
| Method | `GET` |
| Auth | `Bearer <SSO JWT>` |
| `verify_jwt` | `false` |
| Purpose | Returns current user info and role claims |

**Response** (`200`):
```json
{
  "sub": "<user_uuid>",
  "email": "user@sharpsir.group",
  "sso_role": { "id": "<uuid>", "name": "Sales Manager" },
  "scope": { "id": "team", "name": "Team" },
  "crud": "crud",
  "organization": { "id": "<tenant_uuid>", "name": "Sharp Sotheby's" },
  "teams": [{ "id": "<uuid>", "name": "Dubai Sales" }],
  "allowed_apps": [{ "id": "client_id", "name": "Pipeline Management" }],
  "available_roles": [{ "uuid": "<uuid>", "name": "Sales Manager", "scope": "team", "is_primary": true }]
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
| Auth | `Bearer <SSO JWT>` |
| `verify_jwt` | `true` |
| Purpose | Revokes access token and associated refresh token |

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

**Exceptions**: `oauth-revoke`, `admin-set-password`, `generate-sso-token`, `validate-sso-token`, `get-users-with-emails`, `check-privileges` use `verify_jwt: true` (accept Supabase native tokens only).

See [ADR-007](../architecture/decisions/ADR-007.md) for the Edge Function architecture decision.

## Cross-Reference

| For | See |
|-----|-----|
| JWT claims structure | [security-model.md](security-model.md#jwt-claims-structure) |
| ES256 signing logic | [security-model.md](security-model.md#jwt-signing--es256-target--hs256-legacy) |
| ES256 migration plan | [ADR-011](../architecture/decisions/ADR-011.md) |
| App-side auth hooks | [app-template.md](app-template.md#auth-hooks) |
| Full app auth flow | [app-template.md](app-template.md#sso-auth-flow) |
