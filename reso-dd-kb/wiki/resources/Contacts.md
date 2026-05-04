# Contacts

The Contacts resource holds people in an MLS user's personal address book — buyers, sellers, prospects, lenders, vendors. Contacts contain PII (name, email, phone) and are NOT publicly broadcast; access is restricted to the owning Member.

**Adoption** — weighted Org%: **0%** across 2 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 91 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `Anniversary` | Date |  |  |  |  | The month, day and year of the contact's wedding anniversary. | [link](https://ddwiki.reso.org/display/DDW20/Anniversary+Field) |
| `AssistantEmail` | String |  |  |  |  | The email address of the contact's assistant. | [link](https://ddwiki.reso.org/display/DDW20/AssistantEmail+Field) |
| `AssistantName` | String |  |  |  |  | The name of the contact's assistant. | [link](https://ddwiki.reso.org/display/DDW20/AssistantName+Field) |
| `AssistantPhone` | String |  |  |  |  | The phone number of the contact's assistant. | [link](https://ddwiki.reso.org/display/DDW20/AssistantPhone+Field) |
| `AssistantPhoneExt` | String |  |  |  |  | The phone number extension of the contact's assistant. | [link](https://ddwiki.reso.org/display/DDW20/AssistantPhoneExt+Field) |
| `Birthdate` | Date |  |  | 1% | 1% | The month, day and year of the contact's birthday. | [link](https://ddwiki.reso.org/display/DDW20/Birthdate+Field) |
| `BusinessFax` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/BusinessFax+Field) |
| `Children` | String |  |  |  |  | A list of the names of the contact's children in a comma-separated list. | [link](https://ddwiki.reso.org/display/DDW20/Children+Field) |
| `Company` | String |  |  | 1% | 1% | The contact's company or employer. | [link](https://ddwiki.reso.org/display/DDW20/Company+Field) |
| `ContactKey` | String |  |  | 1% | 1% | A system-unique identifier for the contact. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116255) |
| `ContactLoginId` | String |  |  |  |  | The local, well-known identifier for the contact. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116259) |
| `ContactPassword` | String |  |  |  |  | A client password that the member wishes to share with other systems. | [link](https://ddwiki.reso.org/display/DDW20/ContactPassword+Field) |
| `ContactStatus` | String List, Single |  | [ContactStatus](#contactstatus) | 1% | 1% | The status of the contact (i.e., Active, Inactive, On Vacation, Deleted, etc.). | [link](https://ddwiki.reso.org/display/DDW20/ContactStatus+Field) |
| `ContactType` | String List, Multi |  | [ContactType](#contacttype) | 1% | 1% | The type of contact. | [link](https://ddwiki.reso.org/display/DDW20/ContactType+Field) |
| `ContactsOtherPhone` | Collection |  |  |  |  | A collection of the types of other phone fields available for Contacts. | [link](https://ddwiki.reso.org/display/DDW20/ContactsOtherPhone+Field) |
| `ContactsSocialMedia` | Collection |  |  |  |  | A collection of the types of social media fields available for Contacts. | [link](https://ddwiki.reso.org/display/DDW20/ContactsSocialMedia+Field) |
| `Department` | String |  |  |  |  | The department in which the contact works. | [link](https://ddwiki.reso.org/display/DDW20/Department+Field) |
| `DirectPhone` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/DirectPhone+Field) |
| `Email` | String |  |  | 1% | 1% | The email address of the contact. | [link](https://ddwiki.reso.org/display/DDW20/Email+Field) |
| `Email2` | String |  |  | 1% | 1% | The secondary email address of the contact. | [link](https://ddwiki.reso.org/display/DDW20/Email2+Field) |
| `Email3` | String |  |  |  |  | The tertiary email address of the contact. | [link](https://ddwiki.reso.org/display/DDW20/Email3+Field) |
| `FirstName` | String |  |  | 1% | 1% | The first or given name of the contact. | [link](https://ddwiki.reso.org/display/DDW20/FirstName+Field) |
| `FullName` | String |  |  | 1% | 1% | The full name of the contact - first middle last suffix. | [link](https://ddwiki.reso.org/display/DDW20/FullName+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135221) |
| `HomeAddress1` | String |  |  | 1% | 1% | The street number, direction, name and suffix of the contact's home. | [link](https://ddwiki.reso.org/display/DDW20/HomeAddress1+Field) |
| `HomeAddress2` | String |  |  |  |  | The unit/suite number of the contact's home. | [link](https://ddwiki.reso.org/display/DDW20/HomeAddress2+Field) |
| `HomeCarrierRoute` | String |  |  |  |  | The group of addresses to which the U.S. | [link](https://ddwiki.reso.org/display/DDW20/HomeCarrierRoute+Field) |
| `HomeCity` | String |  |  | 1% | 1% | The city of the contact's home. | [link](https://ddwiki.reso.org/display/DDW20/HomeCity+Field) |
| `HomeCountry` | String List, Single |  | [Country](#country) |  |  | The country abbreviation in a postal address. | [link](https://ddwiki.reso.org/display/DDW20/HomeCountry+Field) |
| `HomeCountyOrParish` | String List, Single |  | CountyOrParish |  |  | The county or parish in which the contact's home is addressed. | [link](https://ddwiki.reso.org/display/DDW20/HomeCountyOrParish+Field) |
| `HomeFax` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/HomeFax+Field) |
| `HomePhone` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/HomePhone+Field) |
| `HomePostalCode` | String |  |  |  |  | The postal code of the contact's home. | [link](https://ddwiki.reso.org/display/DDW20/HomePostalCode+Field) |
| `HomePostalCodePlus4` | String |  |  |  |  | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/HomePostalCodePlus4+Field) |
| `HomeStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 1% | 1% | The state or province in which the contact's home is addressed. | [link](https://ddwiki.reso.org/display/DDW20/HomeStateOrProvince+Field) |
| `JobTitle` | String |  |  | 1% | 1% | The title or position of the contact within their organization. | [link](https://ddwiki.reso.org/display/DDW20/JobTitle+Field) |
| `Language` | String List, Multi |  | [Languages](#languages) |  |  | The languages spoken by the contact. | [link](https://ddwiki.reso.org/display/DDW20/Language+Field) |
| `LastName` | String |  |  |  |  | The last or surname of the contact. | [link](https://ddwiki.reso.org/display/DDW20/LastName+Field) |
| `LeadSource` | String |  |  | 1% | 1% | The source or person that provided the contact. | [link](https://ddwiki.reso.org/display/DDW20/LeadSource+Field) |
| `Media` | Collection |  |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135316) |
| `MiddleName` | String |  |  | 1% | 1% | The middle name of the contact. | [link](https://ddwiki.reso.org/display/DDW20/MiddleName+Field) |
| `MobilePhone` | String |  |  |  |  | The mobile phone number of the contact. | [link](https://ddwiki.reso.org/display/DDW20/MobilePhone+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135334) |
| `NamePrefix` | String |  |  | 1% | 1% | The prefix to the name (e.g., Dr., Mr., Ms.). | [link](https://ddwiki.reso.org/display/DDW20/NamePrefix+Field) |
| `NameSuffix` | String |  |  | 1% | 1% | The suffix to the surname (e.g., Esq., Jr., III). | [link](https://ddwiki.reso.org/display/DDW20/NameSuffix+Field) |
| `Nickname` | String |  |  | 1% | 1% | An alternate name used by the contact, usually as a substitute for the first name. | [link](https://ddwiki.reso.org/display/DDW20/Nickname+Field) |
| `Notes` | String |  |  | 1% | 1% | The recorded notes about the client. | [link](https://ddwiki.reso.org/display/DDW20/Notes+Field) |
| `OfficePhone` | String |  |  | 1% | 1% | The main contact phone number of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficePhone+Field) |
| `OfficePhoneExt` | String |  |  |  |  | The extension of the given phone number (if applicable). | [link](https://ddwiki.reso.org/display/DDW20/OfficePhoneExt+Field) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The date/time the contact record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135378) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the contact's record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135383) |
| `OriginatingSystemContactKey` | String |  |  | 1% | 1% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemContactKey+Field) |
| `OriginatingSystemID` | String |  |  | 1% | 1% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135396) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135402) |
| `OtherAddress1` | String |  |  |  |  | The other street number, direction, name and suffix of the contact. | [link](https://ddwiki.reso.org/display/DDW20/OtherAddress1+Field) |
| `OtherAddress2` | String |  |  |  |  | The other unit/suite number of the contact. | [link](https://ddwiki.reso.org/display/DDW20/OtherAddress2+Field) |
| `OtherCarrierRoute` | String |  |  |  |  | The group of addresses to which the U.S. | [link](https://ddwiki.reso.org/display/DDW20/OtherCarrierRoute+Field) |
| `OtherCity` | String |  |  |  |  | The other city of the contact. | [link](https://ddwiki.reso.org/display/DDW20/OtherCity+Field) |
| `OtherCountry` | String List, Single |  | [Country](#country) |  |  | The other country abbreviation in a postal address. | [link](https://ddwiki.reso.org/display/DDW20/OtherCountry+Field) |
| `OtherCountyOrParish` | String List, Single |  | CountyOrParish |  |  | The other county or parish in which the contact is addressed. | [link](https://ddwiki.reso.org/display/DDW20/OtherCountyOrParish+Field) |
| `OtherPhoneType` | String List, Single |  | [OtherPhoneType](#otherphonetype) |  |  | The type of "other" phone that does not already exist in the given phone fields or if a second of any type of phone field is needed (i.e., HomePhone2, BrothersPhone, etc.). | [link](https://ddwiki.reso.org/display/DDW20/OtherPhoneType+Field) |
| `OtherPostalCode` | String |  |  |  |  | The other postal code of the contact. | [link](https://ddwiki.reso.org/display/DDW20/OtherPostalCode+Field) |
| `OtherPostalCodePlus4` | String |  |  |  |  | The other four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/OtherPostalCodePlus4+Field) |
| `OtherStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) |  |  | The other state or province in which the contact is addressed. | [link](https://ddwiki.reso.org/display/DDW20/OtherStateOrProvince+Field) |
| `OwnerMember` | Resource |  |  |  |  | The member who owns the contact's record. | [link](https://ddwiki.reso.org/display/DDW20/OwnerMember+Field) |
| `OwnerMemberID` | String |  |  | 1% | 1% | The local, well-known identifier for the member in charge of the contact. | [link](https://ddwiki.reso.org/display/DDW20/OwnerMemberID+Field) |
| `OwnerMemberKey` | String |  |  |  |  | A system-unique identifier for the member that owns the contact record (References Member.MemberKey). | [link](https://ddwiki.reso.org/display/DDW20/OwnerMemberKey+Field) |
| `Pager` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/Pager+Field) |
| `PhoneTTYTDD` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/PhoneTTYTDD+Field) |
| `PreferredAddress` | String List, Single |  | [PreferredAddress](#preferredaddress) |  |  | A list of the address options (i.e., Home, Work and Other) used to determine the address preferred by the client. | [link](https://ddwiki.reso.org/display/DDW20/PreferredAddress+Field) |
| `PreferredPhone` | String List, Single |  | [PreferredPhone](#preferredphone) |  |  | The phone number that the contact prefers to be contacted at. | [link](https://ddwiki.reso.org/display/DDW20/PreferredPhone+Field) |
| `ReferredBy` | String |  |  |  |  | The name of the person who referred the contact. | [link](https://ddwiki.reso.org/display/DDW20/ReferredBy+Field) |
| `ReverseProspectingEnabledYN` | Boolean |  |  |  |  | Reverse prospecting, a system that allows listing agents to see the agent/member whose client has a search criteria that found the agent's listing, has been enabled for the given client's saved search… | [link](https://ddwiki.reso.org/display/DDW20/ReverseProspectingEnabledYN+Field) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) |  |  | A list of types of sites or social media that the contact Uniform Resource Locator (URL) or ID is referring to (e.g., website, blog, Facebook, Twitter, LinkedIn, Instagram). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135521) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the contact's record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135527) |
| `SourceSystemContactKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemContactKey+Field) |
| `SourceSystemID` | String |  |  |  |  | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135539) |
| `SourceSystemName` | String |  |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135545) |
| `SpousePartnerName` | String |  |  |  |  | The contact's spouse or partner. | [link](https://ddwiki.reso.org/display/DDW20/SpousePartnerName+Field) |
| `TollFreePhone` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TollFreePhone+Field) |
| `VoiceMail` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/VoiceMail+Field) |
| `VoiceMailExt` | String |  |  |  |  | The extension of the given phone number (if applicable). | [link](https://ddwiki.reso.org/display/DDW20/VoiceMailExt+Field) |
| `WorkAddress1` | String |  |  |  |  | The street number, direction, name and suffix of the contact's work. | [link](https://ddwiki.reso.org/display/DDW20/WorkAddress1+Field) |
| `WorkAddress2` | String |  |  |  |  | The unit/suite number of the contact's work. | [link](https://ddwiki.reso.org/display/DDW20/WorkAddress2+Field) |
| `WorkCarrierRoute` | String |  |  |  |  | The group of addresses to which the U.S. | [link](https://ddwiki.reso.org/display/DDW20/WorkCarrierRoute+Field) |
| `WorkCity` | String |  |  |  |  | The city of the contact's work. | [link](https://ddwiki.reso.org/display/DDW20/WorkCity+Field) |
| `WorkCountry` | String List, Single |  | [Country](#country) |  |  | The country abbreviation in a postal address. | [link](https://ddwiki.reso.org/display/DDW20/WorkCountry+Field) |
| `WorkCountyOrParish` | String List, Single |  | CountyOrParish |  |  | The county or parish in which the contact's work is addressed. | [link](https://ddwiki.reso.org/display/DDW20/WorkCountyOrParish+Field) |
| `WorkPostalCode` | String |  |  |  |  | The postal code of the contact's work. | [link](https://ddwiki.reso.org/display/DDW20/WorkPostalCode+Field) |
| `WorkPostalCodePlus4` | String |  |  |  |  | The four-digit extension of a U.S. | [link](https://ddwiki.reso.org/display/DDW20/WorkPostalCodePlus4+Field) |
| `WorkStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) |  |  | The state or province in which the contact's work is addressed. | [link](https://ddwiki.reso.org/display/DDW20/WorkStateOrProvince+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>Anniversary</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Aniversario
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>AssistantEmail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Email de Asistente
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>AssistantName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Asistente
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>AssistantPhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Asistente
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>AssistantPhoneExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Teléfono de Asistente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 17 2016

</details>

<details><summary><code>Birthdate</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Fecha de Nacimiento
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** NOV 09 2016

</details>

<details><summary><code>Children</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Hijos
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>Company</code></summary>

  - **BEDES:** Company Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Compañía
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ContactKey</code></summary>

  - **BEDES:** Subaddress Type = "Key"Contact ID = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Contacto
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ContactLoginId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Ingreso de Contacto
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>ContactStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Contacto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 02 2018

</details>

<details><summary><code>ContactType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Contacto
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2016

</details>

<details><summary><code>ContactsOtherPhone</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ContactsSocialMedia</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Email</code></summary>

  - **BEDES:** Priority = "Primary"Email Address = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Email
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>Email2</code></summary>

  - **BEDES:** Priority = "Secondary"Email Address = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Email 2
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>Email3</code></summary>

  - **BEDES:** Priority = "Tertiary"Email Address = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Email 3
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>FirstName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JAN 23 2019

</details>

<details><summary><code>FullName</code></summary>

  - **BEDES:** Full Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Completo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JAN 23 2019

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022

</details>

<details><summary><code>HomeAddress1</code></summary>

  - **BEDES:** Address Label = "Home"Address Line 1 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Hogar 1
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomeAddress2</code></summary>

  - **BEDES:** Address Label = "Home"Address Line 2 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Hogar 2
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomeCarrierRoute</code></summary>

  - **BEDES:** Address Label = "Home"Street Name Post Type = "Route"ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ruta Transportista Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomeCity</code></summary>

  - **BEDES:** Address Label = "Home"City = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomeCountry</code></summary>

  - **BEDES:** Address Label = "Home"Country Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** País Hogar
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 11 2016

</details>

<details><summary><code>HomeFax</code></summary>

  - **BEDES:** Address Label = "Home"Telephone Number Label = "Fax"Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Fax Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomePhone</code></summary>

  - **BEDES:** Address Label = "Home"Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomePostalCodePlus4</code></summary>

  - **BEDES:** Address Label = "Home"ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más 4 Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>HomeStateOrProvince</code></summary>

  - **BEDES:** Address Label = "Home"State = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Estado o Provincia Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>JobTitle</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Cargo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JAN 23 2019

</details>

<details><summary><code>Language</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Idioma
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 15 2016

</details>

<details><summary><code>LeadSource</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Fuente de Cliente Potencial
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** AUG 23 2016
  - **Added in Version:** 1.6

</details>

<details><summary><code>Media</code></summary>

  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022

</details>

<details><summary><code>MiddleName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Segundo Nombre
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JAN 23 2019

</details>

<details><summary><code>MobilePhone</code></summary>

  - **BEDES:** Telephone Number Label = "Mobile" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Móvil
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015

</details>

<details><summary><code>NamePrefix</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Prefijo Nombre
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>NameSuffix</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Sufijo Nombre
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>Nickname</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Apodo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JAN 23 2019

</details>

<details><summary><code>Notes</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Notas
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** FEB 21 2013

</details>

<details><summary><code>OfficePhone</code></summary>

  - **BEDES:** Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Despacho
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OfficePhoneExt</code></summary>

  - **BEDES:** Telephone Extension = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Extensión Telefónica de Despacho
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 17 2016

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022

</details>

<details><summary><code>OriginatingSystemContactKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Contacto Sistema de Origen
  - **Status Change Date:** FEB 18 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OtherAddress1</code></summary>

  - **BEDES:** Address Label = "Other"Address Line 1 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otra Dirección1
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OtherAddress2</code></summary>

  - **BEDES:** Address Label = "Other"Address Line 2 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otra Dirección2
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OtherCity</code></summary>

  - **BEDES:** Address Label = "Other"City = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otra Ciudad
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OtherCountry</code></summary>

  - **BEDES:** Address Label = "Other"Country Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otro País
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 11 2016

</details>

<details><summary><code>OtherCountyOrParish</code></summary>

  - **BEDES:** Address Label = "Other"County = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otro Condado o Distrito
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** AUG 09 2013

</details>

<details><summary><code>OtherPhoneType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Otro Tipo de Teléfono
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** APR 11 2022

</details>

<details><summary><code>OtherPostalCode</code></summary>

  - **BEDES:** Address Label = "Other"ZIP Code = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otro Código Postal
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OtherPostalCodePlus4</code></summary>

  - **BEDES:** Address Label = "Other"ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otro Código Postal Más4
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>OtherStateOrProvince</code></summary>

  - **BEDES:** Address Label = "Other"State = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Otro Estado o Provincia
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>OwnerMember</code></summary>

  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022

</details>

<details><summary><code>OwnerMemberID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Miembro Propietario
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>OwnerMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro Propietario
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>PreferredAddress</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Dirección Preferida
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 02 2018

</details>

<details><summary><code>PreferredPhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Preferido
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 02 2018

</details>

<details><summary><code>ReferredBy</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Referido por
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** OCT 18 2014

</details>

<details><summary><code>ReverseProspectingEnabledYN</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 30 2019
  - **Revision Date:** APR 30 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Redes Sociales
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** APR 11 2022

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022

</details>

<details><summary><code>SourceSystemContactKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Contacto Sistema Fuente
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

<details><summary><code>TollFreePhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Gratuito
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>VoiceMail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Buzón de Voz
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>VoiceMailExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Buzón de Voz
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 17 2016

</details>

<details><summary><code>WorkAddress1</code></summary>

  - **BEDES:** Address Label = "Work"Address Line 1 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Lugar de Trabajo 1
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>WorkAddress2</code></summary>

  - **BEDES:** Address Label = "Work"Address Line 2 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Lugar de Trabajo 2
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>WorkCarrierRoute</code></summary>

  - **BEDES:** Address Label = "Work"Street Name Post Type = "Route"ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ruta Transportista Lugar de Trabajo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>WorkCity</code></summary>

  - **BEDES:** Address Label = "Work"City = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad de Lugar de Trabajo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>WorkCountry</code></summary>

  - **BEDES:** Address Label = "Work"Country Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** País de Lugar de Trabajo
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JAN 11 2016

</details>

<details><summary><code>WorkCountyOrParish</code></summary>

  - **BEDES:** Address Label = "Work"County = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Condado o Distrito de Lugar de Trabajo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** AUG 09 2013

</details>

<details><summary><code>WorkPostalCodePlus4</code></summary>

  - **BEDES:** Address Label = "Work"ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más 4 de Lugar de Trabajo
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** DEC 12 2012

</details>

<details><summary><code>WorkStateOrProvince</code></summary>

  - **BEDES:** Address Label = "Work"State = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Estado o Provincia de Hogar
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** AUG 12 2015

</details>

## Lookups

### ContactStatus

| Value | Definition |
|---|---|
| `Active` | The contact is active. |
| `Deleted` | The contact has been deleted. |
| `Inactive` | The contact is no longer active. |
| `On Vacation` | The contact is on vacation. |

### ContactType

| Value | Definition |
|---|---|
| `Business` | The contact is a business relation. |
| `Buyer` | The contact is the owner or principal who is purchasing the property in the transaction. |
| `Buyer Attorney` | The contact supports the buyer's legal obligations of the transaction |
| `Family` | The contact is a family member. |
| `Financial Planner` | The contact represents the client's financial interests |
| `Friend` | The contact is a personal friend. |
| `Home Improvement Specialist` | The contact works on improvements and maintenance to the property in the transaction. |
| `Home Inspector` | The contact supports the property inspection obligations of the transaction. |
| `Home Security Provider` | The contact provides and manages home security services to the property in the transaction. |
| `Home Warranty Representative` | The contact provides home warranty services and products to the transaction. |
| `Insurance Representative` | The contact supports the insurance obligations of the transaction. |
| `Landlord` | The contact is the owner or principal who is renting or leasing out the property in the transaction. |
| `Lead` | The lead is a contact that may be a potential buyer or seller to the member. |
| `Loan Officer` | The lender or other role that supports the mortgage obligations of the transaction. |
| `Moving/Storage` | Provides moving or storage services to the transaction. |
| `Other` | Any different type of role than what is explicitly provided as an option. |
| `Prospect` | The contact is a prospective client. |
| `Ready to Buy` | The contact is a client who is ready to start a transaction. |
| `Seller` | The owner or principal who is selling the property in the transaction. |
| `Seller Attorney` | The contact is a lead that may be a potential buyer or seller to the member. |
| `Tenant` | The contact is the prospective renter or lessor of the property in the transaction. |
| `Title Representative` | The contact supports the title and escrow obligations of the transaction. |

### Country

| Value | Definition |
|---|---|
| `AD` | Andorra is the country in which the individual, entity or property is located. |
| `AE` | United Arab Emirates is the country in which the individual, entity or property is located. |
| `AF` | Afghanistan is the country in which the individual, entity or property is located. |
| `AG` | Antigua Barbuda is the country in which the individual, entity or property is located. |
| `AI` | Anguilla is the country in which the individual, entity or property is located. |
| `AL` | Albania is the country in which the individual, entity or property is located. |
| `AM` | Armenia is the country in which the individual, entity or property is located. |
| `AN` | Netherlands Antilles is the country in which the individual, entity or property is located. |
| `AO` | Angola is the country in which the individual, entity or property is located. |
| `AQ` | Antarctica is the country in which the individual, entity or property is located. |
| `AR` | Argentina is the country in which the individual, entity or property is located. |
| `AS` | American Samoa is the country in which the individual, entity or property is located. |
| `AT` | Austria is the country in which the individual, entity or property is located. |
| `AU` | Australia is the country in which the individual, entity or property is located. |
| `AW` | Aruba is the country in which the individual, entity or property is located. |
| `AX` | Aland Islands is the country in which the individual, entity or property is located. |
| `AZ` | Azerbaijan is the country in which the individual, entity or property is located. |
| `BA` | Bosnia Herzegovina is the country in which the individual, entity or property is located. |
| `BB` | Barbados is the country in which the individual, entity or property is located. |
| `BD` | Bangladesh is the country in which the individual, entity or property is located. |
| `BE` | Belgium is the country in which the individual, entity or property is located. |
| `BF` | Burkina Faso is the country in which the individual, entity or property is located. |
| `BG` | Bulgaria is the country in which the individual, entity or property is located. |
| `BH` | Bahrain is the country in which the individual, entity or property is located. |
| `BI` | Burundi is the country in which the individual, entity or property is located. |
| `BJ` | Benin is the country in which the individual, entity or property is located. |
| `BL` | Saint Barthelemy is the country in which the individual, entity or property is located. |
| `BM` | Bermuda is the country in which the individual, entity or property is located. |
| `BN` | Brunei Darussalam is the country in which the individual, entity or property is located. |
| `BO` | Bolivia is the country in which the individual, entity or property is located. |
| `BR` | Brazil is the country in which the individual, entity or property is located. |
| `BS` | Bahamas is the country in which the individual, entity or property is located. |
| `BT` | Bhutan is the country in which the individual, entity or property is located. |
| `BV` | Bouvet Island is the country in which the individual, entity or property is located. |
| `BW` | Botswana is the country in which the individual, entity or property is located. |
| `BY` | Belarus is the country in which the individual, entity or property is located. |
| `BZ` | Belize is the country in which the individual, entity or property is located. |
| `CA` | Canada is the country in which the individual, entity or property is located. |
| `CC` | Cocos (Keeling) Islands is the country in which the individual, entity or property is located. |
| `CD` | Congo Democratic Republic is the country in which the individual, entity or property is located. |
| `CF` | Central African Republic is the country in which the individual, entity or property is located. |
| `CG` | Congo is the country in which the individual, entity or property is located. |
| `CH` | Switzerland is the country in which the individual, entity or property is located. |
| `CI` | Cote d'Ivoire is the country in which the individual, entity or property is located. |
| `CK` | Cook Islands is the country in which the individual, entity or property is located. |
| `CL` | Chile is the country in which the individual, entity or property is located. |
| `CM` | Cameroon is the country in which the individual, entity or property is located. |
| `CN` | China is the country in which the individual, entity or property is located. |
| `CO` | Colombia is the country in which the individual, entity or property is located. |
| `CR` | Costa Rica is the country in which the individual, entity or property is located. |
| `CU` | Cuba is the country in which the individual, entity or property is located. |
| `CV` | Cabo Verde is the country in which the individual, entity or property is located. |
| `CX` | Christmas Island is the country in which the individual, entity or property is located. |
| `CY` | Cyprus is the country in which the individual, entity or property is located. |
| `CZ` | Czechia is the country in which the individual, entity or property is located. |
| `DE` | Germany is the country in which the individual, entity or property is located. |
| `DJ` | Djibouti is the country in which the individual, entity or property is located. |
| `DK` | Denmark is the country in which the individual, entity or property is located. |
| `DM` | Dominica is the country in which the individual, entity or property is located. |
| `DO` | Dominican Republic is the country in which the individual, entity or property is located. |
| `DZ` | Algeria is the country in which the individual, entity or property is located. |
| `EC` | Ecuador is the country in which the individual, entity or property is located. |
| `EE` | Estonia is the country in which the individual, entity or property is located. |
| `EG` | Egypt is the country in which the individual, entity or property is located. |
| `EH` | Western Sahara is the country in which the individual, entity or property is located. |
| `ER` | Eritrea is the country in which the individual, entity or property is located. |
| `ES` | Spain is the country in which the individual, entity or property is located. |
| `ET` | Ethiopia is the country in which the individual, entity or property is located. |
| `FI` | Finland is the country in which the individual, entity or property is located. |
| `FJ` | Fiji is the country in which the individual, entity or property is located. |
| `FK` | Falkland Islands is the country in which the individual, entity or property is located. |
| `FM` | Micronesia is the country in which the individual, entity or property is located. |
| `FO` | Faroe Islands is the country in which the individual, entity or property is located. |
| `FR` | France is the country in which the individual, entity or property is located. |
| `GA` | Gabon is the country in which the individual, entity or property is located. |
| `GB` | United Kingdom is the country in which the individual, entity or property is located. |
| `GD` | Grenada is the country in which the individual, entity or property is located. |
| `GE` | Georgia is the country in which the individual, entity or property is located. |
| `GF` | French Guiana is the country in which the individual, entity or property is located. |
| `GG` | Guernsey is the country in which the individual, entity or property is located. |
| `GH` | Ghana is the country in which the individual, entity or property is located. |
| `GI` | Gibraltar is the country in which the individual, entity or property is located. |
| `GL` | Greenland is the country in which the individual, entity or property is located. |
| `GM` | Gambia is the country in which the individual, entity or property is located. |
| `GN` | Guinea is the country in which the individual, entity or property is located. |
| `GP` | Guadeloupe is the country in which the individual, entity or property is located. |
| `GQ` | Equatorial Guinea is the country in which the individual, entity or property is located. |
| `GR` | Greece is the country in which the individual, entity or property is located. |
| `GS` | South Georgia is the country in which the individual, entity or property is located. |
| `GT` | Guatemala is the country in which the individual, entity or property is located. |
| `GU` | Guam is the country in which the individual, entity or property is located. |
| `GW` | Guinea-Bissau is the country in which the individual, entity or property is located. |
| `GY` | Guyana is the country in which the individual, entity or property is located. |
| `HK` | Hong Kong is the country in which the individual, entity or property is located. |
| `HM` | Heard And McDonald Islands is the country in which the individual, entity or property is located. |
| `HN` | Honduras is the country in which the individual, entity or property is located. |
| `HR` | Croatia is the country in which the individual, entity or property is located. |
| `HT` | Haiti is the country in which the individual, entity or property is located. |
| `HU` | Hungary is the country in which the individual, entity or property is located. |
| `ID` | Indonesia is the country in which the individual, entity or property is located. |
| `IE` | Ireland is the country in which the individual, entity or property is located. |
| `IL` | Israel is the country in which the individual, entity or property is located. |
| `IM` | Isle Of Man is the country in which the individual, entity or property is located. |
| `IN` | India is the country in which the individual, entity or property is located. |
| `IO` | British Indian Ocean Territory is the country in which the individual, entity or property is located. |
| `IQ` | Iraq is the country in which the individual, entity or property is located. |
| `IR` | Iran is the country in which the individual, entity or property is located. |
| `IS` | Iceland is the country in which the individual, entity or property is located. |
| `IT` | Italy is the country in which the individual, entity or property is located. |
| `JE` | Jersey is the country in which the individual, entity or property is located. |
| `JM` | Jamaica is the country in which the individual, entity or property is located. |
| `JO` | Jordan is the country in which the individual, entity or property is located. |
| `JP` | Japan is the country in which the individual, entity or property is located. |
| `KE` | Kenya is the country in which the individual, entity or property is located. |
| `KG` | Kyrgyzstan is the country in which the individual, entity or property is located. |
| `KH` | Cambodia is the country in which the individual, entity or property is located. |
| `KI` | Kiribati is the country in which the individual, entity or property is located. |
| `KM` | Comoros is the country in which the individual, entity or property is located. |
| `KN` | Saint Kitts And Nevis is the country in which the individual, entity or property is located. |
| `KP` | North Korea, officially named the Democratic People's Republic of Korea, is the country in which the individual, entity or property is located. |
| `KR` | South Korea, officially named the Republic of Korea, is the country in which the individual, entity or property is located. |
| `KW` | Kuwait is the country in which the individual, entity or property is located. |
| `KY` | Cayman Islands is the country in which the individual, entity or property is located. |
| `KZ` | Kazakhstan is the country in which the individual, entity or property is located. |
| `LA` | Lao is the country in which the individual, entity or property is located. |
| `LB` | Lebanon is the country in which the individual, entity or property is located. |
| `LC` | Saint Lucia is the country in which the individual, entity or property is located. |
| `LI` | Liechtenstein is the country in which the individual, entity or property is located. |
| `LK` | Sri Lanka is the country in which the individual, entity or property is located. |
| `LR` | Liberia is the country in which the individual, entity or property is located. |
| `LS` | Lesotho is the country in which the individual, entity or property is located. |
| `LT` | Lithuania is the country in which the individual, entity or property is located. |
| `LU` | Luxembourg is the country in which the individual, entity or property is located. |
| `LV` | Latvia is the country in which the individual, entity or property is located. |
| `LY` | Libyan Arab Jamahiriya is the country in which the individual, entity or property is located. |
| `MA` | Morocco is the country in which the individual, entity or property is located. |
| `MC` | Monaco is the country in which the individual, entity or property is located. |
| `MD` | Moldova is the country in which the individual, entity or property is located. |
| `ME` | Montenegro is the country in which the individual, entity or property is located. |
| `MF` | Saint Martin is the country in which the individual, entity or property is located. |
| `MG` | Madagascar is the country in which the individual, entity or property is located. |
| `MH` | Marshall Islands is the country in which the individual, entity or property is located. |
| `MK` | Macedonia is the country in which the individual, entity or property is located. |
| `ML` | Mali is the country in which the individual, entity or property is located. |
| `MM` | Myanmar is the country in which the individual, entity or property is located. |
| `MN` | Mongolia is the country in which the individual, entity or property is located. |
| `MO` | Macao is the country in which the individual, entity or property is located. |
| `MP` | Northern Mariana Islands is the country in which the individual, entity or property is located. |
| `MQ` | Martinique is the country in which the individual, entity or property is located. |
| `MR` | Mauritania is the country in which the individual, entity or property is located. |
| `MS` | Montserrat is the country in which the individual, entity or property is located. |
| `MT` | Malta is the country in which the individual, entity or property is located. |
| `MU` | Mauritius is the country in which the individual, entity or property is located. |
| `MV` | Maldives is the country in which the individual, entity or property is located. |
| `MW` | Malawi is the country in which the individual, entity or property is located. |
| `MX` | Mexico is the country in which the individual, entity or property is located. |
| `MY` | Malaysia is the country in which the individual, entity or property is located. |
| `MZ` | Mozambique is the country in which the individual, entity or property is located. |
| `NA` | Namibia is the country in which the individual, entity or property is located. |
| `NC` | New Caledonia is the country in which the individual, entity or property is located. |
| `NE` | Niger is the country in which the individual, entity or property is located. |
| `NF` | Norfolk Island is the country in which the individual, entity or property is located. |
| `NG` | Nigeria is the country in which the individual, entity or property is located. |
| `NI` | Nicaragua is the country in which the individual, entity or property is located. |
| `NL` | Netherlands is the country in which the individual, entity or property is located. |
| `NP` | Nepal is the country in which the individual, entity or property is located. |
| `NR` | Nauru is the country in which the individual, entity or property is located. |
| `NU` | Niue is the country in which the individual, entity or property is located. |
| `NZ` | New Zealand is the country in which the individual, entity or property is located. |
| `OM` | Oman is the country in which the individual, entity or property is located. |
| `OT` | The country in which the individual, entity or property is located is something other than what is covered by ISO standard 3166 |
| `PA` | Panama is the country in which the individual, entity or property is located. |
| `PE` | Peru is the country in which the individual, entity or property is located. |
| `PF` | French Polynesia is the country in which the individual, entity or property is located. |
| `PG` | Papua New Guinea is the country in which the individual, entity or property is located. |
| `PH` | Philippines is the country in which the individual, entity or property is located. |
| `PK` | Pakistan is the country in which the individual, entity or property is located. |
| `PL` | Poland is the country in which the individual, entity or property is located. |
| `PM` | Saint Pierre And Miquelon is the country in which the individual, entity or property is located. |
| `PN` | Pitcairn is the country in which the individual, entity or property is located. |
| `PR` | Puerto Rico is the country in which the individual, entity or property is located. |
| `PS` | Palestinian Territory is the country in which the individual, entity or property is located. |
| `PT` | Portugal is the country in which the individual, entity or property is located. |
| `PW` | Palau is the country in which the individual, entity or property is located. |
| `PY` | Paraguay is the country in which the individual, entity or property is located. |
| `QA` | Qatar is the country in which the individual, entity or property is located. |
| `RE` | Reunion is the country in which the individual, entity or property is located. |
| `RO` | Romania is the country in which the individual, entity or property is located. |
| `RS` | Serbia is the country in which the individual, entity or property is located. |
| `RU` | Russian Federation is the country in which the individual, entity or property is located. |
| `RW` | Rwanda is the country in which the individual, entity or property is located. |
| `SA` | Saudi Arabia is the country in which the individual, entity or property is located. |
| `SB` | Solomon Islands is the country in which the individual, entity or property is located. |
| `SC` | Seychelles is the country in which the individual, entity or property is located. |
| `SD` | Sudan is the country in which the individual, entity or property is located. |
| `SE` | Sweden is the country in which the individual, entity or property is located. |
| `SG` | Singapore is the country in which the individual, entity or property is located. |
| `SH` | Saint Helena is the country in which the individual, entity or property is located. |
| `SI` | Slovenia is the country in which the individual, entity or property is located. |
| `SJ` | Svalbard - Jan Mayen is the country in which the individual, entity or property is located. |
| `SK` | Slovakia is the country in which the individual, entity or property is located. |
| `SL` | Sierra Leone is the country in which the individual, entity or property is located. |
| `SM` | San Marino is the country in which the individual, entity or property is located. |
| `SN` | Senegal is the country in which the individual, entity or property is located. |
| `SO` | Somalia is the country in which the individual, entity or property is located. |
| `SR` | Suriname is the country in which the individual, entity or property is located. |
| `ST` | Sao Tome And Principe is the country in which the individual, entity or property is located. |
| `SV` | El Salvador is the country in which the individual, entity or property is located. |
| `SY` | Syrian Arab Republic is the country in which the individual, entity or property is located. |
| `SZ` | Swaziland is the country in which the individual, entity or property is located. |
| `TC` | Turks - Caicos Islands is the country in which the individual, entity or property is located. |
| `TD` | Chad is the country in which the individual, entity or property is located. |
| `TF` | French Southern Territories is the country in which the individual, entity or property is located. |
| `TG` | Togo is the country in which the individual, entity or property is located. |
| `TH` | Thailand is the country in which the individual, entity or property is located. |
| `TJ` | Tajikistan is the country in which the individual, entity or property is located. |
| `TK` | Tokelau is the country in which the individual, entity or property is located. |
| `TL` | Timor-Leste is the country in which the individual, entity or property is located. |
| `TM` | Turkmenistan is the country in which the individual, entity or property is located. |
| `TN` | Tunisia is the country in which the individual, entity or property is located. |
| `TO` | Tonga is the country in which the individual, entity or property is located. |
| `TR` | Türkiye is the country in which the individual, entity or property is located. |
| `TT` | Trinidad - Tobago is the country in which the individual, entity or property is located. |
| `TV` | Tuvalu is the country in which the individual, entity or property is located. |
| `TW` | Taiwan is the country in which the individual, entity or property is located. |
| `TZ` | Tanzania is the country in which the individual, entity or property is located. |
| `UA` | Ukraine is the country in which the individual, entity or property is located. |
| `UG` | Uganda is the country in which the individual, entity or property is located. |
| `UM` | United States Minor Islands is the country in which the individual, entity or property is located. |
| `US` | United States is the country in which the individual, entity or property is located. |
| `UY` | Uruguay is the country in which the individual, entity or property is located. |
| `UZ` | Uzbekistan is the country in which the individual, entity or property is located. |
| `VA` | Holy See (Vatican City) is the country in which the individual, entity or property is located. |
| `VC` | Saint Vincent - Grenadines is the country in which the individual, entity or property is located. |
| `VE` | Venezuela is the country in which the individual, entity or property is located. |
| `VG` | Virgin Islands British is the country in which the individual, entity or property is located. |
| `VI` | Virgin Islands U.S. |
| `VN` | Viet Nam is the country in which the individual, entity or property is located. |
| `VU` | Vanuatu is the country in which the individual, entity or property is located. |
| `WF` | Wallis And Futuna is the country in which the individual, entity or property is located. |
| `WS` | Samoa is the country in which the individual, entity or property is located. |
| `YE` | Yemen is the country in which the individual, entity or property is located. |
| `YT` | Mayotte is the country in which the individual, entity or property is located. |
| `ZA` | South Africa is the country in which the individual, entity or property is located. |
| `ZM` | Zambia is the country in which the individual, entity or property is located. |
| `ZW` | Zimbabwe is the country in which the individual, entity or property is located. |

### Languages

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

### OtherPhoneType

| Value | Definition |
|---|---|
| `Direct` | This is the contact's direct number. |
| `Fax` | This is the contact's fax. |
| `First` | This is the contact's first preferred phone. |
| `Home` | This is the contact's home phone. |
| `Mobile` | This is the contact's mobile phone. |
| `Modem` | This is the contact's modem. |
| `Office` | This is the contact's office phone. |
| `Pager` | This is the contact's pager. |
| `Preferred` | This is the contact's preferred phone. |
| `Second` | This is the contact's second preferred phone. |
| `SMS` | This is the contact's SMS/text number. |
| `Third` | This is the contact's third preferred phone. |
| `Toll Free` | This is the contact's toll-free number. |
| `Voicemail` | This is the contact's voicemail. |

### PreferredAddress

| Value | Definition |
|---|---|
| `Home` | The contact prefers the use of their home address. |
| `Other` | The contact prefers the use of their other address. |
| `Work` | The contact prefers the use of their work address. |

### PreferredPhone

| Value | Definition |
|---|---|
| `Direct` | The contact prefers the use of their direct phone. |
| `Home` | The contact prefers the use of their home phone. |
| `Mobile` | The contact prefers the use of their mobile phone. |
| `Office` | The contact prefers the use of their office phone. |
| `Other` | The contact prefers the use of their other phone. |
| `Toll Free` | The contact prefers the use of their toll-free phone. |
| `Voicemail` | The contact prefers the use of their voicemail phone. |

### SocialMediaType

| Value | Definition |
|---|---|
| `Blog` | Information pertaining to the blog of the member/office/contact. |
| `Digg` | Information pertaining to the Digg account of the member/office/contact. |
| `Facebook` | Information pertaining to the Facebook account of the member/office/contact. |
| `Facebook Messenger` | Information pertaining to the Facebook Messenger contact information of the member/office/contact. |
| `GooglePlus` | Information pertaining to the GooglePlus account of the member/office/contact. |
| `iMessage` | Information pertaining to the iMessage contact information of the member/office/contact. |
| `Instagram` | Information pertaining to the Instagram account of the member/office/contact. |
| `LinkedIn` | Information pertaining to the LinkedIn account of the member/office/contact. |
| `Pinterest` | Information pertaining to the Pinterest account of the member/office/contact. |
| `Reddit` | Information pertaining to the Reddit account of the member/office/contact. |
| `Slack` | Information pertaining to the Slack account of the member/office/contact. |
| `Snapchat` | Information pertaining to the Snapchat account of the member/office/contact. |
| `StumbleUpon` | Information pertaining to the StumbleUpon account of the member/office/contact. |
| `Tumblr` | Information pertaining to the Tumblr account of the member/office/contact. |
| `Twitter` | Information pertaining to the X (formerly Twitter) account of the member/office/contact. |
| `Website` | Information pertaining to the website of the member/office/contact. |
| `YouTube` | Information pertaining to the YouTube account of the member/office/contact. |

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
