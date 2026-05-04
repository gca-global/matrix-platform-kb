# OtherPhone

Additional phone numbers for contacts or members, with type information.

**RESO DD 2.0** — 10 fields · last revised 4/4/2023 · [dd.reso.org](https://dd.reso.org/DD2.0/OtherPhone/)

**Adoption** — weighted Org%: **0%** across 8 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 10 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) |  | Name of the class to which the record is referencing. | [link](https://dd.reso.org/DD2.0/OtherPhone/ClassName/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/OtherPhone/HistoryTransactional/) |
| `ModificationTimestamp` | Timestamp |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/OtherPhone/ModificationTimestamp/) |
| `OtherPhoneExt` | String |  |  | 0% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/OtherPhone/OtherPhoneExt/) |
| `OtherPhoneKey` | String |  |  | 0% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/OtherPhone/OtherPhoneKey/) |
| `OtherPhoneNumber` | String |  |  | 0% | The phone option allowing members to convey additional phone numbers other than those already covered by the MemberMobilePhone, MemberFax and other specified fields. | [link](https://dd.reso.org/DD2.0/OtherPhone/OtherPhoneNumber/) |
| `OtherPhoneType` | String List, Single |  | [OtherPhoneType](#otherphonetype) | 0% | The type of phone record that does not already exist in the given phone fields or if a second of any type of phone field is needed (i.e., HomePhone2, BrothersPhone, etc.). | [link](https://dd.reso.org/DD2.0/OtherPhone/OtherPhoneType/) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) | 0% | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/OtherPhone/ResourceName/) |
| `ResourceRecordID` | String |  |  | 0% | The well-known identifier of the related record from the source resource. | [link](https://dd.reso.org/DD2.0/OtherPhone/ResourceRecordID/) |
| `ResourceRecordKey` | String |  |  | 0% | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). | [link](https://dd.reso.org/DD2.0/OtherPhone/ResourceRecordKey/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OtherPhoneExt</code></summary>

  - **BEDES:** Telephone Number Label = "Other"Telephone Extension = [value]
  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OtherPhoneKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OtherPhoneNumber</code></summary>

  - **BEDES:** Telephone Number Label = "Other"Telephone Number = [value]
  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OtherPhoneType</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceRecordID</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceRecordKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/26/2017
  - **Added in Version:** 1.7.0

</details>

## Lookups

### ClassName

17 values · used by 8 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ClassName/)

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

### OtherPhoneType

14 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OtherPhoneType/)

| Value | Definition |
|---|---|
| `Direct` | This is the contact's direct number. |
| `Fax` | This is the contact's fax. |
| `First` | This is the contact's first preferred phone. |
| `Home` | This is the contact's home phone. |
| `Mobile` | This is the contact's mobile phone. |
| `Modem` | This is the contact's modem. |
| `Office` | This is the contact's office phone. |
| `Pager` | This is the contact's pager. |
| `Preferred` | This is the contact's preferred phone. |
| `Second` | This is the contact's second preferred phone. |
| `SMS` | This is the contact's SMS/text number. |
| `Third` | This is the contact's third preferred phone. |
| `Toll Free` | This is the contact's toll-free number. |
| `Voicemail` | This is the contact's voicemail. |

### ResourceName

5 values · used by 7 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ResourceName/)

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
