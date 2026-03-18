# Sharp Matrix SSO & Platform Foundation — 1st Line Support Knowledge Base

> **System name:** Sharp Matrix SSO (Single Sign-On) and Platform Foundation
> **SSO Login URL:** `https://intranet.sharpsir.group/sso-login/`
> **SSO Console URL:** `https://intranet.sharpsir.group/sso-console/` (Admin only)
> **Purpose:** Centralized authentication, user management, roles, permissions, and security for all Sharp Matrix applications.
> **Users:** All Sharp Sotheby's staff (for login); Admins and IT (for management).

---

## What Is Sharp Matrix SSO?

Sharp Matrix SSO is the Single Sign-On system that manages user authentication across all Sharp Matrix applications. When you log in to any app (Client Connect, Meeting Hub, Comms, Agency Portal), you are actually logging in through the SSO system. This means:

- **One login for all apps** — You sign in once and can access any app you are authorized for without logging in again.
- **Centralized user management** — Admins manage all user accounts, roles, and permissions in one place (the SSO Console).
- **Secure access control** — Each user gets a role that determines what they can see and do.

---

## How Login Works (For All Users)

### Logging In

1. Open any Sharp Matrix app (e.g., Agency Portal at `https://intranet.sharpsir.group/agency-portal/`).
2. You are redirected to the SSO Login page.
3. Choose your login method:
   - **Email and Password** — enter your company email and the password provided by your Admin.
   - **Sign in with Microsoft** — click the Microsoft button to use your company Microsoft 365 account.
4. After successful authentication, you are redirected back to the app you were trying to access.

### Logging Out

1. Click your avatar or name in the top-right corner of any app.
2. Click **Sign Out**.
3. You are logged out of all Sharp Matrix apps simultaneously.
4. If you signed in with Microsoft, you may also be logged out of your Microsoft session.

### Session Expiration

- Your login session lasts until you sign out or it expires (typically after extended inactivity).
- If your session expires, you will be redirected to the login page next time you open an app.
- Your data is never lost due to session expiration — just log in again.

---

## User Roles Explained

Every user has a role that determines what they can see and do across all Sharp Matrix apps. Roles are assigned by Admins.

### Common Roles for Business Users

| Role | Typical Position | What They Can Do |
|------|-----------------|-----------------|
| **Broker** | Real estate agent | Register clients, record meetings, view own data |
| **Senior Broker** | Experienced agent | Same as Broker with additional experience-level access |
| **Team Leader** | Team lead | View team data, manage team assignments |
| **Sales Manager** | Office/department manager | View all team data, approve clients, review reports |
| **Office Manager** | Office lead | Similar to Sales Manager |
| **Marketing Manager** | Marketing lead | Access marketing tools, campaigns, analytics |
| **Operations Manager** | Operations lead | Access operational tools and workflows |

### Administrative Roles

| Role | Typical Position | What They Can Do |
|------|-----------------|-----------------|
| **Org Admin** | Company administrator | Full access to all data and settings within the organization |
| **System Admin** | IT administrator | Full access across all organizations (multi-tenant) |
| **IT Support** | IT help desk | User management, troubleshooting access |

### How Visibility Works (Scope)

Each role has a "scope" that determines whose data they can see:

| Scope | Visibility |
|-------|-----------|
| **Self** | Only your own data (clients you registered, meetings you recorded) |
| **Team** | Your data plus data from your team members |
| **Global** | All data in your organization |
| **Org Admin** | All data plus administrative settings |
| **System Admin** | Everything across all organizations |

For example, a Broker with "Self" scope sees only their own clients and meetings. A Sales Manager with "Team" scope sees their team's data. An Org Admin with "Org Admin" scope sees everything.

---

## Permissions (What You Can Access)

### Page Permissions

Each app has pages, and your role determines which pages you can access. For example:

- A Broker in Client Connect can access the "New Client" page but not the "Admin Dashboard."
- A Sales Manager can access the "Review Requests" page.

If you try to access a page you don't have permission for, you will see an "Access Denied" message.

### Action Permissions

Beyond page access, some actions are also permission-controlled:

- Creating, editing, or deleting clients
- Creating, editing, or deleting appointments
- Managing templates
- Running campaigns
- Accessing admin settings

### CRUD Permissions

CRUD stands for Create, Read, Update, Delete. Your role defines which of these operations you can perform:

