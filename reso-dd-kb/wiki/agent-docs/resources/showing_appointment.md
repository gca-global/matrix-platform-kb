[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `showing_appointment` (ShowingAppointment)

> Fields associated with showing appointments, including method, date, time and more.

## At a glance

| | |
|---|---|
| **Primary key** | `showing_appointment_key` |
| **Fields on dd.reso.org** | 12 |
| **Columns in canonical DBML** | 12 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 1 |
| **Source** | [https://dd.reso.org/DD2.0/ShowingAppointment/](https://dd.reso.org/DD2.0/ShowingAppointment/) |
| **Last revised upstream** | 6/16/2022 |

## Relationship diagram

```mermaid
flowchart LR
    showing_appointment["showing_appointment"]
    member["member"]
    showing_appointment -->|"showing_agent_key"| member
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingAppointment record was last modified. | ISO-8601 timestamp (UTC). |  |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. Specifically, in aggregation systems, the ListAgentKey is the system unique identifier from the system in which the record was retrieved. This may be identical to the related xxxId and is a foreign key relating to the Member Key of the Member Resource. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `ShowingAgentMlsId` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. This value may not be unique. Specifically, in the case of aggregation systems, this value should be the identifier from the original system. | Free-form text, up to 255 characters. | `[REVIEW]` |
| `ShowingAppointmentDate` | `showing_appointment_date` | Date |  | The date of the showing appointment. | Date (YYYY-MM-DD). |  |
| `ShowingAppointmentEndTime` | `showing_appointment_end_time` | Timestamp |  | The local end time of the showing appointment. The locale is defined by the showing. | ISO-8601 timestamp (UTC). |  |
| `ShowingAppointmentId` | `showing_appointment_id` | String |  | The ID assigned to a requested appointment. | Free-form text, up to 255 characters. |  |
| `ShowingAppointmentKey` | `showing_appointment_key` | String |  | A system unique identifier. Specifically, the local key to the ShowingAppointment resource. | Unique key for this resource. Use as the FK target whenever another resource references `showing_appointment`. | `pk` |
| `ShowingAppointmentMethod` | `showing_appointment_method` | varchar (multi) | [`showing_appointment_method`](../lookups.md#showing_appointment_method) | The method of showing (i.e., in-person, virtual, etc.) confirmed for the property. | Pick one or more of 3 values from the lookup (closed list). |  |
| `ShowingAppointmentStartTime` | `showing_appointment_start_time` | Timestamp |  | The local start time of the showing appointment. The locale is defined by the showing. | ISO-8601 timestamp (UTC). |  |
| `ShowingAppointmentStatus` | `showing_appointment_status` | enum | [`showing_appointment_status`](../lookups.md#showing_appointment_status) | The status of the requested showing appointment. | Pick exactly one of 4 values from the lookup (closed list). |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. The value may be identical to that of the ShowingKey, but the ShowingId is intended to be the value used by a human to retrieve the information about a specific showing. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 25 characters. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemKey and OriginatingSystemKey. | Free-form text, up to 255 characters. |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`ShowingAppointmentKey` vs `ShowingAppointmentId`**:
  - `ShowingAppointmentKey` - A system unique identifier.
  - `ShowingAppointmentId` - The ID assigned to a requested appointment.
- **`ShowingKey` vs `ShowingId`**:
  - `ShowingKey` - A unique identifier for this record from the immediate source.
  - `ShowingId` - The well-known identifier for the showing record.

## Foreign keys OUT (this resource references)

- `showing_appointment.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `review` | jaccard_0.67_below_id_threshold_0.7 |

