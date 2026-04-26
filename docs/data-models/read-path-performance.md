# Read-path performance — `properties_published` + `listings-search`

> **Goal.** Sub-20 ms in-DB read latency for the `properties_published` hot
> path so the same EF can serve every Sharp Matrix outbound channel
> (matrix-cy-website, matrix-mobile, syndication, AI agents, Dash). This
> doc is the implementation contract behind that goal.

## Latency budget

The plan target is 10–20 ms at the database for a typical
filtered+paginated query against `public.properties_published`. The
end-to-end budget that callers see is dominated by network and EF
warm-up:

| Stage | Budget | Notes |
|---|---|---|
| Postgres execution (planner + scan + return) | ≤ 20 ms p95 | Index-only or 1-index scan + LIMIT |
| Edge Function compute (parse + serialize) | ≤ 30 ms p95 | Module-scope client; no per-call cold start |
| TLS + CDN edge to Supabase | varies | ~150 ms VM→Supabase; ~30–80 ms CDN-edge |
| **Total p95 (warm)** | **≤ 250 ms** | typical authenticated browser caller |

Test budgets (`matrix-testing-suite/tests/apps_atlas/test_atlas_listings_search_perf.sh`)
deliberately include the network tail and aim for:

- p50 ≤ 800 ms
- p95 ≤ 1200 ms
- p99 ≤ 2500 ms

Tightening these requires either fronting `listings-search` with a CDN
cache (intended for Phase-2.5 distribution layer) or co-locating the
caller with the Supabase region.

## Hot-path index strategy (Postgres)

Migration `20260426140000_cdl_properties_published_perf_indexes.sql`
lands eight selective B-tree indexes plus two GIN trigram indexes:

| Index | Columns | Query pattern |
|---|---|---|
| `idx_pp_keyset` | `(published_at desc, id desc) where is_visible and not is_deleted` | Default sort + keyset cursor |
| `idx_pp_status_visible` | `(status) where is_visible and not is_deleted` | Status facet on Listings page |
| `idx_pp_lifecycle` | `(lifecycle_state) where is_visible and not is_deleted` | Dash-aligned active inventory filter |
| `idx_pp_property_type` | `(property_type) where is_visible and not is_deleted` | Type facet |
| `idx_pp_geo` | `(country, city) where is_visible and not is_deleted` | Geo facet |
| `idx_pp_price` | `(price) where is_visible and not is_deleted` | Sort-by-price + range filter |
| `idx_pp_source_id_id` | `(source_id, id desc)` | Per-source pagination |
| `idx_pp_sir_branded` | `(x_sm_is_sir_branded) where x_sm_is_sir_branded` | SIR-only outbound channels |
| `idx_pp_title_trgm` | GIN trgm `(title_en)` | Fuzzy free-text |
| `idx_pp_desc_trgm` | GIN trgm `(description_en)` | Fuzzy free-text |

`pg_trgm` is enabled by the same migration. All indexes are partial
where possible — they only carry visible/non-deleted rows, which keeps
both their on-disk size and their write-side maintenance cost down.

### Statistics targets

`ALTER COLUMN ... SET STATISTICS 500` on `price`, `city`, `country`,
`listing_agent_key`, `property_type` so the planner has enough buckets to
distinguish facet selectivity. Without this, broad facets (e.g.
`country='Cyprus'` covering 90% of rows) can collapse onto the wrong
index.

### Autovacuum

`properties_published` is rewritten by the publish step on every sync,
so autovacuum thresholds are tightened:

```
autovacuum_vacuum_scale_factor   = 0.05  (default 0.2)
autovacuum_vacuum_threshold      = 1000  (default 50)
autovacuum_analyze_scale_factor  = 0.02  (default 0.1)
autovacuum_analyze_threshold     = 500   (default 50)
```

`mls-sync` additionally calls `public.cdl_analyze_published()` (a
`SECURITY DEFINER` wrapper around `analyze public.properties_published`)
at the end of every sync that touched the snapshot, so the planner has
fresh statistics before the next read wave.

## Edge Function tuning (`listings-search`)

The read EF lives at
[`matrix-platform-foundation/supabase/cdl/functions/listings-search/index.ts`](https://github.com/sharpsir-group/matrix-platform-foundation/tree/main/supabase/cdl/functions/listings-search).

### Keyset pagination (cursor)

Default sort is `published_at desc, id desc`. A trailing `id` tiebreak
makes the order deterministic — without it the planner may return rows
in arbitrary order when `published_at` ties, which corrupts cursor
correctness.

The cursor is a base64url-encoded JSON `{published_at, id}`. Clients
pass it back as `cursor` to fetch the next page. When `cursor` is set,
`page` is ignored — keyset is stateless.

### Estimated counts

`countMode: 'estimated'` is the default. Exact counts force a parallel
`COUNT(*)` over the entire selection, which dominates cost on
million-row tables. Admin pages opt in to exact counts with
`estimateCount: false`.

### HTTP caching

Every successful response carries:

```
Cache-Control: public, max-age=0, s-maxage=60, stale-while-revalidate=120
ETag: W/"<quick-hash>"
Vary: Authorization
```

Clients that send back `If-None-Match: <etag>` get a `304 Not Modified`
with no body, which short-circuits the entire query path. CDN edges
honor `s-maxage=60` independently. Public website / mobile callers
benefit immediately; authenticated callers benefit on repeat queries
within the 60 s window.

## Test surface

`matrix-testing-suite/tests/apps_atlas/test_atlas_listings_search_perf.sh`
runs 100 sequential GETs and asserts:

- p50 / p95 / p99 latency under budget
- `nextCursor` returned + cursor follow-up disjoint from page-1 ids
- `ETag` header present + `If-None-Match` returns `304`
- Default `countMode === 'estimated'`

The test discards the first sample (cold start) so the percentiles
reflect warm behaviour.

## Phase-2 hooks

The intelligence-layer foundation migration
(`20260426141000_cdl_phase2_intelligence_foundation.sql`) adds
placeholder columns that don't affect the read path today:

- `embedding vector(1536)` — populated by the Phase-2 `embed-properties`
  EF for semantic search.
- `feature_vector jsonb` — algebraic-search feature space.
- `marketing_metadata jsonb` (GIN-indexed) — channel-distribution
  decisions, recsys signals, Dash override state.

The partial index on `id where embedding is not null` is the primary
search index when Phase-2 is wired; until then it stays empty and
incurs no maintenance cost.

## Cross-reference

| Topic | See |
|---|---|
| Schema overview | [`cdl-schema.md`](cdl-schema.md) |
| Dash projection layer | [`dash-data-model.md`](dash-data-model.md) |
| Stewardship + lifecycle | [`cdl-schema.md`](cdl-schema.md#phase-1-expansion---full-reso-ingestion--dash-projection-apr-2026) |
| Test runner | `matrix-testing-suite/tests/apps_atlas/test_atlas_listings_search_perf.sh` |
