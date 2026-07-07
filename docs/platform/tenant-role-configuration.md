# Tenant Role Configuration

Canonical guide for configuring SSO roles, scopes, and per-app page/action access across Matrix apps.

**KB sources**: [security-model.md](security-model.md), [app-template.md](app-template.md), [ADR-036](../architecture/decisions/ADR-036.md)

## Two enforcement layers

| Layer | Source | Controls |
|-------|--------|----------|
| **L1 — UI** | `sso_role_configurations` (HRMS, Qobrix) or `app_permissions` (ITSM) | Pages and actions visible in sidebar/routes |
| **L2 — Data** | JWT `scope` + `crud` via Postgres RLS | Which rows are readable/writable |

Admin scopes (`global`, `org_admin`, `system_admin`) always pass L1 when no explicit config row exists.

## SSO role tenancy (`sso_roles.tenant_id`)

| Value | Meaning | SSO Console behavior |
|-------|---------|---------------------|
| `NULL` | Global/shared role | Shown for every organization |
| UUID | Tenant-specific role | Shown only when that org is selected |

Acme UAT cloned roles (`ac000001`–`ac000005`) are tenant-scoped to `025a9ba8-2b99-42a1-b6aa-cc573cbef1b5`. They reuse the same **display names** as the global base roles (e.g. `Broker`) but are distinct rows — pick the copy under the user's organization in Console, not Global / shared. **IT Staff** (`ac000005`) is a dedicated Acme role with a unique name for the IT division.

## Data classification by app

### HRMS

| Data class | Tables | Read policy |
|------------|--------|-------------|
| Public directory | `employees`, `employee_managers`, social, reference tables | Tenant-wide |
| Personnel / restricted | vacations, goals, performance, compensation, documents | Pattern B: self / direct reports / admin |
| Team resolution | `employee_managers` (direct reports only) | **Not** JWT `team_ids` |

### Qobrix Sales Automation

| Data class | Tables | Read policy |
|------------|--------|-------------|
| Shared catalog | `properties`, `projects` | Tenant-wide minus `is_private` (ADR-036) |
| Owned CRM records | contacts, opportunities, offers, activities, campaigns | Pattern B via `owner_team_id` + `team_ids` |
| Qobrix historical | via `qobrix-*` EFs | Per-user Qobrix session (read-only) |

### ITSM

| Data class | Tables | Read policy |
|------------|--------|-------------|
| Tenant catalog | service catalog, KB, assets, vendors | Tenant-wide |
| Tickets | `service_desk_tickets` | Self: own; Team: assignee/requester + `requester_team_id ∈ team_ids` |
| Notifications | `notifications` | Recipient only |

## Acme Corp persona matrix (tenant `025a9ba8-2b99-42a1-b6aa-cc573cbef1b5`)

| Persona | SSO role UUID | Scope | CRUD | Teams | HRMS pages | Qobrix pages | ITSM pages |
|---------|---------------|-------|------|-------|------------|--------------|------------|
| Org Admin (×3) | `ac000001` | org_admin | crud | — | `*` (admin fallback) | `*` | `*` |
| Area Manager (×4) | `ac000002` | team | crud | Athens or Thessaloniki sales team | cloned from base Area Manager | home, profile + create/edit/delete/export | requester + agent queue pages |
| Broker (×5) | `ac000003` | self | cru | team membership | cloned from base Broker | home, profile + create/edit | self-service only |
| Senior Broker (×2) | `ac000004` | self | cru | team membership | cloned from base Senior Broker | home, profile + create/edit | self-service only |
| IT Staff (×5) | `ac000005` | org_admin | crud | — | `*` (admin fallback) | `*` | `*` (admin bypass) |

### Sales teams

| Team UUID | Name | Members |
|-----------|------|---------|
| `b7e1c4a2-6f3d-4a91-9c2e-1d8f5a3b7e01` | Athens Sales Team | a.ioannou, k.vlachos, e.papadaki, s.papageorgiou, g.alexiou, s.dimitriou |
| `c8f2d5b3-704e-5b02-ad3f-2e9a6b4c8f02` | Thessaloniki Sales Team | m.theodorou, a.nikolaidis, s.christodoulou, d.katsaros, n.georgiou |

### App reachability (`apps_allowed`)

All five Acme tenant roles include: Portal, Meeting Hub, Client Connect, New Client Registration, HRMS, ITSM, **Qobrix Sales Automation** (`yeBljGGVpyC96RljEDov8n-td2I52cgX`).

**Financial Management (FM)** (`LAmZA9MrZSpJ3NV~a5zyZI8W0.DYscHl`) is granted to **Organization Admin** and **Area Manager** only (management-level sales; IT Staff and brokers excluded). FM uses legacy partial route-gating — `apps_allowed` controls tile visibility; per-page config in the FM app DB is not fully enforced on routes.

## Configuration migrations

| Repo | Migration | Purpose |
|------|-----------|---------|
| `matrix-platform-foundation` | `20260704100000_sso_roles_tenant_id.sql` | `sso_roles.tenant_id` column |
| `matrix-platform-foundation` | `20260704110000_acme_uat_multiapp_config.sql` | Qobrix apps_allowed + role configs + teams |
| `matrix-platform-foundation` | `20260706100000_acme_uat_role_name_cleanup.sql` | Drop `Acme UAT -` prefix; tenant_id disambiguates |
| `matrix-platform-foundation` | `20260706110000_acme_it_staff_role.sql` | IT Staff role (`ac000005`) + FM on Org Admin / Area Manager |
| `matrix-platform-foundation` | `20260706120000_acme_it_staff_remove_fm.sql` | Remove FM from IT Staff `apps_allowed` |
| `matrix-qobrix-sales-automation-rls` | `20260704100000_catalog_listings_is_private.sql` | Catalog RLS + `is_private` |
| `itsm-2-1` | `20260704110000_acme_uat_app_permissions.sql` | Requester vs agent ITSM pages |
| `matrix-hrms` | `20260704110000_acme_uat_manager_hierarchy.sql` | `employee_managers` for HRMS team scope |

## SSO Console operator notes

1. Select the user's **Organization** first on the Account tab.
2. On the **Roles** tab, only global/shared roles and roles for that org are listed.
3. Tenant-specific roles show an org badge on the Roles admin page.
4. Per-app page/action grants are configured in each app's Settings → Role Config (not in SSO Console user edit).
