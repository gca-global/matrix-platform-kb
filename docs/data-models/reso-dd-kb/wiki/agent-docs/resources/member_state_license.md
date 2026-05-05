[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `member_state_license` (MemberStateLicense)

> Supports members that hold multiple state licenses.

## At a glance

| | |
|---|---|
| **Primary key** | `member_state_license_key` |
| **Fields on dd.reso.org** | 10 |
| **Columns in canonical DBML** | 8 (omits 0 satellite drops + 1 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/MemberStateLicense/](https://dd.reso.org/DD2.0/MemberStateLicense/) |
| **Last revised upstream** | 6/17/2021 |

## Relationship diagram

```mermaid
flowchart LR
    member_state_license["member_state_license"]
    member["member"]
    member_state_license -->|"member_key"| member
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the MemberStateLicense record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `member_state_license` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `Member` | `member` | Resource |  | The member of the MemberStateLicense record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `MemberKey` | `member_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemMemberKey and OriginatingSystemMemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. This value may not be unique, specifically in the case of aggregation systems, this value should be the identifier from the original system. | Free-form text, up to 25 characters. |  |
| `MemberStateLicense` | `member_state_license` | String |  | The license of the Member. Separate multiple licenses with a comma and space. | Free-form text, up to 50 characters. |  |
| `MemberStateLicenseExpirationDate` | `member_state_license_expiration_date` | Date |  | The expiration date for the member's license. | Date (YYYY-MM-DD). |  |
| `MemberStateLicenseKey` | `member_state_license_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemMemberKey and OriginatingSystemMemberKey. | Unique key for this resource. Use as the FK target whenever another resource references `member_state_license`. | `pk` |
| `MemberStateLicenseState` | `member_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the member is licensed. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `MemberStateLicenseType` | `member_state_license_type` | enum | [`member_state_license_type`](../lookups.md#member_state_license_type) | The license type of the member. | Pick exactly one of 3 values from the lookup (closed list). |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the MemberStateLicense record was last modified. | ISO-8601 timestamp (UTC). |  |

## Foreign keys OUT (this resource references)

- `member_state_license.member_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `member_state_license`)

