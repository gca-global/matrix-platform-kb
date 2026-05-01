# Member

The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. Members are referenced from Property via ListAgentKey / CoListAgentKey, and are responsible for creating, updating, or being assigned to listings.

**Adoption** — weighted Org%: **46%** across 73 measured fields (median 43%, avg 46%).

## Groups

- **Other** — 87 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135079) |
| `JobTitle` | String |  |  |  | 5% | The title or position of the member within their organization. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116488) |
| `LastLoginTimestamp` | Timestamp |  |  | 15% | 2% | The date/time the member last logged into the source or other system. | [link](https://ddwiki.reso.org/display/DDW20/LastLoginTimestamp+Field) |
| `Media` | Collection |  |  | 10% | 7% | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135096) |
| `MemberAOR` | String List, Single |  | AOR | 45% | 21% | The member's primary board or association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/MemberAOR+Field) |
| `MemberAORMlsId` | String |  |  | 25% | 12% | The local, well-known identifier for the member's association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/MemberAORMlsId+Field) |
| `MemberAORkey` | String |  |  | 10% | 11% | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/MemberAORkey+Field) |
| `MemberAddress1` | String |  |  | 75% | 75% | The street number, direction, name and suffix of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberAddress1+Field) |
| `MemberAddress2` | String |  |  | 65% | 66% | The unit/suite number of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberAddress2+Field) |
| `MemberAlternateId` | String |  |  |  | 3% | This is an alternate ID with no specific use. | [link](https://ddwiki.reso.org/display/DDW20/MemberAlternateId+Field) |
| `MemberAssociationComments` | String |  |  | 15% | 3% | The association's notes regarding the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationComments+Field) |
| `MemberBillingPreference` | String List, Single |  | [BillingPreference](#billingpreference) |  |  | The member's preferred method of billing. | [link](https://ddwiki.reso.org/display/DDW20/MemberBillingPreference+Field) |
| `MemberBio` | String |  |  |  | 11% | A text field containing biography information for the member record. | [link](https://ddwiki.reso.org/display/DDW20/MemberBio+Field) |
| `MemberCarrierRoute` | String |  |  | 15% | 1% | The group of addresses to which the U.S. | [link](https://ddwiki.reso.org/display/DDW20/MemberCarrierRoute+Field) |
| `MemberCity` | String |  |  | 75% | 78% | The city of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberCity+Field) |
| `MemberCommitteeCount` | Number |  |  |  |  | The number of current/active committees in which the member belongs. | [link](https://ddwiki.reso.org/display/DDW20/MemberCommitteeCount+Field) |
| `MemberCountry` | String List, Single |  | [Country](#country) | 45% | 29% | The country abbreviation in a postal address. | [link](https://ddwiki.reso.org/display/DDW20/MemberCountry+Field) |
| `MemberCountyOrParish` | String List, Single |  | CountyOrParish | 30% | 2% | The county or parish in which the member is addressed. | [link](https://ddwiki.reso.org/display/DDW20/MemberCountyOrParish+Field) |
| `MemberDesignation` | String List, Multi |  | [MemberDesignation](#memberdesignation) |  | 49% | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® and each affiliated group upon completion of … | [link](https://ddwiki.reso.org/display/DDW20/MemberDesignation+Field) |
| `MemberDirectPhone` | String |  |  | 40% | 19% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberDirectPhone+Field) |
| `MemberEmail` | String |  |  | 80% | 80% | The email address of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberEmail+Field) |
| `MemberFax` | String |  |  | 65% | 56% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberFax+Field) |
| `MemberFirstName` | String |  |  | 80% | 81% | The first name of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberFirstName+Field) |
| `MemberFullName` | String |  |  | 70% | 77% | The full name of the member - first middle last suffix. | [link](https://ddwiki.reso.org/display/DDW20/MemberFullName+Field) |
| `MemberHomePhone` | String |  |  | 45% | 40% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberHomePhone+Field) |
| `MemberIsAssistantTo` | String |  |  |  | 3% | The MemberMlsId of the agent/broker that this member assists. | [link](https://ddwiki.reso.org/display/DDW20/MemberIsAssistantTo+Field) |
| `MemberKey` | String |  |  | 70% | 80% | A system-unique identifier for the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberKey+Field) |
| `MemberLanguages` | String List, Multi |  | [Languages](#languages) | 45% | 37% | The languages the member speaks. | [link](https://ddwiki.reso.org/display/DDW20/MemberLanguages+Field) |
| `MemberLastName` | String |  |  | 80% | 81% | The last name of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberLastName+Field) |
| `MemberLoginId` | String |  |  | 45% | 44% | The ID used to log on to the MLS system. | [link](https://ddwiki.reso.org/display/DDW20/MemberLoginId+Field) |
| `MemberMailOptOutYN` | Boolean |  |  |  |  | Indicates whether or not the member has opted out of receiving solicitation via mail. | [link](https://ddwiki.reso.org/display/DDW20/MemberMailOptOutYN+Field) |
| `MemberMiddleName` | String |  |  | 60% | 57% | The middle name of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberMiddleName+Field) |
| `MemberMlsAccessYN` | Boolean |  |  |  | 21% | Indicates whether or not the member has access to the MLS system. | [link](https://ddwiki.reso.org/display/DDW20/MemberMlsAccessYN+Field) |
| `MemberMlsId` | String |  |  | 75% | 79% | The local, well-known identifier for the member as assigned by the MLS. | [link](https://ddwiki.reso.org/display/DDW20/MemberMlsId+Field) |
| `MemberMlsSecurityClass` | String List, Single |  | MemberMlsSecurityClass | 25% | 38% | The MLS security group or class given to the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberMlsSecurityClass+Field) |
| `MemberMobilePhone` | String |  |  | 65% | 74% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberMobilePhone+Field) |
| `MemberNamePrefix` | String |  |  |  | 15% | The prefix to the member name (e.g., Dr., Mr., Ms.). | [link](https://ddwiki.reso.org/display/DDW20/MemberNamePrefix+Field) |
| `MemberNameSuffix` | String |  |  | 35% | 9% | The suffix to the member surname (e.g., Esq., Jr., III). | [link](https://ddwiki.reso.org/display/DDW20/MemberNameSuffix+Field) |
| `MemberNationalAssociationEntryDate` | Date |  |  |  | 1% | The date that the member's record was entered with the National Association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/MemberNationalAssociationEntryDate+Field) |
| `MemberNationalAssociationId` | String |  |  | 60% | 72% | The national association ID of the member (e.g., in the U.S., this is the NRDS number). | [link](https://ddwiki.reso.org/display/DDW20/MemberNationalAssociationId+Field) |
| `MemberNickname` | String |  |  | 30% | 9% | An alternate name used by the member, usually as a substitute for the first name. | [link](https://ddwiki.reso.org/display/DDW20/MemberNickname+Field) |
| `MemberOfficePhone` | String |  |  | 65% | 53% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberOfficePhone+Field) |
| `MemberOfficePhoneExt` | String |  |  | 40% | 36% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/MemberOfficePhoneExt+Field) |
| `MemberOtherPhone` | Collection |  |  | 1% | 1% | A collection of the types of other phone fields available for this member. | [link](https://ddwiki.reso.org/display/DDW20/MemberOtherPhone+Field) |
| `MemberOtherPhoneType` | String List, Single |  | [MemberOtherPhoneType](#memberotherphonetype) | 10% | 1% | The type of "other" phone (e.g., Preferred; Office, Mobile; Direct; Home; Fax; Voicemail; 1, 2, 3; First, Second, Third; etc.). | [link](https://ddwiki.reso.org/display/DDW20/MemberOtherPhoneType+Field) |
| `MemberPager` | String |  |  | 35% | 17% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberPager+Field) |
| `MemberPassword` | String |  |  | 20% | 1% | A password that the member wishes to share with other systems. | [link](https://ddwiki.reso.org/display/DDW20/MemberPassword+Field) |
| `MemberPhoneTTYTDD` | String |  |  | 1% | 1% | TTY/TDD stands for Teletypewriter/Telecommunications Device for the Deaf. | [link](https://ddwiki.reso.org/display/DDW20/MemberPhoneTTYTDD+Field) |
| `MemberPostalCode` | String |  |  | 75% | 77% | The postal code of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberPostalCode+Field) |
| `MemberPostalCodePlus4` | String |  |  | 50% | 30% | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/MemberPostalCodePlus4+Field) |
| `MemberPreferredMail` | String List, Single |  | [PreferredMail](#preferredmail) |  |  | The preferred mailing address for the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberPreferredMail+Field) |
| `MemberPreferredMedia` | String List, Single |  | [PreferredMedia](#preferredmedia) |  |  | The method the member prefers to receive media by (e.g., Email, Mail, Fax). | [link](https://ddwiki.reso.org/display/DDW20/MemberPreferredMedia+Field) |
| `MemberPreferredPhone` | String |  |  | 70% | 70% | The phone number that the member prefers to be contacted at. | [link](https://ddwiki.reso.org/display/DDW20/MemberPreferredPhone+Field) |
| `MemberPreferredPhoneExt` | String |  |  | 40% | 29% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/MemberPreferredPhoneExt+Field) |
| `MemberPreferredPublication` | String List, Single |  | [PreferredPublication](#preferredpublication) |  |  | Indicates where the member would like to receive any publications from the association. | [link](https://ddwiki.reso.org/display/DDW20/MemberPreferredPublication+Field) |
| `MemberPrimaryAorId` | String |  |  |  | 1% | The primary association of REALTORS® (AOR) associated with the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberPrimaryAorId+Field) |
| `MemberSocialMedia` | Collection |  |  |  |  | A collection of the types of social media fields available for this member. | [link](https://ddwiki.reso.org/display/DDW20/MemberSocialMedia+Field) |
| `MemberStateLicense` | String |  |  | 70% | 76% | The license of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberStateLicense+Field) |
| `MemberStateLicenseExpirationDate` | Date |  |  |  | 0% | The expiration date for the member's license. | [link](https://ddwiki.reso.org/display/DDW20/MemberStateLicenseExpirationDate+Field) |
| `MemberStateLicenseState` | String List, Single |  | [StateOrProvince](#stateorprovince) | 45% | 9% | The state in which the member is licensed. | [link](https://ddwiki.reso.org/display/DDW20/MemberStateLicenseState+Field) |
| `MemberStateLicenseType` | String |  |  | 10% | 1% | The license type of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberStateLicenseType+Field) |
| `MemberStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 75% | 78% | The state or province in which the member is addressed. | [link](https://ddwiki.reso.org/display/DDW20/MemberStateOrProvince+Field) |
| `MemberStatus` | String List, Single |  | [MemberStatus](#memberstatus) | 70% | 78% | The status of the member's record in the MLS or other organization. | [link](https://ddwiki.reso.org/display/DDW20/MemberStatus+Field) |
| `MemberTollFreePhone` | String |  |  | 25% | 21% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberTollFreePhone+Field) |
| `MemberTransferDate` | Date |  |  |  | 3% | The date that the member transferred from one member office to another | [link](https://ddwiki.reso.org/display/DDW20/MemberTransferDate+Field) |
| `MemberType` | String List, Single |  | [MemberType](#membertype) | 65% | 73% | The type of member. | [link](https://ddwiki.reso.org/display/DDW20/MemberType+Field) |
| `MemberVoiceMail` | String |  |  | 25% | 2% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/MemberVoiceMail+Field) |
| `MemberVoiceMailExt` | String |  |  | 15% | 1% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/MemberVoiceMailExt+Field) |
| `MemberVotingPrecinct` | String |  |  |  |  | The voting precinct of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberVotingPrecinct+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  | 98% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135490) |
| `Office` | Resource |  |  |  |  | The Office resource describes a brokerage office. | [link](https://ddwiki.reso.org/display/DDW20/Office+Field) |
| `OfficeKey` | String |  |  | 65% | 59% | A system-unique identifier for the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeKey+Field) |
| `OfficeMlsId` | String |  |  | 60% | 77% | The local, well-known identifier for the office as assigned by the MLS. | [link](https://ddwiki.reso.org/display/DDW20/OfficeMlsId+Field) |
| `OfficeName` | String |  |  | 50% | 56% | The legal or DBA name of the office. | [link](https://ddwiki.reso.org/display/DDW20/OfficeName+Field) |
| `OfficeNationalAssociationId` | String |  |  |  | 1% | The national association ID of the office (i.e., in the U.S., this is the NRDS number). | [link](https://ddwiki.reso.org/display/DDW20/OfficeNationalAssociationId+Field) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 50% | 61% | The date/time the roster (member or office) record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135525) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the Member record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135531) |
| `OriginatingSystemID` | String |  |  | 45% | 63% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135536) |
| `OriginatingSystemMemberKey` | String |  |  | 65% | 76% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemMemberKey+Field) |
| `OriginatingSystemName` | String |  |  | 60% | 76% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135548) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) | 10% | 2% | A list of types of sites, blogs and social media the member URL or ID is referring to (e.g., Website, Blog, Facebook, Twitter, LinkedIn, Instagram). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116963) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the Member record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135562) |
| `SourceSystemID` | String |  |  |  | 58% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135570) |
| `SourceSystemMemberKey` | String |  |  | 35% | 45% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemMemberKey+Field) |
| `SourceSystemName` | String |  |  | 35% | 31% | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135581) |
| `SyndicateTo` | String List, Multi |  | [SyndicateTo](#syndicateto) |  | 2% | When permitted by the broker, the options made by the individual agent on where they would like their listings syndicated (i.e., Zillow, Trulia, Realtor.com, Homes.com, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135588) |
| `UniqueLicenseeIdentifier` | String |  |  |  |  | The Unique Licensee Identifier (ULI) represents a single ID for a licensed real estate agent. | [link](https://ddwiki.reso.org/display/DDW20/UniqueLicenseeIdentifier+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 11 2020
  - **Revision Date:** JAN 11 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>LastLoginTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Último Ingreso
  - **French-Canadian Name:** Heure et date de la dernière session
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>Media</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 12 2020
  - **Revision Date:** JAN 12 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberAOR</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors" Company Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Miembro de AOR
  - **French-Canadian Name:** Chambre/association du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberAORMlsId</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors" Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Miembro de AOR
  - **French-Canadian Name:** ID MLS de la chambre/association du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberAORkey</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors" Subaddress Type = "Key" Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro de AOR
  - **French-Canadian Name:** Clé de la chambre/association du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberAddress1</code></summary>

  - **BEDES:** Address Line 1 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Miembro 1
  - **French-Canadian Name:** Adresse du membre 1
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberAddress2</code></summary>

  - **BEDES:** Address Line 2 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Miembro 2
  - **French-Canadian Name:** Adresse du membre 2
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberAlternateId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationComments</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Comentarios de Asociación de Miembro
  - **French-Canadian Name:** Remarques de l’association sur le membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberCarrierRoute</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ruta Transportista de Miembro
  - **French-Canadian Name:** Itinéraire de transport du membre
  - **Status Change Date:** JAN 17 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberCity</code></summary>

  - **BEDES:** City = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad de Miembro
  - **French-Canadian Name:** Ville du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberCommitteeCount</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberCountry</code></summary>

  - **BEDES:** Country Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** País de Miembro
  - **French-Canadian Name:** Pays du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberCountyOrParish</code></summary>

  - **BEDES:** County = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Condado o Distrito de Miembro
  - **French-Canadian Name:** Comté ou paroisse du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberDirectPhone</code></summary>

  - **BEDES:** Telephone Number Label = "Direct" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Directo de Miembro
  - **French-Canadian Name:** Numéro de téléphone du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberEmail</code></summary>

  - **BEDES:** Email Address = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Email de Miembro
  - **French-Canadian Name:** Courriel du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberFax</code></summary>

  - **BEDES:** Telephone Number Label = "Fax" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Fax de Miembro
  - **French-Canadian Name:** Numéro de télécopieur du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberFirstName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Miembro
  - **French-Canadian Name:** Prénom du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberFullName</code></summary>

  - **BEDES:** Full Name = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Completo de Miembro
  - **French-Canadian Name:** Nom au complet du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberHomePhone</code></summary>

  - **BEDES:** Telephone Number Label = "Home" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Casa de Miembro
  - **French-Canadian Name:** Numéro de téléphone du domicile du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberKey</code></summary>

  - **BEDES:** Subaddress Type = "Key" Identifier = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro
  - **French-Canadian Name:** Clé du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JAN 09 2022

</details>

<details><summary><code>MemberLanguages</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Idiomas de Miembro
  - **French-Canadian Name:** Langues du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberLastName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Apellido de Miembro
  - **French-Canadian Name:** Nom de famille du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberLoginId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Inicio de Miembro
  - **French-Canadian Name:** ID de connexion du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberMailOptOutYN</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberMiddleName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Segundo Nombre de Miembro
  - **French-Canadian Name:** Deuxième prénom du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Miembro
  - **French-Canadian Name:** ID MLS du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberMlsSecurityClass</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clase de Seguridad de MLS de Miembro
  - **French-Canadian Name:** Classe de sécurité MLS du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberMobilePhone</code></summary>

  - **BEDES:** Telephone Number Label = "Mobile" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Móvil de Miembro
  - **French-Canadian Name:** Numéro de cellulaire du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberNameSuffix</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Sufijo Nombre de Miembro
  - **French-Canadian Name:** Suffixe du nom du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberNationalAssociationId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Asociación Nacional de Miembro
  - **French-Canadian Name:** ID de l’association nationale du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberNickname</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Apodo de Miembro
  - **French-Canadian Name:** Surnom du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberOfficePhone</code></summary>

  - **BEDES:** Telephone Number Label = "Work" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Despacho de Miembro
  - **French-Canadian Name:** Numéro de téléphone du bureau du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberOfficePhoneExt</code></summary>

  - **BEDES:** Telephone Number Label = "Work" Telephone Extension = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Teléfono de Despacho de Miembro
  - **French-Canadian Name:** Poste téléphonique du bureau du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberOtherPhone</code></summary>

  - **Status:** ACTIVE
  - **French-Canadian Name:** Autre numéro de téléphone du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberOtherPhoneType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Otro Tipo de Teléfono de Miembro
  - **French-Canadian Name:** Type de l’autre numéro de téléphone du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** APR 11 2022

</details>

<details><summary><code>MemberPager</code></summary>

  - **BEDES:** Telephone Number Label = "Pager" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Buscapersonas de Miembro
  - **French-Canadian Name:** Téléavertisseur du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPassword</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Contraseña de Miembro
  - **French-Canadian Name:** Mot de passe du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPhoneTTYTDD</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono TTYTDD de Miembro
  - **French-Canadian Name:** Numéro de l’ATME/ATS du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPostalCode</code></summary>

  - **BEDES:** ZIP Code = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal de Miembro
  - **French-Canadian Name:** Code postal du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPostalCodePlus4</code></summary>

  - **BEDES:** ZIP Plus 4 = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más 4 de Miembro
  - **French-Canadian Name:** Code postal du membre +4
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPreferredMail</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberPreferredPhone</code></summary>

  - **BEDES:** Priority = "Primary" Telephone Number = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Preferido de Miembro
  - **French-Canadian Name:** Numéro de téléphone préféré du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPreferredPhoneExt</code></summary>

  - **BEDES:** Priority = "Primary" Telephone Extension = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Teléfono Preferido de Miembro
  - **French-Canadian Name:** Poste téléphonique du numéro préféré du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberPreferredPublication</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberPrimaryAorId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicense</code></summary>

  - **BEDES:** Credential = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Licencia Estatal de Miembro
  - **French-Canadian Name:** Permis du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberStateLicenseExpirationDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicenseState</code></summary>

  - **BEDES:** Credential State = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Licencia Estatal de Miembro
  - **French-Canadian Name:** État ou province de délivrance du permis du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberStateLicenseType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateOrProvince</code></summary>

  - **BEDES:** State = [value]
  - **Status:** ACTIVE
  - **Spanish Name:** Estado o Provincia de Miembro
  - **French-Canadian Name:** État ou province du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Miembro
  - **French-Canadian Name:** Statut du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberTollFreePhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Gratuito de Miembro
  - **French-Canadian Name:** Numéro de téléphone sans frais du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberTransferDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Miembro
  - **French-Canadian Name:** Type de membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberVoiceMail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Buzón de Voz de Miembro
  - **French-Canadian Name:** Boîte vocale du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberVoiceMailExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Buzón de Voz de Miembro
  - **French-Canadian Name:** Poste téléphonique de la boîte vocale du membre
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>MemberVotingPrecinct</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Office</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2020
  - **Revision Date:** JAN 06 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho
  - **French-Canadian Name:** Clé du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Despacho
  - **French-Canadian Name:** Nom du bureau
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OfficeNationalAssociationId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 17 2020
  - **Revision Date:** JAN 17 2020
  - **Added in Version:** 2.0.0

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
  - **Status Change Date:** JAN 07 2020
  - **Revision Date:** JAN 07 2020
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

<details><summary><code>OriginatingSystemMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro Sistema de Origen
  - **French-Canadian Name:** Clé du système d’origine du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **French-Canadian Name:** Nom du système d’origine
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JUN 17 2021

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Redes Sociales
  - **French-Canadian Name:** Type de médias sociaux
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** APR 11 2022

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 08 2020
  - **Revision Date:** JAN 08 2020
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro Sistema Fuente
  - **French-Canadian Name:** Clé du système source du membre
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Sistema Fuente
  - **French-Canadian Name:** Nom du système source
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>UniqueLicenseeIdentifier</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 24 2020
  - **Revision Date:** OCT 24 2020
  - **Added in Version:** 2.0.0

</details>

## Lookups

### BillingPreference

| Value | Definition |
|---|---|
| `Email` | Send billing to the member's email address. |
| `Fax` | Send billing to the member via fax. |
| `Mail` | Send billing to the member via postal mail. |

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

### MemberDesignation

| Value | Definition |
|---|---|
| `Accredited Buyer's Representative / ABR` | The Accredited Buyer’s Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| `Accredited Land Consultant / ALC` | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| `At Home With Diversity / AHWD` | Learn to work effectively with and within today’s diverse real estate market. |
| `Certified Commercial Investment Member / CCIM` | The Certified Commercial Investment Member (CCIM) designation is commercial real estate’s global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| `Certified Distressed Property Expert / CDPE` | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today’s turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| `Certified International Property Specialist / CIPS` | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| `Certified Property Manager / CPM` | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| `Certified Real Estate Brokerage Manager / CRB` | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| `Certified Real Estate Team Specialist / C-RETS` | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| `Certified Residential Specialist / CRS` | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| `Counselor of Real Estate / CRE` | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| `e-PRO` | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |
| `General Accredited Appraiser / GAA` | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Graduate, REALTOR Institute / GRI` | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| `Military Relocation Professional / MRP` | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| `NAR's Green Designation / GREEN` | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| `Performance Management Network / PMN` | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| `Pricing Strategy Advisor / PSA` | Enhance your skills in pricing properties, creating CMAs (comparative market analyses), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| `Real Estate Negotiation Expert / RENE` | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| `REALTOR Association Certified Executive / RCE` | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| `Residential Accredited Appraiser / RAA` | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Resort & Second-Home Property Specialist / RSPS` | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| `Seller Representative Specialist / SRS` | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| `Seniors Real Estate Specialist / SRES` | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| `Short Sales & Foreclosure Resource / SFR` | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| `Society of Industrial and Office REALTORS / SIOR` | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| `Transnational Referral Certification / TRC` | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |

### MemberOtherPhoneType

| Value | Definition |
|---|---|
| `Direct` | This direct number of the member. |
| `Fax` | The fax number of the member. |
| `First` | The preferred phone number of the member. |
| `Home` | The home phone number of the member. |
| `Mobile` | The mobile phone number of the member. |
| `Modem` | The modem of the member. |
| `Office` | The office phone number of the member. |
| `Pager` | The pager number of the member. |
| `Preferred` | The preferred phone number of the member. |
| `Second` | The second preferred phone number of the member. |
| `SMS` | The Short Message Service (SMS)/text number of the member. |
| `Third` | The third preferred phone number of the member. |
| `Toll Free` | The toll-free phone number of the member. |
| `Voicemail` | The voicemail of the member. |

### MemberStatus

| Value | Definition |
|---|---|
| `Active` | The member's account is active. |
| `Inactive` | the member's account is not active. |

### MemberType

| Value | Definition |
|---|---|
| `Affiliate` | The member is affiliated with the real estate industry in some manner (e.g., home inspector, photographer, mortgage consultant) but is not necessarily a REALTOR®. |
| `Assistant` | The member is an assistant. |
| `Association Staff` | The member is a member of an association's staff. |
| `Designated REALTOR Appraiser` | The member is a designated appraiser and a member of the National Association of REALTORS® (NAR). |
| `Designated REALTOR Participant` | The member is a designated broker and a member of the National Association of REALTORS® (NAR). |
| `Leasing Agent` | The member holds a leasing license. |
| `Licensed Assistant` | The member is a licensed assistant. |
| `MLS Only Appraiser` | The member is an appraiser and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| `MLS Only Broker` | The member is a broker and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| `MLS Only Broker Associate` | The member is a broker and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| `MLS Only Salesperson` | The member is a salesperson and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| `MLS Staff` | The individual is a member of MLS staff. |
| `Non Member/Vendor` | The individual is not a member or is a vendor. |
| `Office Manager` | The member is a licensed office manager. |
| `Photographer` | The member is a photographer. |
| `REALTOR Appraiser` | The member is an appraiser and a member of the National Association of REALTORS® (NAR). |
| `REALTOR Broker Associate` | The member has a broker's license but is working under a broker and is a member of the National Association of REALTORS® (NAR). |
| `REALTOR Salesperson` | The member is a sales person and a member of the National Association of REALTORS® (NAR). |
| `Unlicensed Assistant` | The member is an unlicensed assistant. |

### PreferredMail

| Value | Definition |
|---|---|
| `Home Address` | Send mail to the home address. |
| `Mailing Address` | Send mail to the designated mailing address. |
| `Office Mailing Address` | Send mail to the office's designated mailing address. |
| `Office Street Address` | Send mail to office's street address. |

### PreferredMedia

| Value | Definition |
|---|---|
| `Email` | Send media via email. |
| `Fax` | Send media via fax. |
| `Mail` | Send media via postal mail. |

### PreferredPublication

| Value | Definition |
|---|---|
| `Fax` | Send publications via fax. |
| `Home Address` | Send publications to the home address. |
| `Mailing Address` | Send publications to the designated mailing address. |
| `Office Mailing Address` | Send publications to the office mailing address. |
| `Office Street Address` | Send publications to the office street address. |

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
