# PropertyGreenVerification

_RESO Data Dictionary 2.0 resource — 15 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/PropertyGreenVerification+Resource) for the canonical page._

**Adoption** — weighted Org%: **1%** across 13 measured fields (median 1%, avg 1%).

## Groups

- **Other** — 15 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `GreenBuildingVerificationKey` | String |  |  | 20% | 1% | A unique identifier for this record. | [link](https://ddwiki.reso.org/display/DDW20/GreenBuildingVerificationKey+Field) |
| `GreenBuildingVerificationType` | String List, Single |  | [GreenBuildingVerificationType](#greenbuildingverificationtype) | 20% | 1% | The name of the verification or certification awarded to a new or pre-existing residential or commercial structure (e.g., LEED, ENERGY STAR, ICC-700). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135745) |
| `GreenVerificationBody` | String |  |  | 5% | 1% | The name of the body or group providing the verification/certification/rating named in the GreenBuildingVerificationType field. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationBody+Field) |
| `GreenVerificationMetric` | Number |  |  | 15% | 1% | A final score indicating the performance of energy efficiency design and measures in the home as tested by a third-party rater. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationMetric+Field) |
| `GreenVerificationRating` | String |  |  | 10% | 1% | Many verifications or certifications have a rating system that provides an indication of the structure's level of energy efficiency. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationRating+Field) |
| `GreenVerificationSource` | String List, Single |  | [GreenVerificationSource](#greenverificationsource) |  | 1% | The source of the green data. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationSource+Field) |
| `GreenVerificationStatus` | String List, Single |  | [GreenVerificationStatus](#greenverificationstatus) | 10% | 1% | Many verification programs include a multistep process that may begin with plans and specs, involve testing and/or submission of building specifications along the way, and include a final verification step. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationStatus+Field) |
| `GreenVerificationURL` | String |  |  | 10% | 1% | Provides a link to the specific property’s high-performance rating or scoring details directly from and hosted by the sponsoring body of the program. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationURL+Field) |
| `GreenVerificationVersion` | String |  |  | 10% | 1% | The version of the green certification or verification that was awarded. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationVersion+Field) |
| `GreenVerificationYear` | Number |  |  | 10% | 1% | The year the green certification or verification was awarded. | [link](https://ddwiki.reso.org/display/DDW20/GreenVerificationYear+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135803) |
| `Listing` | Resource |  |  |  |  | The listing associated with the PropertyGreenVerification record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135809) |
| `ListingId` | String |  |  | 5% | 1% | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135815) |
| `ListingKey` | String |  |  | 20% | 1% | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135821) |
| `ModificationTimestamp` | Timestamp |  |  | 20% | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135827) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>GreenBuildingVerificationKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Verificación de Edificio Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 09 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenBuildingVerificationType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Verificación de Edificio Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** APR 11 2022
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationBody</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estructura de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationMetric</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Métrica de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationRating</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clasificación de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationURL</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** URL de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationVersion</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Versión de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenVerificationYear</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Año de Verificación Verde
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

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
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### GreenBuildingVerificationType

| Value | Definition |
|---|---|
| `Certified Passive House` | Super-insulated new homes that have been built to meet certification requirements demonstrating minimal or no heating and cooling system. |
| `ENERGY STAR Certified Homes` | EPA ENERGY STAR Certified Homes is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to upgrade a new home's energy efficiency beyond minimum code requirements. |
| `EnerPHit` | Super-insulated existing homes that have been remodeled to meet certification requirements demonstrating minimal or no heating and cooling system. |
| `HERS Index Score` | The HERS Index is a nationally recognized scoring system for measuring a home's energy performance in the U.S. |
| `Home Energy Score` | The Home Energy Score, managed by the U.S. |
| `Home Energy Upgrade Certificate of Energy Efficiency Improvements` | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU). |
| `Home Energy Upgrade Certificate of Energy Efficiency Performance` | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU) and provides one or more measures of a home's performance. |
| `Home Performance with ENERGY STAR` | Home Performance with ENERGY STAR (HPwES) offers whole-house solutions to high energy bills and homes with comfort problems. |
| `Indoor airPLUS` | Indoor airPLUS from the U.S. |
| `LEED For Homes` | The U.S. |
| `Living Building Challenge` | The International Living Future Institute third-party certification that proves that a home produces as much or more energy than is used. |
| `NGBS New Construction` | Home Innovation Research Labs certifies homes to the ICC-700 National Green Building Standard (NGBS), which has undergone the full consensus process and received approval from the American National Standards Institute (ANSI). |
| `NGBS Small Projects Remodel` | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| `NGBS Whole-Home Remodel` | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| `Pearl Certification` | Pearl is a national firm that provides third-party certification of high-performing homes (residential, 1-4 units) at various levels. |
| `PHIUS+` | Super-insulated homes that have met certification requirements demonstrating minimal or no heating and cooling system. |
| `WaterSense` | EPA WaterSense is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to ensure a home uses less water while still providing the same level of comfort and convenience. |
| `Zero Energy Ready Home` | DOE Zero Energy Ready Home is a set of optional construction practices and technologies (above minimum code and ENERGY STAR Certified Home requirements) that builders can follow to ensure high-performance homes that are so energy efficient that all or most annual energy consumption can be offset with renewable energy. |

### GreenVerificationSource

| Value | Definition |
|---|---|
| `Administrator` | An administrator such as a utility, governmental entity, etc. |
| `Assessor` | The assessor provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Builder` | The builder provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Contractor or Installer` | The contractor or installer provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Other` | Data such as photovoltaic characteristics, or a verified score, certification, label, etc. |
| `Owner` | The owner provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Program Sponsor` | The program sponsor provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Program Verifier` | The program verifier hired as a third-party provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `Public Records` | Data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| `See Remarks` | See remarks for information about the source of data, such as photovoltaic characteristics or a verified score, certification, label, etc. |

### GreenVerificationStatus

| Value | Definition |
|---|---|
| `Complete` | Indicates that the verification process is complete. |
| `In Process` | Indicates that the verification process is underway but not complete. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
