# Sharp Matrix Platform — 1st Line Support Overview

> **Platform name:** Sharp Matrix
> **Organization:** Sharp Sotheby's International Realty
> **Markets:** Cyprus, Hungary, Kazakhstan
> **Portal URL:** `https://intranet.sharpsir.group/agency-portal/`
> **Purpose:** Digital brokerage platform for real estate operations — client management, appointments, communications, listings, analytics, and more.

---

## What Is Sharp Matrix?

Sharp Matrix is the digital workplace for Sharp Sotheby's International Realty. It is a set of web applications that all share one login — you sign in once and can open any app without logging in again. All employees use Sharp Matrix for their daily work — registering clients, recording meetings, communicating with leads via WhatsApp, viewing reports, and managing their workflow.

The platform is accessed through a web browser. There is nothing to install — just open the URL and log in.

---

## Platform Apps at a Glance

| App | URL Path | What It Does | Who Uses It |
|-----|----------|-------------|-------------|
| **Agency Portal** | `/agency-portal/` | Home dashboard, app launcher, AI Advisor, stats | Everyone |
| **Client Connect** | `/client-connect/` | Register and verify new clients | Brokers, Contact Center, Sales Managers |
| **Meeting Hub** | `/meeting-hub/` | Record and manage appointments | Brokers, Sales Managers |
| **Matrix Communications** | `/comms/` | WhatsApp Business messaging, campaigns | Brokers, Marketing, Sales |
| **Matrix Pipeline** | `/matrix-pipeline/` | Leads, deals, contacts, MLS data, email/calendar | Brokers, Sales Managers, Call Center |
| **HRMS** | `/matrix-hr-management/` | Employee records, vacations, onboarding, performance | All Employees, HR, Managers |
| **ITSM** | `/itsm/` | IT service requests, assets, licenses, vendors | All (requests), IT Staff (admin) |
| **Matrix FM** | `/matrix-fm/` | Financial reporting, budgeting, planning, analytics | Finance Team, Entity Managers |
| **SSO Console** | `/sso-console/` | User and access management | Admins only |
| **SSO Login** | `/sso-login/` | Login page | Everyone (automatic) |

All apps are hosted at `https://intranet.sharpsir.group/` followed by the path listed above.

---

## How Everything Connects

```
                         ┌──────────────────┐
                         │   SSO Login      │
                         │  (one login for  │
                         │   all apps)      │
                         └────────┬─────────┘
                                  │
                         ┌────────▼─────────┐
                         │  Agency Portal   │
                         │  (your homepage) │
                         └────────┬─────────┘
                                  │
     ┌──────────┬─────────┬───────┼───────┬──────────┬──────────┐
     │          │         │       │       │          │          │
  ┌──▼───┐  ┌──▼──┐  ┌───▼──┐ ┌──▼──┐ ┌──▼───┐  ┌──▼──┐  ┌───▼──┐
  │Client│  │Meet-│  │Matrix│ │Pipe-│ │ HRMS │  │ITSM │  │Matrix│
  │Connct│  │ ing │  │Comms │ │line │ │(HR)  │  │(IT) │  │ FM   │
  │      │  │ Hub │  │      │ │(CRM)│ │      │  │     │  │(Fin.)│
  └──────┘  └─────┘  └──────┘ └─────┘ └──────┘  └─────┘  └──────┘
```

- **One login gives access to all apps** — you don't need to log in separately.
- **Client data is shared** — a client registered in Client Connect is visible in Meeting Hub.
- **The Agency Portal shows stats from all apps** — pipeline, clients, meetings.

---

## Getting Started

### First-Time Users

1. **Get your credentials.** Your Admin will create your account and give you an email and temporary password.
2. **Open the portal.** Go to `https://intranet.sharpsir.group/agency-portal/`.
3. **Log in.** Enter your email and password, or click "Sign in with Microsoft."
4. **Explore the dashboard.** See your stats, access apps, and try the AI Advisor.
5. **Open the apps you need.** Click the app cards or use the Quick Access bar.

### What to Do First Depending on Your Role

| If you are a... | Start here |
|-----------------|------------|
| **Broker / Agent** | Open Client Connect to register your first client. Open Meeting Hub to record an appointment. |
| **Contact Center (MLS Staff)** | Open Client Connect → Client Verification to process pending registrations. |
| **Sales Manager** | Open the Agency Portal to see team stats. Open Client Connect → Review Requests for escalations. |
| **Marketing Manager** | Open Matrix Communications to manage WhatsApp templates and campaigns. |
| **HR Manager** | Open HRMS to manage personnel, vacations, onboarding, and performance reviews. |
| **Finance Manager** | Open Matrix FM to manage financial reporting and budgeting. |
| **IT Staff** | Open ITSM to manage the service desk queue, assets, and licenses. |
| **Admin** | Open the SSO Console to manage users, roles, and permissions. |

---

## Your First Week at Sharp Matrix

Your first week is about getting comfortable with the platform. Here is a day-by-day guide:

### Day 1 — Get Connected
1. **Receive your credentials** from your Admin (email + temporary password).
2. **Log in** to the Agency Portal at `https://intranet.sharpsir.group/agency-portal/`.
3. **Change your password** if prompted.
4. **Explore the dashboard** — see the app cards, your stats, and the AI Advisor.
5. **Check your profile** — click your avatar → Profile to see your role, scope, and team.

### Day 2 — Learn Your Primary App
- **Brokers / Sales staff**: Open **Client Connect** and register a test client (or your first real one). Then open **Meeting Hub** and record a test appointment.
- **Call Center / MLS Staff**: Open **Client Connect** → Client Verification. Familiarize yourself with the verification queue, MLS duplicate checking, and the approve/reject/return workflow.
- **Sales Managers**: Explore the **Agency Portal** stats dashboard. Then open **Matrix Pipeline** to see your team's deal Kanban. Check **Opportunity Reviews** for deals needing your attention.
- **HR staff**: Open **HRMS** → Personnel section. Browse the employee directory, org structure, and leave management.
- **Finance staff**: Open **Matrix FM** → Monthly Reporting. Select your entity and explore the financial grid layout.
- **IT staff**: Open **ITSM** → SD Queue. Explore ticket workflows, asset management, and the classification tree.
- **All employees**: Open **HRMS** and check your own dashboard — your leave balance, documents, and performance reviews are all here.

### Day 3 — Connect the Dots
- **Send a WhatsApp message**: Open **Matrix Communications** and start a conversation using a template.
- **Link an email to a deal**: In **Matrix Pipeline**, connect your Microsoft 365 account (Settings → Microsoft 365) and link an email thread to an opportunity.
- **Submit an IT request**: Open **ITSM** → My Requests → New Request. Practice submitting a request so you know how when you need it.
- **Request time off**: Open **HRMS** → My Vacations and familiarize yourself with the vacation request form (no need to submit yet).

### Day 4 — Understand Your Data Visibility
- **Check your scope**: Your role determines what data you see. Brokers see only their own records. Managers see their team. Directors see everything.
- **Test navigation**: Practice switching between apps using the Agency Portal, the sidebar "Back to Agency Hub" link, and direct URLs.
- **Try both languages**: Some apps (HRMS, Matrix Pipeline, ITSM, Matrix Communications) support English and Russian — use the language toggle in the sidebar footer. Other apps (Agency Portal, Client Connect, Meeting Hub) are currently English-only.

### Day 5 — Build Your Routine
- **Set up your morning workflow**: Open the Agency Portal first for an overview, then go to your primary app.
- **Ask Zoe**: If you have any questions, ask the **AI Advisor** in the Agency Portal or contact Zoe directly. Zoe knows all Sharp Matrix apps and can guide you step by step.
- **Know your escalation path**: If something doesn't work, try troubleshooting with Zoe first. If Zoe can't resolve it, submit an IT request in ITSM.

---

## How Zoe Can Help You

Zoe is your AI assistant for all things Sharp Matrix. Here is what Zoe can do:

