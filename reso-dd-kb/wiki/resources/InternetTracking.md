# InternetTracking

The InternetTracking resource records consumer-facing engagement events on syndicated listings — page views, searches, saves, shares, contact requests, clicks. Events identify the object, the actor (or anonymous flag), and the event timestamp for analytics + reporting.

## Groups

- **Actor** — 29 fields
- **Event** — 17 fields
- **Object** — 13 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ActorCity` | String | Actor |  |  |  | The city location of the actor as recorded by the source. | [link](https://ddwiki.reso.org/display/DDW20/ActorCity+Field) |
| `ActorEmail` | String | Actor |  |  |  | The email address of the actor in this event. | [link](https://ddwiki.reso.org/display/DDW20/ActorEmail+Field) |
| `ActorID` | String | Actor |  |  |  | The local, well-known identifier the actor, provided by the source when applicable. | [link](https://ddwiki.reso.org/display/DDW20/ActorID+Field) |
| `ActorIP` | String | Actor |  |  |  | The recorded IP address of the actor in this event. | [link](https://ddwiki.reso.org/display/DDW20/ActorIP+Field) |
| `ActorKey` | String | Actor |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/ActorKey+Field) |
| `ActorLatitude` | Number | Actor |  |  |  | The geographic latitude of some reference point for the location of the actor, specified in degrees and decimal parts. | [link](https://ddwiki.reso.org/display/DDW20/ActorLatitude+Field) |
| `ActorLongitude` | Number | Actor |  |  |  | The geographic longitude of some reference point for the location of the actor, specified in degrees and decimal parts. | [link](https://ddwiki.reso.org/display/DDW20/ActorLongitude+Field) |
| `ActorOriginatingSystem` | Resource | Actor |  |  |  | The originating system of the Actor record. | [link](https://ddwiki.reso.org/display/DDW20/ActorOriginatingSystem+Field) |
| `ActorOriginatingSystemID` | String | Actor |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/display/DDW20/ActorOriginatingSystemID+Field) |
| `ActorOriginatingSystemName` | String | Actor |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/display/DDW20/ActorOriginatingSystemName+Field) |
| `ActorPhone` | String | Actor |  |  |  | The phone number of the actor in this event. | [link](https://ddwiki.reso.org/display/DDW20/ActorPhone+Field) |
| `ActorPhoneExt` | String | Actor |  |  |  | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/ActorPhoneExt+Field) |
| `ActorPostalCode` | String | Actor |  |  |  | The postal code of the actor. | [link](https://ddwiki.reso.org/display/DDW20/ActorPostalCode+Field) |
| `ActorPostalCodePlus4` | String | Actor |  |  |  | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/ActorPostalCodePlus4+Field) |
| `ActorRegion` | String | Actor |  |  |  | A geographical region defined by the source. | [link](https://ddwiki.reso.org/display/DDW20/ActorRegion+Field) |
| `ActorSourceSystem` | Resource | Actor |  |  |  | The source system of the Actor record. | [link](https://ddwiki.reso.org/display/DDW20/ActorSourceSystem+Field) |
| `ActorSourceSystemID` | String | Actor |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/display/DDW20/ActorSourceSystemID+Field) |
| `ActorSourceSystemName` | String | Actor |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/display/DDW20/ActorSourceSystemName+Field) |
| `ActorStateOrProvince` | String List, Single | Actor | [StateOrProvince](#stateorprovince) |  |  | The state or province location of the actor as recorded by the source. | [link](https://ddwiki.reso.org/display/DDW20/ActorStateOrProvince+Field) |
| `ActorType` | String List, Single | Actor | [ActorType](#actortype) |  |  | A list of actor types; where the event originated from (e.g., Agent, Bot, Consumer). | [link](https://ddwiki.reso.org/display/DDW20/ActorType+Field) |
| `ColorDepth` | Number | Actor |  |  |  | The color depth of the actor's device display. | [link](https://ddwiki.reso.org/display/DDW20/ColorDepth+Field) |
| `DeviceType` | String List, Single | Actor | [DeviceType](#devicetype) |  |  | The device type used by the actor (e.g., Mobile, Desktop) in this event. | [link](https://ddwiki.reso.org/display/DDW20/DeviceType+Field) |
| `EventDescription` | String | Event |  |  |  | A description of the event being tracked (e.g., "The listing was viewed."). | [link](https://ddwiki.reso.org/display/DDW20/EventDescription+Field) |
| `EventKey` | String | Event |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/EventKey+Field) |
| `EventLabel` | String | Event |  |  |  | A short description of the event being tracked. | [link](https://ddwiki.reso.org/display/DDW20/EventLabel+Field) |
| `EventOriginatingSystem` | Resource | Event |  |  |  | The originating system of the InternetTracking event. | [link](https://ddwiki.reso.org/display/DDW20/EventOriginatingSystem+Field) |
| `EventOriginatingSystemID` | String | Event |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/display/DDW20/EventOriginatingSystemID+Field) |
| `EventOriginatingSystemName` | String | Event |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/display/DDW20/EventOriginatingSystemName+Field) |
| `EventReportedTimestamp` | Timestamp | Event |  |  |  | Date/time of when the event was recorded. | [link](https://ddwiki.reso.org/display/DDW20/EventReportedTimestamp+Field) |
| `EventSource` | String List, Single | Event | [EventSource](#eventsource) |  |  | Conveys the source of the EventType. | [link](https://ddwiki.reso.org/display/DDW20/EventSource+Field) |
| `EventSourceSystem` | Resource | Event |  |  |  | The source system of the InternetTracking event. | [link](https://ddwiki.reso.org/display/DDW20/EventSourceSystem+Field) |
| `EventSourceSystemID` | String | Event |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/display/DDW20/EventSourceSystemID+Field) |
| `EventSourceSystemName` | String | Event |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/display/DDW20/EventSourceSystemName+Field) |
| `EventTarget` | String List, Single | Event | [EventTarget](#eventtarget) |  |  | A defined target of the event type. | [link](https://ddwiki.reso.org/display/DDW20/EventTarget+Field) |
| `EventTimestamp` | Timestamp | Event |  |  |  | The date and time the tracked event occurred (ISO 8601). | [link](https://ddwiki.reso.org/display/DDW20/EventTimestamp+Field) |
| `EventType` | String List, Single | Event | [EventType](#eventtype) |  |  | The type of event being tracked. | [link](https://ddwiki.reso.org/display/DDW20/EventType+Field) |
| `ObjectID` | String | Object |  |  |  | An ID pertaining to the ObjectType (i.e., the MLS listing ID for ObjectType.Listing). | [link](https://ddwiki.reso.org/display/DDW20/ObjectID+Field) |
| `ObjectIdType` | String List, Single | Object | [ObjectIdType](#objectidtype) |  |  | A label that better defines the data in the ObjectID field (i.e., ObjectID is an MLS listing ID or ObjectID is a unique ID from the source). | [link](https://ddwiki.reso.org/display/DDW20/ObjectIdType+Field) |
| `ObjectKey` | String | Object |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/ObjectKey+Field) |
| `ObjectOriginatingSystem` | Resource | Object |  |  |  | The originating system of the InternetTracking object. | [link](https://ddwiki.reso.org/display/DDW20/ObjectOriginatingSystem+Field) |
| `ObjectOriginatingSystemID` | String | Object |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/display/DDW20/ObjectOriginatingSystemID+Field) |
| `ObjectOriginatingSystemName` | String | Object |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/display/DDW20/ObjectOriginatingSystemName+Field) |
| `ObjectSourceSystem` | Resource | Object |  |  |  | The source system of the InternetTracking object. | [link](https://ddwiki.reso.org/display/DDW20/ObjectSourceSystem+Field) |
| `ObjectSourceSystemID` | String | Object |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/display/DDW20/ObjectSourceSystemID+Field) |
| `ObjectSourceSystemName` | String | Object |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/display/DDW20/ObjectSourceSystemName+Field) |
| `ObjectType` | String List, Single | Object | [ObjectType](#objecttype) |  |  | The type of object the tracked event applies to (Property, Member, Office, OpenHouse, etc.). | [link](https://ddwiki.reso.org/display/DDW20/ObjectType+Field) |
| `ObjectURL` | String | Object |  |  |  | The Uniform Resource Locator (URL) of the tracked event. | [link](https://ddwiki.reso.org/display/DDW20/ObjectURL+Field) |
| `OriginatingSystemActorKey` | String | Actor |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemActorKey+Field) |
| `OriginatingSystemEventKey` | String | Event |  |  |  | The system key, a unique record identifier, from the originating system, which is the system with authoritative control over the record (e.g., the MLS where the member was input). | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemEventKey+Field) |
| `OriginatingSystemObjectKey` | String | Object |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemObjectKey+Field) |
| `ReferringURL` | String | Event |  |  |  | The referring Uniform Resource Locator (URL) of the tracked event. | [link](https://ddwiki.reso.org/display/DDW20/ReferringURL+Field) |
| `ScreenHeight` | Number | Actor |  |  |  | The screen height, in pixels, of the actor's device. | [link](https://ddwiki.reso.org/display/DDW20/ScreenHeight+Field) |
| `ScreenWidth` | Number | Actor |  |  |  | The screen width, in pixels, of the actor's device. | [link](https://ddwiki.reso.org/display/DDW20/ScreenWidth+Field) |
| `SessionID` | String | Actor |  |  |  | A unique session ID number, created by the source, that can be used to query data for a single session. | [link](https://ddwiki.reso.org/display/DDW20/SessionID+Field) |
| `SourceSystemActorKey` | String | Actor |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemActorKey+Field) |
| `SourceSystemEventKey` | String | Event |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemEventKey+Field) |
| `SourceSystemObjectKey` | String | Object |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemObjectKey+Field) |
| `TimeZoneOffset` | Number | Actor |  |  |  | The time zone offset is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. | [link](https://ddwiki.reso.org/display/DDW20/TimeZoneOffset+Field) |
| `UserAgent` | String | Actor |  |  |  | The software agent acting on behalf of the user (actor) in this event. | [link](https://ddwiki.reso.org/display/DDW20/UserAgent+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ActorCity</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorEmail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Email Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorIP</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** IP Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorLongitude</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Longitud Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** SEP 01 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorOriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorOriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorPhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorPhoneExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext Telefónica Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorPostalCode</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorPostalCodePlus4</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más4 Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorRegion</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Región Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorSourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ActorStateOrProvince</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado o Provincia Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ActorType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Tercero
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ColorDepth</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>DeviceType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Dispositivo
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** AUG 22 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventLabel</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Etiqueta de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventOriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>EventOriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Evento Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventOriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Evento Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventReportedTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 21 2021
  - **Revision Date:** APR 21 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>EventSource</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 30 2019
  - **Revision Date:** APR 30 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>EventSourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Evento Sistema Fuente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventSourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Evento Sistema Fuente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventTarget</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Objetivo de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** AUG 22 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>EventType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Evento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** SEP 01 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectIdType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de ID de Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectOriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ObjectOriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Sistema de Origen del Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectOriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen del Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectSourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ObjectSourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Objeto Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectSourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Objeto Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ObjectURL</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** URL de Objeto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>OriginatingSystemActorKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Tercero Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>OriginatingSystemEventKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Evento Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>OriginatingSystemObjectKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Evento Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ScreenHeight</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ScreenWidth</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemEventKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Evento Sistema Fuente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>SourceSystemObjectKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Objeto Sistema Fuente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>TimeZoneOffset</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>UserAgent</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Agente Usuario
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAR 30 2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### ActorType

| Value | Definition |
|---|---|
| `Agent` | The event was generated by what the source defines as a real estate professional. |
| `Bot` | The event was generated by a bot or some type of scripting tool |
| `Client` | The event was generated by what the source defines as a registered client |
| `Consumer` | The event was generated by what the source defines as a consumer |
| `Unknown` | The generating Actor type could not be identified |

### DeviceType

| Value | Definition |
|---|---|
| `Desktop` | The actor's device has been identified as a desktop device by the source. |
| `Mobile` | The actor's device has been identified as a mobile device by the source. |
| `Tablet` | The actor's device has been identified as a tablet device by the source. |
| `Unknown` | The actor's device could not be identified by the source. |
| `Wearable` | The actor's device has been identified as a wearable device by the source. |

### EventSource

| Value | Definition |
|---|---|
| `AI` | The source of the object is the result of what the client systems deem as Artificial Intelligence (AI). |
| `GPS` | The source of the object is the result of Global Positioning System (GPS) activity. |
| `List` | The source of the object being viewed pertaining to application structure (e.g., the listing impression was displayed in a scrollable list/table with others). |
| `Map` | The source of the object being viewed pertaining to application structure (e.g., the listing impression was displayed on a map). |
| `Search Engine` | The source of the object is the result of a search engine assistant (e.g., Google, Bing, Safari). |
| `Voice Assistant` | The source of the object being viewed pertaining to application structure (e.g., the listing impression was conveyed via a voice assistant like Amazon Echo). |

### EventTarget

| Value | Definition |
|---|---|
| `Agent` | The EventType used a destination pertaining to the listing agent (e.g., the actor's Submission of Lead Form went to the listing agent's contact information). |
| `Broker` | The EventType used a destination pertaining to the listing broker (e.g., the Clicked on Phone Number EventType uses the broker's contact information). |
| `Digg` | The object was shared on Digg. |
| `Email` | The object was sent in an email. |
| `Facebook` | The object was shared on Facebook. |
| `Facebook Messenger` | The object was shared via Facebook Messenger. |
| `iMessage` | The object was shared via iMessage. |
| `Instagram` | The object was shared on Instagram. |
| `LinkedIn` | The object was shared on LinkedIn. |
| `Microsoft Teams` | The object was shared via the Teams application/service. |
| `Pinterest` | The object was pinned on Pinterest. |
| `Reddit` | The object was shared on Reddit. |
| `Slack` | The object was shared via Slack. |
| `SMS` | The object was sent in an SMS message. |
| `Snapchat` | The object was shared on Snapchat. |
| `StumbleUpon` | The object was shared on StumbleUpon. |
| `TikTok` | The object was shared on TikTok. |
| `Tumblr` | The object was shared on Tumblr. |
| `Twitter` | The object was posted on X (formerly Twitter). |
| `WhatsApp` | The object was shared via the WhatsApp application. |
| `YouTube` | The object was shared on YouTube. |

### EventType

| Value | Definition |
|---|---|
| `Click to Primary Hosted Site` | The actor was referred to the object's primary hosted website. |
| `Clicked on Email Address` | The actor engaged in the act of emailing to the object's email address (note: does not indicate an email was sent). |
| `Clicked on Phone Number` | The actor clicked on a phone number link associated with the object. |
| `Comments` | Comments were made on the object. |
| `Detailed View` | The object was the main focal point in the actor's view. |
| `Discard` | The actor has reacted "negatively" to the object. |
| `Driving Directions` | The actor engaged in driving directions with the object |
| `Exit Detailed View` | The actor left the detailed view. |
| `Favorited` | The actor has reacted "positively" to the object. |
| `Impression` | The object appeared as a form of impression. |
| `Maybe` | The actor has reacted "possibly positive" to the object. |
| `Object Modified` | The tracking object was modified in some way. |
| `Photo Gallery` | The actor participated in a photo gallery display. |
| `Printed` | The actor printed the object. |
| `Property Videos` | The actor has interacted with a property video with the object. |
| `Scrolled Depth` | The user has scrolled on the pageview. |
| `Search` | The tracking object data is part of a search and will contain more than one result. |
| `Share` | The sharing of a listing to another media or entity, including social media, IM (instant message), email and SMS (Short Message Service) messages. |
| `Submission of Lead Form` | The actor has submitted a lead form. |
| `Virtual Tour` | The actor viewed the object's virtual tour. |

### ObjectIdType

| Value | Definition |
|---|---|
| `ListingId` | The ObjectID is the MLS listing number. |
| `ListingKey` | The object is a key field from an MLS system. |
| `OpenHouseId` | The ObjectID is an open house ID. |
| `OpenHouseKey` | The ObjectID is the key of an open house record. |
| `ParcelNumber` | When no listing exists or the tracking is property-centric, the ObjectIdType of the property's parcel number is used. |
| `SavedSearchKey` | When the event is the execution of a saved search, the ObjectID will be the SavedSearchKey from the system that executed the search. |
| `Unique` | The ObjectID is a unique ID supplied by the source and is not one of the other types. |
| `UPI` | When no listing exists and the tracking is property-centric, the RESO Universal Property Identifier (UPI) is used. |

### ObjectType

| Value | Definition |
|---|---|
| `Document` | The object of the tracking event is a document. |
| `Listing` | The object of the tracking event is a real estate listing. |
| `Open House` | The object of the tracking event is an open house event. |
| `Photo` | The object of the tracking event is a photo. |
| `Property` | When no listing exists or the tracking is property-centric, the ObjectType of Property is used. |
| `Saved Search` | When the event is the execution of a saved search, the ObjectType will be a Saved Search from the system that executed the search. |
| `Virtual Tour` | The object of the tracking event is considered a virtual tour. |

### StateOrProvince

| Value | Definition |
|---|---|
| `AB` | The Canadian province in which the listing is located is Alberta. |
| `AK` | The U.S. |
| `AL` | The U.S. |
| `AR` | The U.S. |
| `AZ` | The U.S. |
| `BC` | The Canadian province in which the listing is located is British Columbia. |
| `CA` | The U.S. |
| `CO` | The U.S. |
| `CT` | The U.S. |
| `DC` | The U.S. |
| `DE` | The U.S. |
| `FL` | The U.S. |
| `GA` | The U.S. |
| `HI` | The U.S. |
| `IA` | The U.S. |
| `ID` | The U.S. |
| `IL` | The U.S. |
| `IN` | The U.S. |
| `KS` | The U.S. |
| `KY` | The U.S. |
| `LA` | The U.S. |
| `MA` | The U.S. |
| `MB` | The Canadian province in which the listing is located is Manitoba. |
| `MD` | The U.S. |
| `ME` | The U.S. |
| `MI` | The U.S. |
| `MN` | The U.S. |
| `MO` | The U.S. |
| `MS` | The U.S. |
| `MT` | The U.S. |
| `NB` | The Canadian province in which the listing is located is New Brunswick. |
| `NC` | The U.S. |
| `ND` | The U.S. |
| `NE` | The U.S. |
| `NF` | The Canadian province in which the listing is located is Newfoundland and Labrador. |
| `NH` | The U.S. |
| `NJ` | The U.S. |
| `NM` | The U.S. |
| `NS` | The Canadian province in which the listing is located is Nova Scotia. |
| `NT` | The Canadian territory in which the listing is located is Northwest Territories. |
| `NU` | The Canadian territory in which the listing is located is Nunavut. |
| `NV` | The U.S. |
| `NY` | The U.S. |
| `OH` | The U.S. |
| `OK` | The U.S. |
| `ON` | The Canadian province in which the listing is located is Ontario. |
| `OR` | The U.S. |
| `PA` | The U.S. |
| `PE` | The Canadian province in which the listing is located is Prince Edward Island. |
| `QC` | The Canadian province in which the listing is located is Quebec. |
| `RI` | The U.S. |
| `SC` | The U.S. |
| `SD` | The U.S. |
| `SK` | The Canadian province in which the listing is located is Saskatchewan. |
| `TN` | The U.S. |
| `TX` | The U.S. |
| `UT` | The U.S. |
| `VA` | The U.S. |
| `VI` | The U.S. |
| `VT` | The U.S. |
| `WA` | The U.S. |
| `WI` | The U.S. |
| `WV` | The U.S. |
| `WY` | The U.S. |
| `YT` | The Canadian territory in which the listing is located is Yukon. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
