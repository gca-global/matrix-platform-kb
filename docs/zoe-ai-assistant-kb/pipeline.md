# Sharp Matrix Pipeline — 1st Line Support Knowledge Base

> **App name:** Matrix Pipeline
> **URL:** `https://intranet.sharpsir.group/matrix-pipeline/`
> **Purpose:** Manage sales leads, deal pipeline, contacts, MLS property data, Microsoft 365 email/calendar, opportunity reviews, and call center workflows.
> **Users:** Brokers, Sales Managers, Call Center Staff, Admins

---

## What Is Matrix Pipeline?

Matrix Pipeline is the CRM and sales pipeline management app for Sharp Sotheby's International Realty. It is the central tool for managing leads (incoming prospects), opportunities (active deals in the pipeline), contacts (clients and business relationships), and MLS property data. It integrates with Microsoft 365 for email and calendar, supports AI-assisted data entry, and includes a call center module for contact verification. Managers use it for deal reviews and pipeline analytics.

---

## How to Access Matrix Pipeline

1. Open your browser and go to `https://intranet.sharpsir.group/matrix-pipeline/`.
2. You will be redirected to the Sharp Matrix SSO login page.
3. Sign in with your company email and password, or use "Sign in with Microsoft".
4. After login you land on the **Dashboard**.

If you cannot log in, your account may not have access to Matrix Pipeline. Contact your Admin or IT department.

---

## User Roles and What They Can Do

| Role | Home Page | What They Can Do |
|------|-----------|-----------------|
| **Broker** | Dashboard | Manage own leads, opportunities, contacts, emails, and calendar |
| **Sales Manager** | Dashboard | All broker capabilities plus: view team pipeline, conduct deal reviews, manage assignments |
| **Call Center Staff** | Call Center Dashboard | Contact verification, MLS duplicate checking, lead processing |
| **Admin** | Dashboard | Full access: all capabilities plus settings, permissions, integrations, MLS config |

---

## Main Features

### Dashboard

Your personal landing page showing:
- **Stat cards** — Pipeline Budget, Expected Commission, New Leads, Pending Tasks (with overdue count)
- **Pipeline Overview** — deal counts per stage in a visual breakdown
- **Your Progress (7 days)** — chart showing Opportunities Created, Opportunities Moved, and Tasks Done
- **Revenue Forecast (Weighted)** — weighted deal value forecast chart
- **Recent Leads** — latest leads with status
- **Upcoming Tasks** — tasks due soon

Call Center staff see a dedicated **Call Center Dashboard** instead, focused on the verification queue.

The system remembers which page you visited last and returns you there on next login.

### Leads

Capture and manage incoming prospects.

1. Click **Leads** in the sidebar.
2. View all leads with filters for status, source, and date.
3. To create a new lead:
   - Click **New Lead**.
   - Fill in: first name, last name, email, phone, source (Website, Referral, Walk-in, Social Media, Advertising, Partner, Event, Cold Call, Other), property interest, and notes.
   - Save the lead.
4. Lead statuses: **New**, **Contacted**, **Converted**, **Disqualified**.
5. **Convert** a qualified lead into an opportunity — click **Convert**, enter a deal name, and the system creates a pipeline opportunity linked to this lead.

### Pipeline (Opportunities)

Manage active deals through pipeline stages.

1. Click **Pipeline** in the sidebar.
2. View opportunities on a **Kanban board** with drag-and-drop between stage columns.
3. Click any opportunity to see full details:
   - **Contacts** — linked clients and their roles
   - **Properties** — MLS listings connected to this deal
   - **Tasks** — action items and follow-ups
   - **Timeline** — activity history
   - **Emails** — linked email conversations (from Microsoft 365)
   - **Documents** — attached files
