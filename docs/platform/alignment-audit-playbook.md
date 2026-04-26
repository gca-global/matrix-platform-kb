# Alignment Audit Playbook — Eliminating Schema ↔ Code ↔ UI Drift

> A reusable, agent-executable playbook for a **systematic alignment audit** of any
> Matrix App (or any app with a typed frontend + Postgres backend).
>
> **Goal**: eliminate drift between
> **DB schema ↔ generated types ↔ application code ↔ UI labels ↔ backend
> functions ↔ permission / route / page keys** — and leave the codebase
> internally consistent, mechanically enforceable, and manageable by a small
> team aided by agents.
>
> **Style**: harness-style cleanup per OpenAI's
> [*Harness engineering* (Feb 2026)][harness] — small, reviewable, reversible
> diffs; one concern per stage; explicit invariants; verifiable after each
> step; invariants promoted into lints/migrations so the drift cannot return.
>
> **Output contract**: the agent produces a **findings table + staged plan +
> recommendation** first, then waits for explicit human approval before any
> code or migration is written.

[harness]: https://openai.com/index/harness-engineering/

---

## When to run this playbook

Run an alignment audit whenever one or more of these signal that the
schema ↔ code ↔ UI contract is decaying:

- A feature that looked correct in the form silently saves to the wrong column.
- Two list views of the same entity show subtly different fields.
- A RESO-flavoured name appears alongside a Dash-flavoured name for the
  same value.
- An Edge Function exists whose responsibility overlaps with another EF or
  with direct PostgREST access.
- Permission / route / page keys are typed as plain strings and typos do
  not produce a compile error.
- An incomplete rename left the old column, old FK name, or old i18n key behind.
- The app uses denormalised mirror columns (e.g. `office_name` duplicated
  alongside `office_id`) that drift.

If none of these apply, do not run the playbook — cost outweighs reward.

---

## Operating principles (the invariants the audit defends)

These are the principles the audit exists to restore. They are the
*target state*; findings are deviations from them.

1. **Single source of truth.** For every concept (money, status, role,
   page key, entity name) there is exactly *one* authoritative location.
   Everything else derives from it or is deleted. Computed values (totals,
   counters, cached display names) are never written by hand.
2. **Names must match across layers.** A field in the DB, its generated
   type, its form schema, its i18n key, its UI label, and its API/function
   payload use the same vocabulary. No silent aliases, no shims "for
   safety".
3. **Relations are enforced, not assumed.** Every cross-table link is a
   real `FOREIGN KEY` with an explicit `ON DELETE` rule. Denormalised
   mirrors are either removed or kept in sync by trigger — never both at
   once, never neither.
4. **Keys live in typed registries.** Permission keys, route keys, enum
   values, page keys, and entity names live in typed modules (TypeScript
   `as const` objects or Zod enums). Strings drift; enums do not.
5. **Backend functions have one responsibility each.** Overlapping
   responsibilities are consolidated, or the overlap is documented in a
   per-function README with a date-stamped reason.
6. **Parse at the boundary.** Every inbound payload (form, HTTP, EF
   request, webhook) is validated by a schema *at the edge*. The inside
   of the app trusts its own types. See
   [parse-don't-validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/).
7. **No YOLO probing.** Every assumption about DB shape is backed by a
   real introspection query, by generated types, or by a typed SDK —
   never by guessing from a screenshot or from one file's imports.
8. **Validate against domain best practice.** Identify the domain the
   app operates in (real-estate MLS, CRM, HRMS, ITSM, fintech) and check
   the current implementation against established conventions for that
   domain (RESO DD for MLS, ITIL for ITSM, etc.). If something
   contradicts the norm, *flag it* — do not silently "fix" it.

> **Harness-engineering link**: these invariants play the role of the
> [*golden principles*][harness] that recurring cleanup agents enforce.
> After each merged stage, promote the new invariant into
> [`GOLDEN_PRINCIPLES.md`](../GOLDEN_PRINCIPLES.md) so it defends itself
> mechanically forever after.

---

## Audit dimensions

For each dimension, produce `findings → proposed change → risk → rollback`.
The dimensions are deliberately orthogonal so stages can ship
independently.

| # | Dimension | What drift looks like |
|---|-----------|-----------------------|
| D1 | **Data-model duplication** | Multiple sources of truth for the same value; legacy columns superseded by junction tables; denormalised mirrors that go stale; totals written directly instead of computed. |
| D2 | **Naming drift** | Incomplete renames; FK constraints using old names; shim exports kept "for safety"; orphaned aliases; RESO and Dash names coexisting for the same field. |
| D3 | **UI label / variable mismatch** | Form writes column A; list view reads denormalised column B; i18n key says X, schema field is Y; permission key and page label diverge. |
| D4 | **Relational integrity** | Tables with zero FKs; orphan-prone columns; missing `ON DELETE` rules; missing unique constraints on natural keys; nullable columns that should be `NOT NULL`. |
| D5 | **Backend functions / API endpoints** | Overlapping responsibilities; inconsistent invocation paths (some routes hit the EF, others bypass it and write directly); missing or stale contract docs. |
| D6 | **Permission / route / page-key registry** | Mixed naming conventions (`kebab-case` vs `snake_case` vs `camelCase` for the same concept); no central typed list; typos cause silent failures instead of type errors. |
| D7 | **Domain correctness** | Workflows, statuses, and lifecycle transitions that contradict the conventions of the app's domain (e.g. listing lifecycle that skips "Coming Soon"; ITSM ticket statuses that aren't ITIL-shaped; vacation workflow missing manager approval). |

