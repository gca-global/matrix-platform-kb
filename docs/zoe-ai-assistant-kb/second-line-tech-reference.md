# Sharp Matrix — 2nd Line Support Technical Reference

> **Audience:** 2nd Line Support analysts, IT operations, technical staff ONLY
> **Purpose:** Technology orientation and pointers to deep-dive documentation for incident qualification and resolution.
> **Repository:** [github.com/sharpsir-group/matrix-platform-kb](https://github.com/sharpsir-group/matrix-platform-kb)

---

> **⚠️ ZOE AI ASSISTANT — DO NOT SERVE THIS CONTENT TO END USERS.**
>
> This document is for IT support staff only. It contains technical details (database tables, server functions, security policies, code references) that will confuse regular users.
>
> **If a regular user asks a question and this document is retrieved:**
> - Do NOT quote or reference any content from this file.
> - Instead, answer using the appropriate 1st-line KB article (portal.md, client-connect.md, meeting-hub.md, comms.md, pipeline.md, hrms.md, itsm.md, financial-management.md, platform-sso-auth.md).
> - If the user's issue cannot be resolved with 1st-line articles, tell them: "This looks like it needs help from the IT team. Please submit a request in ITSM or contact your Admin."
>
> **Only serve this content when the user explicitly identifies themselves as IT staff, 2nd-line support, or asks a clearly technical question about infrastructure, server logs, or system internals.**

---

## How to Use This Document

When a 1st line incident is escalated to you, use this reference to:

1. **Understand which component is involved** — identify the app, service, or infrastructure layer.
2. **Find the right deep-dive documentation** — each section links to the source document in the GitHub repository.
3. **Qualify the incident** — determine if it's configuration, data, code, or infrastructure.
4. **Resolve or escalate** — fix configuration/data issues yourself; escalate code bugs to 3rd line (dev team).

All documentation links point to the GitHub repository raw files for direct access:

```
Base URL: https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/
```

---

## Platform Architecture at a Glance

Sharp Matrix is built on three platforms:

| Platform | Role | Technology |
|----------|------|-----------|
| **Supabase** | Database, Auth, Edge Functions, Realtime | PostgreSQL, Deno runtime, PostgREST |
| **Databricks** | Data warehouse, ETL pipeline | Apache Spark, Delta Lake, Python |
| **Lovable** | App builder (frontend) | React, TypeScript, Vite, Tailwind CSS |

### Supabase Instances

| Instance | Project ID | Purpose |
|----------|-----------|---------|
| **Sharp Matrix SSO** | `xgubaguglsnokjyudgvc` | SSO, authentication, user management, shared data (CDL) |
| **Matrix Comms** | `ujowkipnqgtazmtdsnlm` | WhatsApp/Comms dedicated database |
| **Matrix Pipeline** | `tiuansahlsgautkjsajk` | Pipeline CRM app database (leads, opportunities, contacts) |
| **HRMS** | `wltuhltnwhudgkkdsvsr` | HR Management app database (employees, vacations, performance) |
| **ITSM** | `irjrcskfcyierdbefrpk` | IT Service & Asset Management app database |
| **Matrix FM** | `retujkznogwplfrbniet` | Financial Management app database (reporting, budgets, planning) |
| **CY Web Site** | `yugymdytplmalumtmyct` | Cyprus real estate website |
| **Lovable Source** | `ibqheiuakfjoznqzrpfe` | Development source (read-only) |

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| Full architecture | `docs/ARCHITECTURE.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/ARCHITECTURE.md) |
| Platform overview | `docs/platform/index.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/index.md) |
| Ecosystem architecture | `docs/platform/ecosystem-architecture.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/ecosystem-architecture.md) |
| App catalog (all apps & status) | `docs/platform/app-catalog.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/app-catalog.md) |

---

## Authentication & SSO

All apps authenticate through the Sharp Matrix SSO system using OAuth 2.0 with PKCE.

### How Login Works (Technical)

