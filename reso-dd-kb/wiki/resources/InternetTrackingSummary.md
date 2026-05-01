# InternetTrackingSummary

_RESO Data Dictionary 2.0 resource — 27 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/InternetTrackingSummary+Resource) for the canonical page._

## Groups

- **Other** — 27 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `CmaCreatedCount` | Number |  |  |  |  | The sum of Competitive Market Analysis (CMA) reports created. | [link](https://ddwiki.reso.org/display/DDW20/CmaCreatedCount+Field) |
| `CmaEmailedCount` | Number |  |  |  |  | The sum of Competitive Market Analysis (CMA) reports emailed. | [link](https://ddwiki.reso.org/display/DDW20/CmaEmailedCount+Field) |
| `CmaRanCount` | Number |  |  |  |  | The sum of Competitive Market Analysis (CMA) reports ran. | [link](https://ddwiki.reso.org/display/DDW20/CmaRanCount+Field) |
| `CmaSharedCount` | Number |  |  |  |  | The sum of Competitive Market Analysis (CMA) reports shared (on social media, SMS, etc.). | [link](https://ddwiki.reso.org/display/DDW20/CmaSharedCount+Field) |
| `EndTimestamp` | Timestamp |  |  |  |  | Indicates the ending timestamp the data is representing. | [link](https://ddwiki.reso.org/display/DDW20/EndTimestamp+Field) |
| `FavoritedCount` | Number |  |  |  |  | The sum of favorited events (liked, starred, add-to-list, etc.) the listing obtained. | [link](https://ddwiki.reso.org/display/DDW20/FavoritedCount+Field) |
| `ImpressionCount` | Number |  |  |  |  | The aggregated sum of impressions that the object obtained during the summary time period. | [link](https://ddwiki.reso.org/display/DDW20/ImpressionCount+Field) |
| `InquiryCount` | Number |  |  |  |  | The sum of end-user inquiry events; also referred to as leads. | [link](https://ddwiki.reso.org/display/DDW20/InquiryCount+Field) |
| `InternetTrackingSummaryKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/InternetTrackingSummaryKey+Field) |
| `ListingId` | String |  |  |  |  | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136047) |
| `ListingsEmailedCount` | Number |  |  |  |  | The sum of emails the listing was involved in. | [link](https://ddwiki.reso.org/display/DDW20/ListingsEmailedCount+Field) |
| `MobileAppImpressionCount` | Number |  |  |  |  | The sum of impressions derived from a mobile app, not a browser. | [link](https://ddwiki.reso.org/display/DDW20/MobileAppImpressionCount+Field) |
| `MobileAppViewCount` | Number |  |  |  |  | The sum of views derived from a mobile app, not a browser. | [link](https://ddwiki.reso.org/display/DDW20/MobileAppViewCount+Field) |
| `MobileLogins` | Number |  |  |  |  | The sum of logins on the product from a mobile device. | [link](https://ddwiki.reso.org/display/DDW20/MobileLogins+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136059) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating system from which this data is derived from. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136065) |
| `ResponseType` | String List, Single |  | [ResponseTypes](#responsetypes) |  |  | An open enumeration that defines the InternetTracking data set in the transaction (e.g., summary data or single events). | [link](https://ddwiki.reso.org/display/DDW20/ResponseType+Field) |
| `SharedCount` | Number |  |  |  |  | The sum of shares (social media, SMS, etc.) the listing was part of. | [link](https://ddwiki.reso.org/display/DDW20/SharedCount+Field) |
| `ShowingCompletedCount` | Number |  |  |  |  | The sum of showings completed. | [link](https://ddwiki.reso.org/display/DDW20/ShowingCompletedCount+Field) |
| `ShowingRequestedCount` | Number |  |  |  |  | The sum of showings requested. | [link](https://ddwiki.reso.org/display/DDW20/ShowingRequestedCount+Field) |
| `StartTimestamp` | Timestamp |  |  |  |  | Indicates the starting timestamp the data is representing. | [link](https://ddwiki.reso.org/display/DDW20/StartTimestamp+Field) |
| `TotalLogins` | Number |  |  |  |  | The sum of logins on the product. | [link](https://ddwiki.reso.org/display/DDW20/TotalLogins+Field) |
| `TrackingDate` | Date |  |  |  |  | The actual date the summary data pertains to. | [link](https://ddwiki.reso.org/display/DDW20/TrackingDate+Field) |
| `TrackingType` | String List, Single |  | [TrackingType](#trackingtype) |  |  | Defines the type of tracking data being sought (e.g., Office, Agent), a single listing itself or the entire data set from a Unique Organization Identifier (UOI). | [link](https://ddwiki.reso.org/display/DDW20/TrackingType+Field) |
| `TrackingValues` | String |  |  |  |  | The comma-delimited values that relate to the TrackingType field in the search. | [link](https://ddwiki.reso.org/display/DDW20/TrackingValues+Field) |
| `UniqueLogins` | Number |  |  |  |  | The sum of logins on the product that are unique. | [link](https://ddwiki.reso.org/display/DDW20/UniqueLogins+Field) |
| `ViewCount` | Number |  |  |  |  | The sum of detailed views the listing obtained. | [link](https://ddwiki.reso.org/display/DDW20/ViewCount+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>CmaCreatedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaEmailedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaRanCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CmaSharedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>EndTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 21 2021
  - **Revision Date:** APR 21 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FavoritedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ImpressionCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>InquiryCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 21 2021
  - **Revision Date:** APR 21 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingsEmailedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileAppImpressionCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileAppViewCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MobileLogins</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ResponseType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 21 2021
  - **Revision Date:** APR 21 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SharedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingCompletedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingRequestedCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TotalLogins</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TrackingDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TrackingValues</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 25 2022
  - **Revision Date:** OCT 25 2022
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ResponseTypes

| Value | Definition |
|---|---|
| `Events` | The client/server data exchange is working with event-level InternetTracking data. |
| `Summary` | The client/server are working with summary-level InternetTracking data. |

### TrackingType

| Value | Definition |
|---|---|
| `ListAgentMlsId` | Indicates that the ListAgentMlsId is the focus of the tracking search. |
| `ListingId` | Indicates that the ListingId is the focus of the tracking search. |
| `ListOfficeMlsId` | Indicates that the ListOfficeMlsId is the focus of the tracking search. |
| `MainOfficeMlsId` | Indicates that the MainOfficeMLSId is the focus of the tracking search. |
| `OUID` | Indicates that the RESO Unique Organization Identifier (UOI) is the focus of the tracking search. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