---

## Evidence-collection protocol (do this first, do not skip)

Harness-style audits are grounded in **runtime evidence**, not in prose.
Before producing a single finding, the agent must gather and paste
concrete evidence. The four legible sources:

### 1. Database introspection (authoritative)

Run these against the target project (SSO, CDL, or per-app DB) via MCP
Supabase tools or `psql`. Paste the outputs verbatim into the findings.

```sql
-- Tables + row counts (spot orphan or empty tables)
SELECT schemaname, relname, n_live_tup
  FROM pg_stat_user_tables
 WHERE schemaname = 'public'
 ORDER BY relname;

-- Foreign keys + ON DELETE rules (spot D4 drift)
SELECT conrelid::regclass AS table,
       conname,
       pg_get_constraintdef(oid) AS definition
  FROM pg_constraint
 WHERE contype = 'f' AND connamespace = 'public'::regnamespace
 ORDER BY 1, 2;

-- Tables with ZERO foreign keys (smells like D4)
SELECT c.relname
  FROM pg_class c
  JOIN pg_namespace n ON n.oid = c.relnamespace
 WHERE n.nspname = 'public' AND c.relkind = 'r'
   AND NOT EXISTS (
     SELECT 1 FROM pg_constraint k
      WHERE k.conrelid = c.oid AND k.contype = 'f')
 ORDER BY 1;

-- Enums + allowed values (cross-check with TS registries)
SELECT t.typname, array_agg(e.enumlabel ORDER BY e.enumsortorder)
  FROM pg_type t JOIN pg_enum e ON e.enumtypid = t.oid
 GROUP BY t.typname;

-- Columns that look like denormalised mirrors (D1)
SELECT table_name, column_name
  FROM information_schema.columns
 WHERE table_schema = 'public'
   AND (column_name LIKE '%_name' OR column_name LIKE '%_label'
        OR column_name LIKE '%_display')
 ORDER BY 1, 2;
```

### 2. Generated types vs DB (must be byte-equal)

```bash
# Matrix apps regenerate TS types from Supabase
supabase gen types typescript --project-id <ref> > src/integrations/supabase/types.ts
git diff src/integrations/supabase/types.ts
```

A non-empty diff *is* a finding.

### 3. Code search for known drift patterns

Use ripgrep (not grep). Concrete patterns to run:

```bash
# Silent aliases / shim exports
rg -n "export .* as .* // (shim|legacy|compat|deprecated)" src/

# Permission/route keys used as strings (D6)
rg -n "requiredPage=['\"]|hasPermission\(['\"]" src/

# Form field names that diverge from column names (D3)
rg -n "name: ['\"][a-z_]+['\"]" src/**/*Form*.tsx

# Denormalised reads (D1)
rg -n "\.(office_name|agent_name|owner_name)\b" src/

# Direct PostgREST writes that bypass an EF (D5)
rg -n "\.from\(['\"][a-z_]+['\"]\)\.(insert|update|upsert|delete)\(" src/
```

Every match worth mentioning goes into the findings table with
`file:line` and a one-line classification.

### 4. UI + i18n cross-check

- List every i18n key referenced in UI under the audited page.
- For each key, assert the underlying schema field exists and the FK
  target exists.
- Screenshot (or DOM snapshot via the `cursor-ide-browser` MCP) the
  list view + form view of the same entity side-by-side; any label
  that differs is a D3 finding.

> **Harness-engineering link**: this protocol is the
> ["record evidence" loop][harness] — repro → evidence → fix → second
> evidence. Every finding has a receipt.

---

## Deliverable 1 — Findings table

The agent produces a single Markdown table. Each row is one concrete,
verifiable drift instance with a receipt.

