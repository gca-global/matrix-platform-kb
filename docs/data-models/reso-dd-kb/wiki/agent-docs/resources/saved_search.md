[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `saved_search` (SavedSearch)

> Saved search criteria and related data.

## At a glance

| | |
|---|---|
| **Primary key** | `saved_search_key` |
| **Fields on dd.reso.org** | 27 |
| **Columns in canonical DBML** | 22 (omits 1 satellite drops + 3 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 1 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/SavedSearch/](https://dd.reso.org/DD2.0/SavedSearch/) |
| **Last revised upstream** | 8/28/2019 |

## Relationship diagram

```mermaid
flowchart LR
    saved_search["saved_search"]
    member["member"]
    saved_search -->|"member_key"| member
    prospecting["prospecting"]
    prospecting -->|"saved_search_key"| saved_search
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | The class or table to which the SearchQuery criteria refers (e.g., Residential, Residential Lease, Residential Income, Commercial Sale). | Pick exactly one of 17 values from the lookup (closed list). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The collection history items related to the SavedSearch record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `saved_search` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `Member` | `member` | Resource |  | The member associated with the saved search. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `MemberKey` | `member_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the MemberKey is the system unique identifier from the system that the record was retrieved. This may be identical to the related xxxId. This is a foreign key relating to the Member Resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Do not write. Phase-2.5 satellite of `MemberKey`; the same value lives on the parent resource and is reachable via the `MemberKey` FK. | `[dropped: satellite of member_key]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was last modified. | ISO-8601 timestamp (UTC). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was entered. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the SavedSearch record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the MLS where the saved search was input). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the saved search was input). There may be cases where the source system (how the record was received) is not the originating system. See Source System Key for more information. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | Unique identifier from the originating system, which is commonly a key to that system. In the case where data is passed through more than one system, this is the originating system key. This is a foreign key relating to the system where this record was originated. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemMemberName` | `originating_system_member_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the listing is originally input by the member. The legal name of the company to be used for display. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the saved search is originally input. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource to which the SearchQuery criteria refers (e.g., Property, OpenHouse, Agent, Office, Contacts). | Pick exactly one of 5 values from the lookup (closed list). |  |
| `SavedSearchDescription` | `saved_search_description` | String |  | A textual description of the saved search input by the member who created the saved search. | Free-form text, up to 4000 characters. |  |
| `SavedSearchKey` | `saved_search_key` | String |  | A unique identifier for this record from the immediate source. This may be a number or string that can include a Uniform Resource Identifier (URI) or other forms. This is the system being connected to and not necessarily the original source of the record. | Unique key for this resource. Use as the FK target whenever another resource references `saved_search`. | `pk` |
| `SavedSearchName` | `saved_search_name` | String |  | The name given to the search by the member inputting the saved search. | Free-form text, up to 255 characters. |  |
| `SavedSearchType` | `saved_search_type` | enum | [`saved_search_type`](../lookups.md#saved_search_type) | Determines if the saved search used to pass criteria is to be stored and executed by the client or if it is a key to be passed to the host for execution (i.e., Client Receives Criteria, Host Returns Listings). May be described at the record level with this field or at some other level of implementation to be determined by the RESO Research & Development Workgroup. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `SearchQuery` | `search_query` | String |  | The textual representation of the search performed by the member that was saved. It is required to present in the OData $filter format. Additional formats are under review. See additional documentation for specific requirements for this field. | Free-form text, up to 8000 characters. |  |
| `SearchQueryExceptionDetails` | `search_query_exception_details` | String |  | A free-text description used to expand on the SearchQueryExceptions selections made by the host. | Free-form text, up to 255 characters. |  |
| `SearchQueryExceptions` | `search_query_exceptions` | enum | [`search_query_exceptions`](../lookups.md#search_query_exceptions) | A list of exceptions or errors with the given search query during its creation by the host. Analogous to an error code, this is the host's opportunity to describe an inability to fully express a saved search under the constraints of the given protocol (i.e., $filter). The client may use this information to bring attention to the user about a given saved search and a need to review or recreate the search. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `SearchQueryHumanReadable` | `search_query_human_readable` | String |  | A human readable version of the search query that is commonly used for display and may not contain all actual criteria. For actual search criteria, use the SearchQuery field. | Free-form text, up to 255 characters. |  |
| `SearchQueryType` | `search_query_type` | enum | [`search_query_type`](../lookups.md#search_query_type) | A pick list of the type of query language used in the SearchQuery field (e.g., DMQL2, $filter). | Pick exactly one of 2 values from the lookup (closed list). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the SavedSearch record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the record provider of the saved search. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |

## Foreign keys OUT (this resource references)

- `saved_search.member_key` -> `member.member_key` (high)

## Foreign keys IN (other resources reference this)

- `prospecting.saved_search_key` -> `saved_search.saved_search_key` (high)

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `saved_search`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `member_mls_id` | `member_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |

