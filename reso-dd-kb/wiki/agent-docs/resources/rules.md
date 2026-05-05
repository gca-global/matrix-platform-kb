[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `rules` (Rules)

> Business and system rules transmitted from host to client application.

## At a glance

| | |
|---|---|
| **Primary key** | `rule_key` |
| **Fields on dd.reso.org** | 28 |
| **Columns in canonical DBML** | 25 (omits 0 satellite drops + 2 `Resource`-typed + 1 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/Rules/](https://dd.reso.org/DD2.0/Rules/) |
| **Last revised upstream** | 5/12/2018 |

## Fields

Columns in their original `dd.reso.org` page order. **Definition** is the verbatim RESO DD prose (full text, not truncated). **Purpose (when to use)** is auto-derived from the field's role + datatype + lookup + status and tells you, in one sentence, what to write into this column. The `Flags` column shows: `pk`, `fk -> target.col` (committed FK in `canonical.dbml`), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs / inverse-1:N below).

| Field | DBML name | Type | Lookup | Definition | Purpose (when to use) | Flags |
|---|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | The class or table to which the rule refers (i.e., Residential, Residential Lease, Income, Mobile, etc.). | Pick exactly one of 17 values from the lookup (closed list). |  |
| `FieldKey` | `field_key` | String |  | The unique identifier of the field to which the rule applies. This is a foreign key relating to the field found in the resource per the ResourceName field. | Free-form text, up to 255 characters. |  |
| `FieldName` | `field_name` | String |  | The name of the field to which the rule applies. | Free-form text, up to 255 characters. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Rules record. | Inverse 1:N: read as 'all `history_transactional` rows that point at this `rules` row'. Not stored as a column; the FK lives on the child side. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the rule was last modified. | ISO-8601 timestamp (UTC). |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the rule was initially entered. | ISO-8601 timestamp (UTC). |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Rules record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. The originating system is the system with authoritative control over the record (e.g., the name of the MLS where the rule originated). In cases where the originating system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider where the rule is originally input, which is the legal name of the company and most commonly the name of the MLS. | Free-form text, up to 255 characters. |  |
| `OriginatingSystemRuleKey` | `originating_system_rule_key` | String |  | The system key, a unique record identifier, from the originating system. The originating system is the system with authoritative control over the record (e.g., the MLS where the rule originated). There may be cases where the source system (how the record is received) is not the originating system. See Source System Rule Key for more information. | Free-form text, up to 255 characters. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource to which the rule refers (e.g., Property, Member, Office, Open House, etc.). | Pick exactly one of 5 values from the lookup (closed list). |  |
| `RuleAction` | `rule_action` | String |  | The action to be taken when processing the rule. | Free-form text, up to 8000 characters. |  |
| `RuleDescription` | `rule_description` | String |  | A detailed textual description of the rule. | Free-form text, up to 8000 characters. |  |
| `RuleEnabledYN` | `rule_enabled_yn` | Boolean |  | Is the rule currently enabled? | Nullable boolean flag (true / false / null = unknown). |  |
| `RuleErrorText` | `rule_error_text` | String |  | Textual information conveyed when the given rule is in error or fails (e.g., the listing price must be greater than 0). | Free-form text, up to 8000 characters. |  |
| `RuleExpression` | `rule_expression` | String |  | The expression or details of the rule. | Free-form text, up to 8000 characters. |  |
| `RuleFormat` | `rule_format` | enum | [`rule_format`](../lookups.md#rule_format) | The format of the rule (e.g., $filter, JavaScript, REBR). | Pick exactly one of 4 values from the lookup (closed list). |  |
| `RuleHelpText` | `rule_help_text` | String |  | The text that might be displayed on a form that helps the user fix the rule (e.g., enter phone number in the following 10-digit format: ###-###-####). | Free-form text, up to 8000 characters. |  |
| `RuleKey` | `rule_key` | String |  | The primary key of the individual Rule record. | Unique key for this resource. Use as the FK target whenever another resource references `rules`. | `pk` |
| `RuleName` | `rule_name` | String |  | A descriptive name for the rule. | Free-form text, up to 255 characters. |  |
| `RuleOrder` | `rule_order` | Number |  | When in use, execution of rules are to follow the order specified by this field. Any rule that references another field will need to be ordered. | Numeric (integer). |  |
| `RuleType` | `rule_type` | enum | [`rule_type`](../lookups.md#rule_type) | The type of rule (e.g., Validation, Required, Warning, etc.). | Free-form string; the lookup is jurisdiction-defined (no closed value list). |  |
| `RuleVersion` | `rule_version` | String |  | A rule version that uses semantic versioning. See https://semver.org/. | Free-form text, up to 255 characters. |  |
| `RuleWarningText` | `rule_warning_text` | String |  | Textual information conveyed when a given rule has met a condition that warrants a warning message (e.g., sale price entered differs from listing price by more than 25%). | Free-form text, up to 8000 characters. |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Rules record. | Logical reference to another resource; not stored as a scalar column in DBML. Look at the sibling `*Key` / `*Id` field on this resource for where the actual FK value lives. | `[Resource]` |
| `SourceSystemHistoryKey` | `source_system_history_key` | String |  | The system key, a unique record identifier, from the source system. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 255 characters. |  |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. The source system is the system from which the record was directly received. In cases where the source system was not where the record originated (the authoritative system), see the Originating System fields. | Free-form text, up to 25 characters. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the rule record provider, that being the system from which the record was directly received and the legal name of the company. | Free-form text, up to 255 characters. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `rules`)

