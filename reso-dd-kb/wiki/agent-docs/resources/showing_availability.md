[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `showing_availability` (ShowingAvailability)

> Fields associated with property availability for showings, including method, dates and duration.

## At a glance

| | |
|---|---|
| **Primary key** | `showing_availability_key` |
| **Fields on dd.reso.org** | 12 |
| **Columns in canonical DBML** | 12 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/ShowingAvailability/](https://dd.reso.org/DD2.0/ShowingAvailability/) |
| **Last revised upstream** | 6/16/2022 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the system representing the date/time the ShowingAvailability record was last modified. | ISO-8601 timestamp (UTC). |  |
| `ShowingAvailabilityKey` | `showing_availability_key` | String |  | A system unique identifier. Specifically, the local key to the ShowingAvailability resource. | Unique key for this resource. Use as the FK target whenever another resource references `showing_availability`. | `pk` |
| `ShowingAvailableEndTime` | `showing_available_end_time` | Timestamp |  | End Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | ISO-8601 timestamp (UTC). |  |
| `ShowingAvailableStartTime` | `showing_available_start_time` | Timestamp |  | Start Time of an "available for appointment scheduling" block in ISO-8601 format in Coordinated Universal Time (UTC). | ISO-8601 timestamp (UTC). |  |
| `ShowingDate` | `showing_date` | Date |  | The date that showing appointments can be requested. | Date (YYYY-MM-DD). |  |
| `ShowingId` | `showing_id` | String |  | The well-known identifier for the showing record. The value may be identical to that of the ShowingKey, but the ShowingId is intended to be the value used by a human to retrieve the information about a specific showing. In a multiple-originating or merged system, this value may not be unique and may require the use of the provider system to create a synthetic unique value. | Free-form text, up to 255 characters. |  |
| `ShowingKey` | `showing_key` | String |  | A unique identifier for this record from the immediate source. This is a string that can include a Uniform Resource Identifier (URI) or other forms. This is the local key of the system. When records are received from other systems, a local key is commonly applied. If conveying the original keys from the source or originating systems, see SourceSystemKey and OriginatingSystemKey. | Free-form text, up to 255 characters. |  |
| `ShowingMaximumDuration` | `showing_maximum_duration` | String |  | The maximum block of time available for a showing. If no minimum duration exists, use this field as default. | Free-form text, up to 50 characters. |  |
| `ShowingMethod` | `showing_method` | varchar (multi) | [`showing_method`](../lookups.md#showing_method) | The type of showings (i.e., in-person, virtual, etc.) allowed for the property. | Pick one or more of 3 values from the lookup (closed list). |  |
| `ShowingMinimumDuration` | `showing_minimum_duration` | String |  | The minimum block of time available for a showing. | Free-form text, up to 50 characters. |  |
| `UniqueOrganizationIdentifier` | `unique_organization_identifier` | String |  | This is the unique ID assigned to organizations included in the OUID Resource. Assignment of Unique Organization Identifiers (UOIs) will be centralized and may not be created by systems hosting the OUID Resource. | Free-form text, up to 25 characters. |  |
| `UniversalPropertyId` | `universal_property_id` | String |  | The Universal Property Identifier (UPI) is a unique identifier based on country and local identification methods for all real property in the U.S. and Canada. For cases such as shares of real property, units and other more granular cases, please utilize the UniversalPropertySubId. | Free-form text, up to 128 characters. |  |

## Field disambiguation

Sibling field clusters that an LLM agent commonly confuses. Auto-detected from name shape; resolve which is which by reading each row's full Definition above.

- **`ShowingKey` vs `ShowingId`**:
  - `ShowingKey` - A unique identifier for this record from the immediate source.
  - `ShowingId` - The well-known identifier for the showing record.

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

