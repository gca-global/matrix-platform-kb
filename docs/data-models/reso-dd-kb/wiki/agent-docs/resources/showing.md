[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `showing` (Showing)

> 

## At a glance

| | |
|---|---|
| **Primary key** | `showing_key` |
| **Fields on dd.reso.org** | 44 |
| **Columns in canonical DBML** | 32 (omits 1 satellite drops + 8 `Resource`-typed + 3 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Showing/](https://dd.reso.org/DD2.0/Showing/) |
| **Last revised upstream** | 6/16/2022 |

## Relationship diagram

```mermaid
flowchart LR
    showing["showing"]
    member["member"]
    showing -->|"showing_agent_key"| member
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `AgentOriginatingSystem` | `agent_originating_system` | Resource |  | The originating system of the member associated with the showing. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `AgentOriginatingSystemID` | `agent_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the listing was input). In cases where the originating system was not where the record was retrieved, see the Source System fields. | Free-form text, up to 25 characters. |  |
| `AgentOriginatingSystemName` | `agent_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the listing is originally input by the member. The legal name of the company. In cases where the originating system was not where the record was retrieved, see the Source System fields. | Free-form text, up to 255 characters. |  |
| `AgentSourceSystem` | `agent_source_system` | Resource |  | The source system of the member associated with the showing. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `AgentSourceSystemID` | `agent_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `AgentSourceSystemName` | `agent_source_system_name` | String |  | The name of the immediate record provider. The system from which the record was directly received. The legal name of the company. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Showing record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `showing` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `Listing` | `listing` | Resource |  | The listing associated with the showing. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing being shown. The value may be identical to that of the listing key, but the listing ID is intended to be the value used by a human to retrieve the information about a specific listing. In a multiple-originating system or a merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ListingKey` | `listing_key` | String |  | A unique identifier for this record. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemKey and OriginatingSystemKey. | Free-form text, up to 255 characters. |  |
| `ListingOriginatingSystem` | `listing_originating_system` | Resource |  | The originating system of the Listing record associated with the showing. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ListingOriginatingSystemID` | `listing_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the listing was input). In cases where the originating system was not where the record was retrieved, see the Source System fields. | Free-form text, up to 25 characters. |  |
| `ListingOriginatingSystemName` | `listing_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the listing is originally input by the member. The legal name of the company. In cases where the originating system was not where the record was retrieved, see the Source System fields. | Free-form text, up to 255 characters. |  |
| `ListingSourceSystem` | `listing_source_system` | Resource |  | The source system of the Listing record associated with the showing. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ListingSourceSystemID` | `listing_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `ListingSourceSystemName` | `listing_source_system_name` | String |  | The name of the immediate record provider. The system from which the record was directly received. The legal name of the company. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `Media` | `media` | Collection |  | The media associated with the Showing record. | Inverse 1:N: read as 'all `media` rows that point at this `showing` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the Showing record was last modified. | ISO-8601 timestamp (UTC). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the showing record was entered and made visible to members of the system. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystemAgentKey` | `originating_system_agent_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the showing service in which the member was input). There may be cases where the source system (how the record is received) is not the originating system. See SourceSystemAgentKey for more information. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemListingKey` | `originating_system_listing_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the member was input). There may be cases where the source system (how the record is received) is not the originating system. See SourceSystemKey for more information. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemShowingKey` | `originating_system_showing_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the member was input). There may be cases where the source system (how the record is received) is not the originating system. See SourceSystemKey fields for more information. | Free-form text, up to 255 characters. |  |
| `ShowingAgent` | `showing_agent` | Resource |  | The showing agent. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. Specifically, in aggregation systems, the ListAgentKey is the system unique identifier from the system where the record was retrieved. This may be identical to the related xxxId. This is a foreign key relating to the Member Resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `ShowingAgentMlsID` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Do not write. Phase-2.5 satellite of `ShowingAgentKey`; the same value lives on the parent resource and is reachable via the `ShowingAgentKey` FK. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAllowed` | `showing_allowed` | Boolean |  | The main Y/N field to denote whether showings are allowed to be requested at this time. There may be future showings previously scheduled. | Boolean. |  |
| `ShowingEndTimestamp` | `showing_end_timestamp` | Timestamp |  | The date and time the showing ends. Where other timestamps are typically stored in Coordinated Universal Time (UTC), showing start and end date/times are typically stored in the local time zone of the property being showed. | ISO-8601 timestamp (UTC). |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the Showing record. The value may be identical to that of the ShowingKey, but the ShowingID is intended to be the value used by a human to retrieve the information about a specific showing. In a multiple-originating system or a merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemShowingKey and OriginatingSystemShowingKey. | Unique key for this resource. Use as the FK target whenever another resource references `showing`. | `pk` |
| `ShowingOriginatingSystem` | `showing_originating_system` | Resource |  | The originating system of the Showing record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ShowingOriginatingSystemID` | `showing_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the listing was input). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `ShowingOriginatingSystemName` | `showing_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the listing is originally input by the member. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `ShowingRequestedTimestamp` | `showing_requested_timestamp` | Timestamp |  | The date/time when the showing agent submitted a request to access the property. This is a system timestamp normally generated by a showing system, which is commonly the originating system for showing records. | ISO-8601 timestamp (UTC). |  |
| `ShowingSourceSystem` | `showing_source_system` | Resource |  | The source system of the Showing record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ShowingSourceSystemID` | `showing_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `ShowingSourceSystemName` | `showing_source_system_name` | String |  | The name of the immediate record provider. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `ShowingStartTimestamp` | `showing_start_timestamp` | Timestamp |  | The date and time the showing begins. Where other timestamps are typically stored in Coordinated Universal Time (UTC), showing start and end date/times are typically stored in the local time zone of the property being showed. | ISO-8601 timestamp (UTC). |  |
| `ShowingStatus` | `showing_status` | enum | [`showing_status`](../lookups.md#showing_status) | The current state of showing acceptance on the listing. | Pick exactly one of 4 values from the lookup (closed list). |  |
| `ShowingTimeZone` | `showing_time_zone` | enum | [`iana_time_zone_values`](../lookups.md#iana_time_zone_values) | The standard name of the time zone, as provided by the IANA tz database. This denotes the time zone of the property being shown. | Pick exactly one of 482 values from the lookup (closed list). |  |
| `ShowingUrl` | `showing_url` | String |  | The Uniform Resource Locator (URL) that links to the originating system. | Free-form text, up to 255 characters. |  |
| `SocialMedia` | `social_media` | Collection |  | The social media associated with the Showing record. | Inverse 1:N: read as 'all `social_media` rows that point at this `showing` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `SourceSystemAgentKey` | `source_system_agent_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemListingKey` | `source_system_listing_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemShowingKey` | `source_system_showing_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`ListingKey` vs `ListingId`**:
  - `ListingKey` - A unique identifier for this record.
  - `ListingId` - The well-known identifier for the listing being shown.
- **`ShowingKey` vs `ShowingId`**:
  - `ShowingKey` - A unique identifier for this record from the immediate source.
  - `ShowingId` - The well-known identifier for the Showing record.

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

