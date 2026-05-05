# Source Mappings - LLM consumption guide

Three task-oriented entry points. Pick the one that matches what you
are doing, then drill into the per-resource page.

## "I'm building a Dash importer"

You receive a Dash form payload (or you are reading a `BlankForm_*.docx`
to understand which fields exist). Find the RESO target:

1. Open [`wiki/agent-docs/by_source/dash.md`](wiki/agent-docs/by_source/dash.md).
2. Find your Dash field label. The row tells you the RESO resource +
   field name. If marked `Unmapped`, raise an issue - the curator
   needs to add a row to `raw/mapping_curated.csv` (or propose an
   `x_sm_*` extension via [platform-extensions.md](../platform-extensions.md)).
3. For lookup-typed fields (e.g. `View`, `Furnished`, `Heating`), open
   [`wiki/agent-docs/lookup_value_mappings.md`](wiki/agent-docs/lookup_value_mappings.md)
   to translate Dash's value to the RESO canonical value.
4. For Property specifically, also read
   [`wiki/agent-docs/by_resource/property.md`](wiki/agent-docs/by_resource/property.md)
   - the "Coverage gaps" section flags fields Dash does not carry that
   you may need to default or pull from another source (e.g. SIR
   business-practice).

## "I'm consuming or migrating from Qobrix"

You are reading from the Qobrix REST API (described in
[`../../references/qobrix-api-summary.md`](../../references/qobrix-api-summary.md))
and need to project Qobrix payloads onto canonical RESO storage.

1. Open [`wiki/agent-docs/by_source/qobrix.md`](wiki/agent-docs/by_source/qobrix.md).
2. Find your Qobrix property path (JSON-Pointer style, e.g.
   `Property/list_selling_price_amount`). The row tells you the RESO
   target field. Confidence column flags semantic-approximate cases
   (e.g. `NewConstructionYN` is a derived approximation - read the
   notes column).
3. For lookup-typed fields, use
   [`wiki/agent-docs/lookup_value_mappings.md`](wiki/agent-docs/lookup_value_mappings.md)
   - especially for `PropertySubType`, `View`, `Furnished`, `Heating`,
   `StandardStatus`.
4. The legacy [`property-field-mapping.md`](../property-field-mapping.md)
   is now a redirect stub; its content was migrated into
   `mapping_curated.csv` and now flows into the generated docs.

## "I'm encoding business-practice rules"

You are implementing a workflow step from the SIR listing checklists
(or [`../../business-processes/listing-checklist.md`](../../business-processes/listing-checklist.md)).

1. Open [`wiki/agent-docs/by_source/sir-business-practice.md`](wiki/agent-docs/by_source/sir-business-practice.md).
2. Each checklist row maps to a RESO field (or a derived signal). The
   `pipeline_stage` column tells you when in the listing lifecycle the
   data must be present (use this to drive RLS / required-fields rules
   per stage).
3. Several SIR checklist items don't have RESO equivalents - they
   surface as `x_sm_*` extensions in
   [`wiki/agent-docs/extensions.md`](wiki/agent-docs/extensions.md).

## Per-resource deep dive

| Resource | Doc | When to read |
|---|---|---|
| Property | [`wiki/agent-docs/by_resource/property.md`](wiki/agent-docs/by_resource/property.md) | Building or consuming listings |
| Member | [`wiki/agent-docs/by_resource/member.md`](wiki/agent-docs/by_resource/member.md) | Mapping brokers / agents (RESO `Member`) |
| Office | [`wiki/agent-docs/by_resource/office.md`](wiki/agent-docs/by_resource/office.md) | Mapping branches / offices |
| Contacts | [`wiki/agent-docs/by_resource/contacts.md`](wiki/agent-docs/by_resource/contacts.md) | Sellers / buyers / inquirers |
| Teams | [`wiki/agent-docs/by_resource/teams.md`](wiki/agent-docs/by_resource/teams.md) | Listing teams, marketing teams |
| Media | [`wiki/agent-docs/by_resource/media.md`](wiki/agent-docs/by_resource/media.md) | Photos, floor plans, virtual tours |

## Refreshing the mapping

When upstream sources change (Dash adds a form field, Qobrix releases a
new schema, SIR updates a checklist):

```bash
cd docs/data-models/source-mappings
python scripts/01_inventory_dash.py     # rebuild dash_inventory.csv
python scripts/02_inventory_qobrix.py   # rebuild qobrix_inventory.csv
python scripts/03_inventory_cbp.py      # rebuild cbp_inventory.csv
# Manually review diffs; edit raw/mapping_curated.csv as needed.
python scripts/04_join_alignment.py     # enforces the 5 hard-fail gates
python scripts/05_emit_mapping_docs.py  # regenerates wiki/agent-docs/
```

The pipeline is deterministic - re-running with no upstream changes
produces zero-byte diffs.

## What this directory does NOT replace

- [`../reso-dd-kb/`](../reso-dd-kb/USAGE.md) - the canonical RESO model
  itself. Read that for "what does RESO say about field X".
- [`../platform-extensions.md`](../platform-extensions.md) - the
  governance catalogue for `x_sm_*` extensions. This directory
  surfaces extension candidates; the catalogue formally adopts them.
- [`../cdl-schema.md`](../cdl-schema.md) - the actual CDL Postgres
  schema. The mapping defines name correspondences; the CDL doc is
  what the Postgres tables actually look like.
