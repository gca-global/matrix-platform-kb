# `social_media` (SocialMedia)

> Social media accounts for members, offices, contacts and other entities.

- Source: [https://dd.reso.org/DD2.0/SocialMedia/](https://dd.reso.org/DD2.0/SocialMedia/)
- Field count on dd.reso.org: **10**
- Primary key: `social_media_key`
- Last revised upstream: 3/27/2026

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | Name of the class to which the record is referencing. |  |
| `DisplayName` | `display_name` | String |  | The display name for the field. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the SocialMedia record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the SocialMedia record was last modified. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource or table of the listing or other record that the media relates to (i.e., Property, Member, Office, etc.). |  |
| `ResourceRecordID` | `resource_record_id` | String |  | The well-known identifier of the related record from the source resource. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). |  |
| `SocialMediaKey` | `social_media_key` | String |  | A system unique identifier. | `pk` |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of sites or social media that a member Uniform Resource Locator (URL) or ID is referring to (e.g., Website, Blog, Facebook, Twitter, LinkedIn, Instagram). |  |
| `SocialMediaUrlOrId` | `social_media_url_or_id` | String |  | The website URL or ID of the social media site or account of the member. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `social_media`)

## Polymorphic FKs

- `resource_record_key` - target resolved at runtime; evidence: prose:P5:"foreign key from the resource selected in the ResourceName field"

