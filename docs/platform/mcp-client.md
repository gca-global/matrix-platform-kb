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
| `server_managed` | Mode C | No client credential; relay server's connect URL verbatim |
| `oauth_user` | Mode D | Per-principal OAuth 2.1 + PKCE; PRM discovery (Qobrix production path) |
| `oauth_service` | — | Client-credentials |

## Agent contract

The agent receives **exactly** the tool catalogue each MCP server publishes via
`tools/list` (cached in `mcp_tools`). Policy, rate limits, audit and session
handling wrap those tools — we do **not** inject synthetic tools.

### `oauth_user` (Qobrix and remote Mode D connectors)

The client is an OAuth 2.1 + PKCE user agent; callback
`{SUPABASE_URL}/functions/v1/mcp-oauth/callback`. HTTP 401 from the remote
server surfaces as a tool error — not a custom platform protocol.

### `server_managed` (Mode C servers)

The MCP server returns its own connect URL inside the tool result text. The client
relays that text **verbatim** to the model. No platform `AUTH_REQUIRED:` prefix
and no chat sign-in UI.

### System prompt

The Playground chat system prompt is composed only from operator-edited employee
fields (`job_title`, `responsibilities`, `system_prompt`, etc.) plus bare runtime
facts (current date/time, caller profile when `identity_required`, RAG chunks and
memory blocks when enabled). No platform-injected directive strings.

## Module layout

```
supabase/functions/_shared/mcp/
  types.ts, errors.ts, crypto.ts, transport.ts, client.ts, registry.ts, principal.ts
  auth/apikey.ts
  auth/oauth/{discovery,client,flow,tokens}.ts
```

## Schema

See `supabase/migrations/` in `matrix-digital-employees` for `mcp_servers`,
`mcp_tools`, `mcp_tool_policies`, `mcp_tool_calls`, `mcp_oauth_*`.
