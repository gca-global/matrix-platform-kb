# MemberAssociation

Joining information relating Member and Association records to each other.

**RESO DD 2.0** — 31 fields · last revised 9/7/2023 · [dd.reso.org](https://dd.reso.org/DD2.0/MemberAssociation/)

**Adoption** — weighted Org%: **3%** across 6 measured fields (median 5%, avg 3%).

## Groups

- **Other** — 31 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `Association` | Resource |  |  |  | The Association of the MemberAssociation record. | [link](https://dd.reso.org/DD2.0/MemberAssociation/Association/) |
| `AssociationKey` | String |  |  |  | The unique identifier for the association record. | [link](https://dd.reso.org/DD2.0/MemberAssociation/AssociationKey/) |
| `AssociationMlsId` | String |  |  |  | The local, well-known identifier for the association of REALTORS®. | [link](https://dd.reso.org/DD2.0/MemberAssociation/AssociationMlsId/) |
| `AssociationNationalAssociationId` | String |  |  |  | The national association ID of the association as known by the national association. | [link](https://dd.reso.org/DD2.0/MemberAssociation/AssociationNationalAssociationId/) |
| `AssociationStaffYN` | Boolean |  |  |  | Determines whether or not the record is associated with an association employee. | [link](https://dd.reso.org/DD2.0/MemberAssociation/AssociationStaffYN/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/MemberAssociation/HistoryTransactional/) |
| `Member` | Resource |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://dd.reso.org/DD2.0/MemberAssociation/Member/) |
| `MemberAssociationBillStatus` | String List, Single |  | [MemberAssociationBillStatus](#memberassociationbillstatus) |  | The billing status of the member. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationBillStatus/) |
| `MemberAssociationBillStatusDescription` | String |  |  |  | The description of the billing status of the member. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationBillStatusDescription/) |
| `MemberAssociationDuesPaidDate` | Date |  |  |  | The last date the member paid dues. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationDuesPaidDate/) |
| `MemberAssociationJoinDate` | Date |  |  |  | The date the member joined the association. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationJoinDate/) |
| `MemberAssociationModificationDateTime` | Timestamp |  |  |  | The modification date for the record. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationModificationDateTime/) |
| `MemberAssociationOrientationDate` | Date |  |  |  | The date the member underwent orientation with the association. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationOrientationDate/) |
| `MemberAssociationPrimaryIndicator` | String |  |  |  | An indicator showing whether the member's association membership status is primary, secondary, or not applicable (i.e., P, S, X). | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationPrimaryIndicator/) |
| `MemberAssociationStatus` | String List, Single |  | [MemberStatus](#memberstatus) | 0% | States if the account is active, inactive or under disciplinary action. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationStatus/) |
| `MemberAssociationStatusDate` | Date |  |  | 0% | The date of change of the member's status in relation to the association. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberAssociationStatusDate/) |
| `MemberKey` | String |  |  | 6% | A system-unique identifier for the member. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberKey/) |
| `MemberLocalDuesWaivedYN` | Boolean |  |  |  | Determines whether or not the member's association dues are waived at the local level. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberLocalDuesWaivedYN/) |
| `MemberMlsId` | String |  |  | 5% | The local, well-known identifier for the member as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberMlsId/) |
| `MemberNationalDuesWaivedYN` | Boolean |  |  |  | Determines whether or not the member's association dues are waived at the national level. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberNationalDuesWaivedYN/) |
| `MemberStatelDuesWaivedYN` | Boolean |  |  |  | Determines whether or not the member's association dues are waived at the state level. | [link](https://dd.reso.org/DD2.0/MemberAssociation/MemberStatelDuesWaivedYN/) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/MemberAssociation/ModificationTimestamp/) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  | The date/time the record was originally input into the source system. | [link](https://dd.reso.org/DD2.0/MemberAssociation/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the MemberAssociation record. | [link](https://dd.reso.org/DD2.0/MemberAssociation/OriginatingSystem/) |
| `OriginatingSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/MemberAssociation/OriginatingSystemId/) |
| `OriginatingSystemMemberKey` | String |  |  | 1% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/MemberAssociation/OriginatingSystemMemberKey/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/MemberAssociation/OriginatingSystemName/) |
| `SourceSystem` | Resource |  |  |  | The source system of the MemberAssociation record. | [link](https://dd.reso.org/DD2.0/MemberAssociation/SourceSystem/) |
| `SourceSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/MemberAssociation/SourceSystemId/) |
| `SourceSystemMemberKey` | String |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/MemberAssociation/SourceSystemMemberKey/) |
| `SourceSystemName` | String |  |  |  | The name of the immediate record provider. | [link](https://dd.reso.org/DD2.0/MemberAssociation/SourceSystemName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>Association</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationMlsId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationNationalAssociationId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AssociationStaffYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

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

<details><summary><code>MemberAssociationBillStatus</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationBillStatusDescription</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationDuesPaidDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationJoinDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationModificationDateTime</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 9/7/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationOrientationDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationPrimaryIndicator</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationStatus</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberAssociationStatusDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberLocalDuesWaivedYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberNationalDuesWaivedYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MemberStatelDuesWaivedYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemMemberKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemId</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemMemberKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

## Lookups

### MemberAssociationBillStatus

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/MemberAssociationBillStatus/)

| Value | Definition |
|---|---|
| `Billed` | The member has been billed by an association of REALTORS®. |
| `Not Billed` | The member has not been billed by an association of REALTORS®. |
| `Paid` | The member has paid an association of REALTORS®. |

### MemberStatus

2 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/MemberStatus/)

| Value | Definition |
|---|---|
| `Active` | The member's account is active. |
| `Inactive` | the member's account is not active. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
