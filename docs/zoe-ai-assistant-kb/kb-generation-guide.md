# How to Generate a Support KB Article for Any Sharp Matrix App

> **Purpose:** Step-by-step instructions for generating a 1st line support knowledge base article for any new or existing Sharp Matrix application. Follow this guide to produce a consistent, RAG-optimized document that the Zoe AI Assistant can use to help end users.

---

## Overview

Each app in the Sharp Matrix platform should have a dedicated support KB article in the `docs/zoe-ai-assistant-kb/` directory. These articles are consumed by a RAG-powered AI assistant (Zoe) that provides 1st line support to business users with minimal technical knowledge.

The articles must be:

- **Self-contained** — each article covers one app completely without requiring external references.
- **Non-technical** — written for everyday business users, not developers or IT professionals.
- **RAG-optimized** — clear section headers, natural-language FAQ, structured troubleshooting tables.
- **Actionable** — step-by-step instructions, not abstract descriptions.
- **Consistent** — all articles follow the same structure for predictable retrieval.

---

## Who Is the Reader? (Zoe's Audience)

Zoe's primary users are **real estate professionals, office staff, and support employees** who:

- Have **limited technology knowledge** — they know how to use a web browser, email, and basic office tools, but they are not "tech-savvy."
- Think in terms of **tasks and outcomes**, not systems and data flows.
- Do **not** understand developer or IT terminology (API, JWT, WebSocket, RLS, Edge Function, database, migration, token, webhook, payload, endpoint, schema, CRUD, etc.).
- May be **frustrated or confused** when something doesn't work — Zoe's tone must be calm, patient, and reassuring.
- Speak **English or Russian** — keep sentences short and simple for easier comprehension and translation.

### Persona Examples

| User | Typical question | What they DON'T know |
|------|-----------------|---------------------|
| Broker (age 45) | "How do I register a new client?" | What an API is, what a database is, what SSO means technically |
| Office assistant | "My page shows an error, what do I do?" | How to open browser console, what a token is, what cache means |
| Sales Manager | "Where do I see my team's numbers?" | What scope or RLS means, what a query is |
| HR coordinator | "How do I approve a vacation?" | What an approval chain is called technically, what AD sync means |
| Finance analyst | "How do I enter last month's numbers?" | What a data layer is, what an Edge Function does |

### Golden Rule

**If a sentence would confuse a 50-year-old real estate broker who only uses their phone and email, rewrite it.**

---

## Tone and Language Rules

### DO:
- Use **plain, everyday language**: "click", "type", "choose", "go to", "you will see"
- Explain **what the user sees on screen**, not what happens behind the scenes
- Use **friendly, patient tone** — assume the user is asking for the first time
- Say **"the system"** or **"the app"** instead of naming technical components
- Describe errors as **"something went wrong"** before giving specific guidance
- Use **analogies** when helpful: "Think of it as your inbox for IT requests"
- Write **short sentences** — aim for 15-20 words per sentence maximum
- Define abbreviations **on first use** in each article: "MLS (the shared property database)"

### DON'T:
- Use developer terms: ~~API~~, ~~endpoint~~, ~~webhook~~, ~~token~~, ~~JWT~~, ~~RLS~~, ~~Edge Function~~, ~~schema~~, ~~migration~~, ~~CRUD~~, ~~payload~~, ~~query~~, ~~WebSocket~~, ~~cache~~ (say "temporary saved data" or "stored page data" instead)
- Reference database tables, column names, or code files
- Mention Supabase, Deno, React, TypeScript, or any framework
- Use IT jargon without explanation: ~~SLA~~, ~~CMDB~~, ~~AD sync~~, ~~OAuth~~, ~~PKCE~~
- Assume the user knows what "clearing browser cache" means — give exact steps instead
- Use passive voice: say "Click Save" not "The record will be saved"
- Use conditional/subjunctive mood: say "Click Save" not "You would click Save"

### When Technical Terms Are Unavoidable

Some terms appear in the UI itself (e.g., "CMDB" is a sidebar label in ITSM). In these cases:
1. Use the term as it appears in the app
2. Immediately explain it in plain language: "CMDB (the list of all IT equipment and software in the company)"
3. Never assume the user already knows what it means

---

## Step 1: Explore the App Repository

Before writing anything, thoroughly explore the app's source code to understand it. Read the following files:

### Required Files to Read

