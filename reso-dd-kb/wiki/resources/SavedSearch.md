# SavedSearch

_RESO Data Dictionary 2.0 resource — 27 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/SavedSearch+Resource) for the canonical page._

**Adoption** — weighted Org%: **0%** across 2 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 27 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) |  |  | The class or table to which the SearchQuery criteria refers (e.g., Residential, Residential Lease, Residential Income, Commercial Sale). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135401) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135407) |
| `Member` | Resource |  |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2117015) |
| `MemberKey` | String |  |  |  |  | A system-unique identifier for the member. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135419) |
| `MemberMlsId` | String |  |  |  |  | The local, well-known identifier for the member as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135425) |
| `ModificationTimestamp` | Timestamp |  |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135431) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was entered. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135437) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the SavedSearch record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135443) |
| `OriginatingSystemID` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135449) |
| `OriginatingSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135455) |
| `OriginatingSystemMemberKey` | String |  |  |  |  | Unique identifier from the originating system, which is commonly a key to that system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135461) |
| `OriginatingSystemMemberName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemMemberName+Field) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135472) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135477) |
| `SavedSearchDescription` | String |  |  |  |  | A textual description of the saved search input by the member who created the saved search. | [link](https://ddwiki.reso.org/display/DDW20/SavedSearchDescription+Field) |
| `SavedSearchKey` | String |  |  |  | 0% | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2117089) |
| `SavedSearchName` | String |  |  |  |  | The name given to the search by the member inputting the saved search. | [link](https://ddwiki.reso.org/display/DDW20/SavedSearchName+Field) |
| `SavedSearchType` | String List, Single |  | SavedSearchType |  |  | Determines if the saved search used to pass criteria is to be stored and executed by the client or if it is a key to be passed to the host for execution (i.e., Client Receives Criteria, Host Returns Listings). | [link](https://ddwiki.reso.org/display/DDW20/SavedSearchType+Field) |
| `SearchQuery` | String |  |  |  |  | The textual representation of the search performed by the member that was saved. | [link](https://ddwiki.reso.org/display/DDW20/SearchQuery+Field) |
| `SearchQueryExceptionDetails` | String |  |  |  |  | A free-text description used to expand on the SearchQueryExceptions selections made by the host. | [link](https://ddwiki.reso.org/display/DDW20/SearchQueryExceptionDetails+Field) |
| `SearchQueryExceptions` | String List, Single |  | SearchQueryExceptions |  |  | A list of exceptions or errors with the given search query during its creation by the host. | [link](https://ddwiki.reso.org/display/DDW20/SearchQueryExceptions+Field) |
| `SearchQueryHumanReadable` | String |  |  |  |  | A human readable version of the search query that is commonly used for display and may not contain all actual criteria. | [link](https://ddwiki.reso.org/display/DDW20/SearchQueryHumanReadable+Field) |
| `SearchQueryType` | String List, Single |  | [SearchQueryType](#searchquerytype) |  |  | A pick list of the type of query language used in the SearchQuery field (e.g., DMQL2, $filter). | [link](https://ddwiki.reso.org/display/DDW20/SearchQueryType+Field) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the SavedSearch record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135537) |
| `SourceSystemID` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135542) |
| `SourceSystemKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135549) |
| `SourceSystemName` | String |  |  |  |  | The name of the record provider of the saved search. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135554) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Member</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** AUG 28 2019

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>OriginatingSystemMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>OriginatingSystemMemberName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Miembro Sistema de Origen
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>SavedSearchDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción de Búsqueda Guardada
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** OCT 18 2014

</details>

<details><summary><code>SavedSearchKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Búsqueda Guardada
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** OCT 18 2014

</details>

<details><summary><code>SearchQuery</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Consulta de Búsqueda
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** APR 16 2015

</details>

<details><summary><code>SearchQueryExceptionDetails</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Detalles de Excepción de Consulta de Búsqueda
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** AUG 15 2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryExceptions</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Excepciones de Consulta de Búsqueda
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** AUG 15 2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryHumanReadable</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Consulta de Búsqueda Legible para Humanos
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** NOV 18 2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Consulta de Búsqueda
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 02 2018

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

### ResourceName

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

### SearchQueryType

| Value | Definition |
|---|---|
| `$filter` | The query is in the form of Odata's $filter. |
| `DMQL2` | The query is in the form of DMQL2. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
