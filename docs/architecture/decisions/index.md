# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Sharp Matrix platform. Each ADR documents a significant architectural choice, its context, and consequences.

## ADR Index

| ADR | Title | Status |
|-----|-------|--------|
| [ADR-001](ADR-001.md) | Why Supabase over Firebase/Hasura for CDL | Accepted |
| [ADR-002](ADR-002.md) | Why dual-Supabase (SSO + per-app DB) over schema-based multi-tenancy | Accepted |
| [ADR-003](ADR-003.md) | Why Lovable as the app builder | Accepted |
| [ADR-004](ADR-004.md) | Why Databricks for ETL over dbt/Airbyte/Fivetran | Accepted |
| [ADR-005](ADR-005.md) | Why RESO DD 2.0 as interop layer with Dash as practical core | Accepted |
| [ADR-006](ADR-006.md) | Why FastAPI + OData 4.0 for the RESO Web API | Accepted |
| [ADR-007](ADR-007.md) | Why Edge Functions over traditional backend (Deno runtime) | Accepted |
| [ADR-008](ADR-008.md) | Why 5-level scope hierarchy over simpler RBAC | Accepted |
| [ADR-009](ADR-009.md) | Why medallion architecture (Bronze/Silver/Gold) for ETL | Accepted |
| [ADR-010](ADR-010.md) | Why PM2 + cron over Kubernetes/ECS for pipeline orchestration | Accepted |
| [ADR-011](ADR-011.md) | ES256 JWT Signing — Migration from HS256 | Accepted (in progress) |
| [ADR-012](ADR-012.md) | Dedicated Matrix CDL Supabase project (separate from SSO) | Accepted |
| [ADR-013](ADR-013.md) | `matrix-platform-foundation` owns both SSO and CDL projects | Accepted |
| [ADR-014](ADR-014.md) | Unified MLS ingestion pipeline (sources → staging → merge) | Accepted |
| [ADR-015](ADR-015.md) | CDL Pipeline EF Surface — broker-scope CRUD for Matrix Pipeline | Proposed (largely folded into ADR-016) |
| [ADR-016](ADR-016.md) | Canonical-into-CDL acceleration for matrix-pipeline 2.0 | Accepted |
| [ADR-017](ADR-017.md) | Browser SSO token storage — localStorage now, BFF/httpOnly remediation path | Accepted |
| [ADR-018](ADR-018.md) | SSO issuer URL + Supabase Third-Party Auth for own-DB apps (ES256 completion) | Accepted |
| [ADR-019](ADR-019.md) | Server-managed PKCE for first-party public clients (webview-proof login) | Accepted |
| [ADR-020](ADR-020.md) | Per-tenant, per-locale UI label/terminology overrides (tenant_key axis + `App.*` namespace + Hungarian) | Accepted |
| [ADR-021](ADR-021.md) | Runtime DB-driven i18n: single bundled English baseline + CDL `app_ui_strings` corpus + `app-i18n` EF (platform standard) | Accepted |
| [ADR-022](ADR-022.md) | Buyer-to-showing linkage as a Sharp Matrix platform extension (`x_contact_key`) | Accepted |
| [ADR-023](ADR-023.md) | Platform extension prefix `x_` (supersedes `x_sm_`) | Accepted |
| [ADR-024](ADR-024.md) | CDL lookup-value normalization layer (canonical RESO StandardValues) | Accepted |
| [ADR-025](ADR-025.md) | Referral + Document as project-flavour CDL resources; offer-economics deferred (zero-`x_`) | Accepted |
| [ADR-026](ADR-026.md) | Event-sourced transaction model on canonical homes; Pipeline owns the Property transaction phase | Accepted |
| [ADR-027](ADR-027.md) | Console-managed Third-Party Auth provisioning for own-DB apps | Accepted |
| [ADR-028](ADR-028.md) | CRM-internal Commission Engine (ERP-lite); app-private, per-country rules, role-config + JWT-scope authz, Finance-ERP reconciliation | Accepted |
| [ADR-029](ADR-029.md) | "Contract agreed" = Pending edge; close = settlement; pipeline stage projection; per-country collection anchor | Accepted |
| [ADR-030](ADR-030.md) | Promote transaction linkage from `HistoryTransactional.raw` to a governed `x_transaction_key` extension | Proposed |