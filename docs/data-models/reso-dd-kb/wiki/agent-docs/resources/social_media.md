[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `social_media` (SocialMedia)

> Social media accounts for members, offices, contacts and other entities.

## At a glance

| | |
|---|---|
| **Primary key** | `social_media_key` |
| **Fields on dd.reso.org** | 10 |
| **Columns in canonical DBML** | 9 (omits 0 satellite drops + 0 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/SocialMedia/](https://dd.reso.org/DD2.0/SocialMedia/) |
| **Last revised upstream** | 3/27/2026 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | Name of the class to which the record is referencing. | Pick exactly one of 17 values from the lookup (closed list). |  |
| `DisplayName` | `display_name` | String |  | The display name for the field. SHOULD be provided in all cases where the use of display names is needed, even if the display name is the same as the underlying field name. The DisplayName MAY be a RESO Standard Display Name or a local one. | Free-form text. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the SocialMedia record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `social_media` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the SocialMedia record was last modified. | ISO-8601 timestamp (UTC). |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource or table of the listing or other record that the media relates to (i.e., Property, Member, Office, etc.). | Pick exactly one of 5 values from the lookup (closed list). |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. The value may be identical to that of the Listing Key, but the Listing ID is intended to be the value used by a human to retrieve the information about a specific listing. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). The system being connected to, not necessarily the original source of the record. A foreign key from the resource selected in the ResourceName field. | Polymorphic key. Resolve the target resource at write time from the row's context (see Definition); store the chosen target's PK in this column. |  |
| `SocialMediaKey` | `social_media_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the key is the system unique identifier from the system that the record was just retrieved. This may be identical to the related xxxId identifier, but the key is guaranteed unique for this record set. | Unique key for this resource. Use as the FK target whenever another resource references `social_media`. | `pk` |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of sites or social media that a member Uniform Resource Locator (URL) or ID is referring to (e.g., Website, Blog, Facebook, Twitter, LinkedIn, Instagram). | Pick exactly one of 17 values from the lookup (closed list). |  |
| `SocialMediaUrlOrId` | `social_media_url_or_id` | String |  | The website URL or ID of the social media site or account of the member. | Free-form text, up to 8000 characters. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `social_media`)

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

