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

## 5. Satellite fields, 2NF, and FK detection

RESO 2.0 ships hundreds of fields that are *satellites* of a foreign
key on the same row. The clearest example: `Property` carries
`ListAgentKey` (FK → `Member.MemberKey`) **and** `ListAgentEmail`,
`ListAgentFullName`, `ListAgentMlsId`, `ListAgentDirectPhone`, etc. —
roughly 25 columns whose value depends on `ListAgentKey`, not on
`Property`'s PK (`ListingKey`). That is a 2NF/3NF violation.

The canonical DBML (`wiki/dbml/reso-2.0-canonical.dbml`) **drops these
satellites**. Across the 41 RESO Resources, 215 satellite fields are
removed in favour of the FK alone. The file's header lists every
dropped field grouped by host + FK. To re-derive a satellite value at
read time, JOIN through the FK column shown next to the host.

Two flavours of satellite exist; both are dropped uniformly:

1. **True denormalizations** — the column also exists on the target
   resource (`Property.ListAgentEmail` mirrors `Member.MemberEmail`).
   Reachable via the FK join.
2. **Auxiliary identifiers / relationship attributes** — the column
   does not exist on the target and would belong in a junction table
   in a fully relational model. Examples:
   `Property.OriginatingSystemKey` ("this listing's identifier in the
   originating system"), `ContactListings.ListingViewedYN` (a
   property of the (Contact, Listing) pair, not of `Property`).
   Currently no junction table is materialised; capture these in your
   operational store if you need them.

### FK signals beyond Resource-typed siblings

Most FKs come from `SimpleDataType = Resource` rows in
`raw/fields.csv` (e.g. `Property.ListAgent` carries `SourceResource =
Member` + `TargetResourceKey = ListAgentKey`). But ~15 FKs lurk in two
other places:

- **Definition prose** like *"This is a foreign key relating to the
  Member Resource's MemberKey"* on plain scalar `*Key` fields
  (e.g. `Media.ChangedByMemberKey`, `OfficeAssociation.OfficeKey`).
- **Name-shape `<Word>Key`** where `<Word>` is itself a Resource name
  (or its singular form for `Contacts`/`Teams`/`Rules`)
  (e.g. `MemberAssociation.AssociationKey`, `ShowingAppointment.ShowingKey`).

The build script picks both up and emits the corresponding DBML `Ref:`
in a separate `// ---- Extra FKs ----` footer block, tagged with the
detection signal so reviewers can verify the heuristic.

### Collection-typed fields are inverse references, not columns

`SimpleDataType = Collection` rows (`Property.Media`,
`Property.OpenHouse`, `Property.Rooms`, `Contacts.ContactsSocialMedia`,
…) are *inverse* 1:N relationships — the FK column lives on the child
resource, not on the host. They are **not** rendered as host columns
in the canonical DBML. Each host table emits an `// Inverse 1:N`
comment listing them so the relationship is documented; the forward FK
from child to host is emitted by the FK detection passes on the child.

The wiki Resource pages still document satellites and Collection
fields because they are part of the published RESO 2.0 spec.
Operational/denormalized stores (Atlas) may opt back in to a chosen
subset of satellites for query performance via
`build_atlas_target_dbml.py`. The canonical model stays clean.

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
