# RESO DD methodology — one-page primer

Read this before opening any `wiki/resources/<Resource>.md`. Five
concepts cover ~95% of "how do I model X in RESO?" questions.

---

## 1. Naming

- **Resources** are PascalCase singular (sometimes plural for
  collections): `Property`, `Member`, `Office`, `Teams`, `OpenHouse`,
  `PropertyRooms`, `PropertyUnitTypes`, `PropertyPowerProduction`,
  `Contacts`, `HistoryTransactional`, `InternetTracking`, ...
- **Fields** are PascalCase: `ListingId`, `OwnerName`, `BuilderName`,
  `RoomType`. The wire-format API also uses PascalCase verbatim;
  Atlas's database mirrors this in `snake_case` per Postgres
  convention (`owner_name`, `builder_name`).
- **Lookups** carry a `LookupName` and have a stable
  `StandardLookupValue`. There are also legacy OData values; prefer
  the standard form.
- **Atlas-custom fields** (e.g. `LifecycleState`) are flagged with
  `source = atlas_custom` in `raw/field_descriptions.csv` and have no
  upstream URL. They exist only inside Atlas to power UI / ETL logic.

## 2. Keys + relationships

RESO uses two parallel id systems:

| Suffix | Purpose | Uniqueness | Example |
|---|---|---|---|
| `*Key` | system-unique surrogate id | global within originating system | `ListingKey`, `MemberKey`, `OfficeKey`, `RoomKey` |
| `*MlsId` / `*Id` | well-known business id | unique per OriginatingSystem | `ListingId` (MLS number), `MemberMlsId`, `OfficeMlsId` |

Foreign keys reference the `*Key` form: `Property.ListAgentKey →
Member.MemberKey`. Use the `*Key` for joins; show the `*MlsId` to
humans.

**Owner / Builder are NOT keys.** RESO models the property owner and
the builder as **scalar text fields on Property** (`OwnerName`,
`OwnerPhone`, `BuilderName`, `BuilderModel`). There is no
`OwnerKey` / `BuilderKey`. To resolve "all listings owned by X",
match on text. This is intentional: the owner is private CRM data
(see `Contacts` resource) and is only optionally backed by a
contact record.

## 3. Lookups

Every lookup field carries:

- a `LookupName` (e.g. `OccupantType`, `RoomLevel`, `PropertyType`),
- one or more rows in `raw/lookups.csv` with `StandardLookupValue` +
  `Definition`,
- a `LookupStatus` declaring **closed** (only listed values allowed)
  or **open** (jurisdictions may extend).

Do not invent values. If you need a value RESO does not have, file a
RESO Change Proposal first; in the interim, store the value in the
nearest `*Remarks` field.

## 4. Lifecycle (Property only)

Two RESO fields, plus one Atlas-derived bucket, classify a listing's
operational state:

| Field | Source | Purpose |
|---|---|---|
| `StandardStatus` | RESO DD | normalized MLS status (`Active`, `Pending`, `Closed`, `Withdrawn`, `Expired`, `Canceled`, `Hold`, `Incomplete`, `Delete`) |
| `MlsStatus` | RESO DD | feed-native status before normalization (free-form) |
| `LifecycleState` | **Atlas-custom** | three-bucket UI chip: `Listing` / `Marketing` / `Rent`. Computed from `ListingService`, `ListingAgreement`, `LeaseConsideredYN`, `SaleConsideredYN`. |

`LifecycleState` is **not** RESO; it exists only to drive the operator-
facing chip filter on the Atlas listings index. Always cite as
"Atlas-custom" when surfacing it.

## 5. Canonical DBML: how it was cooked

The canonical DBML (`wiki/dbml/reso-2.0-canonical.dbml`) is **2NF
normalized**. It is generated end-to-end by
[`scripts/build_reso_canonical_dbml.py`](scripts/build_reso_canonical_dbml.py)
from `raw/fields.csv`, `raw/lookups.csv`, and
`raw/field_metadata.csv`. This section explains every transformation
the script applies, in the order it runs them.

### Inputs

| File | Source | Used for |
|---|---|---|
| `raw/fields.csv` | parsed from `RESO_Data_Dictionary_2.0.xlsx` (`Fields` sheet) | every column, FK, lookup link |
| `raw/lookups.csv` | parsed from `RESO_Data_Dictionary_2.0.xlsx` (`Lookups` sheet) | distinct `LookupName` set -> one ref table per lookup |
| `raw/field_metadata.csv` | scraped from `dd.reso.org/DD2.0/<Resource>/<Field>/` | `Org%` adoption + structured KV in column Notes |

The xlsx is the upstream RESO truth. `dd.reso.org` adds adoption
metrics RESO publishes on the live site but not in the spec file.

### Step 1 — Group fields by Resource and derive each PK

`load_fields()` reads `fields.csv` and groups rows by `ResourceName`.
For every Resource we derive the primary key:

- **`PK_OVERRIDES`** (16 entries) covers Resources where the canonical
  PK is not `<Resource>Key` — e.g. `Property` -> `ListingKey`,
  `Contacts` -> `ContactKey`, `OUID` -> `OrganizationUniqueIdKey`,
  `PropertyRooms` -> `RoomKey`, `Teams` -> `TeamKey`.
- Otherwise: the field named `<Resource>Key` is the PK
  (e.g. `Member.MemberKey`).

These PKs become the `[pk]` columns in DBML and the FK targets for
every relationship downstream.

### Step 2 — Detect satellite fields (2NF normalization)

`compute_satellites(by_res, resource_pks)` walks each host resource
`H` and every Resource-typed field `F` on `H` (rows where
`SimpleDataType = "Resource"`). For each `F` we know:

- `target = SourceResource` (e.g. `Member`)
- `tkey = TargetResourceKey` (e.g. `ListAgentKey`)

We compute the **satellite prefix** = `tkey` with the trailing
`Key` / `ID` / `Id` stripped (e.g. `ListAgent`, `OriginatingSystem`).
A field `g` on `H` is a satellite of `F` iff:

- `g.SimpleDataType` is **not** `Resource` (forward FKs handled below);
- `g.StandardName` starts with the satellite prefix, with an uppercase
  letter immediately after (word boundary so `Contact` doesn't match
  `ContactListingsKey`);
- `g.StandardName` is **not** the host's own PK;
- `g.StandardName` is **not** another FK column on `H` (i.e. not the
  `TargetResourceKey` of some other Resource-typed sibling).

A column matched by multiple FKs is dropped once. The result: 215
satellites across 16 hosts. They split into two flavours, both dropped
uniformly:

1. **True denormalizations** — the column also exists on the target
   (`Property.ListAgentEmail` mirrors `Member.MemberEmail`). Reachable
   via the FK join.
2. **Auxiliary identifiers / relationship attributes** — the column
   does not exist on the target and would belong in a junction table
   in a fully relational model
   (`Property.OriginatingSystemKey`,
   `ContactListings.ListingViewedYN`).

Full per-host list of every drop:
[`wiki/dbml/2nf-satellite-drops.md`](wiki/dbml/2nf-satellite-drops.md).
The same list is reproduced as a comment header inside the canonical
DBML.

### Step 3 — Detect foreign keys (four passes)

For every host `H`, the script emits DBML `Ref:` lines from four
orthogonal signals.

**Pass 1 — Resource-typed siblings (primary signal).** For each row
on `H` with `SimpleDataType = "Resource"`, emit
`Ref: H.<TargetResourceKey> > <SourceResource>.<PK>`. The scalar FK
column itself (`ListAgentKey` etc.) is materialised by another row in
`fields.csv`; this pass only emits the relationship edge.

**Pass 2 — Definition prose, "foreign key relating to ...".** Some
`*Key` fields lack a Resource-typed sibling but their Definition text
says `"This is a foreign key relating to the Member Resource"`. The
regex
`r"(?:foreign key (?:relating|related) to|relates to|relating to|references?)\s+(?:the\s+)?(\w+)\s+[Rr]esource"`
captures the target Resource name. Emit a Ref to `<Target>.<PK>`.

**Pass 3 — Definition prose, `<Resource>'s <field>`.** Variant
phrasing where the Definition names the target inline (e.g. "the OUID
Resource's OrganizationUniqueId"). Lower priority than pass 2.

**Pass 4 — Name-shape `<Word>Key`.** Field name ends in `Key` and the
prefix is itself a known Resource (or its singular form for plural
Resources like `Contacts` -> `Contact`, `Teams` -> `Team`,
`Rules` -> `Rule`). Lowest priority; only fires when no prose was
found.

Passes 2-4 are filtered against the satellite drop set from step 2 (no
point Ref-ing a column we won't render). They land in a dedicated
`// ---- Extra FKs ----` footer block, each tagged with the detection
signal so reviewers can verify the heuristic. Full list:
[`wiki/dbml/extra-fks.md`](wiki/dbml/extra-fks.md).

### Step 4 — Type lookup columns and emit enums in a companion file

Lookups split three ways based on how they are used by fields:

| Bucket | Count | DBML treatment |
|---|---:|---|
| Referenced by ≥1 `String List, Single` column | **99** | `Enum <snake_name> { ... values ... }` block in `wiki/dbml/reso-2.0-lookups.dbml`; the host column in the main canonical DBML is typed as `<snake_name>` |
| Referenced only by `String List, Multi` columns | **94** | NOT enum-able (DBML's single-column type system can't model array membership); host column stays `varchar` and tags `(multi-value; column stores comma-separated codes)` in its Note; LookupName listed at the bottom of the lookups DBML for discoverability |
| Open lookups (declared by RESO, no closed value list in `raw/lookups.csv`) | **29** | NOT enum-able (no closed value set); host column stays `varchar` and tags `(open: jurisdiction-defined; no closed value list)` in its Note; LookupName listed at the bottom of the lookups DBML |
| **Distinct LookupNames referenced by fields** | **222** | 99 + 94 + 29 reconciles |

The open lookups cover jurisdiction-defined value sets: `City`,
`PostalCity`, `CountyOrParish`, `MlsStatus`, `MediaStatus`,
`OrganizationType`, `AOR`, `ElementarySchool`, `HighSchool`,
`MiddleOrJuniorSchool`, `*District`, `MLSAreaMajor`, `MLSAreaMinor`,
`StreetSuffix`, `RuleType`, `SavedSearchType`,
`MemberMlsSecurityClass`, `TeamImpersonationLevel`,
`SyndicateAgentOption`, `ImageSizeDescription`,
`SearchQueryExceptions`, `BuildingFeatures`, `Disclosures`,
`DocumentsAvailable`, `GreenLocation`, `IrrigationSource`,
`ShowingDays`. Each MLS / jurisdiction extends them locally.

#### Why the lookups live in a separate DBML file

DBML enums must be declared at the top level of a DBML file. Bundling
all 99 enums alongside the 41 Resource tables inflated the canonical
file to ~5,000 lines / ~488 KB, beyond what `dbdiagram.io` and similar
tools render comfortably. Splitting them out drops the main file to
~1,800 lines while preserving full enum value sets in a co-loadable
companion:

- `reso-2.0-canonical.dbml` — 41 Resource tables + cross-resource Refs.
  Single-value lookup columns are typed as the snake_case LookupName
  (e.g. `property.standard_status standard_status`). When this file is
  loaded standalone in a DBML viewer, the type renders as an opaque
  custom type — the name itself serves as documentation.
- `reso-2.0-lookups.dbml` — 99 `Enum <snake_name> { ... }` blocks
  carrying every RESO standard value (with `legacy=ComingSoon` style
  Notes for any value whose LegacyODataValue differs from the
  StandardLookupValue). Multi-word values like `Active Under Contract`
  are double-quoted per DBML grammar.

DBML viewers loaded with both files (e.g. `dbdiagram.io` "Import file"
twice into the same diagram) resolve the column type to a real
validated enum. Atlas's `build_atlas_target_dbml.py` is free to choose
its own representation (today it inherits the canonical's choice; this
may change as a separate decision).

#### Why not emit lookup `Ref:` lines

In the previous reference-table design, every single-value lookup
column emitted `Ref: host.col > lookup_name.code`. With enums, the
type-system *is* the constraint — no Ref line is needed. The main
DBML's `Ref:` count drops from 259 to 71 (only cross-resource
relationships remain), and the noise-to-signal ratio improves.

Zero orphan enums: every enum in the lookups DBML has at least one
referencing column in `raw/fields.csv`.

### Step 5 — Skip Collection-typed inverse references

`SimpleDataType = "Collection"` rows (`Property.Media`,
`Property.OpenHouse`, `Property.Rooms`, ...) are inverse 1:N
relationships — the FK column lives on the child resource, not on the
host. They are **not** rendered as host columns. Each host table
emits an `// Inverse 1:N (Collection-typed in RESO; FK lives on
child)` comment listing them so the relationship is documented; the
forward FK from child to host is emitted by passes 1-4 on the child.
54 Collection rows handled this way.

`collection_inverse_targets()` resolves each Collection field's child
target via `SourceResource` first (set on 48/54 rows) and falls back
to matching `StandardName` against known Resource names for the
remaining 6 (`OpenHouse.HistoryTransactional` -> `HistoryTransactional`
resource, etc.). Zero unresolved.

### Step 6 — Render columns and per-column Notes

Non-satellite, non-Collection scalar fields are rendered as DBML
columns. The DBML type comes from `TYPE_MAP`:

| RESO `SimpleDataType` | DBML type |
|---|---|
| `String` | `varchar(<SugMaxLength>)` |
| `String List, Single` / `String List, Multi` | `varchar` |
| `Number` | `numeric` |
| `Boolean` | `boolean` |
| `Date` | `date` |
| `Timestamp` | `timestamp` |

Each column carries a single-line `Note:` with `StandardName`,
`Definition` (truncated to 160 chars), `type=<SimpleDataType>`,
`lookup=<Name>` if applicable, length / precision constraints, and
`adoption org=<Org%> (n/N)` from `field_metadata.csv`.

### Step 7 — Output

Four files are written by a single invocation of
`scripts/build_reso_canonical_dbml.py`:

1. `wiki/dbml/reso-2.0-canonical.dbml` (~1,800 lines) - the schema
   itself: 41 Resource tables + 71 cross-resource Refs (Resource-typed
   siblings + extra FKs from prose / name-shape passes). Single-value
   lookup columns are typed as the snake_case LookupName.
2. `wiki/dbml/reso-2.0-lookups.dbml` (~2,200 lines) - the lookup
   companion: 99 `Enum` blocks with every RESO standard value, plus
   commented sections listing the 94 multi-only and 29 open lookups
   that cannot be enums.
3. `wiki/dbml/2nf-satellite-drops.md` - human-readable enumeration of
   every dropped satellite, grouped by host + FK + target.
4. `wiki/dbml/extra-fks.md` - human-readable enumeration of every FK
   discovered by passes 2-4.

The main DBML's header carries the satellite + extras counts and links
to the companion files; it does NOT re-inline the per-host satellite
list (that's what `2nf-satellite-drops.md` is for). This keeps the
schema small enough for any DBML viewer.

### What this leaves to operational stores

The wiki Resource pages (`wiki/resources/*.md`) still document
satellites and Collection fields because they are part of the
published RESO 2.0 spec — useful when an LLM is asked "what does RESO
say about Property.ListAgentEmail?".
Operational/denormalized stores (Atlas) may opt back in to a chosen
subset of satellites for query performance via
[`scripts/build_atlas_target_dbml.py`](scripts/build_atlas_target_dbml.py).
The canonical model stays clean.

## 6. Reading Org%

Every Field row in `wiki/resources/<Resource>.md` carries one adoption
percentage from RESO certification stats:

| Column | Meaning | Source |
|---|---|---|
| `Org%` | % of organizations that emit this field at least once | dd.reso.org page "Usage — Adoption XX% n of N Organizations" |

Read it as **adoption pressure**, not data quality. `Org% > 50%` means
"most certified organizations publish this field at least once" — a
strong signal that it is a safe canonical to depend on. `Org% < 10%`
means "nearly nobody publishes this" — usually a niche or new field.

`n / N` lives in `raw/field_metadata.csv` (`OrgAdopted` / `OrgTotal`).
We carry the percentage in the Resource pages because that is the
question the agent gets asked; the absolute counts stay in the raw
CSV for forensic answers.

> Historical note: ddwiki.reso.org used to also publish a `Sys%`
> (per-System) breakdown. RESO retired ddwiki and migrated to
> dd.reso.org, which only exposes per-Organization adoption. Older
> commits in this KB still reference `Sys%`; current files do not.

## TL;DR for the LLM

1. Read this page to remember naming, keys, lookups, lifecycle, Org%.
2. Open `wiki/resources/<Resource>.md`.
3. Find the field row in the Fields table.
4. Cite using the dd.reso.org URL in the right-most `Source` column when prose context is needed.
5. Never invent a field or a lookup value.
