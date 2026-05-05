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

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `BillingOfficeKey` | `billing_office_key` | String |  | The office that will be billed (e.g., corporate headquarters). | Free-form text, up to 255 characters. |  |
| `FranchiseAffiliation` | `franchise_affiliation` | String |  | The name of the franchise to which the broker/office is contracted. | Free-form text, up to 50 characters. |  |
| `FranchiseNationalAssociationId` | `franchise_national_association_id` | String |  | The national association ID of the franchise (i.e., the NRDS number in the U.S.). | Free-form text, up to 25 characters. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Office record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `office` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `IDXOfficeParticipationYN` | `idx_office_participation_yn` | Boolean |  | Indicates whether or not the office/broker participates in IDX. | Nullable boolean flag (true / false / null = unknown). |  |
| `MainOffice` | `main_office` | Resource |  | The main office for the Office record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `MainOfficeKey` | `main_office_key` | String |  | The OfficeKey of the main office in a firm/company of offices. This is a self-referencing foreign key relating to this resource's OfficeKey. This key may be the same value as the OfficeKey for a given record if the given office is the main office. | Foreign key -> `office.office_key`. Set this to the `office`'s `office_key` to link this row to its parent `office`. | `-> office.office_key` |
| `MainOfficeMlsId` | `main_office_mls_id` | String |  | The OfficeMlsId of the main office in a firm/company of offices. | Free-form text, up to 25 characters. | `[REVIEW]` |
| `Media` | `media` | Collection |  | The media for the Office record. | Inverse 1:N: read as 'all `media` rows that point at this `office` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the roster (member or office) record was last modified. | ISO-8601 timestamp (UTC). |  |
| `NumberOfBranches` | `number_of_branches` | Number |  | The calculated value for the number of active branches. The count for multiple related offices. | Numeric (integer). |  |
| `NumberOfNonMemberSalespersons` | `number_of_non_member_salespersons` | Number |  | The total number of active salespersons that are not a member of the national association. | Numeric (integer). |  |
| `OfficeAOR` | `office_aor` | enum | [`aor`](../lookups.md#aor) | The office's board or association of REALTORS®. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OfficeAORMlsId` | `office_aor_mls_id` | String |  | The local, well-known identifier for the office's association of REALTORS®. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Free-form text, up to 25 characters. |  |
| `OfficeAORkey` | `office_ao_rkey` | String |  | A system unique identifier. Specifically, in aggregation systems, the OfficeAorKey is the system unique identifier from the system that the record was retrieved. This may be identical to the related xxxId. This is a foreign key relating to the association of REALTORS® member management system in which the record was originated. | Free-form text, up to 255 characters. |  |
| `OfficeAddress1` | `office_address1` | String |  | The street number, direction, name and suffix of the office. | Free-form text, up to 50 characters. |  |
| `OfficeAddress2` | `office_address2` | String |  | The unit/suite number of the office. | Free-form text, up to 50 characters. |  |
| `OfficeAlternateId` | `office_alternate_id` | String |  | An alternate ID with no specific use. | Free-form text, up to 50 characters. |  |
| `OfficeAssociationComments` | `office_association_comments` | String |  | Notes relating to the office. | Free-form text, up to 500 characters. |  |
| `OfficeBio` | `office_bio` | String |  | A text field containing biography information for the office record. This may be resume-like information, including experience and qualifications. | Free-form text, up to 1024 characters. |  |
| `OfficeBranchType` | `office_branch_type` | enum | [`office_branch_type`](../lookups.md#office_branch_type) | The level of the office in a hierarchy (i.e., Main, Branch, Stand-Alone, etc.). | Pick exactly one of 3 values from the lookup (closed list). |  |
| `OfficeBroker` | `office_broker` | Resource |  | The broker for the office. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OfficeBrokerKey` | `office_broker_key` | String |  | The MemberKey of the responsible/owning broker. This is a foreign key relating to the Member resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `OfficeBrokerMlsId` | `office_broker_mls_id` | String |  | The MemberMlsId of the responsible/owning broker. | Free-form text, up to 25 characters. | `[REVIEW]` |
| `OfficeBrokerNationalAssociationId` | `office_broker_national_association_id` | String |  | The national association ID of the broker (i.e., the NRDS number in the U.S.). | Free-form text, up to 25 characters. |  |
| `OfficeCity` | `office_city` | String |  | The city of the office. | Free-form text, up to 50 characters. |  |
| `OfficeCorporateLicense` | `office_corporate_license` | String |  | An independent license number is issued when an office/firm is a corporation. | Free-form text, up to 50 characters. |  |
| `OfficeCountry` | `office_country` | enum | [`country`](../lookups.md#country) | The office's country code for the street address. | Pick exactly one of 246 values from the lookup (closed list). |  |
| `OfficeCountyOrParish` | `office_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the offices is located. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OfficeEmail` | `office_email` | String |  | The email address of the office | Free-form text, up to 80 characters. |  |
| `OfficeFax` | `office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the key is the system unique identifier from the system where the record was just retrieved. This may be identical to the related xxxId identifier, but the key is guaranteed unique for this record set. | Unique key for this resource. Use as the FK target whenever another resource references `office`. | `pk` |
| `OfficeMailAddress1` | `office_mail_address1` | String |  | The street number, direction, name and suffix of the office. | Free-form text, up to 50 characters. |  |
| `OfficeMailAddress2` | `office_mail_address2` | String |  | The unit/suite number of the office. | Free-form text, up to 50 characters. |  |
| `OfficeMailCareOf` | `office_mail_care_of` | String |  | The care of (c/o) for the office's mailing address. | Free-form text, up to 30 characters. |  |
| `OfficeMailCity` | `office_mail_city` | String |  | The office's city for the mailing address. | Free-form text, up to 50 characters. |  |
| `OfficeMailCountry` | `office_mail_country` | enum | [`country`](../lookups.md#country) | The office's country code for the mailing address. | Pick exactly one of 246 values from the lookup (closed list). |  |
| `OfficeMailCountyOrParish` | `office_mail_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The office's county of the mailing address. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `OfficeMailPostalCode` | `office_mail_postal_code` | String |  | The postal code of the office's mailing address. | Free-form text, up to 5 characters. |  |
| `OfficeMailPostalCodePlus4` | `office_mail_postal_code_plus4` | String |  | The four-digit extension of the U.S. ZIP Code. | Free-form text, up to 4 characters. |  |
| `OfficeMailStateOrProvince` | `office_mail_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The office's state or province of the mailing address. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OfficeManager` | `office_manager` | Resource |  | The office manager for the office. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OfficeManagerKey` | `office_manager_key` | String |  | The lead office manager for the given office. This is a foreign key relating to the Member Resource's MemberKey. | Foreign key -> `member.member_key`. Set this to the `member`'s `member_key` to link this row to its parent `member`. | `-> member.member_key` |
| `OfficeManagerMlsId` | `office_manager_mls_id` | String |  | The lead office manager for the given office. | Free-form text, up to 25 characters. | `[REVIEW]` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Free-form text, up to 25 characters. |  |
| `OfficeName` | `office_name` | String |  | The legal name of the brokerage. | Free-form text, up to 255 characters. |  |
| `OfficeNationalAssociationId` | `office_national_association_id` | String |  | The national association ID of the office (e.g., the NRDS number in the U.S.). | Free-form text, up to 25 characters. |  |
| `OfficeNationalAssociationIdInsertDate` | `office_national_association_id_insert_date` | Date |  | The date the office record was initially created in the national association's database (e.g., the date the record was added to NRDS in the U.S.). | Date (YYYY-MM-DD). |  |
| `OfficePhone` | `office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `OfficePhoneExt` | `office_phone_ext` | String |  | The extension of the given phone number (if applicable). | Free-form text, up to 10 characters. |  |
| `OfficePostalCode` | `office_postal_code` | String |  | The postal code of the office. | Free-form text, up to 10 characters. |  |
| `OfficePostalCodePlus4` | `office_postal_code_plus4` | String |  | The four-digit extension of the U.S. ZIP Code. | Free-form text, up to 4 characters. |  |
| `OfficePreferredMedia` | `office_preferred_media` | enum | [`preferred_media`](../lookups.md#preferred_media) | The method the office prefers to receive media. | Pick exactly one of 3 values from the lookup (closed list). |  |
| `OfficePrimaryAorId` | `office_primary_aor_id` | String |  | The primary association of REALTORS® (AOR) associated with the member. This may be another AOR where the member has their primary membership. | Free-form text, up to 25 characters. |  |
| `OfficePrimaryStateOrProvince` | `office_primary_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The office's primary state or province. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OfficeSocialMedia` | `office_social_media` | Collection |  | A collection of the types of social media fields available for this office. The collection includes the type of system and other details relating to social media. | Inverse 1:N: read as 'all `social_media` rows that point at this `office` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `OfficeStateOrProvince` | `office_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the office is located. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `OfficeStatus` | `office_status` | enum | [`office_status`](../lookups.md#office_status) | Indicates whether the office is active, inactive or under disciplinary action. | Pick exactly one of 2 values from the lookup (closed list). |  |
| `OfficeType` | `office_type` | enum | [`office_type`](../lookups.md#office_type) | The type of business conducted by the office (e.g., Appraisal, MLS, Mortgage). | Pick exactly one of 11 values from the lookup (closed list). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the roster (member or office) record was originally input into the source system. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Office record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the office was input). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Foreign key -> `ouid.organization_unique_id_key`. Set this to the `ouid`'s `organization_unique_id_key` to link this row to its parent `ouid`. | `-> ouid.organization_unique_id_key` |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the office is originally input by the member. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemOfficeKey` | `originating_system_office_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the office was input). There may be cases where the source system (how the record was received) is not the originating system. See Source System Office Key for more information. | Free-form text, up to 255 characters. |  |
| `OtherPhone` | `other_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A collection of the types of social media fields available for the office. The collection includes the type of system and other details pertinent to social media. | Pick exactly one of 17 values from the lookup (closed list). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Office record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Foreign key -> `ouid.organization_unique_id_key`. Set this to the `ouid`'s `organization_unique_id_key` to link this row to its parent `ouid`. | `-> ouid.organization_unique_id_key` |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `SourceSystemOfficeKey` | `source_system_office_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SyndicateAgentOption` | `syndicate_agent_option` | enum | [`syndicate_agent_option`](../lookups.md#syndicate_agent_option) | A list of options allowing the broker to pass the decision of syndication choice down to the listing agents (i.e., No Agent Choice, Allow Agent Choice, Restrict Agent Choice, etc.). | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `SyndicateTo` | `syndicate_to` | varchar (multi) | [`syndicate_to`](../lookups.md#syndicate_to) | The principal broker's choice on where they would like their listings syndicated (i.e., Zillow, Trulia, Homes.com, etc.). | Pick one or more of 4 values from the lookup (closed list). |  |
| `VirtualOfficeWebsiteYN` | `virtual_office_website_yn` | Boolean |  | Indicates whether or not this is a Virtual Office Website (VOW). | Nullable boolean flag (true / false / null = unknown). |  |

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

