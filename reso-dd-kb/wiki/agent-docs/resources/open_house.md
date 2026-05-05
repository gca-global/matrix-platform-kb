# `open_house` (OpenHouse)

> Fields commonly used to record an open house event.

- Source: [https://dd.reso.org/DD2.0/OpenHouse/](https://dd.reso.org/DD2.0/OpenHouse/)
- Field count on dd.reso.org: **33**
- Primary key: `open_house_key`
- Last revised upstream: 8/8/2013

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `AppointmentRequiredYN` | `appointment_required_yn` | Boolean |  | Indicates whether or not the open house requires an appointment. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the OpenHouse record. | `[Collection]` |
| `Listing` | `listing` | Resource |  | The listing associated with the open house. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing related to this open house. |  |
| `ListingKey` | `listing_key` | String |  | A unique identifier for the listing record related to this open house. |  |
| `LivestreamOpenHouseURL` | `livestream_open_house_url` | String |  | A link to an open house livestream event. |  |
| `Media` | `media` | Collection |  | The media related to the OpenHouse record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the OpenHouse record was last modified. |  |
| `OpenHouseAttendedBy` | `open_house_attended_by` | enum | [`attended`](../lookups.md#attended) | States whether or not the open house will be attended by a licensed agent (i.e., Agent, Seller, Unattended). |  |
| `OpenHouseDate` | `open_house_date` | Date |  | The date on which the open house will occur. |  |
| `OpenHouseEndTime` | `open_house_end_time` | Timestamp |  | The time the open house ends. |  |
| `OpenHouseId` | `open_house_id` | String |  | The well-known identifier for the OpenHouse Resource. |  |
| `OpenHouseKey` | `open_house_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `OpenHouseRemarks` | `open_house_remarks` | String |  | Comments, instructions or information about the open house. |  |
| `OpenHouseStartTime` | `open_house_start_time` | Timestamp |  | The time the open house begins. |  |
| `OpenHouseStatus` | `open_house_status` | enum | [`open_house_status`](../lookups.md#open_house_status) | Status of the open house (i.e., Active, Canceled, Ended). |  |
| `OpenHouseType` | `open_house_type` | enum | [`open_house_type`](../lookups.md#open_house_type) | The type of open house (i.e., Public, Broker, Office, Association, Private (invitation or targeted publication)). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the open house was entered and made visible to members of the MLS. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the OpenHouse record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `Refreshments` | `refreshments` | String |  | A description of the refreshments that will be served at the open house. |  |
| `ShowingAgent` | `showing_agent` | Resource |  | The member record of the showing agent. | `[Resource]` |
| `ShowingAgentFirstName` | `showing_agent_first_name` | String |  | The first name of the showing agent. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `ShowingAgentLastName` | `showing_agent_last_name` | String |  | The last name of the showing agent. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAgentMlsID` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member. | `[dropped: satellite of showing_agent_key]` |
| `SocialMedia` | `social_media` | Collection |  | The social media related to the OpenHouse record. | `[Collection]` |
| `SourceSystem` | `source_system` | Resource |  | The source system of the OpenHouse record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the open house record provider. |  |

## Foreign keys OUT (this resource references)

- `open_house.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Polymorphic FKs

- `listing_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_first_name` | `showing_agent_key` -> `member.member_first_name` | `drop_from_host` |  |
| `showing_agent_last_name` | `showing_agent_key` -> `member.member_last_name` | `drop_from_host` |  |
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `drop_from_host` |  |

