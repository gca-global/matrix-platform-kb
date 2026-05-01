# ShowingRequest

_RESO Data Dictionary 2.0 resource — 17 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/ShowingRequest+Resource) for the canonical page._

## Groups

- **Other** — 17 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136146) |
| `ShowingAgentKey` | String |  |  |  |  | A system unique identifier of the member who has scheduled to access the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136151) |
| `ShowingAgentMlsId` | String |  |  |  |  | The MemberMlsId of the agent who is showing the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136159) |
| `ShowingId` | String |  |  |  |  | The well-known identifier for the showing record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136164) |
| `ShowingKey` | String |  |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136170) |
| `ShowingMethodRequest` | String List, Multi |  | [ShowingMethodRequest](#showingmethodrequest) |  |  | The method of showing (i.e., in-person, virtual, etc.) requested for the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingMethodRequest+Field) |
| `ShowingRequestDate` | Date |  |  |  |  | The date that the showing request was made. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestDate+Field) |
| `ShowingRequestDuration` | String |  |  |  |  | The amount of time requested for the showing. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestDuration+Field) |
| `ShowingRequestEndTime` | Timestamp |  |  |  |  | The local end time of the showing request. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestEndTime+Field) |
| `ShowingRequestId` | String |  |  |  |  | The requestor's unique ID attached to the request. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestId+Field) |
| `ShowingRequestKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestKey+Field) |
| `ShowingRequestNotes` | String |  |  |  |  | The notes supplementing the request, provided by the requestor. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestNotes+Field) |
| `ShowingRequestStartTime` | Timestamp |  |  |  |  | The local start time of the showing request. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestStartTime+Field) |
| `ShowingRequestType` | String List, Multi |  | [ShowingRequestType](#showingrequesttype) |  |  | The type of showing being requested (e.g., first, second, broker preview, broker price opinion, inspection). | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestType+Field) |
| `ShowingRequestedDate` | Date |  |  |  |  | The date when the showing was requested. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestedDate+Field) |
| `ShowingRequestedTimestamp` | Timestamp |  |  |  |  | The date/time when the showing agent submitted a request to access the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136200) |
| `ShowingRequestor` | String List, Multi |  | [ShowingRequestor](#showingrequestor) |  |  | The role of the person making the request (e.g., showing agent, inspector, buyer, tenant). | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestor+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ShowingAgentMlsId</code></summary>

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

<details><summary><code>ShowingMethodRequest</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestDuration</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestEndTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestStartTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestedDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestedTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestor</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 16 2022
  - **Revision Date:** JUN 16 2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ShowingMethodRequest

| Value | Definition |
|---|---|
| `In-Person` | An in-person showing has been requested for this property. |
| `Other` | A showing type other than those available on this list has been requested for this property. |
| `Virtual` | A virtual showing has been requested for this property. |

### ShowingRequestType

| Value | Definition |
|---|---|
| `Broker Preview` | A broker preview showing request made on a property. |
| `Broker Price Opinion` | A broker price opinion showing request made on a property. |
| `First` | The first showing request being made on a property. |
| `Inspection` | An inspection showing request made on a property. |
| `Second` | The second showing request made on a property. |
| `Walk-through` | A walk-through showing request made on the property. |

### ShowingRequestor

| Value | Definition |
|---|---|
| `Agent` | The role of the person making the request is an agent. |
| `Consumer` | The role of the person making the request is a consumer. |
| `Home Improvement Specialist` | The role of the person making the request is a home improvement specialist. |
| `Home Inspector` | The role of the person making the request is a home inspector. |
| `Home Security Provider` | The role of the person making the request is a home security provider. |
| `Member Type` | The type of member (i.e., agent, broker, office manager, appraiser, REALTOR®, photographer, etc.) |
| `Moving Storage` | The role of the person making the request works at a moving/storage company. |
| `Occupant` | The role of the person making the request is an occupant. |
| `Owner` | The role of the person making the request is an owner. |
| `Property Manager` | The role of the person making the request is a property manager. |
| `Sales Office` | The role of the person making the request is a member of a sales office. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