| # | Dim. | Drift instance | Evidence (file:line / query) | Severity |
|---|------|----------------|------------------------------|----------|
| 1 | D4 | `public.mls_listings.office_id` has no FK | `pg_constraint` query row 14 | High |
| 2 | D3 | Form writes `list_price`, detail page reads `ListPrice` | `src/pages/Listing.tsx:112` vs `src/forms/ListingForm.tsx:48` | Med |
| 3 | D6 | `requiredPage="hrms-vacations"` vs `"hrms_vacations"` elsewhere | `rg` hits in `src/App.tsx`, `sso_role_configurations.page_keys` | Med |

Severity rubric:
- **High** — silent data loss, wrong values shown to users, security impact,
  or blocks a planned rename/migration.
- **Medium** — user-visible inconsistency, duplicated work, or technical
  debt that compounds.
- **Low** — cosmetic or localised cleanup.

---

## Deliverable 2 — Staged remediation plan

Produce `N` stages in execution order. Each stage is a *shippable unit*.

### Stage template

```markdown
### Stage <n>: <short imperative title>

**Invariant established** (what cannot regress after this ships)
: <e.g. "Every row in mls_listings has a referenceable mls_offices.id">

**Dimension(s)**: D1 / D4 / ...

**Files touched** / **added** / **deleted**
: src/…, supabase/migrations/<ts>_<slug>.sql, …

**Migration** (if any, must be re-runnable)
: `IF EXISTS` / `IF NOT EXISTS` / idempotent data-copy guards

**Verification step** (how we know it worked)
: - SQL query that must return 0 rows
  - `supabase gen types` produces no diff
  - UI screenshot matches /docs/ reference
  - `npm run typecheck` passes
  - A new lint or CI check that now fails on the old pattern

**Rollback note** (what to do if reverted)
: - `DROP CONSTRAINT IF EXISTS …`
  - Re-add the mirror column with a backfill query
  - Flip the feature flag off

**Mechanical enforcement added** (so drift cannot return)
: - New row in `GOLDEN_PRINCIPLES.md`
  - New custom ESLint rule / Supabase migration trigger / CI check
  - New entry in the typed registry (+ `as const`)

**Domain justification** (when user-visible)
: - "RESO DD 2.0 §X.Y requires ListingStatus transitions …"
  - "ITIL Incident lifecycle mandates …"
  - "Dash form field X is the canonical name on Anywhere.com"
```

### Stage ordering (risk-adjusted)

| Order | Risk | Typical contents |
|-------|------|------------------|
| 1 | Additive / safe | New FKs (no cascade yet), new typed registries, new Zod parsers at the boundary, new generated types committed |
| 2 | High-UX impact | Consolidating sources of truth (pick the authoritative column, switch all readers to it); wiring computed values through views or triggers |
| 3 | Deletions | Dropping legacy columns, shim exports, old EFs — only after step 2 has cut over all readers |
| 4 | Renames | Column / EF / permission-key renames, with a temporary view or alias + follow-up drop |

This ordering is deliberate: additive-first means every stage is
independently revertible.

---

## Deliverable 3 — Recommendation

A two-sentence recommendation naming the **1–2 stages to ship first**
and the **expected unlock** (what becomes easier once they land). Pick
stages where cost ≪ benefit *and* the invariant is small enough to
defend with a single lint or migration trigger.

---

## Constraints — what the audit never does

- Do **not** refactor authentication / authorization unless explicitly in scope.
  (SSO and CDL RLS are governed by [GOLDEN_PRINCIPLES.md §T, §S, §P8](../GOLDEN_PRINCIPLES.md).)
- Do **not** change security posture (RLS policies, CORS origins, auth
  policies, service-role distribution) without flagging it as a *separate*
  ADR-worthy decision.
- Do **not** split large tables by sub-type unless explicitly in scope —
  it is rarely a local fix.
- Do **not** invent new ingestion EFs; new tenants/sources register in
  `public.mls_settings` and field mappings in `public.field_mappings`
  on the CDL project, then run via `mls-sync` / `mls-sync-orchestrator`
  (CDL invariant P9).
- Every migration must be re-runnable (`IF EXISTS` / `IF NOT EXISTS` /
  guarded data-copy / idempotent upserts).
- Findings and plans are checked into the repo under
  `docs/exec-plans/active/<date>-alignment-audit-<app>.md` — not in chat.
- If the audit uncovers work that is out of scope, record it in
  [`docs/exec-plans/tech-debt-tracker.md`](../exec-plans/tech-debt-tracker.md)
  with a severity and owner.

---

## Post-merge hygiene (the "garbage collection" loop)

After each merged stage:

1. **Update [`GOLDEN_PRINCIPLES.md`](../GOLDEN_PRINCIPLES.md)** with the
   new invariant in the `Rule / Why it fails / Enforcement` format.