| File | What You Learn |
|------|---------------|
| `package.json` | App name, dependencies, scripts |
| `src/App.tsx` | Routes, page structure, base path |
| `src/main.tsx` | Entry point, providers |
| `src/lib/matrix-sso.ts` | CLIENT_ID, BASE_PATH, SSO URLs, environment detection |
| `src/pages/*.tsx` | Every page the user can visit |
| `src/components/layout/` | Sidebar navigation, header, layout structure |
| `src/types/` or `src/lib/api-types.ts` | Data models, entities, enums |
| `src/hooks/` | Data fetching, business logic |
| `src/contexts/AuthContext.tsx` | Auth flow, user state |
| `src/lib/role-permissions.ts` | Role definitions, page permissions |
| `src/data/helpContent.ts` | Existing in-app help (FAQ, troubleshooting) — if it exists |
| `src/integrations/supabase/` | Supabase clients, types, data layer |
| `supabase/functions/` | Edge Functions (server-side logic) |
| `README.md` and `docs/` | Any existing documentation |
| `src/locales/` | i18n translations — if they exist |

### Key Questions to Answer

1. **What is this app?** One-sentence description a non-technical user would understand.
2. **Who uses it?** List each user role and what they do.
3. **What are the main features?** Group by user role.
4. **What are all the pages?** Map routes to user-facing page names.
5. **What entities/data does it manage?** In plain language (e.g., "clients", "appointments", not "contacts table" or "entity_events").
6. **What are the key workflows?** Step-by-step: user opens page → does X → result is Y.
7. **What statuses/states exist?** (e.g., Pending → Approved → Rejected)
8. **What error messages can the user see?** Search for `toast.error`, `toast.warning`, validation messages.
9. **What are known limitations?** Search for TODOs, FIXMEs, hardcoded workarounds, missing features.
10. **What external services does it depend on?** (AI APIs, Twilio, etc.)

---

## Step 2: Write the Article

Use the following template. Every section is required unless marked optional.

### Article Template

```markdown
# Sharp Matrix [App Name] — 1st Line Support Knowledge Base

> **App name:** [Display name]
> **URL:** `https://intranet.sharpsir.group/[path]/`
> **Purpose:** [One sentence — what the app does, in plain language]
> **Users:** [Comma-separated list of user roles]

---

## What Is [App Name]?

[2-3 sentences explaining the app in plain language. No technical jargon.
Focus on what the user achieves, not how it works internally.]

---

## How to Access [App Name]

[Step-by-step login instructions. Always include:]
1. Open browser and go to [URL].
2. SSO login redirect.
3. Sign in (email/password or Microsoft).
4. Landing page after login.

