# Sharp Matrix Meeting Hub — 1st Line Support Knowledge Base

> **App name:** Meeting Hub (Appointment Reports)
> **URL:** `https://intranet.sharpsir.group/meeting-hub/`
> **Purpose:** Record, manage, and analyze buyer, seller, tenant, and landlord appointments.
> **Users:** Brokers/Agents, Sales Managers (Office Managers), Contact Center (MLS Staff), Admins.

---

## What Is Meeting Hub?

Meeting Hub is the appointment reporting app for Sharp Sotheby's International Realty. Brokers use it to record every client meeting — whether showing a property to a buyer, meeting a seller, showing a rental to a tenant, or meeting a landlord. The app tracks details like properties viewed, budgets, client questionnaires, and outcomes. Sales Managers and Admins can view analytics, build reports, and track team performance.

---

## How to Access Meeting Hub

1. Open your browser and go to `https://intranet.sharpsir.group/meeting-hub/`.
2. You will be redirected to the Sharp Matrix SSO login page.
3. Sign in with your company email and password, or use "Sign in with Microsoft".
4. After login you land on your role-specific home page (Dashboard or Broker Dashboard).

If you cannot log in, your account may not have access to Meeting Hub. Contact your manager or IT department.

---

## User Roles and What They Can Do

| Role | Home Page | What They Can Do |
|------|-----------|-----------------|
| **Broker / Agent** | Dashboard | Create and edit their own appointments, view own stats and counts |
| **Sales Manager (Office Manager)** | Dashboard | View all team appointments and aggregate counts, analytics, build reports |
| **Contact Center (MLS Staff)** | Dashboard | View all appointments and aggregate counts, analytics |
| **Admin** | Dashboard | Full access: permissions, settings, all appointments across all brokers |

---

## Appointment Types

Meeting Hub supports four types of appointments:

| Type | Icon | Description |
|------|------|-------------|
| **Buyer Appointment** | Blue | Showing properties to a potential buyer. Includes listings viewed, developers, projects, budget, reservation status. |
| **Seller Appointment** | Green | Meeting with a property owner/seller. Includes price (EUR), city, property type. |
| **Tenant Appointment** | Orange | Showing rental properties to a potential tenant. Includes monthly rent. |
| **Landlord Appointment** | Purple | Meeting with a property owner for rental. Includes monthly rent. |

---

## Main Features

### Creating an Appointment

1. Click **New Appointment** (or navigate to Sidebar → All Appointments → New).
2. Select the appointment type: Buyer, Seller, Tenant, or Landlord.
3. Fill in the form:
   - **Date and time** of the appointment
   - **Client name** (type to search existing clients, or add new)
   - **Outcome** (free-text description of the meeting result)
   - Type-specific fields (see below)
   - **Client Questionnaire** (buyer appointments only — see below)
   - **Notes** — any interesting details
4. Click **Submit Report**.

#### Buyer Showing Fields
- **Budget range** (from–to, currency)
- **Listings viewed** (search and add properties shown)
- **Developers visited** (add developer names)
- **Projects viewed** (add project names under each developer)
- **Reservation** — was a property reserved? (Yes/No, contract value)
- **Outcome** — result of the showing

#### Seller Appointment Fields
- **Price (EUR)** — the asking price (currency is fixed to EUR in the form)
- **City**
- **Property type**

#### Tenant Appointment Fields
- **Monthly rent** — a single rent amount (not a from–to range)

#### Landlord Appointment Fields
- **Monthly rent** — expected monthly rental income

#### Client Questionnaire (Buyer Appointments Only)
The questionnaire is only shown for buyer appointments. It includes:
- Is this the client's first appointment?
- Country of origin
- Country of residence
- Occupation
- Family status
- Reason to buy — options: Cyprus Permanent Residency Investment, Holiday home, Relocation, Education for children, Tax residency, Other

### Voice Input (AI Form Fill)

You can dictate appointment details instead of typing:

1. Click the **microphone icon** on the form.
2. Speak the appointment details (date, client, properties, budget, etc.).
3. The AI processes your speech and fills the form fields.
4. Review the auto-filled fields and correct any mistakes.
5. Save.

Supported languages: English, Russian, and other languages if enabled by Admin.

### Editing an Appointment

1. Go to **All Appointments** in the sidebar.
2. Find the appointment (use search, filters, or tabs).
3. Click the appointment to open it.
4. Click **Edit**.
5. Make your changes and click **Update Report**.

### Deleting an Appointment

1. Find the appointment in the list.
2. Click the delete icon/button.
3. Confirm the deletion.

**Note:** Deleted appointments cannot be recovered. Only delete if you are certain.

### Viewing All Appointments

1. Go to **All Appointments** in the sidebar.
2. Use the tabs to filter by type: Buyer, Seller, Tenant, Landlord.
3. Use the search bar to find specific appointments by client name.
4. Sort by date, client, or type.
5. Click any appointment to view its full details.

### Analytics

1. Go to **Analytics** in the sidebar (available to Managers and Admins).
2. Select a date range preset: Last 7 days, Last 30 days, Last 90 days, or Last year.
3. View stat cards: **Total Appointments**, **Reservations**, **Reservation Rate**, **Avg Budget**.
4. View charts:
   - **Appointments by Broker** — horizontal stacked bar chart showing each broker's name (in "First L." format, e.g., "Nadejda S.") with breakdown by appointment type
   - **Property Types** — pie chart of property type distribution
   - **Appointments Over Time** — line chart showing daily/weekly trends
   - **Top Cities** — bar chart for seller, tenant, and landlord activity by city

### Reports

Meeting Hub includes a powerful Report Builder:

1. Go to **Reports** in the sidebar (available to Managers and Admins).
2. Choose a report template:
   - **Weekly Appointment Summary** — quick overview of this week's activity
   - **Monthly Overview** — month-over-month comparison
   - **Broker Performance** — compare brokers side by side
   - **Budget Analysis** — budget distribution across buyer showings
   - **City/Location Report** — activity by city
   - **Reservation Report** — reservation tracking and values
   - **Property Type Analysis** — breakdown by property type
   - **Developer Report** — developer and project activity
   - **Conversion Funnel** — lead-to-appointment conversion tracking
   - **Outcome Analysis** — success rates and follow-up needs
3. Configure filters (date range, broker, type).
4. View the report.
5. **Export to Excel** if needed.
6. **Save the report** for future reference or sharing.

#### AI Report Assistant

1. In the Report Builder, click **AI Assistant**.
2. Describe the report you want in plain language (e.g., "Show me buyer showings this month with budgets over $500,000").
3. The AI configures the report for you.
4. Review and adjust if needed.

### Dashboard

The main Dashboard shows:

- **Your appointment counts** — Buyer, Seller, Tenant, and Landlord counts for your own appointments (Managers and Admins see totals across all brokers)
- **This Week** — number of your appointments scheduled this week
- **Reserved** — number of buyer appointments where a property was reserved
- **Recent appointments** — your latest recorded meetings
- **Manager Tools** — buttons to access Analytics Dashboard and Report Builder (visible to Managers and Admins only)

---

## Frequently Asked Questions

### General

**Q: What is Meeting Hub?**
A: Meeting Hub is the Sharp Matrix app for recording and managing real-estate appointments — buyer showings, seller meetings, tenant showings, and landlord meetings.

**Q: Who should use Meeting Hub?**
A: Every broker/agent should record their client meetings here. Sales Managers and Admins use it to track team performance and build reports.

**Q: Is Meeting Hub connected to Client Connect?**
A: Both apps share the same client information. Clients registered in Client Connect appear as searchable contacts in Meeting Hub.

### Appointments

**Q: How do I record a meeting?**
A: Click New Appointment, choose the type (Buyer/Seller/Tenant/Landlord), fill in the details, and click Submit Report.

**Q: Can I edit an appointment after saving?**
A: Yes. Go to All Appointments, find it, click Edit, make changes, and click Update Report.

**Q: Can I delete an appointment?**
A: Yes, but be careful — deleted appointments cannot be recovered.

**Q: What is the Client Questionnaire?**
A: A section on buyer appointment forms where you record client background information: country of origin, residence, occupation, family status, and reason to buy. This data helps with analytics and marketing. The questionnaire is shown for buyer appointments only.

**Q: What does "Reservation" mean in a Buyer Showing?**
A: It indicates whether the client reserved (put a hold on) a property during the showing. If yes, you can also record the contract value.

### Voice Input

**Q: How do I use voice input?**
A: Click the microphone icon on the form, speak your meeting details, and the AI fills in the fields. Always review before saving.

**Q: Voice input filled in the wrong data. What should I do?**
A: Manually correct the fields. Voice input is AI-powered and may occasionally misinterpret details, especially unusual names or numbers.

### Reports

**Q: Can I export reports to Excel?**
A: Yes. In the Report Builder, click the Export button to download an Excel file.

**Q: Can I save and share reports?**
A: Yes. Click Save in the Report Builder. Saved reports can be viewed later from the Reports page. Sharing options depend on your admin configuration.

**Q: What is the AI Report Assistant?**
A: It lets you describe a report in plain language, and the AI configures the filters and layout for you.

---

## Troubleshooting

### Login and Access

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in** | Wrong credentials or no account | Check email/password. Contact Admin if you don't have an account. |
| **"Access Denied" on a page** | Your role doesn't have permission | Contact Admin to check your role and page permissions. |
| **Page loads forever** | Network or session issue | Refresh the page. Log out and log back in if needed. |

### Appointment Forms

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot save appointment — validation error** | Required fields are missing | Check that date/time and client name are filled in. |
| **Client name not found in search** | Client not yet registered | Type the name manually. The client can be registered in Client Connect later. |
| **Listings/developers not showing in autocomplete** | Data not yet loaded or list is empty | Type a few characters and wait. If still empty, the listing or developer list may need updating — contact your Admin. |
| **Voice input not working** | Microphone permission denied | Allow microphone access in your browser settings. |
| **Voice input filled wrong fields** | AI misinterpretation | Correct the fields manually. Speak more clearly next time, including explicit labels like "client name is..." or "budget is...". |
| **Form resets after navigating away** | Unsaved changes are lost | Always click Submit Report before leaving the form page. |

### Analytics and Reports

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Analytics show no data** | Date range filter too narrow, or no appointments recorded | Widen the date range. Confirm that appointments exist for the selected period. |
| **Report builder is slow** | Large data set | Try narrowing the date range or filtering by broker/type. |
| **Excel export is empty** | Report has no data for the selected filters | Verify the report shows data on screen before exporting. |
| **AI Report Assistant gives wrong configuration** | AI misunderstood the request | Rephrase your request or manually adjust the filters. |

### Data Issues

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Dashboard counts seem too high** | You may be a Manager/Admin seeing all brokers' data | Managers and Admins see aggregate totals across all brokers. Brokers and Agents see only their own counts. This is by design. |
| **Appointment data looks wrong** | Incorrect data entry or system error | Open the appointment and check the details. If the data was entered incorrectly, edit it. If it seems like a system error, report to your IT department. |
| **Duplicate appointments** | Accidental double-save | Delete the duplicate. If the same client was entered twice, keep the most complete record. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| Voice parsing depends on AI service availability | If voice input fails, enter data manually. Try again later. | Dependency on external AI |
| Developers/Projects naming can be confusing (listings vs developer projects) | "Listings Viewed" = properties shown; "Developers Viewed" and "Projects Viewed" = developer names and their specific projects | Naming |
| Broker Dashboard page key not in default role permissions | Admin must explicitly enable the `broker-dashboard` page permission if access is needed | Configuration |
| Multi-language input toggle may change keyboard behavior | If your input language settings seem wrong, ask Admin to check Settings → Input Language | Configuration |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team.

