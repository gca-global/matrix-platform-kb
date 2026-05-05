# Integration views (Layer 5: per-resource cross-cutting)

The thinnest, most derivative layer of the KB. One page per RESO
resource, joining Layers 1–4 onto a single screen.

## Why this exists

Even with [`INTEGRATION.md`](../INTEGRATION.md) explaining how the
four substantive layers compose, an agent investigating a single
resource still has to navigate four chapters. This chapter
flattens that into one page per resource: open
`wiki/agent-docs/by_resource/property.md` and you see the canonical
RESO definition, the Dash / Qobrix / SIR mappings, the canonical
state machines, and the Sharp-SIR pipelines that touch `Property`.

## How it works (1-script pipeline)

```
Emit phase
                                 +
data-models/reso-dd-kb/raw/...   +
data-models/source-mappings/raw/...+
business-processes/canonical-    +
  processes/raw/citations.csv    +-> 01_emit_resource_views.py -> wiki/agent-docs/by_resource/<res>.md
business-processes/canonical-    +                                + raw/integration_index.csv
  processes/processes/*.md       +                                + wiki/agent-docs/_index.md
business-processes/*.md (flavour)+
```

There is no Author and no Validate phase: this chapter has no
hand-edited markdown. The only logic is the emit script. Re-runs
are deterministic.

## In-scope per-resource pages

A page is emitted for every resource that appears in EITHER

- `data-models/source-mappings/raw/alignment_*.csv` (Layer 2 has
  curated mappings for it), OR
- `business-processes/canonical-processes/raw/citations.csv` (Layer
  3 has at least one process documenting it).

That set currently includes (but is not limited to):
`Property`, `Member`, `Office`, `Contacts`, `Teams`, `Media`,
plus every additional resource cited by a canonical process
(`Showing*`, `LockOrBox`, `OpenHouse`, `Caravan`, `CaravanStop`,
`HistoryTransactional`, `TransactionManagement`, `MemberAssociation`,
`MemberStateLicense`, `OfficeAssociation`, `OfficeCorporateLicense`,
`OUID`, `Prospecting`, `SavedSearch`, `ContactListings`,
`ContactListingNotes`, `TeamMembers`).

## Page layout (per resource)

Every generated page follows the same skeleton:

1. **Header** — resource name, RESO field count, layer touchpoint
   summary.
2. **Layer 1 — canonical RESO definition** — link to
   `reso-dd-kb/wiki/agent-docs/resources/<res>.md`, plus an inline
   field count and the resource's RESO description.
3. **Layer 2 — source mappings** — if Layer 2 covers the resource:
   link to `source-mappings/wiki/agent-docs/by_resource/<res>.md`,
   plus a row count from `alignment_<res>.csv`. If not in scope,
   says "not yet in scope; promote when needed".
4. **Layer 3 — canonical state machines** — list of canonical
   processes citing this resource, each linked to its
   `canonical-processes/processes/<proc>.md`.
5. **Layer 4 — Sharp-SIR flavour** — hand-encoded mapping of the
   resource to the Sharp-SIR pipeline / checklist files (per
   `FLAVOUR_LINKS` in the script).
6. **Determinism note** — "this page is generated; do NOT
   hand-edit".

## Quick start

```bash
cd docs/integration

# Re-emit (deterministic; no inputs changed = zero-byte diff)
python scripts/01_emit_resource_views.py
```

Then read [`wiki/agent-docs/_index.md`](wiki/agent-docs/_index.md)
or the per-resource page you need.

For consumer-facing usage, see [`USAGE.md`](USAGE.md). For the
rules an LLM agent must follow when working in this subtree, see
[`AGENTS.md`](AGENTS.md).

## Anchored in harness engineering

This subsystem mirrors the methodology of the other generative
chapters but is even thinner:

- One emit phase, no Author / Validate phases.
- Hand-edited markdown is forbidden; the script is the only place
  that can change generated output.
- Determinism — re-runs with no input changes produce zero-byte
  diffs.
- Cross-chapter freshness enforced by `validate-kb.sh` Check 8.
