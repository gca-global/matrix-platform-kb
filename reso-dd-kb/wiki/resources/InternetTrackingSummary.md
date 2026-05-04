# InternetTrackingSummary

Sum of specific tracking events over a period of time, such as listings viewed or shared.

**RESO DD 2.0** — 27 fields · last revised 4/21/2021 · [dd.reso.org](https://dd.reso.org/DD2.0/InternetTrackingSummary/)

## Groups

- **Other** — 27 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `CmaCreatedCount` | Number |  |  |  | The sum of Competitive Market Analysis (CMA) reports created. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/CmaCreatedCount/) |
| `CmaEmailedCount` | Number |  |  |  | The sum of Competitive Market Analysis (CMA) reports emailed. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/CmaEmailedCount/) |
| `CmaRanCount` | Number |  |  |  | The sum of Competitive Market Analysis (CMA) reports ran. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/CmaRanCount/) |
| `CmaSharedCount` | Number |  |  |  | The sum of Competitive Market Analysis (CMA) reports shared (on social media, SMS, etc.). | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/CmaSharedCount/) |
| `EndTimestamp` | Timestamp |  |  |  | Indicates the ending timestamp the data is representing. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/EndTimestamp/) |
| `FavoritedCount` | Number |  |  |  | The sum of favorited events (liked, starred, add-to-list, etc.) the listing obtained. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/FavoritedCount/) |
| `ImpressionCount` | Number |  |  |  | The aggregated sum of impressions that the object obtained during the summary time period. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ImpressionCount/) |
| `InquiryCount` | Number |  |  |  | The sum of end-user inquiry events; also referred to as leads. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/InquiryCount/) |
| `InternetTrackingSummaryKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/InternetTrackingSummaryKey/) |
| `ListingId` | String |  |  |  | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ListingId/) |
| `ListingsEmailedCount` | Number |  |  |  | The sum of emails the listing was involved in. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ListingsEmailedCount/) |
| `MobileAppImpressionCount` | Number |  |  |  | The sum of impressions derived from a mobile app, not a browser. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/MobileAppImpressionCount/) |
| `MobileAppViewCount` | Number |  |  |  | The sum of views derived from a mobile app, not a browser. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/MobileAppViewCount/) |
| `MobileLogins` | Number |  |  |  | The sum of logins on the product from a mobile device. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/MobileLogins/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ModificationTimestamp/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating system from which this data is derived from. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/OriginatingSystemName/) |
| `ResponseType` | String List, Single |  | [ResponseTypes](#responsetypes) |  | An open enumeration that defines the InternetTracking data set in the transaction (e.g., summary data or single events). | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ResponseType/) |
| `SharedCount` | Number |  |  |  | The sum of shares (social media, SMS, etc.) the listing was part of. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/SharedCount/) |
| `ShowingCompletedCount` | Number |  |  |  | The sum of showings completed. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ShowingCompletedCount/) |
| `ShowingRequestedCount` | Number |  |  |  | The sum of showings requested. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ShowingRequestedCount/) |
| `StartTimestamp` | Timestamp |  |  |  | Indicates the starting timestamp the data is representing. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/StartTimestamp/) |
| `TotalLogins` | Number |  |  |  | The sum of logins on the product. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/TotalLogins/) |
| `TrackingDate` | Date |  |  |  | The actual date the summary data pertains to. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/TrackingDate/) |
| `TrackingType` | String List, Single |  | [TrackingType](#trackingtype) |  | Defines the type of tracking data being sought (e.g., Office, Agent), a single listing itself or the entire data set from a Unique Organization Identifier (UOI). | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/TrackingType/) |
| `TrackingValues` | String |  |  |  | The comma-delimited values that relate to the TrackingType field in the search. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/TrackingValues/) |
| `UniqueLogins` | Number |  |  |  | The sum of logins on the product that are unique. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/UniqueLogins/) |
| `ViewCount` | Number |  |  |  | The sum of detailed views the listing obtained. | [link](https://dd.reso.org/DD2.0/InternetTrackingSummary/ViewCount/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>CmaCreatedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaEmailedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaRanCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaSharedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>EndTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/21/2021
  - **Revision Date:** 4/21/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FavoritedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ImpressionCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>InquiryCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/21/2021
  - **Revision Date:** 4/21/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>InternetTrackingSummaryKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingsEmailedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileAppImpressionCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileAppViewCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileLogins</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ResponseType</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/21/2021
  - **Revision Date:** 4/21/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SharedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingCompletedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestedCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StartTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/21/2021
  - **Revision Date:** 4/21/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TotalLogins</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TrackingDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TrackingType</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TrackingValues</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>UniqueLogins</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ViewCount</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/25/2022
  - **Revision Date:** 10/25/2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ResponseTypes

2 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ResponseTypes/)

| Value | Definition |
|---|---|
| `Events` | The client/server data exchange is working with event-level InternetTracking data. |
| `Summary` | The client/server are working with summary-level InternetTracking data. |

### TrackingType

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/TrackingType/)

| Value | Definition |
|---|---|
| `ListAgentMlsId` | Indicates that the ListAgentMlsId is the focus of the tracking search. |
| `ListingId` | Indicates that the ListingId is the focus of the tracking search. |
| `ListOfficeMlsId` | Indicates that the ListOfficeMlsId is the focus of the tracking search. |
| `MainOfficeMlsId` | Indicates that the MainOfficeMLSId is the focus of the tracking search. |
| `OUID` | Indicates that the RESO Unique Organization Identifier (UOI) is the focus of the tracking search. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
