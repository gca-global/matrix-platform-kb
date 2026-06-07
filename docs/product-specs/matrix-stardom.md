# Matrix Stardom — Shared Prompt Workspace

> **Matrix Stardom** is a Lovable-managed Matrix app (`sharpsir-group/matrix-stardom`) that serves as the team's shared **HumaticAI workspace**: a place to ask the AI, share the conversations behind the answers, and curate the best prompts as a team. This spec documents the prompt-workspace capability set (prompt library, curation, scheduled automations, engagement-driven ranking) built on top of the app shell.
>
> Deploy / hosting / OAuth details live in [`../platform/app-catalog.md`](../platform/app-catalog.md) (entry 18a). This doc covers the data model and behavior.

## 1. Architecture

- **Dual-Supabase** per the platform template: SSO instance (`xgubaguglsnokjyudgvc`) for auth/permissions; **app DB `wjsafhylqujwbpqgjjlj`** for all business data below.
- Auth is Microsoft SSO via the Matrix OAuth flow; AD profile (display name, avatar, job title) is denormalized onto authored rows for cheap display (no SQL joins to `sso_users`).
- Tenant-scoped: every table carries `tenant_id` and is filtered client-side via `useAuth().tenantId`; realtime subscriptions invalidate React Query caches.
- Data access is through dedicated React Query hooks (`usePrompts`, `usePromptEndorsements`, `usePromptSchedules`, `usePromptRuns`) — never raw fetch.

## 2. Data model (app DB `wjsafhylqujwbpqgjjlj`)

| Table | Purpose | Key columns |
|---|---|---|
| `prompts` | The shared prompt library | `title`, `body`, `description`, `audience` (`executive`/`manager`/`agent`/`discover`/`general`), `topics[]`, `language`, `status` (`proposed`/`approved`/`archived`), `source_conversation_id`, `created_by_*`, `approved_by_*`, `run_count`, `fork_count` |
| `prompt_endorsements` | Per-user "thumbs up" on a prompt | `prompt_id`, `user_id` (one endorsement per user/prompt) |
| `prompt_schedules` | Recurring automated runs of a prompt | `prompt_id`, `cadence` (`weekly_sun_evening`/`monthly_end`/`quarter_end`), `enabled`, `timezone`, `next_run_at`, `last_run_at` |
| `prompt_runs` | Execution log for scheduled/manual runs | `prompt_id`, `schedule_id`, `conversation_id`, `status` (`queued`/`running`/`success`/`error`), `triggered_by` (`schedule`/`manual`), `started_at`, `completed_at`, `output_md`, `error` |
| `shared_conversations` / `shared_messages` | The conversation threads prompts open into | (pre-existing) |
| `conversation_reactions` | Emoji reactions on conversations / messages | (pre-existing) |

RLS is permissive + tenant-scoped; all four prompt tables are in the realtime publication.

### Engagement counters

`prompts.run_count` and `prompts.fork_count` are integer counters incremented via **atomic `SECURITY DEFINER` RPCs** (`increment_prompt_run_count(uuid)`, `increment_prompt_fork_count(uuid)`, granted to `anon, authenticated`). They are called best-effort from the client (failures never surface). Critically, the RPCs do **not** touch `updated_at`, so the "Latest" ordering is unaffected.

## 3. Prompt lifecycle & curation

```
propose ──► proposed ──(admin approve)──► approved ──(admin archive)──► archived
   ▲            │                              │
   │            └── endorse (any user, toggle) ┘
   └── "Promote to prompt" from any conversation (sets source_conversation_id)
   └── fork (any user → a new proposed prompt; bumps original's fork_count)
```

- **Anyone** can propose a prompt, endorse, fork, or promote a conversation into the library.
- **Admins** (`useActiveRole().isGlobal`) can approve (→ board-approved) and archive.
- **Promote to prompt** lives in the conversation thread header `…` menu and prefills the propose dialog from the conversation's first user message + title.

## 4. Scheduled automations (the engine)

Selected prompts can run on a cadence to produce periodic AI output (e.g. weekly exec summaries, quarter-end stats).

- **`humaticai-chat` EF** exposes a non-streaming `action: 'run'` that consumes the HumaticAI SSE stream server-side and returns `{ content, thread_id }`.
- **`prompt-scheduler` EF** (`verify_jwt = false`) processes due `prompt_schedules`: backfills `next_run_at` for new schedules, creates a `shared_conversation` + user/assistant `shared_messages`, calls `humaticai-chat` in run mode, logs a `prompt_runs` row, and advances `next_run_at` via a tz-aware `computeNextRun` helper. Returns `{ processed, succeeded, failed }`.
- **Trigger:** `pg_cron` (+`pg_net`) job `prompt-scheduler-hourly` (`0 * * * *`) POSTs to the EF. **Auth uses the public `anon` key, NOT `service_role`** — the EF runs `verify_jwt = false` and uses its own injected `SUPABASE_SERVICE_ROLE_KEY` for DB writes, so the cron only needs to satisfy the API gateway. This keeps the secret out of the committed migration. (See `~/.cursorrules` → verify_jwt guidance.)

The **Automations** tab in the AI Lab manages schedules (cadence, enable/disable, delete); the **Stats** tab shows run history, success rate, and a most-endorsed leaderboard from `prompt_runs` + `prompts`.

## 5. "Most popular" ranking

`usePrompts({ order: 'popular' })` aggregates endorsement counts and sorts by a composite score:

```
score = endorsement_count*3 + run_count*2 + fork_count*2   (tiebreak: updated_at desc)
```

This feeds the Home "Board-approved · Best prompts" section, the dashboard prompt starters, and the AI Lab "Most popular" tab. The Home sidebar **conversation** "Most popular" card is separate and ranks `shared_conversations` by `reaction_count`.

## 6. UI surfaces

| Surface | What it shows |
|---|---|
| **Home** (`Index.tsx`) | Ask composer + "Board-approved · Best prompts" (popular approved prompts, main column); sidebar "Most popular" (conversations by reactions), "Latest", "Active in your workspace" |
| **Dashboards** (Executive / My Team / My Performance) | `DiscussedByTeam` strip kept; `DashboardPromptStarters` renders audience-aware "Most popular" + "Latest" approved prompts that open a new shared conversation (`?ask=…`) |
| **AI Lab** (`DesignShowcase.tsx`) | Tabs: Board-approved · Most popular · Latest · Mine · **Automations** · **Stats**; per-card run / endorse / fork / admin approve-archive / admin **Schedule** |
| **Conversation thread** | "Promote to prompt", "Duplicate" (clone thread + messages into a new conversation), owner-only "Delete"; message-level 👍/👎 lives only in `ResponseFeedback` (the message `ReactionBar` excludes `like`) |

## 7. Delivery / deploy pattern

Stardom is **Lovable-authored**: Lovable commits UI + `supabase/migrations/` + `supabase/functions/` to GitHub `main` and applies migrations / deploys EFs to the app DB. The `github-watcher` deploys `main` to Apache `/stardom/` on push. The local checkout at `/home/bitnami/matrix-stardom` tracks the same remote. Cursor changes (if any) must be delivered as committed migrations / EF source in the repo — never applied out-of-band.

---

### KB sources consulted

- `docs/platform/app-catalog.md` (entry 18a — Stardom hosting / deploy / OAuth)
- `docs/platform/app-template.md` (dual-Supabase, SSO auth, RLS, hooks conventions)
- `~/.cursorrules` (verify_jwt = false for SSO-compatible EFs; anon-key cron auth)

### KB divergence

None. This is a new app product-spec; no existing KB doc is contradicted.