1. User opens an app → redirected to SSO Login page.
2. User authenticates (email/password or Microsoft AD).
3. Supabase Auth creates a session → session token issued.
4. App calls `oauth-authorize` Edge Function with the session token.
5. SSO validates the client app, checks user permissions, issues an authorization code.
6. App exchanges the code at `oauth-token` for an access token (JWT, 1h) and refresh token (30d).
7. The JWT contains: user ID, role, scope, CRUD permissions, tenant, teams, allowed apps.
8. App uses the JWT for all API calls. RLS policies enforce data access based on JWT claims.

### JWT Payload Structure

Key claims in the SSO JWT:

| Claim | Description | Example |
|-------|-------------|---------|
| `sub` | User UUID | `a1b2c3d4-...` |
| `sso_role` | Active role object | `{"id": "...", "name": "Sales Manager"}` |
| `scope` | Visibility level | `{"id": "team", "name": "Team"}` |
| `crud` | Allowed operations | `"crud"` or `"cr"` or `"r"` |
| `uoi` | Tenant UUID | `d5e6f7g8-...` |
| `teams` | Team memberships | `[{"id": "...", "name": "Cyprus Office"}]` |
| `permissions` | Legacy permission strings | `["rw_global"]` |
| `member_type` | Member type enum | `"Broker"` |
| `allowed_apps` | Apps user can access | `[{"id": "...", "name": "Client Connect"}]` |

### 5-Level Scope Hierarchy

```
self → team → global → org_admin → system_admin
```

| Scope | Data Visibility | Typical Roles |
|-------|----------------|---------------|
| **self** | Own records only | Broker, Agent |
| **team** | Own + team members' records | Team Leader, Sales Manager |
| **global** | All records in the organization | Directors |
| **org_admin** | All records + admin settings | Org Admin |
| **system_admin** | Cross-tenant, everything | System Admin |

### Predefined Roles (23)

