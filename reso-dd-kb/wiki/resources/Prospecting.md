# Prospecting

Automatic email connecting Contacts and SavedSearch resources to send results matching saved search criteria.

**RESO DD 2.0** — 31 fields · last revised 5/2/2017 · [dd.reso.org](https://dd.reso.org/DD2.0/Prospecting/)

**Adoption** — weighted Org%: **0%** across 2 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 31 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ActiveYN` | Boolean |  |  |  | If set to True, the given automated email is active. | [link](https://dd.reso.org/DD2.0/Prospecting/ActiveYN/) |
| `BccEmailList` | String |  |  |  | A comma-separated list of email addresses that are the blind carbon copy (Bcc) address that the automated emails are being sent to. | [link](https://dd.reso.org/DD2.0/Prospecting/BccEmailList/) |
| `BccMeYN` | Boolean |  |  |  | When set to True, the automated mail is also sent as a blind carbon copy (Bcc) to the member who created the automated email. | [link](https://dd.reso.org/DD2.0/Prospecting/BccMeYN/) |
| `CcEmailList` | String |  |  |  | A comma-separated list of email addresses that are the carbon copy (Cc) address that the automated emails are being sent to. | [link](https://dd.reso.org/DD2.0/Prospecting/CcEmailList/) |
| `ClientActivatedYN` | Boolean |  |  |  | If set to True, the client has clicked through to accept automatic emails. | [link](https://dd.reso.org/DD2.0/Prospecting/ClientActivatedYN/) |
| `ConciergeNotificationsYN` | Boolean |  |  |  | If set to True, notifications are to be sent to the member when the auto email is in Concierge mode. | [link](https://dd.reso.org/DD2.0/Prospecting/ConciergeNotificationsYN/) |
| `ConciergeYN` | Boolean |  |  |  | When set to True, the automated mail is in Concierge mode and is to be approved by the member before being sent to the client. | [link](https://dd.reso.org/DD2.0/Prospecting/ConciergeYN/) |
| `Contact` | Resource |  |  |  | The prospecting Contact record. | [link](https://dd.reso.org/DD2.0/Prospecting/Contact/) |
| `ContactKey` | String |  |  |  | A system-unique identifier for the contact. | [link](https://dd.reso.org/DD2.0/Prospecting/ContactKey/) |
| `DailySchedule` | String List, Multi |  | [DailySchedule](#dailyschedule) |  | When Daily is selected as the ScheduleType, a list of days of the week and AM or PM options. | [link](https://dd.reso.org/DD2.0/Prospecting/DailySchedule/) |
| `DisplayTemplateID` | String |  |  |  | The system ID of the display that has been related or set as the default to this saved search. | [link](https://dd.reso.org/DD2.0/Prospecting/DisplayTemplateID/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/Prospecting/HistoryTransactional/) |
| `Language` | String List, Single |  | [Languages](#languages) |  | The language that will be used in the given automated email. | [link](https://dd.reso.org/DD2.0/Prospecting/Language/) |
| `LastNewChangedTimestamp` | Timestamp |  |  |  | The timestamp of when the prospector last found new or modified listings for an automated email. | [link](https://dd.reso.org/DD2.0/Prospecting/LastNewChangedTimestamp/) |
| `LastViewedTimestamp` | Timestamp |  |  |  | A timestamp of when the automated email was last viewed by the client in the portal. | [link](https://dd.reso.org/DD2.0/Prospecting/LastViewedTimestamp/) |
| `Media` | Collection |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://dd.reso.org/DD2.0/Prospecting/Media/) |
| `MessageNew` | String |  |  |  | The body of the automated email message when the first email is sent for the prospecting campaign. | [link](https://dd.reso.org/DD2.0/Prospecting/MessageNew/) |
| `MessageRevise` | String |  |  |  | The body of the automated email message to be used when the criteria or settings of an automated email has been modified. | [link](https://dd.reso.org/DD2.0/Prospecting/MessageRevise/) |
| `MessageUpdate` | String |  |  |  | The body of the automated email message for subsequent email messages after the first email is sent. | [link](https://dd.reso.org/DD2.0/Prospecting/MessageUpdate/) |
| `ModificationTimestamp` | Timestamp |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/Prospecting/ModificationTimestamp/) |
| `NextSendTimestamp` | Timestamp |  |  |  | A timestamp of when the automated email is schedule to next send. | [link](https://dd.reso.org/DD2.0/Prospecting/NextSendTimestamp/) |
| `OwnerMember` | Resource |  |  |  | The member who owns the Prospecting record. | [link](https://dd.reso.org/DD2.0/Prospecting/OwnerMember/) |
| `OwnerMemberID` | String |  |  |  | The local, well-known identifier for the member owning the contact. | [link](https://dd.reso.org/DD2.0/Prospecting/OwnerMemberID/) |
| `OwnerMemberKey` | String |  |  |  | A system-unique identifier for the member that owns the contact record (References Member.MemberKey). | [link](https://dd.reso.org/DD2.0/Prospecting/OwnerMemberKey/) |
| `ProspectingKey` | String |  |  | 0% | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/Prospecting/ProspectingKey/) |
| `ReasonActiveOrDisabled` | String List, Single |  | [ReasonActiveOrDisabled](#reasonactiveordisabled) |  | A list of reasons the automated email was set to inactive or set back to active (e.g., Agent Disabled, Over Limit, No Listings Found, Reactivated, Client Disabled). | [link](https://dd.reso.org/DD2.0/Prospecting/ReasonActiveOrDisabled/) |
| `SavedSearch` | Resource |  |  |  | The saved search associated with the Prospecting record. | [link](https://dd.reso.org/DD2.0/Prospecting/SavedSearch/) |
| `SavedSearchKey` | String |  |  |  | This is the foreign key relating to the SavedSearch Resource. | [link](https://dd.reso.org/DD2.0/Prospecting/SavedSearchKey/) |
| `ScheduleType` | String List, Single |  | [ScheduleType](#scheduletype) |  | A selection of the type of schedule that the automated email will be sent (i.e., Daily, Monthly or ASAP). | [link](https://dd.reso.org/DD2.0/Prospecting/ScheduleType/) |
| `Subject` | String |  |  |  | The subject line of the automated email being sent. | [link](https://dd.reso.org/DD2.0/Prospecting/Subject/) |
| `ToEmailList` | String |  |  |  | A comma-separated list of email addresses that are the "To" address the automated emails are being sent to. | [link](https://dd.reso.org/DD2.0/Prospecting/ToEmailList/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ActiveYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Activo SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>BccEmailList</code></summary>

  - **Status:** Active
  - **Spanish Name:** Lista de Correo Electrónico CCO
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>BccMeYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** CCO Yo SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>CcEmailList</code></summary>

  - **Status:** Active
  - **Spanish Name:** Copiar Lista de Correo
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ClientActivatedYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Activado por Cliente SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ConciergeNotificationsYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Notificaciones de Conserjería SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ConciergeYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Conserjería SN
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Contact</code></summary>

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

<details><summary><code>DailySchedule</code></summary>

  - **Status:** Active
  - **Spanish Name:** Horario Diario
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>DisplayTemplateID</code></summary>

  - **Status:** Active
  - **Spanish Name:** Mostrar ID de Plantilla
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Language</code></summary>

  - **Status:** Active
  - **Spanish Name:** Idioma
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>LastNewChangedTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Último Cambio Nuevo
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>LastViewedTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de TiempoÚltima Vez Visto
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Media</code></summary>

  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MessageNew</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nuevo Mensaje
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>MessageRevise</code></summary>

  - **Status:** Active
  - **Spanish Name:** Revisar Mensaje
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>MessageUpdate</code></summary>

  - **Status:** Active
  - **Spanish Name:** Actualización Mensaje
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

<details><summary><code>NextSendTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Próximo Envío
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>OwnerMember</code></summary>

  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OwnerMemberID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Miembro Propietario
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>OwnerMemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro Propietario
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ProspectingKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Prospección
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ReasonActiveOrDisabled</code></summary>

  - **Status:** Active
  - **Spanish Name:** Modo Activo o Desactivado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>SavedSearch</code></summary>

  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SavedSearchKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Búsqueda Guardada
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ScheduleType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Horario
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>Subject</code></summary>

  - **Status:** Active
  - **Spanish Name:** Asunto
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ToEmailList</code></summary>

  - **Status:** Active
  - **Spanish Name:** Lista de Envíos por Correo Electrónico
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/2/2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### DailySchedule

15 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/DailySchedule/)

| Value | Definition |
|---|---|
| `Friday AM` | The prospect automated email will be sent every Friday morning. |
| `Friday PM` | The prospect automated email will be sent every Friday evening. |
| `Monday AM` | The prospect automated email will be sent every Monday morning. |
| `Monday PM` | The prospect automated email will be sent every Monday evening. |
| `None` | The prospect automated email has not been setup for any daily schedule. |
| `Saturday AM` | The prospect automated email will be sent every Saturday morning. |
| `Saturday PM` | The prospect automated email will be sent every Saturday evening. |
| `Sunday AM` | The prospect automated email will be sent every Sunday morning. |
| `Sunday PM` | The prospect automated email will be sent every Sunday evening. |
| `Thursday AM` | The prospect automated email will be sent every Thursday morning. |
| `Thursday PM` | The prospect automated email will be sent every Thursday evening. |
| `Tuesday AM` | The prospect automated email will be sent every Tuesday morning. |
| `Tuesday PM` | The prospect automated email will be sent every Tuesday evening. |
| `Wednesday AM` | The prospect automated email will be sent every Wednesday morning. |
| `Wednesday PM` | The prospect automated email will be sent every Wednesday evening. |

### Languages

190 values · used by 3 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Languages/)

| Value | Definition |
|---|---|
| `Abkhazian` | The language spoken by the member/individual is Abkhazian. |
| `Afar` | The language spoken by the member/individual is Afar. |
| `Afrikaans` | The language spoken by the member/individual is Afrikaans. |
| `Albanian` | The language spoken by the member/individual is Albanian. |
| `American Sign Language` | The language spoken by the member/individual is American Sign Language. |
| `Amharic` | The language spoken by the member/individual is Amharic. |
| `Arabic` | The language spoken by the member/individual is Arabic. |
| `Aramaic` | The language spoken by the member/individual is Aramaic. |
| `Armenian` | The language spoken by the member/individual is Armenian. |
| `Assamese` | The language spoken by the member/individual is Assamese. |
| `Assyrian Neo-Aramaic` | The language spoken by the member/individual is Assyrian Neo-Aramaic. |
| `Avestan` | The language spoken by the member/individual is Avestan. |
| `Aymara` | The language spoken by the member/individual is Aymara. |
| `Azerbaijani` | The language spoken by the member/individual is Azerbaijani. |
| `Bambara` | The language spoken by the member/individual is Bambara. |
| `Bashkir` | The language spoken by the member/individual is Bashkir. |
| `Basque` | The language spoken by the member/individual is Basque. |
| `Bengali` | The language spoken by the member/individual is Bengali. |
| `Bihari` | The language spoken by the member/individual is Bihari. |
| `Bikol` | The language spoken by the member/individual is Bikol. |
| `Bislama` | The language spoken by the member/individual is Bislama. |
| `Bosnian` | The language spoken by the member/individual is Bosnian. |
| `Brazilian Portuguese` | The language spoken by the member/individual is Brazilian Portuguese. |
| `Bulgarian` | The language spoken by the member/individual is Bulgarian. |
| `Burmese` | The language spoken by the member/individual is Burmese. |
| `Byelorussian` | The language spoken by the member/individual is Byelorussian. |
| `Cambodian` | The language spoken by the member/individual is Cambodian. |
| `Cantonese` | The language spoken by the member/individual is Cantonese. |
| `Cape Verdean Creole` | The language spoken by the member/individual is Cape Verdean Creole. |
| `Catalan` | The language spoken by the member/individual is Catalan. |
| `Cebuano` | The language spoken by the member/individual is Cebuano. |
| `Chamorro` | The language spoken by the member/individual is Chamorro. |
| `Chechen` | The language spoken by the member/individual is Chechen. |
| `Chinese` | The language spoken by the member/individual is Chinese. |
| `Chuukese` | The language spoken by the member/individual is Chuukese. |
| `Chuvash` | The language spoken by the member/individual is Chuvash. |
| `Cornish` | The language spoken by the member/individual is Cornish. |
| `Corsican` | The language spoken by the member/individual is Corsican. |
| `Croatian` | The language spoken by the member/individual is Croatian. |
| `Czech` | The language spoken by the member/individual is Czech. |
| `Danish` | The language spoken by the member/individual is Danish. |
| `Dari (Afghan Persian)` | The language spoken by the member/individual is Dari (Afghan Persian). |
| `Dioula` | The language spoken by the member/individual is Dioula. |
| `Dutch` | The language spoken by the member/individual is Dutch. |
| `Dzongkha` | The language spoken by the member/individual is Dzongkha. |
| `English` | The language spoken by the member/individual is English. |
| `Esperanto` | The language spoken by the member/individual is Esperanto. |
| `Estonian` | The language spoken by the member/individual is Estonian. |
| `Faroese` | The language spoken by the member/individual is Faroese. |
| `Farsi` | The language spoken by the member/individual is Farsi. |
| `Fiji` | The language spoken by the member/individual is Fiji. |
| `Finnish` | The language spoken by the member/individual is Finnish. |
| `Flemish` | The language spoken by the member/individual is Flemish. |
| `French` | The language spoken by the member/individual is French. |
| `Frisian` | The language spoken by the member/individual is Frisian. |
| `Galician` | The language spoken by the member/individual is Galician. |
| `Georgian` | The language spoken by the member/individual is Georgian. |
| `German` | The language spoken by the member/individual is German. |
| `Greek` | The language spoken by the member/individual is Greek. |
| `Greenlandic` | The language spoken by the member/individual is Greenlandic. |
| `Guarani` | The language spoken by the member/individual is Guarani. |
| `Gujarati` | The language spoken by the member/individual is Gujarati. |
| `Haitian Creole` | The language spoken by the member/individual is Haitian Creole. |
| `Hausa` | The language spoken by the member/individual is Hausa. |
| `Hebrew` | The language spoken by the member/individual is Hebrew. |
| `Herero` | The language spoken by the member/individual is Herero. |
| `Hiligaynon` | The language spoken by the member/individual is Hiligaynon. |
| `Hindi` | The language spoken by the member/individual is Hindi. |
| `Hiri Motu` | The language spoken by the member/individual is Hiri Motu. |
| `Hmong` | The language spoken by the member/individual is Hmong. |
| `Hungarian` | The language spoken by the member/individual is Hungarian. |
| `Iban` | The language spoken by the member/individual is Iban. |
| `Icelandic` | The language spoken by the member/individual is Icelandic. |
| `Igbo` | The language spoken by the member/individual is Igbo. |
| `Ilocano` | The language spoken by the member/individual is Ilocano. |
| `Indonesian` | The language spoken by the member/individual is Indonesian. |
| `Interlingua` | The language spoken by the member/individual is Interlingua. |
| `Inuktitut` | The language spoken by the member/individual is Inuktitut. |
| `Inupiak` | The language spoken by the member/individual is Inupiak. |
| `Irish (Gaelic)` | The language spoken by the member/individual is Irish (Gaelic). |
| `Italian` | The language spoken by the member/individual is Italian. |
| `Japanese` | The language spoken by the member/individual is Japanese. |
| `Javanese` | The language spoken by the member/individual is Javanese. |
| `Kannada` | The language spoken by the member/individual is Kannada. |
| `Kashmiri` | The language spoken by the member/individual is Kashmiri. |
| `Kazakh` | The language spoken by the member/individual is Kazakh. |
| `K'iche'` | The language spoken by the member/individual is K'iche'. |
| `Kichwa` | The language spoken by the member/individual is Kichwa. |
| `Kikuyu` | The language spoken by the member/individual is Kikuyu. |
| `Kinyarwanda` | The language spoken by the member/individual is Kinyarwanda. |
| `Kirghiz` | The language spoken by the member/individual is Kirghiz. |
| `Kirundi` | The language spoken by the member/individual is Kirundi. |
| `Komi` | The language spoken by the member/individual is Komi. |
| `Korean` | The language spoken by the member/individual is Korean. |
| `Kpelle` | The language spoken by the member/individual is Kpelle. |
| `Kru` | The language spoken by the member/individual is Kru. |
| `Kurdish` | The language spoken by the member/individual is Kurdish. |
| `Lao` | The language spoken by the member/individual is Lao. |
| `Latin` | The language spoken by the member/individual is Latin. |
| `Latvian` | The language spoken by the member/individual is Latvian. |
| `Lingala` | The language spoken by the member/individual is Lingala. |
| `Lithuanian` | The language spoken by the member/individual is Lithuanian. |
| `Luxemburgish` | The language spoken by the member/individual is Luxemburgish. |
| `Macedonian` | The language spoken by the member/individual is Macedonian. |
| `Malagasy` | The language spoken by the member/individual is Malagasy. |
| `Malay` | The language spoken by the member/individual is Malay. |
| `Malayalam` | The language spoken by the member/individual is Malayalam. |
| `Maltese` | The language spoken by the member/individual is Maltese. |
| `Mandarin` | The language spoken by the member/individual is Mandarin. |
| `Maninka` | The language spoken by the member/individual is Maninka. |
| `Manx Gaelic` | The language spoken by the member/individual is Manx Gaelic. |
| `Maori` | The language spoken by the member/individual is Maori. |
| `Marathi` | The language spoken by the member/individual is Marathi. |
| `Marshallese` | The language spoken by the member/individual is Marshallese. |
| `Moldovan` | The language spoken by the member/individual is Moldovan. |
| `Mongolian` | The language spoken by the member/individual is Mongolian. |
| `Nauru` | The language spoken by the member/individual is Nauru. |
| `Navajo` | The language spoken by the member/individual is Navajo. |
| `Ndebele` | The language spoken by the member/individual is Ndebele. |
| `Ndonga` | The language spoken by the member/individual is Ndonga. |
| `Nepali` | The language spoken by the member/individual is Nepali. |
| `Norwegian` | The language spoken by the member/individual is Norwegian. |
| `Norwegian (Nynorsk)` | The language spoken by the member/individual is Norwegian (Nynorsk). |
| `Nyanja` | The language spoken by the member/individual is Nyanja. |
| `Occitan` | The language spoken by the member/individual is Occitan. |
| `Oriya` | The language spoken by the member/individual is Oriya. |
| `Oromo` | The language spoken by the member/individual is Oromo. |
| `Ossetian` | The language spoken by the member/individual is Ossetian. |
| `Pali` | The language spoken by the member/individual is Pali. |
| `Pangasinan` | The language spoken by the member/individual is Pangasinan. |
| `Papiamento` | The language spoken by the member/individual is Papiamento. |
| `Pashto` | The language spoken by the member/individual is Pashto. |
| `Polish` | The language spoken by the member/individual is Polish. |
| `Portuguese` | The language spoken by the member/individual is Portuguese. |
| `Punjabi` | The language spoken by the member/individual is Punjabi. |
| `Quechua` | The language spoken by the member/individual is Quechua. |
| `Romanian` | The language spoken by the member/individual is Romanian. |
| `Romany` | The language spoken by the member/individual is Romany. |
| `Russian` | The language spoken by the member/individual is Russian. |
| `Sami` | The language spoken by the member/individual is Sami. |
| `Samoan` | The language spoken by the member/individual is Samoan. |
| `Sangho` | The language spoken by the member/individual is Sangho. |
| `Sanskrit` | The language spoken by the member/individual is Sanskrit. |
| `Sardinian` | The language spoken by the member/individual is Sardinian. |
| `Scots Gaelic` | The language spoken by the member/individual is Scots Gaelic. |
| `Serbian` | The language spoken by the member/individual is Serbian. |
| `Serbo-Croatian` | The language spoken by the member/individual is Serbo-Croatian. |
| `Sesotho` | The language spoken by the member/individual is Sesotho. |
| `Setswana` | The language spoken by the member/individual is Setswana. |
| `Shan` | The language spoken by the member/individual is Shan. |
| `Shona` | The language spoken by the member/individual is Shona. |
| `Sindhi` | The language spoken by the member/individual is Sindhi. |
| `Sinhalese` | The language spoken by the member/individual is Sinhalese. |
| `Siswati` | The language spoken by the member/individual is Siswati. |
| `Slovak` | The language spoken by the member/individual is Slovak. |
| `Slovenian` | The language spoken by the member/individual is Slovenian. |
| `Somali` | The language spoken by the member/individual is Somali. |
| `Southern Ndebele` | The language spoken by the member/individual is Southern Ndebele. |
| `Spanish` | The language spoken by the member/individual is Spanish. |
| `Sundanese` | The language spoken by the member/individual is Sundanese. |
| `Swahili` | The language spoken by the member/individual is Swahili. |
| `Swedish` | The language spoken by the member/individual is Swedish. |
| `Syriac` | The language spoken by the member/individual is Syriac. |
| `Tagalog` | The language spoken by the member/individual is Tagalog. |
| `Tahitian` | The language spoken by the member/individual is Tahitian. |
| `Tajik` | The language spoken by the member/individual is Tajik. |
| `Tamil` | The language spoken by the member/individual is Tamil. |
| `Tatar` | The language spoken by the member/individual is Tatar. |
| `Telugu` | The language spoken by the member/individual is Telugu. |
| `Thai` | The language spoken by the member/individual is Thai. |
| `Tibetan` | The language spoken by the member/individual is Tibetan. |
| `Tigrinya` | The language spoken by the member/individual is Tigrinya. |
| `Tongan` | The language spoken by the member/individual is Tongan. |
| `Tsonga` | The language spoken by the member/individual is Tsonga. |
| `Turkish` | The language spoken by the member/individual is Turkish. |
| `Turkmen` | The language spoken by the member/individual is Turkmen. |
| `Twi` | The language spoken by the member/individual is Twi. |
| `Uigur` | The language spoken by the member/individual is Uigur. |
| `Ukrainian` | The language spoken by the member/individual is Ukrainian. |
| `Urdu` | The language spoken by the member/individual is Urdu. |
| `Uzbek` | The language spoken by the member/individual is Uzbek. |
| `Vietnamese` | The language spoken by the member/individual is Vietnamese. |
| `Volapuk` | The language spoken by the member/individual is Volapuk. |
| `Welsh` | The language spoken by the member/individual is Welsh. |
| `Wolof` | The language spoken by the member/individual is Wolof. |
| `Xhosa` | The language spoken by the member/individual is Xhosa. |
| `Yiddish` | The language spoken by the member/individual is Yiddish. |
| `Yoruba` | The language spoken by the member/individual is Yoruba. |
| `Zhuang` | The language spoken by the member/individual is Zhuang. |
| `Zulu` | The language spoken by the member/individual is Zulu. |

### ReasonActiveOrDisabled

16 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ReasonActiveOrDisabled/)

| Value | Definition |
|---|---|
| `Agent Disabled` | The agent has disabled this auto email. |
| `Client Disabled` | The auto email has been disabled by the client/recipient. |
| `Concierge Notification` | The automated email is on hold pending concierge approval by the member and is temporarily disabled. |
| `Final Ignored Warning` | The final warning that the automated email has not been viewed by the client/recipient and may be inactivated due to being ignored but is still active. |
| `Ignored` | The automated email was not viewed by the client/recipient in the time frame designated by the host system and has been disabled. |
| `Initial Ignored Warning` | The first warning that the auto email has not been viewed by the client/recipient. |
| `Invalid` | The automated email is no longer valid per some conditions set by the host system and has been disabled. |
| `No Listings Found` | The automated email has not found any listings matching the criteria and has been disabled per the host system rules. |
| `No Listings Found Warning` | The automated email has not found any listings matching the criteria and may be disabled but is still active. |
| `No One To Send To` | There is no valid email address and the auto email has been inactivated. |
| `Over Limit` | The automated email has reached the limit of listing results as set by the host system and has been disabled. |
| `Re-Activated` | The automated email was previously disabled and has been set back to active. |
| `Revised` | The automated email has been revised and is active. |
| `Search Failing` | The automated email's search criteria is failing, should be reviewed by the host system and has been disabled. |
| `Welcome Email Ignored` | The initial automated email has not been viewed by the client/recipient and has been deactivated. |
| `Welcome Email Ignored Warning` | The initial automated email has not been viewed by the client/recipient but is still active. |

### ScheduleType

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ScheduleType/)

| Value | Definition |
|---|---|
| `ASAP` | The prospect will be sent automated emails as soon as possible through each day. |
| `Daily` | The prospect will be sent automated emails daily. |
| `Monthly` | The prospect will be sent automated emails once per month. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
