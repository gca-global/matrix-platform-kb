[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `queue` (Queue)

> Events that have occurred with records in other resources.

## At a glance

| | |
|---|---|
| **Primary key** | `queue_transaction_key` *(override; RESO uses `QueueTransactionKey`)* |
| **Fields on dd.reso.org** | 16 |
| **Columns in canonical DBML** | 13 (omits 0 satellite drops + 2 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Queue/](https://dd.reso.org/DD2.0/Queue/) |
| **Last revised upstream** | 5/12/2018 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | Name of the class that this queue record is referencing. | Pick exactly one of 17 values from the lookup (closed list). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Queue record. | Inverse 1:N collection; the FK is declared on the child resource, not here. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | Timestamp of the last major change on the listing (see also MajorChangeType). | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Queue record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the queue record was generated. In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the queue record was originally generated. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemQueueKey` | `originating_system_queue_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the queue record was generated). There may be cases where the source system (how the record is received) is not the originating system. See Source System Key for more information. | Free-form text, up to 255 characters. |  |
| `QueueTransactionKey` | `queue_transaction_key` | String |  | A unique identifier for this record from the immediate source. This may be a number, or string that can include Uniform Resource Identifier (URI) or other forms. This is the system you are connecting to and not necessarily the original source of the record. | Unique key for this resource. Use as the FK target whenever another resource references `queue`. | `pk` |
| `QueueTransactionType` | `queue_transaction_type` | enum | [`queue_transaction_type`](../lookups.md#queue_transaction_type) | The type of change that the queue transaction record is representing (e.g., Add, Change, Delete). | Pick exactly one of 3 values from the lookup (closed list). |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The name of the resource which this queue record is referencing. | Pick exactly one of 5 values from the lookup (closed list). |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. The value may be identical to that of the listing key, but the listing ID is intended to be the value used by a human to retrieve the information about a specific listing. In a multiple-originating system or a merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). This is the system being connected to and is not necessarily the original source of the record. This is a foreign key from the resource selected in the ResourceName field. | Polymorphic key. Resolve the target resource at write time from the row's context (see Definition); store the chosen target's PK in this column. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Queue record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the queue record provider. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `SourceSystemQueueKey` | `source_system_queue_key` | String |  | The system key, a unique record identifier, from the source system, which is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