4. To create a new opportunity:
   - Click **New Opportunity** (or create from a contact's detail page using **New Deal**).
   - Fill in: deal name, stage, deal type (Buy or Rent), deal value, expected commission, expected close date, currency, location, property type, and notes.
   - Link contacts and properties.
5. **Move** an opportunity to the next stage by dragging the card on the Kanban board.
6. **Mark Won** or **Mark Lost** to close a deal.
7. Deals can also be **disqualified** (e.g., when a linked contact is rejected during review).

**Voice input:** You can use the voice input feature to dictate opportunity details. The system transcribes your speech (supports English, Russian, German, Greek) and uses AI to fill in form fields automatically.

### Opportunity Reviews

Review opportunities linked to rejected contacts.

1. Click **Opportunity Reviews** in the sidebar.
2. View opportunities with `review_status = pending_review` — these are deals linked to contacts that were rejected during call center verification.
3. For each deal, you can **revoke** (disqualify the opportunity) or **reassign** it to the correct broker.
4. The sidebar badge shows the count of pending reviews.

### Contacts

Manage client and business contact records.

1. Click **Contacts** in the sidebar.
2. Search, filter, and browse all contacts.
3. Click any contact to view their profile, linked opportunities, and relationship history.
4. Add a new contact with the **New Contact** button. Contact types: Buyer, Seller, Investor, Tenant, Landlord, Agent, Referral Agent, Developer, Other.
5. Fill in: first name, last name, email, phone, contact type, company name, city, country.
6. The system checks for duplicates when creating a contact.
7. Contacts can be linked to multiple opportunities. You can also create a new deal directly from a contact's detail page.
8. Contacts cannot be deleted while they are linked to existing opportunities.

### Email (Microsoft 365)

Access your Microsoft 365 email within Matrix Pipeline.

1. Click **Email** in the sidebar.
2. View your email inbox (requires Microsoft 365 connection).
3. **Link emails to opportunities** — attach relevant email threads to deals for context.
4. Compose and reply to emails directly.

**First-time setup:** You need to connect your Microsoft 365 account in Settings → Microsoft 365.

### Calendar (Microsoft 365)

View and manage your calendar.

1. Click **Calendar** in the sidebar.
2. View appointments, meetings, and scheduled events.
3. Create new calendar events linked to opportunities or contacts.

**First-time setup:** Requires Microsoft 365 connection (same as Email — Settings → Microsoft 365).

### MLS Data

Browse MLS property listings and related real estate data.

1. Click **MLS Data** in the sidebar. The page title is **MLS Data Explorer**.
2. Browse data across multiple tabs: **Properties**, **Members**, **Offices**, **Contacts**, **Media**, **Showings**, **Open Houses**, **History**, **Tracking**.
3. Search and filter property listings from the MLS database.
4. View property details, photos, and listing information.
5. Link properties to opportunities in the pipeline.

### Notifications

View all your notifications.

1. Click **Notifications** in the sidebar (or the bell icon in the header).
2. See updates about your leads, opportunities, reviews, and reminders.
3. The sidebar badge shows unread notification count.

### Call Center

For call center staff: verify contacts and process leads.

1. Click **Call Center** in the sidebar (visible to call center roles).
2. View the verification queue — contacts pending verification.
3. **Approve** or **reject** contacts after checking for MLS duplicates.
4. Process incoming leads and route them to brokers.

### Shared Property Lists (Public)

Create and share curated property lists with clients.

- Shared lists are accessible via a unique link (no login required for the recipient).
- Clients can browse selected properties and view details.
- Share events are logged for analytics.

### Settings (Admin)

Admins can configure:

- **General** — app-wide settings (theme, language)
- **Permissions** — role-based page and action access
- **Data Model** — data model configuration
- **Data Layer** — data source configuration
- **Pipeline** — pipeline stage configuration (add, rename, reorder stages)
- **Leads Integration** — set up automatic lead import from external sources (e.g., website forms)
- **Microsoft 365** — Microsoft 365 integration (connect/disconnect email and calendar)
- **MLS** — MLS connection settings and sync
- **Matching** — property matching settings
- **AI Providers** — AI and semantic search settings
- **Agency Hub URL** — return URL for the Back to Agency Hub link
- **Google Maps** — Google Maps integration settings

---

## Use Cases: Real-World Pipeline Scenarios

### Scenario 1: New Buyer Lead Arrives from Website
A potential buyer fills out a form on the Sharp SIR website. The lead arrives automatically in Matrix Pipeline.
1. The lead appears in your **Leads** list with source "Website."
2. Open the lead, review the details (name, email, phone, property interest).
3. Qualify the lead: Is the budget realistic? Is the timeline serious?
4. If qualified, click **Convert** to create a pipeline opportunity.
5. Link relevant MLS properties to the new opportunity.
6. Set the first follow-up task (e.g., "Call to discuss property preferences").

### Scenario 2: Managing a Deal Through the Pipeline
You have a buyer interested in a luxury apartment in Limassol.
1. The opportunity is in the **Qualification** stage.
2. After confirming the client's budget and preferences, move the card to **Matching** on the Kanban board.
3. Link MLS properties that match the client's criteria.
4. Schedule viewings and move to the **Viewing** stage.
5. After a successful viewing, attach the property proposal email by linking it from your M365 inbox.
6. Once terms are agreed, move to **Contracting**. Upload the signed agreement as a document.
7. After payment is processed, move to **Payment** and then mark the deal as **Won**.

### Scenario 3: Manager Reviews Pipeline Health
A Sales Manager reviews the team's pipeline weekly.
1. Open **Pipeline** to see the Kanban board — how many deals in each stage?
2. Check **Opportunity Reviews** for deals flagged by brokers.
3. Look for deals stuck in one stage too long — these may need intervention.
4. Check deal values to forecast monthly revenue.
5. Export the pipeline data for the leadership meeting.

### Scenario 4: Call Center Verifies New Contacts
A new contact arrives for verification.
1. Open **Call Center** to see the verification queue.
2. Review the contact details — name, phone, email.
3. Run **MLS Duplicate Check** to see if this person already exists.
4. If duplicate found → reject with reason. If clean → approve.
5. The approved contact is now available for pipeline opportunities.

### Scenario 5: Sharing a Property List with a Client
You want to send a curated list of properties to a buyer.
1. Select the properties you want to include.
2. Generate a **Shared Property List** — this creates a unique public link.
3. Send the link to your client via email or WhatsApp.
4. The client can browse the properties without logging in.
5. You can see analytics on which properties they viewed.

---

## Best Practices for Pipeline Management

### Lead Management
- **Respond to new leads within 1 hour** — speed is critical in luxury real estate. The first broker to respond often wins.
- **Qualify before converting** — don't create opportunities for every lead. Ask about budget, timeline, and motivation.
- **Record the lead source** — knowing where leads come from helps marketing allocate budget.
- **Don't delete leads** — even if unqualified now, they may come back. Mark as lost with a reason instead.

### Deal Management
- **Update deal stages promptly** — your Kanban board should reflect reality. Don't leave deals in old stages.
- **Link all relevant contacts** — every deal should have the buyer, seller, and any agents linked.
- **Attach emails to deals** — link every important email conversation to the opportunity. This creates an audit trail.
- **Use tasks for follow-ups** — create tasks with due dates so nothing falls through the cracks.
- **Add property links** — connect MLS properties to opportunities so you can track which properties are part of each deal.

### Data Quality
- **One contact per person** — always search before creating a new contact. Use the duplicate check.
- **Keep contact details current** — update phone numbers, emails, and addresses when they change.
- **Record important dates** — birthdays and anniversaries in contact records help build relationships.
- **Fill in deal values** — estimated deal value is critical for pipeline forecasting and revenue reporting.

### For Managers
- **Review the pipeline weekly** — look at stage distribution, stuck deals, and total pipeline value.
- **Flag deals for review** — use Opportunity Reviews to manage deals that need team discussion.
- **Track conversion rates** — how many leads convert to opportunities? How many opportunities close as won?
- **Use analytics for coaching** — identify brokers who need help and provide targeted support.

---

## Pipeline Stages

Opportunities progress through stages. Stages can be customized by your admin in Settings → Pipeline, but the default stages are:

| Stage | What It Means |
|-------|---------------|
| **Qualification** | Evaluating if the deal is viable — confirming budget, timeline, and client motivation |
| **Matching** | Finding suitable properties for the client based on their criteria |
| **Viewing** | Client is viewing properties — scheduling and conducting showings |
| **Contracting** | Terms agreed, contracts being prepared and signed |
| **Payment** | Payments being processed, deal approaching completion |

After the final stage, the deal is marked as **Won** (successfully closed) or **Lost** (did not proceed).

## Deal Statuses

| Status | Meaning |
|--------|---------|
| **Active** | Deal is in progress, moving through pipeline stages |
| **Won** | Deal successfully closed |
| **Lost** | Deal did not proceed (reason is recorded) |
| **Disqualified** | Deal removed from active pipeline (e.g., linked contact was rejected) |

---

## Deal Actions

| Action | What It Does |
|--------|-------------|
| **Create** | Start a new opportunity (from Pipeline page or from a Contact's detail page) |
| **Edit** | Update deal details — name, value, stage, contacts, properties, notes |
| **Move Stage** | Drag the card on the Kanban board to advance or revert to a different stage |
| **Mark Won** | Close the deal as successfully completed |
| **Mark Lost** | Close the deal as unsuccessful (enter a lost reason) |
| **Convert (from lead)** | Turn a qualified lead into a pipeline opportunity — enter a deal name and the system creates the opportunity |

---

## Languages

Matrix Pipeline supports two interface languages:
- **English**
- **Russian**

To switch language, click the language toggle (globe icon) in the sidebar footer.

---

## Frequently Asked Questions

### General

**Q: What is Matrix Pipeline?**
A: It is the CRM and sales pipeline app for Sharp SIR. It helps you manage leads, deals, contacts, and property data.

**Q: What is the difference between a lead and an opportunity?**
A: A lead is an incoming prospect that has not been qualified yet. An opportunity is a qualified deal actively being worked through the pipeline stages.

**Q: Can I see other brokers' deals?**
A: It depends on your role and scope. Brokers typically see only their own deals. Sales Managers can see their team's deals. Admins can see all deals.

### Leads

**Q: How do I create a lead?**
A: Go to Leads → click New Lead → fill in the details → Save.

**Q: How do I convert a lead to an opportunity?**
A: Open the lead and click Convert. This creates a new opportunity in the pipeline linked to the lead's contact.

**Q: Where do leads come from?**
A: Leads can be created manually, or they arrive automatically from external sources (like the company website) configured by your Admin.

### Pipeline

**Q: How do I move a deal to the next stage?**
A: In the Kanban view, drag the card to the next column. Or open the deal and change the stage using the dropdown.

**Q: What happens when I mark a deal as Won?**
A: The deal moves to the Won column and is no longer in the active pipeline. It is counted in your closed deals statistics.

**Q: Can I reopen a lost or disqualified deal?**
A: Contact your manager or admin. They may be able to revert the status.

**Q: What is a deal review?**
A: Managers can flag deals for review. The Opportunity Reviews page shows deals that need management attention.

### Contacts

**Q: How do I link a contact to a deal?**
A: Open the opportunity and add a contact in the Contacts section.

**Q: Can one contact be linked to multiple deals?**
A: Yes. A client can be involved in multiple opportunities.

### Email and Calendar

**Q: I don't see my emails. What's wrong?**
A: You need to connect your Microsoft 365 account first. Go to Settings → Microsoft 365 and connect your account.

**Q: How do I link an email to a deal?**
A: Open the email and use the Link to Opportunity option to attach it to a deal.

### MLS Data

**Q: What is MLS Data?**
A: MLS Data shows property listings from the Multiple Listing Service. You can browse properties and link them to your pipeline opportunities.

**Q: MLS data seems outdated.**
A: MLS data is synced periodically. Check with your admin about the sync schedule.

---

## Troubleshooting

### Login and Access

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in** | Wrong credentials or no account | Check email/password. Contact Admin. |
| **"Page Not Available" on a page** | Your role doesn't have permission | Contact Admin to check role and permissions. |
| **Session expired** | Your login session timed out | Log in again. This is normal after inactivity. |

### Pipeline and Deals

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot create an opportunity** | Missing required fields or no permission | Fill in all required fields. Check with Admin if you lack the create action. |
| **Cannot move a deal to next stage** | Missing required fields for that stage | Open the deal and complete all required fields before advancing. |
| **Deal disappeared from Kanban** | Filtered out, won/lost, or deleted | Check your filters. Look in the Won/Lost/All views. |
| **Opportunity review badge count seems wrong** | Data refresh delay | Refresh the page. |

### Contacts

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Duplicate contact found** | Same person entered multiple times | Contact your admin to merge duplicates. |
| **Cannot edit a contact** | Insufficient permissions | Check your role's edit permissions. |

### Email and Calendar

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Microsoft 365 not connected** | Account not linked | Go to Settings → Microsoft 365 → Connect your account. |
| **Emails not loading** | Your Microsoft connection may need to be refreshed | Disconnect and reconnect your Microsoft account in Settings → Microsoft 365. |
| **Calendar events not syncing** | Sync delay or connection issue | Refresh the page. If persistent, reconnect in Settings → Microsoft 365. |

### MLS Data

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **MLS Data page is empty** | MLS sync not configured or no data | Contact Admin to verify MLS settings. |
| **MLS sync failed** | Connection or credentials issue | Admin should check MLS settings. |
| **Property data seems outdated** | Sync interval not reached | Wait for the next sync cycle or ask Admin to trigger a manual sync. |

### Call Center

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Verification queue is empty** | No pending contacts | This is normal when all contacts have been processed. |
| **MLS duplicate check failed** | MLS connection issue | Contact Admin to check MLS integration settings. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| Sidebar title may show "Matrix Apps Template" instead of "Matrix Pipeline" | This is a cosmetic issue. The app functions correctly. | Known |
| Some sidebar badge counts may show placeholder values | Navigate to the actual page to see real data counts. | Known |
| Shared property list links are intentionally public (no login required) | This is by design for client convenience. Do not share links containing sensitive information. | By design |
| Full UI translation to Russian is partial | Key features are translated; some labels may appear in English. | In progress |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team.

Report the issue using the standard incident template — see [How to Report an Incident](incident-reporting.md). Mention **Matrix Pipeline** as the app name and include the **opportunity ID** or **contact name** if relevant.

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| View dashboard | Sidebar → Dashboard |
| View notifications | Sidebar → Notifications (or bell icon in header) |
| Manage leads | Sidebar → Leads |
| View deal pipeline (Kanban) | Sidebar → Pipeline |
| Create a new opportunity | Sidebar → Pipeline → New Opportunity |
| Review deals (manager) | Sidebar → Opportunity Reviews |
| Manage contacts | Sidebar → Contacts |
| Access email (M365) | Sidebar → Email |
| View calendar (M365) | Sidebar → Calendar |
| Browse MLS properties | Sidebar → MLS Data |
| Process call center queue | Sidebar → Call Center |
| Configure settings (admin) | Sidebar → Settings |
| View my profile | Header → Avatar → Profile |
| Switch language | Sidebar footer → Globe icon |
| Switch theme (light/dark) | Sidebar footer → Theme toggle |
| Return to Agency Hub | Sidebar footer → Back to Agency Hub |
