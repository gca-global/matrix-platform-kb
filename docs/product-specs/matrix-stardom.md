# Matrix Stardom — Shared Prompt Workspace

> **Matrix Stardom** is a Lovable-managed Matrix app (`sharpsir-group/matrix-stardom`) that serves as the team's shared **AI prompt workspace**: a place to ask the AI, share the conversations behind the answers, and curate the best prompts as a team. This spec documents the prompt-workspace capability set (prompt library, curation, scheduled automations, engagement-driven ranking) built on top of the app shell.
>
> Deploy / hosting / OAuth details live in [`../platform/app-catalog.md`](../platform/app-catalog.md) (entry 18a). This doc covers the data model and behavior.

## 1. Architecture

- **Dual-Supabase** per the platform template: SSO instance (`xgubaguglsnokjyudgvc`) for auth/permissions; **app DB `wjsafhylqujwbpqgjjlj`** for all business data below.
- Auth is Microsoft SSO via the Matrix OAuth flow; AD profile (display name, avatar, job title) is denormalized onto authored rows for cheap display (no SQL joins to `sso_users`).
- Tenant-scoped: every table carries `tenant_id` and is filtered client-side via `useAuth().tenantId`; realtime subscriptions invalidate React Query caches.
- Data access is through dedicated React Query hooks (`usePrompts`, `usePromptEndorsements`, `usePromptSchedules`, `usePromptRuns`) — never raw fetch.
- **User identity for writes:** all user-attributed values (`*_user_id`, `conversation_reactions.user_id`, `prompt_endorsements.user_id`, `ai_response_feedback.user_id`) resolve the SSO subject via `useAuth().userId` = `user.sub ?? user.supabase_user_id` — **never `user.id`** (the SSO user object has no `id` field; `decodeUserFromToken` sets `sub`/`supabase_user_id` only). Reading the nonexistent `user.id` yields `null`, which silently drops the write (e.g. `useReactions.toggle` early-returns on `!userId`). This was the root cause of reactions/endorsements/feedback/notifications not persisting and of `created_by_user_id` landing `null` (hence the name-matching ownership fallback in `ConversationCard`); fixed Jun 2026 by exposing `userId` from `AuthContext`.

## 2. Data model (app DB `wjsafhylqujwbpqgjjlj`)

| Table | Purpose | Key columns |
|---|---|---|
| `prompts` | The shared prompt library | `title`, `body`, `description`, `audience` (`executive`/`manager`/`agent`/`discover`/`general`), `topics[]`, `language`, `status` (`proposed`/`approved`/`archived`), `source_conversation_id`, `created_by_*`, `approved_by_*`, `run_count`, `fork_count` |
| `prompt_endorsements` | Per-user "thumbs up" on a prompt | `prompt_id`, `user_id` (one endorsement per user/prompt) |
| `prompt_schedules` | Recurring automated runs of a prompt | `prompt_id`, `cadence` (`weekly_mon_morning`/`monthly_after_end`/`quarter_after_end`), `enabled`, `timezone`, `next_run_at`, `last_run_at` |
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
   └── "Promote" from any conversation (sets source_conversation_id)
   └── fork (any user → a new proposed prompt; bumps original's fork_count)
```

- **Anyone** can propose a prompt, endorse, fork, or promote a conversation into the library.
- **Admins** (`useActiveRole().isGlobal`) can approve (→ board-approved) and archive.
- **Promote** lives in the conversation thread header `…` menu (and the `ConversationCard` `…` menu) and prefills the propose dialog from the conversation's first user message + title. (Renamed from "Promote to prompt" for concision.)

## 4. Scheduled automations (the engine)

Selected prompts can run on a cadence to produce periodic AI output (e.g. weekly exec summaries, quarter-end stats).

- **Chat EF** exposes a non-streaming `action: 'run'` that consumes the RagChat SSE stream server-side and returns `{ content, thread_id }`.
- **`prompt-scheduler` EF** (`verify_jwt = false`) processes due `prompt_schedules`: backfills `next_run_at` for new schedules, creates a `shared_conversation` + user/assistant `shared_messages`, calls the chat EF in run mode, logs a `prompt_runs` row, and advances `next_run_at` via a tz-aware `computeNextRun` helper. Returns `{ processed, succeeded, failed }`.
- **Cadence timing (all at 07:00 local, DST-safe):** `weekly_mon_morning` fires every **Monday 07:00** (reports the just-closed week); `monthly_after_end` fires on the **1st of the month 07:00** (day after month-end, reports last month); `quarter_after_end` fires on the **1st of the quarter** — Jan/Apr/Jul/Oct **07:00** (day after quarter-end, reports last quarter).
- **Period context:** before each run the scheduler prepends a `periodPreamble(cadence, now, tz)` line (e.g. `Reporting period: last week, 1 Jun 2026 to 7 Jun 2026.`) to **both** the stored user message and the chat EF `message`, so the model anchors on the closed window rather than "today".
- **Trigger:** `pg_cron` (+`pg_net`) job `prompt-scheduler-hourly` (`0 * * * *`) POSTs to the EF. **Auth uses the public `anon` key, NOT `service_role`** — the EF runs `verify_jwt = false` and uses its own injected `SUPABASE_SERVICE_ROLE_KEY` for DB writes, so the cron only needs to satisfy the API gateway. This keeps the secret out of the committed migration. (See `~/.cursorrules` → verify_jwt guidance.)

The **Automations** tab in the AI Lab manages schedules (cadence, enable/disable, delete) and has a **"New automation"** button (admin) that opens `ScheduleDialog` in **picker mode**: when no `promptId` is passed the dialog renders a searchable prompt picker sourcing **approved/board prompts plus the user's own non-archived prompts** (so a schedule can be created in-panel, not only from a prompt card). The **Stats** tab shows run history, success rate, and a most-endorsed leaderboard from `prompt_runs` + `prompts`.

### Streaming: sub-turn separation

RagChat emits `message_complete` then `new_message` SSE events between content phases when it runs tools. Both SSE parsers — the client `consumeSse`/`handleSseEvent` and the server-side `consumeSseToText`/`handleSseEvent` in the chat EF — treat those signals as a **sub-turn boundary** via a shared `handleSubTurnBoundary` helper:

- **Plain-text buffers** get a blank line (`\n\n`) appended at the boundary (the client also emits `onDelta('\n\n')` so the live bubble shows the gap immediately), so consecutive sub-turns no longer run together (`"…in parallel."` + `"A key finding…"`).
- **JSON buffers** keep the existing behavior: they only split into a segment-separator-joined segment once structurally complete, preserving `json_only` dashboard parsing (the JSON parser hook splits on that marker).
- Repeated boundary signals are **de-duped** (no-op on an empty / already-`\n\n`-terminated buffer).

## 5. "Most popular" ranking

`usePrompts({ order: 'popular' })` aggregates endorsement counts and sorts by a composite score:

```
score = endorsement_count*3 + run_count*2 + fork_count*2   (tiebreak: updated_at desc)
```

This feeds the Home "Board-approved · Best prompts" section, the dashboard prompt starters, and the AI Lab "Most popular" tab. The Home sidebar **conversation** "Most popular" card is separate and ranks `shared_conversations` by `reaction_count`.

The Home **"Board-approved · Best prompts"** cards mirror the `ConversationCard` shell (horizontal `flex gap-3`, `h-9 w-9` avatar left, title row with an endorsement badge — ThumbsUp + count — in place of message/view badges, author row, and the description as a `line-clamp-2` preview) while preserving run-on-click (`askNow(p.body)` + best-effort `increment_prompt_run_count`).

## 6. UI surfaces

| Surface | What it shows |
|---|---|
| **Home** (`Index.tsx`) | Ask composer + "Board-approved · Best prompts" rendered as **compact starter-style chips** (pill buttons, `BadgeCheck` + title, run-on-click via `askNow` + `increment_prompt_run_count`); sidebar "Most popular" (conversations by reactions), "Latest", "Active in your workspace" |
| **Dashboards** (Executive / My Team / My Performance) | `DiscussedByTeam` rendered as a **recsys block** that is a **swipeable carousel with bullet/dot pagination** (embla `Carousel`) instead of a raw horizontal-scroll strip; each card shows the peer avatar, title, asker + role, recency; `DashboardPromptStarters` renders audience-aware "Most popular" + "Latest" approved prompts that open a new shared conversation (`?ask=…`) |
| **AI Lab** (`DesignShowcase.tsx`) | Tabs: Board-approved · Most popular · Latest · Mine · **Automations** · **Stats**; per-card run / endorse / fork / admin approve-archive / admin **Schedule** |
| **Conversation thread** | "Promote", "Duplicate" (clone thread + messages into a new conversation), owner-only "Delete"; the message-level `ReactionBar` is **identical** to the conversation-card bar (full palette incl. Like/Dislike — `excludeKeys`/`compact` dropped) and `ResponseFeedback`'s separate 👍/👎 + memo is **kept** alongside it (so Like/Dislike may appear twice on AI messages, by request) |

### Digital-peer attribution (Humans x Digital Peers)

Conversation cards, dashboard banners, and the conversation thread use **peer-primary attribution**: the **digital peer that actually responds is the lead avatar** (responder), and the human who started the thread is demoted to an "Asked by [name · job title]" sub-line. This frames Stardom as a *human + digital-peer* collaboration workspace rather than a plain AI chat.

- The sole digital peer today is **Alex · CRM Analyst · Digital Peer** (the RagChat persona behind `alexPromptLibrary.ts`). Identity lives in a single shared constant `src/lib/digitalPeer.ts` (`{ name, role, kind, avatar }`); the avatar is vendored at `public/peers/alex.png`, with the legacy `Sparkles` + `bg-accent` `AvatarFallback` as the graceful fallback.
- Applied in `ConversationCard.tsx`, `dashboards/DiscussedByTeam.tsx`, and the assistant bubble in `SharedConversationThread.tsx`.
- This is intentionally a **single constant, not a registry** — the registry lands with the planned multi-digital-peer workspace (CRM / HR / IT / SDR / SEO / SMM peers).

## 7. Delivery / deploy pattern

Stardom is **Lovable-authored**: Lovable commits UI + `supabase/migrations/` + `supabase/functions/` to GitHub `main` and applies migrations / deploys EFs to the app DB. The `github-watcher` deploys `main` to Apache `/stardom/` on push. The local checkout at `/home/bitnami/matrix-stardom` tracks the same remote. Cursor changes (if any) must be delivered as committed migrations / EF source in the repo — never applied out-of-band.

---

### KB sources consulted

- `docs/platform/app-catalog.md` (entry 18a — Stardom hosting / deploy / OAuth)
- `docs/platform/app-template.md` (dual-Supabase, SSO auth, RLS, hooks conventions)
- `~/.cursorrules` (verify_jwt = false for SSO-compatible EFs; anon-key cron auth)

### KB divergence

None. This is a new app product-spec; no existing KB doc is contradicted.
