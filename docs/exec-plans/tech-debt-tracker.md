# Technical Debt Tracker

> Known technical debt organized by domain, with severity and ownership.
> Updated as debt is discovered or resolved. Agents should consult this before
> starting work in a domain to avoid compounding existing issues.

Last reviewed: 2026-04-14

## Severity Scale

| Severity | Meaning |
|----------|---------|
| **P0** | Blocks users or causes data loss — fix immediately |
| **P1** | Causes silent failures or incorrect behavior — fix within current sprint |
| **P2** | Architectural drift or maintainability risk — schedule in next cycle |
| **P3** | Cosmetic or minor inconsistency — fix opportunistically |

## SSO / Auth

| ID | Description | Severity | Owner | Status |
|----|-------------|----------|-------|--------|
| DEBT-SSO-001 | ES256 public key not yet imported into CDL project; dual-token workaround required for CDL PostgREST | P2 | CDTO | Open — tracked in [ADR-011](../architecture/decisions/ADR-011.md) |
| DEBT-SSO-002 | `admin-roles` Edge Function `requireAdmin` guard only checks `scope === 'global'`, not `org_admin` | P1 | CDTO | Mitigated — HRMS bypasses via direct PostgREST query on `sso_roles` |
| DEBT-SSO-003 | Edge Function logs retained only 24h by Supabase; no external log aggregation | P2 | CDTO | Open — Sentry integration planned |

## CDL / Data Layer

| ID | Description | Severity | Owner | Status |
|----|-------------|----------|-------|--------|
| DEBT-CDL-001 | `sso_tenants` requires anon RLS policy workaround because SSO JWT is not recognized by CDL PostgREST | P2 | CDTO | Mitigated — anon SELECT policy added; proper fix is ES256 key import |
| DEBT-CDL-002 | No automated contract testing between CDL schema and 12+ consuming apps | P2 | Data Eng | Open — manual migration review process documented in [testing-strategy.md](../platform/testing-strategy.md) |

## ETL Pipeline

| ID | Description | Severity | Owner | Status |
|----|-------------|----------|-------|--------|
| DEBT-ETL-001 | CDC pipeline logs have no rotation or retention policy (unbounded disk growth) | P3 | Data Eng | Open |
| DEBT-ETL-002 | Multi-source CDC (Hungary, Kazakhstan) not yet on daily cron schedule | P2 | Data Eng | Open |

## Matrix Apps (Lovable-Managed)

| ID | Description | Severity | Owner | Status |
|----|-------------|----------|-------|--------|
| DEBT-APP-001 | HRMS legacy SSO comments reference deprecated `sso_user_permissions` table | P3 | CDTO | Lovable prompt created (`lovable_prompt_legacy_sso_cleanup.md`) |
| DEBT-APP-002 | Frontend CI/CD not yet implemented for any Matrix App (manual build + rsync) | P2 | CDTO | Open — planned in [operations.md](../platform/operations.md) |
| DEBT-APP-003 | No unit or E2E tests in any Lovable-managed app | P2 | CDTO | Open — Vitest + Playwright planned in [testing-strategy.md](../platform/testing-strategy.md) |

## Knowledge Base

| ID | Description | Severity | Owner | Status |
|----|-------------|----------|-------|--------|
| DEBT-KB-001 | No CI pipeline validating KB structure, cross-links, or freshness | P2 | CDTO | Open — `scripts/validate-kb.sh` being created |
| DEBT-KB-002 | `ARCHITECTURE.md` app list slightly out of date (doesn't list all 11 live apps) | P3 | CDTO | Open |

## Resolved Debt

| ID | Description | Resolved | How |
|----|-------------|----------|-----|
| DEBT-SSO-R01 | `update-tenant-settings` deployed on wrong Supabase instance (HRMS instead of CDL) | 2026-04-13 | Redeployed to CDL instance; Lovable prompt updated frontend URL |
| DEBT-SSO-R02 | No tenant switching capability for `system_admin` | 2026-04-13 | `switch-tenant` Edge Function created and deployed |
| DEBT-CDL-R01 | `sso_tenants` inaccessible to anonymous clients (tenant branding broken) | 2026-04-13 | Added `anon_read_active_tenants` RLS policy |

## Cross-Reference

| For | See |
|-----|-----|
| Execution plans | [exec-plans/index.md](index.md) |
| Quality grades | [QUALITY_SCORE.md](../QUALITY_SCORE.md) |
| Architecture decisions | [ADR index](../architecture/decisions/index.md) |
| Testing strategy | [testing-strategy.md](../platform/testing-strategy.md) |
