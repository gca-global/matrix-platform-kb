# `office_association` (OfficeAssociation)

> Joining information relating Office and Association records to each other.

- Source: [https://dd.reso.org/DD2.0/OfficeAssociation/](https://dd.reso.org/DD2.0/OfficeAssociation/)
- Field count on dd.reso.org: **23**
- Primary key: `association_key`
- Note: PK chosen by override (RESO uses `AssociationKey` for this resource).
- Last revised upstream: 7/25/2019

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `Association` | `association` | Resource |  | The Association of the OfficeAssociation record. | `[Resource]` |
| `AssociationKey` | `association_key` | String |  | The unique identifier for the association record. | `pk` `-> association.association_key` |
| `AssociationMlsId` | `association_mls_id` | String |  | The local, well-known identifier for the association of REALTORS®. |  |
| `AssociationNationalAssociationId` | `association_national_association_id` | String |  | The national association ID of the association as known by the National Association of REALTORS®. |  |
| `BillStatus` | `bill_status` | String |  | The status of the bill (i.e., Not Billed, Billed, Paid or N, B, P). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the OfficeAssociation record. | `[Collection]` |
| `JoinDate` | `join_date` | Date |  | The date the office joined the association. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the OfficeAssociation record was last modified. |  |
| `Office` | `office` | Resource |  | The office of the OfficeAssociation record. | `[Resource]` |
| `OfficeAssociationPrimaryIndicator` | `office_association_primary_indicator` | enum | [`office_association_primary_indicator`](../lookups.md#office_association_primary_indicator) | An indicator showing Primary, Secondary or Not Applicable with the association (i.e., P, S, X). |  |
| `OfficeAssociationStatus` | `office_association_status` | enum | [`office_status`](../lookups.md#office_status) | The status of the office (i.e., Active, Inactive or Under Disciplinary Action). |  |
| `OfficeAssociationStatusDate` | `office_association_status_date` | Date |  | The last time the status field was updated. |  |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of office_key]` |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the OfficeAssociation record. | `[Resource]` |
| `OriginatingSystemId` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the OfficeAssociation record. | `[Resource]` |
| `SourceSystemId` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemMemberKey` | `source_system_member_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |

## Foreign keys OUT (this resource references)

- `office_association.association_key` -> `association.association_key` (medium)
- `office_association.office_key` -> `office.office_key` (high)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `office_association`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `office_association_primary_indicator` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_association_status` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_association_status_date` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_mls_id` | `office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |

