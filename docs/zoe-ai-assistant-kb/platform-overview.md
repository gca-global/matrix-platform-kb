# Sharp Matrix Platform — 1st Line Support Overview

> **Platform name:** Sharp Matrix
> **Organization:** Sharp Sotheby's International Realty
> **Markets:** Cyprus, Hungary, Kazakhstan
> **Portal URL:** `https://intranet.sharpsir.group/agency-portal/`
> **Purpose:** Digital brokerage platform for real estate operations — client management, appointments, communications, listings, analytics, and more.

---

## What Is Sharp Matrix?

Sharp Matrix is the digital workplace for Sharp Sotheby's International Realty. It is a suite of web applications connected by a Single Sign-On (SSO) system. All employees use Sharp Matrix for their daily work — registering clients, recording meetings, communicating with leads via WhatsApp, viewing reports, and managing their workflow.

The platform is accessed through a web browser. There is nothing to install — just open the URL and log in.

---

## Platform Apps at a Glance

| App | URL Path | What It Does | Who Uses It |
|-----|----------|-------------|-------------|
| **Agency Portal** | `/agency-portal/` | Home dashboard, app launcher, AI Advisor, stats | Everyone |
| **Client Connect** | `/client-connect/` | Register and verify new clients | Brokers, Contact Center, Sales Managers |
| **Meeting Hub** | `/meeting-hub/` | Record and manage appointments | Brokers, Sales Managers |
| **Matrix Comms** | `/comms/` | WhatsApp Business messaging, campaigns | Brokers, Marketing, Sales |
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
            ┌────────────────┼────────────────┐
            │                │                │
   ┌────────▼──────┐ ┌──────▼───────┐ ┌──────▼──────┐
   │ Client Connect│ │ Meeting Hub  │ │ Matrix Comms│
   │ (clients)     │ │ (meetings)   │ │ (WhatsApp)  │
   └───────────────┘ └──────────────┘ └─────────────┘
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
| **Marketing Manager** | Open Matrix Comms to manage WhatsApp templates and campaigns. |
| **Admin** | Open the SSO Console to manage users, roles, and permissions. |

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
- **In the Agency Portal:** Ask the **AI Advisor** (chat icon in the bottom-right corner).
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
| **"Not authenticated" error in multiple apps** | Session tokens expired | Log out of all apps, clear browser cookies for `intranet.sharpsir.group`, and log in again. |
| **Blank pages or apps not loading** | JavaScript blocked, old browser, or cache issue | Clear browser cache. Ensure JavaScript is enabled. Update your browser to the latest version. |
| **Error messages in a language I don't understand** | Browser language setting | Check the app's language setting (if available in sidebar/settings). |

### Browser Issues

| Problem | What to Do |
|---------|------------|
| **Pages look broken or misaligned** | Clear browser cache (Ctrl+Shift+Delete). Try a private/incognito window. |
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

### Step 2: Gather Information

For bugs and data issues, collect:

1. **Your name and role**
2. **Which app** (Client Connect, Meeting Hub, Comms, Portal, SSO)
3. **Date and time** of the issue
4. **Page or screen** where it happened
5. **What you did** (step-by-step)
6. **What you expected to happen**
7. **What actually happened** (exact error text if shown)
8. **Screenshot or screen recording** if possible
9. **Browser and device** (e.g., "Chrome 120 on Windows 11 laptop")
10. **Can you reproduce it?** (every time, sometimes, just once)
11. **How many people are affected?** (just me, my team, everyone)

### Step 3: Classify Severity

| Severity | Criteria | Examples |
|----------|----------|---------|
| **Critical** | App or system completely down; cannot work at all | SSO login broken for all users, Comms cannot send any messages |
| **High** | Major feature broken; significant work disruption | Cannot register clients, reports not loading, campaigns failing |
| **Medium** | Feature partially broken; workaround exists | Voice input not working (can type manually), analytics chart wrong |
| **Low** | Cosmetic issue or minor inconvenience | Button misaligned, text truncated, typo in label |

### Step 4: Submit

Send the incident report to the 2nd Line Support team through your established channel (email, ticket system, or Teams).

### Escalation Path

| Level | Team | What They Do |
|-------|------|-------------|
| **1st Line** | AI Support Assistant | Answer questions, provide guidance, identify known issues, suggest workarounds |
| **2nd Line** | Support / Operations / IT | Analyze and qualify incidents, fix configurations, correct data, escalate bugs |
| **3rd Line** | Development Team | Fix bugs, deploy patches, develop new features |

**Typical resolution times:**
- 1st Line (AI): Immediate
- 2nd Line: Same business day for Critical/High; 1-3 days for Medium/Low
- 3rd Line: Varies by complexity — days to weeks

---

## Glossary of Common Terms

| Term | Meaning |
|------|---------|
| **SSO** | Single Sign-On — one login for all apps |
| **Agency Portal** | The home dashboard of Sharp Matrix |
| **Client Connect** | App for registering and verifying clients |
| **Meeting Hub** | App for recording appointments |
| **Matrix Comms** | App for WhatsApp Business messaging |
| **SSO Console** | Admin tool for managing users and permissions |
| **Role** | Your job function in the system (e.g., Broker, Sales Manager, Admin) |
| **Scope** | How much data you can see (Self, Team, Global, Org Admin, System Admin) |
| **CRUD** | Create, Read, Update, Delete — the four types of data operations |
| **RFI** | Request for Information — asking a broker for more client details |
| **MLS** | Multiple Listing Service — the shared real estate database |
| **Pipeline Value** | Total value of active deals and reservations |
| **Template** | Pre-approved message format (used in WhatsApp) |
| **Campaign** | Bulk messaging to multiple contacts (via Comms) |
| **Quick Reply / Snippet** | Saved response text for fast messaging |
| **AI Advisor** | The AI chat assistant in the Agency Portal |
| **Act As** | Feature that lets admins switch to a different role for testing |
| **Tenant** | Organization in the system (Sharp Sotheby's International Realty) |
| **Edge Function** | Server-side code that processes requests (invisible to users) |
| **Webhook** | Automatic notification between systems (e.g., Twilio → Comms) |

---

## App-Specific Support Articles

For detailed support on each app, refer to the dedicated knowledge base articles:

| App | Support Article |
|-----|----------------|
| Agency Portal | `docs/zoe-ai-assistant-kb/portal.md` |
| Client Connect | `docs/zoe-ai-assistant-kb/client-connect.md` |
| Meeting Hub | `docs/zoe-ai-assistant-kb/meeting-hub.md` |
| Matrix Comms | `docs/zoe-ai-assistant-kb/comms.md` |
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