### Ask Zoe Anything About Sharp Matrix
- **"How do I register a new client?"** — Zoe will walk you through Client Connect step by step.
- **"How do I request a vacation?"** — Zoe will explain the HRMS vacation workflow.
- **"My vacation is 'Pending' at the Manager step — what does that mean?"** — Zoe knows all statuses and approval steps.
- **"How do I move a deal to the next stage?"** — Zoe can explain Pipeline workflows.
- **"What is CORE allocation?"** — Zoe can explain financial concepts from Matrix FM.

### Zoe Can Help You Open IT Support Requests
If you have a technical problem with any Sharp Matrix app, Zoe can guide you through creating an ITSM ticket:

1. **Describe the problem to Zoe.** For example: "My Meeting Hub is showing a blank page."
2. **Zoe will try to help first** — checking if it's a known issue, suggesting troubleshooting steps (refresh the page, check your permissions).
3. **If the issue persists**, Zoe will guide you to open an ITSM request:
   - Go to `https://intranet.sharpsir.group/itsm/`
   - Navigate to **My Requests → New Request**
   - Fill in: Title, Description, Priority, Service Type, and Related Asset
   - Zoe can suggest appropriate priority and service type based on your description
4. **Zoe will remind you** to include key details: the app name, what you were doing, the error message, and a screenshot if possible.

### Zoe Knows These Common Situations

| You say... | Zoe will help you... |
|-----------|---------------------|
| "I can't log in" | Troubleshoot SSO, suggest clearing cookies, or direct you to IT |
| "I need a new laptop" | Guide you to ITSM → New Request → Service Request |
| "My app is showing an error" | Check if it's known, suggest fixes, or help you submit an ITSM ticket |
| "How do I export a report?" | Walk you through the export feature in the relevant app |
| "I need access to Matrix Pipeline" | Explain that you need to contact your Admin for role/permission changes |
| "What's my leave balance?" | Direct you to HRMS → My Vacations |
| "A client is duplicated in the system" | Explain the MLS duplicate check process in Client Connect |

---

## Best Practices for All Sharp Matrix Users

### Data Quality
- **Always register clients in Client Connect first** before recording meetings or creating pipeline deals. This ensures proper data flow across apps.
- **Use autocomplete** when entering client or contact names — it pulls from existing records and prevents duplicates.
- **Fill in all required fields** — incomplete records cause issues downstream. Don't skip budget, lead source, or contact details.
- **Save frequently** — especially in Matrix FM and ITSM. There is no auto-save.

### Security and Access
- **Never share your login credentials** — each user has their own SSO account.
- **Log out when using shared computers** — click your avatar → Sign Out.
- **Don't use personal email** — only your `@sharpsir.group` company email works.
- **Report suspicious activity** — if you notice unauthorized changes to data, report immediately to IT via ITSM.

### Productivity Tips
- **Use the Agency Portal as your home base** — it aggregates stats and provides quick access to all apps.
- **Use keyboard shortcuts** — in the financial grid (Matrix FM), you can Tab between cells and paste from Excel.
- **Use voice input** — in Client Connect and Meeting Hub, voice input can speed up data entry.
- **Set language once** — your language preference is saved and applies across sessions.
- **Use dark mode** — all apps support dark mode via the theme toggle in the sidebar footer. It's easier on the eyes during evening work.

### Communication
- **Use templates for first WhatsApp messages** — in Matrix Communications, use an approved template when messaging a client for the first time or after 24 hours of no reply.
- **Link emails to deals** — in Matrix Pipeline, always link relevant email conversations to opportunities. This keeps the full context in one place.
- **Use internal notes** — in Matrix Communications, use notes to share context with colleagues. Clients cannot see internal notes.

---

## Common Tasks Across All Apps

### How to Log In
1. Go to any Sharp Matrix app URL.
2. Enter your email and password on the SSO Login page, or use "Sign in with Microsoft."
3. You are redirected to the app.

### How to Log Out
1. Click your avatar (profile picture or initials) in the top-right corner of any app.
2. Click **Sign Out**.

### How to Switch Between Apps
- From the **Agency Portal**, click any app card.
- From any app's sidebar, click **Back to SharpMatrix** or **Back to Agency Hub**.
- You can also type the app URL directly in your browser.

