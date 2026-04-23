# Quality Scorecard

> Grades each platform domain and architectural layer. Agents should consult
> this to understand where the platform is strong, where gaps exist, and where
> to focus improvement effort.
>
> Grading is subjective but informed by concrete criteria (see scale below).
> Update this file when domains improve or regress.

Last reviewed: 2026-04-14

## Grading Scale

| Grade | Meaning |
|-------|---------|
| **A** | Production-ready, well-tested, well-documented, low debt |
| **B** | Functional and deployed, minor gaps in testing or docs |
| **C** | Working but fragile — missing tests, known workarounds, incomplete docs |
| **D** | Prototype or blocked — significant gaps, not production-safe without fixes |

## Criteria

Each domain is graded across four dimensions:

| Dimension | What It Measures |
|-----------|-----------------|
| **Docs** | KB coverage — are the relevant docs accurate, complete, and cross-linked? |
| **Tests** | Automated test coverage — unit, integration, E2E, contract |
| **Reliability** | Known bugs, workarounds, incident history |
| **Architecture** | Clean boundaries, no hacks, follows golden principles |

## Platform Infrastructure

| Domain | Docs | Tests | Reliability | Architecture | Overall | Notes |
|--------|------|-------|-------------|--------------|---------|-------|
| SSO / Auth (Edge Functions) | A | C | B | B | **B** | 38 Edge Functions documented; no automated tests; ES256 migration in progress |
| CDL Schema & RLS | B | C | B | B | **B** | RLS patterns well-documented (A-E); no automated contract tests across 12+ apps |
| Dual-Supabase Architecture | A | — | B | A | **A-** | Well-documented in app-template; token architecture has known workaround (dual-token) |
| Databricks ETL Pipeline | A | C | B | A | **B+** | Medallion architecture well-documented; CDC runs daily; no automated validation tests |
| RESO Web API | B | C | B | A | **B** | OData 4.0 documented; PM2 managed; limited health checks |

## Matrix Apps (Lovable-Managed)

| App | Docs | Tests | Reliability | Architecture | Overall | Notes |
|-----|------|-------|-------------|--------------|---------|-------|
| Agency Portal | B | D | B | B | **C+** | Live, in use; no tests; limited KB coverage |
| Client Connect | B | D | B | B | **C+** | Live; no tests; Zoe KB article exists |
| Meeting Hub | B | D | B | B | **C+** | Live; no tests; Zoe KB article exists |
| Matrix Comms (WhatsApp) | B | D | B | B | **C+** | Live; no tests; Zoe KB article exists |
| HRMS | A | D | B | B | **B-** | Extensive KB (Zoe + UAT plan); no automated tests; recent SSO cleanup |
| Matrix Pipeline | B | D | C | B | **C** | In progress; CDL-Connected; Zoe KB article exists |
| ITSM | B | D | C | B | **C** | In progress; Zoe KB article exists |
| Matrix FM | B | D | C | B | **C** | In progress; Zoe KB article exists |
| MLS Listing Mgmt | B | D | C | B | **C** | In progress; CDL-Connected with 18 tables |

## Knowledge Base

| Area | Docs | Tests | Reliability | Architecture | Overall | Notes |
|------|------|-------|-------------|--------------|---------|-------|
| KB Structure | A | D | B | A | **B+** | Progressive disclosure, LLM-first, cross-refs; no CI validation |
| ADRs | A | — | A | A | **A** | 11 decisions documented with context and consequences |
| Business Processes | A | — | B | A | **A-** | 5 docs covering both pipelines, qualification, checklists |
| Data Models | A | C | B | A | **A-** | 10+ docs; data contracts defined but not enforced in CI |
| Product Specs | B | — | B | B | **B** | 7 docs; some specs are aspirational (Phase 4+) |
| Zoe AI Assistant KB | A | — | B | A | **A-** | 13 articles covering all live apps + generation guide |

## Improvement Priorities

Based on the scores above, the highest-impact improvements are:

| Priority | Domain | Current | Target | Action |
|----------|--------|---------|--------|--------|
| P1 | App testing (all apps) | D | C | Add Vitest + Playwright to `matrix-apps-template`; smoke tests for auth flow |
| P1 | KB CI validation | D | B | Deploy `scripts/validate-kb.sh` in GitHub Actions |
| P2 | CDL contract testing | C | B | Automated schema diff on migration PRs |
| P2 | SSO Edge Function tests | C | B | Integration tests with mock JWTs |
| P2 | ES256 key import | — | — | Complete [ADR-011](architecture/decisions/ADR-011.md); eliminates dual-token workaround |
| P3 | ETL log retention | — | — | Add log rotation to CDC pipeline scripts |

## Cross-Reference

| For | See |
|-----|-----|
| Technical debt details | [exec-plans/tech-debt-tracker.md](exec-plans/tech-debt-tracker.md) |
| Testing strategy | [platform/testing-strategy.md](platform/testing-strategy.md) |
| Golden principles | [GOLDEN_PRINCIPLES.md](GOLDEN_PRINCIPLES.md) |
| KB methodology | [platform/kb-methodology.md](platform/kb-methodology.md) |