Staff: `broker`, `senior_broker` | Team: `team_leader`, `sales_manager`, `office_manager`, `marketing_manager`, `operations_manager`, `hr_manager`, `it_support`, `finance_officer`, `bu_ceo`, `bu_ceo_hr` | Director: `sales_director`, `marketing_director`, `operations_director`, `hr_director`, `finance_director`, `it_director` | C-Suite: `coo`, `cfo`, `ceo` | Admin: `org_admin`, `system_admin`

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| Security model (full) | `docs/platform/security-model.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/security-model.md) |
| App template (auth flow) | `docs/platform/app-template.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/app-template.md) |
| GDPR & compliance | `docs/platform/compliance.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/compliance.md) |

---

## Edge Functions (Server-Side Logic)

Edge Functions run on Supabase's Deno runtime. They handle OAuth, admin APIs, AI processing, and app-specific logic.

### SSO Edge Functions (on `xgubaguglsnokjyudgvc`)

| Function | Purpose | Common Issues |
|----------|---------|---------------|
| `oauth-authorize` | Start OAuth flow, issue auth codes | Redirect URI mismatch, client_id not registered |
| `oauth-token` | Exchange code for JWT tokens | PKCE verifier mismatch, expired auth code |
| `oauth-userinfo` | Return user profile and permissions | Invalid/expired token |
| `oauth-revoke` | Revoke tokens (logout) | — |
| `admin-users` | User CRUD, role/team assignment | Permission denied (not admin) |
| `admin-apps` | App registry management | — |
| `admin-groups` | Team/group management | — |
| `admin-permissions` | Permission assignments | — |
| `switch-role` | Change user's active role, re-issue JWT | Role not assigned to user |
| `sync-ad-users` | Sync users from Microsoft Azure AD | AD credentials expired, API rate limits |
| `check-permissions` | Verify user permission for a resource | — |

### App Edge Functions

| Function | App | Purpose | Common Issues |
|----------|-----|---------|---------------|
| `parse-client-info` | Client Connect | Voice → AI → form fill | AI API key missing, service unavailable |
| `parse-meeting-info` | Meeting Hub | Voice → AI → form fill | AI API key missing, service unavailable |
| `portal-agent-chat` | Agency Portal | AI Advisor chat | AI service overload |
| `transcribe-audio` | Portal | Speech-to-text | Microphone data format issues |
| `text-to-speech` | Portal | TTS for AI responses | — |
| `conversations` | Comms | Conversation CRUD | DB connection issues |
| `messages` | Comms | Send WhatsApp messages | Twilio API errors |
| `twilio-webhook` | Comms | Receive inbound WhatsApp | Webhook URL misconfiguration |
| `templates` | Comms | WhatsApp template management | Template approval delays (WhatsApp) |
| `campaigns` | Comms | Bulk messaging | Rate limits, invalid numbers |
| `service-desk-tickets` | ITSM | Ticket CRUD and stats | DB connection, permission issues |
| `incident-webhook` | ITSM | External incident ingestion | Webhook secret mismatch, payload format |
| `vendor-logo` | ITSM | Vendor logo proxy (Clearbit/Google) | External API unavailable |
| `lead-webhook` | Pipeline | External lead ingestion | Integration config missing in app_settings |
| `mls-sync-orchestrator` | Pipeline | MLS data sync orchestration | MLS credentials, connection timeout |
| `semantic-search` | Pipeline | Semantic/AI property search | Humatic AI service unavailable |
| `parse-opportunity-info` | Pipeline | Voice/text → structured deal data | AI API key missing |
| `date-reminders` | Pipeline | Scheduled contact date reminders | Cron scheduling, notification delivery |
| `log-share-event` | Pipeline | Shared list access analytics | — |
| `hrms-sync-permissions` | HRMS | SSO permission sync to HRMS DB | SSO token expired |
| `hrms-ad-admin` | HRMS | AD sync and employee management | AD credentials, rate limits |
| `hrms-auto-sync` | HRMS | Scheduled AD auto-sync | Service role config, AD API |
| `employee-sync` | HRMS | Excel + AD employee sync | File format, duplicate handling |
| `vacation-reminders` | HRMS | Vacation notification generation | — |
| `holiday-auto-post` | HRMS | Auto-post upcoming holidays | Public holidays not configured |
| `read-financial-entries` | Matrix FM | Read financial data | SSO token, entity permissions |
| `save-financial-entries` | Matrix FM | Save/upsert financial entries | Submitted month locked, write permission |
| `submit-financial-data` | Matrix FM | Submit/withdraw financial data | Permission denied (not admin/rw_global) |
| `submission-deadlines` | Matrix FM | Deadline management | — |
| `get-audit-log` | Matrix FM | Paginated audit log | — |

### Troubleshooting Edge Functions

**How to check if an Edge Function is working:**
- Call the function URL directly: `https://<project-id>.supabase.co/functions/v1/<function-name>`
- A healthy function returns a proper HTTP response (even if 401 without auth).
- A 500 error or no response indicates the function is down or has a runtime error.

