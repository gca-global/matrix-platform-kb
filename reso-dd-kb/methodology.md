# Methodology - Phase 1 (mirror + extract)

## Why this exists

The previous iteration of `reso-dd-kb/` blended three sources:

1. The xlsx export of the RESO DD 2.0 spreadsheet.
2. A targeted scrape of `dd.reso.org/DD2.0/`.
3. A hand-curated `RESOURCE_ALIASES` map filling the gaps.

The xlsx + wiki sources both derive from RESO's master metadata DB and
agreed on FK info to the bit, but neither carried the full per-field
Definition prose nor surfaced relationships beyond a sparse 113 of
1,745 fields. The alias map was needed to bridge well-known role-name
gaps (`Listing -> Property`, `Contact -> Contacts`,
`OriginatingSystem -> OUID`, ...) that no source declared explicitly.

The Phase 1 rebuild moves to a single source of truth - a verbatim
local mirror of `dd.reso.org/DD2.0/` - and captures *every* visible
metadata cell on every page, including the full Definition prose. The
prose contains explicit FK statements (e.g. "primary key of the source
resource", "foreign key from the X Resource", "X Resource's YKey"),
which Phase 2 will mine for relationships. Once that's done, the alias
map should mostly disappear.

## Phase 1 steps

### 1. Mirror

```bash
bash scripts/01_mirror.sh
```

Uses `wget --mirror` with politeness flags:

| Flag | Why |
|---|---|
| `--mirror` | Recursive, infinite depth, timestamping. |
| `--no-parent` | Do not crawl above `/DD2.0/`. |
| `--convert-links` | Rewrite internal links so the mirror is browsable offline. |
| `--adjust-extension` | Save as `.html` so `index.html` is unambiguous. |
| `--page-requisites` | Pull CSS/images so pages render locally. |
| `--no-host-directories` | Output paths are `mirror/DD2.0/...`, not `mirror/dd.reso.org/DD2.0/...`. |
| `--domains=dd.reso.org` | Refuse to follow off-domain links. |
| `--wait=1 --random-wait` | ~1 req/s with jitter; gentle on the server. |
| `--user-agent=...` | Identifies the bot with a contact email. |
| `--execute robots=on` | Respects RESO's `robots.txt`. |
| `--output-file=...` | Full crawl log goes to `_meta/crawl.log`. |

After wget exits, `scripts/_emit_manifest.py` walks the mirror tree
and emits `_meta/manifest.json`: one entry per file with URL, local
path, status code, byte size, and sha256. This manifest is what later
phases trust - if a fact isn't in the manifest, it isn't in the
canonical KB.

The manifest's authoritative status field is "do we have the bytes?"
(i.e. file present on disk and non-empty -> 200). The historical HTTP
status from the crawl log is preserved in `crawl_log_status` whenever
it disagrees, so reviewers can tell that a file was, for example,
re-fetched manually after a transient 5xx during the original crawl.

#### Manual gap-fills

Two upstream artefacts caused the initial crawl to be off by one:

1. The Property index page contains 652 `<a class="dd-field-link">`
   entries, but one of them (`CoListOfficeAOR`) is rendered with an
   absolute URL (`https://dd.reso.org/DD2.0/Property/CoListOfficeAOR/`)
   while the other 651 are relative. `wget --mirror` follows relative
   hrefs but treats unconverted absolute hrefs as out-of-scope; the
   page was therefore not fetched on the initial pass.
2. `https://dd.reso.org/DD2.0/lookups/PowerProductionType/Photovoltaics/`
   returned a transient `503 Service Unavailable` during the crawl
   and wget did not retry it (the page is reachable as soon as the
   request is repeated).

Both pages were filled in via a one-shot `curl` into the correct
mirror path. The next time `01_mirror.sh` is run, wget's
`--timestamping` will pick them up if upstream changes.

To make these gap-fills self-healing rather than ad-hoc, a future
revision of `01_mirror.sh` should: (a) parse `crawl.log` for any
non-2xx status and re-fetch each URL once with `curl`, and (b) walk
every fetched resource page and confirm that every `dd-field-link`
href has a corresponding on-disk file, fetching any missing ones.
Both checks are cheap (sub-second) and make the mirror step idempotent.

### 2. URL patterns

Confirmed by pre-flight probe on 2026-05-04:

| Page | URL pattern | Count |
|---|---|---|
| Index | `/DD2.0/` | 1 |
| Resource | `/DD2.0/<Resource>/` | 41 (links counted on the index page) |
| Field | `/DD2.0/<Resource>/<Field>/` | ~1,745 |
| Lookup | `/DD2.0/lookups/<LookupName>/` (lowercase plural; confirmed via field page link) | ~222 |
| Lookup value | `/DD2.0/lookups/<LookupName>/<ValueName>/` (URL-encoded spaces) | ~3,500 |
| xref payload | `/DD2.0/xref/payload/<Payload>/` | small |
| xref property-type | `/DD2.0/xref/property-type/<Type>/` | small |
| xref status | `/DD2.0/xref/status/<Status>/` | small |
| xref version-added | `/DD2.0/xref/version-added/<Version>/` | small |

Notes from the probe:

- `https://dd.reso.org/robots.txt` returns 404. There is no
  `robots.txt`, which is treated as "no restrictions" by wget. We
  still pass `--execute robots=on` and snapshot the response body
  (the styled 404 page) to `_meta/robots.txt` for the record.
- Field pages are well-structured: the Definition prose lives in
  `<div class="dd-definition-callout">`, the metadata cells in two
  `<table class="dd-metadata-table">` tables under the "Details"
  `<div class="dd-metadata-card">`, the adoption block in
  `<div class="dd-usage">`, and the per-lookup-value preview in a
  `<table class="dd-lookups-table">`.
- The "Details" tables are key/value pairs (one `<th>` and one
  `<td>` per row). Cells like `Source Resource` use the em-dash
  character `—` to mean "not set" - the parser must treat `—` as
  empty.
- Field pages also embed the per-value lookup table (with each
  value's definition). The parser will still mirror the dedicated
  `/DD2.0/lookups/<Lookup>/<Value>/` pages because they may carry
  additional context (e.g. version-added, synonyms) that the
  embedded preview truncates.

### 3. Parse

```bash
python3 scripts/02_parse_mirror.py
```

Uses `beautifulsoup4 + lxml`. Walks `mirror/DD2.0/**/index.html` and
emits structured CSVs under `raw/`:

| File | Source pages | Captures |
|---|---|---|
| `resources.csv` | `/DD2.0/<Resource>/index.html` | name, description, field_count, source_url |
| `fields.csv` | `/DD2.0/<Resource>/<Field>/index.html` | every metadata cell from the two tables on the page (Standard Name, Display Name, Group, Simple Data Type, Max Length, Max Precision, Synonyms, Status, BEDES, Lookup Status, Lookup, Property Types, Payloads, Spanish Name, French-Canadian Name, Status Change Date, Revised Date, Added in Version, Source Resource) + the Usage / Adoption block (OrgPct, OrgAdopted, OrgTotal) |
| `field_definitions.csv` | same | full Definition prose verbatim, in a separate file because Definitions can be multi-paragraph and would dominate `fields.csv` width |
| `lookups.csv` | `/DD2.0/<Lookup>/index.html` | once URL pattern is confirmed |
| `lookup_values.csv` | `/DD2.0/<Lookup>/<Value>/index.html` | once URL pattern is confirmed |

CSVs are sorted by `(Resource, StandardName)` (or equivalent) and use
a stable column order. Re-running the parser on the same mirror
produces a byte-identical output (so the only diffs in git come from
real changes upstream).

### 4. Verification gates

`02_parse_mirror.py` ends with hard assertions. The script exits
non-zero on any breach. We do NOT commit a partial / inconsistent
mirror.

Required gates:

1. `resources.csv` has exactly N rows where N = number of resources
   linked from the DD 2.0 index page (currently 41).
2. `fields.csv` row count equals `sum(field_count)` over
   `resources.csv` (currently 1,745).
3. Every row in `fields.csv` has a corresponding non-empty Definition
   in `field_definitions.csv`.
4. Every URL in `_meta/manifest.json` has status 200 (no 4xx, no 5xx,
   no missing entries).
5. Every link found inside any resource page resolves to a fetched
   field page in the mirror.
6. (Once lookup URLs are confirmed:) `lookups.csv` and
   `lookup_values.csv` row counts match the link counts found in
   field pages.

## What's deferred

Phase 1 does NOT do any FK detection, satellite analysis, or DBML
generation. Those are explicit Phase 2, 2.5, and 3 concerns and live
in separate methodology sections that will be added when those phases
land.
