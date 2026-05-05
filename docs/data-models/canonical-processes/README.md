# Canonical MLS business processes (RESO DD 2.0 aligned)

The vendor-neutral, RESO-aligned baseline of MLS business processes.

## Why this exists

[`reso-dd-kb/`](../reso-dd-kb/USAGE.md) is the canonical RESO DD 2.0
data model - 41 resources, 1,745 fields, 222 lookups. It tells you
what `Property.StandardStatus = "Pending"` means as a value, but not
what TRANSITIONS in or out of that state, what TRIGGERS them, or
what SIDE EFFECTS those transitions have on other resources.

The data model implies a state machine; this chapter writes that
state machine down and pins it to the data model with mechanically
validated citations.

Canonical means:

- Vendor-neutral. No "Anna sends an email" - that lives in
  [`docs/business-processes/`](../../business-processes/index.md).
- RESO-grounded. Every state, every field, every transition is
  pinned to a real entry in `reso-dd-kb/raw/{resources,fields,
  lookup_values}.csv` via the citation block.
- Implementation-agnostic. Atlas, the CDL, syndication adapters, and
  any future affiliate brokerage all read the same canonical
  baseline.

## How it works (2-script pipeline)

```
Author phase                 Validate phase           Emit phase

processes/*.md          -->  +
  (10 hand-written)          +-> 01_validate_citations.py -> raw/citations.csv
                             +
reso-dd-kb/raw/{resources,   +
  fields,lookup_values}.csv  +
                                                    +
                                                    +-> 02_emit_index.py -> wiki/agent-docs/{_index,state_machines}.md
                                                                          + raw/coverage.csv
```

Three phases (Author / Validate / Emit) are strictly ordered; later
scripts never write to earlier-phase outputs. The 10 process docs
are the only hand-edited files. Validation enforces 5 hard-fail
gates. Emit is deterministic - re-runs with no narrative change
produce zero-byte diffs.

## In-scope processes

| Process | Doc | Primary RESO resources | Primary status lookup(s) |
|---|---|---|---|
| Listing lifecycle | [`processes/listing-lifecycle.md`](processes/listing-lifecycle.md) | `Property`, `HistoryTransactional` | `StandardStatus`, `MlsStatus` |
| Showing lifecycle | [`processes/showing-lifecycle.md`](processes/showing-lifecycle.md) | `ShowingRequest`, `ShowingAppointment`, `ShowingAvailability`, `Showing`, `LockOrBox` | per-resource Status |
| Open house lifecycle | [`processes/open-house-lifecycle.md`](processes/open-house-lifecycle.md) | `OpenHouse` | `OpenHouseStatus`, `OpenHouseType`, `OpenHouseAttendedBy` |
| Lead-Contact lifecycle | [`processes/lead-contact-lifecycle.md`](processes/lead-contact-lifecycle.md) | `Contacts`, `ContactListings`, `ContactListingNotes`, `Prospecting`, `SavedSearch` | `ContactStatus`, `ContactType` |
| Transaction lifecycle | [`processes/transaction-lifecycle.md`](processes/transaction-lifecycle.md) | `HistoryTransactional`, `TransactionManagement` | `StandardStatus` (Pending -> Closed) |
| Member onboarding | [`processes/member-onboarding.md`](processes/member-onboarding.md) | `Member`, `MemberAssociation`, `MemberStateLicense` | `MemberStatus`, `MemberType` |
| Office onboarding | [`processes/office-onboarding.md`](processes/office-onboarding.md) | `Office`, `OfficeAssociation`, `OfficeCorporateLicense`, `OUID` | `OfficeStatus` |
| Team lifecycle | [`processes/team-lifecycle.md`](processes/team-lifecycle.md) | `Teams`, `TeamMembers` | `TeamStatus` |
| Caravan lifecycle | [`processes/caravan-lifecycle.md`](processes/caravan-lifecycle.md) | `Caravan`, `CaravanStop`, `OpenHouse` | `CaravanStatus` |
| Media lifecycle | [`processes/media-lifecycle.md`](processes/media-lifecycle.md) | `Media` | `MediaType`, `MediaCategory` |

`ShowingAppointment`, `Prospecting`, `Rules`, `Queue`,
`InternetTracking`, and other resources play supporting roles inside
the above flows but do not warrant their own dedicated process page
yet.

Out of scope (future plans): saved-search subscription billing,
RESO Web API auth flow, Rules/Queue replay semantics.

## Quick start

```bash
cd docs/data-models/canonical-processes

# Author or revise a process narrative
$EDITOR processes/listing-lifecycle.md

# Validate (5 hard-fail gates)
python scripts/01_validate_citations.py

# Emit catalogue + state-machine index
python scripts/02_emit_index.py
```

Then read [`wiki/agent-docs/_index.md`](wiki/agent-docs/_index.md) or
the per-process page you need.

For consumer-facing usage (state lookup / step implementation /
cross-resource impact), see [`USAGE.md`](USAGE.md). For the rules an
LLM agent must follow when working in this subtree, see
[`AGENTS.md`](AGENTS.md).

## Anchored in harness engineering

This subsystem mirrors the methodology established by
[`../reso-dd-kb/`](../reso-dd-kb/AGENTS.md) and
[`../source-mappings/`](../source-mappings/AGENTS.md):

- Phase-gated pipeline (Author -> Validate -> Emit).
- Hand-edited markdown is the source of truth; everything else is
  generated.
- Mechanically validated citations - dangling `Resource:`, `Field:`,
  or `LookupValue:` cites cause the build to fail.
- Hard-fail verification gates with remediation messages.
- Scoped `AGENTS.md` so the rules travel with the code.
- Generated `_index.md` and `state_machines.md` for agent
  consumption (progressive disclosure).

What it does NOT inherit:

- `reso-dd-kb`'s "RESO DD 2.0 only" boundary - process narratives
  are opinionated by definition, so they live here, not there.
- `source-mappings/`'s project-specific scope - the canonical
  baseline must stay vendor-neutral; project flavours (Sharp SIR,
  affiliates) live in `docs/business-processes/`.
