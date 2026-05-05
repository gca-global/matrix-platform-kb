[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `entity_event` (EntityEvent)

> An event log offering an alternative to timestamps, providing an OData-compliant logical timestamp methodology.

## At a glance

| | |
|---|---|
| **Primary key** | `resource_record_key` |
| **Fields on dd.reso.org** | 4 |
| **Columns in canonical DBML** | 4 (omits 0 satellite drops + 0 `Resource`-typed + 0 `Collection`-typed) |
| **Foreign keys OUT / IN** | 0 / 0 |
| **Review markers** | 0 |
| **Source** | [https://dd.reso.org/DD2.0/EntityEvent/](https://dd.reso.org/DD2.0/EntityEvent/) |
| **Last revised upstream** | 6/20/2019 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `EntityEventSequence` | `entity_event_sequence` | Number |  | A unique, system-wide ID that can be used to represent the sequence in which an EntityEvent occurred in a given system. |  |
| `ResourceName` | `resource_name` | String |  | A unique name given to available resources in order to distinguish them within the producer's system. |  |
| `ResourceRecordKey` | `resource_record_key` | String |  | The primary key of the related record or resource, such as ListingKey, OfficeKey or MemberKey, that allows the record to be uniquely identified as an entity so that it may be fetched from the producer's system. | `pk` |
| `ResourceRecordUrl` | `resource_record_url` | String |  | A Uniform Resource Locator (URL) that specifies where consumers may retrieve data corresponding to the given event. |  |

## Foreign keys OUT (this resource references)

*(none committed)*

## Foreign keys IN (other resources reference this)

*(none committed)*

