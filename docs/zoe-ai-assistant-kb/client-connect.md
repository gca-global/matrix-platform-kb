# Sharp Matrix Client Connect — 1st Line Support Knowledge Base

> **App name:** Client Connect
> **URL:** [https://intranet.sharpsir.group/client-connect/](https://intranet.sharpsir.group/client-connect/)
> **Purpose:** Register new real-estate clients, verify their data, and manage the approval pipeline.
> **Users:** Brokers, Contact Center (MLS Staff), Sales Managers (Office Managers), Admins.

---

## What Is Client Connect?

Client Connect is the client registration and verification app for Sharp Sotheby's International Realty. Brokers use it to register new buyer, seller, tenant, or landlord leads. The Contact Center reviews registrations, checks for duplicates against the MLS database, and approves or returns them. Sales Managers handle flagged or escalated cases.

---

## How to Access Client Connect

1. Open your browser and go to [https://intranet.sharpsir.group/client-connect/](https://intranet.sharpsir.group/client-connect/).
2. You will be redirected to the Sharp Matrix SSO login page.
3. Sign in with your company email and password, or use "Sign in with Microsoft".
4. After successful login you are redirected back to Client Connect and land on your role-specific home page.

If you have never logged in before, your account must first be created by an Admin in the SSO Console. Contact your manager or IT if you cannot log in.

---

## User Roles and What They Can Do

| Role | Home Page | What They Do |
|------|-----------|--------------|
| **Broker / Agent** | New Client form | Register new clients (manual or voice), view own requests and their statuses |
| **Contact Center (MLS Staff)** | Client Verification dashboard | Review pending registrations, approve/reject/return, check MLS duplicates, add comments |
| **Sales Manager (Office Manager)** | Review Requests dashboard | Handle flagged or escalated clients, approve/reject/return, assign responsibility |
| **Admin** | Admin Dashboard | Manage all clients, permissions, and app settings. User/role management is in the SSO Console. |

---

## Main Features

### Registering a New Client (Brokers)

1. Navigate to **New Client** in the sidebar.
2. Fill in the required fields:
   - **First Name** (required)
   - **Phone** (required — minimum 8 digits; 10 for Russian numbers). Phone numbers are automatically normalized (spaces, dashes, and parentheses removed) before saving to ensure accurate duplicate checking.
   - **Lead Source** (required — how the lead was obtained: Broker, Agent, Marketing, or Other; if Agent, Marketing, or Other is selected, additional details are required)
   - **Client Intent** (required — select at least one: Buyer, Seller, Tenant, Landlord)
3. Optionally fill in: Last Name, Organisation, Email, Budget range, Rent Budget, Notes.
4. Click **Submit Client**.
5. The registration appears in the Contact Center queue with status **Pending**.

### Voice Input (AI Form Fill)

Brokers can dictate client details instead of typing:

1. Tap the **microphone button** on the registration form.
2. Speak the client details in any supported language (English, Russian, German, Greek).
3. The AI processes your speech and fills the form fields automatically.
4. Review the filled fields and correct anything if needed.
5. Click **Submit**.

**Tip:** Speak clearly and include the client's name, phone number, and how you met them. The AI works best with complete sentences.

### Viewing Your Requests (Brokers)

- Go to **My Requests** (visible on the Broker page).
- You can see the status of each client you registered: **Pending**, **Review**, **Approved**, **Rejected**, or **Information Requested**.
- Click any client card to see full details and comments from the verification team.

### Verifying Clients (Contact Center / MLS Staff)

1. Go to **Client Verification** in the sidebar.
2. You see a list of pending client registrations.
3. Click a client to open the detail view.
4. Review the information and optionally run a **Duplicate Check** against MLS contacts.
5. Take one of these actions:
   - **Approve** — client is confirmed and moves to Active status.
   - **Reject** — client is declined (provide a reason in the comments).
   - **Return to Broker** — send back to the broker for more information (shown as "Information Requested" / "Returned" in lists).
   - **Request Sales Manager Review** — escalate to a Sales Manager. You must assign a specific Sales Manager from the dropdown before sending.
6. Add comments as needed — the broker will see them.
7. Optionally set **WT Responsible** (the responsible person) and mark **Entered in CRM** when added to the CRM.

### MLS Contacts Search (Contact Center)

- Go to the **MLS Contacts** tab on the Client Verification page.
- Search by name, phone, or email to find existing MLS contacts.
- Use this to check for duplicates before approving a new registration.

### Reviewing Flagged Clients (Sales Managers)

1. Go to **Review Requests** in the sidebar.
2. You see clients that were flagged by the Contact Center.
3. Open a client, review the details and comments.
4. Review and take action. For clients in Review status, the Sales Manager may **Request CC Clarification** to send back to the Contact Center, or process directly.
5. You can assign yourself or another Sales Manager as responsible.

### Admin Functions

- **Admin Dashboard** — overview of all clients across all statuses.
- **Settings** — configure Voice Commands, Multi-Language Input, Dashboard URL, Passkeys, and MLS Integration (connection to the shared property database). Settings are displayed as stacked sections, not tabs.
- **App Permissions** — accessible from the user menu (not the sidebar), set which roles can access which pages.

**Note:** User and role management is handled in the SSO Management Console (`/sso-console/`), not within Client Connect.

---

## Client Statuses Explained

| Status | Display Label | Meaning | Who Sets It |
|--------|--------------|---------|-------------|
| **pending** | Pending | Newly registered, waiting for verification | System (on submit) |
| **review** | Review | Flagged for Sales Manager review | Contact Center |
| **rfi** | Information Requested / Returned | Returned to broker — more info needed | Contact Center or Sales Manager |
| **approved** | Approved | Verified and accepted | Contact Center or Sales Manager |
| **rejected** | Rejected | Declined | Contact Center or Sales Manager |

---

## Frequently Asked Questions

### General

**Q: What is Client Connect?**
A: Client Connect is the Sharp Matrix app for registering and verifying new real-estate clients. Brokers submit new client leads, and the Contact Center verifies them before they become active clients.

**Q: Who can use Client Connect?**
A: All Sharp Sotheby's staff who have been granted access: Brokers, Contact Center staff, Sales Managers, and Admins.

**Q: How do I get access?**
A: Your manager or an Admin must create your account in the SSO Console and assign the appropriate role. Contact your IT department if you need access.

### Registration

**Q: Which fields are required to register a client?**
A: First Name, Phone, Lead Source, and at least one Client Intent (Buyer/Seller/Tenant/Landlord).

**Q: Can I register a client by voice?**
A: Yes. Tap the microphone button, speak the client details, and the AI will fill the form. Review and submit.

**Q: What languages does voice input support?**
A: English, Russian, German, and Greek.

**Q: I submitted a client but made a mistake. Can I edit it?**
A: Once submitted, only the Contact Center or Admin can edit client details. Contact them to request a correction.

**Q: What does "Lead Source" mean?**
A: It records how the client lead was obtained. Options are: Broker, Agent, Marketing, or Other. If you select Agent, Marketing, or Other, you must provide additional details.

### Verification

**Q: What does RFI mean?**
A: RFI stands for "Request for Information." It means the Contact Center needs more details from the broker before the client can be approved. Check your My Requests list for comments explaining what is needed.

**Q: How does the duplicate check work?**
A: The system compares the client's name, phone, and email against existing MLS contacts. Phone numbers are normalized (spaces and formatting removed) before comparison to ensure accurate matching. If a potential match is found, it is shown to the reviewer so they can decide whether this is a new client or a duplicate.

**Q: Who can approve clients?**
A: Contact Center staff and Sales Managers with the appropriate permissions.

### Other

**Q: What does "WT Responsible" mean?**
A: It indicates the person responsible for following up with this client in the Wealth Track system.

**Q: What does "Entered in CRM" mean?**
A: A checkbox indicating that the client has been entered into the CRM system.

**Q: How do I switch roles (Act As)?**
A: If your admin has enabled role switching for your account, click your name in the top-right menu and select a different role from the dropdown. This is typically used by admins for testing.

---

## Troubleshooting

### Login and Access

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot log in — "Invalid credentials"** | Wrong email or password | Double-check your email and password. Use "Forgot Password" if available, or contact your Admin. |
| **Login page keeps redirecting in a loop** | Browser cookies or session issue | Clear your browser cookies for `intranet.sharpsir.group`, close and reopen the browser, try again. |
| **"You do not have access" after login** | Account exists but no role assigned | Contact your Admin to assign the correct role (Broker, MLS Staff, etc.). |
| **"Access Denied" on a specific page** | Your role does not have permission for that page | You may not be authorized for this section. Contact your Admin if you believe this is an error. |
| **Page shows "Loading..." forever** | Network issue or session expired | Refresh the page. If it persists, log out and log back in. Check your internet connection. |

### Registration Form

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **"Please complete all required fields" error** | One or more required fields are empty | Check that First Name, Phone, Lead Source, and Client Intent are all filled in. |
| **Phone number rejected** | Too few digits | Enter at least 8 digits (10 for Russian numbers). You may include spaces or dashes for readability — they are automatically removed before saving. |
| **Form does not submit** | Network issue or you are offline | Check your internet connection. If offline, the system will queue the submission and sync when you reconnect. |
| **Voice recording does not start** | Microphone permission denied | Allow microphone access in your browser settings (usually a popup or padlock icon in the address bar). |
| **Voice input did not fill the form correctly** | AI misinterpreted the speech | Speak more slowly and clearly. You can always correct the fields manually after voice input. |
| **"No speech detected"** | Microphone issue or silence | Check that your microphone is working. Speak louder or closer to the microphone. |

### Data and Display

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Client list is empty** | No clients match your filters, or data has not loaded | Clear filters and refresh. If still empty, check that you are looking at the correct tab. |
| **MLS duplicate check returns no results** | The connection to the property database may be temporarily down | Try again in a few minutes. If it keeps happening, report to your Admin. |
| **Notifications not appearing** | Real-time connection issue | Refresh the page. Notifications rely on a live connection to the server. |

### Offline Mode

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **"Saved offline" message** | You lost internet connection during submission | Your registration was saved locally. It will be submitted automatically when you reconnect. |
| **Offline submissions did not sync** | Reconnection was too brief or browser was closed | Reopen Client Connect with an active internet connection. The queue should sync automatically. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| Voice input may not correctly parse names with unusual spelling | After using voice input, manually review and correct the First Name and Last Name fields before submitting | By design — AI best-effort |
| Phone number masking (hiding digits with `*`) works only for certain field configurations | If phone is partially masked, this is intentional privacy protection for agent referrals | By design |
| Multi-language input fields may appear if the admin has enabled multi-language mode | If you only need English, ask your Admin to disable multi-language input in Settings | Configuration |
| MLS contacts search may be slow with large datasets | Use specific search terms (full name or exact phone) rather than partial matches | Performance |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team. Include the following information:

Report the issue using the standard incident template — see [How to Report an Incident](incident-reporting.md). Mention **Client Connect** as the app name.

---

## Getting Started by Role

### New Broker — Your First Day

1. **Log in** at [https://intranet.sharpsir.group/client-connect/](https://intranet.sharpsir.group/client-connect/) using your company credentials.
2. You land on the **New Client** page — this is your home base.
3. **Register your first client**: fill in First Name, Phone, Lead Origin, and Client Intent, then click Submit.
4. Check **My Requests** (scroll down on the same page) to see the status of your submission.
5. Once the Contact Center approves your client, the status changes to **Approved**.
6. After registering a client here, go to **Meeting Hub** to record your appointment with them.

**Tip:** If you have a phone call or walk-in right now, use **Voice Input** — tap the mic, say something like "New buyer John Smith, phone 99123456, walk-in, budget 300 to 500 thousand euros" and the form fills itself.

### New Contact Center Staff — Your First Day

1. **Log in** — you land on the **Client Verification** dashboard.
2. You see a list of **Pending** client registrations from brokers.
3. **Click any client card** to open the detail view.
4. Review the information — check name, phone, email, lead origin, and notes from the broker.
5. **Run a Duplicate Check** by clicking "Check MLS Duplicate" — the system searches the MLS database for matching phone, email, or name.
6. **Take action**: Approve, Reject (with a comment), Return to Broker (RFI) for more info, or escalate to a Sales Manager.
7. Set **WT Responsible** if applicable, and tick **CRM Entered** when you've added the client to the CRM.

**Tip:** Always run the duplicate check before approving. It takes seconds and prevents double registrations.

### New Sales Manager — Your First Day

1. **Log in** — you land on the **Review Requests** page.
2. You see clients that the Contact Center has flagged for your review.
3. Click a client to see all details, broker notes, and CC comments.
4. **Take action**: Approve, Reject, or Return to Broker (RFI).
5. You can also request CC clarification if you need more context.

**Tip:** You only see clients assigned to you. If the Contact Center assigned a specific manager, only that person sees the client in their queue.

---

## Step-by-Step Workflows

### Workflow: Register a Client by Voice

1. Open **New Client** from the sidebar.
2. Tap the **microphone button** at the top of the form.
3. Speak clearly in one sentence. Example: *"New buyer Maria Petrova, phone 99887766, she found us through our Instagram marketing campaign, budget 200 to 400 thousand euros."*
4. Wait 2–3 seconds for the AI to process.
5. The form fields fill automatically — **review every field carefully**.
6. Correct any mistakes (names and numbers are the most common AI errors).
7. Select **Client Intent** if the AI didn't set it (Buyer, Seller, Tenant, Landlord).
8. Click **Submit**.

### Workflow: Register a Client Manually

1. Open **New Client** from the sidebar.
2. Enter **First Name** (required).
3. Enter **Phone** (required) — select country code, then type the number. Spaces are fine; the system normalizes automatically.
4. Select **Lead Origin** — how you met this client. If Marketing/Agent/Other, add a comment.
5. Select **Client Intent** — check at least one box (Buyer, Seller, Tenant, Landlord).
6. Optionally fill in: Last Name, Company, Email, Budget range, Rent Budget, Notes.
7. Click **Submit**.

### Workflow: Contact Center — Full Verification Process

1. Open **Client Verification** from the sidebar.
2. Click a **Pending** client to open the detail modal.
3. Review all fields: name, phone, email, lead origin, budget, broker notes.
4. Click **Check MLS Duplicate**:
   - If **duplicate found**: review the match. If it's the same person, click **Reject as Duplicate**. The system adds a comment with the MLS ID.
   - If **no duplicate**: proceed to the next step.
5. Add a **comment** if needed (required for Reject and Flag for Review actions).
6. **Choose an action**:
   - **Approve** — moves to Active status. The broker is notified.
   - **Reject** — add a reason. The broker sees the rejection and reason.
   - **Return to Broker (RFI)** — sends back for more information. The broker sees it in My Requests.
   - **Request Sales Manager Review** — select a Sales Manager from the dropdown, then click the button. The client appears in that manager's Review Requests queue.
7. Set **WT Responsible** from the dropdown.
8. Tick **CRM Entered** when added to the CRM system.

### Workflow: Broker — Editing and Resubmitting an RFI Client

1. Go to **My Requests** on the New Client page.
2. Find the client with **RFI** status and click it.
3. Read the Contact Center's comments to understand what's needed.
4. Click **Edit & Resubmit**.
5. Update the requested information.
6. Click **Submit** — the client returns to Pending status for re-verification.

---

## Tips and Best Practices

### For Brokers

- **Register clients promptly** — don't wait until the end of the day. The Contact Center works in real-time; the sooner you register, the sooner the client is verified.
- **Include a phone number** — this is the primary identifier for duplicate checking. Without it, dedup accuracy drops significantly.
- **Use voice input for speed** — it's faster than typing, especially on mobile. Include the client name, phone, lead origin, and budget in one natural sentence.
- **Check My Requests daily** — look for any RFI (returned) clients that need your attention.
- **Be specific about Lead Origin** — "Marketing — Facebook ad for Limassol villas" is far more useful than just "Marketing."

### For Contact Center

- **Always run duplicate check before approving** — even if the name looks unique, the phone number might already exist in MLS.
- **Add meaningful comments** — when returning to broker (RFI), be specific: "Phone number is incomplete — please provide full number with country code" is better than "More info needed."
- **Assign Sales Manager when escalating** — always select a specific Sales Manager from the dropdown. Unassigned reviews may get lost.
- **Mark CRM Entered** — this is important for tracking. If you've added the client to the CRM system, tick the box so others know.

### For Sales Managers

- **Check Review Requests daily** — clients waiting for your review are time-sensitive.
- **Use "Request CC Clarification"** if you need more context from the Contact Center before making a decision.

### Voice Input Tips (All Roles)

- **Speak in complete sentences** — "Buyer Anna, phone 99445566, marketing campaign Instagram" works well.
- **Say the phone number digit by digit** if the AI keeps getting it wrong — "nine nine four four five five six six."
- **Specify the currency** — "budget three hundred to five hundred thousand euros."
- **Supported languages**: English, Russian, German, Greek. The AI auto-detects the language.

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| Register a new client | Sidebar → New Client |
| Register by voice | New Client → Microphone button |
| Check status of my registrations | Sidebar → New Client → My Requests |
| Edit and resubmit an RFI client | My Requests → click RFI client → Edit & Resubmit |
| Verify pending clients | Sidebar → Client Verification |
| Run MLS duplicate check | Client detail modal → Check MLS Duplicate |
| Search MLS contacts | Client Verification → MLS Contacts tab |
| Escalate to Sales Manager | Client detail modal → Select SM → Request Sales Manager Review |
| Review flagged clients | Sidebar → Review Requests |
| Manage users and roles | SSO Console (`/sso-console/`) (Admin only) |
| Change app settings | Sidebar → Settings (Admin only) |
| View your profile | Top-right menu → Profile |
| Return to Sharp Matrix portal | Sidebar → Back to SharpMatrix |
| Get help | Sidebar → Help |
