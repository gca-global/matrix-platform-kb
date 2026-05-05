# `contact_listings` (ContactListings)

> Maintains the relationship between contacts and members around listings in consumer portals.

- Source: [https://dd.reso.org/DD2.0/ContactListings/](https://dd.reso.org/DD2.0/ContactListings/)
- Field count on dd.reso.org: **22**
- Primary key: `contact_listings_key`
- Last revised upstream: 9/26/2017

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `AgentNotesUnreadYN` | `agent_notes_unread_yn` | Boolean |  | Indicates whether or not agent notes have gone unread. |  |
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | The name of the class where the listing record is located. |  |
| `Contact` | `contact` | Resource |  | The contact for the ContactListings record. | `[Resource]` |
| `ContactKey` | `contact_key` | String |  | The foreign key relating to the Contacts Resource. | `-> contacts.contact_key` |
| `ContactListingPreference` | `contact_listing_preference` | enum | [`contact_listing_preference`](../lookups.md#contact_listing_preference) | The contact's preference selection on the given listing (i.e., Favorite, Possibility or Discard). |  |
| `ContactListingsKey` | `contact_listings_key` | String |  | A system unique identifier. | `pk` |
| `ContactLoginId` | `contact_login_id` | String |  | The foreign key referring to the Contacts Resource's local, well-known identifier for the contact. | `[dropped: satellite of contact_key]` |
| `ContactNotesUnreadYN` | `contact_notes_unread_yn` | Boolean |  | A flag indicating whether or not the contact's notes are unread. |  |
| `DirectEmailYN` | `direct_email_yn` | Boolean |  | A flag indicating whether or not this is a direct email. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the ContactListings record. | `[Collection]` |
| `LastAgentNoteTimestamp` | `last_agent_note_timestamp` | Timestamp |  | The date/time the member last added or updated a ListingNote. |  |
| `LastContactNoteTimestamp` | `last_contact_note_timestamp` | Timestamp |  | The date/time the contact last added or updated a ListingNote. |  |
| `Listing` | `listing` | Resource |  | The listing for the ContactListings record. | `[Resource]` |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing. |  |
| `ListingKey` | `listing_key` | String |  | The foreign key related to the Property Resource's unique identifier for this record from the immediate source. | `-> property.listing_key` |
| `ListingModificationTimestamp` | `listing_modification_timestamp` | Timestamp |  | The last time the listing was updated. |  |
| `ListingNotes` | `listing_notes` | Collection |  | The notes input by the member and/or contact in reference to the given listing. | `[Collection]` |
| `ListingSentTimestamp` | `listing_sent_timestamp` | Timestamp |  | The date/time the listing was sent to the contact. |  |
| `ListingViewedYN` | `listing_viewed_yn` | Boolean |  | Indicates whether or not a listing has been viewed. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the ContactListing record was last modified. |  |
| `PortalLastVisitedTimestamp` | `portal_last_visited_timestamp` | Timestamp |  | The date/time the listing was last viewed by the contact. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The name of the resource where the listing record is located. |  |

## Foreign keys OUT (this resource references)

- `contact_listings.contact_key` -> `contacts.contact_key` (medium)
- `contact_listings.listing_key` -> `property.listing_key` (medium)

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `contact_listings`)
- `listing_notes` -> `contact_listing_notes` (many `contact_listing_notes` per `contact_listings`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `contact_listing_preference` | `contact_key` -> `contacts.?` | `keep_both` | no_child_match |
| `contact_listings_key` | `contact_key` -> `contacts.?` | `keep_both` | no_child_match |
| `contact_login_id` | `contact_key` -> `contacts.contact_login_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `contact_notes_unread_yn` | `contact_key` -> `contacts.?` | `keep_both` | no_child_match |

