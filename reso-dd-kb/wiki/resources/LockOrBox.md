# LockOrBox

_RESO Data Dictionary 2.0 resource — 44 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/LockOrBox+Resource) for the canonical page._

## Groups

- **Other** — 44 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135893) |
| `KeyOrCredentialId` | String |  |  |  |  | The local, well-known identifier for a given lockbox/smartlock system key or credential. | [link](https://ddwiki.reso.org/display/DDW20/KeyOrCredentialId+Field) |
| `ListAgentFullName` | String |  |  |  |  | The full name of the listing agent of record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135905) |
| `ListingAddress1` | String |  |  |  |  | The street number, direction, name and suffix of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingAddress1+Field) |
| `ListingAddress2` | String |  |  |  |  | The unit/suite number of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingAddress2+Field) |
| `ListingCity` | String |  |  |  |  | The city of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingCity+Field) |
| `ListingCountry` | String List, Single |  | [Country](#country) |  |  | The country of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingCountry+Field) |
| `ListingId` | String |  |  |  |  | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135933) |
| `ListingKey` | String |  |  |  |  | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135939) |
| `ListingLatitude` | Number |  |  |  |  | The latitude of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingLatitude+Field) |
| `ListingLongitude` | Number |  |  |  |  | The longitude of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingLongitude+Field) |
| `ListingPostalCode` | String |  |  |  |  | The postal code of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingPostalCode+Field) |
| `ListingPostalCodePlus4` | String |  |  |  |  | The four-digit U.S. | [link](https://ddwiki.reso.org/display/DDW20/ListingPostalCodePlus4+Field) |
| `ListingStateOrProvince` | String List, Single |  | [StateOrProvince](#stateorprovince) |  |  | The state or province of the property where the lockbox/smartlock is located. | [link](https://ddwiki.reso.org/display/DDW20/ListingStateOrProvince+Field) |
| `ListingTimeZone` | String |  | [IanaTimeZoneValues](#ianatimezonevalues) |  |  | The standard name of the time zone of the property where the lockbox/smartlock is located, as provided by the IANA tz database. | [link](https://ddwiki.reso.org/display/DDW20/ListingTimeZone+Field) |
| `LockOrBoxAccessTimestamp` | Timestamp |  |  |  |  | The transactional timestamp automatically recorded by the lockbox/smartlock system representing the date/time the lockbox or lock was last accessed. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxAccessTimestamp+Field) |
| `LockOrBoxAccessType` | String List, Multi |  | [LockOrBoxAccessType](#lockorboxaccesstype) |  |  | The method of access for the lockbox or smartlock. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxAccessType+Field) |
| `LockOrBoxId` | String |  |  |  |  | The local, well-known identifier for a given lockbox/smartlock system. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxId+Field) |
| `LockOrBoxInstalledTimestamp` | Timestamp |  |  |  |  | The transactional timestamp automatically recorded by the lockbox/smartlock system representing the date/time the lockbox or lock was last installed at a property. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxInstalledTimestamp+Field) |
| `LockOrBoxKey` | String |  |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxKey+Field) |
| `LockOrBoxOriginatingSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxOriginatingSystemID+Field) |
| `LockOrBoxOriginatingSystemKey` | String |  |  |  |  | The name of the originating record provider. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxOriginatingSystemKey+Field) |
| `LockOrBoxOriginatingSystemName` | String |  |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxOriginatingSystemName+Field) |
| `LockOrBoxSourceSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxSourceSystemID+Field) |
| `LockOrBoxSourceSystemKey` | String |  |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxSourceSystemKey+Field) |
| `LockOrBoxSourceSystemName` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/LockOrBoxSourceSystemName+Field) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=12361004) |
| `Notes` | String |  |  |  |  | Notes or feedback about the property or showing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136043) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the LockOrBox record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136049) |
| `ShowingAgent` | Resource |  |  |  |  | The office contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgent+Field) |
| `ShowingAgentAOR` | String List, Single |  | AOR |  |  | The showing contact's board or association of REALTORS®. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentAOR+Field) |
| `ShowingAgentEmail` | String |  |  |  |  | The email address of the contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentEmail+Field) |
| `ShowingAgentFirstName` | String |  |  |  |  | The first name of the contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentFirstName+Field) |
| `ShowingAgentFullName` | String |  |  |  |  | The first, middle and last name of the contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentFullName+Field) |
| `ShowingAgentId` | String |  |  |  |  | The local, well-known lockbox/smartlock system identifier of the showing contact. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentId+Field) |
| `ShowingAgentLastName` | String |  |  |  |  | The last name of the contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentLastName+Field) |
| `ShowingAgentMlsId` | String |  |  |  |  | The MemberMlsId of the agent who is showing the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentMlsId+Field) |
| `ShowingAgentPhone` | String |  |  |  |  | The North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentPhone+Field) |
| `ShowingAgentPhoneExt` | String |  |  |  |  | The phone number extension of the contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingAgentPhoneExt+Field) |
| `ShowingOffice` | Resource |  |  |  |  | The agent contact for showings of the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingOffice+Field) |
| `ShowingOfficeId` | String |  |  |  |  | The local, well-known lockbox/smartlock system identifier of the showing office. | [link](https://ddwiki.reso.org/display/DDW20/ShowingOfficeId+Field) |
| `ShowingOfficeName` | String |  |  |  |  | The legal name of the brokerage/company showing the property. | [link](https://ddwiki.reso.org/display/DDW20/ShowingOfficeName+Field) |
| `ShowingOfficePhone` | String |  |  |  |  | The North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://ddwiki.reso.org/display/DDW20/ShowingOfficePhone+Field) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the LockOrBox record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136140) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>KeyOrCredentialId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListAgentFullName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingAddress2</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingCity</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingCountry</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingLatitude</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingLongitude</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingPostalCode</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingPostalCodePlus4</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingTimeZone</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxAccessTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxAccessType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxInstalledTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxOriginatingSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxOriginatingSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxOriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxSourceSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxSourceSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LockOrBoxSourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Notes</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentAOR</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentEmail</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentFirstName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentFullName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentLastName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentMlsId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingAgentPhoneExt</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingOffice</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingOfficeId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingOfficeName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingOfficePhone</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
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

### IanaTimeZoneValues

| Value | Definition |
|---|---|
| `Africa/Abidjan` | The time zone is identified as the Africa/Abidjan time zone from the IANA tz database. |
| `Africa/Accra` | The time zone is identified as the Africa/Accra time zone from the IANA tz database. |
| `Africa/Addis_Ababa` | The time zone is identified as the Africa/Addis_Ababa time zone from the IANA tz database. |
| `Africa/Algiers` | The time zone is identified as the Africa/Algiers time zone from the IANA tz database. |
| `Africa/Asmara` | The time zone is identified as the Africa/Asmara time zone from the IANA tz database. |
| `Africa/Asmera` | The time zone is identified as the Africa/Asmera time zone from the IANA tz database. |
| `Africa/Bamako` | The time zone is identified as the Africa/Bamako time zone from the IANA tz database. |
| `Africa/Bangui` | The time zone is identified as the Africa/Bangui time zone from the IANA tz database. |
| `Africa/Banjul` | The time zone is identified as the Africa/Banjul time zone from the IANA tz database. |
| `Africa/Bissau` | The time zone is identified as the Africa/Bissau time zone from the IANA tz database. |
| `Africa/Blantyre` | The time zone is identified as the Africa/Blantyre time zone from the IANA tz database. |
| `Africa/Brazzaville` | The time zone is identified as the Africa/Brazzaville time zone from the IANA tz database. |
| `Africa/Bujumbura` | The time zone is identified as the Africa/Bujumbura time zone from the IANA tz database. |
| `Africa/Cairo` | The time zone is identified as the Africa/Cairo time zone from the IANA tz database. |
| `Africa/Casablanca` | The time zone is identified as the Africa/Casablanca time zone from the IANA tz database. |
| `Africa/Ceuta` | The time zone is identified as the Africa/Ceuta time zone from the IANA tz database. |
| `Africa/Conakry` | The time zone is identified as the Africa/Conakry time zone from the IANA tz database. |
| `Africa/Dakar` | The time zone is identified as the Africa/Dakar time zone from the IANA tz database. |
| `Africa/Dar_es_Salaam` | The time zone is identified as the Africa/Dar_es_Salaam time zone from the IANA tz database. |
| `Africa/Djibouti` | The time zone is identified as the Africa/Djibouti time zone from the IANA tz database. |
| `Africa/Douala` | The time zone is identified as the Africa/Douala time zone from the IANA tz database. |
| `Africa/El_Aaiun` | The time zone is identified as the Africa/El_Aaiun time zone from the IANA tz database. |
| `Africa/Freetown` | The time zone is identified as the Africa/Freetown time zone from the IANA tz database. |
| `Africa/Gaborone` | The time zone is identified as the Africa/Gaborone time zone from the IANA tz database. |
| `Africa/Harare` | The time zone is identified as the Africa/Harare time zone from the IANA tz database. |
| `Africa/Johannesburg` | The time zone is identified as the Africa/Johannesburg time zone from the IANA tz database. |
| `Africa/Juba` | The time zone is identified as the Africa/Juba time zone from the IANA tz database. |
| `Africa/Kampala` | The time zone is identified as the Africa/Kampala time zone from the IANA tz database. |
| `Africa/Khartoum` | The time zone is identified as the Africa/Khartoum time zone from the IANA tz database. |
| `Africa/Kigali` | The time zone is identified as the Africa/Kigali time zone from the IANA tz database. |
| `Africa/Kinshasa` | The time zone is identified as the Africa/Kinshasa time zone from the IANA tz database. |
| `Africa/Lagos` | The time zone is identified as the Africa/Lagos time zone from the IANA tz database. |
| `Africa/Libreville` | The time zone is identified as the Africa/Libreville time zone from the IANA tz database. |
| `Africa/Lome` | The time zone is identified as the Africa/Lome time zone from the IANA tz database. |
| `Africa/Luanda` | The time zone is identified as the Africa/Luanda time zone from the IANA tz database. |
| `Africa/Lubumbashi` | The time zone is identified as the Africa/Lubumbashi time zone from the IANA tz database. |
| `Africa/Lusaka` | The time zone is identified as the Africa/Lusaka time zone from the IANA tz database. |
| `Africa/Malabo` | The time zone is identified as the Africa/Malabo time zone from the IANA tz database. |
| `Africa/Maputo` | The time zone is identified as the Africa/Maputo time zone from the IANA tz database. |
| `Africa/Maseru` | The time zone is identified as the Africa/Maseru time zone from the IANA tz database. |
| `Africa/Mbabane` | The time zone is identified as the Africa/Mbabane time zone from the IANA tz database. |
| `Africa/Mogadishu` | The time zone is identified as the Africa/Mogadishu time zone from the IANA tz database. |
| `Africa/Monrovia` | The time zone is identified as the Africa/Monrovia time zone from the IANA tz database. |
| `Africa/Nairobi` | The time zone is identified as the Africa/Nairobi time zone from the IANA tz database. |
| `Africa/Ndjamena` | The time zone is identified as the Africa/Ndjamena time zone from the IANA tz database. |
| `Africa/Niamey` | The time zone is identified as the Africa/Niamey time zone from the IANA tz database. |
| `Africa/Nouakchott` | The time zone is identified as the Africa/Nouakchott time zone from the IANA tz database. |
| `Africa/Ouagadougou` | The time zone is identified as the Africa/Ouagadougou time zone from the IANA tz database. |
| `Africa/Porto-Novo` | The time zone is identified as the Africa/Porto-Novo time zone from the IANA tz database. |
| `Africa/Sao_Tome` | The time zone is identified as the Africa/Sao_Tome time zone from the IANA tz database. |
| `Africa/Timbuktu` | The time zone is identified as the Africa/Timbuktu time zone from the IANA tz database. |
| `Africa/Tripoli` | The time zone is identified as the Africa/Tripoli time zone from the IANA tz database. |
| `Africa/Tunis` | The time zone is identified as the Africa/Tunis time zone from the IANA tz database. |
| `Africa/Windhoek` | The time zone is identified as the Africa/Windhoek time zone from the IANA tz database. |
| `America/Adak` | The time zone is identified as the America/Adak time zone from the IANA tz database. |
| `America/Anchorage` | The time zone is identified as the America/Anchorage time zone from the IANA tz database. |
| `America/Anguilla` | The time zone is identified as the America/Anguilla time zone from the IANA tz database. |
| `America/Antigua` | The time zone is identified as the America/Antigua time zone from the IANA tz database. |
| `America/Araguaina` | The time zone is identified as the America/Araguaina time zone from the IANA tz database. |
| `America/Argentina/Buenos_Aires` | The time zone is identified as the America/Argentina/Buenos_Aires time zone from the IANA tz database. |
| `America/Argentina/Catamarca` | The time zone is identified as the America/Argentina/Catamarca time zone from the IANA tz database. |
| `America/Argentina/ComodRivadavia` | The time zone is identified as the America/Argentina/ComodRivadavia time zone from the IANA tz database. |
| `America/Argentina/Cordoba` | The time zone is identified as the America/Argentina/Cordoba time zone from the IANA tz database. |
| `America/Argentina/Jujuy` | The time zone is identified as the America/Argentina/Jujuy time zone from the IANA tz database. |
| `America/Argentina/La_Rioja` | The time zone is identified as the America/Argentina/La_Rioja time zone from the IANA tz database. |
| `America/Argentina/Mendoza` | The time zone is identified as the America/Argentina/Mendoza time zone from the IANA tz database. |
| `America/Argentina/Rio_Gallegos` | The time zone is identified as the America/Argentina/Rio_Gallegos time zone from the IANA tz database. |
| `America/Argentina/Salta` | The time zone is identified as the America/Argentina/Salta time zone from the IANA tz database. |
| `America/Argentina/San_Juan` | The time zone is identified as the America/Argentina/San_Juan time zone from the IANA tz database. |
| `America/Argentina/San_Luis` | The time zone is identified as the America/Argentina/San_Luis time zone from the IANA tz database. |
| `America/Argentina/Tucuman` | The time zone is identified as the America/Argentina/Tucuman time zone from the IANA tz database. |
| `America/Argentina/Ushuaia` | The time zone is identified as the America/Argentina/Ushuaia time zone from the IANA tz database. |
| `America/Aruba` | The time zone is identified as the America/Aruba time zone from the IANA tz database. |
| `America/Asuncion` | The time zone is identified as the America/Asuncion time zone from the IANA tz database. |
| `America/Atikokan` | The time zone is identified as the America/Atikokan time zone from the IANA tz database. |
| `America/Atka` | The time zone is identified as the America/Atka time zone from the IANA tz database. |
| `America/Bahia` | The time zone is identified as the America/Bahia time zone from the IANA tz database. |
| `America/Bahia_Banderas` | The time zone is identified as the America/Bahia_Banderas time zone from the IANA tz database. |
| `America/Barbados` | The time zone is identified as the America/Barbados time zone from the IANA tz database. |
| `America/Belem` | The time zone is identified as the America/Belem time zone from the IANA tz database. |
| `America/Belize` | The time zone is identified as the America/Belize time zone from the IANA tz database. |
| `America/Blanc-Sablon` | The time zone is identified as the America/Blanc-Sablon time zone from the IANA tz database. |
| `America/Boa_Vista` | The time zone is identified as the America/Boa_Vista time zone from the IANA tz database. |
| `America/Bogota` | The time zone is identified as the America/Bogota time zone from the IANA tz database. |
| `America/Boise` | The time zone is identified as the America/Boise time zone from the IANA tz database. |
| `America/Buenos_Aires` | The time zone is identified as the America/Buenos_Aires time zone from the IANA tz database. |
| `America/Cambridge_Bay` | The time zone is identified as the America/Cambridge_Bay time zone from the IANA tz database. |
| `America/Campo_Grande` | The time zone is identified as the America/Campo_Grande time zone from the IANA tz database. |
| `America/Cancun` | The time zone is identified as the America/Cancun time zone from the IANA tz database. |
| `America/Caracas` | The time zone is identified as the America/Caracas time zone from the IANA tz database. |
| `America/Catamarca` | The time zone is identified as the America/Catamarca time zone from the IANA tz database. |
| `America/Cayenne` | The time zone is identified as the America/Cayenne time zone from the IANA tz database. |
| `America/Cayman` | The time zone is identified as the America/Cayman time zone from the IANA tz database. |
| `America/Chicago` | The time zone is identified as the America/Chicago time zone from the IANA tz database. |
| `America/Chihuahua` | The time zone is identified as the America/Chihuahua time zone from the IANA tz database. |
| `America/Ciudad_Juarez` | The time zone is identified as the America/Ciudad_Juarez time zone from the IANA tz database. |
| `America/Coral_Harbour` | The time zone is identified as the America/Coral_Harbour time zone from the IANA tz database. |
| `America/Cordoba` | The time zone is identified as the America/Cordoba time zone from the IANA tz database. |
| `America/Costa_Rica` | The time zone is identified as the America/Costa_Rica time zone from the IANA tz database. |
| `America/Creston` | The time zone is identified as the America/Creston time zone from the IANA tz database. |
| `America/Cuiaba` | The time zone is identified as the America/Cuiaba time zone from the IANA tz database. |
| `America/Curacao` | The time zone is identified as the America/Curacao time zone from the IANA tz database. |
| `America/Danmarkshavn` | The time zone is identified as the America/Danmarkshavn time zone from the IANA tz database. |
| `America/Dawson` | The time zone is identified as the America/Dawson time zone from the IANA tz database. |
| `America/Dawson_Creek` | The time zone is identified as the America/Dawson_Creek time zone from the IANA tz database. |
| `America/Denver` | The time zone is identified as the America/Denver time zone from the IANA tz database. |
| `America/Detroit` | The time zone is identified as the America/Detroit time zone from the IANA tz database. |
| `America/Dominica` | The time zone is identified as the America/Dominica time zone from the IANA tz database. |
| `America/Edmonton` | The time zone is identified as the America/Edmonton time zone from the IANA tz database. |
| `America/Eirunepe` | The time zone is identified as the America/Eirunepe time zone from the IANA tz database. |
| `America/El_Salvador` | The time zone is identified as the America/El_Salvador time zone from the IANA tz database. |
| `America/Ensenada` | The time zone is identified as the America/Ensenada time zone from the IANA tz database. |
| `America/Fort_Nelson` | The time zone is identified as the America/Fort_Nelson time zone from the IANA tz database. |
| `America/Fort_Wayne` | The time zone is identified as the America/Fort_Wayne time zone from the IANA tz database. |
| `America/Fortaleza` | The time zone is identified as the America/Fortaleza time zone from the IANA tz database. |
| `America/Glace_Bay` | The time zone is identified as the America/Glace_Bay time zone from the IANA tz database. |
| `America/Godthab` | The time zone is identified as the America/Godthab time zone from the IANA tz database. |
| `America/Goose_Bay` | The time zone is identified as the America/Goose_Bay time zone from the IANA tz database. |
| `America/Grand_Turk` | The time zone is identified as the America/Grand_Turk time zone from the IANA tz database. |
| `America/Grenada` | The time zone is identified as the America/Grenada time zone from the IANA tz database. |
| `America/Guadeloupe` | The time zone is identified as the America/Guadeloupe time zone from the IANA tz database. |
| `America/Guatemala` | The time zone is identified as the America/Guatemala time zone from the IANA tz database. |
| `America/Guayaquil` | The time zone is identified as the America/Guayaquil time zone from the IANA tz database. |
| `America/Guyana` | The time zone is identified as the America/Guyana time zone from the IANA tz database. |
| `America/Halifax` | The time zone is identified as the America/Halifax time zone from the IANA tz database. |
| `America/Havana` | The time zone is identified as the America/Havana time zone from the IANA tz database. |
| `America/Hermosillo` | The time zone is identified as the America/Hermosillo time zone from the IANA tz database. |
| `America/Indiana/Indianapolis` | The time zone is identified as the America/Indiana/Indianapolis time zone from the IANA tz database. |
| `America/Indiana/Knox` | The time zone is identified as the America/Indiana/Knox time zone from the IANA tz database. |
| `America/Indiana/Marengo` | The time zone is identified as the America/Indiana/Marengo time zone from the IANA tz database. |
| `America/Indiana/Petersburg` | The time zone is identified as the America/Indiana/Petersburg time zone from the IANA tz database. |
| `America/Indiana/Tell_City` | The time zone is identified as the America/Indiana/Tell_City time zone from the IANA tz database. |
| `America/Indiana/Vevay` | The time zone is identified as the America/Indiana/Vevay time zone from the IANA tz database. |
| `America/Indiana/Vincennes` | The time zone is identified as the America/Indiana/Vincennes time zone from the IANA tz database. |
| `America/Indiana/Winamac` | The time zone is identified as the America/Indiana/Winamac time zone from the IANA tz database. |
| `America/Indianapolis` | The time zone is identified as the America/Indianapolis time zone from the IANA tz database. |
| `America/Inuvik` | The time zone is identified as the America/Inuvik time zone from the IANA tz database. |
| `America/Iqaluit` | The time zone is identified as the America/Iqaluit time zone from the IANA tz database. |
| `America/Jamaica` | The time zone is identified as the America/Jamaica time zone from the IANA tz database. |
| `America/Jujuy` | The time zone is identified as the America/Jujuy time zone from the IANA tz database. |
| `America/Juneau` | The time zone is identified as the America/Juneau time zone from the IANA tz database. |
| `America/Kentucky/Louisville` | The time zone is identified as the America/Kentucky/Louisville time zone from the IANA tz database. |
| `America/Kentucky/Monticello` | The time zone is identified as the America/Kentucky/Monticello time zone from the IANA tz database. |
| `America/Knox_IN` | The time zone is identified as the America/Knox_IN time zone from the IANA tz database. |
| `America/Kralendijk` | The time zone is identified as the America/Kralendijk time zone from the IANA tz database. |
| `America/La_Paz` | The time zone is identified as the America/La_Paz time zone from the IANA tz database. |
| `America/Lima` | The time zone is identified as the America/Lima time zone from the IANA tz database. |
| `America/Los_Angeles` | The time zone is identified as the America/Los_Angeles time zone from the IANA tz database. |
| `America/Louisville` | The time zone is identified as the America/Louisville time zone from the IANA tz database. |
| `America/Lower_Princes` | The time zone is identified as the America/Lower_Princes time zone from the IANA tz database. |
| `America/Maceio` | The time zone is identified as the America/Maceio time zone from the IANA tz database. |
| `America/Managua` | The time zone is identified as the America/Managua time zone from the IANA tz database. |
| `America/Manaus` | The time zone is identified as the America/Manaus time zone from the IANA tz database. |
| `America/Marigot` | The time zone is identified as the America/Marigot time zone from the IANA tz database. |
| `America/Martinique` | The time zone is identified as the America/Martinique time zone from the IANA tz database. |
| `America/Matamoros` | The time zone is identified as the America/Matamoros time zone from the IANA tz database. |
| `America/Mazatlan` | The time zone is identified as the America/Mazatlan time zone from the IANA tz database. |
| `America/Mendoza` | The time zone is identified as the America/Mendoza time zone from the IANA tz database. |
| `America/Menominee` | The time zone is identified as the America/Menominee time zone from the IANA tz database. |
| `America/Merida` | The time zone is identified as the America/Merida time zone from the IANA tz database. |
| `America/Metlakatla` | The time zone is identified as the America/Metlakatla time zone from the IANA tz database. |
| `America/Mexico_City` | The time zone is identified as the America/Mexico_City time zone from the IANA tz database. |
| `America/Miquelon` | The time zone is identified as the America/Miquelon time zone from the IANA tz database. |
| `America/Moncton` | The time zone is identified as the America/Moncton time zone from the IANA tz database. |
| `America/Monterrey` | The time zone is identified as the America/Monterrey time zone from the IANA tz database. |
| `America/Montevideo` | The time zone is identified as the America/Montevideo time zone from the IANA tz database. |
| `America/Montreal` | The time zone is identified as the America/Montreal time zone from the IANA tz database. |
| `America/Montserrat` | The time zone is identified as the America/Montserrat time zone from the IANA tz database. |
| `America/Nassau` | The time zone is identified as the America/Nassau time zone from the IANA tz database. |
| `America/New_York` | The time zone is identified as the America/New_York time zone from the IANA tz database. |
| `America/Nipigon` | The time zone is identified as the America/Nipigon time zone from the IANA tz database. |
| `America/Nome` | The time zone is identified as the America/Nome time zone from the IANA tz database. |
| `America/Noronha` | The time zone is identified as the America/Noronha time zone from the IANA tz database. |
| `America/North_Dakota/Beulah` | The time zone is identified as the America/North_Dakota/Beulah time zone from the IANA tz database. |
| `America/North_Dakota/Center` | The time zone is identified as the America/North_Dakota/Center time zone from the IANA tz database. |
| `America/North_Dakota/New_Salem` | The time zone is identified as the America/North_Dakota/New_Salem time zone from the IANA tz database. |
| `America/Nuuk` | The time zone is identified as the America/Nuuk time zone from the IANA tz database. |
| `America/Ojinaga` | The time zone is identified as the America/Ojinaga time zone from the IANA tz database. |
| `America/Panama` | The time zone is identified as the America/Panama time zone from the IANA tz database. |
| `America/Pangnirtung` | The time zone is identified as the America/Pangnirtung time zone from the IANA tz database. |
| `America/Paramaribo` | The time zone is identified as the America/Paramaribo time zone from the IANA tz database. |
| `America/Phoenix` | The time zone is identified as the America/Phoenix time zone from the IANA tz database. |
| `America/Port_of_Spain` | The time zone is identified as the America/Port_of_Spain time zone from the IANA tz database. |
| `America/Port-au-Prince` | The time zone is identified as the America/Port-au-Prince time zone from the IANA tz database. |
| `America/Porto_Acre` | The time zone is identified as the America/Porto_Acre time zone from the IANA tz database. |
| `America/Porto_Velho` | The time zone is identified as the America/Porto_Velho time zone from the IANA tz database. |
| `America/Puerto_Rico` | The time zone is identified as the America/Puerto_Rico time zone from the IANA tz database. |
| `America/Punta_Arenas` | The time zone is identified as the America/Punta_Arenas time zone from the IANA tz database. |
| `America/Rainy_River` | The time zone is identified as the America/Rainy_River time zone from the IANA tz database. |
| `America/Rankin_Inlet` | The time zone is identified as the America/Rankin_Inlet time zone from the IANA tz database. |
| `America/Recife` | The time zone is identified as the America/Recife time zone from the IANA tz database. |
| `America/Regina` | The time zone is identified as the America/Regina time zone from the IANA tz database. |
| `America/Resolute` | The time zone is identified as the America/Resolute time zone from the IANA tz database. |
| `America/Rio_Branco` | The time zone is identified as the America/Rio_Branco time zone from the IANA tz database. |
| `America/Rosario` | The time zone is identified as the America/Rosario time zone from the IANA tz database. |
| `America/Santa_Isabel` | The time zone is identified as the America/Santa_Isabel time zone from the IANA tz database. |
| `America/Santarem` | The time zone is identified as the America/Santarem time zone from the IANA tz database. |
| `America/Santiago` | The time zone is identified as the America/Santiago time zone from the IANA tz database. |
| `America/Santo_Domingo` | The time zone is identified as the America/Santo_Domingo time zone from the IANA tz database. |
| `America/Sao_Paulo` | The time zone is identified as the America/Sao_Paulo time zone from the IANA tz database. |
| `America/Scoresbysund` | The time zone is identified as the America/Scoresbysund time zone from the IANA tz database. |
| `America/Shiprock` | The time zone is identified as the America/Shiprock time zone from the IANA tz database. |
| `America/Sitka` | The time zone is identified as the America/Sitka time zone from the IANA tz database. |
| `America/St_Barthelemy` | The time zone is identified as the America/St_Barthelemy time zone from the IANA tz database. |
| `America/St_Johns` | The time zone is identified as the America/St_Johns time zone from the IANA tz database. |
| `America/St_Kitts` | The time zone is identified as the America/St_Kitts time zone from the IANA tz database. |
| `America/St_Lucia` | The time zone is identified as the America/St_Lucia time zone from the IANA tz database. |
| `America/St_Thomas` | The time zone is identified as the America/St_Thomas time zone from the IANA tz database. |
| `America/St_Vincent` | The time zone is identified as the America/St_Vincent time zone from the IANA tz database. |
| `America/Swift_Current` | The time zone is identified as the America/Swift_Current time zone from the IANA tz database. |
| `America/Tegucigalpa` | The time zone is identified as the America/Tegucigalpa time zone from the IANA tz database. |
| `America/Thule` | The time zone is identified as the America/Thule time zone from the IANA tz database. |
| `America/Thunder_Bay` | The time zone is identified as the America/Thunder_Bay time zone from the IANA tz database. |
| `America/Tijuana` | The time zone is identified as the America/Tijuana time zone from the IANA tz database. |
| `America/Toronto` | The time zone is identified as the America/Toronto time zone from the IANA tz database. |
| `America/Tortola` | The time zone is identified as the America/Tortola time zone from the IANA tz database. |
| `America/Vancouver` | The time zone is identified as the America/Vancouver time zone from the IANA tz database. |
| `America/Virgin` | The time zone is identified as the America/Virgin time zone from the IANA tz database. |
| `America/Whitehorse` | The time zone is identified as the America/Whitehorse time zone from the IANA tz database. |
| `America/Winnipeg` | The time zone is identified as the America/Winnipeg time zone from the IANA tz database. |
| `America/Yakutat` | The time zone is identified as the America/Yakutat time zone from the IANA tz database. |
| `America/Yellowknife` | The time zone is identified as the America/Yellowknife time zone from the IANA tz database. |
| `Antarctica/Casey` | The time zone is identified as the Antarctica/Casey time zone from the IANA tz database. |
| `Antarctica/Davis` | The time zone is identified as the Antarctica/Davis time zone from the IANA tz database. |
| `Antarctica/DumontDUrville` | The time zone is identified as the Antarctica/DumontDUrville time zone from the IANA tz database. |
| `Antarctica/Macquarie` | The time zone is identified as the Antarctica/Macquarie time zone from the IANA tz database. |
| `Antarctica/Mawson` | The time zone is identified as the Antarctica/Mawson time zone from the IANA tz database. |
| `Antarctica/McMurdo` | The time zone is identified as the Antarctica/McMurdo time zone from the IANA tz database. |
| `Antarctica/Palmer` | The time zone is identified as the Antarctica/Palmer time zone from the IANA tz database. |
| `Antarctica/Rothera` | The time zone is identified as the Antarctica/Rothera time zone from the IANA tz database. |
| `Antarctica/South_Pole` | The time zone is identified as the Antarctica/South_Pole time zone from the IANA tz database. |
| `Antarctica/Syowa` | The time zone is identified as the Antarctica/Syowa time zone from the IANA tz database. |
| `Antarctica/Troll` | The time zone is identified as the Antarctica/Troll time zone from the IANA tz database. |
| `Antarctica/Vostok` | The time zone is identified as the Antarctica/Vostok time zone from the IANA tz database. |
| `Arctic/Longyearbyen` | The time zone is identified as the Arctic/Longyearbyen time zone from the IANA tz database. |
| `Asia/Aden` | The time zone is identified as the Asia/Aden time zone from the IANA tz database. |
| `Asia/Almaty` | The time zone is identified as the Asia/Almaty time zone from the IANA tz database. |
| `Asia/Amman` | The time zone is identified as the Asia/Amman time zone from the IANA tz database. |
| `Asia/Anadyr` | The time zone is identified as the Asia/Anadyr time zone from the IANA tz database. |
| `Asia/Aqtau` | The time zone is identified as the Asia/Aqtau time zone from the IANA tz database. |
| `Asia/Aqtobe` | The time zone is identified as the Asia/Aqtobe time zone from the IANA tz database. |
| `Asia/Ashgabat` | The time zone is identified as the Asia/Ashgabat time zone from the IANA tz database. |
| `Asia/Ashkhabad` | The time zone is identified as the Asia/Ashkhabad time zone from the IANA tz database. |
| `Asia/Atyrau` | The time zone is identified as the Asia/Atyrau time zone from the IANA tz database. |
| `Asia/Baghdad` | The time zone is identified as the Asia/Baghdad time zone from the IANA tz database. |
| `Asia/Bahrain` | The time zone is identified as the Asia/Bahrain time zone from the IANA tz database. |
| `Asia/Baku` | The time zone is identified as the Asia/Baku time zone from the IANA tz database. |
| `Asia/Bangkok` | The time zone is identified as the Asia/Bangkok time zone from the IANA tz database. |
| `Asia/Barnaul` | The time zone is identified as the Asia/Barnaul time zone from the IANA tz database. |
| `Asia/Beirut` | The time zone is identified as the Asia/Beirut time zone from the IANA tz database. |
| `Asia/Bishkek` | The time zone is identified as the Asia/Bishkek time zone from the IANA tz database. |
| `Asia/Brunei` | The time zone is identified as the Asia/Brunei time zone from the IANA tz database. |
| `Asia/Calcutta` | The time zone is identified as the Asia/Calcutta time zone from the IANA tz database. |
| `Asia/Chita` | The time zone is identified as the Asia/Chita time zone from the IANA tz database. |
| `Asia/Choibalsan` | The time zone is identified as the Asia/Choibalsan time zone from the IANA tz database. |
| `Asia/Chongqing` | The time zone is identified as the Asia/Chongqing time zone from the IANA tz database. |
| `Asia/Chungking` | The time zone is identified as the Asia/Chungking time zone from the IANA tz database. |
| `Asia/Colombo` | The time zone is identified as the Asia/Colombo time zone from the IANA tz database. |
| `Asia/Dacca` | The time zone is identified as the Asia/Dacca time zone from the IANA tz database. |
| `Asia/Damascus` | The time zone is identified as the Asia/Damascus time zone from the IANA tz database. |
| `Asia/Dhaka` | The time zone is identified as the Asia/Dhaka time zone from the IANA tz database. |
| `Asia/Dili` | The time zone is identified as the Asia/Dili time zone from the IANA tz database. |
| `Asia/Dubai` | The time zone is identified as the Asia/Dubai time zone from the IANA tz database. |
| `Asia/Dushanbe` | The time zone is identified as the Asia/Dushanbe time zone from the IANA tz database. |
| `Asia/Famagusta` | The time zone is identified as the Asia/Famagusta time zone from the IANA tz database. |
| `Asia/Gaza` | The time zone is identified as the Asia/Gaza time zone from the IANA tz database. |
| `Asia/Harbin` | The time zone is identified as the Asia/Harbin time zone from the IANA tz database. |
| `Asia/Hebron` | The time zone is identified as the Asia/Hebron time zone from the IANA tz database. |
| `Asia/Ho_Chi_Minh` | The time zone is identified as the Asia/Ho_Chi_Minh time zone from the IANA tz database. |
| `Asia/Hong_Kong` | The time zone is identified as the Asia/Hong_Kong time zone from the IANA tz database. |
| `Asia/Hovd` | The time zone is identified as the Asia/Hovd time zone from the IANA tz database. |
| `Asia/Irkutsk` | The time zone is identified as the Asia/Irkutsk time zone from the IANA tz database. |
| `Asia/Istanbul` | The time zone is identified as the Asia/Istanbul time zone from the IANA tz database. |
| `Asia/Jakarta` | The time zone is identified as the Asia/Jakarta time zone from the IANA tz database. |
| `Asia/Jayapura` | The time zone is identified as the Asia/Jayapura time zone from the IANA tz database. |
| `Asia/Jerusalem` | The time zone is identified as the Asia/Jerusalem time zone from the IANA tz database. |
| `Asia/Kabul` | The time zone is identified as the Asia/Kabul time zone from the IANA tz database. |
| `Asia/Kamchatka` | The time zone is identified as the Asia/Kamchatka time zone from the IANA tz database. |
| `Asia/Karachi` | The time zone is identified as the Asia/Karachi time zone from the IANA tz database. |
| `Asia/Kashgar` | The time zone is identified as the Asia/Kashgar time zone from the IANA tz database. |
| `Asia/Kathmandu` | The time zone is identified as the Asia/Kathmandu time zone from the IANA tz database. |
| `Asia/Katmandu` | The time zone is identified as the Asia/Katmandu time zone from the IANA tz database. |
| `Asia/Khandyga` | The time zone is identified as the Asia/Khandyga time zone from the IANA tz database. |
| `Asia/Kolkata` | The time zone is identified as the Asia/Kolkata time zone from the IANA tz database. |
| `Asia/Krasnoyarsk` | The time zone is identified as the Asia/Krasnoyarsk time zone from the IANA tz database. |
| `Asia/Kuala_Lumpur` | The time zone is identified as the Asia/Kuala_Lumpur time zone from the IANA tz database. |
| `Asia/Kuching` | The time zone is identified as the Asia/Kuching time zone from the IANA tz database. |
| `Asia/Kuwait` | The time zone is identified as the Asia/Kuwait time zone from the IANA tz database. |
| `Asia/Macao` | The time zone is identified as the Asia/Macao time zone from the IANA tz database. |
| `Asia/Macau` | The time zone is identified as the Asia/Macau time zone from the IANA tz database. |
| `Asia/Magadan` | The time zone is identified as the Asia/Magadan time zone from the IANA tz database. |
| `Asia/Makassar` | The time zone is identified as the Asia/Makassar time zone from the IANA tz database. |
| `Asia/Manila` | The time zone is identified as the Asia/Manila time zone from the IANA tz database. |
| `Asia/Muscat` | The time zone is identified as the Asia/Muscat time zone from the IANA tz database. |
| `Asia/Nicosia` | The time zone is identified as the Asia/Nicosia time zone from the IANA tz database. |
| `Asia/Novokuznetsk` | The time zone is identified as the Asia/Novokuznetsk time zone from the IANA tz database. |
| `Asia/Novosibirsk` | The time zone is identified as the Asia/Novosibirsk time zone from the IANA tz database. |
| `Asia/Omsk` | The time zone is identified as the Asia/Omsk time zone from the IANA tz database. |
| `Asia/Oral` | The time zone is identified as the Asia/Oral time zone from the IANA tz database. |
| `Asia/Phnom_Penh` | The time zone is identified as the Asia/Phnom_Penh time zone from the IANA tz database. |
| `Asia/Pontianak` | The time zone is identified as the Asia/Pontianak time zone from the IANA tz database. |
| `Asia/Pyongyang` | The time zone is identified as the Asia/Pyongyang time zone from the IANA tz database. |
| `Asia/Qatar` | The time zone is identified as the Asia/Qatar time zone from the IANA tz database. |
| `Asia/Qostanay` | The time zone is identified as the Asia/Qostanay time zone from the IANA tz database. |
| `Asia/Qyzylorda` | The time zone is identified as the Asia/Qyzylorda time zone from the IANA tz database. |
| `Asia/Rangoon` | The time zone is identified as the Asia/Rangoon time zone from the IANA tz database. |
| `Asia/Riyadh` | The time zone is identified as the Asia/Riyadh time zone from the IANA tz database. |
| `Asia/Saigon` | The time zone is identified as the Asia/Saigon time zone from the IANA tz database. |
| `Asia/Sakhalin` | The time zone is identified as the Asia/Sakhalin time zone from the IANA tz database. |
| `Asia/Samarkand` | The time zone is identified as the Asia/Samarkand time zone from the IANA tz database. |
| `Asia/Seoul` | The time zone is identified as the Asia/Seoul time zone from the IANA tz database. |
| `Asia/Shanghai` | The time zone is identified as the Asia/Shanghai time zone from the IANA tz database. |
| `Asia/Singapore` | The time zone is identified as the Asia/Singapore time zone from the IANA tz database. |
| `Asia/Srednekolymsk` | The time zone is identified as the Asia/Srednekolymsk time zone from the IANA tz database. |
| `Asia/Taipei` | The time zone is identified as the Asia/Taipei time zone from the IANA tz database. |
| `Asia/Tashkent` | The time zone is identified as the Asia/Tashkent time zone from the IANA tz database. |
| `Asia/Tbilisi` | The time zone is identified as the Asia/Tbilisi time zone from the IANA tz database. |
| `Asia/Tehran` | The time zone is identified as the Asia/Tehran time zone from the IANA tz database. |
| `Asia/Tel_Aviv` | The time zone is identified as the Asia/Tel_Aviv time zone from the IANA tz database. |
| `Asia/Thimbu` | The time zone is identified as the Asia/Thimbu time zone from the IANA tz database. |
| `Asia/Thimphu` | The time zone is identified as the Asia/Thimphu time zone from the IANA tz database. |
| `Asia/Tokyo` | The time zone is identified as the Asia/Tokyo time zone from the IANA tz database. |
| `Asia/Tomsk` | The time zone is identified as the Asia/Tomsk time zone from the IANA tz database. |
| `Asia/Ujung_Pandang` | The time zone is identified as the Asia/Ujung_Pandang time zone from the IANA tz database. |
| `Asia/Ulaanbaatar` | The time zone is identified as the Asia/Ulaanbaatar time zone from the IANA tz database. |
| `Asia/Ulan_Bator` | The time zone is identified as the Asia/Ulan_Bator time zone from the IANA tz database. |
| `Asia/Urumqi` | The time zone is identified as the Asia/Urumqi time zone from the IANA tz database. |
| `Asia/Ust-Nera` | The time zone is identified as the Asia/Ust-Nera time zone from the IANA tz database. |
| `Asia/Vientiane` | The time zone is identified as the Asia/Vientiane time zone from the IANA tz database. |
| `Asia/Vladivostok` | The time zone is identified as the Asia/Vladivostok time zone from the IANA tz database. |
| `Asia/Yakutsk` | The time zone is identified as the Asia/Yakutsk time zone from the IANA tz database. |
| `Asia/Yangon` | The time zone is identified as the Asia/Yangon time zone from the IANA tz database. |
| `Asia/Yekaterinburg` | The time zone is identified as the Asia/Yekaterinburg time zone from the IANA tz database. |
| `Asia/Yerevan` | The time zone is identified as the Asia/Yerevan time zone from the IANA tz database. |
| `Atlantic/Azores` | The time zone is identified as the Atlantic/Azores time zone from the IANA tz database. |
| `Atlantic/Bermuda` | The time zone is identified as the Atlantic/Bermuda time zone from the IANA tz database. |
| `Atlantic/Canary` | The time zone is identified as the Atlantic/Canary time zone from the IANA tz database. |
| `Atlantic/Cape_Verde` | The time zone is identified as the Atlantic/Cape_Verde time zone from the IANA tz database. |
| `Atlantic/Faeroe` | The time zone is identified as the Atlantic/Faeroe time zone from the IANA tz database. |
| `Atlantic/Faroe` | The time zone is identified as the Atlantic/Faroe time zone from the IANA tz database. |
| `Atlantic/Jan_Mayen` | The time zone is identified as the Atlantic/Jan_Mayen time zone from the IANA tz database. |
| `Atlantic/Madeira` | The time zone is identified as the Atlantic/Madeira time zone from the IANA tz database. |
| `Atlantic/Reykjavik` | The time zone is identified as the Atlantic/Reykjavik time zone from the IANA tz database. |
| `Atlantic/South_Georgia` | The time zone is identified as the Atlantic/South_Georgia time zone from the IANA tz database. |
| `Atlantic/St_Helena` | The time zone is identified as the Atlantic/St_Helena time zone from the IANA tz database. |
| `Atlantic/Stanley` | The time zone is identified as the Atlantic/Stanley time zone from the IANA tz database. |
| `Australia/ACT` | The time zone is identified as the Australia/ACT time zone from the IANA tz database. |
| `Australia/Adelaide` | The time zone is identified as the Australia/Adelaide time zone from the IANA tz database. |
| `Australia/Brisbane` | The time zone is identified as the Australia/Brisbane time zone from the IANA tz database. |
| `Australia/Broken_Hill` | The time zone is identified as the Australia/Broken_Hill time zone from the IANA tz database. |
| `Australia/Canberra` | The time zone is identified as the Australia/Canberra time zone from the IANA tz database. |
| `Australia/Currie` | The time zone is identified as the Australia/Currie time zone from the IANA tz database. |
| `Australia/Darwin` | The time zone is identified as the Australia/Darwin time zone from the IANA tz database. |
| `Australia/Eucla` | The time zone is identified as the Australia/Eucla time zone from the IANA tz database. |
| `Australia/Hobart` | The time zone is identified as the Australia/Hobart time zone from the IANA tz database. |
| `Australia/LHI` | The time zone is identified as the Australia/LHI time zone from the IANA tz database. |
| `Australia/Lindeman` | The time zone is identified as the Australia/Lindeman time zone from the IANA tz database. |
| `Australia/Lord_Howe` | The time zone is identified as the Australia/Lord_Howe time zone from the IANA tz database. |
| `Australia/Melbourne` | The time zone is identified as the Australia/Melbourne time zone from the IANA tz database. |
| `Australia/North` | The time zone is identified as the Australia/North time zone from the IANA tz database. |
| `Australia/NSW` | The time zone is identified as the Australia/NSW time zone from the IANA tz database. |
| `Australia/Perth` | The time zone is identified as the Australia/Perth time zone from the IANA tz database. |
| `Australia/Queensland` | The time zone is identified as the Australia/Queensland time zone from the IANA tz database. |
| `Australia/South` | The time zone is identified as the Australia/South time zone from the IANA tz database. |
| `Australia/Sydney` | The time zone is identified as the Australia/Sydney time zone from the IANA tz database. |
| `Australia/Tasmania` | The time zone is identified as the Australia/Tasmania time zone from the IANA tz database. |
| `Australia/Victoria` | The time zone is identified as the Australia/Victoria time zone from the IANA tz database. |
| `Australia/West` | The time zone is identified as the Australia/West time zone from the IANA tz database. |
| `Australia/Yancowinna` | The time zone is identified as the Australia/Yancowinna time zone from the IANA tz database. |
| `Brazil/Acre` | The time zone is identified as the Brazil/Acre time zone from the IANA tz database. |
| `Brazil/DeNoronha` | The time zone is identified as the Brazil/DeNoronha time zone from the IANA tz database. |
| `Brazil/East` | The time zone is identified as the Brazil/East time zone from the IANA tz database. |
| `Brazil/West` | The time zone is identified as the Brazil/West time zone from the IANA tz database. |
| `Canada/Atlantic` | The time zone is identified as the Canada/Atlantic time zone from the IANA tz database. |
| `Canada/Central` | The time zone is identified as the Canada/Central time zone from the IANA tz database. |
| `Canada/Eastern` | The time zone is identified as the Canada/Eastern time zone from the IANA tz database. |
| `Canada/Mountain` | The time zone is identified as the Canada/Mountain time zone from the IANA tz database. |
| `Canada/Newfoundland` | The time zone is identified as the Canada/Newfoundland time zone from the IANA tz database. |
| `Canada/Pacific` | The time zone is identified as the Canada/Pacific time zone from the IANA tz database. |
| `Canada/Saskatchewan` | The time zone is identified as the Canada/Saskatchewan time zone from the IANA tz database. |
| `Canada/Yukon` | The time zone is identified as the Canada/Yukon time zone from the IANA tz database. |

### LockOrBoxAccessType

| Value | Definition |
|---|---|
| `App` | The lockbox/smartlock can be unlocked with a mobile application. |
| `Card` | The lockbox/smartlock can be unlocked with an access card. |
| `Code` | The lockbox/smartlock can be unlocked with an access code. |

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
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
