[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `property_power_storage` (PropertyPowerStorage)

> Different means of storing power on a property.

## At a glance

| | |
|---|---|
| **Primary key** | `power_storage_key` |
| **Fields on dd.reso.org** | 6 |
| **Columns in canonical DBML** | 6 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/PropertyPowerStorage/](https://dd.reso.org/DD2.0/PropertyPowerStorage/) |
| **Last revised upstream** | 1/19/2023 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `DateOfInstallation` | `date_of_installation` | Date |  | The date the power storage system was installed. | Date (YYYY-MM-DD). |  |
| `InformationSource` | `information_source` | String |  | The provider of the information about the power storage system. | Free-form text, up to 255 characters. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the PropertyPowerStorage record was last modified. | ISO-8601 timestamp (UTC). |  |
| `NameplateCapacity` | `nameplate_capacity` | Number |  | The kWh the battery is theoretically able to store. | Numeric, up to 2 decimal place(s). |  |
| `PowerStorageKey` | `power_storage_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the PowerStorageKey is the system unique identifier from the system that the record was retrieved. | Unique key for this resource. Use as the FK target whenever another resource references `property_power_storage`. | `pk` |
| `PowerStorageType` | `power_storage_type` | enum | [`power_storage_type`](../lookups.md#power_storage_type) | The type of battery. | Pick exactly one of 5 values from the lookup (closed list). |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