**Common Edge Function issues:**

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| 500 Internal Server Error | Runtime error in function code | Check Supabase dashboard → Edge Functions → Logs. Escalate to 3rd line with log excerpt. |
| 401 Unauthorized | Invalid or expired JWT | User should log out and log back in. If persists, check `JWT_SECRET` env var. |
| 403 Forbidden | User lacks required permission | Check user's role and permissions in SSO Console. |
| CORS error in browser | Missing CORS headers or wrong `Accept` header | Known issue with `oauth-authorize` — ensure `Accept: application/json` header. |
| Function timeout | Long-running operation or external API slow | Check Supabase dashboard for execution times. Comms functions depend on Twilio; Portal AI depends on AI gateway. |
| "Function not found" | Function not deployed | Redeploy via GitHub Actions or manual `supabase functions deploy`. |

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| API contracts | `docs/platform/api-contracts.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/api-contracts.md) |
| App template (Edge Functions) | `docs/platform/app-template.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/app-template.md) |
| Operations & deployment | `docs/platform/operations.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/operations.md) |

---

## Database & Data Layer

### Row-Level Security (RLS)

All Supabase tables use RLS policies enforced by JWT claims. Key RLS helper functions:

| Function | Returns | Source |
|----------|---------|--------|
| `get_current_tenant_id()` | Tenant UUID from JWT `uoi` claim | Ensures tenant isolation |
| `get_current_user_id()` | User UUID from JWT `sub` claim | Filters own records |
| `get_active_scope()` | Scope level from JWT | Controls visibility |
| `get_crud()` | CRUD string from JWT | Controls allowed operations |
| `get_current_team_ids()` | Team UUIDs from JWT | Filters team records |
| `is_admin_scope()` | Boolean: global/org_admin/system_admin | Admin access check |

**RLS Patterns:**

| Pattern | Scope | Policy Logic |
|---------|-------|-------------|
| **A — Self** | self | `owning_user_id = get_current_user_id()` |
| **B — Team** | team | Pattern A + `owning_user_id IN (SELECT user_id FROM team_members WHERE team_id IN get_current_team_ids())` |
| **C — Global** | global | `tenant_id = get_current_tenant_id()` |
| **D — Org Admin** | org_admin | Pattern C (all tenant data + admin operations) |
| **E — System Admin** | system_admin | No tenant filter (cross-tenant) |

### Key Database Tables

| Table | Instance | Purpose |
|-------|----------|---------|
| `contacts` | SSO | Client/contact records |
| `entity_events` | SSO | Appointments (buyer/seller/tenant/landlord) |
| `sso_applications` | SSO | Registered apps |
| `sso_roles` | SSO | Role definitions |
| `user_role_assignments` | SSO | User ↔ role mapping |
| `sso_user_groups` | SSO | Teams/groups |
| `sso_user_group_memberships` | SSO | User ↔ team mapping |
| `sso_user_permissions` | SSO | Legacy permissions (rw_global, etc.) |
| `app_permissions` | SSO | Per-app page/action permissions |
| `admin_settings` | SSO | Platform configuration (key/value) |
| `tenants` | SSO | Organizations |
| `offices` | SSO | Office locations |
| `conversations` | Comms | WhatsApp conversations |
| `messages` | Comms | WhatsApp messages |
| `leads` | Pipeline | Sales leads |
| `opportunities` | Pipeline | Pipeline deals/opportunities |
| `crm_contacts` | Pipeline | CRM contact records |
| `pipeline_stages` | Pipeline | Configurable pipeline stage definitions |
| `employees` | HRMS | Employee records |
| `vacations` | HRMS | Vacation/leave requests and approvals |
| `review_cycles` | HRMS | Performance review cycles |
| `onboarding_checklists` | HRMS | New hire onboarding tasks |
| `service_desk_tickets` | ITSM | IT service desk tickets |
| `it_assets` | ITSM | IT asset inventory (CMDB) |
| `software_assets` | ITSM | Software license records |
| `vendors` | ITSM | IT vendor records |
| `entities` | Matrix FM | Group entities/companies |
| `financial_entries` | Matrix FM | Financial line item data |
| `financial_submissions` | Matrix FM | Monthly submission status (draft/submitted) |
| `core_allocations` | Matrix FM | CORE cost allocation percentages |

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| MLS CDL schema (18 tables) | `docs/data-models/mls-cdl-schema.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/mls-cdl-schema.md) |
| Dash data model | `docs/data-models/dash-data-model.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/dash-data-model.md) |
| Platform extensions (x_sm_*) | `docs/data-models/platform-extensions.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/platform-extensions.md) |
| RESO canonical schema | `docs/data-models/reso-canonical-schema.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/reso-canonical-schema.md) |
| Field mapping (Dash ↔ RESO ↔ Qobrix) | `docs/data-models/property-field-mapping.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/property-field-mapping.md) |
| Data quality | `docs/data-models/data-quality.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/data-quality.md) |

---

## Data Pipeline (ETL)

The MLS 2.0 data pipeline uses Databricks with a medallion architecture:

```
Qobrix API → Bronze (raw JSON) → Silver (cleaned, typed) → Gold (aggregated) → Supabase CDL
```

| Layer | Purpose | Technology |
|-------|---------|-----------|
| **Bronze** | Raw data ingestion from Qobrix API | Databricks notebooks, Delta Lake |
| **Silver** | Cleaned, validated, RESO-mapped data | Spark SQL, data quality checks |
| **Gold** | Aggregated analytics, KPIs | Spark SQL, scheduled jobs |
| **CDL Sync** | Push Gold data to Supabase for apps | Python, Supabase REST API |

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| ETL pipeline architecture | `docs/data-models/etl-pipeline.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/etl-pipeline.md) |
| MLS datamart & migration | `docs/platform/mls-datamart.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/mls-datamart.md) |
| Data contracts | `docs/data-models/data-contracts.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/data-contracts.md) |
| RESO Web API | `docs/data-models/reso-web-api.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/data-models/reso-web-api.md) |

---

## Frontend Technology Stack

All Sharp Matrix apps share the same stack:

| Technology | Version | Purpose |
|-----------|---------|---------|
| **React** | 18 | UI framework |
| **TypeScript** | 5.x | Type safety |
| **Vite** | 5.x | Build tool and dev server |
| **Tailwind CSS** | 3.x | Utility-first styling |
| **shadcn/ui** | latest | Component library (Radix-based) |
| **TanStack React Query** | 5.x | Server state / data fetching |
| **React Router** | 6.x | Client-side routing |
| **Supabase JS** | 2.x | Database client |
| **i18next** | latest | Internationalization (Comms app) |
| **Zod** | latest | Schema validation |
| **react-hook-form** | latest | Form management |

### App Hosting

| Component | Hosted At |
|-----------|----------|
| Frontend apps | Apache (`/opt/bitnami/apache/htdocs/`) on `intranet.sharpsir.group` |
| Edge Functions | Supabase (Deno runtime) |
| Database | Supabase (PostgreSQL) |
| File storage | Supabase Storage |
| ETL | Databricks workspace |

### App URL Paths

| App | Path | Base Path in Code |
|-----|------|------------------|
| Agency Portal | `/agency-portal/` | `/agency-portal` |
| Client Connect | `/client-connect/` | `/client-connect` |
| Meeting Hub | `/meeting-hub/` | `/meeting-hub` |
| Matrix Comms | `/comms/` | `/comms` |
| Matrix Pipeline | `/matrix-pipeline/` | `/matrix-apps-template` (needs update) |
| HRMS | `/matrix-hr-management/` | `/matrix-hr-management` |
| ITSM | `/itsm/` | `/matrix-apps-template` (needs update) |
| Matrix FM | `/matrix-fm/` | `/matrix-apps-template` (needs update) |
| SSO Console | `/sso-console/` | `/console` |
| SSO Login | `/sso-login/` | `/sso-login` |

### Deep-Dive Documentation

| Topic | Document | GitHub Raw URL |
|-------|----------|---------------|
| App template (full stack details) | `docs/platform/app-template.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/app-template.md) |
| Testing strategy | `docs/platform/testing-strategy.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/testing-strategy.md) |
| Performance targets | `docs/platform/performance.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/performance.md) |
| Mobile strategy | `docs/platform/mobile-strategy.md` | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/platform/mobile-strategy.md) |

