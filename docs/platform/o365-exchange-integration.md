# O365 Exchange Integration — Email & Calendar

> **Source:** SM Pipeline (`matrix-pipeline`), Edge Function `ms-graph-proxy`, Microsoft Graph API v1.0
>
> **Supabase instance:** `tiuansahlsgautkjsajk` (SM Pipeline)
>
> This document describes the **implemented** O365 integration in SM Pipeline. All features below are live and working.

## Overview

SM Pipeline integrates with Microsoft 365 Exchange Online via a single `ms-graph-proxy` Edge Function that proxies all Graph API calls. Brokers connect their Microsoft account once (via OAuth) and then use email and calendar features directly inside the pipeline app.

| Capability | Status | Graph API Scope |
|-----------|--------|-----------------|
| **Email inbox browsing** | Implemented | `Mail.Read` |
| **Email folder browsing** | Implemented | `Mail.Read` |
| **Email send** | Implemented | `Mail.Send` |
| **Email reply / reply-all** | Implemented | `Mail.Send` |
| **Email delete (move to trash)** | Implemented | `Mail.Read` (uses `/move`) |
| **Email move to folder** | Implemented | `Mail.Read` |
| **Email mark read/unread** | Implemented | `Mail.Read` |
| **Email attach to deal** | Implemented | `Mail.Read` |
| **Email link to deal/contact** | Implemented | `Mail.Read` |
| **Calendar read (Outlook → app)** | Implemented | `Calendars.ReadWrite` |
| **Calendar create (app → Outlook)** | Implemented | `Calendars.ReadWrite` |
| **Free/busy check** | Implemented | `Calendars.ReadWrite` |
| **Verification reply scan** | Implemented | `Mail.Read` |

All operations use **delegated permissions** — each broker accesses only their own mailbox and calendar.

---

## OAuth Flow

SM Pipeline uses its **own OAuth flow**, separate from the SSO authentication. The broker connects their Microsoft account from the Settings page.

### Azure AD App Registration

| Parameter | Value |
|-----------|-------|
| Client ID | `d7e5b1da-121b-43be-ba40-8307be55934c` |
| Tenant ID | `2ae67cc3-38e7-4c03-95af-c271b0fbf917` |
| Scopes | `openid Mail.Read Mail.Send Calendars.ReadWrite offline_access` |
| Redirect URI | `{app_origin}/auth/ms-callback` |
| Token endpoint | `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token` |

### Flow

```
1. User clicks "Connect Microsoft 365" in Settings
2. App generates a state nonce, stores user_id in sessionStorage
3. Redirect → Azure AD authorize endpoint (with PKCE-like state)
4. User authenticates and consents
5. Azure AD redirects back to /auth/ms-callback with auth code
6. MsCallback page sends code to ms-graph-proxy (action: "callback")
7. Edge Function exchanges code for tokens via token endpoint
8. Tokens stored in ms_graph_tokens table (per-user, with refresh token)
9. User is connected — all subsequent Graph calls use stored tokens
```

### Token Refresh

- Access tokens expire after ~60-90 minutes
- Before every Graph API call, `getGraphToken()` checks if the token is within 2 minutes of expiry
- If expired: refreshes via `grant_type=refresh_token` to the Azure AD token endpoint
- If refresh fails (token revoked, password changed): tokens are deleted, user must reconnect
- New tokens are stored back in `ms_graph_tokens`

---

## Edge Function: `ms-graph-proxy`

**Single Edge Function** handling all O365 operations via action-based routing.

| Aspect | Detail |
|--------|--------|
| Path | `supabase/functions/ms-graph-proxy/index.ts` |
| Method | POST (all actions) |
| Auth | Bearer (Matrix SSO JWT) — `verify_jwt: false` |
| Config | `MS_GRAPH_CLIENT_ID`, `MS_GRAPH_CLIENT_SECRET` in env |

### Authentication

The function resolves the user through a 3-tier fallback:

1. **Project Supabase** — `getUser()` with the project's anon key
2. **SSO Supabase** — `getUser()` against `xgubaguglsnokjyudgvc` (Matrix SSO)
3. **Manual JWT decode** — extract `sub` claim from an SSO JWT that Supabase can't parse (due to non-standard `scope` object)

### Actions

