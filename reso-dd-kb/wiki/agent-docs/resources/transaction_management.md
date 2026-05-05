# `transaction_management` (TransactionManagement)

> Tracking different types of transactions such as listing for sale or listing for lease.

- Source: [https://dd.reso.org/DD2.0/TransactionManagement/](https://dd.reso.org/DD2.0/TransactionManagement/)
- Field count on dd.reso.org: **4**
- Primary key: `transaction_key`
- Last revised upstream: 2/24/2022

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the TransactionManagement record was last modified. |  |
| `TransactionId` | `transaction_id` | String |  | The well-known identifier for the transaction record. |  |
| `TransactionKey` | `transaction_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `TransactionType` | `transaction_type` | enum | [`transaction_type`](../lookups.md#transaction_type) | A list of types of transactions (e.g., Listing for Sale, Listing for Lease, Other). |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

