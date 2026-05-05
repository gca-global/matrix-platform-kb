# `association` (Association)

> Fields pertaining to the local real estate trade association.

- Source: [https://dd.reso.org/DD2.0/Association/](https://dd.reso.org/DD2.0/Association/)
- Field count on dd.reso.org: **45**
- Primary key: `association_key`
- Last revised upstream: 8/5/2024

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `AssociationAddress1` | `association_address1` | String |  | The street number, direction, name and suffix of the association. |  |
| `AssociationAddress2` | `association_address2` | String |  | The unit/suite number of the association. |  |
| `AssociationCareOf` | `association_care_of` | String |  | The care of (c/o) information for the association's street address. |  |
| `AssociationCharterDate` | `association_charter_date` | Date |  | The charter date for the association. |  |
| `AssociationCity` | `association_city` | String |  | The city where the association is located. |  |
| `AssociationCountry` | `association_country` | enum | [`country`](../lookups.md#country) | The association's country code for the street address. |  |
| `AssociationCountyOrParish` | `association_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The association's county of the street address. |  |
| `AssociationFax` | `association_fax` | String |  | The North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `AssociationKey` | `association_key` | String |  | The unique identifier for the association record. | `pk` |
| `AssociationMailAddress1` | `association_mail_address1` | String |  | The street number, direction, name and suffix of the association's mailing address. |  |
| `AssociationMailAddress2` | `association_mail_address2` | String |  | The unit/suite number of the association's mailing address. |  |
| `AssociationMailCareOf` | `association_mail_care_of` | String |  | The care of (c/o) information for the association's mailing address. |  |
| `AssociationMailCity` | `association_mail_city` | String |  | The city in which the association's mail is received. |  |
| `AssociationMailCountry` | `association_mail_country` | enum | [`country`](../lookups.md#country) | The country code for the association's mailing address. |  |
| `AssociationMailCountyOrParish` | `association_mail_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county in which the association's mailing address is located. |  |
| `AssociationMailPostalCode` | `association_mail_postal_code` | String |  | The postal code in which the association's mail is received. |  |
| `AssociationMailPostalCodePlus4` | `association_mail_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `AssociationMailStateOfProvince` | `association_mail_state_of_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the association's mail is received. |  |
| `AssociationMember` | `association_member` | Resource |  | The member of the association. | `[Resource]` |
| `AssociationMlsId` | `association_mls_id` | String |  | The local, well-known identifier for the association of REALTORS®. |  |
| `AssociationName` | `association_name` | String |  | The name of the association. |  |
| `AssociationNationalAssociationId` | `association_national_association_id` | String |  | The national association ID of the association as known by the National Association of REALTORS®. |  |
| `AssociationPhone` | `association_phone` | String |  | The North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `AssociationPostalCode` | `association_postal_code` | String |  | The postal code of the association. |  |
| `AssociationPostalCodePlus4` | `association_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `AssociationSocialMedia` | `association_social_media` | Collection |  | A collection of the types of social media fields available for the association, including the type of system and other details pertinent to social media. | `[Collection]` |
| `AssociationStateOrProvince` | `association_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the association is addressed. |  |
| `AssociationStatus` | `association_status` | enum | [`association_status`](../lookups.md#association_status) | The status of the association (i.e., Active, Inactive). |  |
| `AssociationType` | `association_type` | enum | [`association_type`](../lookups.md#association_type) | The type of association (MLS, Local, Not Applicable, etc.). |  |
| `ExecutiveOfficerMemberKey` | `executive_officer_member_key` | String |  | The executive officer's member key. |  |
| `ExecutiveOfficerMemberMlsId` | `executive_officer_member_mls_id` | String |  | The local, well-known identifier for the executive officer. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Association record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the Association record was last modified. |  |
| `MultipleListingServiceId` | `multiple_listing_service_id` | String |  | The ID of the Multiple Listing Service (MLS) used by the association. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | Date/time the record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Association record. | `[Resource]` |
| `OriginatingSystemAssociationKey` | `originating_system_association_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemId` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of websites or social media the association Uniform Resource Locator (URL) or ID is referring to (e.g., Website, Blog, Facebook, Twitter, LinkedIn, Instagram). |  |
| `SocialMediaUrlOrId` | `social_media_url_or_id` | String |  | The website URL or ID of social media site or account of the Association. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Association record. | `[Resource]` |
| `SourceSystemAssociationKey` | `source_system_association_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemId` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

- `member_association.association_key` -> `association.association_key` (medium)
- `office_association.association_key` -> `association.association_key` (medium)

## Inverse 1:N (collection-typed companions)

- `association_social_media` -> `social_media` (many `social_media` per `association`)
- `history_transactional` -> `history_transactional` (many `history_transactional` per `association`)

