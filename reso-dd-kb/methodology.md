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
in separate methodology sections.

# Methodology - Phase 2 (FK correlation analysis)

## Goal

Read the structured CSVs produced by Phase 1 and emit
`raw/relationships.csv`: a human-reviewable inventory of every
detected foreign key, with per-row evidence (Definition prose / type /
name shape) and a confidence score. Phase 2 does NOT modify the
schema, drop columns, or generate DBML.

## Three signals

The detection engine combines three independent signals. Each lives in
its own intermediate CSV under `raw/_signals_*.csv` so reviewers can
drill into any `relationships.csv` row.

### Signal 1: Definition prose

The dd.reso.org Definition cells contain explicit FK statements that
no xlsx-derived data has ever surfaced. From a manual scan of all 51
fields whose Definition contains the literal phrase "foreign key", we
catalogued five canonical prose patterns. They are all matched
case-insensitively on the cleaned single-line Definition text.

Each pattern's matched substring is recorded verbatim in the
`evidence` column so a reviewer can confirm without re-opening the
page.

| # | Pattern (regex sketch) | Example | Target |
|---|---|---|---|
| 1 | `foreign key (?:relating\|referring\|related)\s+(?:to)?\s+(?:the )?<X>\s+[Rr]esource['\u2019]?s\s+<Y>` | "This is a foreign key relating to the Member Resource's MemberKey." | `<X>.<Y>` |
| 2 | `foreign key\s+(?:relating\|referring\|related)\s+to\s+(?:the )?<Y>\s+(?:K|k)ey of\s+(?:the )?<X>\s+[Rr]esource` | "...is a foreign key relating to the MemberKey of the Member Resource." | `<X>.<Y>Key` |
| 3 | `foreign key\s+(?:to\|from\|in\|of\|relating to\|referring to\|referencing\|related to\|related)\s+(?:the )?<X>\s+[Rr]esource` | "This is a foreign key to the CaravanStop Resource." | `<X>` (column inferred to host's same name) |
| 4 | `self-referencing foreign key\s+(?:relating\|referring)\s+to\s+this\s+resource['\u2019]?s\s+<Y>` | "self-referencing foreign key relating to this resource's OfficeKey." | `<host>.<Y>` |
| 5 | `foreign key\s+from\s+the\s+resource\s+selected\s+in\s+the\s+(?:[A-Z]\w+)\s+field` | "foreign key from the resource selected in the ResourceName field." | polymorphic - target left empty, `notes=polymorphic_via_<field>` |

A sixth complementary pattern catches FK statements that do NOT use
the literal phrase "foreign key" but still name a target resource and
column via a possessive construction. The dd.reso.org corpus has 11
such fields (all `OriginatingSystemID` / `SourceSystemID` -> OUID's
`OrganizationUniqueId`). Without this pattern we'd miss them.

| # | Pattern | Example | Target |
|---|---|---|---|
| 6 | `(?<!foreign key )<X>\s+[Rr]esource['\u2019]?s\s+<Y>` | "The OUID Resource's OrganizationUniqueId of the originating record provider." | `<X>.<Y>` |

Patterns 1, 2, 4, and 6 are *strong* (they name both target resource
and target column). Patterns 3 and 5 are *medium* (target resource
known, target column inferred or polymorphic).

We deliberately do NOT match the noun-phrase "X Resource" appearing
on its own (without "foreign key" or a possessive). Most fields'
Definitions reference their host resource or related resources in
passing without intending an FK declaration; matching that phrase
would flood the output with false positives.

### Signal 2: Type

The DD 2.0 model has two FK-bearing SimpleDataTypes:

- **`Resource`** (89 fields) - a many-to-one FK from the host. The
  target is named in the field's `SourceResource` cell (77 of 89
  populated; the other 12 fall back to a stem-match on the field
  name, see Signal 3, and stay `confidence=medium` if found).
- **`Collection`** (54 fields) - the inverse 1:N. The host carries
  no column; the FK lives on the child resource (named by
  `SourceResource`). Collection rows have `fk_kind=collection_typed`
  and exist so Phase 3 can sanity-check that the matching child-side
  FK was detected.

### Signal 3: Name shape

For every field whose StandardName ends in `Key` or `Id`, derive
`Stem = StandardName[:-3]` (or `[:-2]` for `Id`). Search
`resources.csv` for a target by:

1. Exact match: `Stem == ResourceName`. Strong.
2. Tail match: `Stem.endswith(ResourceName)` (e.g. `OwnerMember`
   -> `Member`). Medium-strength stem match.
3. No match: emit no row from this signal alone.

The name-shape signal is the *weakest* of the three. On its own it
produces `confidence=low` rows; in combination with prose or type it
graduates to `medium` or `high`.

We deliberately do NOT carry over the previous iteration's
`RESOURCE_ALIASES` map (e.g. `ListAgent -> Member`,
`OriginatingSystem -> OUID`). Those bindings are real but they are
*evidenced by the Definition prose* (`ListAgentKey` says "foreign
key relating to the Member Resource's MemberKey" verbatim), so we
prefer to surface them through Signal 1 + the SourceResource cell
rather than baking them into the detector.

## Merge and scoring rules

Each `(host_resource, host_field, target_resource)` triple gets one
row in `relationships.csv`.

`fk_kind` is set to the strongest signal type that contributed to the
row, in priority order:
`resource_typed > collection_typed > prose > name_shape`.

`confidence`:

- **high** - two or more independent signals agree on the same
  target_resource (e.g. SourceResource cell + Definition prose both
  name `Member`).
- **medium** - exactly one strong signal: `Resource` /
  `Collection`-typed *or* explicit Definition prose with a named
  target.
- **low** - exactly one weak signal: name-shape only, or a polymorphic
  pattern (5) where no concrete target is known.

`evidence` is a `|`-joined list of `signal:detail` strings, e.g.
`prose:"foreign key relating to the Member Resource's MemberKey"|type:SourceResource=Member|name:ListAgentKey->Member`.

## Verification gates (hard-fail)

`03_merge_signals.py` exits non-zero if any of:

1. A `relationships.csv` row's `target_resource` is not in
   `resources.csv` (polymorphic rows with empty target_resource are
   exempt).
2. A row's `(host_resource, host_field)` pair doesn't exist in
   `fields.csv`.
3. `fk_kind` is not one of
   `resource_typed | collection_typed | prose | name_shape`.
4. `confidence` is not one of `high | medium | low`.
5. The intermediate `_signals_*.csv` files are missing or unreadable.

## Spot-check protocol

Before committing the Phase-2 output, sample 30 high-confidence and
30 low-confidence rows by hand against the dd.reso.org pages (or
their mirror equivalents under `mirror/DD2.0/`). Record any false
positives or false negatives in the "Spot-check results" subsection
below. Tune the prose patterns or stem regex if high-confidence
precision falls below ~95%.

### Spot-check results (2026-05-05)

Performed against the seeded sample (`random.seed(42)`).

**HIGH-confidence pool: 17 rows (smaller than the requested 30, so
all 17 were audited).** Precision: **17 / 17 = 100%**. Every row
combined an explicit Definition-prose FK statement (P1/P3/P3b/P4)
with a corroborating name-shape match. Examples:
`Property.ListOfficeKey -> Office.OfficeKey`,
`Office.MainOfficeKey -> Office.OfficeKey` (self-FK, P4),
`Prospecting.SavedSearchKey -> SavedSearch.SavedSearchKey`. None
required tuning.

**LOW-confidence pool: 60 rows; sampled 30.** First-pass precision:
~13 / 30 (~43%, expected for a name-only signal). Two systematic
false-positive patterns emerged from the audit:

1. **Host-PK collision via tail-stem.** Stems that end in another
   resource's name by coincidence flagged spurious FKs from the
   host's own primary key, e.g. `SocialMedia.SocialMediaKey` -> Media
   (the field is the host's PK; "SocialMedia" tail-matches "Media")
   and `TeamMembers.TeamMemberKey` -> Member (the field is the host
   PK; "TeamMember" tail-matches "Member").

2. **`OriginatingSystem<X>Key` / `SourceSystem<X>Key` host-key
   pattern.** RESO uses these to mean "the host's own key as it
   appears on the originating / source system" - they are NOT FKs to
   `<X>`. Examples: `Association.OriginatingSystemAssociationKey`,
   `Queue.OriginatingSystemQueueKey`, `Showing.SourceSystemShowingKey`.

Both were fixed in `03c_extract_name_signals.py`:
- Suppress tail_stem matches when the stem matches the host's own
  PK (`stem == host_resource` or `stem == host_resource[:-1]` for
  pluralised hosts like `TeamMembers`).
- Suppress tail_stem matches whose head is `OriginatingSystem` or
  `SourceSystem` and whose target is the host (or its singular).

After the fix, low-confidence rows dropped from 60 to 46 (14 false
positives removed) and the legitimate FKs in the same shape
(`MemberStateLicense.MemberKey -> Member`,
`ShowingAppointment.ShowingKey -> Showing`) were preserved.

**Remaining ambiguities (not defects)**:

- `*NationalAssociationId` fields (e.g.
  `Property.ListAgentNationalAssociationId`,
  `Member.MemberNationalAssociationId`) name-match `Association` via
  the tail. The RESO `Association` resource models the local trade
  association; `*NationalAssociationId` is an external identifier
  (NRDS number) and may or may not be modelled as an FK to that
  resource - the human reviewer decides per row in Phase 2.5.
- Per-resource `*Id` alt-keys (e.g. `Contacts.OwnerMemberID`) point
  at the target's well-known alt-key rather than its `*Key` PK. The
  detector flags the relationship correctly (target_resource =
  Member) but fills `target_field=MemberKey` as a heuristic; the
  evidence column shows the actual semantics. Phase 3 will reconcile.

### Final histogram

| fk_kind          | high | medium | low |
|------------------|-----:|-------:|----:|
| resource_typed   |    0 |     77 |   0 |
| collection_typed |    0 |     48 |   0 |
| prose            |   17 |     38 |   0 |
| name_shape       |    0 |      0 |  46 |

Plus 6 polymorphic rows (`*ResourceRecordKey` + `OpenHouse.ListingKey`)
emitted with `target_resource=""` and `notes=polymorphic`.

Total: 226 relationships covering 226 distinct fields out of 1,745.
The 86% of fields with no FK signal are scalar columns (strings,
numbers, dates, lookups) - exactly as expected.

## What Phase 2 does NOT do

- No column drops, no satellite detection - that's Phase 2.5.
- No DBML emission - that's Phase 3.
- No `RESOURCE_ALIASES` or other hand-curated bridge.
- No write to `mirror/`, `_meta/`, or any Phase-1 file.
