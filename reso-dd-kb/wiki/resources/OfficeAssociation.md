# OfficeAssociation

_RESO Data Dictionary 2.0 resource — 23 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/OfficeAssociation+Resource) for the canonical page._

**Adoption** — weighted Org%: **4%** across 6 measured fields (median 5%, avg 4%).

## Groups

- **Other** — 23 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `Association` | Resource |  |  |  |  | The Association of the OfficeAssociation record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135888) |
| `AssociationKey` | String |  |  |  |  | The unique identifier for the association record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135894) |
| `AssociationMlsId` | String |  |  |  |  | The local, well-known identifier for the association of REALTORS®. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135902) |
| `AssociationNationalAssociationId` | String |  |  |  |  | The national association ID of the association as known by the National Association of REALTORS®. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135907) |
| `BillStatus` | String |  |  |  | 5% | The status of the bill (i.e., Not Billed, Billed, Paid or N, B, P). | [link](https://ddwiki.reso.org/display/DDW20/BillStatus+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135918) |
| `JoinDate` | Date |  |  | 5% | 4% | The date the office joined the association. | [link](https://ddwiki.reso.org/display/DDW20/JoinDate+Field) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | 4% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135930) |
| `Office` | Resource |  |  |  |  | The Office resource describes a brokerage office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135937) |
| `OfficeAssociationPrimaryIndicator` | String List, Single |  | [OfficeAssociationPrimaryIndicator](#officeassociationprimaryindicator) |  |  | An indicator showing Primary, Secondary or Not Applicable with the association (i.e., P, S, X). | [link](https://ddwiki.reso.org/display/DDW20/OfficeAssociationPrimaryIndicator+Field) |
| `OfficeAssociationStatus` | String List, Single |  | [OfficeStatus](#officestatus) |  |  | The status of the office (i.e., Active, Inactive or Under Disciplinary Action). | [link](https://ddwiki.reso.org/display/DDW20/OfficeAssociationStatus+Field) |
| `OfficeAssociationStatusDate` | Date |  |  |  | 0% | The last time the status field was updated. | [link](https://ddwiki.reso.org/display/DDW20/OfficeAssociationStatusDate+Field) |
| `OfficeKey` | String |  |  | 10% | 4% | A system-unique identifier for the office. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135962) |
| `OfficeMlsId` | String |  |  |  | 0% | The local, well-known identifier for the office as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135968) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The date/time the record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135974) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the OfficeAssociation record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135980) |
| `OriginatingSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135986) |
| `OriginatingSystemMemberKey` | String |  |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135990) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135996) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the OfficeAssociation record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136003) |
| `SourceSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136010) |
| `SourceSystemMemberKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136017) |
| `SourceSystemName` | String |  |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136023) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>Association</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationMlsId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>JoinDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Office</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationPrimaryIndicator</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationStatus</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationStatusDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMlsId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

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

<details><summary><code>OriginatingSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

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

<details><summary><code>SourceSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

## Lookups

### OfficeAssociationPrimaryIndicator

| Value | Definition |
|---|---|
| `Not Applicable` | The office status as primary, secondary, etc., is not applicable. |
| `Primary` | The office is primary with the related association. |
| `Secondary` | The office is secondary with the related association. |
| `Tertiary` | The office is tertiary with the related association. |

### OfficeStatus

| Value | Definition |
|---|---|
| `Active` | The member office's account is active. |
| `Inactive` | The member office's account is not active. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
