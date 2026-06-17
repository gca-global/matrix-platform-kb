# Matrix MCP Server (MLS / Property)

> The **matrix-mcp** server is the AI-agent access layer over the Common Data
> Layer (CDL) for the MLS / property side of Sharp Matrix. It lets LLM agents
> (Claude, GPT, Cursor) and Matrix Apps read listings, brokers, and geo data
> through the **Model Context Protocol (MCP)** instead of talking to Supabase
> directly. It is the property counterpart to the
> [`qobrix-crm-mcp`](https://github.com/sharpsir-group/qobrix-crm-mcp) (CRM side).

This is the **planned hub/bridge** that supplies CDL data to other systems. It
realises part of the Phase-2 intelligence layer (see
[architecture/intelligence-layer.md](../architecture/intelligence-layer.md)).

| Property | Value |
|---|---|
| Repo | [`matrix-mcp`](https://github.com/sharpsir-group/matrix-mcp) |
| Role | Read-only MCP access layer over CDL (listings / brokers / geo) |
| Transport | MCP Streamable HTTP (JSON-RPC) — not REST |
| Public endpoint | `https://mls.sharpsir.group/matrix/mcp/` |
| Health | `https://mls.sharpsir.group/matrix/health/{live,ready}` (public) |
| Data source | Supabase **Matrix CDL** (`ofzcokolkeejgqfjaszq`) snake_case schema |
| Auth | HS256 JWT (`SUPABASE_JWT_SECRET`), required on `/mcp` |
| Status | **Live demo** — 5 of 7 designed tools registered |
| Ops runbook | `matrix-ops` → `runbooks/matrix-mcp.md` |

## Why an MCP server (not direct DB access)

CDL-Connected apps read RESO-named Supabase tables directly (see
[index.md](index.md) → "How Apps Share Data"). AI agents are different
consumers: they need **typed, discoverable tools** with guardrails (auth, rate
limits, caching, no SQL injection surface) rather than raw table access. The MCP
server is that contract — one place where listing/broker/geo queries are
exposed safely to any LLM client, and the bridge other future systems consume.

## Tools (current)

| Tool | What it does |
|---|---|
| `search_listings` | Structured filter search (country, city, price, bedrooms, type, status) |
| `search_by_text` | Free-text query → filters via DeepSeek LLM → structured search |
| `get_listing_details` | Full listing payload incl. broker (office contact) and media |
| `geo_search` | Radius search via haversine distance + filters |
| `broker_directory` | Broker discovery by country / language with listings count |

Deferred until embeddings exist: `search_by_intent`, `find_similar` (vector
search via pgvector + reranker). DeepSeek is a chat LLM with no embeddings API,
so it powers natural-language **filter extraction**, not vector search.

## Schema alignment

The server queries the **real CDL snake_case schema** (post PR4/PR6 renames):
`properties`, `members`, `property_media`. Key joins:

- `properties.list_agent_key = members.member_key` (text key, not UUID FK)
- `property_media.property_id = properties.id` (UUID) for media
- `title = COALESCE(x_property_name, unparsed_address)`, geo via
  `latitude`/`longitude` numerics (PostGIS not required)

See [data-models/cdl-schema.md](../data-models/cdl-schema.md) for the canonical
column reference.

## Access (for app/agent integrators)

1. Get a JWT from the ops owner (minted with `SUPABASE_JWT_SECRET`, one `sub`
   per consumer).
2. Point any MCP client at `https://mls.sharpsir.group/matrix/mcp/` with header
   `Authorization: Bearer <token>`.
3. Call `tools/list` then `tools/call`. Full API reference, token minting, and
   test recipes: `matrix-mcp` → [`docs/live-deployment.md`](https://github.com/sharpsir-group/matrix-mcp/blob/main/docs/live-deployment.md).

## Security posture

- Read-only by design; pooled DB role; JWT-gated `/mcp`; per-tenant rate limits
  (Redis); health endpoints public.
- Secrets currently in `.env` — should move to a secret manager and rotate.
- Related CDL hardening (RLS, RPC `EXECUTE` grants, storage buckets) tracked in
  [security-model.md](security-model.md).
