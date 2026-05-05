[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `member` (Member)

> Roster of agents, brokers, appraisers, assistants, affiliates and other MLS/association members.

## At a glance

| | |
|---|---|
| **Primary key** | `member_key` |
| **Fields on dd.reso.org** | 87 |
| **Columns in canonical DBML** | 78 (omits 2 satellite drops + 3 `Resource`-typed + 4 `Collection`-typed) |
| **Foreign keys OUT / IN** | 3 / 24 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Member/](https://dd.reso.org/DD2.0/Member/) |
| **Last revised upstream** | 7/25/2019 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Member record. | `[Collection]` |
| `JobTitle` | `job_title` | String |  | The title or position of the member within their organization. |  |
| `LastLoginTimestamp` | `last_login_timestamp` | Timestamp |  | The date/time the member last logged into the source or other system. |  |
| `Media` | `media` | Collection |  | The media for the Member record. | `[Collection]` |
| `MemberAOR` | `member_aor` | enum | [`aor`](../lookups.md#aor) | The member's primary board or association of REALTORS®. |  |
| `MemberAORMlsId` | `member_aor_mls_id` | String |  | The local, well-known identifier for the member's association of REALTORS®. |  |
| `MemberAORkey` | `member_ao_rkey` | String |  | A system unique identifier. |  |
| `MemberAddress1` | `member_address1` | String |  | The street number, direction, name and suffix of the member. |  |
| `MemberAddress2` | `member_address2` | String |  | The unit/suite number of the member. |  |
| `MemberAlternateId` | `member_alternate_id` | String |  | This is an alternate ID with no specific use. |  |
| `MemberAssociationComments` | `member_association_comments` | String |  | The association's notes regarding the member. |  |
| `MemberBillingPreference` | `member_billing_preference` | enum | [`billing_preference`](../lookups.md#billing_preference) | The member's preferred method of billing. |  |
| `MemberBio` | `member_bio` | String |  | A text field containing biography information for the member record. |  |
| `MemberCarrierRoute` | `member_carrier_route` | String |  | The group of addresses to which the U.S. |  |
| `MemberCity` | `member_city` | String |  | The city of the member. |  |
| `MemberCommitteeCount` | `member_committee_count` | Number |  | The number of current/active committees in which the member belongs. |  |
| `MemberCountry` | `member_country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. |  |
| `MemberCountyOrParish` | `member_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the member is addressed. |  |
| `MemberDesignation` | `member_designation` | varchar (multi) | [`member_designation`](../lookups.md#member_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® and each affiliated group upon completion of required courses. |  |
| `MemberDirectPhone` | `member_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberEmail` | `member_email` | String |  | The email address of the member. |  |
| `MemberFax` | `member_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberFirstName` | `member_first_name` | String |  | The first name of the member. |  |
| `MemberFullName` | `member_full_name` | String |  | The first, middle and last name of the member or an alternate full name. |  |
| `MemberHomePhone` | `member_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberIsAssistantTo` | `member_is_assistant_to` | String |  | The MemberMlsId of the agent/broker that this member assists. |  |
| `MemberKey` | `member_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `MemberLanguages` | `member_languages` | varchar (multi) | [`languages`](../lookups.md#languages) | The languages the member speaks. |  |
| `MemberLastName` | `member_last_name` | String |  | The last name of the member. |  |
| `MemberLoginId` | `member_login_id` | String |  | The ID used to log on to the MLS system. |  |
| `MemberMailOptOutYN` | `member_mail_opt_out_yn` | Boolean |  | Indicates whether or not the member has opted out of receiving solicitation via mail. |  |
| `MemberMiddleName` | `member_middle_name` | String |  | The middle name of the member. |  |
| `MemberMlsAccessYN` | `member_mls_access_yn` | Boolean |  | Indicates whether or not the member has access to the MLS system. |  |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. |  |
| `MemberMlsSecurityClass` | `member_mls_security_class` | enum | [`member_mls_security_class`](../lookups.md#member_mls_security_class) | The MLS security group or class given to the member. |  |
| `MemberMobilePhone` | `member_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberNamePrefix` | `member_name_prefix` | String |  | The prefix to the member name (e.g., Dr., Mr., Ms.). |  |
| `MemberNameSuffix` | `member_name_suffix` | String |  | The suffix to the member surname (e.g., Esq., Jr., III). |  |
| `MemberNationalAssociationEntryDate` | `member_national_association_entry_date` | Date |  | The date that the member's record was entered with the National Association of REALTORS®. |  |
| `MemberNationalAssociationId` | `member_national_association_id` | String |  | The national association ID of the member (e.g., in the U.S., this is the NRDS number). |  |
| `MemberNickname` | `member_nickname` | String |  | An alternate name used by the member, usually as a substitute for the first name. |  |
| `MemberOfficePhone` | `member_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberOfficePhoneExt` | `member_office_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `MemberOtherPhone` | `member_other_phone` | Collection |  | A collection of the types of other phone fields available for this member. | `[Collection]` |
| `MemberOtherPhoneType` | `member_other_phone_type` | enum | [`member_other_phone_type`](../lookups.md#member_other_phone_type) | A list of phone types (e.g., Home, Mobile, Second) that do not already exist in the given phone fields or if a second type of phone field is needed. |  |
| `MemberPager` | `member_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberPassword` | `member_password` | String |  | A password that the member wishes to share with other systems. |  |
| `MemberPhoneTTYTDD` | `member_phone_ttytdd` | String |  | TTY/TDD stands for Teletypewriter/Telecommunications Device for the Deaf. |  |
| `MemberPostalCode` | `member_postal_code` | String |  | The postal code of the member. |  |
| `MemberPostalCodePlus4` | `member_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `MemberPreferredMail` | `member_preferred_mail` | enum | [`preferred_mail`](../lookups.md#preferred_mail) | The preferred mailing address for the member. |  |
| `MemberPreferredMedia` | `member_preferred_media` | enum | [`preferred_media`](../lookups.md#preferred_media) | The method the member prefers to receive media by (e.g., Email, Mail, Fax). |  |
| `MemberPreferredPhone` | `member_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberPreferredPhoneExt` | `member_preferred_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `MemberPreferredPublication` | `member_preferred_publication` | enum | [`preferred_publication`](../lookups.md#preferred_publication) | Indicates where the member would like to receive any publications from the association. |  |
| `MemberPrimaryAorId` | `member_primary_aor_id` | String |  | The primary association of REALTORS® (AOR) associated with the member. |  |
| `MemberSocialMedia` | `member_social_media` | Collection |  | A collection of the types of social media fields available for this member. | `[Collection]` |
| `MemberStateLicense` | `member_state_license` | String |  | The license of the member. |  |
| `MemberStateLicenseExpirationDate` | `member_state_license_expiration_date` | Date |  | The expiration date for the member's license. |  |
| `MemberStateLicenseState` | `member_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the member is licensed. |  |
| `MemberStateLicenseType` | `member_state_license_type` | String |  | The license type of the member. |  |
| `MemberStateOrProvince` | `member_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the member is addressed. |  |
| `MemberStatus` | `member_status` | enum | [`member_status`](../lookups.md#member_status) | Indicates if the account is active, inactive or under disciplinary action. |  |
| `MemberTollFreePhone` | `member_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberTransferDate` | `member_transfer_date` | Date |  | The date that the member transferred from one member office to another |  |
| `MemberType` | `member_type` | enum | [`member_type`](../lookups.md#member_type) | The type of member (i.e., Agent, Broker, Office Manager, Appraiser, Photographer, Assistant, Mortgage Loan Originator, REALTOR, Association Staff, MLS Staff, etc.). |  |
| `MemberVoiceMail` | `member_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `MemberVoiceMailExt` | `member_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `MemberVotingPrecinct` | `member_voting_precinct` | String |  | The voting precinct of the member. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the roster (member or office) record was last modified. |  |
| `Office` | `office` | Resource |  | The office the member belongs to. | `[Resource]` |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of office_key]` |
| `OfficeName` | `office_name` | String |  | The legal name of the brokerage. | `[dropped: satellite of office_key]` |
| `OfficeNationalAssociationId` | `office_national_association_id` | String |  | The national association ID of the office (i.e., in the U.S., this is the NRDS number). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the roster (member or office) record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Member record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. | `-> ouid.organization_unique_id_key` |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of social media platforms (e.g., Facebook, LinkedIn, Instagram) associated with the MemberSocialMedia field. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Member record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. | `-> ouid.organization_unique_id_key` |
| `SourceSystemMemberKey` | `source_system_member_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |
| `SyndicateTo` | `syndicate_to` | varchar (multi) | [`syndicate_to`](../lookups.md#syndicate_to) | When permitted by the broker, the options made by the individual agent on where they would like their listings syndicated (i.e., Zillow, Trulia, Realtor.com, Homes.com, etc.). |  |
| `UniqueLicenseeIdentifier` | `unique_licensee_identifier` | String |  | The Unique Licensee Identifier (ULI) represents a single ID for a licensed real estate agent. |  |

## Foreign keys OUT (this resource references)

- `member.office_key` -> `office.office_key` (high)
- `member.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `member.source_system_id` -> `ouid.organization_unique_id_key` (medium)

## Foreign keys IN (other resources reference this)

- `caravan_stop.stop_showing_agent_key` -> `member.member_key` (medium)
- `contacts.owner_member_id` -> `member.member_key` (medium)
- `contacts.owner_member_key` -> `member.member_key` (high)
- `history_transactional.changed_by_member_key` -> `member.member_key` (high)
- `media.changed_by_member_id` -> `member.member_key` (medium)
- `media.changed_by_member_key` -> `member.member_key` (high)
- `member_association.member_key` -> `member.member_key` (medium)
- `member_state_license.member_key` -> `member.member_key` (medium)
- `office.office_broker_key` -> `member.member_key` (medium)
- `office.office_manager_key` -> `member.member_key` (medium)
- `open_house.showing_agent_key` -> `member.member_key` (medium)
- `ouid.changed_by_member_id` -> `member.member_key` (medium)
- `ouid.changed_by_member_key` -> `member.member_key` (high)
- `property.buyer_agent_key` -> `member.member_key` (medium)
- `property.co_buyer_agent_key` -> `member.member_key` (medium)
- `property.co_list_agent_key` -> `member.member_key` (medium)
- `property.list_agent_key` -> `member.member_key` (medium)
- `prospecting.owner_member_key` -> `member.member_key` (high)
- `saved_search.member_key` -> `member.member_key` (high)
- `showing.showing_agent_key` -> `member.member_key` (medium)
- `showing_appointment.showing_agent_key` -> `member.member_key` (medium)
- `showing_request.showing_agent_key` -> `member.member_key` (medium)
- `team_members.member_key` -> `member.member_key` (high)
- `teams.team_lead_key` -> `member.member_key` (medium)

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `member`)
- `media` -> `media` (many `media` per `member`)
- `member_other_phone` -> `other_phone` (many `other_phone` per `member`)
- `member_social_media` -> `social_media` (many `social_media` per `member`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `office_mls_id` | `office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `office_name` | `office_key` -> `office.office_name` | `drop_from_host` |  |
| `originating_system_member_key` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `originating_system_name` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_member_key` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_name` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |

