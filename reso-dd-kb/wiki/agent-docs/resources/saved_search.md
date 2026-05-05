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

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | The class or table to which the SearchQuery criteria refers (e.g., Residential, Residential Lease, Residential Income, Commercial Sale). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The collection history items related to the SavedSearch record. | `[Collection]` |
| `Member` | `member` | Resource |  | The member associated with the saved search. | `[Resource]` |
| `MemberKey` | `member_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. | `[dropped: satellite of member_key]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was entered. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the SavedSearch record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | Unique identifier from the originating system, which is commonly a key to that system. |  |
| `OriginatingSystemMemberName` | `originating_system_member_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource to which the SearchQuery criteria refers (e.g., Property, OpenHouse, Agent, Office, Contacts). |  |
| `SavedSearchDescription` | `saved_search_description` | String |  | A textual description of the saved search input by the member who created the saved search. |  |
| `SavedSearchKey` | `saved_search_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `SavedSearchName` | `saved_search_name` | String |  | The name given to the search by the member inputting the saved search. |  |
| `SavedSearchType` | `saved_search_type` | enum | [`saved_search_type`](../lookups.md#saved_search_type) | Determines if the saved search used to pass criteria is to be stored and executed by the client or if it is a key to be passed to the host for execution (i.e., Client Receives Criteria, Host Returns Listings). |  |
| `SearchQuery` | `search_query` | String |  | The textual representation of the search performed by the member that was saved. |  |
| `SearchQueryExceptionDetails` | `search_query_exception_details` | String |  | A free-text description used to expand on the SearchQueryExceptions selections made by the host. |  |
| `SearchQueryExceptions` | `search_query_exceptions` | enum | [`search_query_exceptions`](../lookups.md#search_query_exceptions) | A list of exceptions or errors with the given search query during its creation by the host. |  |
| `SearchQueryHumanReadable` | `search_query_human_readable` | String |  | A human readable version of the search query that is commonly used for display and may not contain all actual criteria. |  |
| `SearchQueryType` | `search_query_type` | enum | [`search_query_type`](../lookups.md#search_query_type) | A pick list of the type of query language used in the SearchQuery field (e.g., DMQL2, $filter). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the SavedSearch record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the record provider of the saved search. |  |

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