- **C** = Create new records
- **R** = Read (view) records
- **U** = Update (edit) records
- **D** = Delete records

For example, a Broker might have "CRU" (create, read, update but not delete), while an Admin has full "CRUD".

---

## Teams and Groups

Users can be organized into Teams (Groups). Teams affect:

- **Data visibility** — Users with "Team" scope can see data from all team members.
- **Assignments** — Clients and conversations can be assigned within teams.
- **Reports** — Managers can filter reports by team.

Your team membership is managed by your Admin in the SSO Console.

---

## SSO Console (Admin Only)

The SSO Console is the administration interface for managing the Sharp Matrix platform. Only users with Admin or IT Support roles can access it.

**URL:** `https://intranet.sharpsir.group/sso-console/`

### What Admins Can Do in the SSO Console

| Function | Description |
|----------|-------------|
| **User Management** | Create, edit, deactivate user accounts; assign roles and teams |
| **Role Management** | View and manage roles (predefined roles; custom roles may be added) |
| **Team Management** | Create teams, add/remove members |
| **App Management** | View registered applications, manage app access |
| **Permission Management** | Assign global permissions (rw_global, rw_org, rw_own) |
| **Microsoft AD Integration** | Configure Microsoft Azure AD sync for automatic user provisioning |
| **Password Reset** | Reset a user's password |
| **Activity Log** | View user login and activity history |

### Common Admin Tasks

#### Creating a New User
1. Open the SSO Console → User Management.
2. Click **Add User**.
3. Enter the user's email, name, and initial password.
4. Assign a role (e.g., Broker, Sales Manager).
5. Assign to a team if applicable.
6. Save.
7. Share the login credentials with the new user.

#### Changing a User's Role
1. Open SSO Console → User Management.
2. Find the user.
3. Click Edit.
4. Change the role.
5. Save. The change takes effect on the user's next login.

#### Resetting a User's Password
1. Open SSO Console → User Management.
2. Find the user.
3. Click **Reset Password** or **Set Password**.
4. Enter a new temporary password.
5. Communicate the new password to the user securely.

#### Adding a User to a Team
1. Open SSO Console → Teams/Groups.
2. Find or create the team.
3. Add the user to the team.
4. Save.

---

## Frequently Asked Questions

### Login

**Q: I forgot my password. How do I reset it?**
A: Contact your Admin or IT department. They can reset your password from the SSO Console. There is currently no self-service password reset.

**Q: I get "Invalid credentials" when logging in.**
A: Double-check your email and password. Make sure you are using your Sharp Sotheby's email. If you recently changed your password, use the new one. Contact Admin if the problem persists.

**Q: Can I use my Microsoft 365 account to log in?**
A: Yes, if your company has Microsoft AD integration enabled. Click "Sign in with Microsoft" on the login page.

**Q: I logged in with Microsoft but got "You do not have access."**
A: Your Microsoft account was authenticated, but your Sharp Matrix account may not be set up or may not have the right permissions. Contact your Admin.

**Q: Do I need to log in separately for each app?**
A: No. Once you log in through SSO, you are authenticated for all Sharp Matrix apps. Just click the app in the Agency Portal.

**Q: My session keeps expiring too quickly.**
A: Sessions expire after a period of inactivity (typically 1 hour for the access token, refreshed automatically). If your session keeps expiring unexpectedly, try clearing your browser cookies and logging in again. Contact IT if it persists.

### Roles and Permissions

**Q: How do I know what role I have?**
A: Open any app → click your avatar → Profile. Your role and permissions are displayed there.

**Q: I can't access a page that I should have access to.**
A: Contact your Admin. They may need to update your role or enable the page permission for your role.

**Q: My colleague can see data that I cannot.**
A: This is likely because they have a different role or broader scope. For example, a Sales Manager sees team data while a Broker sees only their own.

**Q: I need access to a new app. What do I do?**
A: Contact your Admin. They need to ensure the app is registered in the SSO Console and that your role has access to it.

### Account Management

**Q: How do I change my display name or email?**
A: Contact your Admin. User profile changes are managed through the SSO Console.

**Q: Can I have multiple roles?**
A: You have one primary role. However, Admins can enable "Act As" role switching, which lets you temporarily view the system as a different role (mainly for testing and support).

**Q: I'm leaving the company. What happens to my account?**
A: Your Admin will deactivate your account in the SSO Console. Your data (clients, meetings, etc.) is preserved for the organization.

