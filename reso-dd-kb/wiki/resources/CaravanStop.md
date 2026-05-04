# CaravanStop

Stops along a caravan tour, connecting Caravan records to Open House records.

**RESO DD 2.0** — 25 fields · last revised 2/3/2021 · [dd.reso.org](https://dd.reso.org/DD2.0/CaravanStop/)

## Groups

- **Other** — 25 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `CaravanKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/CaravanStop/CaravanKey/) |
| `CaravanStopKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/CaravanStop/CaravanStopKey/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/CaravanStop/ModificationTimestamp/) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  | The date/time the CaravanStop record was originally input into the source system. | [link](https://dd.reso.org/DD2.0/CaravanStop/OriginalEntryTimestamp/) |
| `OriginatingSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/CaravanStop/OriginatingSystemId/) |
| `OriginatingSystemKey` | String |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/CaravanStop/OriginatingSystemKey/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/CaravanStop/OriginatingSystemName/) |
| `SourceSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/CaravanStop/SourceSystemId/) |
| `SourceSystemKey` | String |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/CaravanStop/SourceSystemKey/) |
| `SourceSystemName` | String |  |  |  | The name of the caravan stop's record provider. | [link](https://dd.reso.org/DD2.0/CaravanStop/SourceSystemName/) |
| `StopAttendedBy` | String List, Single |  | [CaravanStopAttended](#caravanstopattended) |  | This states whether a caravan stop will be attended by a licensed agent (i.e., Attended by Agent, Attended by the Seller or Unattended). | [link](https://dd.reso.org/DD2.0/CaravanStop/StopAttendedBy/) |
| `StopClassName` | String List, Single |  | [CaravanStopClassName](#caravanstopclassname) |  | The name of the class that that applies to this caravan stop record. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopClassName/) |
| `StopDate` | Date |  |  |  | The date the caravan stop will be open. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopDate/) |
| `StopEndTime` | Timestamp |  |  |  | The time the caravan stop will be closed. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopEndTime/) |
| `StopId` | String |  |  |  | The ID of a caravan stop record. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopId/) |
| `StopKey` | String |  |  |  | The key of a caravan stop record. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopKey/) |
| `StopOrder` | Number |  |  |  | This is used when the order of stops needs to be communicated. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopOrder/) |
| `StopRefreshments` | String |  |  |  | A description of the refreshments that will be served at the caravan stop. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopRefreshments/) |
| `StopRemarks` | String |  |  |  | Comments, instructions or information about the caravan stop. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopRemarks/) |
| `StopResourceName` | String List, Single |  | [CaravanResourceName](#caravanresourcename) |  | The name of the resource that applies to this caravan stop record. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopResourceName/) |
| `StopShowingAgentFirstName` | String |  |  |  | The first name of the showing agent for the caravan stop. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopShowingAgentFirstName/) |
| `StopShowingAgentKey` | String |  |  |  | A system unique identifier for the caravan stop's showing agent. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopShowingAgentKey/) |
| `StopShowingAgentLastName` | String |  |  |  | The last name of the showing agent for the caravan stop. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopShowingAgentLastName/) |
| `StopShowingAgentMlsId` | String |  |  |  | The local, well-known identifier for the showing agent. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopShowingAgentMlsId/) |
| `StopStartTime` | Timestamp |  |  |  | The time the caravan stop will be open. | [link](https://dd.reso.org/DD2.0/CaravanStop/StopStartTime/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>CaravanKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CaravanStopKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopAttendedBy</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopClassName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopEndTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopOrder</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopRefreshments</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopRemarks</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopResourceName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentFirstName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentLastName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopShowingAgentMlsId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StopStartTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 2/3/2021
  - **Revision Date:** 2/3/2021
  - **Added in Version:** 2.0.0

</details>

## Lookups

### CaravanResourceName

7 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CaravanResourceName/)

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

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CaravanStopAttended/)

| Value | Definition |
|---|---|
| `Agent` | The caravan stop will be attended by a licensed agent. |
| `Seller` | The caravan stop will be attended by the seller. |
| `Unattended` | The caravan stop will not be attended. |

### CaravanStopClassName

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CaravanStopClassName/)

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
