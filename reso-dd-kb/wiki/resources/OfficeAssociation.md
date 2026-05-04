# OfficeAssociation

Joining information relating Office and Association records to each other.

**RESO DD 2.0** — 23 fields · last revised 7/25/2019 · [dd.reso.org](https://dd.reso.org/DD2.0/OfficeAssociation/)

**Adoption** — weighted Org%: **4%** across 6 measured fields (median 5%, avg 4%).

## Groups

- **Other** — 23 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `Association` | Resource |  |  |  | The Association of the OfficeAssociation record. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/Association/) |
| `AssociationKey` | String |  |  |  | The unique identifier for the association record. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/AssociationKey/) |
| `AssociationMlsId` | String |  |  |  | The local, well-known identifier for the association of REALTORS®. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/AssociationMlsId/) |
| `AssociationNationalAssociationId` | String |  |  |  | The national association ID of the association as known by the National Association of REALTORS®. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/AssociationNationalAssociationId/) |
| `BillStatus` | String |  |  | 5% | The status of the bill (i.e., Not Billed, Billed, Paid or N, B, P). | [link](https://dd.reso.org/DD2.0/OfficeAssociation/BillStatus/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/HistoryTransactional/) |
| `JoinDate` | Date |  |  | 5% | The date the office joined the association. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/JoinDate/) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/ModificationTimestamp/) |
| `Office` | Resource |  |  |  | The Office resource describes a brokerage office. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/Office/) |
| `OfficeAssociationPrimaryIndicator` | String List, Single |  | [OfficeAssociationPrimaryIndicator](#officeassociationprimaryindicator) |  | An indicator showing Primary, Secondary or Not Applicable with the association (i.e., P, S, X). | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OfficeAssociationPrimaryIndicator/) |
| `OfficeAssociationStatus` | String List, Single |  | [OfficeStatus](#officestatus) |  | The status of the office (i.e., Active, Inactive or Under Disciplinary Action). | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OfficeAssociationStatus/) |
| `OfficeAssociationStatusDate` | Date |  |  | 0% | The last time the status field was updated. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OfficeAssociationStatusDate/) |
| `OfficeKey` | String |  |  | 6% | A system-unique identifier for the office. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OfficeKey/) |
| `OfficeMlsId` | String |  |  | 0% | The local, well-known identifier for the office as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OfficeMlsId/) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  | The date/time the record was originally input into the source system. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the OfficeAssociation record. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OriginatingSystem/) |
| `OriginatingSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OriginatingSystemId/) |
| `OriginatingSystemMemberKey` | String |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OriginatingSystemMemberKey/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/OriginatingSystemName/) |
| `SourceSystem` | Resource |  |  |  | The source system of the OfficeAssociation record. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/SourceSystem/) |
| `SourceSystemId` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/SourceSystemId/) |
| `SourceSystemMemberKey` | String |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/SourceSystemMemberKey/) |
| `SourceSystemName` | String |  |  |  | The name of the immediate record provider. | [link](https://dd.reso.org/DD2.0/OfficeAssociation/SourceSystemName/) |

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

<details><summary><code>BillStatus</code></summary>

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

<details><summary><code>JoinDate</code></summary>

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

<details><summary><code>Office</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationPrimaryIndicator</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationStatus</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeAssociationStatusDate</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 7/25/2019
  - **Revision Date:** 7/25/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OfficeMlsId</code></summary>

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

### OfficeAssociationPrimaryIndicator

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OfficeAssociationPrimaryIndicator/)

| Value | Definition |
|---|---|
| `Not Applicable` | The office status as primary, secondary, etc., is not applicable. |
| `Primary` | The office is primary with the related association. |
| `Secondary` | The office is secondary with the related association. |
| `Tertiary` | The office is tertiary with the related association. |

### OfficeStatus

2 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OfficeStatus/)

| Value | Definition |
|---|---|
| `Active` | The member office's account is active. |
| `Inactive` | The member office's account is not active. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
