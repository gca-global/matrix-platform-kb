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

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `FieldKey` | `field_key` | String |  | The key used to uniquely identify the field. | Unique key for this resource. Use as the FK target whenever another resource references `field`. | `pk` |
| `FieldName` | `field_name` | String |  | The name of the field as expressed in the payload. For OData APIs, this field MUST meet certain naming requirements and should be consistent with what's advertised in the OData XML metadata (to be verified in certification). For example, "ListPrice." | Free-form text. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The timestamp when the field metadata item was last modified. This is used to help rebuild caches when metadata items change so consumers don't have to re-pull and reprocess the entire set of metadata when only a small number of changes have been made. | ISO-8601 timestamp (UTC). |  |
| `ResourceName` | `resource_name` | String |  | The name of the resource the field belongs to. This will be a RESO Standard Name, when applicable, but may also be a local resource name (e.g., "Property"). | Free-form text. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

