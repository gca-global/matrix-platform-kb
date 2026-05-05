# `internet_tracking` (InternetTracking)

> A standard data set for recording and transfer of event-related information of real estate products.

- Source: [https://dd.reso.org/DD2.0/InternetTracking/](https://dd.reso.org/DD2.0/InternetTracking/)
- Field count on dd.reso.org: **59**
- Primary key: `event_key`
- Note: PK chosen by override (RESO uses `EventKey` for this resource).
- Last revised upstream: 9/1/2017

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ActorCity` | `actor_city` | String |  | The city location of the actor as recorded by the source. |  |
| `ActorEmail` | `actor_email` | String |  | The email address of the actor in this event. |  |
| `ActorID` | `actor_id` | String |  | The local, well-known identifier the actor, provided by the source when applicable. |  |
| `ActorIP` | `actor_ip` | String |  | The recorded IP address of the actor in this event. |  |
| `ActorKey` | `actor_key` | String |  | A unique identifier for this record from the immediate source. |  |
| `ActorLatitude` | `actor_latitude` | Number |  | The geographic latitude of some reference point for the location of the actor, specified in degrees and decimal parts. |  |
| `ActorLongitude` | `actor_longitude` | Number |  | The geographic longitude of some reference point for the location of the actor, specified in degrees and decimal parts. |  |
| `ActorOriginatingSystem` | `actor_originating_system` | Resource |  | The originating system of the Actor record. | `[Resource]` |
| `ActorOriginatingSystemID` | `actor_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `ActorOriginatingSystemName` | `actor_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `ActorPhone` | `actor_phone` | String |  | The phone number of the actor in this event. |  |
| `ActorPhoneExt` | `actor_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `ActorPostalCode` | `actor_postal_code` | String |  | The postal code of the actor. |  |
| `ActorPostalCodePlus4` | `actor_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `ActorRegion` | `actor_region` | String |  | A geographical region defined by the source. |  |
| `ActorSourceSystem` | `actor_source_system` | Resource |  | The source system of the Actor record. | `[Resource]` |
| `ActorSourceSystemID` | `actor_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `ActorSourceSystemName` | `actor_source_system_name` | String |  | The name of the immediate record provider. |  |
| `ActorStateOrProvince` | `actor_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province location of the actor as recorded by the source. |  |
| `ActorType` | `actor_type` | enum | [`actor_type`](../lookups.md#actor_type) | A list of actor types; where the event originated from (e.g., Agent, Bot, Consumer). |  |
| `ColorDepth` | `color_depth` | Number |  | The color depth of the actor's device display. |  |
| `DeviceType` | `device_type` | enum | [`device_type`](../lookups.md#device_type) | The device type used by the actor (e.g., Mobile, Desktop) in this event. |  |
| `EventDescription` | `event_description` | String |  | A description of the event being tracked (e.g., "The listing was viewed."). |  |
| `EventKey` | `event_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `EventLabel` | `event_label` | String |  | A short description of the event being tracked. |  |
| `EventOriginatingSystem` | `event_originating_system` | Resource |  | The originating system of the InternetTracking event. | `[Resource]` |
| `EventOriginatingSystemID` | `event_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `EventOriginatingSystemName` | `event_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `EventReportedTimestamp` | `event_reported_timestamp` | Timestamp |  | Date/time of when the event was recorded. |  |
| `EventSource` | `event_source` | enum | [`event_source`](../lookups.md#event_source) | Conveys the source of the EventType. |  |
| `EventSourceSystem` | `event_source_system` | Resource |  | The source system of the InternetTracking event. | `[Resource]` |
| `EventSourceSystemID` | `event_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `EventSourceSystemName` | `event_source_system_name` | String |  | The name of the immediate record provider. |  |
| `EventTarget` | `event_target` | enum | [`event_target`](../lookups.md#event_target) | A defined target of the event type. |  |
| `EventTimestamp` | `event_timestamp` | Timestamp |  | A Coordinated Universal Time (UTC) timestamp of when the event being tracked occurred. |  |
| `EventType` | `event_type` | enum | [`event_type`](../lookups.md#event_type) | The type of event being tracked. |  |
| `ObjectID` | `object_id` | String |  | An ID pertaining to the ObjectType (i.e., the MLS listing ID for ObjectType.Listing). |  |
| `ObjectIdType` | `object_id_type` | enum | [`object_id_type`](../lookups.md#object_id_type) | A label that better defines the data in the ObjectID field (i.e., ObjectID is an MLS listing ID or ObjectID is a unique ID from the source). |  |
| `ObjectKey` | `object_key` | String |  | A unique identifier for this record from the immediate source. |  |
| `ObjectOriginatingSystem` | `object_originating_system` | Resource |  | The originating system of the InternetTracking object. | `[Resource]` |
| `ObjectOriginatingSystemID` | `object_originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `ObjectOriginatingSystemName` | `object_originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `ObjectSourceSystem` | `object_source_system` | Resource |  | The source system of the InternetTracking object. | `[Resource]` |
| `ObjectSourceSystemID` | `object_source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `ObjectSourceSystemName` | `object_source_system_name` | String |  | The name of the immediate record provider. |  |
| `ObjectType` | `object_type` | enum | [`object_type`](../lookups.md#object_type) | The type of object being tracked in this event. |  |
| `ObjectURL` | `object_url` | String |  | The Uniform Resource Locator (URL) of the tracked event. |  |
| `OriginatingSystemActorKey` | `originating_system_actor_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemEventKey` | `originating_system_event_key` | String |  | The system key, a unique record identifier, from the originating system, which is the system with authoritative control over the record (e.g., the MLS where the member was input). |  |
| `OriginatingSystemObjectKey` | `originating_system_object_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `ReferringURL` | `referring_url` | String |  | The referring Uniform Resource Locator (URL) of the tracked event. |  |
| `ScreenHeight` | `screen_height` | Number |  | The screen height, in pixels, of the actor's device. |  |
| `ScreenWidth` | `screen_width` | Number |  | The screen width, in pixels, of the actor's device. |  |
| `SessionID` | `session_id` | String |  | A unique session ID number, created by the source, that can be used to query data for a single session. |  |
| `SourceSystemActorKey` | `source_system_actor_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemEventKey` | `source_system_event_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemObjectKey` | `source_system_object_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `TimeZoneOffset` | `time_zone_offset` | Number |  | The time zone offset is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. |  |
| `UserAgent` | `user_agent` | String |  | The software agent acting on behalf of the user (actor) in this event. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

