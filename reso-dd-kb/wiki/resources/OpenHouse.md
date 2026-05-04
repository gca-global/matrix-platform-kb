# OpenHouse

Fields commonly used to record an open house event.

**RESO DD 2.0** — 33 fields · last revised 8/8/2013 · [dd.reso.org](https://dd.reso.org/DD2.0/OpenHouse/)

**Adoption** — weighted Org%: **43%** across 26 measured fields (median 46%, avg 43%).

## Groups

- **Other** — 33 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `AppointmentRequiredYN` | Boolean |  |  | 1% | Indicates whether or not the open house requires an appointment. | [link](https://dd.reso.org/DD2.0/OpenHouse/AppointmentRequiredYN/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/OpenHouse/HistoryTransactional/) |
| `Listing` | Resource |  |  |  | The listing associated with the open house. | [link](https://dd.reso.org/DD2.0/OpenHouse/Listing/) |
| `ListingId` | String |  |  | 65% | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/OpenHouse/ListingId/) |
| `ListingKey` | String |  |  | 89% | A system-unique identifier for the listing. | [link](https://dd.reso.org/DD2.0/OpenHouse/ListingKey/) |
| `LivestreamOpenHouseURL` | String |  |  | 19% | A link to an open house livestream event. | [link](https://dd.reso.org/DD2.0/OpenHouse/LivestreamOpenHouseURL/) |
| `Media` | Collection |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://dd.reso.org/DD2.0/OpenHouse/Media/) |
| `ModificationTimestamp` | Timestamp |  |  | 76% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/OpenHouse/ModificationTimestamp/) |
| `OpenHouseAttendedBy` | String List, Single |  | [Attended](#attended) | 1% | States whether or not the open house will be attended by a licensed agent (i.e., Agent, Seller, Unattended). | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseAttendedBy/) |
| `OpenHouseDate` | Date |  |  | 79% | The date of the open house event. | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseDate/) |
| `OpenHouseEndTime` | Timestamp |  |  | 92% | The end date and time of the open house event (ISO 8601). | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseEndTime/) |
| `OpenHouseId` | String |  |  | 47% | The well-known identifier for the OpenHouse Resource. | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseId/) |
| `OpenHouseKey` | String |  |  | 90% | A system-unique identifier for the open house event. | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseKey/) |
| `OpenHouseRemarks` | String |  |  | 86% | Free-form remarks describing the open house event (refreshments, parking instructions, etc.). | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseRemarks/) |
| `OpenHouseStartTime` | Timestamp |  |  | 92% | The start date and time of the open house event (ISO 8601). | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseStartTime/) |
| `OpenHouseStatus` | String List, Single |  | [OpenHouseStatus](#openhousestatus) | 47% | The status of the open house event. | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseStatus/) |
| `OpenHouseType` | String List, Single |  | [OpenHouseType](#openhousetype) | 46% | The type of the open house event. | [link](https://dd.reso.org/DD2.0/OpenHouse/OpenHouseType/) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 18% | The transactional timestamp automatically recorded by the MLS system representing the date/time the open house was entered and made visible to members of the MLS. | [link](https://dd.reso.org/DD2.0/OpenHouse/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the OpenHouse record. | [link](https://dd.reso.org/DD2.0/OpenHouse/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  | 34% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/OpenHouse/OriginatingSystemID/) |
| `OriginatingSystemKey` | String |  |  | 46% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/OpenHouse/OriginatingSystemKey/) |
| `OriginatingSystemName` | String |  |  | 58% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/OpenHouse/OriginatingSystemName/) |
| `Refreshments` | String |  |  | 18% | A description of the refreshments that will be served at the open house. | [link](https://dd.reso.org/DD2.0/OpenHouse/Refreshments/) |
| `ShowingAgent` | Resource |  |  |  | The member record of the showing agent. | [link](https://dd.reso.org/DD2.0/OpenHouse/ShowingAgent/) |
| `ShowingAgentFirstName` | String |  |  | 10% | The first name of the showing agent. | [link](https://dd.reso.org/DD2.0/OpenHouse/ShowingAgentFirstName/) |
| `ShowingAgentKey` | String |  |  | 5% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/OpenHouse/ShowingAgentKey/) |
| `ShowingAgentLastName` | String |  |  | 9% | The last name of the showing agent. | [link](https://dd.reso.org/DD2.0/OpenHouse/ShowingAgentLastName/) |
| `ShowingAgentMlsID` | String |  |  | 24% | The local, well-known identifier for the member. | [link](https://dd.reso.org/DD2.0/OpenHouse/ShowingAgentMlsID/) |
| `SocialMedia` | Collection |  |  |  | The social media related to the OpenHouse record. | [link](https://dd.reso.org/DD2.0/OpenHouse/SocialMedia/) |
| `SourceSystem` | Resource |  |  |  | The source system of the OpenHouse record. | [link](https://dd.reso.org/DD2.0/OpenHouse/SourceSystem/) |
| `SourceSystemID` | String |  |  | 24% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/OpenHouse/SourceSystemID/) |
| `SourceSystemKey` | String |  |  | 47% | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/OpenHouse/SourceSystemKey/) |
| `SourceSystemName` | String |  |  | 5% | The name of the open house record provider. | [link](https://dd.reso.org/DD2.0/OpenHouse/SourceSystemName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>AppointmentRequiredYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Se Requiere Cita SN
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/8/2013

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **BEDES:** Identifier Label = "Listing" Identifier = [value]
  - **Status:** Active
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>ListingKey</code></summary>

  - **BEDES:** Identifier Label = "Listing"Subaddress Type = "Key"Identifier = [value]
  - **Status:** Active
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>LivestreamOpenHouseURL</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/18/2020
  - **Revision Date:** 6/18/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Media</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseAttendedBy</code></summary>

  - **Status:** Active
  - **Spanish Name:** Jornada de Puertas Abiertas Asistida por
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 11/19/2015

</details>

<details><summary><code>OpenHouseDate</code></summary>

  - **BEDES:** Date = [value]
  - **Status:** Active
  - **Spanish Name:** Fecha de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseEndTime</code></summary>

  - **BEDES:** Interval End Time = [value]
  - **Status:** Active
  - **Spanish Name:** Hora de Finalización de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Jornada de Puertas Abiertas
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/27/2019

</details>

<details><summary><code>OpenHouseKey</code></summary>

  - **BEDES:** Subaddress Type = "Key"Contact ID = [value]
  - **Status:** Active
  - **Spanish Name:** Clave de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseRemarks</code></summary>

  - **Status:** Active
  - **Spanish Name:** Observaciones de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseStartTime</code></summary>

  - **BEDES:** Interval Start Time = [value]
  - **Status:** Active
  - **Spanish Name:** Hora de Inicio de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseStatus</code></summary>

  - **Status:** Active
  - **Spanish Name:** Estado de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OpenHouseType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Jornada de Puertas Abiertas
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **BEDES:** Date Status = "Created"Date = [value]
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016

</details>

<details><summary><code>Refreshments</code></summary>

  - **Status:** Active
  - **Spanish Name:** Refrescos
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>ShowingAgent</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ShowingAgentFirstName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Mostrar Nombre de Agente
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>ShowingAgentKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Mostrar Clave de Agente
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018

</details>

<details><summary><code>ShowingAgentLastName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Mostrar Apellido de Agente
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>ShowingAgentMlsID</code></summary>

  - **Status:** Active
  - **Spanish Name:** Mostrar ID de MLS de Agente
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>SocialMedia</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave Sistema Fuente
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 12/5/2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

## Lookups

### Attended

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Attended/)

| Value | Definition |
|---|---|
| `Agent` | A licensed real estate agent will be present at the open house event. |
| `Seller` | A licensed real estate agent will not be present and the property owner will be present at the open house event. |
| `Unattended` | The open house event will not be attended. |

### OpenHouseStatus

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OpenHouseStatus/)

| Value | Definition |
|---|---|
| `Active` | The open house is active and continuing as scheduled. |
| `Canceled` | The open house has been canceled. |
| `Ended` | The open house has ended and is past the scheduled open house date and time. |

### OpenHouseType

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OpenHouseType/)

| Value | Definition |
|---|---|
| `Broker` | The open house is only open to brokers and, at times, agents. |
| `Livestream Broker` | The open house is livestreamed and only open to brokers and, at times, agents. |
| `Livestream Public` | The open house is livestreamed and open to the general public. |
| `Office` | The open house is only open to the members of a particular office or offices. |
| `Public` | The open house is open to the general public. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
