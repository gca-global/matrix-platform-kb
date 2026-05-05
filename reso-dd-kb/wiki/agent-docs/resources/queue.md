# `queue` (Queue)

> Events that have occurred with records in other resources.

- Source: [https://dd.reso.org/DD2.0/Queue/](https://dd.reso.org/DD2.0/Queue/)
- Field count on dd.reso.org: **16**
- Primary key: `queue_transaction_key`
- Note: PK chosen by override (RESO uses `QueueTransactionKey` for this resource).
- Last revised upstream: 5/12/2018

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | Name of the class that this queue record is referencing. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Queue record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | Timestamp of the last major change on the listing (see also MajorChangeType). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Queue record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `OriginatingSystemQueueKey` | `originating_system_queue_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `QueueTransactionKey` | `queue_transaction_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `QueueTransactionType` | `queue_transaction_type` | enum | [`queue_transaction_type`](../lookups.md#queue_transaction_type) | The type of change that the queue transaction record is representing (e.g., Add, Change, Delete). |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The name of the resource which this queue record is referencing. |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Queue record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the queue record provider. |  |
| `SourceSystemQueueKey` | `source_system_queue_key` | String |  | The system key, a unique record identifier, from the source system, which is the system from which the record was directly received. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

