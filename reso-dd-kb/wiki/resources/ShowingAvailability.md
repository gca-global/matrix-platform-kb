# ShowingAvailability

_RESO Data Dictionary 2.0 resource — 12 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/ShowingAvailability+Resource) for the canonical page._

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136113) |
| `ShowingAvailabilityKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAvailabilityKey+Field) |
| `ShowingAvailableEndTime` | Timestamp |  |  |  |  | End Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | [link](https://ddwiki.reso.org/display/DDW20/ShowingAvailableEndTime+Field) |
| `ShowingAvailableStartTime` | Timestamp |  |  |  |  | Start Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | [link](https://ddwiki.reso.org/display/DDW20/ShowingAvailableStartTime+Field) |
| `ShowingDate` | Date |  |  |  |  | The date that showing appointments can be requested. | [link](https://ddwiki.reso.org/display/DDW20/ShowingDate+Field) |
| `ShowingId` | String |  |  |  |  | The well-known identifier for the showing record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136144) |
| `ShowingKey` | String |  |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136150) |
| `ShowingMaximumDuration` | String |  |  |  |  | The maximum block of time available for a showing. | [link](https://ddwiki.reso.org/display/DDW20/ShowingMaximumDuration+Field) |
| `ShowingMethod` | String List, Multi |  | [ShowingMethod](#showingmethod) |  |  | The type of showings (i.e., in-person, virtual, etc.) allowed for the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingMethod+Field) |
| `ShowingMinimumDuration` | String |  |  |  |  | The minimum block of time available for a showing. | [link](https://ddwiki.reso.org/display/DDW20/ShowingMinimumDuration+Field) |
| `UniqueOrganizationIdentifier` | String |  |  |  |  | This is the unique ID assigned to organizations included in the OUID Resource. | [link](https://ddwiki.reso.org/display/DDW20/UniqueOrganizationIdentifier+Field) |
| `UniversalPropertyId` | String |  |  |  |  | The Universal Property Identifier (UPI) is a unique identifier based on country and local identification methods for all real property in the U.S. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136179) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailabilityKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailableEndTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAvailableStartTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingDate</code></summary>

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

<details><summary><code>ShowingMaximumDuration</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingMethod</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingMinimumDuration</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>UniqueOrganizationIdentifier</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>UniversalPropertyId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ShowingMethod

| Value | Definition |
|---|---|
| `In-Person` | In-person showings are allowed for this property. |
| `Other` | Other types of showings are allowed for this property. |
| `Virtual` | Virtual showings are allowed for this property. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
