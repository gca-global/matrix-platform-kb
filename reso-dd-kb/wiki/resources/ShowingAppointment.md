# ShowingAppointment

The ShowingAppointment resource describes a scheduled in-person showing of a Property by a buyer's agent. It captures the appointment time window, the showing agent, the appointment status, and how the appointment was made (Method).

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136101) |
| `ShowingAgentKey` | String |  |  |  |  | A system unique identifier of the member who has scheduled to access the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136106) |
| `ShowingAgentMlsId` | String |  |  |  |  | The MemberMlsId of the agent who is showing the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136112) |
| `ShowingAppointmentDate` | Date |  |  |  |  | The date of the showing appointment. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentDate+Field) |
| `ShowingAppointmentEndTime` | Timestamp |  |  |  |  | The end date and time of the showing appointment (ISO 8601). | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentEndTime+Field) |
| `ShowingAppointmentId` | String |  |  |  |  | A system-unique identifier for the showing appointment. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentId+Field) |
| `ShowingAppointmentKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentKey+Field) |
| `ShowingAppointmentMethod` | String List, Multi |  | [ShowingAppointmentMethod](#showingappointmentmethod) |  |  | The way the showing appointment was scheduled or will be conducted. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentMethod+Field) |
| `ShowingAppointmentStartTime` | Timestamp |  |  |  |  | The start date and time of the showing appointment (ISO 8601). | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentStartTime+Field) |
| `ShowingAppointmentStatus` | String List, Single |  | [ShowingAppointmentStatus](#showingappointmentstatus) |  |  | The status of the showing appointment. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAppointmentStatus+Field) |
| `ShowingId` | String |  |  |  |  | The well-known identifier for the showing record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136162) |
| `ShowingKey` | String |  |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136167) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ShowingAgentKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentEndTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentMethod</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentStartTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentStatus</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ShowingAppointmentMethod

| Value | Definition |
|---|---|
| `In-Person` | An in-person showing appointment is confirmed for this property. |
| `Other` | A showing appointment type other than those available on this list is confirmed for this property. |
| `Virtual` | A virtual showing appointment is confirmed for this property. |

### ShowingAppointmentStatus

| Value | Definition |
|---|---|
| `Cancelled` | The status of this appointment request is canceled. |
| `Confirmed` | The status of this appointment request is confirmed. |
| `Denied` | The status of this appointment request is denied. |
| `Pending` | The status of this appointment request is pending. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
