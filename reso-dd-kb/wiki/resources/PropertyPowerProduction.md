# PropertyPowerProduction

_RESO Data Dictionary 2.0 resource — 12 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/PropertyPowerProduction+Resource) for the canonical page._

**Adoption** — weighted Org%: **1%** across 6 measured fields (median 1%, avg 1%).

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135747) |
| `Listing` | Resource |  |  |  |  | The listing associated with the PropertyPowerProduction record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135754) |
| `ListingId` | String |  |  |  | 1% | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135759) |
| `ListingKey` | String |  |  |  | 1% | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135766) |
| `ModificationTimestamp` | Timestamp |  |  |  | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135773) |
| `PowerProductionAnnual` | Number |  |  |  |  | The most important metric of a renewables system is the amount of power it produces per year. | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionAnnual+Field) |
| `PowerProductionAnnualStatus` | String List, Single |  | [PowerProductionAnnualStatus](#powerproductionannualstatus) |  |  | The most important metric of a renewables system is the amount of power it produces per year. | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionAnnualStatus+Field) |
| `PowerProductionKey` | String |  |  |  | 1% | A unique identifier for this record. | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionKey+Field) |
| `PowerProductionOwnership` | String List, Single |  | [PowerProductionOwnership](#powerproductionownership) |  | 1% | The ownership of the power production system (e.g., Seller Owned or Third-Party Owned). | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionOwnership+Field) |
| `PowerProductionSize` | Number |  |  |  |  | The "capacity" of a renewables system. | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionSize+Field) |
| `PowerProductionType` | String List, Single |  | [PowerProductionType](#powerproductiontype) |  | 1% | A list of the type of power production systems available on the property. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135810) |
| `PowerProductionYearInstall` | Number |  |  |  |  | The year a renewables system was installed. | [link](https://ddwiki.reso.org/display/DDW20/PowerProductionYearInstall+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionAnnual</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Producción de Energía Anual
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionAnnualStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Producción de Energía Anual
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Producción de Energía
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionOwnership</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUN 21 2019
  - **Revision Date:** JUN 30 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PowerProductionSize</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tamaño de Producción de Energía
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Producción de Energía
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionYearInstall</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Instalación Anual de Producción de Energía
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### PowerProductionAnnualStatus

| Value | Definition |
|---|---|
| `Actual` | Annual production derived from 12 or more months of actual data. |
| `Estimated` | Annual production as estimated at the time or before the system began operation. |
| `Partially Estimated` | Annual production derived from less than 12 months of actual data, and therefore extrapolated to estimate annual production. |

### PowerProductionOwnership

| Value | Definition |
|---|---|
| `Seller Owned` | The selected power production system is owned by the seller of the property. |
| `Third-Party Owned` | The selected power production system is owned by a third party (e.g., Leased, Power Purchase Agreement). |

### PowerProductionType

| Value | Definition |
|---|---|
| `Photovoltaics` | Solar photovoltaic (PV) devices which generate electricity directly from sunlight via an electronic process that occurs naturally in certain types of material, called semiconductors. |
| `Wind` | Renewable form of onsite power generation. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