---

## Troubleshooting

### Login Issues

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **"Invalid credentials"** | Wrong email or password | Re-enter carefully. Contact Admin for password reset. |
| **Login page does not load** | Network issue or server down | Check your internet. Try again in a few minutes. If the problem persists, contact IT. |
| **Login redirects in a loop** | Cookie or session conflict | Clear browser cookies for `intranet.sharpsir.group` and `supabase.co`. Close and reopen the browser. |
| **Microsoft login fails** | AD integration issue or account not linked | Contact IT. Your Microsoft account may not be synced with Sharp Matrix. |
| **"You do not have access" after login** | Account exists but no role/permissions | Contact Admin to assign role and app access. |
| **"Session expired" while using an app** | Access token expired and could not refresh | Log in again. This is normal after long inactivity. |

### Permission Issues

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **"Access Denied" on a page** | Your role does not have permission | Contact Admin to enable the page for your role. |
| **Cannot create/edit/delete records** | CRUD restrictions on your role | Your role may only have Read access. Contact Admin if you need write access. |
| **Data is missing (cannot see other users' records)** | Scope limitation (Self scope) | This is by design. You see only data within your scope. Ask a Manager or Admin for a report if you need broader data. |

### SSO Console Issues (Admin)

| Problem | Possible Cause | What to Do |
|---------|---------------|------------|
| **Cannot access SSO Console** | Not an Admin role | Only Org Admin, System Admin, and IT Support roles can access the Console. |
| **User changes not taking effect** | User has not re-logged | Changes take effect on the user's next login. Ask them to log out and log back in. |
| **Cannot assign a role** | Role does not exist | Check the available roles in the Console. Custom roles may need to be created. |
| **AD sync not updating users** | Microsoft AD sync configuration issue | Check the AD integration settings. Verify the sync schedule. Contact IT if needed. |

---

## Known Issues and Workarounds

| Issue | Workaround | Status |
|-------|-----------|--------|
| No self-service password reset | Users must contact Admin for password resets | Planned feature |
| Role changes require re-login | After Admin changes a role, the user must log out and log back in for the change to take effect | By design |
| Microsoft login may show a brief blank screen before redirecting | Wait 2-3 seconds — the redirect will complete automatically | Known |
| Some apps may show a brief "loading" state while checking permissions | Normal behavior — wait for the page to finish loading | By design |
| "Act As" role switching may not be visible to all users | Only users with `act_as_roles` configured by Admin can switch roles | Configuration |

---

## When to Escalate — Incident Reporting

If you cannot resolve the issue using the troubleshooting steps above, submit an incident to the 2nd Line Support team.

### What to Include in an Incident Report

1. **Your name and role**
2. **System:** SSO / Login / User Management
3. **Date and time** the issue occurred
4. **What you were trying to do** (e.g., "Log in to Client Connect", "Access Analytics page")
5. **What happened instead** (exact error message)
6. **Which app** were you trying to access
7. **Login method** used (email/password or Microsoft)
8. **Screenshot** if possible
9. **Browser and device**
10. **Is the issue reproducible?**
11. **How many users are affected?** (just you, your team, everyone)
12. **Severity:**
    - **Critical** — No one can log in; SSO is completely down
    - **High** — Some users cannot log in or access apps
    - **Medium** — Individual permission or role issue
    - **Low** — Minor inconvenience or question

### Escalation Path

| Level | Team | Handles |
|-------|------|---------|
| **1st Line** | AI Support Assistant (you are here) | Login guidance, permission questions, known issues |
| **2nd Line** | Support / Operations / IT Team | Account issues, role assignments, AD sync, configuration |
| **3rd Line** | Development Team | SSO bugs, OAuth flow issues, Edge Function failures |

---

## Quick Reference Card

| Task | How |
|------|-----|
| Log in | Go to any app URL → SSO Login → enter credentials |
| Log out | Any app → avatar menu → Sign Out |
| Check your role | Any app → avatar menu → Profile |
| Reset password (Admin) | SSO Console → User Management → Find user → Reset Password |
| Create a user (Admin) | SSO Console → User Management → Add User |
| Change a role (Admin) | SSO Console → User Management → Edit user → Change role |
| Manage teams (Admin) | SSO Console → Groups/Teams |
| Manage app access (Admin) | SSO Console → App Management |
