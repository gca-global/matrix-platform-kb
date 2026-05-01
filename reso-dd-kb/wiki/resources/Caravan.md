# Caravan

_RESO Data Dictionary 2.0 resource — 33 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/Caravan+Resource) for the canonical page._

## Groups

- **Other** — 33 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `CancellationPolicyUrl` | String |  |  |  |  | The Uniform Resource Locator (aka, URL or link) to the cancellation policy of the tour organizer. | [link](https://ddwiki.reso.org/display/DDW20/CancellationPolicyUrl+Field) |
| `CaravanAllowedClassNames` | String List, Multi |  | [CaravanAllowedClassNames](#caravanallowedclassnames) |  |  | A comma-separated list of the classes allowed by the tour's host. | [link](https://ddwiki.reso.org/display/DDW20/CaravanAllowedClassNames+Field) |
| `CaravanAllowedStatuses` | String List, Multi |  | [CaravanAllowedStatuses](#caravanallowedstatuses) |  |  | A comma-separated list of the listing statuses allowed by the tour's host. | [link](https://ddwiki.reso.org/display/DDW20/CaravanAllowedStatuses+Field) |
| `CaravanAreaDescription` | String |  |  |  |  | A textual description of the geographic or locally known areas that all properties to be included in the tour must be located. | [link](https://ddwiki.reso.org/display/DDW20/CaravanAreaDescription+Field) |
| `CaravanBlackoutDates` | String |  |  |  |  | A comma-separated list of the dates when a reoccurring tour will not take place (e.g., holidays, weekends, etc.). | [link](https://ddwiki.reso.org/display/DDW20/CaravanBlackoutDates+Field) |
| `CaravanDate` | Date |  |  |  |  | The date of the organized tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanDate+Field) |
| `CaravanDaysRecurring` | String |  |  |  |  | Used with unbound timeframes (e.g., second Tuesday of month). | [link](https://ddwiki.reso.org/display/DDW20/CaravanDaysRecurring+Field) |
| `CaravanEndTime` | Timestamp |  |  |  |  | The end time of the organized tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanEndTime+Field) |
| `CaravanInputDeadlineDescription` | String |  |  |  |  | A textual description of the deadline to add a stop (property or open house) to the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanInputDeadlineDescription+Field) |
| `CaravanInputDeadlineTimestamp` | Timestamp |  |  |  |  | A date/time of the deadline to add a stop (property or open house) to the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanInputDeadlineTimestamp+Field) |
| `CaravanKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/CaravanKey+Field) |
| `CaravanName` | String |  |  |  |  | The name or short description of the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanName+Field) |
| `CaravanOrganizerContactInfo` | String |  |  |  |  | Contact information for the tour organizer, such as phone or email. | [link](https://ddwiki.reso.org/display/DDW20/CaravanOrganizerContactInfo+Field) |
| `CaravanOrganizerKey` | String |  |  |  |  | A system unique identifier for the entity hosting the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanOrganizerKey+Field) |
| `CaravanOrganizerMlsId` | String |  |  |  |  | The local, well-known identifier for the entity hosting the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanOrganizerMlsId+Field) |
| `CaravanOrganizerName` | String |  |  |  |  | The name of the entity hosting the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanOrganizerName+Field) |
| `CaravanOrganizerResourceName` | String List, Single |  | [CaravanResourceName](#caravanresourcename) |  |  | The resource or table of the record to which the CaravanOrganizerKey or MlsId refers (i.e., Office, Association, etc.). | [link](https://ddwiki.reso.org/display/DDW20/CaravanOrganizerResourceName+Field) |
| `CaravanPolicyUrl` | String |  |  |  |  | The Uniform Resource Locator (aka, URL or link) to the general tour policies of the tour organizer. | [link](https://ddwiki.reso.org/display/DDW20/CaravanPolicyUrl+Field) |
| `CaravanRemarks` | String |  |  |  |  | The detailed description, directions, policy or other details about the tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanRemarks+Field) |
| `CaravanStartLocation` | String |  |  |  |  | A description or address of the location where the tour begins. | [link](https://ddwiki.reso.org/display/DDW20/CaravanStartLocation+Field) |
| `CaravanStartLocationGiveaways` | String |  |  |  |  | A description of prizes, drawings, etc., that will be given at the tour start location. | [link](https://ddwiki.reso.org/display/DDW20/CaravanStartLocationGiveaways+Field) |
| `CaravanStartLocationRefreshments` | String |  |  |  |  | A description of the refreshments that will be served at the tour start location. | [link](https://ddwiki.reso.org/display/DDW20/CaravanStartLocationRefreshments+Field) |
| `CaravanStartTime` | Timestamp |  |  |  |  | The start time of the organized tour. | [link](https://ddwiki.reso.org/display/DDW20/CaravanStartTime+Field) |
| `CaravanStatus` | String List, Single |  | [CaravanStatus](#caravanstatus) |  |  | Status of the organized tour (e.g., Active, Cancelled, Ended, etc.). | [link](https://ddwiki.reso.org/display/DDW20/CaravanStatus+Field) |
| `CaravanType` | String List, Single |  | [CaravanType](#caravantype) |  |  | The type of organized tour (e.g., AOR, Broker, Other, etc.). | [link](https://ddwiki.reso.org/display/DDW20/CaravanType+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136154) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The date/time the Caravan record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136161) |
| `OriginatingSystemId` | String |  |  |  |  | The RESO UOI's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136168) |
| `OriginatingSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136174) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136181) |
| `SourceSystemId` | String |  |  |  |  | The RESO UOI's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136185) |
| `SourceSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136192) |
| `SourceSystemName` | String |  |  |  |  | The name of the CaravanStop record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136198) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>CaravanAllowedClassNames</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanAllowedStatuses</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanAreaDescription</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanBlackoutDates</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanDaysRecurring</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanEndTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanInputDeadlineDescription</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanOrganizerContactInfo</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanOrganizerKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanOrganizerName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanOrganizerResourceName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanPolicyUrl</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStartLocation</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStartLocationGiveaways</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStartLocationRefreshments</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStartTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStatus</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

## Lookups

### CaravanAllowedClassNames

| Value | Definition |
|---|---|
| `Business Opportunity` | The class, sometimes known as property type, is a business for sale. |
| `Commercial Lease` | The class, sometimes known as property type, is a commercial property for lease. |
| `Commercial Sale` | The class, sometimes known as property type, is a commercial property for sale. |
| `Farm` | The class, sometimes known as property type, is a farm. |
| `Land` | The class, sometimes known as property type, is land for sale or lease. |
| `Manufactured In Park` | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| `Residential` | The class, sometimes known as property type, is residential property for sale. |
| `Residential Income` | The class, sometimes known as property type, is income or multifamily property for sale. |
| `Residential Lease` | The class, sometimes known as property type, is residential property for lease. |

### CaravanAllowedStatuses

| Value | Definition |
|---|---|
| `Active` | The listing is on market, and an offer has not been accepted. |
| `Active Under Contract` | An offer has been accepted, but the listing is still on market. |
| `Pending` | An offer has been accepted, and the listing is no longer on market. |

### CaravanResourceName

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association resource. |
| `Caravan` | This record is related to another record in the Caravan resource. |
| `Contacts` | This record is related to another record in the Contacts resource. |
| `Member` | This record is related to another record in the Member resource. |
| `Office` | This record is related to another record in the Office resource. |
| `OpenHouse` | This record is related to another record in the OpenHouse resource. |
| `Property` | This record is related to another record in the Property resource. |

### CaravanStatus

| Value | Definition |
|---|---|
| `Active` | The organized tour is upcoming or in progress and has not been canceled. |
| `Canceled` | The organized tour has been canceled. |
| `Ended` | The organized tour has occurred and has ended. |

### CaravanType

| Value | Definition |
|---|---|
| `Association` | The tour is being organized by an association or board of REALTORS®. |
| `Broker` | The tour is being organized by a brokerage. |
| `Other` | The tour is being organized by an entity other than an association or brokerage. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
