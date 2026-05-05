# `property_power_storage` (PropertyPowerStorage)

> Different means of storing power on a property.

- Source: [https://dd.reso.org/DD2.0/PropertyPowerStorage/](https://dd.reso.org/DD2.0/PropertyPowerStorage/)
- Field count on dd.reso.org: **6**
- Primary key: `power_storage_key`
- Last revised upstream: 1/19/2023

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `DateOfInstallation` | `date_of_installation` | Date |  | The date the power storage system was installed. |  |
| `InformationSource` | `information_source` | String |  | The provider of the information about the power storage system. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the PropertyPowerStorage record was last modified. |  |
| `NameplateCapacity` | `nameplate_capacity` | Number |  | The kWh the battery is theoretically able to store. |  |
| `PowerStorageKey` | `power_storage_key` | String |  | A system unique identifier. | `pk` |
| `PowerStorageType` | `power_storage_type` | enum | [`power_storage_type`](../lookups.md#power_storage_type) | The type of battery. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

