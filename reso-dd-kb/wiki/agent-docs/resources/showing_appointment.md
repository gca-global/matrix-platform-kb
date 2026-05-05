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

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingAppointment record was last modified. |  |
| `ShowingAgentKey` | `showing_agent_key` | String |  | A system unique identifier of the member who has scheduled to access the property. | `-> member.member_key` |
| `ShowingAgentMlsId` | `showing_agent_mls_id` | String |  | The local, well-known identifier for the member who has scheduled to access the property, most commonly representing a buyer. | `[REVIEW]` |
| `ShowingAppointmentDate` | `showing_appointment_date` | Date |  | The date of the showing appointment. |  |
| `ShowingAppointmentEndTime` | `showing_appointment_end_time` | Timestamp |  | The local end time of the showing appointment. |  |
| `ShowingAppointmentId` | `showing_appointment_id` | String |  | The ID assigned to a requested appointment. |  |
| `ShowingAppointmentKey` | `showing_appointment_key` | String |  | A system unique identifier. | `pk` |
| `ShowingAppointmentMethod` | `showing_appointment_method` | varchar (multi) | [`showing_appointment_method`](../lookups.md#showing_appointment_method) | The method of showing (i.e., in-person, virtual, etc.) confirmed for the property. |  |
| `ShowingAppointmentStartTime` | `showing_appointment_start_time` | Timestamp |  | The local start time of the showing appointment. |  |
| `ShowingAppointmentStatus` | `showing_appointment_status` | enum | [`showing_appointment_status`](../lookups.md#showing_appointment_status) | The status of the requested showing appointment. |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. |  |

## Foreign keys OUT (this resource references)

- `showing_appointment.showing_agent_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `showing_agent_mls_id` | `showing_agent_key` -> `member.member_mls_id` | `review` | jaccard_0.67_below_id_threshold_0.7 |