### How to Check Your Role and Permissions
1. Click your avatar in the top-right corner.
2. Click **Profile**.
3. Your role, scope, permissions, and team membership are displayed.

### How to Get Help
- **In each app:** Look for a **Help** item in the sidebar or menu.
- **In the Agency Portal:** Ask the **AI Advisor** (the Sparkles ✨ button in the bottom-right corner).
- **For account or access issues:** Contact your Admin or IT department.
- **For persistent issues:** Follow the incident reporting process (see below).

---

## Frequently Asked Questions

### General Platform

**Q: What is Sharp Matrix?**
A: It is the digital platform used by Sharp Sotheby's International Realty for managing clients, appointments, communications, and analytics. It includes several web apps connected by a single login system.

**Q: Do I need to install anything?**
A: No. Sharp Matrix runs in your web browser. Use Chrome, Edge, Safari, or Firefox (latest versions).

**Q: Which browser is recommended?**
A: Google Chrome or Microsoft Edge for the best experience. Safari and Firefox also work.

**Q: Can I use Sharp Matrix on my phone?**
A: Yes. The apps are mobile-responsive and work on smartphones and tablets. For the best experience, use your phone's web browser in landscape mode for apps with tables/dashboards.

**Q: Is my data safe?**
A: Yes. All data is encrypted in transit (HTTPS) and at rest. Access is controlled by roles and permissions. The platform follows GDPR guidelines for data protection.

### Login and Access

**Q: I forgot my password.**
A: Contact your Admin or IT department. They can reset your password from the SSO Console.

**Q: I can't access an app.**
A: Your role may not have permission for that app. Contact your Admin to verify your access.

**Q: I got logged out unexpectedly.**
A: Your session may have expired due to inactivity. Log in again — your data is safe.

**Q: Can I use my personal email?**
A: No. You must use your Sharp Sotheby's company email address.

### Data

**Q: I can't see data that my colleague can see.**
A: You may have a different role or scope. Brokers see only their own data, while Managers see team-wide data. This is by design.

**Q: Data I entered in one app shows up in another.**
A: Yes, this is expected. Client Connect, Meeting Hub, and the Agency Portal share data to give you a complete picture.

**Q: I accidentally deleted something. Can it be recovered?**
A: Contact your Admin or 2nd Line Support immediately. Some data may be recoverable from backups, but there is no undo button.

---

## Cross-App Troubleshooting

### Issues That Affect All Apps

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in to any app** | SSO system is down, or credentials issue | Try again in a few minutes. If widespread, IT is likely already investigating. Contact IT. |
| **All apps are slow** | Server performance issue or network problem | Check your internet speed. Try a different browser. If all colleagues have the same issue, report to IT. |
| **"Not authenticated" error in multiple apps** | Your login session has expired | Log out of all apps. Then close your browser, reopen it, and log in again. If the problem continues, press Ctrl+Shift+Delete, clear "Cookies" for the last hour, and try again. |
| **Blank pages or apps not loading** | Old browser or stored page data issue | Press Ctrl+Shift+Delete, select "Cached images and files", and click Clear. Make sure your browser (Chrome, Edge, Safari, or Firefox) is updated to the latest version. |
| **Error messages in a language I don't understand** | Browser language setting | Check the app's language setting (if available in sidebar/settings). |

### Browser Issues

| Problem | What to Do |
|---------|------------|
| **Pages look broken or misaligned** | Press Ctrl+Shift+Delete, select "Cached images and files", click Clear, and refresh the page. Or try opening the page in a private/incognito window (Ctrl+Shift+N in Chrome). |
| **Features not working in Safari** | Some features work best in Chrome or Edge. Try switching browsers. |
| **Pop-ups or new windows blocked** | Allow pop-ups from `intranet.sharpsir.group` in your browser settings. |
| **Microphone or camera not working** | Allow microphone/camera access for the site in your browser settings (padlock icon in address bar). |

---

## Incident Reporting Guide

When you encounter an issue that cannot be resolved with the information in this knowledge base, submit an incident to the 2nd Line Support team.

### Step 1: Determine If It Is a Bug or a Question

| Type | Description | Example |
|------|-------------|---------|
| **How-To Question** | You want to know how to do something | "How do I register a client?" → Check the app's KB article first |
| **Access Issue** | You cannot access an app or page | "I get Access Denied on Analytics" → Contact Admin first |
| **Bug** | Something is broken or behaving incorrectly | "I click Save but nothing happens and I get an error" |
| **Data Issue** | Data appears wrong, missing, or duplicated | "My pipeline value shows zero even though I have active deals" |
| **Feature Request** | You want something new or different | "It would be nice if I could export to PDF" |

### Step 2: Submit Using the Standard Template

Use the incident reporting template to describe the issue, classify severity, and submit.

See the full guide: **[How to Report an Incident](incident-reporting.md)** — includes the 4-question template, a filled-out example, app-specific hints, severity guide, and escalation path.

---

## Glossary of Common Terms

| Term | Meaning |
|------|---------|
| **SSO (Single Sign-On)** | The shared login system — you sign in once and get access to all Sharp Matrix apps |
| **Agency Portal** | The home dashboard of Sharp Matrix |
| **Client Connect** | App for registering and verifying clients |
| **Meeting Hub** | App for recording appointments |
| **Matrix Communications** | App for WhatsApp Business messaging |
| **SSO Console** | Admin tool for managing users and permissions |
| **Role** | Your job function in the system (e.g., Broker, Sales Manager, Admin) |
| **Scope** | How much data you can see — ranges from "only my own data" to "everything in the company" |
| **RFI** | Request for Information — asking a broker for more client details |
| **MLS** | Multiple Listing Service — the shared property listing system |
| **Pipeline Value** | Total value of active deals and reservations |
| **Template** | Pre-approved message format (used in WhatsApp) |
| **Campaign** | Bulk messaging to multiple contacts (via Comms) |
| **Quick Reply / Snippet** | Saved response text for fast messaging |
| **AI Advisor** | The AI chat assistant in the Agency Portal |
| **Matrix Pipeline** | App for managing sales leads, deals, contacts, and MLS property data |
| **HRMS** | Human Resources Management System — app for employee records, vacations, onboarding, performance |
| **ITSM** | IT Service Management — app for submitting IT requests, managing assets and licenses |
| **Matrix FM** | Matrix Financial Management — app for financial reporting, budgeting, and planning |
| **CMDB** | Configuration Management Database — IT asset inventory in ITSM |
| **CORE Allocation** | Distribution of central overhead costs across group entities (in Matrix FM) |
| **Act As** | Feature that lets admins switch to a different role for testing |

---

## App-Specific Support Articles

For detailed support on each app, refer to the dedicated knowledge base articles:

| App | Support Article |
|-----|----------------|
| Agency Portal | `docs/zoe-ai-assistant-kb/portal.md` |
| Client Connect | `docs/zoe-ai-assistant-kb/client-connect.md` |
| Meeting Hub | `docs/zoe-ai-assistant-kb/meeting-hub.md` |
| Matrix Communications | `docs/zoe-ai-assistant-kb/comms.md` |
| Matrix Pipeline | `docs/zoe-ai-assistant-kb/pipeline.md` |
| Matrix HR Management | `docs/zoe-ai-assistant-kb/hrms.md` |
| ITSM | `docs/zoe-ai-assistant-kb/itsm.md` |
| Matrix Financial Management | `docs/zoe-ai-assistant-kb/financial-management.md` |
| SSO & Authentication | `docs/zoe-ai-assistant-kb/platform-sso-auth.md` |
| 2nd Line Tech Reference | `docs/zoe-ai-assistant-kb/second-line-tech-reference.md` |

---

## Support Contact Information

| Channel | When to Use |
|---------|------------|
| **AI Support Assistant** | First point of contact for all questions and issues |
| **Your Manager / Admin** | Access and permission requests, role changes |
| **IT Department** | Login issues, Microsoft AD problems, infrastructure |
| **2nd Line Support** | Qualified incidents after 1st line triage |