[Add a note about what to do if they can't log in.]

---

## User Roles and What They Can Do

[Table with columns: Role | Home Page | What They Can Do]

---

## Main Features

### [Feature 1 Name] ([Which Role])

[Step-by-step instructions. Number each step. Include what the user sees,
what they click, what they type, and what happens next.]

### [Feature 2 Name]

[Repeat for each major feature. Group by workflow or role.]

---

## [Domain-Specific Concepts] (if applicable)

[Explain any statuses, types, or terminology the user needs to understand.
Use a table: Term | Meaning]

---

## Frequently Asked Questions

### [Category]

**Q: [Natural question a user would ask]**
A: [Clear, direct answer. No jargon.]

[Include 10-20 FAQ entries covering:]
- What is this app?
- Who can use it?
- How do I do [common task]?
- What does [status/term] mean?
- What if I made a mistake?
- Can I [common request]?

---

## Troubleshooting

### [Category]

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| [What the user sees] | [Why it happens] | [Specific fix steps] |

[Include 10-15 troubleshooting entries covering:]
- Login / access issues
- Form / data entry problems
- Display / loading issues
- Feature-specific problems
- Network / connectivity issues

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| [Description] | [How to work around it] | [By design / Known / Planned fix / Configuration] |

---

## When to Escalate — Incident Reporting

If the user cannot resolve the issue, direct them to the standard incident template:

> Report the issue using the standard template — see [How to Report an Incident](incident-reporting.md). Mention **[App Name]** as the app name.

Do **not** duplicate the template or severity guide in each app article. The centralized [incident-reporting.md](incident-reporting.md) contains the 4-question template, app-specific hints, severity guide, and escalation path.

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| [Common task] | [Navigation path] |
[10-15 entries covering all main tasks]
```

---

## Step 3: Quality Checklist

Before finalizing, verify:

### Structure
- [ ] **Header block** has app name, URL, purpose, and users.
- [ ] **"What Is"** section uses no technical jargon.
- [ ] **"How to Access"** includes login steps (say "log in with your company email" — avoid "SSO" as a user-facing term).
- [ ] **Roles table** lists every role the app supports.
- [ ] **Features** section has step-by-step instructions (numbered) for every major workflow.
- [ ] **FAQ** has 10+ entries covering common user questions.
- [ ] **Troubleshooting** has 10+ entries in Problem/Cause/Solution table format.
- [ ] **Known Issues** table exists (even if empty — "No known issues at this time").
- [ ] **Escalation** section points to the incident reporting guide.
- [ ] **Quick Reference Card** covers all main tasks.
- [ ] File is saved as `docs/zoe-ai-assistant-kb/[app-slug].md`.

### Language (Critical — read every sentence aloud)
- [ ] No code snippets, API references, or developer terminology anywhere.
- [ ] No mention of: Supabase, Edge Functions, JWT, tokens, RLS, webhooks, schemas, CRUD, WebSocket, Deno, React.
- [ ] Statuses and domain terms are explained in plain language on first use.
- [ ] "Clearing cache" is replaced with specific browser steps (e.g., "Press Ctrl+Shift+Delete, select 'Cached images and files', and click Clear").
- [ ] Every instruction uses active voice and starts with a verb: "Click", "Go to", "Type", "Select".
- [ ] Sentences average 15-20 words. No paragraphs longer than 4 sentences.
- [ ] The article passes the "50-year-old broker" test — would they understand every sentence without help?

---

## Step 4: Register the Article

After creating the article:

1. **Update the index:** Add the new article to `docs/zoe-ai-assistant-kb/index.md`.
2. **Update the main index:** Add a row to the Chapter 7 table in `docs/INDEX.md`.
3. **Update AGENTS.md:** Add the article path to the "For Zoe AI Assistant" section.
4. **Update platform-overview.md:** Add the app to the "App-Specific Support Articles" table.

---

## Step 5: AI Agent Prompt (Automated Generation)

If you are an AI agent generating a KB article, use this prompt framework:

```
Thoroughly explore the repository at /home/bitnami/[app-directory]. Gather:

1. App purpose, target users, main features
2. All pages/routes and what each does
3. All UI components and their roles
4. Data models and entities
5. Sidebar/navigation structure
6. Key workflows and business processes
7. Integration points (APIs, external services)
8. Permission model and roles
9. Error handling, toast messages, validation rules
10. i18n languages (if any)
11. Configuration (matrix-sso.ts, supabase clients)
12. In-app help content (helpContent.ts)
13. Known issues or limitations

Then write a support KB article following the template in
docs/zoe-ai-assistant-kb/kb-generation-guide.md.

CRITICAL — Audience and tone:
- Write for real estate professionals with LIMITED technology knowledge.
- They know how to use a browser and email. That's it.
- Never use developer terms (API, token, cache, webhook, database, schema, CRUD, RLS, JWT, Edge Function, WebSocket, etc.).
- Explain everything as "what you see on screen" and "what to click".
- If a technical term appears in the UI (like "CMDB"), always explain it in parentheses on first use.
- Keep sentences short (15-20 words). Use active voice. Start instructions with verbs.
- The article must pass the "50-year-old broker" test — would they understand every word?
Use the exact section structure from the template.
```

---

## Naming Convention

| Aspect | Convention | Example |
|--------|-----------|---------|
| File name | Kebab-case app slug | `client-connect.md`, `meeting-hub.md` |
| Article title | "Sharp Matrix [Display Name] — 1st Line Support Knowledge Base" | "Sharp Matrix Client Connect — 1st Line Support Knowledge Base" |
| Directory | `docs/zoe-ai-assistant-kb/` | — |

---

## Existing Articles

| App | File | Created |
|-----|------|---------|
| Agency Portal | `portal.md` | Yes |
| Client Connect | `client-connect.md` | Yes |
| Meeting Hub | `meeting-hub.md` | Yes |
| Matrix Comms | `comms.md` | Yes |
| Matrix Pipeline | `pipeline.md` | Yes |
| Matrix HR Management | `hrms.md` | Yes |
| ITSM | `itsm.md` | Yes |
| Matrix Financial Management | `financial-management.md` | Yes |
| SSO & Auth | `platform-sso-auth.md` | Yes |
| Platform Overview | `platform-overview.md` | Yes |
| 2nd Line Tech Reference | `second-line-tech-reference.md` | Yes |
