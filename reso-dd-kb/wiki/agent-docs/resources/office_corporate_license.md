[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `office_corporate_license` (OfficeCorporateLicense)

> Supports offices that hold multiple state licenses.

## At a glance

| | |
|---|---|
| **Primary key** | `office_corporate_license_key` |
| **Fields on dd.reso.org** | 10 |
| **Columns in canonical DBML** | 6 (omits 2 satellite drops + 1 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 1 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/OfficeCorporateLicense/](https://dd.reso.org/DD2.0/OfficeCorporateLicense/) |
| **Last revised upstream** | 6/17/2021 |

## Relationship diagram

```mermaid
flowchart LR
    office_corporate_license["office_corporate_license"]
    office["office"]
    office_corporate_license -->|"office_key"| office
```

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the OfficeCorporateLicense record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `office_corporate_license` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the OfficeCorporateLicense record was last modified. | ISO-8601 timestamp (UTC). |  |
| `Office` | `office` | Resource |  | The Office of the OfficeCorporateLicense record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OfficeCorporateLicense` | `office_corporate_license` | String |  | When an office/firm is a corporation, an independent license number is issued. | Do not write. Phase-2.5 satellite of `OfficeKey`; the same value lives on the parent resource and is reachable via the `OfficeKey` FK. | `[dropped: satellite of office_key]` |
| `OfficeCorporateLicenseExpirationDate` | `office_corporate_license_expiration_date` | Date |  | The expiration date for the office corporation's license. | Date (YYYY-MM-DD). |  |
| `OfficeCorporateLicenseKey` | `office_corporate_license_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemMemberKey and OriginatingSystemMemberKey. | Unique key for this resource. Use as the FK target whenever another resource references `office_corporate_license`. | `pk` |
| `OfficeCorporateLicenseState` | `office_corporate_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the office corporation is licensed. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OfficeCorporateLicenseType` | `office_corporate_license_type` | enum | [`office_corporate_license_type`](../lookups.md#office_corporate_license_type) | The license type of the office corporation. | Pick exactly one of 2 values from the lookup (closed list). |  |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the Key is the system unique identifier from the system that the record was just retrieved. This may be identical to the related xxxId identifier, but the key is guaranteed unique for this record set. This is a foreign key relating to the Office resource's OfficeKey. | Foreign key -> `office.office_key`. Set this to the `office`'s `office_key` to link this row to its parent `office`. | `-> office.office_key` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. This value may not be unique, specifically in the case of aggregation systems, this value should be the identifier from the original system. | Do not write. Phase-2.5 satellite of `OfficeKey`; the same value lives on the parent resource and is reachable via the `OfficeKey` FK. | `[dropped: satellite of office_key]` |

## Foreign keys OUT (this resource references)

- `office_corporate_license.office_key` -> `office.office_key` (high)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `office_corporate_license`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `office_corporate_license` | `office_key` -> `office.office_corporate_license` | `drop_from_host` |  |
| `office_corporate_license_expiration_date` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_corporate_license_key` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_corporate_license_state` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_corporate_license_type` | `office_key` -> `office.?` | `keep_both` | no_child_match |
| `office_mls_id` | `office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |

