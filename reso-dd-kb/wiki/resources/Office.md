# Office

Roster of offices who are members of the MLS and/or association.

**RESO DD 2.0** — 73 fields · last revised 8/5/2024 · [dd.reso.org](https://dd.reso.org/DD2.0/Office/)

**Adoption** — weighted Org%: **43%** across 61 measured fields (median 29%, avg 43%).

## Groups

- **Other** — 73 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `BillingOfficeKey` | String |  |  | 0% | The office that will be billed (e.g., corporate headquarters). | [link](https://dd.reso.org/DD2.0/Office/BillingOfficeKey/) |
| `FranchiseAffiliation` | String |  |  | 5% | The name of the franchise to which the broker/office is contracted. | [link](https://dd.reso.org/DD2.0/Office/FranchiseAffiliation/) |
| `FranchiseNationalAssociationId` | String |  |  | 1% | The national association ID of the franchise (i.e., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Office/FranchiseNationalAssociationId/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/Office/HistoryTransactional/) |
| `IDXOfficeParticipationYN` | Boolean |  |  | 70% | Indicates whether or not the office/broker participates in IDX. | [link](https://dd.reso.org/DD2.0/Office/IDXOfficeParticipationYN/) |
| `MainOffice` | Resource |  |  | 0% | The main office for the Office record. | [link](https://dd.reso.org/DD2.0/Office/MainOffice/) |
| `MainOfficeKey` | String |  |  | 71% | The OfficeKey of the main office in a firm/company of offices. | [link](https://dd.reso.org/DD2.0/Office/MainOfficeKey/) |
| `MainOfficeMlsId` | String |  |  | 70% | The OfficeMlsId of the main office in a firm/company of offices. | [link](https://dd.reso.org/DD2.0/Office/MainOfficeMlsId/) |
| `Media` | Collection |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://dd.reso.org/DD2.0/Office/Media/) |
| `ModificationTimestamp` | Timestamp |  |  | 99% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/Office/ModificationTimestamp/) |
| `NumberOfBranches` | Number |  |  | 6% | The calculated value for the number of active branches. | [link](https://dd.reso.org/DD2.0/Office/NumberOfBranches/) |
| `NumberOfNonMemberSalespersons` | Number |  |  |  | The total number of active salespersons that are not a member of the national association. | [link](https://dd.reso.org/DD2.0/Office/NumberOfNonMemberSalespersons/) |
| `OfficeAOR` | String List, Single |  | AOR | 30% | The office's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Office/OfficeAOR/) |
| `OfficeAORMlsId` | String |  |  | 13% | The local, well-known identifier for the office's association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Office/OfficeAORMlsId/) |
| `OfficeAORkey` | String |  |  | 13% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Office/OfficeAORkey/) |
| `OfficeAddress1` | String |  |  | 98% | The first address line of the physical address of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeAddress1/) |
| `OfficeAddress2` | String |  |  | 85% | The unit/suite number of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeAddress2/) |
| `OfficeAlternateId` | String |  |  | 1% | An alternate ID with no specific use. | [link](https://dd.reso.org/DD2.0/Office/OfficeAlternateId/) |
| `OfficeAssociationComments` | String |  |  | 6% | Notes relating to the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeAssociationComments/) |
| `OfficeBio` | String |  |  | 7% | A text field containing biography information for the office record. | [link](https://dd.reso.org/DD2.0/Office/OfficeBio/) |
| `OfficeBranchType` | String List, Single |  | [OfficeBranchType](#officebranchtype) | 11% | The level of the office in a hierarchy (i.e., Main, Branch, Stand-Alone, etc.). | [link](https://dd.reso.org/DD2.0/Office/OfficeBranchType/) |
| `OfficeBroker` | Resource |  |  |  | The broker for the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeBroker/) |
| `OfficeBrokerKey` | String |  |  | 65% | The MemberKey of the responsible/owning broker. | [link](https://dd.reso.org/DD2.0/Office/OfficeBrokerKey/) |
| `OfficeBrokerMlsId` | String |  |  | 64% | The MemberMlsId of the broker of record for the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeBrokerMlsId/) |
| `OfficeBrokerNationalAssociationId` | String |  |  |  | The national association ID of the broker (i.e., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Office/OfficeBrokerNationalAssociationId/) |
| `OfficeCity` | String |  |  | 98% | The city of the physical address of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeCity/) |
| `OfficeCorporateLicense` | String |  |  | 72% | An independent license number is issued when an office/firm is a corporation. | [link](https://dd.reso.org/DD2.0/Office/OfficeCorporateLicense/) |
| `OfficeCountry` | String List, Single |  | [Country](#country) | 3% | The country of the physical address of the office (ISO country code). | [link](https://dd.reso.org/DD2.0/Office/OfficeCountry/) |
| `OfficeCountyOrParish` | String List, Single |  | CountyOrParish | 8% | The county or parish in which the offices is located. | [link](https://dd.reso.org/DD2.0/Office/OfficeCountyOrParish/) |
| `OfficeEmail` | String |  |  | 98% | The contact email address of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeEmail/) |
| `OfficeFax` | String |  |  | 92% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Office/OfficeFax/) |
| `OfficeKey` | String |  |  | 99% | A system-unique identifier for the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeKey/) |
| `OfficeMailAddress1` | String |  |  | 17% | The street number, direction, name and suffix of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailAddress1/) |
| `OfficeMailAddress2` | String |  |  | 6% | The unit/suite number of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailAddress2/) |
| `OfficeMailCareOf` | String |  |  | 11% | The care of (c/o) for the office's mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailCareOf/) |
| `OfficeMailCity` | String |  |  | 17% | The office's city for the mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailCity/) |
| `OfficeMailCountry` | String List, Single |  | [Country](#country) | 1% | The office's country code for the mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailCountry/) |
| `OfficeMailCountyOrParish` | String List, Single |  | CountyOrParish | 1% | The office's county of the mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailCountyOrParish/) |
| `OfficeMailPostalCode` | String |  |  | 17% | The postal code of the office's mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailPostalCode/) |
| `OfficeMailPostalCodePlus4` | String |  |  | 12% | The four-digit extension of the U.S. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailPostalCodePlus4/) |
| `OfficeMailStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 17% | The office's state or province of the mailing address. | [link](https://dd.reso.org/DD2.0/Office/OfficeMailStateOrProvince/) |
| `OfficeManager` | Resource |  |  |  | The office manager for the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeManager/) |
| `OfficeManagerKey` | String |  |  | 14% | The lead office manager for the given office. | [link](https://dd.reso.org/DD2.0/Office/OfficeManagerKey/) |
| `OfficeManagerMlsId` | String |  |  | 17% | The lead office manager for the given office. | [link](https://dd.reso.org/DD2.0/Office/OfficeManagerMlsId/) |
| `OfficeMlsId` | String |  |  | 97% | The local, well-known identifier for the office as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/Office/OfficeMlsId/) |
| `OfficeName` | String |  |  | 100% | The legal or DBA name of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficeName/) |
| `OfficeNationalAssociationId` | String |  |  | 81% | The national association ID of the office (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Office/OfficeNationalAssociationId/) |
| `OfficeNationalAssociationIdInsertDate` | Date |  |  |  | The date the office record was initially created in the national association's database (e.g., the date the record was added to NRDS in the U.S.). | [link](https://dd.reso.org/DD2.0/Office/OfficeNationalAssociationIdInsertDate/) |
| `OfficePhone` | String |  |  | 98% | The main contact phone number of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficePhone/) |
| `OfficePhoneExt` | String |  |  | 29% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/Office/OfficePhoneExt/) |
| `OfficePostalCode` | String |  |  | 98% | The postal code of the office. | [link](https://dd.reso.org/DD2.0/Office/OfficePostalCode/) |
| `OfficePostalCodePlus4` | String |  |  | 43% | The four-digit extension of the U.S. | [link](https://dd.reso.org/DD2.0/Office/OfficePostalCodePlus4/) |
| `OfficePreferredMedia` | String List, Single |  | [PreferredMedia](#preferredmedia) | 0% | The method the office prefers to receive media. | [link](https://dd.reso.org/DD2.0/Office/OfficePreferredMedia/) |
| `OfficePrimaryAorId` | String |  |  |  | The primary association of REALTORS® (AOR) associated with the member. | [link](https://dd.reso.org/DD2.0/Office/OfficePrimaryAorId/) |
| `OfficePrimaryStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 0% | The office's primary state or province. | [link](https://dd.reso.org/DD2.0/Office/OfficePrimaryStateOrProvince/) |
| `OfficeSocialMedia` | Collection |  |  |  | A collection of the types of social media fields available for this office. | [link](https://dd.reso.org/DD2.0/Office/OfficeSocialMedia/) |
| `OfficeStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 98% | The state or province in which the office is located. | [link](https://dd.reso.org/DD2.0/Office/OfficeStateOrProvince/) |
| `OfficeStatus` | String List, Single |  | [OfficeStatus](#officestatus) | 88% | The status of the office's record in the MLS or other organization. | [link](https://dd.reso.org/DD2.0/Office/OfficeStatus/) |
| `OfficeType` | String List, Single |  | [OfficeType](#officetype) | 76% | The type of business conducted by the office (e.g., Appraisal, MLS, Mortgage). | [link](https://dd.reso.org/DD2.0/Office/OfficeType/) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 73% | The date/time the roster (member or office) record was originally input into the source system. | [link](https://dd.reso.org/DD2.0/Office/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the Office record. | [link](https://dd.reso.org/DD2.0/Office/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  | 70% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/Office/OriginatingSystemID/) |
| `OriginatingSystemName` | String |  |  | 93% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/Office/OriginatingSystemName/) |
| `OriginatingSystemOfficeKey` | String |  |  | 89% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/Office/OriginatingSystemOfficeKey/) |
| `OtherPhone` | String |  |  | 5% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Office/OtherPhone/) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) | 1% | A collection of the types of social media fields available for the office. | [link](https://dd.reso.org/DD2.0/Office/SocialMediaType/) |
| `SourceSystem` | Resource |  |  |  | The source system of the Office record. | [link](https://dd.reso.org/DD2.0/Office/SourceSystem/) |
| `SourceSystemID` | String |  |  | 59% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/Office/SourceSystemID/) |
| `SourceSystemName` | String |  |  | 40% | The name of the immediate record provider. | [link](https://dd.reso.org/DD2.0/Office/SourceSystemName/) |
| `SourceSystemOfficeKey` | String |  |  | 58% | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/Office/SourceSystemOfficeKey/) |
| `SyndicateAgentOption` | String List, Single |  | SyndicateAgentOption | 1% | A list of options allowing the broker to pass the decision of syndication choice down to the listing agents (i.e., No Agent Choice, Allow Agent Choice, Restrict Agent Choice, etc.). | [link](https://dd.reso.org/DD2.0/Office/SyndicateAgentOption/) |
| `SyndicateTo` | String List, Multi |  | [SyndicateTo](#syndicateto) | 10% | The principal broker's choice on where they would like their listings syndicated (i.e., Zillow, Trulia, Homes.com, etc.). | [link](https://dd.reso.org/DD2.0/Office/SyndicateTo/) |
| `VirtualOfficeWebsiteYN` | Boolean |  |  |  | Indicates whether or not this is a Virtual Office Website (VOW). | [link](https://dd.reso.org/DD2.0/Office/VirtualOfficeWebsiteYN/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>BillingOfficeKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FranchiseAffiliation</code></summary>

  - **Status:** Active
  - **Spanish Name:** Afiliación de Franquicia
  - **French-Canadian Name:** Franchise/affiliation
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FranchiseNationalAssociationId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>IDXOfficeParticipationYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Participación en IDX SN
  - **French-Canadian Name:** Participation du bureau au système IDX O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MainOffice</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MainOfficeKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Despacho Principal
  - **French-Canadian Name:** Clé du bureau principal
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MainOfficeMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau principal
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Media</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **French-Canadian Name:** Heure et date de la modification
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfBranches</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>NumberOfNonMemberSalespersons</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAOR</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Company Name = [value]
  - **Status:** Active
  - **Spanish Name:** Despacho de AOR
  - **French-Canadian Name:** Chambre/association du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeAORMlsId</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Identifier = [value]
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho de AOR
  - **French-Canadian Name:** ID MLS de la chambre/association du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeAORkey</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Subaddress Type = "Key"Identifier = [value]
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho de AOR
  - **French-Canadian Name:** Clé de la chambre/association du bureau
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeAddress1</code></summary>

  - **BEDES:** Address Line 1 = [value]
  - **Status:** Active
  - **Spanish Name:** Dirección de Despacho1
  - **French-Canadian Name:** Adresse du bureau 1
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeAddress2</code></summary>

  - **BEDES:** Address Line 2 = [value]
  - **Status:** Active
  - **Spanish Name:** Dirección de Despacho2
  - **French-Canadian Name:** Adresse du bureau 2
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeAlternateId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationComments</code></summary>

  - **Status:** Active
  - **Spanish Name:** Comentarios de Asociación de Despacho
  - **French-Canadian Name:** Remarques de l’association sur le bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeBio</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/18/2023
  - **Revision Date:** 4/18/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeBranchType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Sucursal
  - **French-Canadian Name:** Type de bureau
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>OfficeBroker</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeBrokerKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Corredor de Despacho
  - **French-Canadian Name:** Clé du dirigeant du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeBrokerMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Corredor de Despacho
  - **French-Canadian Name:** ID MLS du dirigeant du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeBrokerNationalAssociationId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCity</code></summary>

  - **BEDES:** City = [value]
  - **Status:** Active
  - **Spanish Name:** Ciudad de Despacho
  - **French-Canadian Name:** Ville du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeCorporateLicense</code></summary>

  - **Status:** Active
  - **Spanish Name:** Licencia Corporativa de Despacho
  - **French-Canadian Name:** Licence de société du bureau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeCountry</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCountyOrParish</code></summary>

  - **BEDES:** County = [value]
  - **Status:** Active
  - **Spanish Name:** Condado o Distrito de Despacho
  - **French-Canadian Name:** Comté ou paroisse du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeEmail</code></summary>

  - **BEDES:** Email Address = [value]
  - **Status:** Active
  - **Spanish Name:** Email de Despacho
  - **French-Canadian Name:** Adresse courriel du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeFax</code></summary>

  - **BEDES:** Telephone Number Label = "Fax"Telephone Number = [value]
  - **Status:** Active
  - **Spanish Name:** Fax de Despacho
  - **French-Canadian Name:** Numéro de télécopieur du bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeKey</code></summary>

  - **BEDES:** Subaddress Type = "Key"Contact ID = [value]
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho
  - **French-Canadian Name:** Clé du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeMailAddress1</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 8/5/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailAddress2</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 8/5/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCareOf</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCity</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 8/5/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCountry</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCountyOrParish</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailPostalCode</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailPostalCodePlus4</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailStateOrProvince</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeManager</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeManagerKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Gerente de Despacho
  - **French-Canadian Name:** Clé du gestionnaire de bureau
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeManagerMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Gerente de Despacho
  - **French-Canadian Name:** ID MLS du gestionnaire de bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeName</code></summary>

  - **BEDES:** Company Name = [value]
  - **Status:** Active
  - **Spanish Name:** Nombre de Despacho
  - **French-Canadian Name:** Nom du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeNationalAssociationId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Asociación Nacional de Despacho
  - **French-Canadian Name:** ID de l’association nationale du bureau
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeNationalAssociationIdInsertDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePhone</code></summary>

  - **BEDES:** Telephone Number = [value]
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho
  - **French-Canadian Name:** Numéro de téléphone du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficePhoneExt</code></summary>

  - **BEDES:** Telephone Extension = [value]
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Despacho
  - **French-Canadian Name:** Poste téléphonique du bureau
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficePostalCode</code></summary>

  - **BEDES:** ZIP Code = [value]
  - **Status:** Active
  - **Spanish Name:** Código Postal de Despacho
  - **French-Canadian Name:** Code postal du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficePostalCodePlus4</code></summary>

  - **BEDES:** ZIP Plus 4 = [value]
  - **Status:** Active
  - **Spanish Name:** Código Postal Más 4 de Despacho
  - **French-Canadian Name:** Code postal du bureau +4
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficePreferredMedia</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePrimaryAorId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePrimaryStateOrProvince</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeSocialMedia</code></summary>

  - **Status:** Active
  - **French-Canadian Name:** Médias sociaux du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeStateOrProvince</code></summary>

  - **BEDES:** State = [value]
  - **Status:** Active
  - **Spanish Name:** Estado o Provincia de Despacho
  - **French-Canadian Name:** État ou province du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeStatus</code></summary>

  - **Status:** Active
  - **Spanish Name:** Estado de Despacho
  - **French-Canadian Name:** Statut du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OfficeType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Despacho
  - **French-Canadian Name:** Type de bureau
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **BEDES:** Date Status = "Created"Date = [value]
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **French-Canadian Name:** Date et heure de l’entrée originale
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema de Origen
  - **French-Canadian Name:** ID du système d’origine
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **French-Canadian Name:** Nom du système d’origine
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginatingSystemOfficeKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Despacho de Sistema de Origen
  - **French-Canadian Name:** Clé du système d’origine du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OtherPhone</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Redes Sociales
  - **French-Canadian Name:** Type de médias sociaux
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2020
  - **Revision Date:** 1/20/2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema Fuente
  - **French-Canadian Name:** ID du système source
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre Sistema Fuente
  - **French-Canadian Name:** Nom du système source
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemOfficeKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Despacho Sistema Fuente
  - **French-Canadian Name:** Clé du système source du bureau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SyndicateAgentOption</code></summary>

  - **Status:** Active
  - **Spanish Name:** Opción de Redifusión Agente
  - **French-Canadian Name:** Délégation du lieu d’affichage au courtier/agent
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SyndicateTo</code></summary>

  - **Status:** Active
  - **Spanish Name:** Redifundir a
  - **French-Canadian Name:** Afficher sur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>VirtualOfficeWebsiteYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

## Lookups

### Country

246 values · used by 12 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Country/)

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

### OfficeBranchType

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OfficeBranchType/)

| Value | Definition |
|---|---|
| `Branch` | This office is a branch office. |
| `Main` | This office is the broker's main office. |
| `Stand Alone` | This office is a stand-alone or single-office brokerage. |

### OfficeStatus

2 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OfficeStatus/)

| Value | Definition |
|---|---|
| `Active` | The member office's account is active. |
| `Inactive` | The member office's account is not active. |

### OfficeType

11 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OfficeType/)

| Value | Definition |
|---|---|
| `Affiliate` | The record in the office roster is an affiliate office. |
| `Appraiser` | The record in the office roster is an appraiser office. |
| `Association` | The record in the office roster is an association office. |
| `MLS` | The record in the office roster is an MLS office. |
| `MLS Only Branch` | The record in the office roster is a broker branch office who receives only MLS service. |
| `MLS Only Firm` | The record in the office roster is a broker firm office that receives only MLS service. |
| `MLS Only Office` | The record in the office roster is a broker office that receives only MLS service. |
| `Non Member/Vendor` | The record in the office roster is a nonmember/vendor office. |
| `Realtor Branch Office` | The record in the office roster is a REALTOR® branch office. |
| `Realtor Firm` | The record in the office roster is a REALTOR® firm office. |
| `Realtor Office` | The record in the office roster is a REALTOR® office. |

### PreferredMedia

3 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PreferredMedia/)

| Value | Definition |
|---|---|
| `Email` | Send media via email. |
| `Fax` | Send media via fax. |
| `Mail` | Send media via postal mail. |

### SocialMediaType

17 values · used by 7 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SocialMediaType/)

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

65 values · used by 19 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/StateOrProvince/)

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

### SyndicateTo

4 values · used by 3 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SyndicateTo/)

| Value | Definition |
|---|---|
| `Homes.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Homes.com. |
| `ListHub` | The broker, or member if permitted by the broker, is allowing their listings to be sent to ListHub.com. |
| `Realtor.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Realtor.com. |
| `Zillow/Trulia` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Zillow and Trulia. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
