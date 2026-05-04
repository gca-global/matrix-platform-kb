# ShowingAppointment

Fields associated with showing appointments, including method, date, time and more.

**RESO DD 2.0** — 12 fields · last revised 6/16/2022 · [dd.reso.org](https://dd.reso.org/DD2.0/ShowingAppointment/)

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ModificationTimestamp/) |
| `ShowingAgentKey` | String |  |  |  | A system unique identifier of the member who has scheduled to access the property. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAgentKey/) |
| `ShowingAgentMlsId` | String |  |  |  | The MemberMlsId of the agent who is showing the property. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAgentMlsId/) |
| `ShowingAppointmentDate` | Date |  |  |  | The date of the showing appointment. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentDate/) |
| `ShowingAppointmentEndTime` | Timestamp |  |  |  | The end date and time of the showing appointment (ISO 8601). | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentEndTime/) |
| `ShowingAppointmentId` | String |  |  |  | A system-unique identifier for the showing appointment. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentId/) |
| `ShowingAppointmentKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentKey/) |
| `ShowingAppointmentMethod` | String List, Multi |  | [ShowingAppointmentMethod](#showingappointmentmethod) |  | The way the showing appointment was scheduled or will be conducted. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentMethod/) |
| `ShowingAppointmentStartTime` | Timestamp |  |  |  | The start date and time of the showing appointment (ISO 8601). | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentStartTime/) |
| `ShowingAppointmentStatus` | String List, Single |  | [ShowingAppointmentStatus](#showingappointmentstatus) |  | The status of the showing appointment. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingAppointmentStatus/) |
| `ShowingId` | String |  |  |  | The well-known identifier for the showing record. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingId/) |
| `ShowingKey` | String |  |  |  | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/ShowingAppointment/ShowingKey/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentMlsId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentEndTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentMethod</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentStartTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAppointmentStatus</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ShowingAppointmentMethod

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingAppointmentMethod/)

| Value | Definition |
|---|---|
| `In-Person` | An in-person showing appointment is confirmed for this property. |
| `Other` | A showing appointment type other than those available on this list is confirmed for this property. |
| `Virtual` | A virtual showing appointment is confirmed for this property. |

### ShowingAppointmentStatus

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingAppointmentStatus/)

| Value | Definition |
|---|---|
| `Cancelled` | The status of this appointment request is canceled. |
| `Confirmed` | The status of this appointment request is confirmed. |
| `Denied` | The status of this appointment request is denied. |
| `Pending` | The status of this appointment request is pending. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
