# `office_corporate_license` (OfficeCorporateLicense)

> Supports offices that hold multiple state licenses.

- Source: [https://dd.reso.org/DD2.0/OfficeCorporateLicense/](https://dd.reso.org/DD2.0/OfficeCorporateLicense/)
- Field count on dd.reso.org: **10**
- Primary key: `office_corporate_license_key`
- Last revised upstream: 6/17/2021

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of history items related to the OfficeCorporateLicense record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the OfficeCorporateLicense record was last modified. |  |
| `Office` | `office` | Resource |  | The Office of the OfficeCorporateLicense record. | `[Resource]` |
| `OfficeCorporateLicense` | `office_corporate_license` | String |  | When an office/firm is a corporation, an independent license number is issued. | `[dropped: satellite of office_key]` |
| `OfficeCorporateLicenseExpirationDate` | `office_corporate_license_expiration_date` | Date |  | The expiration date for the office corporation's license. |  |
| `OfficeCorporateLicenseKey` | `office_corporate_license_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `OfficeCorporateLicenseState` | `office_corporate_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the office corporation is licensed. |  |
| `OfficeCorporateLicenseType` | `office_corporate_license_type` | enum | [`office_corporate_license_type`](../lookups.md#office_corporate_license_type) | The license type of the office corporation. |  |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of office_key]` |

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

