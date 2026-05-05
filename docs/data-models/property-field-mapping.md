# Property field mapping (Dash / Qobrix / SIR -> RESO DD 2.0)

> **Moved.** This document has been superseded by the auto-generated, gate-validated source-mapping pipeline.

## Where to read now

- **Property field-by-field mapping**: [`source-mappings/wiki/agent-docs/by_resource/property.md`](source-mappings/wiki/agent-docs/by_resource/property.md)
- **All resources covered (Property, Member, Office, Contacts, Teams, Media)**: [`source-mappings/wiki/agent-docs/_index.md`](source-mappings/wiki/agent-docs/_index.md)
- **Per-source views (Dash / Qobrix / SIR)**: [`source-mappings/wiki/agent-docs/by_source/`](source-mappings/wiki/agent-docs/by_source/)
- **Lookup value translations** (e.g. Qobrix `mountain_view` -> RESO `View.Mountain(s)`): [`source-mappings/wiki/agent-docs/lookup_value_mappings.md`](source-mappings/wiki/agent-docs/lookup_value_mappings.md)
- **`x_sm_*` extensions surfaced by gap analysis**: [`source-mappings/wiki/agent-docs/extensions.md`](source-mappings/wiki/agent-docs/extensions.md)

## Why the move

The old hand-curated table in this file drifted out of sync with both the
upstream source schemas (Qobrix OpenAPI, Dash DOCX forms, SIR XLSX
checklists) and the canonical [`reso-dd-kb/`](reso-dd-kb/USAGE.md)
field catalogue. The new pipeline:

1. Inventories each upstream source mechanically (`scripts/01..03_inventory_*.py`).
2. Joins those inventories with a single hand-curated CSV
   (`raw/mapping_curated.csv`) and the canonical RESO DD fields/lookups,
   enforcing five hard-fail gates that catch dangling references.
3. Emits the per-resource and per-source markdown deterministically.

For background and the regen workflow, read
[`source-mappings/README.md`](source-mappings/README.md) and
[`source-mappings/AGENTS.md`](source-mappings/AGENTS.md).

This stub remains so existing links into `property-field-mapping.md`
keep resolving.
