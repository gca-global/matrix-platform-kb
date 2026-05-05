# `showing_request` (ShowingRequest)

> Fields associated with showing requests, including method, date, time and more.

- Source: [https://dd.reso.org/DD2.0/ShowingRequest/](https://dd.reso.org/DD2.0/ShowingRequest/)
- Field count on dd.reso.org: **17**
- Primary key: `showing_request_key`
- Last revised upstream: 6/16/2022

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingRequest record was last modified. |  |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. | `-> member.member_key` |
| `ShowingAgentMlsId` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. | `[REVIEW]` |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. |  |
| `ShowingMethodRequest` | `showing_method_request` | varchar (multi) | [`showing_method_request`](../lookups.md#showing_method_request) | The method of showing (i.e., in-person, virtual, etc.) requested for the property. |  |
| `ShowingRequestDate` | `showing_request_date` | Date |  | The date that the showing request was made. |  |
| `ShowingRequestDuration` | `showing_request_duration` | String |  | The amount of time requested for the showing. |  |
| `ShowingRequestEndTime` | `showing_request_end_time` | Timestamp |  | The local end time of the showing request. |  |
| `ShowingRequestId` | `showing_request_id` | String |  | The requestor's unique ID attached to the request. |  |
| `ShowingRequestKey` | `showing_request_key` | String |  | A system unique identifier. | `pk` |
| `ShowingRequestNotes` | `showing_request_notes` | String |  | The notes supplementing the request, provided by the requestor. |  |
| `ShowingRequestStartTime` | `showing_request_start_time` | Timestamp |  | The local start time of the showing request. |  |
| `ShowingRequestType` | `showing_request_type` | varchar (multi) | [`showing_request_type`](../lookups.md#showing_request_type) | The type of showing being requested (e.g., first, second, broker preview, broker price opinion, inspection). |  |
| `ShowingRequestedDate` | `showing_requested_date` | Date |  | The date when the showing was requested. |  |
| `ShowingRequestedTimestamp` | `showing_requested_timestamp` | Timestamp |  | The date/time when the showing agent submitted a request to access the property. |  |
| `ShowingRequestor` | `showing_requestor` | varchar (multi) | [`showing_requestor`](../lookups.md#showing_requestor) | The role of the person making the request (e.g., showing agent, inspector, buyer, tenant). |  |

## Foreign keys OUT (this resource references)

- `showing_request.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `review` | jaccard_0.67_below_id_threshold_0.7 |

