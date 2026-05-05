# `internet_tracking_summary` (InternetTrackingSummary)

> Sum of specific tracking events over a period of time, such as listings viewed or shared.

- Source: [https://dd.reso.org/DD2.0/InternetTrackingSummary/](https://dd.reso.org/DD2.0/InternetTrackingSummary/)
- Field count on dd.reso.org: **27**
- Primary key: `internet_tracking_summary_key`
- Last revised upstream: 4/21/2021

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `CmaCreatedCount` | `cma_created_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports created. |  |
| `CmaEmailedCount` | `cma_emailed_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports emailed. |  |
| `CmaRanCount` | `cma_ran_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports ran. |  |
| `CmaSharedCount` | `cma_shared_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports shared (on social media, SMS, etc.). |  |
| `EndTimestamp` | `end_timestamp` | Timestamp |  | Indicates the ending timestamp the data is representing. |  |
| `FavoritedCount` | `favorited_count` | Number |  | The sum of favorited events (liked, starred, add-to-list, etc.) the listing obtained. |  |
| `ImpressionCount` | `impression_count` | Number |  | The aggregated sum of impressions that the object obtained during the summary time period. |  |
| `InquiryCount` | `inquiry_count` | Number |  | The sum of end-user inquiry events; also referred to as leads. |  |
| `InternetTrackingSummaryKey` | `internet_tracking_summary_key` | String |  | A system unique identifier. | `pk` |
| `ListingId` | `listing_id` | String |  | The unique ID that the summary data is based on, when applicable. |  |
| `ListingsEmailedCount` | `listings_emailed_count` | Number |  | The sum of emails the listing was involved in. |  |
| `MobileAppImpressionCount` | `mobile_app_impression_count` | Number |  | The sum of impressions derived from a mobile app, not a browser. |  |
| `MobileAppViewCount` | `mobile_app_view_count` | Number |  | The sum of views derived from a mobile app, not a browser. |  |
| `MobileLogins` | `mobile_logins` | Number |  | The sum of logins on the product from a mobile device. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the InternetTrackingSummary record was last modified. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating system from which this data is derived from. |  |
| `ResponseType` | `response_type` | enum | [`response_types`](../lookups.md#response_types) | An open enumeration that defines the InternetTracking data set in the transaction (e.g., summary data or single events). |  |
| `SharedCount` | `shared_count` | Number |  | The sum of shares (social media, SMS, etc.) the listing was part of. |  |
| `ShowingCompletedCount` | `showing_completed_count` | Number |  | The sum of showings completed. |  |
| `ShowingRequestedCount` | `showing_requested_count` | Number |  | The sum of showings requested. |  |
| `StartTimestamp` | `start_timestamp` | Timestamp |  | Indicates the starting timestamp the data is representing. |  |
| `TotalLogins` | `total_logins` | Number |  | The sum of logins on the product. |  |
| `TrackingDate` | `tracking_date` | Date |  | The actual date the summary data pertains to. |  |
| `TrackingType` | `tracking_type` | enum | [`tracking_type`](../lookups.md#tracking_type) | Defines the type of tracking data being sought (e.g., Office, Agent), a single listing itself or the entire data set from a Unique Organization Identifier (UOI). |  |
| `TrackingValues` | `tracking_values` | String |  | The comma-delimited values that relate to the TrackingType field in the search. |  |
| `UniqueLogins` | `unique_logins` | Number |  | The sum of logins on the product that are unique. |  |
| `ViewCount` | `view_count` | Number |  | The sum of detailed views the listing obtained. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

