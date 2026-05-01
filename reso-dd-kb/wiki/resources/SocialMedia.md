# SocialMedia

_RESO Data Dictionary 2.0 resource — 10 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/SocialMedia+Resource) for the canonical page._

**Adoption** — weighted Org%: **4%** across 9 measured fields (median 1%, avg 4%).

## Groups

- **Other** — 10 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) | 5% | 1% | Name of the class to which the record is referencing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135822) |
| `DisplayName` | String |  |  |  | 8% | The display name for the field. | [link](https://ddwiki.reso.org/display/DDW20/DisplayName+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135834) |
| `ModificationTimestamp` | Timestamp |  |  | 10% | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135840) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) | 10% | 1% | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135846) |
| `ResourceRecordID` | String |  |  | 5% | 1% | The well-known identifier of the related record from the source resource. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135853) |
| `ResourceRecordKey` | String |  |  |  | 1% | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135859) |
| `SocialMediaKey` | String |  |  | 10% | 1% | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/SocialMediaKey+Field) |
| `SocialMediaType` | String List, Single |  | [SocialMediaType](#socialmediatype) | 10% | 1% | A list of types of sites or social media that a member Uniform Resource Locator (URL) or ID is referring to (e.g., Website, Blog, Facebook, Twitter, LinkedIn, Instagram). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135871) |
| `SocialMediaUrlOrId` | String |  |  |  | 8% | The website URL or ID of the social media site or account of the member. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2117201) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>DisplayName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 08 2021
  - **Revision Date:** DEC 08 2021
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceRecordID</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SocialMediaKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 26 2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SocialMediaType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** APR 11 2022
  - **Added in Version:** 1.7.0

</details>

## Lookups

### ClassName

| Value | Definition |
|---|---|
| `Business Opportunity` | The class, sometimes known as property type, is a business for sale. |
| `Commercial Lease` | The class, sometimes known as property type, is a commercial property for lease. |
| `Commercial Sale` | The class, sometimes known as property type, is a commercial property for sale. |
| `Contacts` | The class is the collection of the member's contacts/clients. |
| `Cross Property` | The class, sometimes known as property type, is a collection of all listing property types. |
| `Farm` | The class, sometimes known as property type, is a farm. |
| `History Transactional` | The class is the transactional history of another class. |
| `Land` | The class, sometimes known as property type, is land for sale or lease. |
| `Manufactured In Park` | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| `Media` | The class is one that contains records referencing media files. |
| `Member` | The class containing member records. |
| `Office` | The class containing office records. |
| `Open House` | The class containing open house records. |
| `Residential` | The class, sometimes known as property type, is residential property for sale. |
| `Residential Income` | The class, sometimes known as property type, is income or multifamily property for sale. |
| `Residential Lease` | The class, sometimes known as property type, is residential property for lease. |
| `Saved Search` | The class containing saved search data. |

### ResourceName

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

### SocialMediaType

| Value | Definition |
|---|---|
| `Blog` | Information pertaining to the blog of the member/office/contact. |
| `Digg` | Information pertaining to the Digg account of the member/office/contact. |
| `Facebook` | Information pertaining to the Facebook account of the member/office/contact. |
| `Facebook Messenger` | Information pertaining to the Facebook Messenger contact information of the member/office/contact. |
| `GooglePlus` | Information pertaining to the GooglePlus account of the member/office/contact. |
| `iMessage` | Information pertaining to the iMessage contact information of the member/office/contact. |
| `Instagram` | Information pertaining to the Instagram account of the member/office/contact. |
| `LinkedIn` | Information pertaining to the LinkedIn account of the member/office/contact. |
| `Pinterest` | Information pertaining to the Pinterest account of the member/office/contact. |
| `Reddit` | Information pertaining to the Reddit account of the member/office/contact. |
| `Slack` | Information pertaining to the Slack account of the member/office/contact. |
| `Snapchat` | Information pertaining to the Snapchat account of the member/office/contact. |
| `StumbleUpon` | Information pertaining to the StumbleUpon account of the member/office/contact. |
| `Tumblr` | Information pertaining to the Tumblr account of the member/office/contact. |
| `Twitter` | Information pertaining to the X (formerly Twitter) account of the member/office/contact. |
| `Website` | Information pertaining to the website of the member/office/contact. |
| `YouTube` | Information pertaining to the YouTube account of the member/office/contact. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
