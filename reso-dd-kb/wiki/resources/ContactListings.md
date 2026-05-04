# ContactListings

_RESO Data Dictionary 2.0 resource — 22 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/ContactListings+Resource) for the canonical page._

## Groups

- **Other** — 22 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `AgentNotesUnreadYN` | Boolean |  |  |  |  | Indicates whether or not agent notes have gone unread. | [link](https://ddwiki.reso.org/display/DDW20/AgentNotesUnreadYN+Field) |
| `ClassName` | String List, Single |  | [ClassName](#classname) |  |  | The name of the class where the listing record is located. | [link](https://ddwiki.reso.org/display/DDW20/ClassName+Field) |
| `Contact` | Resource |  |  |  |  | The contact for the ContactListings record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116188) |
| `ContactKey` | String |  |  |  |  | A system-unique identifier for the contact. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135229) |
| `ContactListingPreference` | String List, Single |  | [ContactListingPreference](#contactlistingpreference) |  |  | The contact's preference selection on the given listing (i.e., Favorite, Possibility or Discard). | [link](https://ddwiki.reso.org/display/DDW20/ContactListingPreference+Field) |
| `ContactListingsKey` | String |  |  |  |  | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/ContactListingsKey+Field) |
| `ContactLoginId` | String |  |  |  |  | The foreign key referring to the Contacts Resource's local, well-known identifier for the contact. | [link](https://ddwiki.reso.org/display/DDW20/ContactLoginId+Field) |
| `ContactNotesUnreadYN` | Boolean |  |  |  |  | A flag indicating whether or not the contact's notes are unread. | [link](https://ddwiki.reso.org/display/DDW20/ContactNotesUnreadYN+Field) |
| `DirectEmailYN` | Boolean |  |  |  |  | A flag indicating whether or not this is a direct email. | [link](https://ddwiki.reso.org/display/DDW20/DirectEmailYN+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135265) |
| `LastAgentNoteTimestamp` | Timestamp |  |  |  |  | The date/time the member last added or updated a ListingNote. | [link](https://ddwiki.reso.org/display/DDW20/LastAgentNoteTimestamp+Field) |
| `LastContactNoteTimestamp` | Timestamp |  |  |  |  | The date/time the contact last added or updated a ListingNote. | [link](https://ddwiki.reso.org/display/DDW20/LastContactNoteTimestamp+Field) |
| `Listing` | Resource |  |  |  |  | The listing for the ContactListings record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116249) |
| `ListingId` | String |  |  |  |  | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135288) |
| `ListingKey` | String |  |  |  |  | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135294) |
| `ListingModificationTimestamp` | Timestamp |  |  |  |  | The last time the listing was updated. | [link](https://ddwiki.reso.org/display/DDW20/ListingModificationTimestamp+Field) |
| `ListingNotes` | Collection |  |  |  |  | The notes input by the member and/or contact in reference to the given listing. | [link](https://ddwiki.reso.org/display/DDW20/ListingNotes+Field) |
| `ListingSentTimestamp` | Timestamp |  |  |  |  | The date/time the listing was sent to the contact. | [link](https://ddwiki.reso.org/display/DDW20/ListingSentTimestamp+Field) |
| `ListingViewedYN` | Boolean |  |  |  |  | Indicates whether or not a listing has been viewed. | [link](https://ddwiki.reso.org/display/DDW20/ListingViewedYN+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135324) |
| `PortalLastVisitedTimestamp` | Timestamp |  |  |  |  | The date/time the listing was last viewed by the contact. | [link](https://ddwiki.reso.org/display/DDW20/PortalLastVisitedTimestamp+Field) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://ddwiki.reso.org/display/DDW20/ResourceName+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>AgentNotesUnreadYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Notas de Agente sin Leer SN
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ClassName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** SEP 26 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Contact</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ContactKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Contacto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactListingPreference</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Preferencia de Contacto de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactLoginId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Ingreso de Contacto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactNotesUnreadYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Notas de Contacto No Leídas SN
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>DirectEmailYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Email Directo SN
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LastAgentNoteTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de TiempoÚltima Nota del Agente
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>LastContactNoteTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de TiempoÚltima Nota de Contrato
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingSentTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Listado Enviado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** AUG 28 2019
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingViewedYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Listado Visto SN
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PortalLastVisitedTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Última Visita al Portal
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 02 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** SEP 26 2017
  - **Added in Version:** 1.6.0

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

### ContactListingPreference

| Value | Definition |
|---|---|
| `Discard` | The contact has flagged to discard the given listing. |
| `Favorite` | The contact has flagged the given listing as a favorite. |
| `Possibility` | The contact has flagged the given listing as a possibility. |

### ResourceName

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
