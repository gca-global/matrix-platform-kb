# Sharp Matrix Client Connect — 1st Line Support Knowledge Base

> **App name:** Client Connect
> **URL:** `https://intranet.sharpsir.group/client-connect/`
> **Purpose:** Register new real-estate clients, verify their data, and manage the approval pipeline.
> **Users:** Brokers, Contact Center (MLS Staff), Sales Managers (Office Managers), Admins.

---

## What Is Client Connect?

Client Connect is the client registration and verification app for Sharp Sotheby's International Realty. Brokers use it to register new buyer, seller, tenant, or landlord leads. The Contact Center reviews registrations, checks for duplicates against the MLS database, and approves or returns them. Sales Managers handle flagged or escalated cases.

---

## How to Access Client Connect

1. Open your browser and go to `https://intranet.sharpsir.group/client-connect/`.
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
| **Admin** | Admin Dashboard | Manage all clients, users, roles, permissions, and app settings |

---

## Main Features

### Registering a New Client (Brokers)

1. Navigate to **New Client** in the sidebar.
2. Fill in the required fields:
   - **First Name** (required)
   - **Phone** (required — minimum 8 digits; 10 for Russian numbers)
   - **Lead Origin** (required — how the lead was obtained; if "Agent Referral", "Marketing", or "Other" is selected, a comment is also required)
   - **Client Intent** (required — select at least one: Buyer, Seller, Tenant, Landlord)
3. Optionally fill in: Last Name, Company, Email, Budget range, Rent Budget.
4. Click **Submit**.
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
- You can see the status of each client you registered: Pending, In Review, Approved, Rejected, or RFI (Request for Information).
- Click any client card to see full details and comments from the verification team.

### Verifying Clients (Contact Center / MLS Staff)

1. Go to **Client Verification** in the sidebar.
2. You see a list of pending client registrations.
3. Click a client to open the detail view.
4. Review the information and optionally run a **Duplicate Check** against MLS contacts.
5. Take one of these actions:
   - **Approve** — client is confirmed and moves to Active status.
   - **Reject** — client is declined (provide a reason in the comments).
   - **Return (RFI)** — send back to the broker for more information.
   - **Flag for Review** — escalate to a Sales Manager.
6. Add comments as needed — the broker will see them.
7. Optionally set **WT Responsible** (the responsible person) and mark **CRM Entered** when added to the CRM.

### MLS Contacts Search (Contact Center)

- Go to the **MLS Contacts** tab on the Client Verification page.
- Search by name, phone, or email to find existing MLS contacts.
- Use this to check for duplicates before approving a new registration.

### Reviewing Flagged Clients (Sales Managers)

1. Go to **Review Requests** in the sidebar.
2. You see clients that were flagged by the Contact Center.
3. Open a client, review the details and comments.
4. Approve, Reject, or Return (RFI) the client.
5. You can assign yourself or another Sales Manager as responsible.

### Admin Functions

- **Admin Dashboard** — overview of all clients across all statuses.
- **User Management** — add or remove users, change roles.
- **Settings** — configure Voice API key, MLS API settings, multi-language input, dashboard URL.
- **Permissions** — set which roles can access which pages.

---

## Client Statuses Explained

| Status | Meaning | Who Sets It |
|--------|---------|-------------|
| **Pending** (Prospect) | Newly registered, waiting for verification | System (on submit) |
| **In Review** (PendingReview) | Being reviewed by Contact Center | Contact Center |
| **RFI** (Request for Information) | Returned to broker — more info needed | Contact Center or Sales Manager |
| **Approved** (Active/Client) | Verified and accepted | Contact Center or Sales Manager |
| **Rejected** (Do Not Contact) | Declined | Contact Center or Sales Manager |

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
A: First Name, Phone, Lead Origin, and at least one Client Intent (Buyer/Seller/Tenant/Landlord).

**Q: Can I register a client by voice?**
A: Yes. Tap the microphone button, speak the client details, and the AI will fill the form. Review and submit.

**Q: What languages does voice input support?**
A: English, Russian, German, and Greek.

**Q: I submitted a client but made a mistake. Can I edit it?**
A: Once submitted, only the Contact Center or Admin can edit client details. Contact them to request a correction.

**Q: What does "Lead Origin" mean?**
A: It records how the client lead was obtained (e.g., Walk-in, Phone Call, Website, Agent Referral, Marketing Campaign, Other).

### Verification

**Q: What does RFI mean?**
A: RFI stands for "Request for Information." It means the Contact Center needs more details from the broker before the client can be approved. Check your My Requests list for comments explaining what is needed.

**Q: How does the duplicate check work?**
A: The system compares the client's name, phone, and email against existing MLS contacts. If a potential match is found, it is shown to the reviewer so they can decide whether this is a new client or a duplicate.

**Q: Who can approve clients?**
A: Contact Center staff and Sales Managers with the appropriate permissions.

### Other

**Q: What does "WT Responsible" mean?**
A: It indicates the person responsible for following up with this client in the Wealth Track system.

**Q: What does "CRM Entered" mean?**
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
| **"Please complete all required fields" error** | One or more required fields are empty | Check that First Name, Phone, Lead Origin, and Client Intent are all filled in. |
| **Phone number rejected** | Too few digits | Enter at least 8 digits (10 for Russian numbers). Do not include spaces or dashes. |
| **Form does not submit** | Network issue or you are offline | Check your internet connection. If offline, the system will queue the submission and sync when you reconnect. |
| **Voice recording does not start** | Microphone permission denied | Allow microphone access in your browser settings (usually a popup or padlock icon in the address bar). |
| **Voice input did not fill the form correctly** | AI misinterpreted the speech | Speak more slowly and clearly. You can always correct the fields manually after voice input. |
| **"No speech detected"** | Microphone issue or silence | Check that your microphone is working. Speak louder or closer to the microphone. |

### Data and Display

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Client list is empty** | No clients match your filters, or data has not loaded | Clear filters and refresh. If still empty, check that you are looking at the correct tab. |
| **MLS duplicate check returns no results** | MLS API may be temporarily unavailable | Try again in a few minutes. If persistent, report to Admin (MLS API configuration issue). |
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

### What to Include in an Incident Report

1. **Your name and role** (e.g., "Maria Petrova, Broker")
2. **App name:** Client Connect
3. **Date and time** the issue occurred
4. **Page/section** where the issue happened (e.g., "New Client form", "Client Verification dashboard")
5. **What you were trying to do** (step by step)
6. **What happened instead** (exact error message if any)
7. **Screenshot** if possible
8. **Browser and device** (e.g., "Chrome on Windows laptop", "Safari on iPhone")
9. **Is the issue reproducible?** (Does it happen every time, or was it a one-time event?)
10. **Severity:**
    - **Critical** — Cannot register or verify clients at all; work is blocked
    - **High** — A major feature is broken but there is a partial workaround
    - **Medium** — Minor feature issue; does not block work
    - **Low** — Cosmetic issue or suggestion

### Escalation Path

| Level | Team | Handles |
|-------|------|---------|
| **1st Line** | AI Support Assistant (you are here) | Common questions, how-to guidance, known issues, workarounds |
| **2nd Line** | Support / Operations Team | Issue analysis, qualification, configuration fixes, data corrections |
| **3rd Line** | Development Team | Bug fixes, new features, infrastructure issues |

---

## Quick Reference Card

| Task | Where to Go |
|------|-------------|
| Register a new client | Sidebar → New Client |
| Check status of my registrations | Sidebar → New Client → My Requests |
| Verify pending clients | Sidebar → Client Verification |
| Search MLS contacts | Client Verification → MLS Contacts tab |
| Review flagged clients | Sidebar → Review Requests |
| Manage users and roles | Sidebar → User Management (Admin only) |
| Change app settings | Sidebar → Settings (Admin only) |
| View your profile | Top-right menu → Profile |
| Return to Sharp Matrix portal | Sidebar → Back to SharpMatrix |
| Get help | Sidebar → Help |
