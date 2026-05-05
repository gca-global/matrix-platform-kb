# `member_association` (MemberAssociation)

> Joining information relating Member and Association records to each other.

- Source: [https://dd.reso.org/DD2.0/MemberAssociation/](https://dd.reso.org/DD2.0/MemberAssociation/)
- Field count on dd.reso.org: **31**
- Primary key: `association_key`
- Note: PK chosen by override (RESO uses `AssociationKey` for this resource).
- Last revised upstream: 9/7/2023

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `Association` | `association` | Resource |  | The Association of the MemberAssociation record. | `[Resource]` |
| `AssociationKey` | `association_key` | String |  | The unique identifier for the association record. | `pk` `-> association.association_key` |
| `AssociationMlsId` | `association_mls_id` | String |  | The local, well-known identifier for the association of REALTORS®. |  |
| `AssociationNationalAssociationId` | `association_national_association_id` | String |  | The national association ID of the association as known by the national association. |  |
| `AssociationStaffYN` | `association_staff_yn` | Boolean |  | Determines whether or not the record is associated with an association employee. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the MemberAssociation record. | `[Collection]` |
| `Member` | `member` | Resource |  | The member of the MemberAssociation record. | `[Resource]` |
| `MemberAssociationBillStatus` | `member_association_bill_status` | enum | [`member_association_bill_status`](../lookups.md#member_association_bill_status) | The billing status of the member. |  |
| `MemberAssociationBillStatusDescription` | `member_association_bill_status_description` | String |  | The description of the billing status of the member. |  |
| `MemberAssociationDuesPaidDate` | `member_association_dues_paid_date` | Date |  | The last date the member paid dues. |  |
| `MemberAssociationJoinDate` | `member_association_join_date` | Date |  | The date the member joined the association. |  |
| `MemberAssociationModificationDateTime` | `member_association_modification_date_time` | Timestamp |  | The modification date for the record. |  |
| `MemberAssociationOrientationDate` | `member_association_orientation_date` | Date |  | The date the member underwent orientation with the association. |  |
| `MemberAssociationPrimaryIndicator` | `member_association_primary_indicator` | String |  | An indicator showing whether the member's association membership status is primary, secondary, or not applicable (i.e., P, S, X). |  |
| `MemberAssociationStatus` | `member_association_status` | enum | [`member_status`](../lookups.md#member_status) | States if the account is active, inactive or under disciplinary action. |  |
| `MemberAssociationStatusDate` | `member_association_status_date` | Date |  | The date of change of the member's status in relation to the association. |  |
| `MemberKey` | `member_key` | String |  | A unique identifier for this record from the immediate source. | `-> member.member_key` |
| `MemberLocalDuesWaivedYN` | `member_local_dues_waived_yn` | Boolean |  | Determines whether or not the member's association dues are waived at the local level. |  |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. |  |
| `MemberNationalDuesWaivedYN` | `member_national_dues_waived_yn` | Boolean |  | Determines whether or not the member's association dues are waived at the national level. |  |
| `MemberStatelDuesWaivedYN` | `member_statel_dues_waived_yn` | Boolean |  | Determines whether or not the member's association dues are waived at the state level. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the MemberAssociation record was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the MemberAssociation record. | `[Resource]` |
| `OriginatingSystemId` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the MemberAssociation record. | `[Resource]` |
| `SourceSystemId` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemMemberKey` | `source_system_member_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |

## Foreign keys OUT (this resource references)

- `member_association.association_key` -> `association.association_key` (medium)
- `member_association.member_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `member_association`)

