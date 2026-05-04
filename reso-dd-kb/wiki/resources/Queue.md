# Queue

Events that have occurred with records in other resources.

**RESO DD 2.0** — 16 fields · last revised 5/12/2018 · [dd.reso.org](https://dd.reso.org/DD2.0/Queue/)

## Groups

- **Other** — 16 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `ClassName` | String List, Single |  | [ClassName](#classname) |  | Name of the class that this queue record is referencing. | [link](https://dd.reso.org/DD2.0/Queue/ClassName/) |
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/Queue/HistoryTransactional/) |
| `ModificationTimestamp` | Timestamp |  |  |  | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/Queue/ModificationTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the Queue record. | [link](https://dd.reso.org/DD2.0/Queue/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/Queue/OriginatingSystemID/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/Queue/OriginatingSystemName/) |
| `OriginatingSystemQueueKey` | String |  |  |  | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/Queue/OriginatingSystemQueueKey/) |
| `QueueTransactionKey` | String |  |  |  | A unique identifier for this record from the immediate source. | [link](https://dd.reso.org/DD2.0/Queue/QueueTransactionKey/) |
| `QueueTransactionType` | String List, Single |  | [QueueTransactionType](#queuetransactiontype) |  | The type of change that the queue transaction record is representing (e.g., Add, Change, Delete). | [link](https://dd.reso.org/DD2.0/Queue/QueueTransactionType/) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://dd.reso.org/DD2.0/Queue/ResourceName/) |
| `ResourceRecordID` | String |  |  |  | The well-known identifier of the related record from the source resource. | [link](https://dd.reso.org/DD2.0/Queue/ResourceRecordID/) |
| `ResourceRecordKey` | String |  |  |  | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey). | [link](https://dd.reso.org/DD2.0/Queue/ResourceRecordKey/) |
| `SourceSystem` | Resource |  |  |  | The source system of the Queue record. | [link](https://dd.reso.org/DD2.0/Queue/SourceSystem/) |
| `SourceSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/Queue/SourceSystemID/) |
| `SourceSystemName` | String |  |  |  | The name of the queue record provider. | [link](https://dd.reso.org/DD2.0/Queue/SourceSystemName/) |
| `SourceSystemQueueKey` | String |  |  |  | The system key, a unique record identifier, from the source system, which is the system from which the record was directly received. | [link](https://dd.reso.org/DD2.0/Queue/SourceSystemQueueKey/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ClassName</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status Change Date:** 4/4/2023
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

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

<details><summary><code>OriginatingSystemQueueKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>QueueTransactionKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>QueueTransactionType</code></summary>

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

<details><summary><code>ResourceRecordID</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ResourceRecordKey</code></summary>

  - **Status:** Active
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 5/12/2018
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
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

<details><summary><code>SourceSystemQueueKey</code></summary>

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

### QueueTransactionType

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/QueueTransactionType/)

| Value | Definition |
|---|---|
| `Add` | The resource record being referenced by the queue does not yet exist in the target and is an addition. |
| `Change` | The resource record being referenced by the queue exists in the target and is being modified. |
| `Delete` | The resource record being referenced by the queue exists in the target and is to be removed. |

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
