# OfficeCorporateLicense

_RESO Data Dictionary 2.0 resource — 10 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicense+Resource) for the canonical page._

## Groups

- **Other** — 10 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135977) |
| `ModificationTimestamp` | Timestamp |  |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135982) |
| `Office` | Resource |  |  |  |  | The Office resource describes a brokerage office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135988) |
| `OfficeCorporateLicense` | String |  |  |  |  | When an office/firm is a corporation, an independent license number is issued. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135994) |
| `OfficeCorporateLicenseExpirationDate` | Date |  |  |  |  | The expiration date for the office corporation's license. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicenseExpirationDate+Field) |
| `OfficeCorporateLicenseKey` | String |  |  |  |  | A unique identifier for this record from the immediate source. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicenseKey+Field) |
| `OfficeCorporateLicenseState` | String List, Single |  | [StateOrProvince](#stateorprovince) |  |  | The state in which the office corporation is licensed. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicenseState+Field) |
| `OfficeCorporateLicenseType` | String List, Single |  | [OfficeCorporateLicenseType](#officecorporatelicensetype) |  |  | The license type of the office corporation. | [link](https://ddwiki.reso.org/display/DDW20/OfficeCorporateLicenseType+Field) |
| `OfficeKey` | String |  |  |  |  | A system-unique identifier for the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136022) |
| `OfficeMlsId` | String |  |  |  |  | The local, well-known identifier for the office as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136027) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **French-Canadian Name:** Heure et date de la modification
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Office</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCorporateLicense</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Licencia Corporativa de Despacho
  - **French-Canadian Name:** Licence de société du bureau
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCorporateLicenseExpirationDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** OCT 27 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeCorporateLicenseType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Despacho
  - **French-Canadian Name:** Clé du bureau
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau
  - **Status Change Date:** OCT 27 2020
  - **Revision Date:** JUN 17 2021
  - **Added in Version:** 2.0.0

</details>

## Lookups

### OfficeCorporateLicenseType

| Value | Definition |
|---|---|
| `Appraiser` | The office corporate license type is appraiser. |
| `Broker` | The office corporate license type is broker. |

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