| Action | Purpose | Auth Required |
|--------|---------|---------------|
| `callback` | Exchange OAuth code for tokens, store in DB | No (code is single-use) |
| `status` | Check if user has a valid Microsoft connection | Graceful (returns `{connected: false}` if unauthed) |
| `disconnect` | Delete stored tokens and synced_emails cache | Yes |
| `list-emails` | List emails filtered by contact emails and/or deal subject tag | Yes |
| `list-folders` | List mail folders with unread counts | Yes |
| `list-folder-emails` | List emails in a specific folder (paginated, searchable) | Yes |
| `get-email` | Get single email with full body, attachments, and deal links | Yes |
| `send-email` | Send email via Graph (optionally tagged with `[DEAL-{id}]`) | Yes |
| `reply-email` | Reply or Reply All to an email | Yes |
| `delete-email` | Move email to Deleted Items | Yes |
| `move-email` | Move email to a folder | Yes |
| `toggle-read` | Mark email as read or unread | Yes |
| `attach-email` | Attach email snapshot to a deal → `opportunity_emails` | Yes |
| `detach-email` | Remove attached email from a deal | Yes |
| `list-attached-emails` | List emails attached to a deal | Yes |
| `link-email` | Link email to a deal/contact (metadata only) → `email_links` | Yes |
| `unlink-email` | Remove email link | Yes |
| `list-calendar` | List Outlook events for a date range | Yes |
| `create-event` | Create Outlook event + local `calendar_events` + `broker_meetings` | Yes |
| `get-schedule` | Check free/busy availability | Yes |
| `check-verification-replies` | Scan for broker replies to "Additional information needed" emails | Yes |

---

## Client-Side Invocation

All Graph calls go through a shared helper that attaches Matrix SSO tokens:

```typescript
// src/lib/msGraphInvoke.ts
export async function invokeGraphProxy(body: Record<string, unknown>) {
  await ensureFreshAuth();
  const token = localStorage.getItem('matrix_supabase_access_token')
    || localStorage.getItem('matrix_sso_access_token');
  const resp = await fetch(`${SUPABASE_URL}/functions/v1/ms-graph-proxy`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'apikey': SUPABASE_ANON_KEY, 'Authorization': `Bearer ${token}` },
    body: JSON.stringify(body),
  });
  return await resp.json();
}
```

### Key Hooks

| Hook | File | Purpose |
|------|------|---------|
| `useMicrosoftGraph` | `src/hooks/useMicrosoftGraph.ts` | Connect/disconnect, status check, OAuth code exchange |
| `useEmailClient` | `src/hooks/useEmailClient.ts` | Folder/email browsing, send, reply, delete, move, read toggle |
| `useDealEmails` | `src/hooks/useDealEmails.ts` | List emails related to a deal (by contact + subject tag) |
| `useOpportunityEmails` | `src/hooks/useOpportunityEmails.ts` | Attach/detach/list emails on a deal |
| `useDealCalendarSync` | `src/hooks/useDealCalendarSync.ts` | List Outlook calendar events |
| `useBrokerMeetings` | `src/hooks/useBrokerMeetings.ts` | CRUD for broker_meetings table |

---

## Email Integration

### Features

| Feature | How It Works |
|---------|-------------|
| **Inbox browsing** | `list-folders` → `list-folder-emails` — full Outlook folder tree with message list, search, pagination |
| **Deal-scoped emails** | `list-emails` with `contact_emails` + `deal_id` — finds emails by participant match or `[DEAL-{short_id}]` subject tag |
| **Full email view** | `get-email` — returns HTML body, attachment metadata, read status, deal/contact links |
| **Send** | `send-email` — sends via Graph; auto-tags subject with `[DEAL-{short_id}]` if deal context |
| **Reply** | `reply-email` — reply or reply-all via Graph |
| **Attach to deal** | `attach-email` — fetches full email from Graph, creates immutable snapshot in `opportunity_emails` |
| **Link to deal/contact** | `link-email` — lightweight metadata-only link in `email_links` (no snapshot) |

### Email Caching

When listing deal-scoped emails, results are cached in `synced_emails` for offline/fast access. The cache stores metadata (subject, sender, snippet) keyed by `(user_id, graph_message_id)`.

### Verification Reply Scanning

The `check-verification-replies` action scans for unread emails matching "Additional information needed: {contactName}" in the subject. When found, it:

1. Matches the sender email to a broker profile
2. Matches the contact name to a `crm_contacts` record
3. Creates an `internal_messages` entry (threaded by contact)
4. Logs an `activity_log` entry on the contact and linked deals

