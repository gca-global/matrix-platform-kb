# HRMS Data Access Matrix

> **Authoritative reference** for which roles can read/write which data in the HRMS app.
> Tests in `matrix-testing-suite/tests/apps_hrms/` validate these rules.
> Lovable-generated RLS policies and frontend hooks must conform to this matrix.

Last updated: 2026-04-08

## Role scopes (lowest → highest)

| Scope | Example roles | JWT `scope` value |
|-------|--------------|-------------------|
| Self | Staff, Broker, Senior Broker | `self` |
| Team | Office Manager, Team Leader | `team` |
| Global | HR Manager, Sales Director | `global` |
| Org Admin | Org Admin (Finance) | `org_admin` |
| System Admin | System Admin | `system_admin` |

## Row visibility model

**Principle:** Higher scope always sees >= lower scope rows on employee-linked tables.

- **Self** — own records only (where `employee_id` = current user's employee)
- **Team** — own + direct reports / same department
- **Global** — all rows in the tenant
- **Org Admin** — all rows in the tenant (+ admin write privileges)
- **System Admin** — all rows across tenants

---

## Table-by-table access

### Legend

| Symbol | Meaning |
|--------|---------|
| R | SELECT (read) |
| C | INSERT (create) |
| U | UPDATE |
| D | DELETE |
| own | Only rows belonging to current user |
| team | Own + direct reports / same department |
| all | All rows in tenant |
| masked | Row visible but sensitive columns redacted |
| -- | No access |

---

### Core HR — People & Organization

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `employees` | R: all (masked) | R: all (masked) | R/C/U/D: all | R/C/U/D: all | Everyone sees all employees in tenant; sensitive cols masked for non-admin |
| `employee_directory` (view) | R: all (masked) | R: all (salary visible for reports) | R: all (unmasked) | R: all (unmasked) | Managers see salary for direct reports only |
| `departments` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Reference table; read by all, write by admin |
| `locations` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Same pattern as departments |
| `employee_managers` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Org chart; read by all, write by admin |

### Compensation & Payroll

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `compensation_history` | R: own | R: team | R: all | R: all | Employees see own comp; managers see reports'; HR/Finance see all |
| `payroll_records` | R: own | R: team | R: all | R/C/U/D: all | Same read hierarchy; Finance has full CRUD |
| `vacation_balances` | R: own | R: team | R: all | R/C/U/D: all | Managers read-only for team; only Finance/HR can write |

### Leave & Vacation

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `vacations` | R: own; C/U: own | R: team; U: approve/reject | R: all; C/U: HR step | R: all; U: finance step | Multi-step approval: employee → manager → HR → finance |
| `leave_policies` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Reference table; everyone reads, admin writes |
| `public_holidays` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Same as leave_policies |

### Performance

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `performance_reviews` | R: own | R: team | R/C/U/D: all | R: all | |
| `review_cycles` | R: all | R: all; C: team cycles | R/C/U/D: all | R: all | Managers can create review cycles for their team |
| `review_participants` | R: own; U: self-review fields | R: team; U: manager-review fields | R/C/U/D: all | R: all | Self updates self_review; manager updates manager_review |
| `goals` | R: own; C/U: own | R: team | R: all | R: all | |

### Documents

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `document_templates` | R: all | R: all | R/C/U/D: all | R/C/U/D: all | Reference table; managers cannot create templates |
| `document_distributions` | R: own; U: sign | R: team | R/C/U/D: all | R: all | Employees sign; HR distributes |
| `employee_documents` | R: own | R: team | R: all | R: all | |

### Onboarding & Offboarding

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `onboarding_templates` | R: all | R: all | R/C/U/D: all | R: all | Column: `name` (not `title`) |
| `onboarding_checklists` | R: own | R: team | R/C/U/D: all | R: all | |
| `onboarding_tasks` | R: own | R: team | R/C/U/D: all | R: all | |
| `offboarding_templates` | -- | -- | R/C/U/D: all | R: all | HR+ only; self/team blocked |
| `offboarding_checklists` | R: own | R: team | R/C/U/D: all | R: all | |
| `offboarding_tasks` | R: own | R: team | R/C/U/D: all | R: all | |

### Internal Changes

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `internal_changes` | R: own; C: request | R: team; C: request | R/C/U/D: all | R: all | Managers see their team's changes |
| `employee_edit_requests` | R: own; C: request | R: team | R/C/U/D: all | R: all | Self cannot self-approve |

### Social

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `social_posts` | R: all; C/U/D: own | R: all; C/U/D: own | R: all; C/U/D: own | R: all; C/U/D: own | Tenant-wide read; author-gated write; requires `c`/`u`/`d` in JWT crud |
| `social_comments` | R: all; C/U/D: own | Same | Same | Same | Same pattern as posts |
| `social_reactions` | R: all; C/D: own | Same | Same | Same | |
| `social_post_views` | R: all; C: own | Same | Same | Same | |

### Notifications

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `notifications` | R: own; U: mark read | R: scope-filtered | R/C/U/D: all | R/C/U/D: all | Key column: `recipient_id` (not `employee_id`). Self cannot delete; admin creates system notifications |

### Audit

| Table | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|-------|------|----------------|-------------|---------------------|-------|
| `employee_audit_log` | R: own | R: team | R/C: all | R/C: all | Self cannot insert; admin inserts audit entries |

### Storage

| Bucket / path | Self | Team (Manager) | Global (HR) | Org Admin (Finance) | Notes |
|---------------|------|----------------|-------------|---------------------|-------|
| `employee-documents/{emp_id}/` | R/C/U/D: own path | R: team paths | R/C/U/D: all | R: all | Employee manages own folder; HR manages all |

---

## Key design decisions (2026-04-08)

1. **Directory is tenant-wide** — all employees see all other employees in the same tenant, with sensitive columns (salary, tax_id) masked. No scope-filtering on the directory view.

2. **Compensation visible to self** — employees see their own `compensation_history`; managers see their reports'; HR and Finance see all.

3. **Managers see reports' salary** — in `employee_directory`, managers can see the `current_salary` field for their direct reports only. All others see it masked.

4. **Vacation balances: managers read-only** — managers can view team balances but cannot create/update/delete. Only Finance (org_admin) and HR (global) have write access.

5. **Managers see team internal changes** — `internal_changes` rows for the manager's direct reports are visible to team scope.

6. **Managers can create review cycles** — team-scope managers can create `review_cycles` scoped to their team. They cannot create `leave_policies`, `public_holidays`, or `document_templates`.

---

## Test coverage mapping

| Access rule | Validated by test script(s) | Status |
|-------------|---------------------------|--------|
| Directory tenant-wide read | `test_hrms_rls_directory_view.sh`, `test_hrms_rls_segregation.sh` A1/A2 | Passing |
| Compensation hierarchy (real team JWTs) | `test_hrms_compensation_reads.sh` A1/A2/B1/B2 | Passing |
| Self sees own compensation only | `test_hrms_compensation_reads.sh` A_OWN, B_OWN | Passing |
| Salary masking + manager-sees-report | `test_hrms_rls_directory_view.sh` VD2-VD5, VD5b | Passing |
| Vacation approval chain | `test_hrms_workflow_vacation.sh`, `test_hrms_process_vacation_chain.sh` | Passing |
| Balance CRUD (team read-only) | `test_hrms_compensation_reads.sh` C1b/C5b-d, `test_hrms_persona_finance.sh` | Passing |
| Internal changes team visibility | `test_hrms_process_internal_changes.sh` G2/G4 | **APP GAP** — RLS blocks team scope |
| Policy table admin-only write | `test_hrms_rls_policy_tables.sh`, `test_hrms_persona_finance.sh` | Passing |
| Review cycle manager create | `test_hrms_rls_policy_tables.sh` C3b | **APP GAP** — RLS blocks team INSERT (403) |
| App-level page/action permissions | `test_hrms_app_permissions.sh` | **APP GAP** — app token can't read configs |

---

## Actual table schemas (verified 2026-04-08)

Column names from PostgREST OpenAPI spec and migration files on HRMS instance `wltuhltnwhudgkkdsvsr`.
RLS helpers: `get_active_scope()`, `get_current_tenant_id()`, `get_current_user_id()`, `get_my_employee_id_v2()`, `get_my_report_ids()`, `is_admin_scope()`.

| Table | Columns (bold = commonly mis-referenced) |
|-------|---------|
| `employees` | id, givenName, surname, displayName, mail, **sso_user_id**, **team_id**, tenant_id, department_id, location_id, jobTitle, current_salary, tax_id, employment_status, employeeType, employeeHireDate, +40 more (see types.ts) |
| `employee_directory` (view) | All `employees` columns except: **current_salary** (masked unless admin/self/manager), **social_security_number**, **tax_id**, **bank_account_last4**, **payroll_id** (all masked unless admin/self). **BUG: missing `SECURITY INVOKER` — anon can read (FIX 9).** |
| `review_participants` | id, cycle_id, employee_id, reviewer_id, self_review_text, self_review_rating, self_review_submitted_at, manager_review_text, manager_review_rating, manager_strengths, manager_areas_for_improvement, manager_review_submitted_at, final_rating, final_comments, status, tenant_id, created_at, updated_at |
| `notifications` | id, **recipient_id**, title, body, type, is_read, read_at, action_url, reference_id, reference_type, tenant_id, created_at |
| `onboarding_templates` | id, **name**, description, is_active, tenant_id, created_at, updated_at |
| `offboarding_templates` | id, **name**, description, is_active, tenant_id, created_at, updated_at |
| `employee_edit_requests` | id, employee_id, requested_by, **requested_changes**, status, reviewed_by, reviewed_at, rejection_reason, tenant_id, created_at, updated_at |
| `social_posts` | id, **author_id**, content, is_system_post, media_urls, view_count, tenant_id, created_at, updated_at |
| `review_cycles` | id, **name**, description, review_type, status, start_date, end_date, self_review_deadline, manager_review_deadline, **created_by**, tenant_id, created_at, updated_at |
| `leave_policies` | id, **leave_type**, **annual_allowance**, accrual_type, max_carryover, min_notice_days, requires_approval, blackout_dates, is_active, location_id, tenant_id, created_at, updated_at |
| `public_holidays` | id, **name**, date, is_recurring, location_id, tenant_id, created_at |
| `internal_changes` | id, employee_id, change_type, summary, old_value, new_value, effective_date, status, **is_applied**, notes, requested_by, approved_by, approved_at, applied_at, rejection_reason, tenant_id, created_at, updated_at |
| `vacation_balances` | id, employee_id, **type**, year, allocated_days, used_days, carried_over, expires_at, tenant_id, created_at, updated_at |
| `vacations` | id, employee_id, sso_user_id, type, start_date, end_date, days_requested, status, approval_step, notes, plan_year, is_withdrawal, original_vacation_id, withdrawal_days, approver_id, approved_at, manager_approved_by, manager_approved_at, hr_processed_by, hr_processed_at, finance_processed_by, finance_processed_at, rejection_reason, tenant_id, created_at, updated_at |

---

## Known bugs (regression test 2026-04-08)

Full fix request details: `/home/bitnami/tmp/lovable_fix_requests_20260408.md`

| # | Bug | Severity | Category |
|---|-----|----------|----------|
| 1 | `employee_id` resolution returns "" — `sso_user_id` not linked in `employees` | CRITICAL | Auth/Data |
| 2 | `notifications` uses `employee_id` — actual column is `recipient_id` | HIGH | Column name |
| 3 | `onboarding_templates` uses `title` — actual column is `name` | HIGH | Column name |
| 4 | `employee_edit_requests` uses `notes` — column doesn't exist | MEDIUM | Column name |
| 5 | `offboarding_templates` RLS allows self/team — should be HR+ only | MEDIUM | RLS permissive |
| 6 | `internal_changes.is_applied` no DEFAULT — returns null instead of `false` | LOW | Schema |
| 7 | `internal_changes` RLS blocks team-scope from reports' changes | MEDIUM | RLS restrictive |
| 8 | `review_cycles` RLS blocks team INSERT (403) | MEDIUM | RLS restrictive |
| 9 | `employee_directory` view readable by anonymous | HIGH | RLS missing |
| 10 | `sso_user_permissions` (SSO) — self can't read own, admin can't read all | HIGH | SSO RLS |
| 11 | Admin `employees.sso_user_id` and `team_id` empty | HIGH | Data linkage |
| 12 | `locations` allows team INSERT — admin-only | LOW | RLS permissive |
| 13 | `document_templates` allows team INSERT — admin-only | LOW | RLS permissive |
| 14 | Vacation self-approval not blocked | MEDIUM | Workflow |
| 15 | `goals` self-scope sees all rows (not own) | HIGH | RLS permissive |
| 16 | Multi-user: broker sees all 92 employees | TEST-FIX (resolved) | Test fix — aligned with directory model |
| 17 | Broker/Staff roles get `cru` instead of `r`/`ru` | HIGH | SSO role config |
| 18 | `locations` returns 0 for org_admin | MEDIUM | RLS restrictive |
| 19 | Vacation finance step doesn't set `finance_processed_at` | MEDIUM | Workflow |
| 20 | `sso_applications` readable by anonymous | HIGH | SSO RLS (accepted risk — see FIX 20 note) |
| 21 | RLS Core `employees` self-scope expects <=1 row (should be tenant-wide) | TEST-FIX (partial) | Test fix — `rls_segregation.sh` updated, `rls.sh` still needs update |
| 22 | `public_holidays` blocks self/team SELECT | MEDIUM | RLS restrictive |
