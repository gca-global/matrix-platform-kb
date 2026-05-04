# Teams

_RESO Data Dictionary 2.0 resource — 45 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/Teams+Resource) for the canonical page._

**Adoption** — weighted Org%: **0%** across 18 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 45 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135628) |
| `Media` | Collection |  |  |  |  | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135635) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135641) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 5% | 1% | The date/time the roster (team or office) record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135646) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the Teams record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135652) |
| `OriginatingSystemID` | String |  |  | 1% | 1% | The RESO Unique Organization Identifier's (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135659) |
| `OriginatingSystemKey` | String |  |  | 5% | 1% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135664) |
| `OriginatingSystemName` | String |  |  | 5% | 1% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135670) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) | 1% | 1% | A list of types of sites or social media that the team Uniform Resource Locator (URL) or ID is referring to (e.g., website, blog, Facebook, Twitter, LinkedIn, Instagram). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135674) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the Teams record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135679) |
| `SourceSystemID` | String |  |  |  | 0% | The RESO Unique Organization Identifier's (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135685) |
| `SourceSystemKey` | String |  |  | 1% | 1% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135691) |
| `SourceSystemName` | String |  |  | 1% | 1% | The name of the team record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135697) |
| `TeamAddress1` | String |  |  | 5% | 1% | The street number, direction, name and suffix of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamAddress1+Field) |
| `TeamAddress2` | String |  |  | 5% | 1% | The unit/suite number of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamAddress2+Field) |
| `TeamCarrierRoute` | String |  |  | 1% | 1% | The group of addresses to which the U.S. | [link](https://ddwiki.reso.org/display/DDW20/TeamCarrierRoute+Field) |
| `TeamCity` | String |  |  | 5% | 1% | The city of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamCity+Field) |
| `TeamCountry` | String List, Single |  | [Country](#country) |  |  | The country abbreviation in a postal address. | [link](https://ddwiki.reso.org/display/DDW20/TeamCountry+Field) |
| `TeamCountyOrParish` | String List, Single |  | CountyOrParish | 1% | 1% | The county or parish in which the team is addressed. | [link](https://ddwiki.reso.org/display/DDW20/TeamCountyOrParish+Field) |
| `TeamDescription` | String |  |  | 1% | 1% | A description or marketing information about the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamDescription+Field) |
| `TeamDirectPhone` | String |  |  | 5% | 1% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamDirectPhone+Field) |
| `TeamEmail` | String |  |  | 5% | 1% | The contact email address of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamEmail+Field) |
| `TeamFax` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamFax+Field) |
| `TeamKey` | String |  |  | 5% | 1% | A system-unique identifier for the team. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2117293) |
| `TeamLead` | Resource |  |  |  |  | The team lead for the given team. | [link](https://ddwiki.reso.org/display/DDW20/TeamLead+Field) |
| `TeamLeadKey` | String |  |  | 1% | 1% | The unique system identifier of the team's lead member. | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadKey+Field) |
| `TeamLeadLoginId` | String |  |  | 5% | 1% | The ID used to log on to the MLS system. | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadLoginId+Field) |
| `TeamLeadMlsId` | String |  |  | 5% | 1% | The MemberMlsId of the lead member of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadMlsId+Field) |
| `TeamLeadNationalAssociationId` | String |  |  |  |  | The national association ID of the team lead (i.e., NRDS number in the U.S.). | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadNationalAssociationId+Field) |
| `TeamLeadStateLicense` | String |  |  | 5% | 1% | The license of the team lead. | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadStateLicense+Field) |
| `TeamLeadStateLicenseState` | String List, Single |  | [StateOrProvince](#stateorprovince) | 1% | 1% | The state in which the team lead is licensed. | [link](https://ddwiki.reso.org/display/DDW20/TeamLeadStateLicenseState+Field) |
| `TeamMobilePhone` | String |  |  | 5% | 1% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamMobilePhone+Field) |
| `TeamName` | String |  |  | 5% | 1% | The name of the team as established by the team's leader and members. | [link](https://ddwiki.reso.org/display/DDW20/TeamName+Field) |
| `TeamOfficePhone` | String |  |  | 5% | 1% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamOfficePhone+Field) |
| `TeamOfficePhoneExt` | String |  |  | 5% | 1% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/TeamOfficePhoneExt+Field) |
| `TeamPostalCode` | String |  |  | 5% | 1% | The postal code of the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamPostalCode+Field) |
| `TeamPostalCodePlus4` | String |  |  | 5% | 1% | The four-digit extension of the U.S. | [link](https://ddwiki.reso.org/display/DDW20/TeamPostalCodePlus4+Field) |
| `TeamPreferredPhone` | String |  |  | 5% | 1% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamPreferredPhone+Field) |
| `TeamPreferredPhoneExt` | String |  |  | 5% | 1% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/TeamPreferredPhoneExt+Field) |
| `TeamStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) | 1% | 1% | The state or province in which the team is addressed. | [link](https://ddwiki.reso.org/display/DDW20/TeamStateOrProvince+Field) |
| `TeamStatus` | String List, Single |  | [TeamStatus](#teamstatus) | 5% | 1% | The status of the team's record in the MLS or other organization. | [link](https://ddwiki.reso.org/display/DDW20/TeamStatus+Field) |
| `TeamTollFreePhone` | String |  |  |  |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamTollFreePhone+Field) |
| `TeamVoiceMail` | String |  |  | 1% | 1% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/TeamVoiceMail+Field) |
| `TeamVoiceMailExt` | String |  |  | 1% | 1% | The extension of the given phone number, if applicable. | [link](https://ddwiki.reso.org/display/DDW20/TeamVoiceMailExt+Field) |
| `TeamsSocialMedia` | Collection |  |  |  |  | A collection of the types of social media fields available for this team. | [link](https://ddwiki.reso.org/display/DDW20/TeamsSocialMedia+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Media</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015
  - **Added in Version:** 1.4.0

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
  - **Status Change Date:** FEB 18 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Redes Sociales
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Sistema Fuente
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

<details><summary><code>TeamAddress1</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Equipo 1
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamAddress2</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Dirección de Equipo 2
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamCarrierRoute</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ruta Transportista de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamCity</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ciudad de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamCountyOrParish</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Condado o Distrito de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamDirectPhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Directo de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamEmail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Email de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamLead</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>TeamLeadKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Jefe de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamLeadLoginId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Ingreso Jefe de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamLeadMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS Jefe de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamLeadStateLicense</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Licencia Estatal Jefe de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamLeadStateLicenseState</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Licencia Estatal Jefe de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMobilePhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Móvil de Equipo
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamOfficePhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono de Despacho de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamOfficePhoneExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Extensión Telefónica de Despacho de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamPostalCode</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamPostalCodePlus4</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Código Postal Más4 de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamPreferredPhone</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Teléfono Preferido de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamPreferredPhoneExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Teléfono Preferido de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamStateOrProvince</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado o Provincia de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** AUG 12 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamVoiceMail</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Buzón de Voz de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamVoiceMailExt</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Ext de Buzón de Voz de Equipo
  - **Status Change Date:** JUL 21 2015
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamsSocialMedia</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

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

### TeamStatus

| Value | Definition |
|---|---|
| `Active` | The team is active. |
| `Inactive` | The team is not active. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
