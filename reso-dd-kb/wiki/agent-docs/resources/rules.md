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

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `ClassName` | `class_name` | enum | [`class_name`](../lookups.md#class_name) | The class or table to which the rule refers (i.e., Residential, Residential Lease, Income, Mobile, etc.). |  |
| `FieldKey` | `field_key` | String |  | The unique identifier of the field to which the rule applies. |  |
| `FieldName` | `field_name` | String |  | The name of the field to which the rule applies. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | The history of the Rules record. | `[Collection]` |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the rule was last modified. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the rule was initially entered. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Rules record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider where the rule is originally input, which is the legal name of the company and most commonly the name of the MLS. |  |
| `OriginatingSystemRuleKey` | `originating_system_rule_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `ResourceName` | `resource_name` | enum | [`resource_name`](../lookups.md#resource_name) | The resource to which the rule refers (e.g., Property, Member, Office, Open House, etc.). |  |
| `RuleAction` | `rule_action` | String |  | The action to be taken when processing the rule. |  |
| `RuleDescription` | `rule_description` | String |  | A detailed textual description of the rule. |  |
| `RuleEnabledYN` | `rule_enabled_yn` | Boolean |  | Is the rule currently enabled? |  |
| `RuleErrorText` | `rule_error_text` | String |  | Textual information conveyed when the given rule is in error or fails (e.g., the listing price must be greater than 0). |  |
| `RuleExpression` | `rule_expression` | String |  | The expression or details of the rule. |  |
| `RuleFormat` | `rule_format` | enum | [`rule_format`](../lookups.md#rule_format) | The format of the rule (e.g., $filter, JavaScript, REBR). |  |
| `RuleHelpText` | `rule_help_text` | String |  | The text that might be displayed on a form that helps the user fix the rule (e.g., enter phone number in the following 10-digit format: ###-###-####). |  |
| `RuleKey` | `rule_key` | String |  | The primary key of the individual Rule record. | `pk` |
| `RuleName` | `rule_name` | String |  | A descriptive name for the rule. |  |
| `RuleOrder` | `rule_order` | Number |  | When in use, execution of rules are to follow the order specified by this field. |  |
| `RuleType` | `rule_type` | enum | [`rule_type`](../lookups.md#rule_type) | The type of rule (e.g., Validation, Required, Warning, etc.). |  |
| `RuleVersion` | `rule_version` | String |  | A rule version that uses semantic versioning. |  |
| `RuleWarningText` | `rule_warning_text` | String |  | Textual information conveyed when a given rule has met a condition that warrants a warning message (e.g., sale price entered differs from listing price by more than 25%). |  |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Rules record. | `[Resource]` |
| `SourceSystemHistoryKey` | `source_system_history_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemID` | `source_system_id` | String |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the rule record provider, that being the system from which the record was directly received and the legal name of the company. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

## Inverse 1:N (collection-typed companions)

- `history_transactional` -> `history_transactional` (many `history_transactional` per `rules`)

