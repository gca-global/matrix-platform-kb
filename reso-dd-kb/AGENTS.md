# reso-dd-kb — Agent schema

> Drop any LLM agent (Cursor, Codex, Claude Code, Lovable) into this folder
> and it can answer "what does RESO say about X?" with citations, while
> keeping itself current as RESO publishes new DD or Cert data.

This file is the **schema** the agent obeys. It is hand-written and
read first; never overwritten by tooling.

---

## Layout

```
reso-dd-kb/
  AGENTS.md          # this file (schema)
  README.md          # 1-page human intro
  methodology.md     # ONE methodology page (naming, keys, lookups, lifecycle, Sys%/Org%)
  raw/               # immutable inputs — agent reads, never writes
    RESO_Data_Dictionary_2.0.xlsx
    fields.csv               # parsed from xlsx
    lookups.csv              # parsed from xlsx
    field_usage.csv          # RESO certification stats (Org% only)
    resource_usage.csv       # per-resource adoption summary
    field_descriptions.csv   # dumped from public.reso_field_descriptions
    field_metadata.csv       # scraped from DDwiki (full Sys%/Org% + structured KV)
  wiki/
    resources/<Resource>.md  # ONE generated MD per RESO Resource (~41 files)
  scripts/
    refresh.py               # idempotent rebuild of wiki/ from raw/
    fetch_field_metadata.py  # DDwiki scraper -> raw/field_metadata.csv
    dump_descriptions.sh     # supabase -> raw/field_descriptions.csv
```

## Boundaries

| Path | Owner | Modify? |
|---|---|---|
| `raw/` | source of truth | NEVER edit by hand. Replace whole CSVs from upstream sources. |
| `wiki/resources/` | generated | NEVER edit by hand. Re-run `scripts/refresh.py`. |
| `scripts/` | human + agent | Edit freely; keep idempotent. |
| `AGENTS.md`, `README.md`, `methodology.md` | human | Edit on policy change. |

## Resource page anatomy (what `refresh.py` produces)

Every `wiki/resources/<Resource>.md` has the same shape so the agent can
pattern-match without reading prose:

1. `# <Resource>` heading.
2. **Overview line** — one short paragraph from `field_descriptions.csv`
   (or a fallback pointing to the canonical DDwiki page).
3. **Adoption banner** — `WeightedOrgPct / FieldsWithUsage / Median /
   Avg` from `resource_usage.csv`.
4. `## Groups` — bullet list of Groups with field counts (lets the
   agent jump straight to the relevant Group).
5. `## Fields` — single table:
   `Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki`.
6. `## Field details` — collapsible `<details>` blocks per field with
   structured KV (BEDES, PropertyTypes, Spanish/French-Canadian names,
   Status / Revision dates) — only when the scrape captured anything
   non-trivial.
7. `## Lookups` — one section per LookupName referenced by this
   Resource, with `Value | Definition` table from `lookups.csv`.

## Query workflow (read order for any "what does RESO say about X?" question)

1. **Read `methodology.md` first** — it explains naming, keys, lookups,
   lifecycle, and how to read `Sys%` / `Org%`.
2. **Open the relevant `wiki/resources/<Resource>.md`** — the Fields
   table is the authoritative answer surface.
3. **Cite the field row** in your response. Use the `DDwiki` link only
   when the user asks for prose context the table cannot deliver.
4. **Never invent a field.** If a field is not in the table, it is not
   RESO. Tell the user.
5. **Atlas-custom fields** (e.g. `LifecycleState`) live in
   `field_descriptions.csv` with `source = atlas_custom`. They are
   labelled as such in the Resource pages and have no DDwiki URL.

## Refresh workflow (when RESO publishes a new spec)

1. Drop the new `RESO_Data_Dictionary_X.Y.xlsx` into `raw/`. Update the
   filename inside `scripts/refresh.py` if the version changes.
2. Re-parse: open the xlsx, dump `Fields` + `Lookups` sheets to
   `raw/fields.csv` + `raw/lookups.csv`. (5 lines of openpyxl —
   inlined when needed; not yet a dedicated script.)
3. Re-scrape DDwiki: `python3 scripts/fetch_field_metadata.py`.
   Honors `If-Modified-Since` so steady-state refreshes touch ~30-50
   pages instead of all ~1750.
4. Re-dump descriptions: `PSQL_URL=... bash scripts/dump_descriptions.sh`.
5. Re-render wiki: `python3 scripts/refresh.py`.
6. Commit the diff. The diff IS the changelog.

## Citation style

When the agent surfaces a field, cite it as:

```
RESO DD 2.0 · Property.OwnerName  (Sys% 35 / Org% 18)
[reso-dd-kb/wiki/resources/Property.md]
[https://ddwiki.reso.org/display/DDW20/OwnerName+Field]
```

For Atlas-custom fields:

```
Atlas-custom · LifecycleState (computed; not RESO DD)
[matrix-platform-foundation/supabase/cdl/migrations/...]
```

## Out of scope (intentionally)

- No HTML-to-MD prose mirror of DDwiki. The agent clicks the DDwiki
  link when it needs deep prose; this keeps the repo at ~5 MB instead
  of 12-240 MB.
- No vector store / embedding search. Markdown grep + the agent's
  built-in retrieval is enough at this corpus size.
- No `index.md` / `log.md` / `validate.sh` — premature for ~41
  generated files.
- No edits to `matrix-atlas-mls` or `matrix-platform-foundation`
  repos. This sub-wiki is a read-only KB.
