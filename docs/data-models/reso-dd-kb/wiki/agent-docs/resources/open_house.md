[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `open_house` (OpenHouse)

> Fields commonly used to record an open house event.

## At a glance

| | |
|---|---|
| **Primary key** | `open_house_key` |
| **Fields on dd.reso.org** | 33 |
| **Columns in canonical DBML** | 23 (omits 3 satellite drops + 4 `Resource`-typed + 3 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/OpenHouse/](https://dd.reso.org/DD2.0/OpenHouse/) |
| **Last revised upstream** | 8/8/2013 |

## Relationship diagram

```mermaid
flowchart LR
    open_house["open_house"]
    member["member"]
    open_house -->|"showing_agent_key"| member
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `AppointmentRequiredYN` | `appointment_required_yn` | Boolean |  | Indicates whether or not the open house requires an appointment. | Nullable boolean flag (true / false / null = unknown). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the OpenHouse record. | Inverse 1:N collection; the FK is declared on the child resource, not here. | `[Collection]` |
| `Listing` | `listing` | Resource |  | The listing associated with the open house. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing related to this open house. The value may be identical to that of the listing key, but the listing ID is intended to be the value used by a human to retrieve the information about a specific listing. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ListingKey` | `listing_key` | String |  | A unique identifier for the listing record related to this open house. This may be a number or string that can include a Uniform Resource Identifier (URI) or other forms. This is the system being connected to and not necessarily the original source of the record. This may be a foreign key from the resource selected in the ResourceName field. | Polymorphic key. Resolve the target resource at write time from the row's context (see Definition); store the chosen target's PK in this column. |  |
| `LivestreamOpenHouseURL` | `livestream_open_house_url` | String |  | A link to an open house livestream event. | Free-form text, up to 8000 characters. |  |
| `Media` | `media` | Collection |  | The media related to the OpenHouse record. | Inverse 1:N collection; the FK is declared on the child resource, not here. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the OpenHouse record was last modified. | ISO-8601 timestamp (UTC). |  |
| `OpenHouseAttendedBy` | `open_house_attended_by` | enum | [`attended`](../lookups.md#attended) | States whether or not the open house will be attended by a licensed agent (i.e., Agent, Seller, Unattended). | Pick exactly one of 3 values from the lookup (closed list). |  |
| `OpenHouseDate` | `open_house_date` | Date |  | The date on which the open house will occur. | Date (YYYY-MM-DD). |  |
| `OpenHouseEndTime` | `open_house_end_time` | Timestamp |  | The time the open house ends. | ISO-8601 timestamp (UTC). |  |
| `OpenHouseId` | `open_house_id` | String |  | The well-known identifier for the OpenHouse Resource. The value may be identical to that of OpenHouseKey, but OpenHouseId is intended to be the value used by a human to retrieve the information about a specific open house. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `OpenHouseKey` | `open_house_key` | String |  | A unique identifier for this record from the immediate source. This may be a number or string that can include a Uniform Resource Identifier (URI) or other forms. This is the system you are connecting to and not necessarily the original source of the record. | Unique key for this resource. Use as the FK target whenever another resource references `open_house`. | `pk` |
| `OpenHouseRemarks` | `open_house_remarks` | String |  | Comments, instructions or information about the open house. | Free-form text, up to 500 characters. |  |
| `OpenHouseStartTime` | `open_house_start_time` | Timestamp |  | The time the open house begins. | ISO-8601 timestamp (UTC). |  |
| `OpenHouseStatus` | `open_house_status` | enum | [`open_house_status`](../lookups.md#open_house_status) | Status of the open house (i.e., Active, Canceled, Ended). | Pick exactly one of 3 values from the lookup (closed list). |  |
| `OpenHouseType` | `open_house_type` | enum | [`open_house_type`](../lookups.md#open_house_type) | The type of open house (i.e., Public, Broker, Office, Association, Private (invitation or targeted publication)). | Pick exactly one of 5 values from the lookup (closed list). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the open house was entered and made visible to members of the MLS. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the OpenHouse record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the MLS where the open house was input). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the open house was input). There may be cases where the source system (how the record was received) is not the originating system. See Source System Key for more information. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the open house is originally input. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `Refreshments` | `refreshments` | String |  | A description of the refreshments that will be served at the open house. | Free-form text, up to 255 characters. |  |
| `ShowingAgent` | `showing_agent` | Resource |  | The member record of the showing agent. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ShowingAgentFirstName` | `showing_agent_first_name` | String |  | The first name of the showing agent. | Do not write. Phase-2.5 satellite of `ShowingAgentKey`; the same value lives on the parent resource and is reachable via the `ShowingAgentKey` FK. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the ListAgentKey is the system unique identifier from the system where the record was retrieved. This may be identical to the related xxxId. This is a foreign key relating to the Member Resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `ShowingAgentLastName` | `showing_agent_last_name` | String |  | The last name of the showing agent. | Do not write. Phase-2.5 satellite of `ShowingAgentKey`; the same value lives on the parent resource and is reachable via the `ShowingAgentKey` FK. | `[dropped: satellite of showing_agent_key]` |
| `ShowingAgentMlsID` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Do not write. Phase-2.5 satellite of `ShowingAgentKey`; the same value lives on the parent resource and is reachable via the `ShowingAgentKey` FK. | `[dropped: satellite of showing_agent_key]` |
| `SocialMedia` | `social_media` | Collection |  | The social media related to the OpenHouse record. | Inverse 1:N collection; the FK is declared on the child resource, not here. | `[Collection]` |
| `SourceSystem` | `source_system` | Resource |  | The source system of the OpenHouse record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the open house record provider. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`ListingKey` vs `ListingId`**:
  - `ListingKey` - A unique identifier for the listing record related to this open house.
  - `ListingId` - The well-known identifier for the listing related to this open house.
- **`OpenHouseKey` vs `OpenHouseId`**:
  - `OpenHouseKey` - A unique identifier for this record from the immediate source.
  - `OpenHouseId` - The well-known identifier for the OpenHouse Resource.

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

