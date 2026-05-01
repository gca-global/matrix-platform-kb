# PropertyUnitTypes

The PropertyUnitTypes resource describes the different unit types within a multi-unit Property (Studio, 1 Bedroom, 2 Bedroom, Penthouse, ...). Each row carries beds/baths/units totals plus rent and description for that unit type. Critical for new-construction developments where a single project listing fans into many sellable unit types.

**Adoption** — weighted Org%: **14%** across 15 measured fields (median 18%, avg 14%).

## Groups

- **Other** — 17 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135788) |
| `Listing` | Resource |  |  |  |  | The listing associated with the PropertyUnitTypes record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135794) |
| `ListingId` | String |  |  | 15% | 12% | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135800) |
| `ListingKey` | String |  |  | 20% | 12% | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135806) |
| `ModificationTimestamp` | Timestamp |  |  | 20% | 12% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135812) |
| `UnitTypeActualRent` | Number |  |  | 15% | 10% | Current rent per unit of this type (numeric). | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeActualRent+Field) |
| `UnitTypeBathsTotal` | Number |  |  | 15% | 11% | Number of bathrooms per unit of this type. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeBathsTotal+Field) |
| `UnitTypeBedsTotal` | Number |  |  | 15% | 11% | Number of bedrooms per unit of this type. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeBedsTotal+Field) |
| `UnitTypeDescription` | String |  |  | 15% | 8% | Free-text description of the unit type for marketing copy. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeDescription+Field) |
| `UnitTypeFurnished` | String List, Single |  | [Furnished](#furnished) | 10% | 2% | A single-value lookup: Furnished \| Partially \| Unfurnished. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeFurnished+Field) |
| `UnitTypeGarageAttachedYN` | Boolean |  |  | 10% | 1% | Answers whether or not the given type of unit has an attached garage. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeGarageAttachedYN+Field) |
| `UnitTypeGarageSpaces` | Number |  |  | 10% | 1% | Number of garage spaces allocated to a single unit of this type. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeGarageSpaces+Field) |
| `UnitTypeKey` | String |  |  | 20% | 12% | The unique identifier for a unit type within the originating system. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeKey+Field) |
| `UnitTypeProForma` | Number |  |  |  | 1% | The pro forma rent or the expected rental income from the given type of unit. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeProForma+Field) |
| `UnitTypeTotalRent` | Number |  |  | 10% | 3% | Aggregate rent across all units of this type (UnitTypeActualRent * UnitTypeUnitsTotal in the simple case). | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeTotalRent+Field) |
| `UnitTypeType` | String List, Single |  | [UnitTypeType](#unittypetype) | 15% | 5% | A single-value lookup describing the unit type: Apartments \| Studio \| Loft \| Penthouse \| 1 Bedroom \| 2 Bedroom \| 3 Bedroom \| 4 Bedroom Or More \| Efficiency \| Manager's Unit. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135876) |
| `UnitTypeUnitsTotal` | Number |  |  | 15% | 4% | Total number of units of this type within the parent Property. | [link](https://ddwiki.reso.org/display/DDW20/UnitTypeUnitsTotal+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Listing</code></summary>

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
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeActualRent</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Alquiler Real Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeBathsTotal</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Total de Baños Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeBedsTotal</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Total de Camas Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeFurnished</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Amueblado Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** APR 11 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeGarageAttachedYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Garaje Adjunto SN Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeGarageSpaces</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Espacios de Garaje Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeTotalRent</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Alquiler Total Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitTypeUnitsTotal</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Total de Unidades Tipo de Unidad
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### Furnished

| Value | Definition |
|---|---|
| `Furnished` | The dwelling being leased is furnished. |
| `Negotiable` | The property may be furnished or left unfurnished at the lessor's request. |
| `Partially` | The dwelling being leased is partially furnished. |
| `Unfurnished` | The dwelling being leased is not furnished. |

### UnitTypeType

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
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
