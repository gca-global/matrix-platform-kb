# Sharp Matrix Agency Portal — 1st Line Support Knowledge Base

> **App name:** Matrix Agency Portal (Agency Hub)
> **URL:** [https://intranet.sharpsir.group/agency-portal/](https://intranet.sharpsir.group/agency-portal/)
> **Purpose:** Central dashboard and app launcher for all Sharp Matrix applications. Your starting point for daily work.
> **Users:** All Sharp Sotheby's staff — Agents, Brokers, Sales Managers, Contact Center, Staff, Admins.
> **Note:** This app uses a header-based layout (no sidebar). Navigation is through the top header bar, Quick Access bar, and app launcher cards.

---

## What Is the Agency Portal?

The Agency Portal is the home page of Sharp Matrix. It is a dashboard that gives you quick access to all your apps, shows your key performance numbers (pipeline value, client counts, meetings), your recent activity, and today's agenda. It also includes an AI Advisor you can chat with for quick answers and actions.

Think of it as your "control center" for the Sharp Matrix platform.

---

## How to Access the Agency Portal

1. Open your browser and go to [https://intranet.sharpsir.group/agency-portal/](https://intranet.sharpsir.group/agency-portal/).
2. You will be redirected to the Sharp Matrix SSO login page.
3. Sign in with your company email and password, or use "Sign in with Microsoft".
4. After login you land on the main Dashboard.

The Agency Portal is typically the first app you see after logging in.

---

## What You See on the Dashboard

### Stats Widgets (Top Row)

Four key metrics displayed at the top of the dashboard:

| Widget | What It Shows |
|--------|---------------|
| **Pipeline Value** | Total budget value (€M) from your contacts |
| **Approved Clients** | Number of clients with Approved status |
| **New Clients** | Number of clients registered this calendar month |
| **This Week** | Number of meetings this week (displayed as "N Meetings") |

These numbers update in near real-time based on your data in Client Connect and Meeting Hub.

### Applications

A grid of app cards in the center of the dashboard (section title: **Applications**). Click any card to open that app.

**Live app tiles** are loaded automatically based on your permissions. The apps you see depend on what has been set up by your Admin.

**Static "Coming Soon" tiles** are also displayed for planned features such as Listings & Pipeline, Calendar, Clients, Documents, Photography, Legal, Analytics, Finance, and Communications.

You can **reorder app cards** by dragging and dropping them to your preferred layout. Your order is saved automatically.

### Quick Access Bar

A shortcut bar fixed at the top of the screen (on desktop) or bottom (on mobile) with icons for frequently used apps. Click an icon to jump directly to that app.

To configure which apps appear in the Quick Access Bar:
1. On desktop: click the **⋯** (three dots) icon to open the **Customize Quick Access** popover. On mobile: tap the **More** button.
2. Toggle apps on or off.
3. Your selection is saved automatically.

### Recent Activity

Shows your most recent client registrations and appointments, pulling data from Client Connect and Meeting Hub.

### Today's Agenda

Shows meetings and appointments scheduled for today, so you can see your daily plan at a glance.

### AI Advisor

A floating button with a **Sparkles (✨)** icon (bottom-right corner) that opens an AI assistant panel.

**What you can ask the AI Advisor:**
- "What's my pipeline value?"
- "Show today's agenda"
- "Register new client John Smith"
- Any question about your clients, meetings, or pipeline

**How to use the AI Advisor:**
1. Click the floating Sparkles (✨) button.
2. Type your question or request, or use the microphone for voice input.
3. The AI responds with information or takes actions (e.g., opens a form, navigates to a page).
4. You can listen to responses using the text-to-speech button.

---

## Main Features

### Navigating Between Apps

From the dashboard, you can reach any Sharp Matrix app:

- **Click an app card** in the Applications section
- **Click a Quick Access icon** in the shortcut bar
- **Use the AI Advisor** — ask it to navigate you (e.g., "Open Client Connect")

All apps share the same login session (Single Sign-On). You do not need to log in again when switching between apps.

### Profile

1. Click your avatar or name in the top-right corner of the header.
2. Select **Profile**.
3. View your profile sections (displayed as cards, not tabs):
   - **Account Information** — name, email, role
   - **Permissions** — what pages and actions you can access
   - **Groups** — teams/groups you belong to (if any)

### App Permissions (Admin Only)

Admins can manage which roles can access which portal pages:

1. Navigate to `/admin/permissions` directly (this page is not in the user dropdown).
2. Select a role (Broker, Sales Manager, Contact Center).
3. Toggle page access on or off for each page.
4. Click **Save**.

### Role Switching (Act As)

If your Admin has enabled role switching for your account:

1. Click your avatar in the top-right corner.
2. You will see a role dropdown.
3. Select a different role to see the portal as that role would see it.
4. This is mainly used by Admins and managers for testing and support purposes.

### Accessing Admin Tools

All admin functions (User Management, Connected Apps, SSO Permissions, Groups, Settings) are accessed directly through the **SSO Management Console** at [https://intranet.sharpsir.group/sso-console/](https://intranet.sharpsir.group/sso-console/). The Agency Portal user dropdown no longer contains admin links.

The **App Permissions** page for the Portal is accessible at `/admin/permissions` via direct URL for administrators.

---

## Frequently Asked Questions

### General

**Q: What is the Agency Portal?**
A: It is your central dashboard in Sharp Matrix. It shows your key metrics, gives you access to all apps, and includes an AI Advisor for quick questions.

**Q: Why do I see different apps than my colleague?**
A: The apps you see depend on your role and permissions. Admins may have access to more apps than brokers. Contact your Admin if you believe an app is missing.

**Q: How do I rearrange the app tiles?**
A: Click and drag any app card to move it to a different position. Your layout is saved automatically.

**Q: How do I add apps to the Quick Access bar?**
A: Click the "More" button in the Quick Access bar and toggle on the apps you want.

### Stats and Data

**Q: Where do the dashboard numbers come from?**
A: Pipeline Value and Client counts come from Client Connect data. Meeting counts come from Meeting Hub data. Numbers update automatically.

**Q: The numbers look wrong or outdated.**
A: Try refreshing the page. If the numbers still seem incorrect, the underlying data may need correction in Client Connect or Meeting Hub. Contact your Admin or 2nd Line Support.

**Q: I don't see any stats or recent activity.**
A: You may not have any data yet, or your role may not have visibility to the data. Currently, stats are filtered by your own user ID — each user sees their own data.

### AI Advisor

**Q: What can the AI Advisor do?**
A: It can answer questions about your clients and meetings, show your pipeline, open forms, and navigate you to other apps. Think of it as a helpful assistant that knows your data.

**Q: The AI Advisor is not responding.**
A: Try refreshing the page. If you see "AI service is busy. Please wait.", wait a moment and try again. If the issue persists, use the apps directly — the AI Advisor is a convenience feature.

**Q: Can I use voice with the AI Advisor?**
A: Yes. Click the microphone icon, speak your question, and the AI will process it. You can also listen to responses with the speaker icon.

### Login

**Q: I logged in but see a blank dashboard.**
A: Your account may not have the dashboard permission enabled. Contact your Admin.

**Q: Why am I asked to log in again when I open the portal?**
A: Your session may have expired. This happens after a period of inactivity. Log in again — your data is not affected.

---

## Troubleshooting

### Login and Access

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in** | Wrong credentials or no account | Check email/password. Contact Admin or IT. |
| **Blank page after login** | No permissions assigned | Contact Admin to assign your role and page permissions. |
| **"You do not have access" error** | Role not authorized for this app | Contact Admin to verify your role assignment. |
| **Apps take long to load after clicking** | Network issue | Check your internet. Try clicking again. |

### Dashboard

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Stats show zero or "N/A"** | No data for your account, or data has not loaded | Refresh the page. If you have data in Client Connect/Meeting Hub, wait a moment for it to load. |
| **App cards are missing** | Admin has not enabled the app for your role, or the app is not registered | Contact Admin. |
| **Quick Access bar is empty** | No apps are toggled on | Click "More" in the bar and toggle on the apps you want. |
| **Recent Activity is empty** | No recent clients or meetings | This is normal if you haven't recorded any activity recently. |
| **Today's Agenda is empty** | No meetings scheduled for today | This is normal if you have no appointments today. |

### AI Advisor

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **"Not authenticated" message** | Session expired | Log in again. |
| **"AI service is busy. Please wait."** | Too many requests or service overload | Wait 10-15 seconds and try again. |
| **"Session expired"** | Your login session timed out | Refresh the page and log in again. |
| **Voice input not working** | Microphone permission denied | Allow microphone access in browser settings. |
| **"No speech detected"** | Microphone issue or silence | Check that your microphone is working. Speak louder. |
| **AI gives incorrect or irrelevant answer** | AI misunderstood the question | Rephrase your question. If the issue is consistent, report it. |

### Navigation

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Clicking an app opens a "Coming Soon" page** | Feature not yet built (Listings & Pipeline, Calendar, Clients, Documents, etc.) | These are planned features. Use the specific apps (Client Connect, Meeting Hub) instead. |
| **"Back to Dashboard" button not working** | Browser navigation issue | Click the logo in the header, or type the URL directly. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| Listings, Calendar, Clients, and Documents pages show "Coming Soon" | These features are under development. Use Client Connect for clients and Meeting Hub for calendar/appointments. | Planned |
| Some Quick Access shortcuts may not have matching pages | Clicking them leads to a 404 or blank page. Remove them from your Quick Access bar. | Known |
| Admin Permissions page only shows Broker, Sales Manager, and Contact Center — not Agent or Staff | To set permissions for Agent or Staff roles, use the SSO Console directly. | Planned fix |
| Stats currently show only your own data (filtered by your user ID) regardless of role | This is the current implementation. Contact Admin if team-wide stats are needed. | By design |
| App card order may reset after a system update | Re-arrange your cards after any major system update. | Rare |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team.

Report the issue using the standard incident template — see [How to Report an Incident](incident-reporting.md). Mention **Agency Portal** as the app name.

---

## Getting Started — Your First Day

### For Everyone (All Roles)

1. **Open the Portal** at [https://intranet.sharpsir.group/agency-portal/](https://intranet.sharpsir.group/agency-portal/) and log in.
2. **Explore the Dashboard** — look at your stat widgets (Pipeline Value, Approved Clients, New Clients, This Week).
3. **Open your main app** from the Applications section:
   - **Broker/Agent** → Click **Client Connect** to register clients, then **Meeting Hub** to record appointments.
   - **Contact Center** → Click **Client Connect** to verify incoming registrations.
   - **Sales Manager** → Click **Client Connect** to review flagged clients.
4. **Set up Quick Access** — click "More" in the Quick Access bar and toggle on the apps you use most. These appear as icons for one-click access.
5. **Rearrange app cards** — drag and drop app tiles to put your favorites first. The layout saves automatically.
6. **Try the AI Advisor** — click the Sparkles (✨) button (bottom-right) and ask "What's my pipeline value?" or "Show today's agenda."

### For Admins

1. After exploring the dashboard, head to the **SSO Console** at `/sso-console/` to manage users, permissions, and connected apps.
2. To manage portal-specific page permissions, navigate to `/admin/permissions` directly.
3. Remember: admin functions are in the **SSO Console**, not in the portal dropdown.

---

## Step-by-Step Workflows

### Workflow: Customize Your Dashboard Layout

1. **Rearrange app cards**: Click and hold any app card, drag it to a new position, release. Your order is saved.
2. **Set Quick Access shortcuts**: Click "More" in the Quick Access bar → toggle on your top 3–5 apps → click outside to close.
3. **Check your numbers**: the stat widgets pull data automatically from Client Connect and Meeting Hub. If they show zero, you may not have data yet.

### Workflow: Start Your Workday via the Portal

1. Open the Portal — review your **stats** at the top. Are your client counts growing? Any new meetings this week?
2. Check **Today's Agenda** (right panel) — see what meetings are scheduled.
3. Check **Recent Activity** — review last few client registrations and appointments.
4. Click into the app you need:
   - Have new clients to register? → **Client Connect**
   - Have appointments to record? → **Meeting Hub**
   - Need to check messages? → **Matrix Comms**
5. When done in any app, click **← Back to Dashboard** in the header to return to the Portal (or use the **Hub** link in the header from non-dashboard pages).

### Workflow: Use the AI Advisor for Quick Actions

1. Click the **Sparkles (✨) button** (bottom-right corner).
2. **Ask a question:**
   - "How many meetings did I have this week?"
   - "What is my pipeline value?"
   - "Show my upcoming appointments"
3. **Request an action:**
   - "Open Client Connect"
   - "Register a new client named Anna Smith, phone 99223344"
   - "Take me to Meeting Hub"
4. **Use voice:** Click the microphone icon, speak your question, and listen to the AI's response with the speaker icon.
5. Close the chat by clicking the X or clicking outside the panel.

---

## Tips and Best Practices

### Dashboard Tips

- **Start every workday here** — the Portal gives you a 30-second overview of your business. Check stats, review agenda, then dive into apps.
- **Refresh if numbers look stale** — a page refresh (F5 or pull-down on mobile) reloads all widgets with the latest data.
- **Pipeline Value** — this shows the total budget value (€M) from your contacts. If it drops, check Client Connect for changes.
- **Stats show your own data** — currently, all users see their own personal data on the dashboard.

### AI Advisor Power Tips

- **Be specific** — "Show today's meetings" is better than "Show meetings."
- **Use it for navigation** — saying "Open Meeting Hub" is faster than scrolling to find the app card.
- **Ask about data** — the AI can pull your pipeline numbers, client counts, and meeting totals without you opening another app.
- **Try follow-ups** — after asking "How many clients did I register this month?", you can ask "And how many were approved?"
- **Voice works in noisy environments** — speak clearly and close to the mic. Short sentences work best.
- **If the AI misunderstands**, rephrase with simpler words. For example, instead of "Show me my KPIs" try "What are my numbers?"

### Quick Access Bar Tips

- **Put your top 3 apps there** — Quick Access is for apps you open multiple times a day.
- **Remove unused shortcuts** — too many icons defeats the purpose. Keep it focused.
- **The bar persists** — your selection is saved and appears every time you log in.

### For Managers and Admins

- **Use the Portal as your daily status view** — check your stats, recent activity, and today's agenda at a glance.
- **Bookmark the SSO Console** — admin functions like user management and permissions are accessed from `/sso-console/`, not from the Portal dropdown.
- **Check the Portal once a day** — even if you spend most of your time in Client Connect or Meeting Hub, a quick Portal check gives you the big picture.

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| See your dashboard | Open Agency Portal (home page) |
| Open an app | Click its card on the dashboard |
| Configure Quick Access shortcuts | Quick Access bar → More |
| Rearrange app tiles | Drag and drop on the dashboard |
| Check today's agenda | Right panel on the dashboard |
| Check recent activity | Dashboard → Recent Activity section |
| Ask the AI Advisor | Click the Sparkles (✨) button (bottom-right) |
| Use voice with AI Advisor | AI Advisor panel → Microphone icon |
| View your profile | Top-right avatar → Profile |
| Manage permissions (Admin) | Navigate to `/admin/permissions` directly |
| Manage users (Admin) | SSO Console (`/sso-console/users`) |
| Manage connected apps (Admin) | SSO Console (`/sso-console/apps`) |
| Switch role (Act As) | Top-right avatar → Role dropdown |
| Sign out | Top-right avatar → Sign Out |
