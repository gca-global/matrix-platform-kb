# API Contracts — Edge Function API Surface

> Source: matrix-platform-foundation/openapi.yaml, supabase/functions/
>
> **For Lovable**: This document defines the API contracts for SSO Edge Functions
> that your app calls for authentication, permissions, and admin operations.

## Overview

The full OpenAPI specification lives in `matrix-platform-foundation/openapi.yaml` (1700+ lines). Use it for detailed request/response schemas, error codes, and examples. This document summarizes the catalog and governance.

## Edge Function Catalog

### OAuth (6 functions)

| Name | Path | Method(s) | Auth | Purpose |
|------|------|------------|------|---------|
| oauth-authorize | `/oauth-authorize` | GET | None | Initiate OAuth flow, redirect to login |
| oauth-token | `/oauth-token` | POST | None | Exchange auth code for JWT |
| oauth-callback | `/oauth-callback` | GET | None | OAuth callback handler |
| oauth-login | `/oauth-login` | POST | None | Direct login (username/password) |
| oauth-revoke | `/oauth-revoke` | POST | Bearer | Revoke refresh token |
| oauth-userinfo | `/oauth-userinfo` | GET | Bearer | Fetch user info with JWT claims |

### Admin (8 functions)

| Name | Path | Method(s) | Auth | Purpose |
|------|------|------------|------|---------|
| admin-users | `/admin-users` | GET, POST, PATCH, DELETE | Bearer (admin) | User CRUD |
| admin-roles | `/admin-roles` | GET, POST, PATCH, DELETE | Bearer (admin) | Role management |
| admin-apps | `/admin-apps` | GET, POST, PATCH, DELETE | Bearer (admin) | App registration |
| admin-permissions | `/admin-permissions` | GET, POST, DELETE | Bearer (admin) | Permission grants |
| admin-groups | `/admin-groups` | GET, POST, PATCH, DELETE | Bearer (admin) | Group management |
| admin-dashboard | `/admin-dashboard` | GET | Bearer (admin) | Stats, activity feed |
| admin-microsoft-auth | `/admin-microsoft-auth` | POST | Bearer (admin) | Microsoft auth config |
| admin-ad-users | `/admin-ad-users` | GET | Bearer (admin) | Query Azure AD user directory |

### O365 Integration (4 functions)

| Name | Path | Method(s) | Auth | Purpose |
|------|------|------------|------|---------|
| email-messages | `/email-messages` | GET | Bearer | Read/search broker's Exchange emails via Graph API |
| email-attach | `/email-attach` | GET, POST, DELETE | Bearer | Attach/detach email snapshots to/from opportunities |
| calendar-events | `/calendar-events` | GET, POST, PATCH, DELETE | Bearer | CRUD on broker's Outlook calendar events |
| calendar-sync | `/calendar-sync` | POST | Bearer (admin) | Bidirectional sync between CRM showings/meetings and Outlook |

All O365 functions use the user's Microsoft `provider_token` (stored server-side) to call Microsoft Graph API with delegated permissions (`Mail.Read`, `Calendars.ReadWrite`). See [o365-exchange-integration.md](o365-exchange-integration.md) for full details.

### Utility (7 functions)

| Name | Path | Method(s) | Auth | Purpose |
|------|------|------------|------|---------|
| switch-role | `/switch-role` | POST | Bearer | Switch active role → re-issue JWT |
| switch-tenant | `/switch-tenant` | POST | Bearer (system_admin) | Switch active tenant → re-issue JWT with new org context |
| check-permissions | `/check-permissions` | POST | Bearer | Check page/action access |
| check-mls-duplicate | `/check-mls-duplicate` | POST | Bearer | MLS duplicate detection |
| register-app | `/register-app` | POST | Bearer (admin) | Register new OAuth app |
| sync-ad-users | `/sync-ad-users` | POST | Bearer (admin) | Sync Azure AD users |
| sync-azure-profile | `/sync-azure-profile` | POST | Bearer | Sync user profile from Azure |

## Auth Requirements

All functions use `verify_jwt: false` and implement **custom JWT verification** internally. They accept:
- **SSO JWT tokens** (from `oauth-token`) — primary for Matrix Apps
- **Supabase auth tokens** — for compatibility where applicable

Apps send `Authorization: Bearer <token>` with the SSO JWT obtained from the OAuth flow.

## Contract Governance

| Practice | Detail |
|----------|--------|
| **Documentation** | New endpoints: update `openapi.yaml` in matrix-platform-foundation |
| **Breaking changes** | ADR + changelog; notify app owners before deployment |
| **Versioning** | URL path versioning not used — all endpoints are v1 |

## Per-App API Dependency Map

| App | OAuth | switch-role | switch-tenant | check-permissions | Admin | Other SSO Functions | App-Specific Edge Functions |
|-----|-------|-------------|---------------|-------------------|-------|--------------------|-----------------------------|
| All Matrix Apps | oauth-authorize, oauth-token, oauth-userinfo | ✓ | system_admin only | ✓ | — | — | — |
| SSO Console | All OAuth | ✓ | ✓ | ✓ | admin-* (all 8) | register-app | — |
| HRMS | All OAuth | ✓ | ✓ | ✓ | admin-roles | sync-ad-users | hrms-sync-permissions, hrms-ad-admin, hrms-auto-sync, employee-sync, vacation-reminders, holiday-auto-post |
| Matrix Pipeline | All OAuth | ✓ | ✓ | ✓ | admin-roles | check-mls-duplicate | lead-webhook, mls-sync-orchestrator, mls-fetch, ms-graph-proxy, semantic-search, parse-opportunity-info, transcribe-audio, date-reminders, log-share-event, cdl-write |
| ITSM | All OAuth | ✓ | ✓ | ✓ | admin-roles | — | service-desk-tickets, incident-webhook, vendor-logo, ms-graph-proxy, mls-fetch |
| Matrix FM | All OAuth | ✓ | ✓ | ✓ | admin-roles | — | read-financial-entries, save-financial-entries, submit-financial-data, submission-deadlines, get-submission-progress, get-audit-log, export-audit-log, get-recent-updates, generate-test-data, delete-test-data, sso-oauth |
| MLS | All OAuth | ✓ | ✓ | ✓ | — | check-mls-duplicate | — |
| Broker App | All OAuth | ✓ | ✓ | ✓ | — | email-messages, email-attach, calendar-events, calendar-sync | — |
| Manager App | All OAuth | ✓ | ✓ | ✓ | — | email-messages (read-only on team), calendar-events (team view) | — |
| Client Portal, etc. | All OAuth | ✓ | ✓ | ✓ | — | — | — |

**Common subset**: Every app calls `oauth-authorize`, `oauth-token`, `switch-role`, `check-permissions`. `switch-tenant` is available to all apps but only usable by `system_admin` users. Admin apps add `admin-*` functions. Apps with AD sync add `sync-ad-users`. Pipeline and Broker apps add O365 integration functions. Each app deploys its own Edge Functions to its app-specific Supabase instance (see app-catalog.md for project IDs).

## Cross-Reference

| For | See |
|-----|-----|
| JWT structure and RLS | [security-model.md](security-model.md) |
| Deployment and CI/CD | [operations.md](operations.md) |
| App integration patterns | [app-template.md](app-template.md) |
| O365 email & calendar integration | [o365-exchange-integration.md](o365-exchange-integration.md) |