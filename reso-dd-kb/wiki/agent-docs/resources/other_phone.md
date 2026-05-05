[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `other_phone` (OtherPhone)

> Additional phone numbers for contacts or members, with type information.

## At a glance

| | |
|---|---|
| **Primary key** | `other_phone_key` |
| **Fields on dd.reso.org** | 10 |
| **Columns in canonical DBML** | 9 (omits 0 satellite drops + 0 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/OtherPhone/](https://dd.reso.org/DD2.0/OtherPhone/) |
| **Last revised upstream** | 4/4/2023 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | Name of the class to which the record is referencing. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the OtherPhone record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the OtherPhone record was last modified. |  |
| `OtherPhoneExt` | `other_phone_ext` | String |  | The extension of the given phone number (if applicable). |  |
| `OtherPhoneKey` | `other_phone_key` | String |  | A system unique identifier. | `pk` |
| `OtherPhoneNumber` | `other_phone_number` | String |  | The phone option allowing members to convey additional phone numbers other than those already covered by the MemberMobilePhone, MemberFax and other specified fields. |  |
| `OtherPhoneType` | `other_phone_type` | enum | [`other_phone_type`](../lookups.md#other_phone_type) | The type of phone record that does not already exist in the given phone fields or if a second of any type of phone field is needed (i.e., HomePhone2, BrothersPhone, etc.). |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource or table of the listing or other record the media relates to (i.e., Property, Member, Office, etc.). |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `other_phone`)

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

