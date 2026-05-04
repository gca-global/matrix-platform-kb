# MemberAssociation

_RESO Data Dictionary 2.0 resource — 31 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/MemberAssociation+Resource) for the canonical page._

**Adoption** — weighted Org%: **3%** across 6 measured fields (median 5%, avg 3%).

## Groups

- **Other** — 31 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `Association` | Resource |  |  |  |  | The Association of the MemberAssociation record. | [link](https://ddwiki.reso.org/display/DDW20/Association+Field) |
| `AssociationKey` | String |  |  |  |  | The unique identifier for the association record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135889) |
| `AssociationMlsId` | String |  |  |  |  | The local, well-known identifier for the association of REALTORS®. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135895) |
| `AssociationNationalAssociationId` | String |  |  |  |  | The national association ID of the association as known by the national association. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135900) |
| `AssociationStaffYN` | Boolean |  |  |  |  | Determines whether or not the record is associated with an association employee. | [link](https://ddwiki.reso.org/display/DDW20/AssociationStaffYN+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135912) |
| `Member` | Resource |  |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://ddwiki.reso.org/display/DDW20/Member+Field) |
| `MemberAssociationBillStatus` | String List, Single |  | [MemberAssociationBillStatus](#memberassociationbillstatus) |  |  | The billing status of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationBillStatus+Field) |
| `MemberAssociationBillStatusDescription` | String |  |  |  |  | The description of the billing status of the member. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationBillStatusDescription+Field) |
| `MemberAssociationDuesPaidDate` | Date |  |  |  |  | The last date the member paid dues. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationDuesPaidDate+Field) |
| `MemberAssociationJoinDate` | Date |  |  |  |  | The date the member joined the association. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationJoinDate+Field) |
| `MemberAssociationModificationDateTime` | Timestamp |  |  |  |  | The modification date for the record. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationModificationDateTime+Field) |
| `MemberAssociationOrientationDate` | Date |  |  |  |  | The date the member underwent orientation with the association. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationOrientationDate+Field) |
| `MemberAssociationPrimaryIndicator` | String |  |  |  |  | An indicator showing whether the member's association membership status is primary, secondary, or not applicable (i.e., P, S, X). | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationPrimaryIndicator+Field) |
| `MemberAssociationStatus` | String List, Single |  | [MemberStatus](#memberstatus) |  | 0% | States if the account is active, inactive or under disciplinary action. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationStatus+Field) |
| `MemberAssociationStatusDate` | Date |  |  |  | 0% | The date of change of the member's status in relation to the association. | [link](https://ddwiki.reso.org/display/DDW20/MemberAssociationStatusDate+Field) |
| `MemberKey` | String |  |  | 10% | 4% | A system-unique identifier for the member. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135975) |
| `MemberLocalDuesWaivedYN` | Boolean |  |  |  |  | Determines whether or not the member's association dues are waived at the local level. | [link](https://ddwiki.reso.org/display/DDW20/MemberLocalDuesWaivedYN+Field) |
| `MemberMlsId` | String |  |  |  | 5% | The local, well-known identifier for the member as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135987) |
| `MemberNationalDuesWaivedYN` | Boolean |  |  |  |  | Determines whether or not the member's association dues are waived at the national level. | [link](https://ddwiki.reso.org/display/DDW20/MemberNationalDuesWaivedYN+Field) |
| `MemberStatelDuesWaivedYN` | Boolean |  |  |  |  | Determines whether or not the member's association dues are waived at the state level. | [link](https://ddwiki.reso.org/display/DDW20/MemberStatelDuesWaivedYN+Field) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | 4% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136005) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  |  | The date/time the record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136011) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the MemberAssociation record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136018) |
| `OriginatingSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136024) |
| `OriginatingSystemMemberKey` | String |  |  | 5% | 1% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136030) |
| `OriginatingSystemName` | String |  |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136035) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the MemberAssociation record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136041) |
| `SourceSystemId` | String |  |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136048) |
| `SourceSystemMemberKey` | String |  |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136052) |
| `SourceSystemName` | String |  |  |  |  | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1136058) |

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

<details><summary><code>AssociationNationalAssociationId</code></summary>

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

<details><summary><code>Member</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationBillStatus</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationBillStatusDescription</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationDuesPaidDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationJoinDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationModificationDateTime</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** SEP 07 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationOrientationDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationPrimaryIndicator</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationStatus</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationStatusDate</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberLocalDuesWaivedYN</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStatelDuesWaivedYN</code></summary>

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

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JUL 25 2019
  - **Revision Date:** JUL 25 2019
  - **Added in Version:** 2.0.0

</details>

## Lookups

### MemberAssociationBillStatus

| Value | Definition |
|---|---|
| `Billed` | The member has been billed by an association of REALTORS®. |
| `Not Billed` | The member has not been billed by an association of REALTORS®. |
| `Paid` | The member has paid an association of REALTORS®. |

### MemberStatus

| Value | Definition |
|---|---|
| `Active` | The member's account is active. |
| `Inactive` | the member's account is not active. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
