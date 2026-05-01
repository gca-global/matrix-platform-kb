# Office

The Office resource describes a brokerage office. Offices employ Members and are referenced from Property via ListOfficeKey / CoListOfficeKey. Each office has identity, contact information, and a designated broker.

**Adoption** — weighted Org%: **43%** across 61 measured fields (median 29%, avg 43%).

## Groups

- **Other** — 73 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `BillingOfficeKey` | String |  |  |  | 0% | The office that will be billed (e.g., corporate headquarters). | [link](https://ddwiki.reso.org/display/DDW20/BillingOfficeKey+Field) |
| `FranchiseAffiliation` | String |  |  | 30% | 2% | The name of the franchise to which the broker/office is contracted. | [link](https://ddwiki.reso.org/display/DDW20/FranchiseAffiliation+Field) |
| `FranchiseNationalAssociationId` | String |  |  |  | 1% | The national association ID of the franchise (i.e., the NRDS number in the U.S.). | [link](https://ddwiki.reso.org/display/DDW20/FranchiseNationalAssociationID+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135098) |
| `IDXOfficeParticipationYN` | Boolean |  |  | 50% | 45% | Indicates whether or not the office/broker participates in IDX. | [link](https://ddwiki.reso.org/display/DDW20/IDXOfficeParticipationYN+Field) |
| `MainOffice` | Resource |  |  |  | 0% | The main office for the Office record. | [link](https://ddwiki.reso.org/display/DDW20/MainOffice+Field) |
| `MainOfficeKey` | String |  |  | 50% | 55% | The OfficeKey of the main office in a firm/company of offices. | [link](https://ddwiki.reso.org/display/DDW20/MainOfficeKey+Field) |
| `MainOfficeMlsId` | String |  |  | 50% | 55% | The OfficeMlsId of the main office in a firm/company of offices. | [link](https://ddwiki.reso.org/display/DDW20/MainOfficeMlsId+Field) |
| `Media` | Collection |  |  | 1% | 1% | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135126) |
| `ModificationTimestamp` | Timestamp |  |  | 85% | 82% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135132) |
| `NumberOfBranches` | Number |  |  | 5% | 4% | The calculated value for the number of active branches. | [link](https://ddwiki.reso.org/display/DDW20/NumberOfBranches+Field) |
| `NumberOfNonMemberSalespersons` | Number |  |  |  |  | The total number of active salespersons that are not a member of the national association. | [link](https://ddwiki.reso.org/display/DDW20/NumberOfNonMemberSalespersons+Field) |
| `OfficeAOR` | String List, Single |  | AOR | 35% | 21% | The office's board or association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAOR+Field) |
| `OfficeAORMlsId` | String |  |  | 20% | 11% | The local, well-known identifier for the office's association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAORMlsId+Field) |
| `OfficeAORkey` | String |  |  | 10% | 11% | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAORkey+Field) |
| `OfficeAddress1` | String |  |  | 80% | 82% | The first address line of the physical address of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAddress1+Field) |
| `OfficeAddress2` | String |  |  | 65% | 69% | The unit/suite number of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAddress2+Field) |
| `OfficeAlternateId` | String |  |  |  | 1% | An alternate ID with no specific use. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAlternateId+Field) |
| `OfficeAssociationComments` | String |  |  | 10% | 2% | Notes relating to the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAssociationComments+Field) |
| `OfficeBio` | String |  |  | 5% | 1% | A text field containing biography information for the office record. | [link](https://ddwiki.reso.org/display/DDW20/OfficeBio+Field) |
| `OfficeBranchType` | String List, Single |  | [OfficeBranchType](#officebranchtype) |  | 11% | The level of the office in a hierarchy (i.e., Main, Branch, Stand-Alone, etc.). | [link](https://ddwiki.reso.org/display/DDW20/OfficeBranchType+Field) |
| `OfficeBroker` | Resource |  |  |  |  | The broker for the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeBroker+Field) |
| `OfficeBrokerKey` | String |  |  | 60% | 48% | The MemberKey of the responsible/owning broker. | [link](https://ddwiki.reso.org/display/DDW20/OfficeBrokerKey+Field) |
| `OfficeBrokerMlsId` | String |  |  | 60% | 45% | The MemberMlsId of the broker of record for the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeBrokerMlsId+Field) |
| `OfficeBrokerNationalAssociationId` | String |  |  |  |  | The national association ID of the broker (i.e., the NRDS number in the U.S.). | [link](https://ddwiki.reso.org/display/DDW20/OfficeBrokerNationalAssociationID+Field) |
| `OfficeCity` | String |  |  | 80% | 82% | The city of the physical address of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCity+Field) |
| `OfficeCorporateLicense` | String |  |  | 65% | 56% | An independent license number is issued when an office/firm is a corporation. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicense+Field) |
| `OfficeCountry` | String |  | [Country](#country) | 5% | 1% | The country of the physical address of the office (ISO country code). | [link](https://ddwiki.reso.org/display/DDW20/OfficeCountry+Field) |
| `OfficeCountyOrParish` | String List, Single |  | CountyOrParish | 35% | 4% | The county or parish in which the offices is located. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCountyOrParish+Field) |
| `OfficeEmail` | String |  |  | 85% | 81% | The contact email address of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeEmail+Field) |
| `OfficeFax` | String |  |  | 75% | 77% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/OfficeFax+Field) |
| `OfficeKey` | String |  |  | 75% | 82% | A system-unique identifier for the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135261) |
| `OfficeMailAddress1` | String |  |  | 5% | 1% | The street number, direction, name and suffix of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailAddress1+Field) |
| `OfficeMailAddress2` | String |  |  | 5% | 1% | The unit/suite number of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailAddress2+Field) |
| `OfficeMailCareOf` | String |  |  |  | 11% | The care of (c/o) for the office's mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailCareOf+Field) |
| `OfficeMailCity` | String |  |  | 5% | 1% | The office's city for the mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailCity+Field) |
| `OfficeMailCountry` | String |  | [Country](#country) |  | 1% | The office's country code for the mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailCountry+Field) |
| `OfficeMailCountyOrParish` | String List, Single |  | CountyOrParish |  | 1% | The office's county of the mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailCountyOrParish+Field) |
| `OfficeMailPostalCode` | String |  |  |  | 17% | The postal code of the office's mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailPostalCode+Field) |
| `OfficeMailPostalCodePlus4` | String |  |  |  | 12% | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailPostalCodePlus4+Field) |
| `OfficeMailStateOrProvince` | String |  | [StateOrProvince](#stateorprovince) |  | 17% | The office's state or province of the mailing address. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMailStateOrProvince+Field) |
| `OfficeManager` | Resource |  |  |  |  | The office manager for the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeManager+Field) |
| `OfficeManagerKey` | String |  |  | 30% | 5% | The lead office manager for the given office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeManagerKey+Field) |
| `OfficeManagerMlsId` | String |  |  | 30% | 7% | The lead office manager for the given office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeManagerMlsId+Field) |
| `OfficeMlsId` | String |  |  | 75% | 80% | The local, well-known identifier for the office as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135337) |
| `OfficeName` | String |  |  |  | 100% | The legal or DBA name of the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135343) |
| `OfficeNationalAssociationId` | String |  |  | 55% | 66% | The national association ID of the office (e.g., the NRDS number in the U.S.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135349) |
| `OfficeNationalAssociationIdInsertDate` | Date |  |  |  |  | The date the office record was initially created in the national association's database (e.g., the date the record was added to NRDS in the U.S.). | [link](https://ddwiki.reso.org/display/DDW20/OfficeNationalAssociationIdInsertDate+Field) |
| `OfficePhone` | String |  |  | 85% | 81% | The main contact phone number of the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116905) |
| `OfficePhoneExt` | String |  |  | 35% | 21% | The extension of the given phone number (if applicable). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116911) |
| `OfficePostalCode` | String |  |  | 80% | 81% | The postal code of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficePostalCode+Field) |
| `OfficePostalCodePlus4` | String |  |  | 45% | 31% | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/OfficePostalCodePlus4+Field) |
| `OfficePreferredMedia` | String List, Single |  | [PreferredMedia](#preferredmedia) | 5% | 1% | The method the office prefers to receive media. | [link](https://ddwiki.reso.org/display/DDW20/OfficePreferredMedia+Field) |
| `OfficePrimaryAorId` | String |  |  |  |  | The primary association of REALTORS® (AOR) associated with the member. | [link](https://ddwiki.reso.org/display/DDW20/OfficePrimaryAorId+Field) |
| `OfficePrimaryStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) |  | 0% | The office's primary state or province. | [link](https://ddwiki.reso.org/display/DDW20/OfficePrimaryStateOrProvince+Field) |
| `OfficeSocialMedia` | Collection |  |  |  |  | A collection of the types of social media fields available for this office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeSocialMedia+Field) |
| `OfficeStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) |  | 98% | The state or province in which the office is located. | [link](https://ddwiki.reso.org/display/DDW20/OfficeStateOrProvince+Field) |
| `OfficeStatus` | String List, Single |  | [OfficeStatus](#officestatus) | 75% | 74% | The status of the office's record in the MLS or other organization. | [link](https://ddwiki.reso.org/display/DDW20/OfficeStatus+Field) |
| `OfficeType` | String List, Single |  | [OfficeType](#officetype) | 60% | 62% | The type of business conducted by the office (e.g., Appraisal, MLS, Mortgage). | [link](https://ddwiki.reso.org/display/DDW20/OfficeType+Field) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 55% | 62% | The date/time the roster (member or office) record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135429) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the Office record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135435) |
| `OriginatingSystemID` | String |  |  | 45% | 64% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135440) |
| `OriginatingSystemName` | String |  |  |  | 93% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135447) |
| `OriginatingSystemOfficeKey` | String |  |  | 75% | 77% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemOfficeKey+Field) |
| `OtherPhone` | String |  |  |  | 5% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/OtherPhone+Field) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) | 5% | 1% | A collection of the types of social media fields available for the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135464) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the Office record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135470) |
| `SourceSystemID` | String |  |  | 35% | 46% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135476) |
| `SourceSystemName` | String |  |  | 40% | 32% | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135484) |
| `SourceSystemOfficeKey` | String |  |  | 40% | 44% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemOfficeKey+Field) |
| `SyndicateAgentOption` | String List, Single |  | SyndicateAgentOption | 10% | 1% | A list of options allowing the broker to pass the decision of syndication choice down to the listing agents (i.e., No Agent Choice, Allow Agent Choice, Restrict Agent Choice, etc.). | [link](https://ddwiki.reso.org/display/DDW20/SyndicateAgentOption+Field) |
| `SyndicateTo` | String List, Multi |  | [SyndicateTo](#syndicateto) | 35% | 5% | The principal broker's choice on where they would like their listings syndicated (i.e., Zillow, Trulia, Homes.com, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135503) |
| `VirtualOfficeWebsiteYN` | Boolean |  |  |  |  | Indicates whether or not this is a Virtual Office Website (VOW). | [link](https://ddwiki.reso.org/display/DDW20/VirtualOfficeWebsiteYN+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>BillingOfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FranchiseAffiliation</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Afiliación de Franquicia
  - **French-Canadian Name:** Franchise/affiliation
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>FranchiseNationalAssociationId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 17 2020
  - **Revision Date:** JAN 17 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>IDXOfficeParticipationYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Participación en IDX SN
  - **French-Canadian Name:** Participation du bureau au système IDX O/N
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MainOffice</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MainOfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho Principal
  - **French-Canadian Name:** Clé du bureau principal
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MainOfficeMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau principal
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>Media</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **French-Canadian Name:** Heure et date de la modification
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>NumberOfBranches</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAOR</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Company Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Despacho de AOR
  - **French-Canadian Name:** Chambre/association du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeAORMlsId</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Despacho de AOR
  - **French-Canadian Name:** ID MLS de la chambre/association du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeAORkey</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Subaddress Type = "Key"Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho de AOR
  - **French-Canadian Name:** Clé de la chambre/association du bureau
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeAddress1</code></summary>

  - **BEDES:** Address Line 1 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Despacho1
  - **French-Canadian Name:** Adresse du bureau 1
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeAddress2</code></summary>

  - **BEDES:** Address Line 2 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Despacho2
  - **French-Canadian Name:** Adresse du bureau 2
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeAlternateId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationComments</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Comentarios de Asociación de Despacho
  - **French-Canadian Name:** Remarques de l’association sur le bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeBio</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 18 2023
  - **Revision Date:** APR 18 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeBroker</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeBrokerKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Corredor de Despacho
  - **French-Canadian Name:** Clé du dirigeant du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeBrokerMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Corredor de Despacho
  - **French-Canadian Name:** ID MLS du dirigeant du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeCity</code></summary>

  - **BEDES:** City = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad de Despacho
  - **French-Canadian Name:** Ville du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeCorporateLicense</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Licencia Corporativa de Despacho
  - **French-Canadian Name:** Licence de société du bureau
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeCountry</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCountyOrParish</code></summary>

  - **BEDES:** County = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Condado o Distrito de Despacho
  - **French-Canadian Name:** Comté ou paroisse du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeEmail</code></summary>

  - **BEDES:** Email Address = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Email de Despacho
  - **French-Canadian Name:** Adresse courriel du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeFax</code></summary>

  - **BEDES:** Telephone Number Label = "Fax"Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Fax de Despacho
  - **French-Canadian Name:** Numéro de télécopieur du bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeKey</code></summary>

  - **BEDES:** Subaddress Type = "Key"Contact ID = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho
  - **French-Canadian Name:** Clé du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeMailAddress1</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailAddress2</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCareOf</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCity</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailCountry</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailPostalCode</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailPostalCodePlus4</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMailStateOrProvince</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeManager</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeManagerKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Gerente de Despacho
  - **French-Canadian Name:** Clé du gestionnaire de bureau
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeManagerMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Gerente de Despacho
  - **French-Canadian Name:** ID MLS du gestionnaire de bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeNationalAssociationId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Asociación Nacional de Despacho
  - **French-Canadian Name:** ID de l’association nationale du bureau
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeNationalAssociationIdInsertDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePhone</code></summary>

  - **BEDES:** Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Despacho
  - **French-Canadian Name:** Numéro de téléphone du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficePhoneExt</code></summary>

  - **BEDES:** Telephone Extension = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Extensión Telefónica de Despacho
  - **French-Canadian Name:** Poste téléphonique du bureau
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficePostalCode</code></summary>

  - **BEDES:** ZIP Code = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal de Despacho
  - **French-Canadian Name:** Code postal du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficePostalCodePlus4</code></summary>

  - **BEDES:** ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más 4 de Despacho
  - **French-Canadian Name:** Code postal du bureau +4
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficePreferredMedia</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePrimaryAorId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficePrimaryStateOrProvince</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Despacho
  - **French-Canadian Name:** Statut du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Despacho
  - **French-Canadian Name:** Type de bureau
  - **Status Change Date:** MAY 21 2013
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **BEDES:** Date Status = "Created"Date = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **French-Canadian Name:** Date et heure de l’entrée originale
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **French-Canadian Name:** ID du système d’origine
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemOfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho de Sistema de Origen
  - **French-Canadian Name:** Clé du système d’origine du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OtherPhone</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Redes Sociales
  - **French-Canadian Name:** Type de médias sociaux
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** APR 11 2022

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 20 2020
  - **Revision Date:** JAN 20 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema Fuente
  - **French-Canadian Name:** ID du système source
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Sistema Fuente
  - **French-Canadian Name:** Nom du système source
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemOfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho Sistema Fuente
  - **French-Canadian Name:** Clé du système source du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SyndicateAgentOption</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Opción de Redifusión Agente
  - **French-Canadian Name:** Délégation du lieu d’affichage au courtier/agent
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SyndicateTo</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Redifundir a
  - **French-Canadian Name:** Afficher sur
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>VirtualOfficeWebsiteYN</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

## Lookups

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

### OfficeBranchType

| Value | Definition |
|---|---|
| `Branch` | This office is a branch office. |
| `Main` | This office is the broker's main office. |
| `Stand Alone` | This office is a stand-alone or single-office brokerage. |

### OfficeStatus

| Value | Definition |
|---|---|
| `Active` | The member office's account is active. |
| `Inactive` | The member office's account is not active. |

### OfficeType

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

| Value | Definition |
|---|---|
| `Email` | Send media via email. |
| `Fax` | Send media via fax. |
| `Mail` | Send media via postal mail. |

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

### SyndicateTo

| Value | Definition |
|---|---|
| `Homes.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Homes.com. |
| `ListHub` | The broker, or member if permitted by the broker, is allowing their listings to be sent to ListHub.com. |
| `Realtor.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Realtor.com. |
| `Zillow/Trulia` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Zillow and Trulia. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
