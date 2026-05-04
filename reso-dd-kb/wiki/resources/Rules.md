# Rules

Business and system rules transmitted from host to client application.

**RESO DD 2.0** — 28 fields · last revised 5/12/2018 · [dd.reso.org](https://dd.reso.org/DD2.0/Rules/)

## Groups

- **Other** — 28 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) |  | The class or table to which the rule refers (i.e., Residential, Residential Lease, Income, Mobile, etc.). | [link](https://dd.reso.org/DD2.0/Rules/ClassName/) |
| `FieldKey` | String |  |  |  | The unique identifier of the field to which the rule applies. | [link](https://dd.reso.org/DD2.0/Rules/FieldKey/) |
| `FieldName` | String |  |  |  | The name of the field that was changed in the resource record. | [link](https://dd.reso.org/DD2.0/Rules/FieldName/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/Rules/HistoryTransactional/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/Rules/ModificationTimestamp/) |
| `OriginalEntryTimestamp` | Timestamp |  |  |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the rule was initially entered. | [link](https://dd.reso.org/DD2.0/Rules/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the Rules record. | [link](https://dd.reso.org/DD2.0/Rules/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/Rules/OriginatingSystemID/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider where the rule is originally input, which is the legal name of the company and most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/Rules/OriginatingSystemName/) |
| `OriginatingSystemRuleKey` | String |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/Rules/OriginatingSystemRuleKey/) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/Rules/ResourceName/) |
| `RuleAction` | String |  |  |  | The action to be taken when processing the rule. | [link](https://dd.reso.org/DD2.0/Rules/RuleAction/) |
| `RuleDescription` | String |  |  |  | A detailed textual description of the rule. | [link](https://dd.reso.org/DD2.0/Rules/RuleDescription/) |
| `RuleEnabledYN` | Boolean |  |  |  | Is the rule currently enabled? | [link](https://dd.reso.org/DD2.0/Rules/RuleEnabledYN/) |
| `RuleErrorText` | String |  |  |  | Textual information conveyed when the given rule is in error or fails (e.g., the listing price must be greater than 0). | [link](https://dd.reso.org/DD2.0/Rules/RuleErrorText/) |
| `RuleExpression` | String |  |  |  | The expression or details of the rule. | [link](https://dd.reso.org/DD2.0/Rules/RuleExpression/) |
| `RuleFormat` | String List, Single |  | [RuleFormat](#ruleformat) |  | The format of the rule (e.g., $filter, JavaScript, REBR). | [link](https://dd.reso.org/DD2.0/Rules/RuleFormat/) |
| `RuleHelpText` | String |  |  |  | The text that might be displayed on a form that helps the user fix the rule (e.g., enter phone number in the following 10-digit format: ###-###-####). | [link](https://dd.reso.org/DD2.0/Rules/RuleHelpText/) |
| `RuleKey` | String |  |  |  | The primary key of the individual Rule record. | [link](https://dd.reso.org/DD2.0/Rules/RuleKey/) |
| `RuleName` | String |  |  |  | A descriptive name for the rule. | [link](https://dd.reso.org/DD2.0/Rules/RuleName/) |
| `RuleOrder` | Number |  |  |  | When in use, execution of rules are to follow the order specified by this field. | [link](https://dd.reso.org/DD2.0/Rules/RuleOrder/) |
| `RuleType` | String List, Single |  | RuleType |  | The type of rule (e.g., Validation, Required, Warning, etc.). | [link](https://dd.reso.org/DD2.0/Rules/RuleType/) |
| `RuleVersion` | String |  |  |  | A rule version that uses semantic versioning. | [link](https://dd.reso.org/DD2.0/Rules/RuleVersion/) |
| `RuleWarningText` | String |  |  |  | Textual information conveyed when a given rule has met a condition that warrants a warning message (e.g., sale price entered differs from listing price by more than 25%). | [link](https://dd.reso.org/DD2.0/Rules/RuleWarningText/) |
| `SourceSystem` | Resource |  |  |  | The source system of the Rules record. | [link](https://dd.reso.org/DD2.0/Rules/SourceSystem/) |
| `SourceSystemHistoryKey` | String |  |  |  | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/Rules/SourceSystemHistoryKey/) |
| `SourceSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/Rules/SourceSystemID/) |
| `SourceSystemName` | String |  |  |  | The name of the rule record provider, that being the system from which the record was directly received and the legal name of the company. | [link](https://dd.reso.org/DD2.0/Rules/SourceSystemName/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>FieldKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>FieldName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemRuleKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleAction</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleDescription</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleEnabledYN</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleErrorText</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleExpression</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleFormat</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleHelpText</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleOrder</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleType</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleVersion</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>RuleWarningText</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemHistoryKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
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

### ResourceName

5 values · used by 7 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ResourceName/)

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

### RuleFormat

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RuleFormat/)

| Value | Definition |
|---|---|
| `$filter` | Business rules expressed utilizing the OData $filter syntax. |
| `JavaScript` | Business rules expressed utilizing the JavaScript language. |
| `REBR` | Real Estate Business Rule (REBR) notation, based on RuleSpeak-structured notation, uses a predictable syntax to allow humans to clearly and unambiguously specify real estate business rules. |
| `RetsValidation` | Business rules expressed using the well defined RETS 1.9 Validation Expressions. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