---

## External Integrations

| Service | Used By | Purpose | Common Issues |
|---------|---------|---------|---------------|
| **Microsoft Azure AD** | SSO | User authentication, profile sync | Token expiry, sync delays, account not linked |
| **Twilio** | Comms | WhatsApp Business API | API rate limits, template approval delays, webhook failures |
| **HumaticAI** | Comms | AI-powered reply suggestions | Service availability, incorrect AI responses |
| **OpenAI / Gemini** | Client Connect, Meeting Hub | Voice-to-form AI processing | API key expiry, rate limits, parsing errors |
| **Lovable AI Gateway** | Meeting Hub, Portal | AI processing backend | Service availability |
| **Qobrix CRM** | ETL Pipeline | Legacy data source (being replaced) | API changes, rate limits |
| **SIR/Anywhere.com (Dash)** | Listings | Listing syndication platform | Sync delays, field mapping issues |

---

## Business Processes

Understanding the business helps qualify incidents correctly.

| Process | Summary | Deep-Dive |
|---------|---------|-----------|
| **Listing Pipeline** | Seller-side: 8 stages from Prospect to Closed | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/business-processes/listing-pipeline.md) |
| **Sales Pipeline** | Buyer-side: 8 stages from Qualification to Closed | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/business-processes/sales-pipeline.md) |
| **Lead Qualification** | MQL → SQL using BANT criteria | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/business-processes/lead-qualification.md) |
| **Follow-Up vs Active Sales** | Nurturing vs active deal boundary | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/business-processes/follow-up-vs-active-sales.md) |
| **Listing Checklist** | Broker, marketing, finance checklists | [View](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/business-processes/listing-checklist.md) |