2. **Install the enforcement** that makes regression mechanically
   detectable (custom lint, migration trigger, CI query, schema-diff
   check). Custom lint error messages should *inject remediation
   instructions* so the next agent knows how to fix the violation —
   per harness-engineering practice.
3. **Update [`QUALITY_SCORE.md`](../QUALITY_SCORE.md)** for the affected
   domain (A–D grade).
4. **Update or create the app's entry** in
   [`docs/exec-plans/tech-debt-tracker.md`](../exec-plans/tech-debt-tracker.md)
   — resolved items are struck through, residual items get a date.
5. **Move the exec plan** from `docs/exec-plans/active/` to
   `docs/exec-plans/completed/` when all stages have shipped.
6. **Regenerate types** (`supabase gen types`) and commit the diff —
   a clean diff is the signal that the audit landed cleanly.

---

## Output contract (what the agent must do, in order)

When this playbook is invoked, the agent:

1. **Reads** this file, [`GOLDEN_PRINCIPLES.md`](../GOLDEN_PRINCIPLES.md),
   the relevant app's entry in
   [`app-catalog.md`](app-catalog.md), and any ADRs linked from there.
2. **Gathers evidence** per the protocol above and pastes receipts.
3. **Produces the three deliverables**: findings table, staged plan,
   recommendation — as a single Markdown document saved to
   `docs/exec-plans/active/<YYYY-MM-DD>-alignment-audit-<app>.md`.
4. **Stops and waits** for explicit human approval before writing any
   code, migration, or EF change.
5. Once approved, executes **one stage at a time**, runs the stage's
   verification step, and pauses before the next stage so a reviewer
   (human or agent) can sign off. This is the
   [Ralph Wiggum loop][wiggum] applied to cleanup: review → fix → review
   → merge, with agent-to-agent review preferred where safe.
6. After the final stage, performs the **post-merge hygiene** checklist.

[wiggum]: https://ghuntley.com/loop/

---

## Ready-to-use agent prompt

Copy this into a new agent session when you want to run an audit on a
specific app. Replace `<APP>` and `<DOMAIN>` before sending.

````markdown
You are a senior staff engineer running the **Codebase & Data-Model
Alignment Audit** on the `<APP>` application (domain: `<DOMAIN>`).

Read the playbook at
`/home/bitnami/matrix-platform-kb/docs/platform/alignment-audit-playbook.md`
and follow it verbatim.

Your job in this turn:
1. Gather evidence per the playbook's *Evidence-collection protocol*
   (DB introspection, generated-type diff, code search, UI/i18n
   cross-check). Paste the raw outputs.
2. Produce the three deliverables (**findings table**, **staged plan**,
   **recommendation**) as a single Markdown file at
   `/home/bitnami/matrix-platform-kb/docs/exec-plans/active/<YYYY-MM-DD>-alignment-audit-<APP>.md`.
3. **Stop and wait** for explicit approval. Do not write application
   code, migrations, or Edge Function changes in this turn.

Hard constraints:
- Do not touch auth / RLS / CORS / service-role paths (out of scope).
- Do not invent new ingestion EFs (violates CDL invariant P9).
- Every proposed migration must be re-runnable
  (`IF EXISTS` / `IF NOT EXISTS` / idempotent).
- Findings must cite `file:line` or a pasted query result — no prose
  speculation.
- Order stages by risk-adjusted impact: additive → consolidation →
  deletion → rename.
- For every user-visible change, cite the domain convention
  (RESO DD, ITIL, Dash form field, etc.) that justifies it.

When I approve, execute stages one at a time, run the stage's
verification step, and stop before the next stage. After the last
stage, perform the playbook's *Post-merge hygiene* checklist.
````

---

## Cross-reference

| For | See |
|-----|-----|
| Engineering invariants this audit defends | [GOLDEN_PRINCIPLES.md](../GOLDEN_PRINCIPLES.md) |
| Quality grades by domain (before / after) | [QUALITY_SCORE.md](../QUALITY_SCORE.md) |
| Execution-plan format | [exec-plans/index.md](../exec-plans/index.md) |
| Known debt tracker | [exec-plans/tech-debt-tracker.md](../exec-plans/tech-debt-tracker.md) |
| App inventory + ownership | [app-catalog.md](app-catalog.md) |
| Testing strategy (what verification looks like) | [testing-strategy.md](testing-strategy.md) |
| KB doc-gardening methodology | [kb-methodology.md](kb-methodology.md) |
| Source inspiration | [OpenAI — *Harness engineering*][harness] · [Logic.inc — *AI is forcing us to write good code*](https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code) · [matklad — *ARCHITECTURE.md*](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html) · [parse-don't-validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) |
