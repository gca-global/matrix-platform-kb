# Canonical processes - LLM consumption guide

Three task-oriented entry points. Pick the one that matches what you
are doing, then drill into the per-process page.

## "I need to know what a state means"

You see a record with `Property.StandardStatus = "Pending"` (or
`ShowingRequest.Status = "Approved"`, etc.) and need to know what
that state implies operationally.

1. Open [`wiki/agent-docs/state_machines.md`](wiki/agent-docs/state_machines.md).
2. Find the lookup whose name matches your field. The state diagram
   shows every legal target state and how to get there.
3. For the full transition semantics (trigger, actor, required field
   changes, side effects), open the corresponding process doc -
   `processes/<process>-lifecycle.md`.

## "I need to implement a state-changing step"

You are writing code (an Edge Function, a UI flow, a syndication
adapter) that changes a record's state.

1. Identify the source state and target state. Open the matching
   process doc in `processes/`.
2. Read the row in the **Transitions** table for that
   (from -> to) edge. It tells you:
   - The trigger (what event caused the transition).
   - The actor (broker / system / external).
   - The fields you must update atomically with the status change.
   - Side effects on other resources (showings, contacts, media,
     transactions).
3. Cross-check with [`reso-dd-kb/wiki/agent-docs/resources/<snake>.md`](../../data-models/reso-dd-kb/wiki/agent-docs/_index.md)
   for the canonical field definition.
4. If the transition you need is NOT in the table, raise an issue -
   adding undocumented transitions silently is forbidden.

## "I need to know cross-resource impact of a state change"

You are about to change `Property.StandardStatus` from Active to
Pending. What else needs to happen?

1. Open `processes/<process>-lifecycle.md` for the originating
   resource (Property -> `processes/listing-lifecycle.md`).
2. Read the **Cross-resource interactions** section. It enumerates
   downstream effects on Showings, Contacts, Media, Transactions.
3. Cross-check the **state machine** in the affected resource's own
   process doc - e.g. `processes/showing-lifecycle.md` for showing
   side effects.

## Per-process deep dive

| Process | Doc | Primary RESO resources |
|---|---|---|
| Listing lifecycle | [`processes/listing-lifecycle.md`](processes/listing-lifecycle.md) | `Property`, `HistoryTransactional` |
| Showing lifecycle | [`processes/showing-lifecycle.md`](processes/showing-lifecycle.md) | `ShowingRequest`, `ShowingAppointment`, `ShowingAvailability`, `Showing`, `LockOrBox` |
| Open house lifecycle | [`processes/open-house-lifecycle.md`](processes/open-house-lifecycle.md) | `OpenHouse` |
| Lead-Contact lifecycle | [`processes/lead-contact-lifecycle.md`](processes/lead-contact-lifecycle.md) | `Contacts`, `ContactListings`, `ContactListingNotes`, `Prospecting`, `SavedSearch` |
| Transaction lifecycle | [`processes/transaction-lifecycle.md`](processes/transaction-lifecycle.md) | `HistoryTransactional`, `TransactionManagement` |
| Member onboarding | [`processes/member-onboarding.md`](processes/member-onboarding.md) | `Member`, `MemberAssociation`, `MemberStateLicense` |
| Office onboarding | [`processes/office-onboarding.md`](processes/office-onboarding.md) | `Office`, `OfficeAssociation`, `OfficeCorporateLicense`, `OUID` |
| Team lifecycle | [`processes/team-lifecycle.md`](processes/team-lifecycle.md) | `Teams`, `TeamMembers` |
| Caravan lifecycle | [`processes/caravan-lifecycle.md`](processes/caravan-lifecycle.md) | `Caravan`, `CaravanStop`, `OpenHouse` |
| Media lifecycle | [`processes/media-lifecycle.md`](processes/media-lifecycle.md) | `Media` |

## Cross-cutting pages

- [`wiki/agent-docs/_index.md`](wiki/agent-docs/_index.md) - process
  catalogue, per-resource and per-`*Status`-lookup coverage matrices.
- [`wiki/agent-docs/state_machines.md`](wiki/agent-docs/state_machines.md) -
  consolidated mermaid index of every state diagram in this chapter.

## Refreshing the catalogue

When a process doc changes (state added, transition revised):

```bash
cd docs/data-models/canonical-processes
$EDITOR processes/<process>-lifecycle.md
python scripts/01_validate_citations.py     # enforces the 5 hard-fail gates
python scripts/02_emit_index.py             # regenerates wiki/agent-docs/ + raw/coverage.csv
```

The pipeline is deterministic - re-running with no narrative changes
produces zero-byte diffs.

## What this directory does NOT replace

- [`reso-dd-kb/`](../../data-models/reso-dd-kb/USAGE.md) - the canonical RESO
  data model itself. Read that for "what does RESO say about field
  X". This chapter cites those entries; it does not redefine them.
- [`source-mappings/`](../../data-models/source-mappings/USAGE.md) - the
  Dash/Qobrix/SIR -> RESO field mapping. That subtree handles
  inbound/outbound name correspondence; this subtree handles
  state-machine semantics.
- [`docs/business-processes/`](../index.md) -
  Sharp-SIR's actual operational flow with project-specific stage
  names and human roles. Sharp SIR's flow maps INTO the canonical
  baseline here, but the SIR-flavoured docs stay where they are.
- [`platform-extensions.md`](../../data-models/platform-extensions.md) - governs
  `x_sm_*` extensions. If a process needs a state RESO doesn't model,
  surface it as an extension there first; it must not appear in this
  chapter's citation block until adopted.
