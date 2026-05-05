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

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the MemberStateLicense record. | `[Collection]` |
| `Member` | `member` | Resource |  | The member of the MemberStateLicense record. | `[Resource]` |
| `MemberKey` | `member_key` | String |  | A unique identifier for this record from the immediate source. | `-> member.member_key` |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. |  |
| `MemberStateLicense` | `member_state_license` | String |  | The license of the Member. |  |
| `MemberStateLicenseExpirationDate` | `member_state_license_expiration_date` | Date |  | The expiration date for the member's license. |  |
| `MemberStateLicenseKey` | `member_state_license_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `MemberStateLicenseState` | `member_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the member is licensed. |  |
| `MemberStateLicenseType` | `member_state_license_type` | enum | [`member_state_license_type`](../lookups.md#member_state_license_type) | The license type of the member. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the MemberStateLicense record was last modified. |  |

## Foreign keys OUT (this resource references)

- `member_state_license.member_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `member_state_license`)

