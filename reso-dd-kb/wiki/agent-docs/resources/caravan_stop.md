# `caravan_stop` (CaravanStop)

> Stops along a caravan tour, connecting Caravan records to Open House records.

- Source: [https://dd.reso.org/DD2.0/CaravanStop/](https://dd.reso.org/DD2.0/CaravanStop/)
- Field count on dd.reso.org: **25**
- Primary key: `caravan_stop_key`
- Last revised upstream: 2/3/2021

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `CaravanKey` | `caravan_key` | String |  | A system unique identifier. | `-> caravan.caravan_key` |
| `CaravanStopKey` | `caravan_stop_key` | String |  | A system unique identifier. | `pk` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the CaravanStop record was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the CaravanStop record was originally input into the source system. |  |
| `OriginatingSystemId` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SourceSystemId` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the caravan stop's record provider. |  |
| `StopAttendedBy` | `stop_attended_by` | enum | [`caravan_stop_attended`](../lookups.md#caravan_stop_attended) | This states whether a caravan stop will be attended by a licensed agent (i.e., Attended by Agent, Attended by the Seller or Unattended). |  |
| `StopClassName` | `stop_class_name` | enum | [`caravan_stop_class_name`](../lookups.md#caravan_stop_class_name) | The name of the class that applies to this caravan stop record. |  |
| `StopDate` | `stop_date` | Date |  | The date the caravan stop will be open. |  |
| `StopEndTime` | `stop_end_time` | Timestamp |  | The time the caravan stop will be closed. |  |
| `StopId` | `stop_id` | String |  | The ID of a caravan stop record. |  |
| `StopKey` | `stop_key` | String |  | The key of a caravan stop record. |  |
| `StopOrder` | `stop_order` | Number |  | This is used when the order of stops needs to be communicated. |  |
| `StopRefreshments` | `stop_refreshments` | String |  | A description of the refreshments that will be served at the caravan stop. |  |
| `StopRemarks` | `stop_remarks` | String |  | Comments, instructions or information about the caravan stop. |  |
| `StopResourceName` | `stop_resource_name` | enum | [`caravan_resource_name`](../lookups.md#caravan_resource_name) | The name of the resource that applies to this caravan stop record. |  |
| `StopShowingAgentFirstName` | `stop_showing_agent_first_name` | String |  | The first name of the showing agent for the caravan stop. | `[REVIEW]` |
| `StopShowingAgentKey` | `stop_showing_agent_key` | String |  | A system unique identifier for the caravan stop's showing agent. | `-> member.member_key` |
| `StopShowingAgentLastName` | `stop_showing_agent_last_name` | String |  | The last name of the showing agent for the caravan stop. | `[REVIEW]` |
| `StopShowingAgentMlsId` | `stop_showing_agent_mls_id` | String |  | The local, well-known identifier for the showing agent. | `[dropped: satellite of stop_showing_agent_key]` |
| `StopStartTime` | `stop_start_time` | Timestamp |  | The time the caravan stop will be open. |  |

## Foreign keys OUT (this resource references)

- `caravan_stop.caravan_key` -> `caravan.caravan_key` (high)
- `caravan_stop.stop_showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Polymorphic FKs

- `stop_class_name` - target resolved at runtime; evidence: prose:P5b:"might also be another custom"
- `stop_id` - target resolved at runtime; evidence: prose:P5b:"might also be another custom"
- `stop_key` - target resolved at runtime; evidence: prose:P5b:"might also be another custom"
- `stop_resource_name` - target resolved at runtime; evidence: prose:P5b:"might also be another custom"

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `caravan_stop_key` | `caravan_key` -> `caravan.?` | `keep_both` | no_child_match |
| `stop_showing_agent_first_name` | `stop_showing_agent_key` -> `member.member_first_name` | `review` | borderline_jaccard |
| `stop_showing_agent_last_name` | `stop_showing_agent_key` -> `member.member_last_name` | `review` | borderline_jaccard |
| `stop_showing_agent_mls_id` | `stop_showing_agent_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |

