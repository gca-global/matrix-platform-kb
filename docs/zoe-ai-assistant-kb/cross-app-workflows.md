# Cross-App Workflows & Daily Routines — 1st Line Support Knowledge Base

> **Purpose:** Understand how Client Connect, Meeting Hub, and the Agency Portal work together. Learn end-to-end client lifecycle, daily routines by role, and how data flows between apps.
> **Audience:** All Sharp Sotheby's staff — Brokers, Agents, Contact Center, Sales Managers, Admins.

---

## The Client Lifecycle: End to End

A client passes through several stages across multiple apps. Here is the full journey:

```
Broker meets client
       ↓
[Client Connect] Register client → Contact Center verifies → Approved
       ↓
[Meeting Hub] Record the appointment → Fill in budget, listings, outcome
       ↓
[Agency Portal] Dashboard reflects updated stats → Pipeline value grows
       ↓
(Repeat: more meetings, reservations, deal closes)
```

### Stage 1: Client Registration (Client Connect)

1. **Broker registers the client** via Client Connect — enters name, phone, lead origin, client intent (Buyer/Seller/Tenant/Landlord), and optionally budget and notes.
2. Client status becomes **Pending**.

### Stage 2: Verification (Client Connect)

3. **Contact Center picks up the pending client** — reviews details, runs MLS duplicate check.
4. Contact Center takes one of these actions:
   - **Approve** → client becomes Active/Approved.
   - **Reject** → client is closed with a reason (e.g., duplicate, incomplete).
   - **Return to Broker (RFI)** → broker must update info and resubmit.
   - **Request Sales Manager Review** → assigns to a specific Sales Manager for a decision.

### Stage 3: Sales Manager Review (Client Connect, if escalated)

5. **Sales Manager reviews** the flagged client and decides: Approve, Reject, or Return to Broker.

### Stage 4: Appointment (Meeting Hub)

6. **Broker records the meeting** in Meeting Hub — selects the appointment type (Buyer, Seller, Tenant, Landlord), fills in client details, budget, listings shown, developers visited, and outcome.
7. The appointment is saved and appears on the broker's dashboard and in Analytics.

### Stage 5: Dashboard & Analytics (Portal + Meeting Hub)

8. **Agency Portal** stat widgets update: New Clients count, Approved Clients count, This Week Meetings, Pipeline Value.
9. **Meeting Hub Analytics** shows the appointment in "Appointments by Broker" charts, city breakdowns, and trends.

### Stage 6: Ongoing Activity

10. Broker continues to record follow-up meetings in Meeting Hub.
11. If a **reservation** is made, the broker marks it in the appointment form — Pipeline Value increases on the Portal dashboard.
12. Managers and Admins can track the team's performance through Analytics and Reports.

---

## Daily Routines by Role

### Broker / Agent — Daily Routine

| Time | Action | App |
|------|--------|-----|
| **Start of day** | Open Agency Portal — check stats, review Today's Agenda | Portal |
| **Morning** | Check My Requests in Client Connect for RFIs or approved clients | Client Connect |
| **Before each meeting** | Confirm client details in Client Connect | Client Connect |
| **After each meeting** | Record the appointment in Meeting Hub (voice input is fastest) | Meeting Hub |
| **Walk-in or phone call** | Register the new client in Client Connect immediately | Client Connect |
| **End of day** | Quick check: Portal dashboard — are numbers as expected? Any missing entries? | Portal |

**Weekly:** Review your Analytics in Meeting Hub to see appointment trends and success rates.

### Contact Center Staff — Daily Routine

| Time | Action | App |
|------|--------|-----|
| **Start of day** | Open Client Connect → Client Verification dashboard | Client Connect |
| **Throughout the day** | Process pending client registrations: verify, duplicate-check, approve/reject/RFI | Client Connect |
| **When escalation needed** | Flag for Sales Manager Review — select the right SM from the dropdown | Client Connect |
| **End of day** | Check there are no pending clients left unprocessed | Client Connect |
| **Quick check** | Open Portal to see aggregate client counts | Portal |

### Sales Manager — Daily Routine

| Time | Action | App |
|------|--------|-----|
| **Start of day** | Open Client Connect → Review Requests page | Client Connect |
| **Morning** | Process flagged clients: approve, reject, or return to broker | Client Connect |
| **Throughout the day** | Monitor Analytics in Meeting Hub for team performance | Meeting Hub |
| **Weekly** | Build and export a Broker Performance report in Meeting Hub | Meeting Hub |
| **Quick check** | Open Portal dashboard for big-picture stats | Portal |

### Admin — Daily Routine

| Time | Action | App |
|------|--------|-----|
| **Start of day** | Open Portal — check company-wide stats | Portal |
| **As needed** | Manage users and permissions in SSO Console | SSO Console |
| **As needed** | Review Analytics and Reports in Meeting Hub | Meeting Hub |
| **Weekly** | Export reports and share with management | Meeting Hub |
| **As needed** | Configure app settings in Client Connect or Meeting Hub | App → Settings |

---

## How Data Flows Between Apps

### Client Connect → Meeting Hub

- When a broker records an appointment in Meeting Hub and types a client name, the **autocomplete** draws from contact records.
- Budget information entered during registration can be cross-referenced with the budget entered in the Meeting Hub appointment form.
- There is no automatic data push — the broker manually enters appointment details in Meeting Hub.

### Client Connect → Agency Portal

- **New Clients** widget: counts recently registered clients.
- **Approved Clients** widget: counts clients with Approved status.
- **Pipeline Value** widget: reflects the value of active deals and reservations.
- These widgets pull data directly from the Client Connect database in near real-time.

### Meeting Hub → Agency Portal

- **This Week Meetings** widget: counts appointments scheduled for the current week.
- **Recent Activity** section: shows the latest recorded appointments.
- **Today's Agenda** section: shows today's scheduled meetings.

### SSO Console → All Apps

- User accounts, roles, and permissions are managed in the SSO Console.
- Changes to a user's role (e.g., promoting from Broker to Sales Manager) take effect across all apps after the next login.
- App permissions (which pages a role can see) are configured per-app in the SSO Console.

---

## Cross-App Scenarios

### Scenario: Broker Registers a Client and Records a Meeting

1. **Client Connect**: Broker opens New Client, fills in "Maria Petrova, phone 99887766, buyer, budget 300–500k EUR", submits.
2. **Client Connect**: Contact Center sees the pending registration, runs MLS duplicate check (no match found), approves.
3. **Meeting Hub**: Broker opens New Appointment → Buyer, enters "Maria Petrova", appointment date today, budget 300k–500k, shows 3 properties in Limassol, outcome: "Interested, wants second viewing."
4. **Portal**: Dashboard now shows +1 in New Clients, +1 in Approved Clients, +1 in This Week Meetings.

### Scenario: Contact Center Finds a Duplicate

1. **Client Connect**: Broker submits a new client "John Smith, 99112233".
2. **Client Connect**: Contact Center opens the card, clicks "Check MLS Duplicate" — system finds a match: "John Smith, +35799112233" already exists in MLS.
3. **Client Connect**: Contact Center clicks "Reject as Duplicate" and adds a comment: "Existing MLS contact #12345."
4. **Client Connect**: Broker sees the rejection and reason in My Requests.

### Scenario: Sales Manager Escalation

1. **Client Connect**: Contact Center is unsure about a high-value client and clicks "Request Sales Manager Review" → selects "Natalia Sorokina" from the dropdown.
2. **Client Connect**: Natalia sees the client in her Review Requests queue.
3. **Client Connect**: Natalia reviews the details and Contact Center comments, decides to approve.
4. **Meeting Hub**: The broker records the subsequent meeting with the now-approved client.

### Scenario: Manager Prepares a Weekly Team Report

1. **Portal**: Manager opens the Portal to see aggregate weekly stats across all brokers.
2. **Meeting Hub → Analytics**: Manager drills into the "Appointments by Broker" chart to see who had the most meetings.
3. **Meeting Hub → Reports**: Manager generates a "Broker Performance" report for the last 7 days, reviews it on screen, then exports to Excel.
4. The Excel file is shared with the team lead in the weekly status meeting.

---

## Frequently Asked Questions

**Q: Do I need to enter client data twice — once in Client Connect and once in Meeting Hub?**
A: Partially. You register the client in Client Connect (name, phone, lead origin). In Meeting Hub, you enter appointment-specific details (listings, budget, outcome). The client name autocompletes, so you don't retype it.

**Q: If I update a client's phone number in Client Connect, does it update in Meeting Hub?**
A: Meeting Hub stores appointment data independently. The client name links back, but there is no automatic sync of phone or email changes. Update both if needed.

**Q: Can I record a meeting without registering the client first?**
A: Yes — you can type any name in Meeting Hub. However, it's best practice to register in Client Connect first so the client goes through verification and appears in your Portal stats.

**Q: Where do the Portal dashboard numbers come from?**
A: Pipeline Value and Client counts come from Client Connect. Meeting counts come from Meeting Hub. They pull data in near real-time.

**Q: My Portal stats don't match what I see in Client Connect or Meeting Hub.**
A: Try refreshing the Portal. If the numbers still don't match, check that you're comparing the same date range and that all your data was saved successfully.

**Q: Which app should I open first in the morning?**
A: Start with the **Agency Portal** for a quick overview, then go to your primary app: **Client Connect** (Contact Center, Sales Managers) or **Meeting Hub** (Brokers after meetings).

**Q: How does the "Pipeline Value" on the Portal dashboard get calculated?**
A: It sums up the values of active reservations and deals recorded across Client Connect and Meeting Hub appointment forms.

---

## Glossary of Cross-App Terms

| Term | Meaning |
|------|---------|
| **Pending** | Client registered but not yet verified by Contact Center |
| **Approved** | Client verified and cleared for business activity |
| **Rejected** | Client declined (duplicate, incomplete, or other reason) |
| **RFI (Return for Information)** | Client sent back to broker for more details |
| **Flagged for Review** | Client escalated to a Sales Manager for a decision |
| **WT Responsible** | The WealthTech responsible person assigned to the client |
| **CRM Entered** | Contact Center has added the client to the external CRM system |
| **Lead Origin** | How the client was acquired (walk-in, marketing, referral, etc.) |
| **Client Intent** | What the client wants: Buy, Sell, Rent, or Let |
| **Pipeline Value** | Total monetary value of active deals and reservations |
| **Reservation** | A confirmed intent to purchase, recorded in Meeting Hub |
| **MLS Duplicate** | A matching contact found in the MLS (Multiple Listing Service) database |
| **SSO Console** | The admin app for managing users, roles, permissions, and connected apps |
| **Quick Access Bar** | Shortcut icons at the top of the Portal dashboard |
