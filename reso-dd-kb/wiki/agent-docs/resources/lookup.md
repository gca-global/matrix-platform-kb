# `lookup` (Lookup)

> Metadata about lookups (enumerations) available on a given server.

- Source: [https://dd.reso.org/DD2.0/Lookup/](https://dd.reso.org/DD2.0/Lookup/)
- Field count on dd.reso.org: **6**
- Primary key: `lookup_key`
- Last revised upstream: 2/2/2022

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `LegacyODataValue` | `legacy_o_data_value` | String |  | The name of the resource the field belongs to. |  |
| `LookupKey` | `lookup_key` | String |  | The key used to uniquely identify the lookup entry. | `pk` |
| `LookupName` | `lookup_name` | String |  | The name of the enumeration. |  |
| `LookupValue` | `lookup_value` | String |  | The human-friendly display name the data consumer receives in the payload and uses in queries. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The timestamp for when the enumeration value was last modified. |  |
| `StandardLookupValue` | `standard_lookup_value` | String |  | The Data Dictionary LookupDisplayName of the enumerated value. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

