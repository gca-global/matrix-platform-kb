# `prospecting` (Prospecting)

> Automatic email connecting Contacts and SavedSearch resources to send results matching saved search criteria.

- Source: [https://dd.reso.org/DD2.0/Prospecting/](https://dd.reso.org/DD2.0/Prospecting/)
- Field count on dd.reso.org: **31**
- Primary key: `prospecting_key`
- Last revised upstream: 5/2/2017

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ActiveYN` | `active_yn` | Boolean |  | If set to True, the given automated email is active. |  |
| `BccEmailList` | `bcc_email_list` | String |  | A comma-separated list of email addresses that are the blind carbon copy (Bcc) address that the automated emails are being sent to. |  |
| `BccMeYN` | `bcc_me_yn` | Boolean |  | When set to True, the automated mail is also sent as a blind carbon copy (Bcc) to the member who created the automated email. |  |
| `CcEmailList` | `cc_email_list` | String |  | A comma-separated list of email addresses that are the carbon copy (Cc) address that the automated emails are being sent to. |  |
| `ClientActivatedYN` | `client_activated_yn` | Boolean |  | If set to True, the client has clicked through to accept automatic emails. |  |
| `ConciergeNotificationsYN` | `concierge_notifications_yn` | Boolean |  | If set to True, notifications are to be sent to the member when the auto email is in Concierge mode. |  |
| `ConciergeYN` | `concierge_yn` | Boolean |  | When set to True, the automated mail is in Concierge mode and is to be approved by the member before being sent to the client. |  |
| `Contact` | `contact` | Resource |  | The prospecting Contact record. | `[Resource]` |
| `ContactKey` | `contact_key` | String |  | This is the foreign key relating to the Contacts Resource. | `-> contacts.contact_key` |
| `DailySchedule` | `daily_schedule` | varchar (multi) | [`daily_schedule`](../lookups.md#daily_schedule) | When Daily is selected as the ScheduleType, a list of days of the week and AM or PM options. |  |
| `DisplayTemplateID` | `display_template_id` | String |  | The system ID of the display that has been related or set as the default to this saved search. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Prospecting record. | `[Collection]` |
| `Language` | `language` | enum | [`languages`](../lookups.md#languages) | The language that will be used in the given automated email. |  |
| `LastNewChangedTimestamp` | `last_new_changed_timestamp` | Timestamp |  | The timestamp of when the prospector last found new or modified listings for an automated email. |  |
| `LastViewedTimestamp` | `last_viewed_timestamp` | Timestamp |  | A timestamp of when the automated email was last viewed by the client in the portal. |  |
| `Media` | `media` | Collection |  | The media related to the Prospecting record. | `[Collection]` |
| `MessageNew` | `message_new` | String |  | The body of the automated email message when the first email is sent for the prospecting campaign. |  |
| `MessageRevise` | `message_revise` | String |  | The body of the automated email message to be used when the criteria or settings of an automated email has been modified. |  |
| `MessageUpdate` | `message_update` | String |  | The body of the automated email message for subsequent email messages after the first email is sent. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The date/time the Prospecting record was last modified. |  |
| `NextSendTimestamp` | `next_send_timestamp` | Timestamp |  | A timestamp of when the automated email is schedule to next send. |  |
| `OwnerMember` | `owner_member` | Resource |  | The member who owns the Prospecting record. | `[Resource]` |
| `OwnerMemberID` | `owner_member_id` | String |  | The local, well-known identifier for the member owning the contact. |  |
| `OwnerMemberKey` | `owner_member_key` | String |  | The unique identifier (key) of the member owning the contact. | `-> member.member_key` |
| `ProspectingKey` | `prospecting_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `ReasonActiveOrDisabled` | `reason_active_or_disabled` | enum | [`reason_active_or_disabled`](../lookups.md#reason_active_or_disabled) | A list of reasons the automated email was set to inactive or set back to active (e.g., Agent Disabled, Over Limit, No Listings Found, Reactivated, Client Disabled). |  |
| `SavedSearch` | `saved_search` | Resource |  | The saved search associated with the Prospecting record. | `[Resource]` |
| `SavedSearchKey` | `saved_search_key` | String |  | This is the foreign key relating to the SavedSearch Resource. | `-> saved_search.saved_search_key` |
| `ScheduleType` | `schedule_type` | enum | [`schedule_type`](../lookups.md#schedule_type) | A selection of the type of schedule that the automated email will be sent (i.e., Daily, Monthly or ASAP). |  |
| `Subject` | `subject` | String |  | The subject line of the automated email being sent. |  |
| `ToEmailList` | `to_email_list` | String |  | A comma-separated list of email addresses that are the "To" address the automated emails are being sent to. |  |

## Foreign keys OUT (this resource references)

- `prospecting.contact_key` -> `contacts.contact_key` (medium)
- `prospecting.owner_member_key` -> `member.member_key` (high)
- `prospecting.saved_search_key` -> `saved_search.saved_search_key` (high)

## Foreign keys IN (other resources reference this)

*(none committed)*

