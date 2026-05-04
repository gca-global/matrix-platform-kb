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
  methodology.md     # ONE methodology page (naming, keys, lookups, lifecycle, Org%)
  raw/               # immutable inputs — agent reads, never writes
    RESO_Data_Dictionary_2.0.xlsx
    fields.csv               # parsed from xlsx
    lookups.csv              # parsed from xlsx
    field_usage.csv          # RESO certification stats (Org% only) — fallback
    resource_usage.csv       # per-resource adoption summary
    field_descriptions.csv   # dumped from public.reso_field_descriptions
    field_metadata.csv       # scraped from dd.reso.org per Field (Org% + structured KV)
    resource_metadata.csv    # scraped from dd.reso.org per Resource (definition + counts)
    lookup_metadata.csv      # scraped from dd.reso.org per LookupName (UsedBy + counts)
  wiki/
    resources/<Resource>.md          # ONE generated MD per RESO Resource (~41 files)
    dbml/reso-2.0-canonical.dbml     # generated full RESO 2.0 canonical DBML (2NF normalized)
    atlas/atlas-target.dbml          # generated Atlas-adapted DBML (may re-add satellites)
  scripts/
    refresh.py                     # idempotent rebuild of wiki/resources/ from raw/
    fetch_resource_metadata.py     # dd.reso.org -> raw/resource_metadata.csv
    fetch_field_metadata.py        # dd.reso.org -> raw/field_metadata.csv
    fetch_lookup_metadata.py       # dd.reso.org -> raw/lookup_metadata.csv
    build_reso_canonical_dbml.py   # raw/ -> wiki/dbml/reso-2.0-canonical.dbml
    build_atlas_target_dbml.py     # raw/ -> wiki/atlas/atlas-target.dbml
    dump_descriptions.sh           # supabase -> raw/field_descriptions.csv
```

**Upstream source.** All `*_metadata.csv` files are scraped from
[dd.reso.org/DD2.0](https://dd.reso.org/DD2.0/), the official RESO
documentation site. The legacy [ddwiki.reso.org](https://ddwiki.reso.org/)
is being retired by RESO; this KB no longer reads it. The
`WikiPageUrl` columns inside `raw/fields.csv` and `raw/lookups.csv`
(parsed from the official RESO xlsx) still point at ddwiki and are
preserved as tombstones; primary links go to dd.reso.org.

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
2. **Overview line** — definition prose from `resource_metadata.csv`
   (with `field_descriptions.csv` as fallback).
3. **dd.reso.org banner** — `<N> fields · last revised <date> · [dd.reso.org]`
   from `resource_metadata.csv`.
4. **Adoption banner** — `WeightedOrgPct / FieldsWithUsage / Median /
   Avg` from `resource_usage.csv`.
5. `## Groups` — bullet list of Groups with field counts (lets the
   agent jump straight to the relevant Group).
6. `## Fields` — single table:
   `Field | Type | Group | Lookup | Org% | Description | Source`.
7. `## Field details` — collapsible `<details>` blocks per field with
   structured KV (BEDES, PropertyTypes, Spanish/French-Canadian names,
   Status / Revision dates) — only when the scrape captured anything
   non-trivial.
8. `## Lookups` — one section per LookupName referenced by this
   Resource, with a `<N> values · used by <K> field(s) · [dd.reso.org]`
   subhead from `lookup_metadata.csv` and a `Value | Definition` table
   from `lookups.csv`.

> Note on `Sys%`: ddwiki used to publish a per-System adoption
> percentage in addition to per-Organization. dd.reso.org dropped
> the per-System breakdown, so the KB now exposes `Org%` only.

## Canonical DBML normalization (2NF)

The canonical DBML (`wiki/dbml/reso-2.0-canonical.dbml`) is **2NF
normalized**. RESO 2.0 ships with hundreds of *satellite fields* —
scalar columns whose value depends on a Resource-typed FK on the same
host (e.g. `Property.ListAgentEmail`, `Property.OriginatingSystemName`,
`ContactListings.ListingId`). They violate 2NF because they are
functionally dependent on the FK column rather than the host PK.

`scripts/build_reso_canonical_dbml.py` detects them automatically: for
each Resource-typed FK on host `H` with `TargetResourceKey K`, every
other non-Resource scalar field on `H` whose name starts with the
prefix-of-`K` (with the trailing `Key` / `ID` / `Id` stripped) is a
satellite, except for `H`'s own PK and other FK columns.

Two flavours of satellite are dropped uniformly:

1. **True denormalizations** — the column also exists on the target
   (`Property.ListAgentEmail` mirrors `Member.MemberEmail`). Reachable
   via the FK join.
2. **Auxiliary identifiers / relationship attributes** — the column
   does not exist on the target and would belong in a junction table
   in a fully relational model (`Property.OriginatingSystemKey` =
   "this listing's identifier in the originating system";
   `ContactListings.ListingViewedYN` is a property of the
   `(Contact, Listing)` pair, not of `Property` alone).

Both flavours are removed from the canonical model. The full list of
dropped satellites is reproduced as a comment header at the top of
`wiki/dbml/reso-2.0-canonical.dbml`. Operational stores (Atlas) may
re-add a chosen subset for query performance via
`build_atlas_target_dbml.py`; the wiki resource pages
(`wiki/resources/*.md`) still document satellites because they are
part of the RESO 2.0 spec, even though they are not modelled as
columns in the canonical DBML.

## Query workflow (read order for any "what does RESO say about X?" question)

1. **Read `methodology.md` first** — it explains naming, keys, lookups,
   lifecycle, and how to read `Org%`.
2. **Open the relevant `wiki/resources/<Resource>.md`** — the Fields
   table is the authoritative answer surface.
3. **Cite the field row** in your response. Use the `Source` link
   (dd.reso.org) only when the user asks for prose context the table
   cannot deliver.
4. **Never invent a field.** If a field is not in the table, it is not
   RESO. Tell the user.
5. **Atlas-custom fields** (e.g. `LifecycleState`) live in
   `field_descriptions.csv` with `source = atlas_custom`. They are
   labelled as such in the Resource pages and have no upstream URL.

## Refresh workflow (when RESO publishes a new spec)

1. Drop the new `RESO_Data_Dictionary_X.Y.xlsx` into `raw/`. Update the
   filename inside `scripts/refresh.py` if the version changes.
2. Re-parse: open the xlsx, dump `Fields` + `Lookups` sheets to
   `raw/fields.csv` + `raw/lookups.csv`. (5 lines of openpyxl —
   inlined when needed; not yet a dedicated script.)
3. Re-scrape dd.reso.org (in any order):
   - `python3 scripts/fetch_resource_metadata.py` (~41 pages)
   - `python3 scripts/fetch_lookup_metadata.py` (~290 pages)
   - `python3 scripts/fetch_field_metadata.py` (~1,745 pages)
   All three honour `If-Modified-Since` so steady-state refreshes touch
   tens of pages instead of thousands.
4. Re-dump descriptions: `PSQL_URL=... bash scripts/dump_descriptions.sh`.
5. Re-render wiki: `python3 scripts/refresh.py`.
6. Re-build the canonical DBML: `python3 scripts/build_reso_canonical_dbml.py`.
7. Commit the diff. The diff IS the changelog.

## Citation style

When the agent surfaces a field, cite it as:

```
RESO DD 2.0 · Property.OwnerName  (Org% 18)
[reso-dd-kb/wiki/resources/Property.md]
[https://dd.reso.org/DD2.0/Property/OwnerName/]
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
