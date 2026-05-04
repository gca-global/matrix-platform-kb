# SavedSearch

Saved search criteria and related data.

**RESO DD 2.0** — 27 fields · last revised 8/28/2019 · [dd.reso.org](https://dd.reso.org/DD2.0/SavedSearch/)

**Adoption** — weighted Org%: **0%** across 2 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 27 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) |  | The class or table to which the SearchQuery criteria refers (e.g., Residential, Residential Lease, Residential Income, Commercial Sale). | [link](https://dd.reso.org/DD2.0/SavedSearch/ClassName/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/SavedSearch/HistoryTransactional/) |
| `Member` | Resource |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://dd.reso.org/DD2.0/SavedSearch/Member/) |
| `MemberKey` | String |  |  |  | A system-unique identifier for the member. | [link](https://dd.reso.org/DD2.0/SavedSearch/MemberKey/) |
| `MemberMlsId` | String |  |  |  | The local, well-known identifier for the member as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/SavedSearch/MemberMlsId/) |
| `ModificationTimestamp` | Timestamp |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/SavedSearch/ModificationTimestamp/) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  | The transactional timestamp automatically recorded by the MLS system representing the date/time that the saved search was entered. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the SavedSearch record. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystemID/) |
| `OriginatingSystemKey` | String |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystemKey/) |
| `OriginatingSystemMemberKey` | String |  |  |  | Unique identifier from the originating system, which is commonly a key to that system. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystemMemberKey/) |
| `OriginatingSystemMemberName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystemMemberName/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/SavedSearch/OriginatingSystemName/) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/SavedSearch/ResourceName/) |
| `SavedSearchDescription` | String |  |  |  | A textual description of the saved search input by the member who created the saved search. | [link](https://dd.reso.org/DD2.0/SavedSearch/SavedSearchDescription/) |
| `SavedSearchKey` | String |  |  | 0% | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/SavedSearch/SavedSearchKey/) |
| `SavedSearchName` | String |  |  |  | The name given to the search by the member inputting the saved search. | [link](https://dd.reso.org/DD2.0/SavedSearch/SavedSearchName/) |
| `SavedSearchType` | String List, Single |  | SavedSearchType |  | Determines if the saved search used to pass criteria is to be stored and executed by the client or if it is a key to be passed to the host for execution (i.e., Client Receives Criteria, Host Returns Listings). | [link](https://dd.reso.org/DD2.0/SavedSearch/SavedSearchType/) |
| `SearchQuery` | String |  |  |  | The textual representation of the search performed by the member that was saved. | [link](https://dd.reso.org/DD2.0/SavedSearch/SearchQuery/) |
| `SearchQueryExceptionDetails` | String |  |  |  | A free-text description used to expand on the SearchQueryExceptions selections made by the host. | [link](https://dd.reso.org/DD2.0/SavedSearch/SearchQueryExceptionDetails/) |
| `SearchQueryExceptions` | String List, Single |  | SearchQueryExceptions |  | A list of exceptions or errors with the given search query during its creation by the host. | [link](https://dd.reso.org/DD2.0/SavedSearch/SearchQueryExceptions/) |
| `SearchQueryHumanReadable` | String |  |  |  | A human readable version of the search query that is commonly used for display and may not contain all actual criteria. | [link](https://dd.reso.org/DD2.0/SavedSearch/SearchQueryHumanReadable/) |
| `SearchQueryType` | String List, Single |  | [SearchQueryType](#searchquerytype) |  | A pick list of the type of query language used in the SearchQuery field (e.g., DMQL2, $filter). | [link](https://dd.reso.org/DD2.0/SavedSearch/SearchQueryType/) |
| `SourceSystem` | Resource |  |  |  | The source system of the SavedSearch record. | [link](https://dd.reso.org/DD2.0/SavedSearch/SourceSystem/) |
| `SourceSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/SavedSearch/SourceSystemID/) |
| `SourceSystemKey` | String |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/SavedSearch/SourceSystemKey/) |
| `SourceSystemName` | String |  |  |  | The name of the record provider of the saved search. | [link](https://dd.reso.org/DD2.0/SavedSearch/SourceSystemName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/12/2015

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Member</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/28/2019

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/28/2019

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
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016

</details>

<details><summary><code>OriginatingSystemMemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro Sistema de Origen
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>OriginatingSystemMemberName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Miembro Sistema de Origen
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/12/2015

</details>

<details><summary><code>SavedSearchDescription</code></summary>

  - **Status:** Active
  - **Spanish Name:** Descripción de Búsqueda Guardada
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 10/18/2014

</details>

<details><summary><code>SavedSearchKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Búsqueda Guardada
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 10/18/2014

</details>

<details><summary><code>SavedSearchName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Búsqueda Guardada
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 10/18/2014

</details>

<details><summary><code>SavedSearchType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Búsqueda Guardada
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 10/18/2014

</details>

<details><summary><code>SearchQuery</code></summary>

  - **Status:** Active
  - **Spanish Name:** Consulta de Búsqueda
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 4/16/2015

</details>

<details><summary><code>SearchQueryExceptionDetails</code></summary>

  - **Status:** Active
  - **Spanish Name:** Detalles de Excepción de Consulta de Búsqueda
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/15/2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryExceptions</code></summary>

  - **Status:** Active
  - **Spanish Name:** Excepciones de Consulta de Búsqueda
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/15/2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryHumanReadable</code></summary>

  - **Status:** Active
  - **Spanish Name:** Consulta de Búsqueda Legible para Humanos
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 11/18/2015
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SearchQueryType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Consulta de Búsqueda
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

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
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave Sistema Fuente
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

### ResourceName

5 values · used by 7 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ResourceName/)

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

### SearchQueryType

2 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SearchQueryType/)

| Value | Definition |
|---|---|
| `$filter` | The query is in the form of Odata's $filter. |
| `DMQL2` | The query is in the form of DMQL2. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
