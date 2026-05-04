# MemberStateLicense

Supports members that hold multiple state licenses.

**RESO DD 2.0** — 10 fields · last revised 6/17/2021 · [dd.reso.org](https://dd.reso.org/DD2.0/MemberStateLicense/)

## Groups

- **Other** — 10 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/HistoryTransactional/) |
| `Member` | Resource |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/Member/) |
| `MemberKey` | String |  |  |  | A system-unique identifier for the member. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberKey/) |
| `MemberMlsId` | String |  |  |  | The local, well-known identifier for the member as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberMlsId/) |
| `MemberStateLicense` | String |  |  |  | The license of the Member. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberStateLicense/) |
| `MemberStateLicenseExpirationDate` | Date |  |  |  | The expiration date for the member's license. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberStateLicenseExpirationDate/) |
| `MemberStateLicenseKey` | String |  |  |  | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberStateLicenseKey/) |
| `MemberStateLicenseState` | String List, Single |  | [StateOrProvince](#stateorprovince) |  | The state in which the member is licensed. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberStateLicenseState/) |
| `MemberStateLicenseType` | String List, Single |  | [MemberStateLicenseType](#memberstatelicensetype) |  | The license type of the member. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/MemberStateLicenseType/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/MemberStateLicense/ModificationTimestamp/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Member</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro
  - **French-Canadian Name:** Clé du membre
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Miembro
  - **French-Canadian Name:** ID MLS du membre
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicense</code></summary>

  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Miembro
  - **French-Canadian Name:** Permis du membre
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicenseExpirationDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 10/27/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicenseKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 10/27/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicenseState</code></summary>

  - **Status:** Active
  - **Spanish Name:** Estado de Licencia Estatal de Miembro
  - **French-Canadian Name:** État ou province de délivrance du permis du membre
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStateLicenseType</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 10/27/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **French-Canadian Name:** Heure et date de la modification
  - **Status Change Date:** 10/27/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

## Lookups

### MemberStateLicenseType

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/MemberStateLicenseType/)

| Value | Definition |
|---|---|
| `Appraiser` | The member state license type is appraiser. |
| `Broker` | The member state license type is broker. |
| `Salesperson` | The member state license type is salesperson. |

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

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
