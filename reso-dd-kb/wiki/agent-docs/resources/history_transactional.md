# `history_transactional` (HistoryTransactional)

> A transactional history of the listing, showing before and after values of field changes.

- Source: [https://dd.reso.org/DD2.0/HistoryTransactional/](https://dd.reso.org/DD2.0/HistoryTransactional/)
- Field count on dd.reso.org: **23**
- Primary key: `history_transactional_key`
- Last revised upstream: 9/24/2015

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ChangeType` | `change_type` | enum | [`change_type`](../lookups.md#change_type) | A description of the last major change on the listing (i.e., Price Reduction, Back on Market, etc.). |  |
| `ChangedByMember` | `changed_by_member` | Resource |  | The member who changed the historical item. | `[Resource]` |
| `ChangedByMemberID` | `changed_by_member_id` | String |  | The local, well-know identifier of the member (user) who made the change. |  |
| `ChangedByMemberKey` | `changed_by_member_key` | String |  | The unique identifier of the member (user) who made the change. | `-> member.member_key` |
| `ClassName` | `class_name` | String | [`class_name`](../lookups.md#class_name) | The name of the class in which this history record applies. |  |
| `EntityEventSequence` | `entity_event_sequence` | Number |  | A unique, system-wide ID that can be used to represent the sequence in which an EntityEvent occurred in a given system. |  |
| `FieldKey` | `field_key` | String |  | The unique identifier of the field with data being changed. |  |
| `FieldName` | `field_name` | String |  | The name of the field where data is being changed. |  |
| `HistoryTransactionalKey` | `history_transactional_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The timestamp of the last major change on the listing (see also MajorChangeType). |  |
| `NewValue` | `new_value` | String |  | The new value applied to the named field. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the HistoryTransactional record. | `[Resource]` |
| `OriginatingSystemHistoryKey` | `originating_system_history_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. | `-> ouid.organization_unique_id` |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `PreviousValue` | `previous_value` | String |  | The value found in the named field prior to the change represented by this record. |  |
| `ResourceName` | `resource_name` | String |  | The name of the resource in which this history record applies. |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the HistoryTransactional record. | `[Resource]` |
| `SourceSystemHistoryKey` | `source_system_history_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. | `-> ouid.organization_unique_id` |
| `SourceSystemName` | `source_system_name` | String |  | The name of the historical record provider. |  |

## Foreign keys OUT (this resource references)

- `history_transactional.changed_by_member_key` -> `member.member_key` (high)
- `history_transactional.originating_system_id` -> `ouid.organization_unique_id` (medium)
- `history_transactional.source_system_id` -> `ouid.organization_unique_id` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `originating_system_history_key` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `originating_system_name` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_history_key` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_name` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |

