# `property_rooms` (PropertyRooms)

> Detailed information about separate rooms in a property.

- Source: [https://dd.reso.org/DD2.0/PropertyRooms/](https://dd.reso.org/DD2.0/PropertyRooms/)
- Field count on dd.reso.org: **19**
- Primary key: `room_key`
- Note: PK chosen by override (RESO uses `RoomKey` for this resource).
- Last revised upstream: 8/18/2023

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `BedroomClosetType` | `bedroom_closet_type` | enum | [`closet_type`](../lookups.md#closet_type) | A list of possible closet types for a bedroom. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the PropertyRooms record. | `[Collection]` |
| `Listing` | `listing` | Resource |  | The listing associated with the PropertyRooms record. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | This is the foreign ID relating to the Property Resource. | `-> property.listing_key` |
| `ListingKey` | `listing_key` | String |  | This is the foreign key relating to the Property resource. | `-> property.listing_key` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the PropertyRooms record was last modified. |  |
| `RoomArea` | `room_area` | Number |  | The area of the room being described. |  |
| `RoomAreaSource` | `room_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurement of the given room's area. |  |
| `RoomAreaUnits` | `room_area_units` | enum | [`area_units`](../lookups.md#area_units) | The unit of measurement used for the value in the RoomArea field (e.g., Square Feet, Square Meters). |  |
| `RoomDescription` | `room_description` | String |  | A textual description of the given room. |  |
| `RoomDimensions` | `room_dimensions` | String |  | A textual description of the dimensions of the given room. |  |
| `RoomFeatures` | `room_features` | varchar (multi) | [`interior_or_room_features`](../lookups.md#interior_or_room_features) | A list of features present in the given room. |  |
| `RoomKey` | `room_key` | String |  | A unique identifier for this record. | `pk` |
| `RoomLength` | `room_length` | Number |  | A numeric representation of the length of the given room. |  |
| `RoomLengthWidthSource` | `room_length_width_source` | enum | [`room_length_width_source`](../lookups.md#room_length_width_source) | The source of the measurement of the given units length and width. |  |
| `RoomLengthWidthUnits` | `room_length_width_units` | enum | [`linear_units`](../lookups.md#linear_units) | The unit of measurement used for the value of RoomLength and RoomWidth fields (e.g., Feet, Meters). |  |
| `RoomLevel` | `room_level` | enum | [`room_level`](../lookups.md#room_level) | The level within the dwelling on which the given room is located. |  |
| `RoomType` | `room_type` | enum | [`room_type`](../lookups.md#room_type) | The type of room being described by the other fields in the PropertyRooms resource. |  |
| `RoomWidth` | `room_width` | Number |  | A numeric representation of the width of a given room. |  |

## Foreign keys OUT (this resource references)

- `property_rooms.listing_id` -> `property.listing_key` (medium)
- `property_rooms.listing_key` -> `property.listing_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `property_rooms`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `listing_id` | `listing_key` -> `property.?` | `keep_both` | no_child_match |