Report the issue using the standard incident template — see [How to Report an Incident](incident-reporting.md). Mention **Meeting Hub** as the app name and include the **Appointment ID** if the issue is about a specific appointment.

---

## Getting Started by Role

### New Broker — Your First Day

1. **Log in** at `https://intranet.sharpsir.group/meeting-hub/` using your company credentials.
2. You land on the **Dashboard** — it shows your appointment counts, this week's total, and recent meetings.
3. Click **New Appointment** (top-right button).
4. Select the type: **Buyer**, **Seller**, **Tenant**, or **Landlord**.
5. Fill in the date, client name, and type-specific fields (budget, listings, rent, etc.).
6. Optionally complete the **Client Questionnaire** — this helps analytics.
7. Click **Submit Report**.
8. Your appointment appears in **All Appointments** and your Dashboard counts update immediately.

**Tip:** Register the client first in **Client Connect** — then their name will auto-complete when you type it in Meeting Hub.

### Manager / Admin — Your First Day

1. **Log in** — you land on the **Dashboard** showing aggregate counts across all brokers.
2. Check **Analytics** (sidebar) to see team performance: appointments by broker, trends over time, top cities.
3. Use **Reports** (sidebar) to build weekly or monthly summaries. Start with the "Weekly Summary" template.
4. **Export to Excel** from any report for offline review or sharing.

**Tip:** The "Appointments by Broker" chart on Analytics shows each broker's name and their appointment breakdown. Use it in team meetings to review performance.

---

## Step-by-Step Workflows

### Workflow: Record a Buyer Showing

1. Click **New Appointment** → select **Buyer**.
2. Enter the **appointment date and time**.
3. Type the **client name** — select from suggestions or type a new name.
4. Set the **budget range** (from–to). You can type exact amounts; the slider adjusts visually but doesn't change what you typed.
5. Add **listings viewed** — search by name and add each property you showed.
6. Add **developers visited** and **projects** if applicable.
7. Set **Reservation**: Yes/No. If Yes, enter the contract value.
8. Write an **outcome** — this is a free-text field where you describe the result (e.g., "Client interested in sea view apartments, wants second viewing next week").
9. Fill in the **Client Questionnaire** (buyer appointments only).
10. Add any **notes** about the meeting.
11. Click **Submit Report**.

### Workflow: Record a Seller Meeting

1. Click **New Appointment** → select **Seller**.
2. Enter the **date and time**.
3. Enter the **seller/owner name**.
4. Enter the **Price (EUR)** — the asking price.
5. Select the **city** and **property type**.
6. Write an **outcome** (free text).
7. Add notes.
8. Click **Submit Report**.

### Workflow: Record a Tenant or Landlord Meeting

1. Click **New Appointment** → select **Tenant** or **Landlord**.
2. Enter the **date and time** and **client name**.
3. For Tenants: enter the **monthly rent** amount.
4. For Landlords: enter the **monthly rent** amount.
5. Write an outcome (free text) and add notes.
6. Click **Submit Report**.

### Workflow: Use Voice Input for Appointments

1. Open the appointment form (any type).
2. Click the **microphone icon** next to a field or at the top of the form.
3. Speak naturally. Example for a buyer showing: *"Meeting with John Smith today at 2pm, showed three apartments in Limassol, budget 300 to 500 thousand euros, he liked the sea view apartment, wants to schedule a second viewing."*
4. The AI fills the form fields — **review carefully**.
5. Correct any errors (especially names, numbers, and dates).
6. Click **Submit Report**.

### Workflow: Build a Report (Managers/Admins)

1. Go to **Reports** in the sidebar.
2. Select a template (10 templates available):
   - **Weekly Appointment Summary** — quick overview of this week's activity
   - **Monthly Overview** — month-over-month comparison
   - **Broker Performance** — compare brokers side by side
   - **City/Location Report** — activity by city
   - **Property Type Analysis** — breakdown by property type
   - **Outcome Analysis** — success rates and follow-up needs
   - **Budget Analysis** — budget distribution across buyer showings
   - **Reservation Report** — reservation tracking and values
   - **Developer Report** — developer and project activity
   - **Conversion Funnel** — lead-to-appointment conversion
3. Set your **date range** and any filters (specific broker, appointment type).
4. Click **Generate**.
5. Review the report on screen.
6. Click **Export to Excel** to download.
7. Click **Save** to keep the report for later.

### Workflow: Read the Analytics Dashboard

1. Go to **Analytics** in the sidebar.
2. Set the **date range** at the top (default is last 30 days).
3. Review the charts:
   - **Appointments by Broker** (horizontal bar chart) — each broker's name with stacked colors for Buyer/Seller/Tenant/Landlord. Hover over a bar for exact numbers.
   - **Property Types** (pie chart) — what property types are most common.
   - **Appointments Over Time** (line chart) — daily/weekly trend lines per type.
   - **Top Cities** (bar chart) — which cities have the most activity.

---

## Tips and Best Practices

### For Brokers

- **Record appointments the same day** — details are freshest right after the meeting. Voice input makes this quick even from your phone.
- **Always fill in budget** — even an approximate range helps analytics and reports immensely.
- **Complete the Client Questionnaire on first meetings** — country of origin, occupation, family status, and how they found you provide valuable marketing insights.
- **Use the client name autocomplete** — type a few characters and select from the list. This links the appointment to an existing contact.
- **Check your Dashboard daily** — the stat cards show your current totals. If something looks off, check whether an appointment was saved correctly.
- **Add developer names for new-build showings** — the "Developers Visited" and "Projects Viewed" fields help track which developments are getting the most interest.

### For Managers

- **Use "Broker Performance" report for weekly team reviews** — it shows each broker's appointment count, reservation rate, and outcomes side by side.
- **Export reports to Excel before meetings** — share with team leads or send to management.
- **Check Analytics weekly** — the "Appointments Over Time" chart reveals trends before they become problems (e.g., a sudden drop in showings).
- **Use "City Report" for market analysis** — see where client activity is concentrated.

### Voice Input Tips

- **Include the date** — "meeting today at 3pm" or "meeting on March 15" works well.
- **Say currency amounts clearly** — "budget three hundred to five hundred thousand euros."
- **Mention the meeting type** — "buyer showing" or "seller meeting" helps the AI choose the right fields.
- **Pause briefly between details** — "Client name is Anna Petrova. [pause] Budget 200 to 400 thousand. [pause] Showed apartment in Paphos."

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| Create a new appointment | Dashboard → New Appointment button, or Sidebar → All Appointments → New |
| Record a buyer showing | New Appointment → Buyer tab |
| Record a seller meeting | New Appointment → Seller tab |
| Record a tenant showing | New Appointment → Tenant tab |
| Record a landlord meeting | New Appointment → Landlord tab |
| Use voice input | Any appointment form → Microphone icon |
| View all appointments | Sidebar → All Appointments |
| Filter by type | All Appointments → Buyer / Seller / Tenant / Landlord tabs |
| Search appointments | All Appointments → Search bar |
| Edit an appointment | All Appointments → Click appointment → Edit |
| Delete an appointment | All Appointments → Click delete icon → Confirm |
| View my dashboard | Sidebar → Dashboard |
| View team analytics | Sidebar → Analytics |
| Build a report | Sidebar → Reports → Choose template |
| Export report to Excel | Reports → Generate → Export button |
| Manage permissions (Admin) | Sidebar → App Permissions |
| View your profile | Top-right menu → Profile |
| Switch role (Act As) | Top-right menu → Role dropdown |
| Return to Sharp Matrix portal | Sidebar → Back to SharpMatrix |
| Get help | Top-right menu → Help & Support |
