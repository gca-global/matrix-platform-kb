# `showing_availability` (ShowingAvailability)

> Fields associated with property availability for showings, including method, dates and duration.

- Source: [https://dd.reso.org/DD2.0/ShowingAvailability/](https://dd.reso.org/DD2.0/ShowingAvailability/)
- Field count on dd.reso.org: **12**
- Primary key: `showing_availability_key`
- Last revised upstream: 6/16/2022

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingAvailability record was last modified. |  |
| `ShowingAvailabilityKey` | `showing_availability_key` | String |  | A system unique identifier. | `pk` |
| `ShowingAvailableEndTime` | `showing_available_end_time` | Timestamp |  | End Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). |  |
| `ShowingAvailableStartTime` | `showing_available_start_time` | Timestamp |  | Start Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). |  |
| `ShowingDate` | `showing_date` | Date |  | The date that showing appointments can be requested. |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. |  |
| `ShowingMaximumDuration` | `showing_maximum_duration` | String |  | The maximum block of time available for a showing. |  |
| `ShowingMethod` | `showing_method` | varchar (multi) | [`showing_method`](../lookups.md#showing_method) | The type of showings (i.e., in-person, virtual, etc.) allowed for the property. |  |
| `ShowingMinimumDuration` | `showing_minimum_duration` | String |  | The minimum block of time available for a showing. |  |
| `UniqueOrganizationIdentifier` | `unique_organization_identifier` | String |  | This is the unique ID assigned to organizations included in the OUID Resource. |  |
| `UniversalPropertyId` | `universal_property_id` | String |  | The Universal Property Identifier (UPI) is a unique identifier based on country and local identification methods for all real property in the U.S. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

