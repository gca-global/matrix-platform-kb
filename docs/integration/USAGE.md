# USAGE.md - integration views

> Task-oriented entry points for the per-resource integrated view.

## What lives here

- One per-resource integrated page per RESO resource that has
  cross-layer coverage. Each page surfaces:
  - The canonical RESO definition (Layer 1).
  - The Dash / Qobrix / SIR mappings (Layer 2).
  - The canonical state machines (Layer 3).
  - The Sharp-SIR project flavour pipelines (Layer 4).
  - Outbound links to each system-of-record document.

## Quick tasks

### "Show me everything about `Property`"

1. Open
   [`wiki/agent-docs/by_resource/property.md`](wiki/agent-docs/by_resource/property.md).
2. The page is sectioned by layer; jump to the layer you need.

### "Which resources have integrated views?"

1. Open
   [`wiki/agent-docs/_index.md`](wiki/agent-docs/_index.md) for the
   roll-up.
2. The `raw/integration_index.csv` row for each resource shows the
   number of layer touchpoints.

### "I need an integrated view for a resource that doesn't have one"

1. The script generates a page for every Layer-1 resource whose
   `ResourceName` appears in `source-mappings/raw/alignment_*.csv`
   OR in `canonical-processes/raw/citations.csv`. Adding a new
   resource happens automatically once Layer 2 or Layer 3 covers
   it.
2. If you want to force a page for a Layer-1-only resource, add it
   to the `FORCE_RESOURCES` list at the top of
   [`scripts/01_emit_resource_views.py`](scripts/01_emit_resource_views.py)
   and re-emit.

### "I see a stale field on an integrated page"

1. The integrated page is generated. Find the source-of-record
   chapter (cited at the top of each section) and fix it there.
2. Re-run the emit pipeline of that chapter.
3. Re-run `python scripts/01_emit_resource_views.py` here.
4. Run `bash ../../scripts/validate-kb.sh` from the repo root and
   confirm 0 errors.

## Re-emit (the only command you'll run here)

```bash
cd docs/integration
python scripts/01_emit_resource_views.py
```

Re-runs are deterministic - if no upstream input changed, the
diff is zero bytes.

## Read-only or write?

Read: every file under `wiki/agent-docs/` and `raw/`.
Write: only via `scripts/01_emit_resource_views.py`. Hand-editing
generated files is a hard error in
[`AGENTS.md`](AGENTS.md).

## See also

- [`../INTEGRATION.md`](../INTEGRATION.md) - the master
  layer-cake explaining how Layers 1–5 compose.
- [`../data-models/reso-dd-kb/USAGE.md`](../data-models/reso-dd-kb/USAGE.md)
  - Layer 1.
- [`../data-models/source-mappings/USAGE.md`](../data-models/source-mappings/USAGE.md)
  - Layer 2.
- [`../business-processes/canonical-processes/USAGE.md`](../business-processes/canonical-processes/USAGE.md)
  - Layer 3.
- [`../business-processes/index.md`](../business-processes/index.md)
  - Layer 4 (Sharp-SIR flavour).
