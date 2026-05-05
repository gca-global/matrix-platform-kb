# `ouid` (OUID)

> Organization Unique Identifier (UOI), a common ID system for organizations that exchange real estate data.

- Source: [https://dd.reso.org/DD2.0/OUID/](https://dd.reso.org/DD2.0/OUID/)
- Field count on dd.reso.org: **46**
- Primary key: `organization_unique_id_key`
- Note: PK chosen by override (RESO uses `OrganizationUniqueIdKey` for this resource).
- Last revised upstream: 9/1/2017

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ChangedByMember` | `changed_by_member` | Resource |  | The member who made the changes to the OUID record. | `[Resource]` |
| `ChangedByMemberID` | `changed_by_member_id` | String |  | The local, well-know identifier of the member (user) who made the change. | `-> member.member_key` |
| `ChangedByMemberKey` | `changed_by_member_key` | String |  | The unique identifier of the member (user) who made the change. | `-> member.member_key` |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the OUID record. | `[Collection]` |
| `Media` | `media` | Collection |  | The media associated with the OUID record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the OUID record was last modified. |  |
| `OrganizationAOR` | `organization_aor` | enum | [`aor`](../lookups.md#aor) | The organization's primary local board or association of REALTORS®, if applicable. |  |
| `OrganizationAddress1` | `organization_address1` | String |  | The street number, direction, name and suffix of the organization. |  |
| `OrganizationAddress2` | `organization_address2` | String |  | The unit/suite number of the organization. |  |
| `OrganizationAorOuid` | `organization_aor_ouid` | String |  | The Unique Organization Identifier (UOI) for the organization's association of REALTORS®, if applicable. |  |
| `OrganizationAorOuidKey` | `organization_aor_ouid_key` | String |  | The OrganizationUniqueIdKey of the association of REALTORS® from the system serving the Unique Organization Identifier (UOI) resource. |  |
| `OrganizationCarrierRoute` | `organization_carrier_route` | String |  | The group of addresses to which the United States Postal Service (USPS) assigns the same code to aid in mail delivery. |  |
| `OrganizationCity` | `organization_city` | String |  | The city of the organization. |  |
| `OrganizationComments` | `organization_comments` | String |  | Comments or notes about the organization. |  |
| `OrganizationContactEmail` | `organization_contact_email` | String |  | The email address of the organization contact. |  |
| `OrganizationContactFax` | `organization_contact_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `OrganizationContactFirstName` | `organization_contact_first_name` | String |  | The first name of the organization contact. |  |
| `OrganizationContactFullName` | `organization_contact_full_name` | String |  | The first, middle and last name of the organization contact. |  |
| `OrganizationContactJobTitle` | `organization_contact_job_title` | String |  | The title or position of the organization contact. |  |
| `OrganizationContactLastName` | `organization_contact_last_name` | String |  | The last name of the organization contact. |  |
| `OrganizationContactMiddleName` | `organization_contact_middle_name` | String |  | The middle name of the organization contact. |  |
| `OrganizationContactNamePrefix` | `organization_contact_name_prefix` | String |  | Prefix to the name of the organization contact. |  |
| `OrganizationContactNameSuffix` | `organization_contact_name_suffix` | String |  | Suffix to the surname (e.g., Esq., Jr., III) of the organization contact. |  |
| `OrganizationContactPhone` | `organization_contact_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `OrganizationContactPhoneExt` | `organization_contact_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `OrganizationCountry` | `organization_country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. |  |
| `OrganizationCountyOrParish` | `organization_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the organization is addressed. |  |
| `OrganizationMemberCount` | `organization_member_count` | Number |  | The total number of active members in the organization, if applicable. |  |
| `OrganizationMlsCode` | `organization_mls_code` | String |  | If the organization is an MLS, it is likely that it already has an ID or code based on its name or an abbreviation. |  |
| `OrganizationMlsVendorName` | `organization_mls_vendor_name` | String |  | If the organization uses an MLS system, this is the textual name of the vendor. |  |
| `OrganizationMlsVendorOuid` | `organization_mls_vendor_ouid` | String |  | If the organization uses an MLS system, this is that vendor's Unique Organization Identifier (UOI). |  |
| `OrganizationName` | `organization_name` | String |  | The textual name of the organization represented by a given Unique Organization Identifier (UOI) record. |  |
| `OrganizationNationalAssociationId` | `organization_national_association_id` | String |  | The national association ID of the organization, if applicable (e.g., in the U.S., this is the NRDS number). |  |
| `OrganizationPostalCode` | `organization_postal_code` | String |  | The postal code of the organization. |  |
| `OrganizationPostalCodePlus4` | `organization_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `OrganizationSocialMedia` | `organization_social_media` | Collection |  | A collection of the types of social media fields available for this organization. | `[Collection]` |
| `OrganizationSocialMediaType` | `organization_social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of sites or social media that the organization Uniform Resource Locator (URL) or ID is referring to (e.g., website, blog, Facebook, Twitter, LinkedIn, Instagram). |  |
| `OrganizationStateLicense` | `organization_state_license` | String |  | The license of the organization, if applicable. |  |
| `OrganizationStateLicenseState` | `organization_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the organization is licensed, if applicable. |  |
| `OrganizationStateOrProvince` | `organization_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the organization is addressed. |  |
| `OrganizationStatus` | `organization_status` | Boolean |  | Determines whether or not if the organization is active or inactive. |  |
| `OrganizationStatusChangeTimestamp` | `organization_status_change_timestamp` | Timestamp |  | The date/time of when the organization status was last changed. |  |
| `OrganizationType` | `organization_type` | enum | [`organization_type`](../lookups.md#organization_type) | The type of organization (i.e., MLS, vendor, association, etc.). |  |
| `OrganizationUniqueId` | `organization_unique_id` | String |  | This is the unique ID assigned to organizations included in the OUID resource. |  |
| `OrganizationUniqueIdKey` | `organization_unique_id_key` | String |  | The key field used by the system hosting a table of Unique Organization Identifiers (UOIs). | `pk` |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the organization record was originally input into the source system. |  |

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

