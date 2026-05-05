[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `internet_tracking_summary` (InternetTrackingSummary)

> Sum of specific tracking events over a period of time, such as listings viewed or shared.

## At a glance

| | |
|---|---|
| **Primary key** | `internet_tracking_summary_key` |
| **Fields on dd.reso.org** | 27 |
| **Columns in canonical DBML** | 27 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/InternetTrackingSummary/](https://dd.reso.org/DD2.0/InternetTrackingSummary/) |
| **Last revised upstream** | 4/21/2021 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `CmaCreatedCount` | `cma_created_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports created. | Numeric (integer). |  |
| `CmaEmailedCount` | `cma_emailed_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports emailed. | Numeric (integer). |  |
| `CmaRanCount` | `cma_ran_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports ran. | Numeric (integer). |  |
| `CmaSharedCount` | `cma_shared_count` | Number |  | The sum of Competitive Market Analysis (CMA) reports shared (on social media, SMS, etc.). | Numeric (integer). |  |
| `EndTimestamp` | `end_timestamp` | Timestamp |  | Indicates the ending timestamp the data is representing. | ISO-8601 timestamp (UTC). |  |
| `FavoritedCount` | `favorited_count` | Number |  | The sum of favorited events (liked, starred, add-to-list, etc.) the listing obtained. | Numeric (integer). |  |
| `ImpressionCount` | `impression_count` | Number |  | The aggregated sum of impressions that the object obtained during the summary time period. | Numeric (integer). |  |
| `InquiryCount` | `inquiry_count` | Number |  | The sum of end-user inquiry events; also referred to as leads. The end-user submitted an inquiry for more information (e.g., click of a button or link). | Numeric (integer). |  |
| `InternetTrackingSummaryKey` | `internet_tracking_summary_key` | String |  | A system unique identifier. Specifically, the local key to the InternetTrackingSummary resource. | Unique key for this resource. Use as the FK target whenever another resource references `internet_tracking_summary`. | `pk` |
| `ListingId` | `listing_id` | String |  | The unique ID that the summary data is based on, when applicable. | Free-form text, up to 255 characters. |  |
| `ListingsEmailedCount` | `listings_emailed_count` | Number |  | The sum of emails the listing was involved in. | Numeric (integer). |  |
| `MobileAppImpressionCount` | `mobile_app_impression_count` | Number |  | The sum of impressions derived from a mobile app, not a browser. | Numeric (integer). |  |
| `MobileAppViewCount` | `mobile_app_view_count` | Number |  | The sum of views derived from a mobile app, not a browser. | Numeric (integer). |  |
| `MobileLogins` | `mobile_logins` | Number |  | The sum of logins on the product from a mobile device. | Numeric (integer). |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the InternetTrackingSummary record was last modified. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating system from which this data is derived from. | Free-form text, up to 255 characters. |  |
| `ResponseType` | `response_type` | enum | [`response_types`](../lookups.md#response_types) | An open enumeration that defines the InternetTracking data set in the transaction (e.g., summary data or single events). | Pick exactly one of 2 values from the lookup (closed list). |  |
| `SharedCount` | `shared_count` | Number |  | The sum of shares (social media, SMS, etc.) the listing was part of. | Numeric (integer). |  |
| `ShowingCompletedCount` | `showing_completed_count` | Number |  | The sum of showings completed. | Numeric (integer). |  |
| `ShowingRequestedCount` | `showing_requested_count` | Number |  | The sum of showings requested. | Numeric (integer). |  |
| `StartTimestamp` | `start_timestamp` | Timestamp |  | Indicates the starting timestamp the data is representing. | ISO-8601 timestamp (UTC). |  |
| `TotalLogins` | `total_logins` | Number |  | The sum of logins on the product. | Numeric (integer). |  |
| `TrackingDate` | `tracking_date` | Date |  | The actual date the summary data pertains to. | Date (YYYY-MM-DD). |  |
| `TrackingType` | `tracking_type` | enum | [`tracking_type`](../lookups.md#tracking_type) | Defines the type of tracking data being sought (e.g., Office, Agent), a single listing itself or the entire data set from a Unique Organization Identifier (UOI). | Pick exactly one of 5 values from the lookup (closed list). |  |
| `TrackingValues` | `tracking_values` | String |  | The comma-delimited values that relate to the TrackingType field in the search. | Free-form text, up to 255 characters. |  |
| `UniqueLogins` | `unique_logins` | Number |  | The sum of logins on the product that are unique. | Numeric (integer). |  |
| `ViewCount` | `view_count` | Number |  | The sum of detailed views the listing obtained. | Numeric (integer). |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

