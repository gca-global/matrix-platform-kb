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

# Methodology - Phase 2.5 (satellite / 2NF audit)

## Goal

For every FK on a host resource, find the *carry-along* columns that
duplicate data already reachable through the FK join. Phase 2.5
produces `raw/satellites.csv` - one row per
(host_resource, host_field, candidate_satellite, target_resource,
target_field) pair, with a recommendation in
`{drop_from_host, drop_from_child, keep_both, review}`. Phase 3
consumes the recommendations to build a true 2NF DBML.

## Source-of-truth observation

Manual inspection of the canonical pattern (Property's listing-agent
satellites against the Member resource) confirmed RESO's convention:
each resource prefixes its columns with the resource name (`Member`
has `MemberFirstName`, `MemberMlsId`; `Office` has `OfficeName`,
`OfficeEmail`). The satellite columns on the host echo the FK column's
stem (`ListAgent`, `BuyerOffice`) and replace the resource-name
prefix on the target side. So:

  Property.ListAgentFirstName  <==>  Member.MemberFirstName
  Property.BuyerOfficeName     <==>  Office.OfficeName
  TeamMembers.MemberMlsId      <==>  Member.MemberMlsId

24 of 26 `Property.ListAgent*` columns matched a `Member.Member*`
column in the same shape; 8 of 10 `Property.ListOffice*` matched
an `Office.Office*` column. The two unmatched cases per group are
the bare `Resource`-typed companion (`ListAgent`, `ListOffice` -
the FK's typed inverse, not a satellite) and `URL` columns that
have no Member/Office equivalent.

## Four signals

Each candidate (host_resource, candidate_satellite, target_resource,
target_field) triple is independently evaluated by four signals.
A separate `_satellites_*.csv` carries each signal's raw output so
reviewers can drill in.

### Signal A: name prefix on host

For every FK column `(host, host_field=fk, target)` in
`relationships.csv` with `confidence in {high, medium}` and
non-empty target_resource (polymorphic FKs are skipped), derive
`stem = strip_key_id_suffix(fk)`. Every other column on `host`
whose StandardName starts with `stem` (and is not itself another
FK column or the bare `Resource`-typed companion) is a candidate
satellite. The portion after the stem is the candidate's `suffix`.

### Signal B: child-side column match

For each candidate, attempt to find a column on `target_resource`
named (in priority order):

1. `<target><suffix>` (e.g. suffix=`FirstName`, target=`Member` ->
   `MemberFirstName`)
2. `<target_singular><suffix>` (for pluralised resources like
   `TeamMembers` -> `TeamMember`, `Contacts` -> `Contact`)
3. `<suffix>` (bare; rarely hits in DD 2.0 but kept for safety)

Match scores: exact 1.0; case-folded 0.9; underscore-stripped 0.8;
no match 0. The first non-zero score wins.

### Signal C: Definition similarity

Jaccard on whitespace-tokenised, lowercased, punctuation-stripped
Definition prose with two filter sets removed:

- **Stopwords**: `the, a, of, to, in, for, from, this, that, is, was,
  be, an, on, with, by, as, at, or, and, it, its, if, e.g., i.e.,
  etc., their, which, may, this, has, have`.
- **Role-context tokens**: `listing, list, buyer, co, cobuyer,
  agent, member, office, contact, contacts, team, teams, broker,
  manager, owner, source, originating`. Without this set the
  perfectly-equivalent `Property.ListAgentFirstName` ("The first
  name of the listing agent.") vs `Member.MemberFirstName` ("The
  first name of the member.") would score 0.4 (shared = `{first,
  name}`); with the set removed it scores 1.0 (shared = `{first,
  name}`, union = `{first, name}`).

Calibration on 3 known carry-alongs:

| pair | raw jaccard | role-stripped jaccard |
|---|---:|---:|
| Property.ListAgentMlsId / Member.MemberMlsId | 1.00 | 1.00 |
| Property.ListOfficeName / Office.OfficeName | 0.60 | ~0.80 |
| Property.ListAgentFirstName / Member.MemberFirstName | 0.40 | 1.00 |

Threshold: jaccard >= 0.6 fires Signal C. jaccard in [0.4, 0.6) is
borderline and feeds the `review` recommendation.

### Signal D: type + lookup match

Compare SimpleDataType and Lookup cells between host candidate and
target field:

- both match exactly -> `type_match=1`
- only SimpleDataType matches -> `type_match=0.5`
- mismatch -> `type_match=0`

For Lookup specifically, both empty counts as a match (it just means
neither column is enum-typed).

## Recommendation rules

`recommendation` in `{drop_from_host, drop_from_child, keep_both,
review}`:

- **drop_from_host** - all four signals fire AND jaccard >= 0.6 AND
  type_match >= 0.5. The host column is a verbatim carry-along; the
  FK already provides the join, so the host column violates 2NF.
  Identifier columns (suffix matches `MlsId`, `Id`, `Key`,
  `NationalAssociationId`, `LoginId`) require the stricter jaccard
  >= 0.7 to limit denormalisation false positives.
- **review** - 3 signals fire, OR all 4 fire but jaccard in
  [0.4, 0.6). Common case: short definitions or definitions where
  the host adds context the role-stripping didn't catch.
- **keep_both** - 0..2 signals fire. The columns are unrelated
  despite the prefix.
- **drop_from_child** - reserved for human-supplied overrides via
  `raw/_satellites_overrides.csv` (not auto-emitted in this phase).

## Verification gates (hard-fail)

`04_merge_satellites.py` exits non-zero if any of:

1. A `satellites.csv` row's `(host_resource, host_field)` is not in
   `fields.csv`.
2. A row's `(target_resource, target_field)` is not in `fields.csv`.
3. The row's `(host_resource, fk_column, target_resource)` FK is
   not in `relationships.csv` with `confidence in {high, medium}`.
4. `recommendation` not in
   `{drop_from_host, drop_from_child, keep_both, review}`.

## What Phase 2.5 does NOT do

- Does NOT delete columns from any CSV. It produces a recommendation
  file that Phase 3 consumes after human review.
- Does NOT generate DBML.
- Does NOT touch `mirror/`, `_meta/`, or any Phase-1 file.
- Does NOT create new FKs - it only audits FKs already in
  `relationships.csv`.

## Spot-check results (2026-05-05)

Two seeded samples (random.seed=42, then random.seed=1729 for a
non-overlapping second pass) of `drop_from_host`, plus an audit of
all `review` rows and all `keep_both` rows that name a non-empty
target field.

**`drop_from_host` precision: 30 / 30 = 100%** across both samples.
Every audited row was a verbatim or near-verbatim carry-along
of the target column. Examples:

- `Property.ListAgentMlsId` <-> `Member.MemberMlsId` (jaccard=1.0)
- `Property.BuyerOfficeName` <-> `Office.OfficeName` (jaccard=0.667;
  host adds "representing the buyer", but the column IS the same)
- `Property.CoListAgentVoiceMailExt` <-> `Member.MemberVoiceMailExt`
  (jaccard=1.0; identical content)
- `Property.CoListOfficeName` <-> `Office.OfficeName` (jaccard=0.6)
- `OpenHouse.ShowingAgentMlsID` <-> `Member.MemberMlsId` (jaccard=1.0)

**Tokenization fix during spot-check.** The first pass left `'` and
`-` un-split, so possessives (`buyer's`) and compound role tokens
(`co-agent`, `co-listing`) stayed as opaque tokens that role-context
removal couldn't strip. Definitions like "the first name of the
buyer's co-agent" got jaccard=0.5 against `Member.MemberFirstName`
("the first name of the member") and were sent to `review` instead
of `drop_from_host`. Fixed in `04c_definition_similarity.py` by
splitting on `\s\-'\u2019` and discarding the trailing `s` from
possessive remnants. After the fix:

- 11 buyer's / co-agent / co-listing rows correctly graduated to
  `drop_from_host`;
- 5 high-name + high-type but low-jaccard cases (`Office.OfficeBrokerMlsId`
  -> `Member.MemberMlsId`, `Property.BuyerTeamName` -> `Teams.TeamName`,
  etc.) were lifted from `keep_both` -> `review` so the human
  reviewer sees them.

**Final histogram (208 candidates across 42 distinct FKs):**

| recommendation     |  count |
|--------------------|-------:|
| drop_from_host     |    134 |
| keep_both          |     65 |
| review             |      9 |

Of the 65 `keep_both` rows, 60 have an empty `target_field` (Signal
B unmatched - the host has a `*URL` or `*StateLicense` column the
target doesn't carry, which is correct semantics) and 5 are
identifier columns where the FK already implies the join but the
host column has been intentionally given a different role
(`MainOfficeMlsId`, `OfficeBrokerMlsId` cases) - we did promote 3
of these to `review` in the rule fix above; the remaining 5 are
where Signal C still rejected the pair on prose grounds.

The 9 `review` rows split:
- 4 borderline-jaccard rows (extra context like "for the caravan
  stop" or "scheduled to access the property") that a reviewer
  would convert to drop;
- 5 name+type-match-but-prose-differs rows (the
  `OfficeBrokerMlsId` family) that need a deliberate human call.

Phase 3 should consume only the `drop_from_host` rows after a human
sign-off pass, treating `review` as a queue and `keep_both` as
"leave alone".

## What Phase 2 does NOT do

- No column drops, no satellite detection - that's Phase 2.5.
- No DBML emission - that's Phase 3.
- No `RESOURCE_ALIASES` or other hand-curated bridge.
- No write to `mirror/`, `_meta/`, or any Phase-1 file.

# Methodology - Phase 3 (DBML build)

## What Phase 3 does

Phase 3 reads the Phase-1 raw CSVs, the Phase-2 `relationships.csv`,
and the Phase-2.5 `satellites.csv`, and emits the canonical DBML model:

- `wiki/dbml/canonical.dbml` - 41 `Table` blocks, FK `Ref` lines, and
  `// polymorphic FK` comments.
- `wiki/dbml/lookups.dbml` - 99 `Enum` blocks for single-value lookups
  + reference comments for multi-value-only and open lookups.

Phase 3 is a pure code-gen pass: every Table / Column / Ref / Note /
Enum traces back to a row in the input CSVs. The generator does NOT
perform implicit FK detection, does NOT consult any alias map, and
does NOT make schema decisions - except for the per-resource
`PK_OVERRIDES` table (9 entries) where the PK column's name does not
match the obvious `<Resource>Key` shape.

## Dependency chain

```
mirror/                          (Phase 1)
  -> raw/resources.csv,
     raw/fields.csv,
     raw/field_definitions.csv,
     raw/lookups.csv,
     raw/lookup_values.csv

raw/_signals_*.csv               (Phase 2)
  -> raw/relationships.csv

raw/_satellites_*.csv            (Phase 2.5)
  -> raw/satellites.csv

raw/{resources,fields,field_definitions,lookups,lookup_values,
     relationships,satellites}.csv
  -> wiki/dbml/{canonical,lookups}.dbml          (Phase 3)
```

Phase 3 does not write under `mirror/`, `_meta/`, or `raw/`.

## Type mapping (RESO SimpleDataType -> DBML)

| SimpleDataType        | DBML type                                    |
|-----------------------|----------------------------------------------|
| `String`              | `varchar` (or `varchar(<MaxLength>)` if MaxLength is in (0, 4000)) |
| `Number`              | `int` (widened to `double` if `MaxPrecision > 0`) |
| `Boolean`             | `bool`                                       |
| `Timestamp`           | `timestamp`                                  |
| `Date`                | `date`                                       |
| `String List, Single` | `<lookup>` enum reference (when the lookup has a closed value list); else `varchar` with note `open: jurisdiction-defined` |
| `String List, Multi`  | `varchar` with note `multi: <lookup>` (DBML enums are scalar; the multi-value list is documented in the column note) |
| `Resource`            | (no scalar column emitted; the Ref attaches to the natural scalar carrier on the host) |
| `Collection`          | (no scalar column emitted; recorded as a `// inverse 1:N` comment above the host table) |

Each column carries a Note string of the form
`<StandardName> | <first sentence of Definition> | type=<SimpleDataType> | max_len=<MaxLength> | lookup=<Lookup>`
with NULL/empty fragments dropped.

## FK policy

Source: `raw/relationships.csv` (the Phase-2 deliverable).

| Row in relationships.csv               | Phase 3 emission                              |
|----------------------------------------|-----------------------------------------------|
| `confidence = high`                    | `Ref:` line                                   |
| `confidence = medium`                  | `Ref:` line                                   |
| `confidence = low`                     | skipped (too noisy without human review)      |
| `fk_kind = collection_typed`           | skipped (it is the inverse of an FK already declared on the child) |
| `notes = polymorphic`                  | `// polymorphic FK ...` comment               |
| `target_resource = ""` (poly P5/P5b)   | `// polymorphic FK ...` comment               |

For `fk_kind = resource_typed` (the host column is `Resource`-typed
with no scalar value), Phase 3 picks a sibling scalar carrier on the
host of the form `<base>Id` / `<base>ID` / `<base>Key` BUT only when
the candidate's Definition mentions the target resource name OR the
target's PK column name. This guards against attaching the FK to an
upstream local-key column (e.g. `Property.SourceSystemKey` is the
upstream system's local record key, NOT a UOI reference - the actual
UOI ref lives on `Property.SourceSystemId` whose Definition explicitly
names "OrganizationUniqueId").

When multiple Refs from the same source column would point at
different columns on the same target table (e.g. OUID has both
`OrganizationUniqueId` (UOI) and `OrganizationUniqueIdKey` (PK)), the
generator collapses to a single Ref aimed at the target's PK.

`target_field` is resolved per row via this priority order in the
merge step (`03_merge_signals.py`):

1. **host_field is a `*Key`/`*Id` column AND a column with the same
   name exists on the target** (and target != host) - the same-named
   column is the join column. This is what makes
   `PropertyRooms.ListingKey -> Property.ListingKey` resolve correctly
   even when the prose says "Property Resource's SourceSystemKey".
2. Strong prose pattern (P1/P2/P4/P6) named the column verbatim AND
   that column exists on the target.
3. Name-signal PK column (`<Target>Key`) AND it exists on the target.
4. Type-signal heuristic `<Target>Key` AND it exists on the target.
5. Verbatim prose-strong column even if not in the target schema (so
   the reviewer can see the hint in the evidence column).

## Column-drop and review policy

Source: `raw/satellites.csv` (the Phase-2.5 deliverable).

| recommendation     | Phase 3 action                                          |
|--------------------|---------------------------------------------------------|
| `drop_from_host`   | column omitted from the host's table                    |
| `review`           | column kept, prefixed with a `// REVIEW: <reason>` line |
| `keep_both`        | column kept silently                                    |
| `drop_from_child`  | not implemented in this phase (overrides only)          |

In addition to the satellites policy, columns whose `SimpleDataType`
is `Resource` or `Collection` have no scalar value and are never
emitted as table columns - their FK contribution is captured in the
Refs / inverse-1:N comments instead.

## File split

The model is split into two files for tooling compatibility (the
previous iteration used the same split, so existing dbml-renderers
keep working):

- `canonical.dbml` - tables, refs, polymorphic comments. Has its own
  `Project reso_canonical_dd_2_0` block.
- `lookups.dbml` - enum blocks + open/multi-only lookup comments. Has
  its own `Project reso_canonical_dd_2_0_lookups` block.

Identifiers are snake_case (table = `snake(ResourceName)`, column =
`snake(StandardName)`, enum = `snake(LookupName)`).

## Verification gates

`scripts/05_emit_dbml.py` runs six hard-fail gates before exit:

1. Each `Table` block declared exactly once.
2. The number of declared tables equals the number of rows in
   `resources.csv`.
3. Every `Ref:` source/target table is one of the declared tables.
4. Every `Ref:` source/target column exists in its declared table.
5. Every Enum referenced from a column is declared in `lookups.dbml`.
6. No `(resource, field)` from `fields.csv` that survived the
   drop-and-skip policy is silently missing from the DBML output.

## Spot-check (Property, Member, Office, OpenHouse, OUID)

| table       | cols | pk                              | out-refs | in-refs | review |
|-------------|-----:|---------------------------------|---------:|--------:|-------:|
| property    |  512 | listing_key                     |       12 |      10 |      2 |
| member      |   78 | member_key                      |        3 |      24 |      0 |
| office      |   65 | office_key                      |        5 |       9 |      3 |
| open_house  |   23 | open_house_key                  |        1 |       0 |      0 |
| ouid        |   42 | organization_unique_id_key      |        2 |      20 |      0 |

All Refs in the spot-check resolve to existing tables and columns;
all PKs match their `dd.reso.org` page; all `// REVIEW` comments
correspond to a `recommendation = review` row in `satellites.csv`.

## Regression diff vs the previous iteration (commit 107709d)

|                       | previous | new |  delta |
|-----------------------|---------:|----:|-------:|
| `Table` blocks        |       41 |  41 |    0   |
| `Ref:` lines          |      108 |  64 |  -44   |
| `Enum` blocks         |       99 |  99 |    0   |

The Ref delta is the visible cost of removing the
`RESOURCE_ALIASES` map and refusing implicit FK detection inside the
generator:

- The previous iteration mapped role-named `*OriginatingSystemKey` /
  `*SourceSystemKey` columns to OUID via curated alias. The new
  pipeline rejects those because the Definition prose for those
  columns describes them as upstream-system *local* record keys
  ("the system key, a unique record identifier, from the originating
  system"), not as UOI references. The actual UOI references live
  on `*OriginatingSystemId` / `*SourceSystemId` (whose Definition
  text names "OrganizationUniqueId"), and those are captured.
- A handful of other lost Refs (`Showing.OriginatingSystemListingKey
  -> Property`, etc.) belong to the same upstream-local-key family.
- The previous iteration also produced 4 wrong Refs from PropertyXxx
  sub-resources to `Property.SourceSystemKey` instead of the natural
  PK `Property.ListingKey`; the new merge rule (host-name = target-PK
  preference) fixes those.

The lost Refs are recoverable by either (a) extending the Phase-2
prose patterns to match a wider set of UOI phrasings, or (b)
introducing a small, declared alias overlay file under `raw/`. Both
options are deferred to a future revision; the current state favours
precision over recall and remains 100 % derived from prose evidence.

## What Phase 3 does NOT do

- No alias map. No implicit FK detection.
- No write to `mirror/`, `_meta/`, or `raw/*.csv`.
- No human-curated overrides outside of `PK_OVERRIDES` (which is in
  the script, not in a CSV - because resource PKs do not change in
  RESO DD 2.0).
- No JSON Schema, no Avro, no SQL DDL. DBML only.

# Methodology - Phase 4 (agent-consumption docs)

## What Phase 4 does

Phase 4 adds an agent-consumption layer on top of the Phase-1/2/2.5/3
artifacts so that any coding agent (Lovable, Cursor, Copilot, ...)
reading this directory cold can answer "which table / field / enum
value should I use?" without having to parse CSVs or DBML themselves.

Outputs:

- `USAGE.md` (single human-curated narrative entry doc, stable across
  refreshes).
- `wiki/agent-docs/_index.md` (generated index of the 41 resources +
  pointers to `lookups.md` / `relationships.md`).
- `wiki/agent-docs/resources/<snake>.md` (41 generated per-resource
  pages with fields, FKs, satellite-audit notes).
- `wiki/agent-docs/lookups.md` (single generated file, 222 sections).
- `wiki/agent-docs/relationships.md` (single generated file:
  committed Refs parsed from `canonical.dbml`, plus Phase-2 detected
  signals, polymorphic FKs, inverse 1:N, low-confidence).

## Why a separate generated layer rather than just the DBML

DBML is great for tooling but verbose for an LLM. The agent docs are
markdown, table-shaped, deterministic, and grep-friendly. The DBML and
the CSVs remain the source of truth; the agent docs are a derived view
optimised for "an LLM is reading you cold".

## Dependency chain

```
mirror/                          (Phase 1)
  -> raw/*.csv                   (Phase 1/2/2.5)
  -> wiki/dbml/*.dbml            (Phase 3)
  -> wiki/agent-docs/**          (Phase 4)
```

Phase 4 does NOT modify any earlier-phase output and does NOT make
any schema decisions of its own (`PK_OVERRIDES` is duplicated from
`scripts/05_emit_dbml.py` so the docs cite the same chosen PK).

## Page templates

### Per-resource (`resources/<snake>.md`)

| Section                             | Source                                                |
|-------------------------------------|-------------------------------------------------------|
| H1 + 1-line summary                 | `raw/resources.csv` (`Description`)                   |
| PK + override note                  | `PK_OVERRIDES` dict + `raw/fields.csv`                |
| Fields table                        | `raw/fields.csv` + `raw/field_definitions.csv` + `raw/satellites.csv` |
| Foreign keys OUT                    | `wiki/dbml/canonical.dbml` (parsed Refs)              |
| Foreign keys IN                     | `wiki/dbml/canonical.dbml` (parsed Refs)              |
| Inverse 1:N                         | `raw/relationships.csv` (`fk_kind=collection_typed`)  |
| Polymorphic FKs                     | `raw/relationships.csv` (`notes=polymorphic`)         |
| Phase 2.5 satellite audit           | `raw/satellites.csv`                                  |

The fields table flags column shows: `pk`, `-> target.col` (committed
FK), `[REVIEW]`, `[dropped: satellite of <fk>]`, `[Resource]` /
`[Collection]`. Dropped columns ARE listed (with the marker) so the
agent sees what RESO defines but the canonical model omits.

### `lookups.md`

One TOC table + one anchored section per lookup with kind
(`closed-SV` / `closed-MV` / `open`), source name, value count,
referenced columns, and the full value table
(`StandardValue | LegacyODataValue | Definition`).

### `relationships.md`

Four sections:
1. **Committed Refs (in DBML)** - parsed from `wiki/dbml/canonical.dbml`.
   This is the source of truth for "what FKs exist in the canonical
   model".
2. **Phase-2 detected signals** - wider net from `raw/relationships.csv`;
   includes `resource_typed` rows that Phase 3 anchored to a scalar
   sibling (and therefore folded into a single committed Ref).
3. **Polymorphic FKs** - `notes=polymorphic`.
4. **Inverse 1:N** - `fk_kind=collection_typed`.
5. **Low-confidence** - shown for transparency; NOT in DBML.

## Naming and anchors

All identifiers in agent-docs are snake_case (matches the DBML).
Markdown headings use snake_case so GFM anchors are stable across
refreshes (e.g. `## property_type` -> `#property_type`). The fields
table on a resource page deep-links lookups via
`[../lookups.md#<snake_lookup_name>]`.

## Verification gates

`scripts/06_emit_agent_docs.py` runs five hard-fail gates before exit:

1. One resource page per row in `resources.csv` (count match).
2. Every Enum referenced in `canonical.dbml` has a section in
   `lookups.md`.
3. Every internal markdown link from emitted pages resolves to a
   declared file or a declared anchor in this output set.
4. Every `(host, candidate_satellite)` row in `satellites.csv` with
   recommendation in `{drop_from_host, review}` is listed on its
   host's resource page (transparency gate; the dropped column is
   not silently hidden).
5. `_index.md` links every emitted page exactly once.

## Sizes (as of the first emission)

| File                                | Bytes / lines      |
|-------------------------------------|--------------------|
| `USAGE.md`                          | ~9 KB              |
| `wiki/agent-docs/_index.md`         | ~7 KB              |
| `wiki/agent-docs/lookups.md`        | ~470 KB / 6,682 lines |
| `wiki/agent-docs/relationships.md`  | ~28 KB / 261 lines |
| `wiki/agent-docs/resources/*.md`    | 41 files; 1.3 KB to 18 KB; `property.md` is the largest at 8.4 KB |

`lookups.md` is the only large file. We chose a single file rather
than per-lookup files because (a) consuming agents grep / CMD-F
faster within one file, (b) GFM anchors keep deep-linking from
resource pages stable, and (c) 470 KB is comparable to
`canonical.dbml` (270 KB) and well within an LLM's read budget.

## What Phase 4 does NOT do

- No write under `mirror/`, `_meta/`, `raw/`, or `wiki/dbml/`.
- No FK detection or schema decisions of its own.
- No project-specific opinions. `reso-dd-kb/` documents the RESO DD
  2.0 model only; "we always use ListAgentKey for the showing agent"
  type rules belong in the consuming project's docs.
