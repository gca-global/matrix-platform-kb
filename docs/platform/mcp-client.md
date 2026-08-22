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

The agent receives **exactly** the tool catalogue each MCP server publishes via
`tools/list` (cached in `mcp_tools`). Policy, rate limits, audit and session
handling wrap those tools — we do **not** inject synthetic tools (no platform
`sign_in` helper). If the server itself exposes a session tool (e.g. Qobrix
`qobrix_sign_in`), it appears only when enabled in policy.

When a catalogue tool hits an unauthenticated session, the client returns a tool
result starting with `AUTH_REQUIRED:` and the exact single-use OAuth URL minted
by `createAuthUrl`. `AUTH_REQUIRED_TOOL_RULE` in the system prompt instructs the
model to paste that URL as plain text — never invent or shorten it. The user
opens the link, completes consent, and retries; the next tool call uses the
stored per-principal grant.

There is no separate chat UI for sign-in links — relay through the assistant
reply is intentional.

## Schema

Tables: `mcp_servers`, `mcp_server_secrets`, `mcp_oauth_clients`,
`mcp_oauth_states`, `mcp_principal_tokens`, `mcp_service_tokens`, `mcp_tools`,
`mcp_tool_policies`, `mcp_tool_calls`, `mcp_server_health`.
