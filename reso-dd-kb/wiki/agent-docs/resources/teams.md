# `teams` (Teams)

> Name and other information about teams of members who work together.

- Source: [https://dd.reso.org/DD2.0/Teams/](https://dd.reso.org/DD2.0/Teams/)
- Field count on dd.reso.org: **45**
- Primary key: `team_key`
- Last revised upstream: 9/24/2015

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Teams record. | `[Collection]` |
| `Media` | `media` | Collection |  | The media associated with the Teams record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the roster (team or office) record was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The date/time the roster (team or office) record was originally input into the source system. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Teams record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier's (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `SocialMediaType` | `social_media_type` | enum | [`social_media_type`](../lookups.md#social_media_type) | A list of types of sites or social media that the team Uniform Resource Locator (URL) or ID is referring to (e.g., website, blog, Facebook, Twitter, LinkedIn, Instagram). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Teams record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier's (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the team record provider. |  |
| `TeamAddress1` | `team_address1` | String |  | The street number, direction, name and suffix of the team. |  |
| `TeamAddress2` | `team_address2` | String |  | The unit/suite number of the team. |  |
| `TeamCarrierRoute` | `team_carrier_route` | String |  | The group of addresses to which the U.S. |  |
| `TeamCity` | `team_city` | String |  | The city of the team. |  |
| `TeamCountry` | `team_country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. |  |
| `TeamCountyOrParish` | `team_county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county or parish in which the team is addressed. |  |
| `TeamDescription` | `team_description` | String |  | A description or marketing information about the team. |  |
| `TeamDirectPhone` | `team_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamEmail` | `team_email` | String |  | The email address of the team. |  |
| `TeamFax` | `team_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamKey` | `team_key` | String |  | A system unique identifier. | `pk` |
| `TeamLead` | `team_lead` | Resource |  | The team lead for the given team. | `[Resource]` |
| `TeamLeadKey` | `team_lead_key` | String |  | The unique system identifier of the team's lead member. | `-> member.member_key` |
| `TeamLeadLoginId` | `team_lead_login_id` | String |  | The ID used to log on to the MLS system. |  |
| `TeamLeadMlsId` | `team_lead_mls_id` | String |  | The local, well-known identifier for the team lead. |  |
| `TeamLeadNationalAssociationId` | `team_lead_national_association_id` | String |  | The national association ID of the team lead (i.e., NRDS number in the U.S.). |  |
| `TeamLeadStateLicense` | `team_lead_state_license` | String |  | The license of the team lead. |  |
| `TeamLeadStateLicenseState` | `team_lead_state_license_state` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state in which the team lead is licensed. |  |
| `TeamMobilePhone` | `team_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamName` | `team_name` | String |  | The name under which the team operates. |  |
| `TeamOfficePhone` | `team_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamOfficePhoneExt` | `team_office_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `TeamPostalCode` | `team_postal_code` | String |  | The postal code of the team. |  |
| `TeamPostalCodePlus4` | `team_postal_code_plus4` | String |  | The four-digit extension of the U.S. |  |
| `TeamPreferredPhone` | `team_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamPreferredPhoneExt` | `team_preferred_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `TeamStateOrProvince` | `team_state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | The state or province in which the team is addressed. |  |
| `TeamStatus` | `team_status` | enum | [`team_status`](../lookups.md#team_status) | Determines whether the account is active, inactive or under disciplinary action. |  |
| `TeamTollFreePhone` | `team_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamVoiceMail` | `team_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `TeamVoiceMailExt` | `team_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `TeamsSocialMedia` | `teams_social_media` | Collection |  | A collection of the types of social media fields available for this team. | `[Collection]` |

## Foreign keys OUT (this resource references)

- `teams.team_lead_key` -> `member.member_key` (medium)

## Foreign keys IN (other resources reference this)

- `property.buyer_team_key` -> `teams.team_key` (medium)
- `property.list_team_key` -> `teams.team_key` (medium)
- `team_members.team_key` -> `teams.team_key` (medium)

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `teams`)
- `media` -> `media` (many `media` per `teams`)
- `teams_social_media` -> `social_media` (many `social_media` per `teams`)

