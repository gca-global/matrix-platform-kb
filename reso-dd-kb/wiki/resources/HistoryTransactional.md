# HistoryTransactional

A transactional history of the listing, showing before and after values of field changes.

**RESO DD 2.0** — 23 fields · last revised 9/24/2015 · [dd.reso.org](https://dd.reso.org/DD2.0/HistoryTransactional/)

**Adoption** — weighted Org%: **6%** across 19 measured fields (median 10%, avg 6%).

## Groups

- **Other** — 23 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ChangeType` | String List, Single |  | [ChangeType](#changetype) | 12% | The type of change recorded. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ChangeType/) |
| `ChangedByMember` | Resource |  |  |  | The member who changed the historical item. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ChangedByMember/) |
| `ChangedByMemberID` | String |  |  | 1% | The local, well-know identifier of the member (user) who made the change. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ChangedByMemberID/) |
| `ChangedByMemberKey` | String |  |  | 11% | The unique identifier of the member (user) who made the change. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ChangedByMemberKey/) |
| `ClassName` | String |  | [ClassName](#classname) |  | The name of the class in which this history record applies. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ClassName/) |
| `EntityEventSequence` | Number |  |  | 10% | A unique, system-wide ID that can be used to represent the sequence in which an EntityEvent occurred in a given system. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/EntityEventSequence/) |
| `FieldKey` | String |  |  | 0% | The unique identifier of the field with data being changed. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/FieldKey/) |
| `FieldName` | String |  |  | 12% | The name of the field that was changed in the resource record. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/FieldName/) |
| `HistoryTransactionalKey` | String |  |  | 12% | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/HistoryTransactionalKey/) |
| `ModificationTimestamp` | Timestamp |  |  | 12% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ModificationTimestamp/) |
| `NewValue` | String |  |  | 12% | The new value of the field after the change. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/NewValue/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the HistoryTransactional record. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/OriginatingSystem/) |
| `OriginatingSystemHistoryKey` | String |  |  | 1% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/OriginatingSystemHistoryKey/) |
| `OriginatingSystemID` | String |  |  | 1% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/OriginatingSystemID/) |
| `OriginatingSystemName` | String |  |  | 1% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/OriginatingSystemName/) |
| `PreviousValue` | String |  |  | 12% | The previous value of the field before the change. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/PreviousValue/) |
| `ResourceName` | String |  |  | 11% | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ResourceName/) |
| `ResourceRecordID` | String |  |  | 1% | The well-known identifier of the related record from the source resource. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ResourceRecordID/) |
| `ResourceRecordKey` | String |  |  | 12% | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). | [link](https://dd.reso.org/DD2.0/HistoryTransactional/ResourceRecordKey/) |
| `SourceSystem` | Resource |  |  |  | The source system of the HistoryTransactional record. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/SourceSystem/) |
| `SourceSystemHistoryKey` | String |  |  | 0% | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/SourceSystemHistoryKey/) |
| `SourceSystemID` | String |  |  | 0% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/SourceSystemID/) |
| `SourceSystemName` | String |  |  | 1% | The name of the historical record provider. | [link](https://dd.reso.org/DD2.0/HistoryTransactional/SourceSystemName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ChangeType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Cambio
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 12/12/2012

</details>

<details><summary><code>ChangedByMember</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2020
  - **Revision Date:** 1/6/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ChangedByMemberID</code></summary>

  - **Status:** Active
  - **Spanish Name:** Cambiado por ID de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>ChangedByMemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Cambiado por Clave de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/2/2018

</details>

<details><summary><code>EntityEventSequence</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/20/2019
  - **Revision Date:** 6/20/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FieldKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Campo
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 2/1/2015

</details>

<details><summary><code>FieldName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Campo
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 12/12/2012

</details>

<details><summary><code>HistoryTransactionalKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave Transaccional Histórica
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 10/18/2014

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 9/24/2015

</details>

<details><summary><code>NewValue</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nuevo Valor
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 12/12/2012

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2020
  - **Revision Date:** 1/6/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemHistoryKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave Histórica de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016

</details>

<details><summary><code>PreviousValue</code></summary>

  - **Status:** Active
  - **Spanish Name:** Valor Anterior
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 12/12/2012

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/12/2015

</details>

<details><summary><code>ResourceRecordID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Registro de Recurso
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 12/12/2012

</details>

<details><summary><code>ResourceRecordKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Registro de Recurso
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 2/1/2015

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2020
  - **Revision Date:** 1/6/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemHistoryKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Historial Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
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

### ChangeType

13 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ChangeType/)

| Value | Definition |
|---|---|
| `Active` | The change to the listing was a change of status to Active. |
| `Active Under Contract` | The change to the listing was a change of status to Active Under Contract. |
| `Back On Market` | The change to the listing was a change of status to Back On Market. |
| `Canceled` | The change to the listing was a change of status to Canceled. |
| `Closed` | The change to the listing was a change of status to Closed. |
| `Coming Soon` | The change to the listing was a change of status to Coming Soon. |
| `Deleted` | The change to the listing was a change of status to Deleted. |
| `Expired` | The change to the listing was a change of status to Expired. |
| `Hold` | The change to the listing was a change of status to Hold. |
| `New Listing` | The listing is new and hasn't had any status or price changes since its original input. |
| `Pending` | The change to the listing was a change of status to Pending. |
| `Price Change` | The change to the listing was a change to the ListPrice. |
| `Withdrawn` | The change to the listing was a change of status to Withdrawn. |

### ClassName

17 values · used by 8 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ClassName/)

| Value | Definition |
|---|---|
| `Business Opportunity` | The class, sometimes known as property type, is a business for sale. |
| `Commercial Lease` | The class, sometimes known as property type, is a commercial property for lease. |
| `Commercial Sale` | The class, sometimes known as property type, is a commercial property for sale. |
| `Contacts` | The class is the collection of the member's contacts/clients. |
| `Cross Property` | The class, sometimes known as property type, is a collection of all listing property types. |
| `Farm` | The class, sometimes known as property type, is a farm. |
| `History Transactional` | The class is the transactional history of another class. |
| `Land` | The class, sometimes known as property type, is land for sale or lease. |
| `Manufactured In Park` | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| `Media` | The class is one that contains records referencing media files. |
| `Member` | The class containing member records. |
| `Office` | The class containing office records. |
| `Open House` | The class containing open house records. |
| `Residential` | The class, sometimes known as property type, is residential property for sale. |
| `Residential Income` | The class, sometimes known as property type, is income or multifamily property for sale. |
| `Residential Lease` | The class, sometimes known as property type, is residential property for lease. |
| `Saved Search` | The class containing saved search data. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
