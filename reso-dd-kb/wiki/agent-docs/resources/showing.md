# `showing` (Showing)

> 

- Source: [https://dd.reso.org/DD2.0/Showing/](https://dd.reso.org/DD2.0/Showing/)
- Field count on dd.reso.org: **44**
- Primary key: `showing_key`
- Last revised upstream: 6/16/2022

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `AgentOriginatingSystem` | `agent_originating_system` | Resource |  | The originating system of the member associated with the showing. | `[Resource]` |
| `AgentOriginatingSystemID` | `agent_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `AgentOriginatingSystemName` | `agent_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `AgentSourceSystem` | `agent_source_system` | Resource |  | The source system of the member associated with the showing. | `[Resource]` |
| `AgentSourceSystemID` | `agent_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `AgentSourceSystemName` | `agent_source_system_name` | String |  | The name of the immediate record provider. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Showing record. | `[Collection]` |
| `Listing` | `listing` | Resource |  | The listing associated with the showing. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing being shown. |  |
| `ListingKey` | `listing_key` | String |  | A unique identifier for this record. |  |
| `ListingOriginatingSystem` | `listing_originating_system` | Resource |  | The originating system of the Listing record associated with the showing. | `[Resource]` |
| `ListingOriginatingSystemID` | `listing_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `ListingOriginatingSystemName` | `listing_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `ListingSourceSystem` | `listing_source_system` | Resource |  | The source system of the Listing record associated with the showing. | `[Resource]` |
| `ListingSourceSystemID` | `listing_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `ListingSourceSystemName` | `listing_source_system_name` | String |  | The name of the immediate record provider. |  |
| `Media` | `media` | Collection |  | The media associated with the Showing record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the Showing record was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the showing record was entered and made visible to members of the system. |  |
| `OriginatingSystemAgentKey` | `originating_system_agent_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemListingKey` | `originating_system_listing_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemShowingKey` | `originating_system_showing_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `ShowingAgent` | `showing_agent` | Resource |  | The showing agent. | `[Resource]` |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. | `-> member.member_key` |
| `ShowingAgentMlsID` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAllowed` | `showing_allowed` | Boolean |  | The main Y/N field to denote whether showings are allowed to be requested at this time. |  |
| `ShowingEndTimestamp` | `showing_end_timestamp` | Timestamp |  | The date and time the showing ends. |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the Showing record. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `ShowingOriginatingSystem` | `showing_originating_system` | Resource |  | The originating system of the Showing record. | `[Resource]` |
| `ShowingOriginatingSystemID` | `showing_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `ShowingOriginatingSystemName` | `showing_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `ShowingRequestedTimestamp` | `showing_requested_timestamp` | Timestamp |  | The date/time when the showing agent submitted a request to access the property. |  |
| `ShowingSourceSystem` | `showing_source_system` | Resource |  | The source system of the Showing record. | `[Resource]` |
| `ShowingSourceSystemID` | `showing_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `ShowingSourceSystemName` | `showing_source_system_name` | String |  | The name of the immediate record provider. |  |
| `ShowingStartTimestamp` | `showing_start_timestamp` | Timestamp |  | The date and time the showing begins. |  |
| `ShowingStatus` | `showing_status` | enum | [`showing_status`](../lookups.md#showing_status) | The current state of showing acceptance on the listing. |  |
| `ShowingTimeZone` | `showing_time_zone` | enum | [`iana_time_zone_values`](../lookups.md#iana_time_zone_values) | The standard name of the time zone, as provided by the IANA tz database. |  |
| `ShowingUrl` | `showing_url` | String |  | The Uniform Resource Locator (URL) that links to the originating system. |  |
| `SocialMedia` | `social_media` | Collection |  | The social media associated with the Showing record. | `[Collection]` |
| `SourceSystemAgentKey` | `source_system_agent_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemListingKey` | `source_system_listing_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemShowingKey` | `source_system_showing_key` | String |  | The system key, a unique record identifier, from the source system. |  |

## Foreign keys OUT (this resource references)

- `showing.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `showing`)
- `media` -> `media` (many `media` per `showing`)
- `social_media` -> `social_media` (many `social_media` per `showing`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `drop_from_host` |  |

