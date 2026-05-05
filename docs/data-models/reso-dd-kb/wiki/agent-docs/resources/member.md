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

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Member record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `member` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `JobTitle` | `job_title` | String |  | The title or position of the member within their organization. | Free-form text, up to 50 characters. |  |
| `LastLoginTimestamp` | `last_login_timestamp` | Timestamp |  | The date/time the member last logged into the source or other system. | ISO-8601 timestamp (UTC). |  |
| `Media` | `media` | Collection |  | The media for the Member record. | Inverse 1:N: read as 'all `media` rows that point at this `member` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `MemberAOR` | `member_aor` | enum | [`aor`](../lookups.md#aor) | The member's primary board or association of REALTORS®. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `MemberAORMlsId` | `member_aor_mls_id` | String |  | The local, well-known identifier for the member's association of REALTORS®. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Free-form text, up to 25 characters. |  |
| `MemberAORkey` | `member_ao_rkey` | String |  | A system unique identifier. Specifically, in aggregation systems, the Member AOR Key is the system unique identifier from the system that the record was retrieved. This may be identical to the related xxxId. | Free-form text, up to 255 characters. |  |
| `MemberAddress1` | `member_address1` | String |  | The street number, direction, name and suffix of the member. | Free-form text, up to 50 characters. |  |
| `MemberAddress2` | `member_address2` | String |  | The unit/suite number of the member. | Free-form text, up to 50 characters. |  |
| `MemberAlternateId` | `member_alternate_id` | String |  | This is an alternate ID with no specific use. | Free-form text, up to 50 characters. |  |
| `MemberAssociationComments` | `member_association_comments` | String |  | The association's notes regarding the member. | Free-form text, up to 500 characters. |  |
| `MemberBillingPreference` | `member_billing_preference` | enum | [`billing_preference`](../lookups.md#billing_preference) | The member's preferred method of billing. | Pick exactly one of 3 values from the lookup (closed list). |  |
| `MemberBio` | `member_bio` | String |  | A text field containing biography information for the member record. This may be resume-like information, including experience and qualifications. | Free-form text, up to 1024 characters. |  |
| `MemberCarrierRoute` | `member_carrier_route` | String |  | The group of addresses to which the U.S. Postal Service (USPS) assigns the same code to aid in mail delivery. For the USPS, these codes are nine digits: five numbers for the ZIP code, one letter for the carrier route type and three numbers for the carrier route number. | Free-form text, up to 9 characters. |  |
| `MemberCity` | `member_city` | String |  | The city of the member. | Free-form text, up to 50 characters. |  |
| `MemberCommitteeCount` | `member_committee_count` | Number |  | The number of current/active committees in which the member belongs. | Numeric (integer). |  |
| `MemberCountry` | `member_country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. | Pick exactly one of 246 values from the lookup (closed list). |  |
| `MemberCountyOrParish` | `member_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the member is addressed. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `MemberDesignation` | `member_designation` | varchar (multi) | [`member_designation`](../lookups.md#member_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® and each affiliated group upon completion of required courses. | Pick one or more of 27 values from the lookup (closed list). |  |
| `MemberDirectPhone` | `member_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberEmail` | `member_email` | String |  | The email address of the member. | Free-form text, up to 80 characters. |  |
| `MemberFax` | `member_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberFirstName` | `member_first_name` | String |  | The first name of the member. | Free-form text, up to 50 characters. |  |
| `MemberFullName` | `member_full_name` | String |  | The first, middle and last name of the member or an alternate full name. | Free-form text, up to 150 characters. |  |
| `MemberHomePhone` | `member_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberIsAssistantTo` | `member_is_assistant_to` | String |  | The MemberMlsId of the agent/broker that this member assists. The typical use will be to add the agent's ID to this field when editing the member record of the assistant. | Free-form text, up to 50 characters. |  |
| `MemberKey` | `member_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemMemberKey and OriginatingSystemMemberKey. | Unique key for this resource. Use as the FK target whenever another resource references `member`. | `pk` |
| `MemberLanguages` | `member_languages` | varchar (multi) | [`languages`](../lookups.md#languages) | The languages the member speaks. | Pick exactly one of 190 values from the lookup (closed list). |  |
| `MemberLastName` | `member_last_name` | String |  | The last name of the member. | Free-form text, up to 50 characters. |  |
| `MemberLoginId` | `member_login_id` | String |  | The ID used to log on to the MLS system. | Free-form text, up to 25 characters. |  |
| `MemberMailOptOutYN` | `member_mail_opt_out_yn` | Boolean |  | Indicates whether or not the member has opted out of receiving solicitation via mail. | Nullable boolean flag (true / false / null = unknown). |  |
| `MemberMiddleName` | `member_middle_name` | String |  | The middle name of the member. | Free-form text, up to 50 characters. |  |
| `MemberMlsAccessYN` | `member_mls_access_yn` | Boolean |  | Indicates whether or not the member has access to the MLS system. | Nullable boolean flag (true / false / null = unknown). |  |
| `MemberMlsId` | `member_mls_id` | String |  | The local, well-known identifier for the member. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Free-form text, up to 25 characters. |  |
| `MemberMlsSecurityClass` | `member_mls_security_class` | enum | [`member_mls_security_class`](../lookups.md#member_mls_security_class) | The MLS security group or class given to the member. | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `MemberMobilePhone` | `member_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberNamePrefix` | `member_name_prefix` | String |  | The prefix to the member name (e.g., Dr., Mr., Ms.). | Free-form text, up to 10 characters. |  |
| `MemberNameSuffix` | `member_name_suffix` | String |  | The suffix to the member surname (e.g., Esq., Jr., III). | Free-form text, up to 10 characters. |  |
| `MemberNationalAssociationEntryDate` | `member_national_association_entry_date` | Date |  | The date that the member's record was entered with the National Association of REALTORS®. | Date (YYYY-MM-DD). |  |
| `MemberNationalAssociationId` | `member_national_association_id` | String |  | The national association ID of the member (e.g., in the U.S., this is the NRDS number). | Free-form text, up to 25 characters. |  |
| `MemberNickname` | `member_nickname` | String |  | An alternate name used by the member, usually as a substitute for the first name. | Free-form text, up to 50 characters. |  |
| `MemberOfficePhone` | `member_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberOfficePhoneExt` | `member_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | Free-form text, up to 10 characters. |  |
| `MemberOtherPhone` | `member_other_phone` | Collection |  | A collection of the types of other phone fields available for this member. The collection includes the type of system and other details pertinent about other phone numbers | Inverse 1:N: read as 'all `other_phone` rows that point at this `member` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `MemberOtherPhoneType` | `member_other_phone_type` | enum | [`member_other_phone_type`](../lookups.md#member_other_phone_type) | A list of phone types (e.g., Home, Mobile, Second) that do not already exist in the given phone fields or if a second type of phone field is needed. | Pick exactly one of 14 values from the lookup (closed list). |  |
| `MemberPager` | `member_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberPassword` | `member_password` | String |  | A password that the member wishes to share with other systems. Normal security considerations apply and are the responsibility of the entity utilizing this field. | Free-form text, up to 25 characters. |  |
| `MemberPhoneTTYTDD` | `member_phone_ttytdd` | String |  | TTY/TDD stands for Teletypewriter/Telecommunications Device for the Deaf. This involves a user terminal with keyboard input and printer or display output used by the hearing and speech impaired. The device contains a modem and is used over a standard analog phone line. If a recipient does not have a corresponding terminal device, TTY/TDD users dial a relay service composed of operators who receive the typed messages, call the recipients and speak the messages to them. The operators also type the responses back to the TTY/TDD user. | Free-form text, up to 16 characters. |  |
| `MemberPostalCode` | `member_postal_code` | String |  | The postal code of the member. | Free-form text, up to 10 characters. |  |
| `MemberPostalCodePlus4` | `member_postal_code_plus4` | String |  | The four-digit extension of the U.S. Zip Code. | Free-form text, up to 4 characters. |  |
| `MemberPreferredMail` | `member_preferred_mail` | enum | [`preferred_mail`](../lookups.md#preferred_mail) | The preferred mailing address for the member. | Pick exactly one of 4 values from the lookup (closed list). |  |
| `MemberPreferredMedia` | `member_preferred_media` | enum | [`preferred_media`](../lookups.md#preferred_media) | The method the member prefers to receive media by (e.g., Email, Mail, Fax). | Pick exactly one of 3 values from the lookup (closed list). |  |
| `MemberPreferredPhone` | `member_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberPreferredPhoneExt` | `member_preferred_phone_ext` | String |  | The extension of the given phone number, if applicable. | Free-form text, up to 10 characters. |  |
| `MemberPreferredPublication` | `member_preferred_publication` | enum | [`preferred_publication`](../lookups.md#preferred_publication) | Indicates where the member would like to receive any publications from the association. | Pick exactly one of 5 values from the lookup (closed list). |  |
| `MemberPrimaryAorId` | `member_primary_aor_id` | String |  | The primary association of REALTORS® (AOR) associated with the member. This may be another AOR where the member has their primary membership. | Free-form text, up to 25 characters. |  |
| `MemberSocialMedia` | `member_social_media` | Collection |  | A collection of the types of social media fields available for this member. The collection includes the type of system and other details pertinent to social media. | Inverse 1:N: read as 'all `social_media` rows that point at this `member` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `MemberStateLicense` | `member_state_license` | String |  | The license of the member. Multiple licenses should be separated by a comma and space. | Free-form text, up to 50 characters. |  |
| `MemberStateLicenseExpirationDate` | `member_state_license_expiration_date` | Date |  | The expiration date for the member's license. | Date (YYYY-MM-DD). |  |
| `MemberStateLicenseState` | `member_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the member is licensed. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `MemberStateLicenseType` | `member_state_license_type` | String |  | The license type of the member. | Free-form text, up to 30 characters. |  |
| `MemberStateOrProvince` | `member_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the member is addressed. | Pick exactly one of 65 values from the lookup (closed list). |  |
| `MemberStatus` | `member_status` | enum | [`member_status`](../lookups.md#member_status) | Indicates if the account is active, inactive or under disciplinary action. | Pick exactly one of 2 values from the lookup (closed list). |  |
| `MemberTollFreePhone` | `member_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberTransferDate` | `member_transfer_date` | Date |  | The date that the member transferred from one member office to another | Date (YYYY-MM-DD). |  |
| `MemberType` | `member_type` | enum | [`member_type`](../lookups.md#member_type) | The type of member (i.e., Agent, Broker, Office Manager, Appraiser, Photographer, Assistant, Mortgage Loan Originator, REALTOR, Association Staff, MLS Staff, etc.). | Pick exactly one of 19 values from the lookup (closed list). |  |
| `MemberVoiceMail` | `member_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). Other conventions should use the common local standard. International numbers should be preceded by a plus symbol. | Free-form text, up to 16 characters. |  |
| `MemberVoiceMailExt` | `member_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. | Free-form text, up to 10 characters. |  |
| `MemberVotingPrecinct` | `member_voting_precinct` | String |  | The voting precinct of the member. | Free-form text, up to 50 characters. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the roster (member or office) record was last modified. | ISO-8601 timestamp (UTC). |  |
| `Office` | `office` | Resource |  | The office the member belongs to. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OfficeKey` | `office_key` | String |  | A system unique identifier. Specifically, in aggregation systems, the key is the system unique identifier from the system where the record was just retrieved. This may be identical to the related xxxId identifier, but the key is guaranteed unique for this record set. This is a foreign key relating to the Office Resource's OfficeKey. | Foreign key -> `office.office_key`. Set this to the `office`'s `office_key` to link this row to its parent `office`. | `-> office.office_key` |
| `OfficeMlsId` | `office_mls_id` | String |  | The local, well-known identifier. This value may not be unique, specifically in the case of aggregation systems, and it should be the identifier from the original system. | Do not write. Phase-2.5 satellite of `OfficeKey`; the same value lives on the parent resource and is reachable via the `OfficeKey` FK. | `[dropped: satellite of office_key]` |
| `OfficeName` | `office_name` | String |  | The legal name of the brokerage. | Do not write. Phase-2.5 satellite of `OfficeKey`; the same value lives on the parent resource and is reachable via the `OfficeKey` FK. | `[dropped: satellite of office_key]` |
| `OfficeNationalAssociationId` | `office_national_association_id` | String |  | The national association ID of the office (i.e., in the U.S., this is the NRDS number). | Free-form text, up to 25 characters. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the roster (member or office) record was originally input into the source system. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Member record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the MLS where the member was input). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Foreign key -> `ouid.organization_unique_id_key`. Set this to the `ouid`'s `organization_unique_id_key` to link this row to its parent `ouid`. | `-> ouid.organization_unique_id_key` |
| `OriginatingSystemMemberKey` | `originating_system_member_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the member was input). There may be cases where the source system (how the record was received) is not the originating system. See Source System Member Key for more information. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. The place where the member is originally input by the member. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of social media platforms (e.g., Facebook, LinkedIn, Instagram) associated with the MemberSocialMedia field. | Pick exactly one of 17 values from the lookup (closed list). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Member record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Foreign key -> `ouid.organization_unique_id_key`. Set this to the `ouid`'s `organization_unique_id_key` to link this row to its parent `ouid`. | `-> ouid.organization_unique_id_key` |
| `SourceSystemMemberKey` | `source_system_member_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. The system from which the record was directly received. The legal name of the company. | Free-form text, up to 255 characters. |  |
| `SyndicateTo` | `syndicate_to` | varchar (multi) | [`syndicate_to`](../lookups.md#syndicate_to) | When permitted by the broker, the options made by the individual agent on where they would like their listings syndicated (i.e., Zillow, Trulia, Realtor.com, Homes.com, etc.). | Pick one or more of 4 values from the lookup (closed list). |  |
| `UniqueLicenseeIdentifier` | `unique_licensee_identifier` | String |  | The Unique Licensee Identifier (ULI) represents a single ID for a licensed real estate agent. It differs from the National Association of REALTORS® NRDS ID in that being a REALTOR is not a requirement. | Free-form text, up to 255 characters. |  |

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

