# HistoryTransactional

The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. Each row records the resource, record id, field name, change type (Add/Modify/Delete), previous and new value, and the Member who made the change.

**Adoption** — weighted Org%: **6%** across 19 measured fields (median 10%, avg 6%).

## Groups

- **Other** — 23 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ChangeType` | String List, Single |  | [ChangeType](#changetype) | 10% | 1% | The type of change recorded. | [link](https://ddwiki.reso.org/display/DDW20/ChangeType+Field) |
| `ChangedByMember` | Resource |  |  |  |  | The member who changed the historical item. | [link](https://ddwiki.reso.org/display/DDW20/ChangedByMember+Field) |
| `ChangedByMemberID` | String |  |  | 5% | 1% | The local, well-know identifier of the member (user) who made the change. | [link](https://ddwiki.reso.org/display/DDW20/ChangedByMemberID+Field) |
| `ChangedByMemberKey` | String |  |  |  | 11% | The unique identifier of the member (user) who made the change. | [link](https://ddwiki.reso.org/display/DDW20/ChangedByMemberKey+Field) |
| `ClassName` | String |  | [ClassName](#classname) |  |  | The name of the class in which this history record applies. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135185) |
| `EntityEventSequence` | Number |  |  |  | 10% | A unique, system-wide ID that can be used to represent the sequence in which an EntityEvent occurred in a given system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116308) |
| `FieldKey` | String |  |  |  | 0% | The unique identifier of the field with data being changed. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116314) |
| `FieldName` | String |  |  | 10% | 1% | The name of the field that was changed in the resource record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116320) |
| `HistoryTransactionalKey` | String |  |  | 5% | 1% | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/HistoryTransactionalKey+Field) |
| `ModificationTimestamp` | Timestamp |  |  | 10% | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135214) |
| `NewValue` | String |  |  | 10% | 1% | The new value of the field after the change. | [link](https://ddwiki.reso.org/display/DDW20/NewValue+Field) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the HistoryTransactional record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135226) |
| `OriginatingSystemHistoryKey` | String |  |  | 5% | 1% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemHistoryKey+Field) |
| `OriginatingSystemID` | String |  |  |  | 1% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135238) |
| `OriginatingSystemName` | String |  |  |  | 1% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135244) |
| `PreviousValue` | String |  |  | 10% | 1% | The previous value of the field before the change. | [link](https://ddwiki.reso.org/display/DDW20/PreviousValue+Field) |
| `ResourceName` | String |  |  | 10% | 1% | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135256) |
| `ResourceRecordID` | String |  |  | 5% | 1% | The well-known identifier of the related record from the source resource. | [link](https://ddwiki.reso.org/display/DDW20/ResourceRecordID+Field) |
| `ResourceRecordKey` | String |  |  | 5% | 1% | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135268) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the HistoryTransactional record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135274) |
| `SourceSystemHistoryKey` | String |  |  |  | 0% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemHistoryKey+Field) |
| `SourceSystemID` | String |  |  | 5% | 1% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135287) |
| `SourceSystemName` | String |  |  | 5% | 1% | The name of the historical record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135292) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ChangeType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Cambio
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ChangedByMember</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2020
  - **Revision Date:** JAN 06 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ChangedByMemberID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Cambiado por ID de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ClassName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** JUN 02 2018

</details>

<details><summary><code>EntityEventSequence</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 20 2019
  - **Revision Date:** JUN 20 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FieldKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Campo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** FEB 01 2015

</details>

<details><summary><code>FieldName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Campo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HistoryTransactionalKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Transaccional Histórica
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** OCT 18 2014

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015

</details>

<details><summary><code>NewValue</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nuevo Valor
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2020
  - **Revision Date:** JAN 06 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemHistoryKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Histórica de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>PreviousValue</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Valor Anterior
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>ResourceRecordID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Registro de Recurso
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ResourceRecordKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Registro de Recurso
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** FEB 01 2015

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2020
  - **Revision Date:** JAN 06 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemHistoryKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Historial Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
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

### ChangeType

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
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