---

## Incident Qualification Guide for 2nd Line

When you receive an escalated incident, follow this decision tree:

### Step 1: Identify the Component

| User reports... | Component | Check first |
|----------------|-----------|-------------|
| Cannot log in | SSO / Auth | SSO Edge Functions, user account status |
| Cannot access a page | Permissions | `app_permissions` or `role_configurations` table, user role |
| Data not showing | Database / RLS | RLS policies, scope, tenant_id |
| Feature not working | App / Edge Function | Edge Function logs, browser console |
| Messages not sending | Comms / Twilio | Twilio dashboard, webhook config |
| IT ticket not saving | ITSM Edge Functions | `service-desk-tickets` function logs, required asset validation |
| Vacation approval stuck | HRMS workflow | `vacations` table `approval_step`, manager assignment |
| Financial data locked | Matrix FM submission | `financial_submissions` table status, month already submitted |
| Pipeline deal not moving | Pipeline stage rules | Required fields for stage, opportunity status |
| AI not responding | AI Services | API key validity, external service status |
| Slow performance | Infrastructure | Supabase dashboard, network |

### Step 2: Check Severity and Impact

| Check | How |
|-------|-----|
| Is it affecting one user or many? | Ask the reporter; check if others have the same issue |
| Is there a workaround? | Test alternative workflows |
| Is data at risk? | Check if data was lost or corrupted |
| Is it a blocker? | Can the user continue their work another way? |

### Step 3: Resolve or Escalate

| Issue Type | 2nd Line Can Fix | Escalate to 3rd Line |
|-----------|-----------------|---------------------|
| **User account/role issue** | Yes — SSO Console | — |
| **Permission misconfiguration** | Yes — SSO Console or app_permissions table | — |
| **Data correction** | Yes — via database | — |
| **App configuration** | Yes — admin_settings, app_settings | — |
| **Twilio/webhook config** | Yes — Supabase secrets, Twilio dashboard | — |
| **Edge Function error (500)** | Possibly — check logs, redeploy | Yes, if code fix needed |
| **UI bug** | — | Yes |
| **Business logic error** | — | Yes |
| **RLS policy bug** | — | Yes |
| **Performance degradation** | Possibly — check indexes, query plans | Yes, if code optimization needed |

### Escalation to 3rd Line — What to Include

1. **Incident ID** and severity
2. **Component**: which app, Edge Function, or table
3. **Steps to reproduce**
4. **Error logs**: Edge Function logs, browser console errors
5. **Screenshots or screen recordings**
6. **Number of affected users**
7. **Attempted fixes** and their results
8. **Urgency**: business impact assessment

---

## Useful Links

| Resource | URL |
|----------|-----|
| Knowledge Base (GitHub) | [github.com/sharpsir-group/matrix-platform-kb](https://github.com/sharpsir-group/matrix-platform-kb) |
| Supabase Dashboard (SSO) | `https://supabase.com/dashboard/project/xgubaguglsnokjyudgvc` |
| Supabase Dashboard (Comms) | `https://supabase.com/dashboard/project/ujowkipnqgtazmtdsnlm` |
| Supabase Dashboard (Pipeline) | `https://supabase.com/dashboard/project/tiuansahlsgautkjsajk` |
| Supabase Dashboard (HRMS) | `https://supabase.com/dashboard/project/wltuhltnwhudgkkdsvsr` |
| Supabase Dashboard (ITSM) | `https://supabase.com/dashboard/project/irjrcskfcyierdbefrpk` |
| Supabase Dashboard (Matrix FM) | `https://supabase.com/dashboard/project/retujkznogwplfrbniet` |
| SSO Console | `https://intranet.sharpsir.group/sso-console/` |
| Agency Portal | `https://intranet.sharpsir.group/agency-portal/` |
| Full KB Index | [docs/INDEX.md](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/docs/INDEX.md) |
| AGENTS.md (entry point) | [AGENTS.md](https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/AGENTS.md) |
