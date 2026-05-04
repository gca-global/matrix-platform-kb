# ContactListings

Maintains the relationship between contacts and members around listings in consumer portals.

**RESO DD 2.0** — 22 fields · last revised 9/26/2017 · [dd.reso.org](https://dd.reso.org/DD2.0/ContactListings/)

## Groups

- **Other** — 22 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `AgentNotesUnreadYN` | Boolean |  |  |  | Indicates whether or not agent notes have gone unread. | [link](https://dd.reso.org/DD2.0/ContactListings/AgentNotesUnreadYN/) |
| `ClassName` | String List, Single |  | [ClassName](#classname) |  | The name of the class where the listing record is located. | [link](https://dd.reso.org/DD2.0/ContactListings/ClassName/) |
| `Contact` | Resource |  |  |  | The contact for the ContactListings record. | [link](https://dd.reso.org/DD2.0/ContactListings/Contact/) |
| `ContactKey` | String |  |  |  | A system-unique identifier for the contact. | [link](https://dd.reso.org/DD2.0/ContactListings/ContactKey/) |
| `ContactListingPreference` | String List, Single |  | [ContactListingPreference](#contactlistingpreference) |  | The contact's preference selection on the given listing (i.e., Favorite, Possibility or Discard). | [link](https://dd.reso.org/DD2.0/ContactListings/ContactListingPreference/) |
| `ContactListingsKey` | String |  |  |  | A system unique identifier. | [link](https://dd.reso.org/DD2.0/ContactListings/ContactListingsKey/) |
| `ContactLoginId` | String |  |  |  | The foreign key referring to the Contacts Resource's local, well-known identifier for the contact. | [link](https://dd.reso.org/DD2.0/ContactListings/ContactLoginId/) |
| `ContactNotesUnreadYN` | Boolean |  |  |  | A flag indicating whether or not the contact's notes are unread. | [link](https://dd.reso.org/DD2.0/ContactListings/ContactNotesUnreadYN/) |
| `DirectEmailYN` | Boolean |  |  |  | A flag indicating whether or not this is a direct email. | [link](https://dd.reso.org/DD2.0/ContactListings/DirectEmailYN/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/ContactListings/HistoryTransactional/) |
| `LastAgentNoteTimestamp` | Timestamp |  |  |  | The date/time the member last added or updated a ListingNote. | [link](https://dd.reso.org/DD2.0/ContactListings/LastAgentNoteTimestamp/) |
| `LastContactNoteTimestamp` | Timestamp |  |  |  | The date/time the contact last added or updated a ListingNote. | [link](https://dd.reso.org/DD2.0/ContactListings/LastContactNoteTimestamp/) |
| `Listing` | Resource |  |  |  | The listing for the ContactListings record. | [link](https://dd.reso.org/DD2.0/ContactListings/Listing/) |
| `ListingId` | String |  |  |  | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingId/) |
| `ListingKey` | String |  |  |  | A system-unique identifier for the listing. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingKey/) |
| `ListingModificationTimestamp` | Timestamp |  |  |  | The last time the listing was updated. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingModificationTimestamp/) |
| `ListingNotes` | Collection |  |  |  | The notes input by the member and/or contact in reference to the given listing. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingNotes/) |
| `ListingSentTimestamp` | Timestamp |  |  |  | The date/time the listing was sent to the contact. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingSentTimestamp/) |
| `ListingViewedYN` | Boolean |  |  |  | Indicates whether or not a listing has been viewed. | [link](https://dd.reso.org/DD2.0/ContactListings/ListingViewedYN/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/ContactListings/ModificationTimestamp/) |
| `PortalLastVisitedTimestamp` | Timestamp |  |  |  | The date/time the listing was last viewed by the contact. | [link](https://dd.reso.org/DD2.0/ContactListings/PortalLastVisitedTimestamp/) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/ContactListings/ResourceName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>AgentNotesUnreadYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Notas de Agente sin Leer SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 9/26/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Contact</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ContactKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Contacto
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactListingPreference</code></summary>

  - **Status:** Active
  - **Spanish Name:** Preferencia de Contacto de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactListingsKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/3/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ContactLoginId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Ingreso de Contacto
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ContactNotesUnreadYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Notas de Contacto No Leídas SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>DirectEmailYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Email Directo SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LastAgentNoteTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de TiempoÚltima Nota del Agente
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>LastContactNoteTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de TiempoÚltima Nota de Contrato
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Modificación de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingNotes</code></summary>

  - **Status:** Active
  - **Spanish Name:** Notas de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingSentTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Listado Enviado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 8/28/2019
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingViewedYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Listado Visto SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PortalLastVisitedTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Última Visita al Portal
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Recurso
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 9/26/2017
  - **Added in Version:** 1.6.0

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

### ContactListingPreference

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ContactListingPreference/)

| Value | Definition |
|---|---|
| `Discard` | The contact has flagged to discard the given listing. |
| `Favorite` | The contact has flagged the given listing as a favorite. |
| `Possibility` | The contact has flagged the given listing as a possibility. |

### ResourceName

5 values · used by 7 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ResourceName/)

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
