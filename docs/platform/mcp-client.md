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

## Agent contract

The agent receives **exactly** the tool catalogue each MCP server publishes via
`tools/list` (cached in `mcp_tools`). Policy, rate limits, audit and session
handling wrap those tools — we do **not** inject synthetic tools.

### `server_managed` (Qobrix Mode C via `/mcp-c`)

The MCP server returns its own connect URL inside the tool result text (Markdown
link, `isError: false`). The client relays that text **verbatim** to the model.
There is no platform `AUTH_REQUIRED:` prefix and no chat sign-in UI.

Per-user vault isolation uses signed `X-Chat-*` headers
(`QOBRIX_MCP_IDENTITY_SECRET` on both the MCP host and the Edge Function).

### `oauth_user` (remote Mode D connectors)

The client is an OAuth 2.1 + PKCE user agent; callback
`{SUPABASE_URL}/functions/v1/mcp-oauth/callback`. HTTP 401 from the remote
server surfaces as a tool error — not a custom platform protocol.

### System directives

Runtime imperative fragments (date/time guidance, RAG/memory wrappers, tool
messages) live in `employees.system_directives` and the employee **System** tab
— not in hardcoded Edge Function strings. See [ADR-041](../architecture/decisions/ADR-041.md).

## Module layout

```
supabase/functions/_shared/mcp/
  types.ts, errors.ts, crypto.ts, transport.ts, client.ts, registry.ts, principal.ts
  auth/apikey.ts, auth/identity.ts
  auth/oauth/{discovery,client,flow,tokens}.ts
system-directives.ts
```

## Schema

Tables: `mcp_servers`, `mcp_server_secrets`, `mcp_oauth_clients`,
`mcp_oauth_states`, `mcp_principal_tokens`, `mcp_service_tokens`, `mcp_tools`,
`mcp_tool_policies`, `mcp_tool_calls`, `mcp_server_health`.
