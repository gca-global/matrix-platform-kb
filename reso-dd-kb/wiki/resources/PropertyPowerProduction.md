# PropertyPowerProduction

Different means of producing power on a property, such as solar and wind systems.

**RESO DD 2.0** — 12 fields · last revised 6/30/2022 · [dd.reso.org](https://dd.reso.org/DD2.0/PropertyPowerProduction/)

**Adoption** — weighted Org%: **1%** across 6 measured fields (median 1%, avg 1%).

## Groups

- **Other** — 12 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/HistoryTransactional/) |
| `Listing` | Resource |  |  |  | The listing associated with the PropertyPowerProduction record. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/Listing/) |
| `ListingId` | String |  |  | 1% | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/ListingId/) |
| `ListingKey` | String |  |  | 1% | A system-unique identifier for the listing. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/ListingKey/) |
| `ModificationTimestamp` | Timestamp |  |  | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/ModificationTimestamp/) |
| `PowerProductionAnnual` | Number |  |  |  | The most important metric of a renewables system is the amount of power it produces per year. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionAnnual/) |
| `PowerProductionAnnualStatus` | String List, Single |  | [PowerProductionAnnualStatus](#powerproductionannualstatus) |  | The most important metric of a renewables system is the amount of power it produces per year. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionAnnualStatus/) |
| `PowerProductionKey` | String |  |  | 1% | A unique identifier for this record. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionKey/) |
| `PowerProductionOwnership` | String List, Single |  | [PowerProductionOwnership](#powerproductionownership) | 1% | The ownership of the power production system (e.g., Seller Owned or Third-Party Owned). | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionOwnership/) |
| `PowerProductionSize` | Number |  |  |  | The "capacity" of a renewables system. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionSize/) |
| `PowerProductionType` | String List, Single |  | [PowerProductionType](#powerproductiontype) | 1% | A list of the type of power production systems available on the property. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionType/) |
| `PowerProductionYearInstall` | Number |  |  |  | The year a renewables system was installed. | [link](https://dd.reso.org/DD2.0/PropertyPowerProduction/PowerProductionYearInstall/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Listado
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionAnnual</code></summary>

  - **Status:** Active
  - **Spanish Name:** Producción de Energía Anual
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionAnnualStatus</code></summary>

  - **Status:** Active
  - **Spanish Name:** Estado de Producción de Energía Anual
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Producción de Energía
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionOwnership</code></summary>

  - **Status:** Active
  - **Status Change Date:** 6/21/2019
  - **Revision Date:** 6/30/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PowerProductionSize</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tamaño de Producción de Energía
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Producción de Energía
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionYearInstall</code></summary>

  - **Status:** Active
  - **Spanish Name:** Instalación Anual de Producción de Energía
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

## Lookups

### PowerProductionAnnualStatus

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PowerProductionAnnualStatus/)

| Value | Definition |
|---|---|
| `Actual` | Annual production derived from 12 or more months of actual data. |
| `Estimated` | Annual production as estimated at the time or before the system began operation. |
| `Partially Estimated` | Annual production derived from less than 12 months of actual data, and therefore extrapolated to estimate annual production. |

### PowerProductionOwnership

2 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PowerProductionOwnership/)

| Value | Definition |
|---|---|
| `Seller Owned` | The selected power production system is owned by the seller of the property. |
| `Third-Party Owned` | The selected power production system is owned by a third party (e.g., Leased, Power Purchase Agreement). |

### PowerProductionType

2 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PowerProductionType/)

| Value | Definition |
|---|---|
| `Photovoltaics` | Solar photovoltaic (PV) devices which generate electricity directly from sunlight via an electronic process that occurs naturally in certain types of material, called semiconductors. |
| `Wind` | Renewable form of onsite power generation. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
