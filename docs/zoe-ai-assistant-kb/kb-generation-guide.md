# How to Generate a Support KB Article for Any Sharp Matrix App

> **Purpose:** Step-by-step instructions for generating a 1st line support knowledge base article for any new or existing Sharp Matrix application. Follow this guide to produce a consistent, RAG-optimized document that the Zoe AI Assistant can use to help end users.

---

## Overview

Each app in the Sharp Matrix platform should have a dedicated support KB article in the `docs/zoe-ai-assistant-kb/` directory. These articles are consumed by a RAG-powered AI assistant (Zoe) that provides 1st line support to business users with minimal technical knowledge.

The articles must be:

- **Self-contained** — each article covers one app completely without requiring external references.
- **Non-technical** — written for business users (brokers, agents, managers), not developers.
- **RAG-optimized** — clear section headers, natural-language FAQ, structured troubleshooting tables.
- **Actionable** — step-by-step instructions, not abstract descriptions.
- **Consistent** — all articles follow the same structure for predictable retrieval.

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

[Standard escalation section — copy from existing articles and adjust app name]

### What to Include in an Incident Report

1. Your name and role
2. App name: [App Name]
3. Date and time
4. Page/section
5. What you were trying to do
6. What happened instead
7. [App-specific ID if applicable]
8. Screenshot
9. Browser and device
10. Reproducible?
11. Severity: Critical / High / Medium / Low

### Escalation Path

| Level | Team | Handles |
|-------|------|---------|
| 1st Line | AI Support Assistant | Questions, guidance, known issues, workarounds |
| 2nd Line | Support / Operations | Analysis, qualification, config fixes, data corrections |
| 3rd Line | Development Team | Bug fixes, features, infrastructure |

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

- [ ] **Header block** has app name, URL, purpose, and users.
- [ ] **"What Is"** section uses no technical jargon.
- [ ] **"How to Access"** includes SSO login steps.
- [ ] **Roles table** lists every role the app supports.
- [ ] **Features** section has step-by-step instructions (numbered) for every major workflow.
- [ ] **FAQ** has 10+ entries covering common user questions.
- [ ] **Troubleshooting** has 10+ entries in Problem/Cause/Solution table format.
- [ ] **Known Issues** table exists (even if empty — "No known issues at this time").
- [ ] **Escalation** section has incident report template and severity definitions.
- [ ] **Quick Reference Card** covers all main tasks.
- [ ] No code snippets, API references, or developer terminology.
- [ ] Statuses and domain terms are explained in plain language.
- [ ] File is saved as `docs/zoe-ai-assistant-kb/[app-slug].md`.

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
Write for business users with zero technical knowledge.
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
| SSO & Auth | `platform-sso-auth.md` | Yes |
| Platform Overview | `platform-overview.md` | Yes |
| 2nd Line Tech Reference | `second-line-tech-reference.md` | Yes |
