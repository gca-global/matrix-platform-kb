[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `lookup` (Lookup)

> Metadata about lookups (enumerations) available on a given server.

## At a glance

| | |
|---|---|
| **Primary key** | `lookup_key` |
| **Fields on dd.reso.org** | 6 |
| **Columns in canonical DBML** | 6 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Lookup/](https://dd.reso.org/DD2.0/Lookup/) |
| **Last revised upstream** | 2/2/2022 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `LegacyODataValue` | `legacy_o_data_value` | String |  | The name of the resource the field belongs to. This will be a RESO Standard Name, such as "Property", but may also be a non-standard local resource name. | Free-form text. |  |
| `LookupKey` | `lookup_key` | String |  | The key used to uniquely identify the lookup entry. | Unique key for this resource. Use as the FK target whenever another resource references `lookup`. | `pk` |
| `LookupName` | `lookup_name` | String |  | The name of the enumeration. This is the LookupField in the adopted Data Dictionary spreadsheet. It is called a "LookupName" in this proposal because more than one field can have a given lookup, so it refers to the name of the lookup rather than a given field. For example, Listing with CountyOrParish and Office with OfficeCountyOrParish having the same CountyOrParish LookupName. This MUST match the Data Dictionary definition for in cases where the lookup is defined. Vendors MAY add their own enumerations otherwise. The LookupName a given field uses is required to be annotated at the field level in the OData XML Metadata, as outlined later in this proposal. | Free-form text. |  |
| `LookupValue` | `lookup_value` | String |  | The human-friendly display name the data consumer receives in the payload and uses in queries. This may be a local name or synonym for a given RESO Data Dictionary lookup item. | Free-form text. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The timestamp for when the enumeration value was last modified. This is used to help rebuild caches when metadata items change so consumers don't have to re-pull and reprocess the entire set of metadata when only a small number of changes have been made. | ISO-8601 timestamp (UTC). |  |
| `StandardLookupValue` | `standard_lookup_value` | String |  | The Data Dictionary LookupDisplayName of the enumerated value. This field is required when the LookupValue for a given item corresponds to a RESO standard value, meaning a standard lookup display name, known synonym, local name or translation of that value. Local lookups may omit this value if they don't correspond to an existing RESO standard lookup value. | Free-form text. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