### Microsoft Graph Mail Endpoints Used

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/me/messages` | GET | List/search emails |
| `/me/messages/{id}` | GET | Get full email |
| `/me/messages/{id}` | PATCH | Mark read/unread |
| `/me/messages/{id}/attachments` | GET | List attachment metadata |
| `/me/messages/{id}/reply` | POST | Reply |
| `/me/messages/{id}/replyAll` | POST | Reply All |
| `/me/messages/{id}/move` | POST | Move to folder / delete (move to Deleted Items) |
| `/me/mailFolders` | GET | List folders with counts |
| `/me/mailFolders/{id}/messages` | GET | List emails in folder |
| `/me/sendMail` | POST | Send new email |

---

## Calendar Integration

### Features

| Feature | How It Works |
|---------|-------------|
| **View Outlook events** | `list-calendar` → Graph `calendarView` for a date range (default: -30 to +90 days) |
| **Create event** | `create-event` → creates in Outlook + inserts in `calendar_events` and `broker_meetings` |
| **Free/busy check** | `get-schedule` → Graph `getSchedule` for one or more users |

### Sync Direction

- **Outlook → App:** Read-only. Outlook events are displayed in the CRM calendar but not stored permanently unless created from within the app.
- **App → Outlook:** When a user creates an event in the app, it is pushed to Outlook and stored locally with the Outlook event ID.
- Events created directly in Outlook are visible in the CRM calendar view but are **not** linked to CRM records unless manually linked.

### Meeting Types

Events created from the app are categorized by `meeting_type` in `broker_meetings`:

| Type | Use Case |
|------|----------|
| `viewing` | Property showings (maps to "showing_appointment" in the UI) |
| `follow_up_call` | Follow-up calls with clients |
| `seller_meeting` | Meetings with property sellers/owners |
| `contract_signing` | Contract signing appointments |
| `other` | Any other meeting type |

### Calendar Event Creation Flow

1. User opens the calendar and clicks "Create Event"
2. Fills in: title, date/time, location, attendees, meeting type, linked deal/contact/property
3. On save, the Edge Function:
   - Creates the event in Outlook via `POST /me/events` (with Teams link if online)
   - Inserts into `calendar_events` with `external_id` = Outlook event ID, `external_source` = "microsoft"
   - If `meeting_type` is set: inserts into `broker_meetings` with `outlook_event_id`, `outlook_sync_status` = "synced"
4. Returns the Outlook web link and Teams meeting URL (if applicable)

### Microsoft Graph Calendar Endpoints Used

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/me/calendarView` | GET | List events in date range |
| `/me/events` | POST | Create event (with attendees, location, Teams) |
| `/me/calendar/getSchedule` | POST | Check free/busy |

---

## Data Model

### `ms_graph_tokens` — Per-user Microsoft OAuth tokens

```sql
CREATE TABLE ms_graph_tokens (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  access_token TEXT NOT NULL,
  refresh_token TEXT NOT NULL,
  token_expires_at TIMESTAMPTZ NOT NULL,
  scopes TEXT[] NOT NULL DEFAULT '{}',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(user_id)
);
```

RLS: users can only access their own tokens.

### `opportunity_emails` — Email snapshots attached to deals

```sql
CREATE TABLE opportunity_emails (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  opportunity_id UUID NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
  attached_by UUID NOT NULL,
  attached_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  exchange_message_id TEXT NOT NULL,
  internet_message_id TEXT,
  conversation_id TEXT,
  subject TEXT NOT NULL,
  from_name TEXT,
  from_email TEXT NOT NULL,
  to_recipients JSONB,              -- [{email, name}]
  cc_recipients JSONB,              -- [{email, name}]
  received_at TIMESTAMPTZ NOT NULL,
  body_preview TEXT,
  body_html TEXT,
  has_attachments BOOLEAN DEFAULT false,
  attachment_names TEXT[],
  importance TEXT DEFAULT 'normal',
  note TEXT,
  x_sm_tenant_id UUID,
  x_sm_created_by UUID,
  x_sm_modified_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(opportunity_id, exchange_message_id)
);
```

### `email_links` — Lightweight email-to-deal/contact links

```sql
CREATE TABLE email_links (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  graph_message_id TEXT NOT NULL,
  deal_id UUID,
  contact_id UUID,
  subject TEXT,
  from_address TEXT,
  received_at TIMESTAMPTZ,
  note TEXT
);
```

### `synced_emails` — Cached email metadata for deal context

```sql
CREATE TABLE synced_emails (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  graph_message_id TEXT NOT NULL,
  deal_id UUID REFERENCES deals(id) ON DELETE SET NULL,
  contact_id UUID REFERENCES crm_contacts(id) ON DELETE SET NULL,
  subject TEXT,
  from_address TEXT,
  from_name TEXT,
  to_addresses TEXT[] DEFAULT '{}',
  received_at TIMESTAMPTZ,
  snippet TEXT,
  is_read BOOLEAN DEFAULT false,
  has_attachments BOOLEAN DEFAULT false,
  web_link TEXT,
  match_type TEXT,                  -- 'contact' | 'subject_tag'
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(user_id, graph_message_id)
);
```

### `broker_meetings` — CRM meetings with Outlook sync

