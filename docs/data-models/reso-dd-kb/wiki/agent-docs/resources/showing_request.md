[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `showing_request` (ShowingRequest)

> Fields associated with showing requests, including method, date, time and more.

## At a glance

| | |
|---|---|
| **Primary key** | `showing_request_key` |
| **Fields on dd.reso.org** | 17 |
| **Columns in canonical DBML** | 17 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 1 |
| **Source** | [https://dd.reso.org/DD2.0/ShowingRequest/](https://dd.reso.org/DD2.0/ShowingRequest/) |
| **Last revised upstream** | 6/16/2022 |

## Relationship diagram

```mermaid
flowchart LR
    showing_request["showing_request"]
    member["member"]
    showing_request -->|"showing_agent_key"| member
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingRequest record was last modified. | ISO-8601 timestamp (UTC). |  |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. Specifically, in aggregation systems, the ListAgentKey is the system unique identifier from the system in which the record was retrieved. This may be identical to the related xxxId and is a foreign key relating to the MemberKey of the Member Resource. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `ShowingAgentMlsId` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. This value may not be unique. Specifically, in the case of aggregation systems, this value should be the identifier from the original system. | Free-form text, up to 25 characters. | `[REVIEW]` |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. The value may be identical to that of the ShowingKey, but the ShowingId is intended to be the value used by a human to retrieve the information about a specific showing. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemKey and OriginatingSystemKey. | Free-form text, up to 255 characters. |  |
| `ShowingMethodRequest` | `showing_method_request` | varchar (multi) | [`showing_method_request`](../lookups.md#showing_method_request) | The method of showing (i.e., in-person, virtual, etc.) requested for the property. | Pick one or more of 3 values from the lookup (closed list). |  |
| `ShowingRequestDate` | `showing_request_date` | Date |  | The date that the showing request was made. | Date (YYYY-MM-DD). |  |
| `ShowingRequestDuration` | `showing_request_duration` | String |  | The amount of time requested for the showing. | Free-form text, up to 50 characters. |  |
| `ShowingRequestEndTime` | `showing_request_end_time` | Timestamp |  | The local end time of the showing request. The locale is defined by the showing. | ISO-8601 timestamp (UTC). |  |
| `ShowingRequestId` | `showing_request_id` | String |  | The requestor's unique ID attached to the request. | Free-form text, up to 255 characters. |  |
| `ShowingRequestKey` | `showing_request_key` | String |  | A system unique identifier. Specifically, the local key to the ShowingRequest resource. | Unique key for this resource. Use as the FK target whenever another resource references `showing_request`. | `pk` |
| `ShowingRequestNotes` | `showing_request_notes` | String |  | The notes supplementing the request, provided by the requestor. | Free-form text, up to 255 characters. |  |
| `ShowingRequestStartTime` | `showing_request_start_time` | Timestamp |  | The local start time of the showing request. The locale is defined by the showing. | ISO-8601 timestamp (UTC). |  |
| `ShowingRequestType` | `showing_request_type` | varchar (multi) | [`showing_request_type`](../lookups.md#showing_request_type) | The type of showing being requested (e.g., first, second, broker preview, broker price opinion, inspection). | Pick one or more of 6 values from the lookup (closed list). |  |
| `ShowingRequestedDate` | `showing_requested_date` | Date |  | The date when the showing was requested. | Date (YYYY-MM-DD). |  |
| `ShowingRequestedTimestamp` | `showing_requested_timestamp` | Timestamp |  | The date/time when the showing agent submitted a request to access the property. This is a system timestamp normally generated by a showing system, which is commonly the originating system for showing records. | ISO-8601 timestamp (UTC). |  |
| `ShowingRequestor` | `showing_requestor` | varchar (multi) | [`showing_requestor`](../lookups.md#showing_requestor) | The role of the person making the request (e.g., showing agent, inspector, buyer, tenant). | Pick one or more of 11 values from the lookup (closed list). |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`ShowingKey` vs `ShowingId`**:
  - `ShowingKey` - A unique identifier for this record from the immediate source.
  - `ShowingId` - The well-known identifier for the showing record.
- **`ShowingRequestKey` vs `ShowingRequestId`**:
  - `ShowingRequestKey` - A system unique identifier.
  - `ShowingRequestId` - The requestor's unique ID attached to the request.

## Foreign keys OUT (this resource references)

- `showing_request.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `review` | jaccard_0.67_below_id_threshold_0.7 |

