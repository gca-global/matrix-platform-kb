# PropertyUnitTypes

Unit type details for residential income and multifamily properties.

**RESO DD 2.0** — 17 fields · last revised 5/24/2017 · [dd.reso.org](https://dd.reso.org/DD2.0/PropertyUnitTypes/)

**Adoption** — weighted Org%: **14%** across 15 measured fields (median 18%, avg 14%).

## Groups

- **Other** — 17 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/HistoryTransactional/) |
| `Listing` | Resource |  |  |  | The listing associated with the PropertyUnitTypes record. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/Listing/) |
| `ListingId` | String |  |  | 20% | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/ListingId/) |
| `ListingKey` | String |  |  | 21% | A system-unique identifier for the listing. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/ListingKey/) |
| `ModificationTimestamp` | Timestamp |  |  | 20% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/ModificationTimestamp/) |
| `UnitTypeActualRent` | Number |  |  | 22% | Current rent per unit of this type (numeric). | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeActualRent/) |
| `UnitTypeBathsTotal` | Number |  |  | 22% | Number of bathrooms per unit of this type. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeBathsTotal/) |
| `UnitTypeBedsTotal` | Number |  |  | 23% | Number of bedrooms per unit of this type. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeBedsTotal/) |
| `UnitTypeDescription` | String |  |  | 18% | Free-text description of the unit type for marketing copy. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeDescription/) |
| `UnitTypeFurnished` | String List, Single |  | [Furnished](#furnished) | 5% | A single-value lookup: Furnished \| Partially \| Unfurnished. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeFurnished/) |
| `UnitTypeGarageAttachedYN` | Boolean |  |  | 1% | Answers whether or not the given type of unit has an attached garage. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeGarageAttachedYN/) |
| `UnitTypeGarageSpaces` | Number |  |  | 3% | Number of garage spaces allocated to a single unit of this type. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeGarageSpaces/) |
| `UnitTypeKey` | String |  |  | 24% | The unique identifier for a unit type within the originating system. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeKey/) |
| `UnitTypeProForma` | Number |  |  | 1% | The pro forma rent or the expected rental income from the given type of unit. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeProForma/) |
| `UnitTypeTotalRent` | Number |  |  | 10% | Aggregate rent across all units of this type (UnitTypeActualRent * UnitTypeUnitsTotal in the simple case). | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeTotalRent/) |
| `UnitTypeType` | String List, Single |  | [UnitTypeType](#unittypetype) | 15% | A single-value lookup describing the unit type: Apartments \| Studio \| Loft \| Penthouse \| 1 Bedroom \| 2 Bedroom \| 3 Bedroom \| 4 Bedroom Or More \| Efficiency \| Manager's Unit. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeType/) |
| `UnitTypeUnitsTotal` | Number |  |  | 10% | Total number of units of this type within the parent Property. | [link](https://dd.reso.org/DD2.0/PropertyUnitTypes/UnitTypeUnitsTotal/) |

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
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeActualRent</code></summary>

  - **Status:** Active
  - **Spanish Name:** Alquiler Real Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeBathsTotal</code></summary>

  - **Status:** Active
  - **Spanish Name:** Total de Baños Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeBedsTotal</code></summary>

  - **Status:** Active
  - **Spanish Name:** Total de Camas Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeDescription</code></summary>

  - **Status:** Active
  - **Spanish Name:** Descripción Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeFurnished</code></summary>

  - **Status:** Active
  - **Spanish Name:** Amueblado Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeGarageAttachedYN</code></summary>

  - **Status:** Active
  - **Spanish Name:** Garaje Adjunto SN Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeGarageSpaces</code></summary>

  - **Status:** Active
  - **Spanish Name:** Espacios de Garaje Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeProForma</code></summary>

  - **Status:** Active
  - **Spanish Name:** Pro Forma Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeTotalRent</code></summary>

  - **Status:** Active
  - **Spanish Name:** Alquiler Total Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeUnitsTotal</code></summary>

  - **Status:** Active
  - **Spanish Name:** Total de Unidades Tipo de Unidad
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.6.0

</details>

## Lookups

### Furnished

4 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Furnished/)

| Value | Definition |
|---|---|
| `Furnished` | The dwelling being leased is furnished. |
| `Negotiable` | The property may be furnished or left unfurnished at the lessor's request. |
| `Partially` | The dwelling being leased is partially furnished. |
| `Unfurnished` | The dwelling being leased is not furnished. |

### UnitTypeType

10 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/UnitTypeType/)

| Value | Definition |
|---|---|
| `1 Bedroom` | The type of unit has one bedroom. |
| `2 Bedroom` | The type of unit has two bedrooms. |
| `3 Bedroom` | The type of unit has three bedrooms. |
| `4 Bedroom Or More` | The type of unit has four or more bedrooms. |
| `Apartments` | The type of unit is apartments. |
| `Efficiency` | The type of unit is an efficiency. |
| `Loft` | The type of unit is a loft. |
| `Manager's Unit` | The type of unit is a manager's unit. |
| `Penthouse` | The type of unit is a penthouse. |
| `Studio` | The type of unit is a studio. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
