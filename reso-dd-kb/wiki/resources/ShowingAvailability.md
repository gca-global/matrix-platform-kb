# ShowingAvailability

Fields associated with property availability for showings, including method, dates and duration.

**RESO DD 2.0** — 12 fields · last revised 6/16/2022 · [dd.reso.org](https://dd.reso.org/DD2.0/ShowingAvailability/)

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ModificationTimestamp/) |
| `ShowingAvailabilityKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingAvailabilityKey/) |
| `ShowingAvailableEndTime` | Timestamp |  |  |  | End Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingAvailableEndTime/) |
| `ShowingAvailableStartTime` | Timestamp |  |  |  | Start Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingAvailableStartTime/) |
| `ShowingDate` | Date |  |  |  | The date that showing appointments can be requested. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingDate/) |
| `ShowingId` | String |  |  |  | The well-known identifier for the showing record. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingId/) |
| `ShowingKey` | String |  |  |  | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingKey/) |
| `ShowingMaximumDuration` | String |  |  |  | The maximum block of time available for a showing. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingMaximumDuration/) |
| `ShowingMethod` | String List, Multi |  | [ShowingMethod](#showingmethod) |  | The type of showings (i.e., in-person, virtual, etc.) allowed for the property. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingMethod/) |
| `ShowingMinimumDuration` | String |  |  |  | The minimum block of time available for a showing. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/ShowingMinimumDuration/) |
| `UniqueOrganizationIdentifier` | String |  |  |  | This is the unique ID assigned to organizations included in the OUID Resource. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/UniqueOrganizationIdentifier/) |
| `UniversalPropertyId` | String |  |  |  | The Universal Property Identifier (UPI) is a unique identifier based on country and local identification methods for all real property in the U.S. | [link](https://dd.reso.org/DD2.0/ShowingAvailability/UniversalPropertyId/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailabilityKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailableEndTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailableStartTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingDate</code></summary>

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

<details><summary><code>ShowingMaximumDuration</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingMethod</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingMinimumDuration</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>UniqueOrganizationIdentifier</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>UniversalPropertyId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/16/2022
  - **Revision Date:** 6/16/2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ShowingMethod

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingMethod/)

| Value | Definition |
|---|---|
| `In-Person` | In-person showings are allowed for this property. |
| `Other` | Other types of showings are allowed for this property. |
| `Virtual` | Virtual showings are allowed for this property. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
