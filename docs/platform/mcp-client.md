# Matrix MCP client (Digital Employees)

> Companion to [matrix-mcp-server.md](matrix-mcp-server.md) and
> [ADR-040](../architecture/decisions/ADR-040.md).
> Server-side reference: [ADR-039](../architecture/decisions/ADR-039.md).

## Role

`matrix-digital-employees` is an MCP **client**. Tenants register remote MCP
servers; admins enable tools per digital employee; agents call tools under an
explicit **principal** with governance (Allow / Ask / Deny, rate limits, audit).

## Auth modes

| `auth_mode` | Maps to Qobrix | Notes |
|-------------|----------------|-------|
| `none` | — | Public / open servers |
| `api_key` | Mode B | Arbitrary header set; secrets encrypted or env `secret_ref` |
| `server_managed` | Mode C | No client credential; relay server's connect URL |
| `oauth_user` | Mode D | Per-principal OAuth 2.1 + PKCE; PRM discovery |
| `oauth_service` | — | Client-credentials |

## Module layout

```
supabase/functions/_shared/mcp/
  types.ts, errors.ts, crypto.ts, transport.ts, client.ts, registry.ts, principal.ts
  auth/apikey.ts, auth/server-managed.ts
  auth/oauth/{discovery,client,flow,tokens}.ts
```

Edge functions: `mcp-admin` (registry/policy/approvals), `mcp-oauth` (callback +
start/status/disconnect). Legacy `tools-api` / `tools-oauth` are shims.

Canonical redirect URI: `{SUPABASE_URL}/functions/v1/mcp-oauth/callback`  
(Legacy `…/tools-oauth` kept for Qobrix AS allow-list.)

## Agent contract

Tool results that need sign-in start with `AUTH_REQUIRED:` and include the exact
single-use URL. Models must paste that URL as plain text — never invent one.
Sign-in tools are registered for OAuth / server-managed servers regardless of
whether the tool catalogue is warm.

## Schema

Tables: `mcp_servers`, `mcp_server_secrets`, `mcp_oauth_clients`,
`mcp_oauth_states`, `mcp_principal_tokens`, `mcp_service_tokens`, `mcp_tools`,
`mcp_tool_policies`, `mcp_tool_calls`, `mcp_server_health`.
