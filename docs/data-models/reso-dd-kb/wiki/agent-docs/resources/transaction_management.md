[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `transaction_management` (TransactionManagement)

> Tracking different types of transactions such as listing for sale or listing for lease.

## At a glance

| | |
|---|---|
| **Primary key** | `transaction_key` |
| **Fields on dd.reso.org** | 4 |
| **Columns in canonical DBML** | 4 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/TransactionManagement/](https://dd.reso.org/DD2.0/TransactionManagement/) |
| **Last revised upstream** | 2/24/2022 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the TransactionManagement record was last modified. | ISO-8601 timestamp (UTC). |  |
| `TransactionId` | `transaction_id` | String |  | The well-known identifier for the transaction record. The value may be identical to that of the TransactionKey, but the TransactionId is intended to be the value used by a human to retrieve the information about a specific transaction. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `TransactionKey` | `transaction_key` | String |  | A unique identifier for this record from the immediate source. A string that can include a Uniform Resource Identifier (URI) or other forms. Alternatively, use the TransactionKeyNumeric for a numeric-only key field. The local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemKey and OriginatingSystemKey. | Unique key for this resource. Use as the FK target whenever another resource references `transaction_management`. | `pk` |
| `TransactionType` | `transaction_type` | enum | [`transaction_type`](../lookups.md#transaction_type) | A list of types of transactions (e.g., Listing for Sale, Listing for Lease, Other). | Pick exactly one of 5 values from the lookup (closed list). |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`TransactionKey` vs `TransactionId`**:
  - `TransactionKey` - A unique identifier for this record from the immediate source.
  - `TransactionId` - The well-known identifier for the transaction record.

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

