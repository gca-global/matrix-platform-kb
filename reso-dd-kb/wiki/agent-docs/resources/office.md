[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `office` (Office)

> Roster of offices who are members of the MLS and/or association.

## At a glance

| | |
|---|---|
| **Primary key** | `office_key` |
| **Fields on dd.reso.org** | 73 |
| **Columns in canonical DBML** | 65 (omits 0 satellite drops + 5 `Resource`-typed + 3 `Collection`-typed) |
| **Foreign keys OUT / IN** | 5 / 9 |
| **Review markers** | 3 |
| **Source** | [https://dd.reso.org/DD2.0/Office/](https://dd.reso.org/DD2.0/Office/) |
| **Last revised upstream** | 8/5/2024 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `BillingOfficeKey` | `billing_office_key` | String |  | The office that will be billed (e.g., corporate headquarters). |  |
| `FranchiseAffiliation` | `franchise_affiliation` | String |  | The name of the franchise to which the broker/office is contracted. |  |
| `FranchiseNationalAssociationId` | `franchise_national_association_id` | String |  | The national association ID of the franchise (i.e., the NRDS number in the U.S.). |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Office record. | `[Collection]` |
| `IDXOfficeParticipationYN` | `idx_office_participation_yn` | Boolean |  | Indicates whether or not the office/broker participates in IDX. |  |
| `MainOffice` | `main_office` | Resource |  | The main office for the Office record. | `[Resource]` |
| `MainOfficeKey` | `main_office_key` | String |  | The OfficeKey of the main office in a firm/company of offices. | `-> office.office_key` |
| `MainOfficeMlsId` | `main_office_mls_id` | String |  | The OfficeMlsId of the main office in a firm/company of offices. | `[REVIEW]` |
| `Media` | `media` | Collection |  | The media for the Office record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the roster (member or office) record was last modified. |  |
| `NumberOfBranches` | `number_of_branches` | Number |  | The calculated value for the number of active branches. |  |
| `NumberOfNonMemberSalespersons` | `number_of_non_member_salespersons` | Number |  | The total number of active salespersons that are not a member of the national association. |  |
| `OfficeAOR` | `office_aor` | enum | [`aor`](../lookups.md#aor) | The office's board or association of REALTORS®. |  |
| `OfficeAORMlsId` | `office_aor_mls_id` | String |  | The local, well-known identifier for the office's association of REALTORS®. |  |
| `OfficeAORkey` | `office_ao_rkey` | String |  | A system unique identifier. |  |
| `OfficeAddress1` | `office_address1` | String |  | The street number, direction, name and suffix of the office. |  |
| `OfficeAddress2` | `office_address2` | String |  | The unit/suite number of the office. |  |
| `OfficeAlternateId` | `office_alternate_id` | String |  | An alternate ID with no specific use. |  |
| `OfficeAssociationComments` | `office_association_comments` | String |  | Notes relating to the office. |  |
| `OfficeBio` | `office_bio` | String |  | A text field containing biography information for the office record. |  |
| `OfficeBranchType` | `office_branch_type` | enum | [`office_branch_type`](../lookups.md#office_branch_type) | The level of the office in a hierarchy (i.e., Main, Branch, Stand-Alone, etc.). |  |
| `OfficeBroker` | `office_broker` | Resource |  | The broker for the office. | `[Resource]` |
| `OfficeBrokerKey` | `office_broker_key` | String |  | The MemberKey of the responsible/owning broker. | `-> member.member_key` |
| `OfficeBrokerMlsId` | `office_broker_mls_id` | String |  | The MemberMlsId of the responsible/owning broker. | `[REVIEW]` |
| `OfficeBrokerNationalAssociationId` | `office_broker_national_association_id` | String |  | The national association ID of the broker (i.e., the NRDS number in the U.S.). |  |
| `OfficeCity` | `office_city` | String |  | The city of the office. |  |
| `OfficeCorporateLicense` | `office_corporate_license` | String |  | An independent license number is issued when an office/firm is a corporation. |  |
| `OfficeCountry` | `office_country` | enum | [`country`](../lookups.md#country) | The office's country code for the street address. |  |
| `OfficeCountyOrParish` | `office_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the offices is located. |  |
| `OfficeEmail` | `office_email` | String |  | The email address of the office |  |
| `OfficeFax` | `office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. | `pk` |
| `OfficeMailAddress1` | `office_mail_address1` | String |  | The street number, direction, name and suffix of the office. |  |
| `OfficeMailAddress2` | `office_mail_address2` | String |  | The unit/suite number of the office. |  |
| `OfficeMailCareOf` | `office_mail_care_of` | String |  | The care of (c/o) for the office's mailing address. |  |
| `OfficeMailCity` | `office_mail_city` | String |  | The office's city for the mailing address. |  |
| `OfficeMailCountry` | `office_mail_country` | enum | [`country`](../lookups.md#country) | The office's country code for the mailing address. |  |
| `OfficeMailCountyOrParish` | `office_mail_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The office's county of the mailing address. |  |
| `OfficeMailPostalCode` | `office_mail_postal_code` | String |  | The postal code of the office's mailing address. |  |
| `OfficeMailPostalCodePlus4` | `office_mail_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `OfficeMailStateOrProvince` | `office_mail_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The office's state or province of the mailing address. |  |
| `OfficeManager` | `office_manager` | Resource |  | The office manager for the office. | `[Resource]` |
| `OfficeManagerKey` | `office_manager_key` | String |  | The lead office manager for the given office. | `-> member.member_key` |
| `OfficeManagerMlsId` | `office_manager_mls_id` | String |  | The lead office manager for the given office. | `[REVIEW]` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. |  |
| `OfficeName` | `office_name` | String |  | The legal name of the brokerage. |  |
| `OfficeNationalAssociationId` | `office_national_association_id` | String |  | The national association ID of the office (e.g., the NRDS number in the U.S.). |  |
| `OfficeNationalAssociationIdInsertDate` | `office_national_association_id_insert_date` | Date |  | The date the office record was initially created in the national association's database (e.g., the date the record was added to NRDS in the U.S.). |  |
| `OfficePhone` | `office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `OfficePhoneExt` | `office_phone_ext` | String |  | The extension of the given phone number (if applicable). |  |
| `OfficePostalCode` | `office_postal_code` | String |  | The postal code of the office. |  |
| `OfficePostalCodePlus4` | `office_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `OfficePreferredMedia` | `office_preferred_media` | enum | [`preferred_media`](../lookups.md#preferred_media) | The method the office prefers to receive media. |  |
| `OfficePrimaryAorId` | `office_primary_aor_id` | String |  | The primary association of REALTORS® (AOR) associated with the member. |  |
| `OfficePrimaryStateOrProvince` | `office_primary_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The office's primary state or province. |  |
| `OfficeSocialMedia` | `office_social_media` | Collection |  | A collection of the types of social media fields available for this office. | `[Collection]` |
| `OfficeStateOrProvince` | `office_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the office is located. |  |
| `OfficeStatus` | `office_status` | enum | [`office_status`](../lookups.md#office_status) | Indicates whether the office is active, inactive or under disciplinary action. |  |
| `OfficeType` | `office_type` | enum | [`office_type`](../lookups.md#office_type) | The type of business conducted by the office (e.g., Appraisal, MLS, Mortgage). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the roster (member or office) record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Office record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. | `-> ouid.organization_unique_id_key` |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `OriginatingSystemOfficeKey` | `originating_system_office_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OtherPhone` | `other_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A collection of the types of social media fields available for the office. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Office record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. | `-> ouid.organization_unique_id_key` |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |
| `SourceSystemOfficeKey` | `source_system_office_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SyndicateAgentOption` | `syndicate_agent_option` | enum | [`syndicate_agent_option`](../lookups.md#syndicate_agent_option) | A list of options allowing the broker to pass the decision of syndication choice down to the listing agents (i.e., No Agent Choice, Allow Agent Choice, Restrict Agent Choice, etc.). |  |
| `SyndicateTo` | `syndicate_to` | varchar (multi) | [`syndicate_to`](../lookups.md#syndicate_to) | The principal broker's choice on where they would like their listings syndicated (i.e., Zillow, Trulia, Homes.com, etc.). |  |
| `VirtualOfficeWebsiteYN` | `virtual_office_website_yn` | Boolean |  | Indicates whether or not this is a Virtual Office Website (VOW). |  |

## Foreign keys OUT (this resource references)

- `office.main_office_key` -> `office.office_key` (high)
- `office.office_broker_key` -> `member.member_key` (medium)
- `office.office_manager_key` -> `member.member_key` (medium)
- `office.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `office.source_system_id` -> `ouid.organization_unique_id_key` (medium)

## Foreign keys IN (other resources reference this)

- `lock_or_box.showing_office_id` -> `office.office_key` (medium)
- `member.office_key` -> `office.office_key` (high)
- `office.main_office_key` -> `office.office_key` (high)
- `office_association.office_key` -> `office.office_key` (high)
- `office_corporate_license.office_key` -> `office.office_key` (high)
- `property.buyer_office_key` -> `office.office_key` (high)
- `property.co_buyer_office_key` -> `office.office_key` (high)
- `property.co_list_office_key` -> `office.office_key` (high)
- `property.list_office_key` -> `office.office_key` (high)

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `office`)
- `media` -> `media` (many `media` per `office`)
- `office_social_media` -> `social_media` (many `social_media` per `office`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `main_office_mls_id` | `main_office_key` -> `office.office_mls_id` | `review` | name_type_match_but_definitions_differ |
| `office_broker_mls_id` | `office_broker_key` -> `member.member_mls_id` | `review` | name_type_match_but_definitions_differ |
| `office_manager_mls_id` | `office_manager_key` -> `member.member_mls_id` | `review` | name_type_match_but_definitions_differ |
| `originating_system_name` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `originating_system_office_key` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_name` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_office_key` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |

