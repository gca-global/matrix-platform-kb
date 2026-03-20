# How to Report an Incident

> **Audience:** All Sharp Sotheby's staff
>
> **Purpose:** Standard template for reporting technical issues across all Sharp Matrix applications. Using this format helps the support team reproduce and resolve problems quickly.

---

## The Incident Template

When you encounter an issue you cannot resolve, describe it using these four questions:

> **1. What are you trying to do?**
> *(Describe the task or action you were performing)*
>
> **2. What is going wrong?**
> *(Briefly describe the issue — what you see on screen, any error messages)*
>
> **3. What should happen instead?**
> *(Based on documentation or expected behaviour)*
>
> **4. Screenshot / screen recording** *(if applicable)*

---

## Example

> **1. What are you trying to do?**
> I'm trying to register a new buyer client in Client Connect.
>
> **2. What is going wrong?**
> After filling in all fields and clicking Submit, the page shows a spinning icon for 30 seconds and then returns "Network error."
>
> **3. What should happen instead?**
> The client should be saved and appear in My Requests with "Pending" status.
>
> **4. Screenshot / screen recording**
> *(screenshot attached)*

---

## What Else to Include

Always mention:
- **Your name and role** (e.g., "Maria Petrova, Broker")
- **Which app** you were using
- **Browser and device** if relevant (e.g., "Chrome on Windows laptop")

Some apps have additional details that help the support team:

| App | Extra Info to Include |
|-----|----------------------|
| **Client Connect** | Client name or phone number if the issue is about a specific client |
| **Meeting Hub** | Appointment ID (visible in the URL when viewing an appointment) |
| **Matrix Comms** | Conversation ID or Campaign ID |
| **Agency Portal** | Which dashboard widget or app card is affected |
| **SSO / Login** | Login method used (email/password or Microsoft), which app you were trying to access, how many users are affected |

---

## Severity Guide

Classify your issue so the team can prioritize:

| Severity | Criteria | Examples |
|----------|----------|---------|
| **Critical** | App or system completely down; cannot work at all | SSO login broken for all users; Comms cannot send any messages; Client Connect unreachable |
| **High** | Major feature broken; significant work disruption | Cannot register clients; reports not loading; campaigns failing to send; no one can create appointments |
| **Medium** | Feature partially broken; workaround exists | Voice input not working (can type manually); analytics chart displays incorrectly; minor display issue |
| **Low** | Cosmetic issue or minor inconvenience | Button misaligned; text truncated; typo in label; suggestion for improvement |

---

## Is It a Bug or Something Else?

Before submitting, check whether your issue is actually a bug:

| Type | Description | What to Do |
|------|-------------|------------|
| **How-To Question** | You want to know how to do something | Check the app's KB article first, or ask Zoe |
| **Access Issue** | You cannot access an app or page | Contact your Admin — this is usually a permissions issue |
| **Bug** | Something is broken or behaving incorrectly | Submit an incident using the template above |
| **Data Issue** | Data appears wrong, missing, or duplicated | Submit an incident — include specifics about what data looks wrong |
| **Feature Request** | You want something new or different | Submit separately as a feature request, not a bug |

---

## Where to Submit

Send the incident report to the **2nd Line Support team** through your established channel (email, ticket system, or Teams).

---

## Escalation Path

| Level | Team | What They Do |
|-------|------|-------------|
| **1st Line** | AI Support Assistant (Zoe) | Answer questions, provide guidance, identify known issues, suggest workarounds |
| **2nd Line** | Support / Operations / IT | Analyze and qualify incidents, fix configurations, correct data, escalate bugs |
| **3rd Line** | Development Team | Fix bugs, deploy patches, develop new features |

**Typical resolution times:**
- 1st Line (AI): Immediate
- 2nd Line: Same business day for Critical/High; 1-3 days for Medium/Low
- 3rd Line: Varies by complexity — days to weeks