```sql
CREATE TABLE broker_meetings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  broker_id UUID NOT NULL,
  meeting_type TEXT NOT NULL,       -- 'viewing' | 'follow_up_call' | 'seller_meeting' | 'contract_signing' | 'other'
  opportunity_id UUID REFERENCES deals(id),
  contact_id UUID,
  property_id UUID,
  subject TEXT NOT NULL,
  description TEXT,
  start_time TIMESTAMPTZ NOT NULL,
  end_time TIMESTAMPTZ NOT NULL,
  time_zone TEXT DEFAULT 'Asia/Nicosia',
  location TEXT,
  is_online BOOLEAN DEFAULT false,
  online_meeting_url TEXT,
  attendees JSONB DEFAULT '[]',     -- [{email, name?}]
  outlook_event_id TEXT,
  outlook_ical_uid TEXT,
  outlook_sync_status TEXT DEFAULT 'not_linked',  -- 'synced' | 'not_linked'
  outlook_last_synced_at TIMESTAMPTZ,
  status TEXT DEFAULT 'scheduled',  -- 'scheduled' | 'completed' | 'cancelled' | 'no_show'
  outcome_notes TEXT,
  x_sm_tenant_id UUID,
  x_sm_created_by UUID,
  x_sm_created_at TIMESTAMPTZ DEFAULT now(),
  x_sm_modified_at TIMESTAMPTZ DEFAULT now()
);
```

### `calendar_events` — Local calendar events (with Outlook sync columns)

```sql
-- Existing table with added columns:
ALTER TABLE calendar_events
  ADD COLUMN external_id TEXT,          -- Outlook event ID
  ADD COLUMN external_source TEXT,      -- 'microsoft'
  ADD COLUMN sync_status TEXT;          -- 'synced' | null
```

---

## UI Components

| Component | Path | Purpose |
|-----------|------|---------|
| `MicrosoftSettings` | `src/components/settings/MicrosoftSettings.tsx` | Connect/disconnect Microsoft 365 account |
| `MsCallback` | `src/pages/MsCallback.tsx` | OAuth callback handler page |
| `EmailPage` | `src/pages/Email.tsx` | Full email client (folders, list, reading pane) |
| `EmailReadingPane` | `src/components/email/EmailReadingPane.tsx` | Read email, reply, delete, link to deal |
| `ComposeEmailDialog` | `src/components/email/ComposeEmailDialog.tsx` | Compose new email (from Email page) |
| `OpportunityEmailPanel` | `src/components/pipeline/OpportunityEmailPanel.tsx` | Attach/detach emails on a deal |
| `ComposeEmail` | `src/components/pipeline/ComposeEmail.tsx` | Compose email from deal context |
| `DealCommunicationPanel` | `src/components/pipeline/DealCommunicationPanel.tsx` | Tabbed panel: emails, messages, activity on a deal |
| `CRMCalendar` | `src/components/calendar/CRMCalendar.tsx` | Calendar view (merges Outlook + CRM events) |
| `CreateEventDialog` | `src/components/calendar/CreateEventDialog.tsx` | Create new calendar event |

---

## Security Considerations

| Principle | Implementation |
|-----------|---------------|
| **Delegated only** | Each broker accesses only their own mailbox and calendar |
| **Token isolation** | Microsoft tokens stored server-side in `ms_graph_tokens`; never sent to the client |
| **Auto-refresh** | Tokens refreshed transparently before expiry; deleted on refresh failure |
| **Separate OAuth** | Microsoft connection is independent from SSO login — can be connected/disconnected at will |
| **RLS** | `ms_graph_tokens` and `synced_emails` have RLS policies scoped to `auth.uid()` |
| **Snapshot immutability** | Once an email is attached to a deal, the snapshot is immutable (can only be detached) |
| **Soft delete** | Email "delete" moves to Deleted Items in Outlook (not hard delete) |

---

## Use Cases Mapped to Sales Pipeline

| Pipeline Stage | Feature | Action |
|---------------|---------|--------|
| **Qualification** | Send intro email, schedule discovery call | `send-email`, `create-event` |
| **Demand Research** | Review client emails, schedule follow-ups | `list-emails`, `create-event` (follow_up_call) |
| **Solution / Viewing** | Schedule viewings, attach confirmation emails | `create-event` (viewing), `attach-email` |
| **Decision Making** | Attach negotiation emails, check team availability | `attach-email`, `get-schedule` |
| **Deal Signing** | Schedule signing, send deal documents | `create-event` (contract_signing), `send-email` |
| **Verification** | Scan for broker replies to info requests | `check-verification-replies` |

---

## Cross-Reference

| For | See |
|-----|-----|
| SSO OAuth flow (separate from O365 OAuth) | [app-template.md](app-template.md) §Dual-Supabase Architecture |
| Security model and RLS patterns | [security-model.md](security-model.md) |
| Edge Function API catalog | [api-contracts.md](api-contracts.md) |
| Sales pipeline stages | [sales-pipeline.md](../business-processes/sales-pipeline.md) |
| SM Pipeline codebase | `/home/bitnami/matrix-pipeline` |
