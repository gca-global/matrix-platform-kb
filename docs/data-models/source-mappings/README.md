# Source Mappings to RESO DD 2.0

Cross-source field mapping for the Sharp Matrix platform. This is
where Dash, Qobrix, and SIR business-practice fields meet the
canonical RESO DD 2.0 model.

## Why this exists

CDL/Atlas storage is canonical RESO DD 2.0 (snake_case names).
Real-world data flows in from three sources:

- **Dash / Anywhere.com** - SIR-network listing platform; 6 DOCX form
  templates capture the broker-facing field requirements.
- **Qobrix CRM** - legacy Cyprus CRM, exposed via OpenAPI 3.0
  (`raw/qobrix/qobrix_openapi.yaml`, 68k lines, 83 schemas).
- **SIR business practice** - operational checklists encoding the
  brokerage's stage-by-stage listing pipeline.

Each source uses its own naming. To get correct data into and out of
canonical RESO storage we need a deterministic, validated mapping.

## How it works (5-script pipeline)

```
Inventory phase                 Curate phase            Join phase             Emit phase

raw/dash/*.docx          ->  +
raw/qobrix/...yaml       ->  +-> 01,02,03_inventory_*.py -> raw/*_inventory.csv
raw/current-business-... ->  +                                       +
                                                                     +-> 04_join_alignment.py -> raw/alignment_*.csv
raw/mapping_curated.csv  -- (HAND-EDITED) -----------------> +       +
                                                                     +-> 05_emit_mapping_docs.py -> wiki/agent-docs/**
../reso-dd-kb/raw/{fields,lookups,...}.csv  ----------------> +
```

Three phases (Inventory / Curate / Join / Emit) are strictly ordered;
later scripts never write to earlier-phase outputs. Inventories are
mechanical; the curated CSV is the only hand-edited file. Both the
join and the emit are deterministic - re-runs with no upstream change
produce zero-byte diffs.

## In-scope resources

The 6 RESO resources all three sources collectively touch:

| Resource | Why in scope |
|---|---|
| Property | The listing surface (Residential Sale/Rental, Commercial Sale/Lease) |
| Member | Brokers / agents in Dash team forms, Qobrix `Agent`, SIR brokers |
| Office | Branch / office in all three sources |
| Contacts | Sellers / buyers / inquirers (Dash Person form, Qobrix `Contact`, SIR seller cells) |
| Teams | Dash Team form, Qobrix `Group`, SIR marketing/listing teams |
| Media | Qobrix `Media`, SIR/Dash photo requirements |

`ShowingAppointment`, `OpenHouse`, `HistoryTransactional`, and
`Prospecting` are deferred to a follow-up plan.

## Quick start

```bash
cd docs/data-models/source-mappings

# Inventory (read raw sources)
python scripts/01_inventory_dash.py
python scripts/02_inventory_qobrix.py
python scripts/03_inventory_cbp.py

# Curate (hand-edit if upstream changed)
$EDITOR raw/mapping_curated.csv

# Join + Emit (regenerate)
python scripts/04_join_alignment.py
python scripts/05_emit_mapping_docs.py
```

Then read [`wiki/agent-docs/_index.md`](wiki/agent-docs/_index.md) or
the per-resource page you need.

For consumer-facing usage (importer / migration / business-rule
encoding), see [`USAGE.md`](USAGE.md). For the rules an LLM agent must
follow when working in this subtree, see [`AGENTS.md`](AGENTS.md).

## Anchored in harness engineering

This subsystem mirrors the methodology established by
[`../reso-dd-kb/`](../reso-dd-kb/AGENTS.md):

- Phase-gated pipeline (no time travel).
- Deterministic CSV outputs (`csv.QUOTE_MINIMAL`, sorted, stable
  column order).
- Hard-fail verification gates with remediation messages.
- Scoped `AGENTS.md` so the rules travel with the code.
- Generated markdown for agent consumption (progressive disclosure
  via `wiki/agent-docs/` per-resource files).

What it does NOT inherit from `reso-dd-kb`:

- That subtree is "RESO DD 2.0 only". This one is project-specific by
  design - it encodes Sharp Matrix's source-system reality.
