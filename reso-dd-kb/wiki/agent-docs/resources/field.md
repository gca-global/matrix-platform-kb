[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `field` (Field)

> Metadata about available fields on a given server in a predictable and user-friendly format.

## At a glance

| | |
|---|---|
| **Primary key** | `field_key` |
| **Fields on dd.reso.org** | 4 |
| **Columns in canonical DBML** | 4 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Field/](https://dd.reso.org/DD2.0/Field/) |
| **Last revised upstream** | 12/8/2021 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `FieldKey` | `field_key` | String |  | The key used to uniquely identify the field. | `pk` |
| `FieldName` | `field_name` | String |  | The name of the field as expressed in the payload. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The timestamp when the field metadata item was last modified. |  |
| `ResourceName` | `resource_name` | String |  | The name of the resource the field belongs to. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

