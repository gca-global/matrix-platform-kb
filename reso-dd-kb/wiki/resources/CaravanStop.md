# CaravanStop

_RESO Data Dictionary 2.0 resource — 25 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/CaravanStop+Resource) for the canonical page._

## Groups

- **Other** — 25 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `CaravanKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136028) |
| `CaravanStopKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/CaravanStopKey+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136039) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The date/time the CaravanStop record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136045) |
| `OriginatingSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136050) |
| `OriginatingSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136056) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136062) |
| `SourceSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136068) |
| `SourceSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136074) |
| `SourceSystemName` | String |  |  |  |  | The name of the caravan stop's record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136080) |
| `StopAttendedBy` | String List, Single |  | [CaravanStopAttended](#caravanstopattended) |  |  | This states whether a caravan stop will be attended by a licensed agent (i.e., Attended by Agent, Attended by the Seller or Unattended). | [link](https://ddwiki.reso.org/display/DDW20/StopAttendedBy+Field) |
| `StopClassName` | String List, Single |  | [CaravanStopClassName](#caravanstopclassname) |  |  | The name of the class that that applies to this caravan stop record. | [link](https://ddwiki.reso.org/display/DDW20/StopClassName+Field) |
| `StopDate` | Date |  |  |  |  | The date the caravan stop will be open. | [link](https://ddwiki.reso.org/display/DDW20/StopDate+Field) |
| `StopEndTime` | Timestamp |  |  |  |  | The time the caravan stop will be closed. | [link](https://ddwiki.reso.org/display/DDW20/StopEndTime+Field) |
| `StopId` | String |  |  |  |  | The ID of a caravan stop record. | [link](https://ddwiki.reso.org/display/DDW20/StopId+Field) |
| `StopKey` | String |  |  |  |  | The key of a caravan stop record. | [link](https://ddwiki.reso.org/display/DDW20/StopKey+Field) |
| `StopOrder` | Number |  |  |  |  | This is used when the order of stops needs to be communicated. | [link](https://ddwiki.reso.org/display/DDW20/StopOrder+Field) |
| `StopRefreshments` | String |  |  |  |  | A description of the refreshments that will be served at the caravan stop. | [link](https://ddwiki.reso.org/display/DDW20/StopRefreshments+Field) |
| `StopRemarks` | String |  |  |  |  | Comments, instructions or information about the caravan stop. | [link](https://ddwiki.reso.org/display/DDW20/StopRemarks+Field) |
| `StopResourceName` | String List, Single |  | [CaravanResourceName](#caravanresourcename) |  |  | The name of the resource that applies to this caravan stop record. | [link](https://ddwiki.reso.org/display/DDW20/StopResourceName+Field) |
| `StopShowingAgentFirstName` | String |  |  |  |  | The first name of the showing agent for the caravan stop. | [link](https://ddwiki.reso.org/display/DDW20/StopShowingAgentFirstName+Field) |
| `StopShowingAgentKey` | String |  |  |  |  | A system unique identifier for the caravan stop's showing agent. | [link](https://ddwiki.reso.org/display/DDW20/StopShowingAgentKey+Field) |
| `StopShowingAgentLastName` | String |  |  |  |  | The last name of the showing agent for the caravan stop. | [link](https://ddwiki.reso.org/display/DDW20/StopShowingAgentLastName+Field) |
| `StopShowingAgentMlsId` | String |  |  |  |  | The local, well-known identifier for the showing agent. | [link](https://ddwiki.reso.org/display/DDW20/StopShowingAgentMlsId+Field) |
| `StopStartTime` | Timestamp |  |  |  |  | The time the caravan stop will be open. | [link](https://ddwiki.reso.org/display/DDW20/StopStartTime+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>CaravanStopKey</code></summary>

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

<details><summary><code>StopAttendedBy</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopClassName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopEndTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopOrder</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopRefreshments</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopRemarks</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopResourceName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentFirstName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentLastName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentMlsId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** FEB 03 2021
  - **Revision Date:** FEB 03 2021
  - **Added in Version:** 2.0.0

</details>

## Lookups

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

### CaravanStopAttended

| Value | Definition |
|---|---|
| `Agent` | The caravan stop will be attended by a licensed agent. |
| `Seller` | The caravan stop will be attended by the seller. |
| `Unattended` | The caravan stop will not be attended. |

### CaravanStopClassName

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

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
