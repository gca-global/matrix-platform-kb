# OpenHouse

The OpenHouse resource describes a scheduled event during which a Property is open for public or broker viewing. Each open house has a date, start/end time, status, and an optional remark; multiple open houses can be scheduled per Property.

**Adoption** — weighted Org%: **43%** across 26 measured fields (median 46%, avg 43%).

## Groups

- **Other** — 33 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `AppointmentRequiredYN` | Boolean |  |  | 10% | 1% | Indicates whether or not the open house requires an appointment. | [link](https://ddwiki.reso.org/display/DDW20/AppointmentRequiredYN+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135426) |
| `Listing` | Resource |  |  |  |  | The listing associated with the open house. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135433) |
| `ListingId` | String |  |  | 60% | 47% | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135438) |
| `ListingKey` | String |  |  | 60% | 71% | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135445) |
| `LivestreamOpenHouseURL` | String |  |  | 15% | 1% | A link to an open house livestream event. | [link](https://ddwiki.reso.org/display/DDW20/LivestreamOpenHouseURL+Field) |
| `Media` | Collection |  |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135457) |
| `ModificationTimestamp` | Timestamp |  |  | 75% | 57% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135462) |
| `OpenHouseAttendedBy` | String List, Single |  | [Attended](#attended) | 15% | 1% | States whether or not the open house will be attended by a licensed agent (i.e., Agent, Seller, Unattended). | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseAttendedBy+Field) |
| `OpenHouseDate` | Date |  |  | 70% | 65% | The date of the open house event. | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseDate+Field) |
| `OpenHouseEndTime` | Timestamp |  |  | 80% | 74% | The end date and time of the open house event (ISO 8601). | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseEndTime+Field) |
| `OpenHouseId` | String |  |  |  | 47% | The well-known identifier for the OpenHouse Resource. | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseId+Field) |
| `OpenHouseKey` | String |  |  |  | 90% | A system-unique identifier for the open house event. | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseKey+Field) |
| `OpenHouseRemarks` | String |  |  | 70% | 68% | Free-form remarks describing the open house event (refreshments, parking instructions, etc.). | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseRemarks+Field) |
| `OpenHouseStartTime` | Timestamp |  |  | 75% | 74% | The start date and time of the open house event (ISO 8601). | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseStartTime+Field) |
| `OpenHouseStatus` | String List, Single |  | [OpenHouseStatus](#openhousestatus) | 45% | 37% | The status of the open house event. | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseStatus+Field) |
| `OpenHouseType` | String List, Single |  | [OpenHouseType](#openhousetype) | 65% | 36% | The type of the open house event. | [link](https://ddwiki.reso.org/display/DDW20/OpenHouseType+Field) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 45% | 12% | The transactional timestamp automatically recorded by the MLS system representing the date/time the open house was entered and made visible to members of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135522) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the OpenHouse record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135529) |
| `OriginatingSystemID` | String |  |  | 45% | 30% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135534) |
| `OriginatingSystemKey` | String |  |  | 60% | 36% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135540) |
| `OriginatingSystemName` | String |  |  | 60% | 45% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135547) |
| `Refreshments` | String |  |  | 25% | 11% | A description of the refreshments that will be served at the open house. | [link](https://ddwiki.reso.org/display/DDW20/Refreshments+Field) |
| `ShowingAgent` | Resource |  |  |  |  | The member record of the showing agent. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116814) |
| `ShowingAgentFirstName` | String |  |  | 35% | 5% | The first name of the showing agent. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116820) |
| `ShowingAgentKey` | String |  |  | 25% | 1% | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentKey+Field) |
| `ShowingAgentLastName` | String |  |  | 35% | 4% | The last name of the showing agent. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116829) |
| `ShowingAgentMlsID` | String |  |  | 40% | 21% | The local, well-known identifier for the member. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116835) |
| `SocialMedia` | Collection |  |  |  |  | The social media related to the OpenHouse record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135589) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the OpenHouse record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135595) |
| `SourceSystemID` | String |  |  | 25% | 15% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135601) |
| `SourceSystemKey` | String |  |  |  | 47% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135607) |
| `SourceSystemName` | String |  |  | 20% | 1% | The name of the open house record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135614) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>AppointmentRequiredYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Se Requiere Cita SN
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 08 2013

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **BEDES:** Identifier Label = "Listing" Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>ListingKey</code></summary>

  - **BEDES:** Identifier Label = "Listing"Subaddress Type = "Key"Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>LivestreamOpenHouseURL</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 18 2020
  - **Revision Date:** JUN 18 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Media</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseAttendedBy</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Jornada de Puertas Abiertas Asistida por
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** NOV 19 2015

</details>

<details><summary><code>OpenHouseDate</code></summary>

  - **BEDES:** Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Fecha de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseEndTime</code></summary>

  - **BEDES:** Interval End Time = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Hora de Finalización de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseRemarks</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Observaciones de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseStartTime</code></summary>

  - **BEDES:** Interval Start Time = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Hora de Inicio de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OpenHouseType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Jornada de Puertas Abiertas
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **BEDES:** Date Status = "Created"Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>Refreshments</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Refrescos
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>ShowingAgent</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ShowingAgentFirstName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Mostrar Nombre de Agente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ShowingAgentKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Mostrar Clave de Agente
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>ShowingAgentLastName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Mostrar Apellido de Agente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ShowingAgentMlsID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Mostrar ID de MLS de Agente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>SocialMedia</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

## Lookups

### Attended

| Value | Definition |
|---|---|
| `Agent` | A licensed real estate agent will be present at the open house event. |
| `Seller` | A licensed real estate agent will not be present and the property owner will be present at the open house event. |
| `Unattended` | The open house event will not be attended. |

### OpenHouseStatus

| Value | Definition |
|---|---|
| `Active` | The open house is active and continuing as scheduled. |
| `Canceled` | The open house has been canceled. |
| `Ended` | The open house has ended and is past the scheduled open house date and time. |

### OpenHouseType

| Value | Definition |
|---|---|
| `Broker` | The open house is only open to brokers and, at times, agents. |
| `Livestream Broker` | The open house is livestreamed and only open to brokers and, at times, agents. |
| `Livestream Public` | The open house is livestreamed and open to the general public. |
| `Office` | The open house is only open to the members of a particular office or offices. |
| `Public` | The open house is open to the general public. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
