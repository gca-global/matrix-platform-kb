[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `ouid` (OUID)

> Organization Unique Identifier (UOI), a common ID system for organizations that exchange real estate data.

## At a glance

| | |
|---|---|
| **Primary key** | `organization_unique_id_key` *(override; RESO uses `OrganizationUniqueIdKey`)* |
| **Fields on dd.reso.org** | 46 |
| **Columns in canonical DBML** | 42 (omits 0 satellite drops + 1 `Resource`-typed + 3 `Collection`-typed) |
| **Foreign keys OUT / IN** | 2 / 11 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/OUID/](https://dd.reso.org/DD2.0/OUID/) |
| **Last revised upstream** | 9/1/2017 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ChangedByMember` | `changed_by_member` | Resource |  | The member who made the changes to the OUID record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `ChangedByMemberID` | `changed_by_member_id` | String |  | The local, well-know identifier of the member (user) who made the change. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `ChangedByMemberKey` | `changed_by_member_key` | String |  | The unique identifier of the member (user) who made the change. This is a foreign key relating to the Member Resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the OUID record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `ouid` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `Media` | `media` | Collection |  | The media associated with the OUID record. | Inverse 1:N: read as 'all `media` rows that point at this `ouid` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the OUID record was last modified. | ISO-8601 timestamp (UTC). |  |
| `OrganizationAOR` | `organization_aor` | enum | [`aor`](../lookups.md#aor) | The organization's primary local board or association of REALTORS®, if applicable. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OrganizationAddress1` | `organization_address1` | String |  | The street number, direction, name and suffix of the organization. | Free-form text, up to 50 characters. |  |
| `OrganizationAddress2` | `organization_address2` | String |  | The unit/suite number of the organization. | Free-form text, up to 50 characters. |  |
| `OrganizationAorOuid` | `organization_aor_ouid` | String |  | The Unique Organization Identifier (UOI) for the organization's association of REALTORS®, if applicable. | Free-form text, up to 25 characters. |  |
| `OrganizationAorOuidKey` | `organization_aor_ouid_key` | String |  | The OrganizationUniqueIdKey of the association of REALTORS® from the system serving the Unique Organization Identifier (UOI) resource. | Free-form text, up to 255 characters. |  |
| `OrganizationCarrierRoute` | `organization_carrier_route` | String |  | The group of addresses to which the United States Postal Service (USPS) assigns the same code to aid in mail delivery. For the USPS, these codes are 9 digits: 5 numbers for the ZIP Code, one letter for the carrier route type and 3 numbers for the carrier route number. | Free-form text, up to 9 characters. |  |
| `OrganizationCity` | `organization_city` | String |  | The city of the organization. | Free-form text, up to 50 characters. |  |
| `OrganizationComments` | `organization_comments` | String |  | Comments or notes about the organization. | Free-form text, up to 500 characters. |  |
| `OrganizationContactEmail` | `organization_contact_email` | String |  | The email address of the organization contact. | Free-form text, up to 80 characters. |  |
| `OrganizationContactFax` | `organization_contact_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `OrganizationContactFirstName` | `organization_contact_first_name` | String |  | The first name of the organization contact. | Free-form text, up to 50 characters. |  |
| `OrganizationContactFullName` | `organization_contact_full_name` | String |  | The first, middle and last name of the organization contact. | Free-form text, up to 150 characters. |  |
| `OrganizationContactJobTitle` | `organization_contact_job_title` | String |  | The title or position of the organization contact. | Free-form text, up to 50 characters. |  |
| `OrganizationContactLastName` | `organization_contact_last_name` | String |  | The last name of the organization contact. | Free-form text, up to 50 characters. |  |
| `OrganizationContactMiddleName` | `organization_contact_middle_name` | String |  | The middle name of the organization contact. | Free-form text, up to 50 characters. |  |
| `OrganizationContactNamePrefix` | `organization_contact_name_prefix` | String |  | Prefix to the name of the organization contact. (e.g., Dr., Mr., Ms.). | Free-form text, up to 10 characters. |  |
| `OrganizationContactNameSuffix` | `organization_contact_name_suffix` | String |  | Suffix to the surname (e.g., Esq., Jr., III) of the organization contact. | Free-form text, up to 10 characters. |  |
| `OrganizationContactPhone` | `organization_contact_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `OrganizationContactPhoneExt` | `organization_contact_phone_ext` | String |  | The extension of the given phone number, if applicable. | Free-form text, up to 10 characters. |  |
| `OrganizationCountry` | `organization_country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. | Pick exactly one of 246 values from the lookup (closed list). |  |
| `OrganizationCountyOrParish` | `organization_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the organization is addressed. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OrganizationMemberCount` | `organization_member_count` | Number |  | The total number of active members in the organization, if applicable. | Numeric (integer). |  |
| `OrganizationMlsCode` | `organization_mls_code` | String |  | If the organization is an MLS, it is likely that it already has an ID or code based on its name or an abbreviation. This field supports the continued use/reference to that legacy code. | Free-form text, up to 25 characters. |  |
| `OrganizationMlsVendorName` | `organization_mls_vendor_name` | String |  | If the organization uses an MLS system, this is the textual name of the vendor. | Free-form text, up to 255 characters. |  |
| `OrganizationMlsVendorOuid` | `organization_mls_vendor_ouid` | String |  | If the organization uses an MLS system, this is that vendor's Unique Organization Identifier (UOI). | Free-form text, up to 25 characters. |  |
| `OrganizationName` | `organization_name` | String |  | The textual name of the organization represented by a given Unique Organization Identifier (UOI) record. | Free-form text, up to 255 characters. |  |
| `OrganizationNationalAssociationId` | `organization_national_association_id` | String |  | The national association ID of the organization, if applicable (e.g., in the U.S., this is the NRDS number). | Free-form text, up to 25 characters. |  |
| `OrganizationPostalCode` | `organization_postal_code` | String |  | The postal code of the organization. | Free-form text, up to 10 characters. |  |
| `OrganizationPostalCodePlus4` | `organization_postal_code_plus4` | String |  | The four-digit extension of the U.S. Zip Code. | Free-form text, up to 4 characters. |  |
| `OrganizationSocialMedia` | `organization_social_media` | Collection |  | A collection of the types of social media fields available for this organization. The collection includes the type of system and other details pertinent about social media | Inverse 1:N: read as 'all `social_media` rows that point at this `ouid` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `OrganizationSocialMediaType` | `organization_social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of sites or social media that the organization Uniform Resource Locator (URL) or ID is referring to (e.g., website, blog, Facebook, Twitter, LinkedIn, Instagram). | Pick exactly one of 17 values from the lookup (closed list). |  |
| `OrganizationStateLicense` | `organization_state_license` | String |  | The license of the organization, if applicable. Multiple licenses should be separated with a comma and space. | Free-form text, up to 50 characters. |  |
| `OrganizationStateLicenseState` | `organization_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the organization is licensed, if applicable. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OrganizationStateOrProvince` | `organization_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the organization is addressed. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OrganizationStatus` | `organization_status` | Boolean |  | Determines whether or not if the organization is active or inactive. Active organizations are marked by a 1 and inactive organizations are marked by a 0. This field is not nullable. | Boolean. |  |
| `OrganizationStatusChangeTimestamp` | `organization_status_change_timestamp` | Timestamp |  | The date/time of when the organization status was last changed. | ISO-8601 timestamp (UTC). |  |
| `OrganizationType` | `organization_type` | enum | [`organization_type`](../lookups.md#organization_type) | The type of organization (i.e., MLS, vendor, association, etc.). This is not a substitute or alternative for the Office resource; however, it may be that a brokerage has a record in this table for a nonlisting purpose. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OrganizationUniqueId` | `organization_unique_id` | String |  | This is the unique ID assigned to organizations included in the OUID resource. Assignment of Unique Organization Identifier (UOI) numbers will be centralized and may not be created by systems hosting the OUID resource. Contact info@reso.org for information on obtaining a UOI number. | Free-form text, up to 25 characters. |  |
| `OrganizationUniqueIdKey` | `organization_unique_id_key` | String |  | The key field used by the system hosting a table of Unique Organization Identifiers (UOIs). This key is likely to be unique to each hosting system and is not meant to be a universal ID for an organization, but rather a key used by clients of the hosting system. The actual UOI is the Organization Unique ID field. | Unique key for this resource. Use as the FK target whenever another resource references `ouid`. | `pk` |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the organization record was originally input into the source system. | ISO-8601 timestamp (UTC). |  |

## Foreign keys OUT (this resource references)

- `ouid.changed_by_member_id` -> `member.member_key` (medium)
- `ouid.changed_by_member_key` -> `member.member_key` (high)

## Foreign keys IN (other resources reference this)

- `contacts.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `contacts.source_system_id` -> `ouid.organization_unique_id_key` (medium)
- `history_transactional.originating_system_id` -> `ouid.organization_unique_id` (medium)
- `history_transactional.source_system_id` -> `ouid.organization_unique_id` (medium)
- `media.source_system_id` -> `ouid.organization_unique_id_key` (medium)
- `member.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `member.source_system_id` -> `ouid.organization_unique_id_key` (medium)
- `office.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `office.source_system_id` -> `ouid.organization_unique_id_key` (medium)
- `property.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `property.source_system_id` -> `ouid.organization_unique_id_key` (medium)

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `ouid`)
- `media` -> `media` (many `media` per `ouid`)
- `organization_social_media` -> `social_media` (many `social_media` per `ouid`)

