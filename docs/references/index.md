# Chapter 6: References — Index

> Raw API catalogs, data dictionary summaries, source repositories, and live endpoints.
> These are **reference and migration sources** for the Sharp Matrix Platform —
> not the platform itself. The canonical data layer is RESO DD 2.0.

## Documents

| Document | What It Contains | Role |
|----------|-----------------|------|
| [qobrix-api-summary.md](qobrix-api-summary.md) | All 83 Qobrix API resource groups and 149 schemas | Reference: current CRM capabilities to replicate |
| [reso-dd-fields-summary.md](reso-dd-fields-summary.md) | RESO DD 2.0 resource names, key fields, and lookup categories | Canonical: the standard Sharp Matrix builds on |

## Source Repositories

| Repo | Path | Purpose |
|------|------|---------|
| **matrix-apps-template** | `/home/bitnami/matrix-apps-template` | App starter kit: dual-Supabase, SSO, permissions, RLS, UI conventions |
| **matrix-hrms** | `/home/bitnami/matrix-hrms` | Working example: Domain-Specific app (25+ tables, 30+ hooks) |
| **mls_2_0** | `/home/bitnami/mls_2_0` | Data pipeline: Databricks ETL (Bronze/Silver/Gold) + RESO Web API |

## Live Endpoints

| Endpoint | URL | Auth | Purpose |
|----------|-----|------|---------|
| RESO Web API | `https://{host}:3900/reso` | OAuth 2.0 Client Credentials | OData 4.0 access to gold layer data |
| HomeOverseas Export | `https://{host}:3900/export/homesoverseas.xml` | Public | Cyprus listings XML feed |

## Supabase Project References

Supabase projects are split across two organizations:

- **`Sharp SIR Group`** (Pro) — platform core (**Matrix SSO**, **Matrix CDL-MLS**) + target home for customer-facing sites (HU, CY). New project provisioning for platform/sites goes here.
- **`SharpMatrix`** (Pro) — hosts per-app DBs (Pipeline, HRMS, FM, MLS app, ITSM) and the CY prod project (under review). Also contains several legacy / dangling projects slated for cleanup (see "Cleanup candidates" below).

### Org `Sharp SIR Group` (platform core + site targets)

| Name | Project ID | Role |
|------|-----------|------|
| **Matrix SSO** | `xgubaguglsnokjyudgvc` | Identity only: Auth, RBAC, Tenants, AD Users (ADR-012). Nano, `eu-west-1` (Ireland). **Active** (~230k req / 7 days; last migration `fix_sso_roles_and_rls`). Owner: `matrix-platform-foundation/supabase/`. |
| **Matrix CDL-MLS** | `ofzcokolkeejgqfjaszq` | Consolidated CDL + MLS backend (Micro, `eu-central-1` Frankfurt). Empty so far (0 migrations, ~18 req / 7 days). Will own shared `mls_*` tables + ingestion control plane (`reso-import` / `csv-import` / `crm-import` / `listing-merge`) per ADR-012/013/014, plus the MLS data currently served by Databricks `mls_2_0` RESO Web API. Owner: `matrix-platform-foundation/supabase-cdl/` (may be renamed `supabase-cdl-mls/`). See Matrix-CICD §7.3. |
| **HU Website 1GH — prod** | TBD (to be provisioned) | Target prod Supabase for `sothebys-realty.hu`. Recommended region: `eu-central-1`. See Matrix-CICD §0.1. |
| **HU Website 1GH — staging** | TBD (to be provisioned) | Target staging Supabase for `sothebys-realty.hu`. Recommended region: `eu-central-1`. See Matrix-CICD §0.1. |
| **CY Website 2.0 — prod** | TBD (to be provisioned) | Target prod Supabase for CY SPA (after legacy-PHP cutover). See Matrix-CICD §0.3 / §5.2. |
| **CY Website 2.0 — staging** | TBD (to be provisioned) | Target staging Supabase for CY SPA. See Matrix-CICD §0.3. |

> **Regional note:** the org is regionally mixed — SSO is in `eu-west-1` (historical, not being moved), CDL-MLS is in `eu-central-1`. New HU/CY projects should go to `eu-central-1` for latency parity with Budapest / Nicosia and the AWS `eu-central-1` prod HU VM.

### Org `SharpMatrix` (per-app DBs + under-review)

> ⚠ Org membership of the per-app DBs below is **assumed from historical KB entries**; only `Matrix SSO` and `Matrix CDL-MLS` have been verified against the live dashboard. Run `supabase projects list` to confirm each row and update this file.

| Name | Project ID | Role |
|------|-----------|------|
| **Matrix MLS app DB** | `wckwfbbqiupvallmhqbu` | `matrix-mls` application DB (role_configurations, app-local). Org unverified. |
| **Matrix Pipeline app DB** | `mydojctcewxrbwjckuyz` | Matrix Pipeline CRM application DB. Org unverified. |
| **Matrix HRMS app DB** | `wltuhltnwhudgkkdsvsr` | HR Management System (domain-specific app). Org unverified. |
| **Matrix FM app DB** | `retujkznogwplfrbniet` | Matrix FM (Financial Management) app DB. Org unverified. |
| **ITSM app DB** | `irjrcskfcyierdbefrpk` | ITSM app DB. Org unverified. |
| **CY Web Site** | `yugymdytplmalumtmyct` | Cyprus real estate prod project. Under review — may move to `Sharp SIR Group` alongside CY staging migration; see Matrix-CICD §0.3. |

### Cleanup candidates (org `SharpMatrix`)

These projects exist in `SharpMatrix` but should be decommissioned per Matrix-CICD §0.1 / §0.3 / §0.4:

| Name | Project ID | Status |
|------|-----------|--------|
| **Sergey Lobov personal sandbox** (displayed as `SharpMatrix`, Nano, `eu-north-1`) | `tiuansahlsgautkjsajk` | ⚠ HU staging + prod currently both point here (hardcoded in `1gh-of-hungary-sotheby-s-website/src/integrations/supabase/client.ts` on `main`). **~32–33k req/24h** from HU. Migrate HU to new `HU Website 1GH` projects in `Sharp SIR Group`, then rotate keys; project remains as Sergey's personal sandbox (not for any Matrix App/site). Matrix-CICD §0.1. |
| **HU Website 1GH (dangling)** | `iooyncgcumgecznfpnsk` | Nano, `eu-north-1`. Provisioned for HU but never connected (~8 req/60 min — idle). **Candidate for deletion** after HU cutover to `Sharp SIR Group`. Matrix-CICD §0.1. |
| **CSIR Website 2.0 (CY SPA staging)** | `rlfxsieleseimylumhwc` | Micro, **`eu-west-1` Ireland**. Current CY SPA staging backend. Migrate edge/schema/data → new `CY Website 2.0 — staging` in `Sharp SIR Group`, then **delete**. Matrix-CICD §0.3. |
| **websites-matrix-staging (empty)** | `hxbzyfadhwzlvfjgqase` | Micro, **`eu-central-2` Zurich**. 0 migrations / 0 req / 0 branches — never used. **Delete**. Matrix-CICD §0.4. |

### Other

| Name | Project ID | Role |
|------|-----------|------|
| **Lovable Source** | `ibqheiuakfjoznqzrpfe` | Development source (read-only) |

## Raw Source Files

| File | Where | Role in Sharp Matrix |
|------|-------|---------------------|
| `reso dd/RESO_Data_Dictionary_2.0.xlsx` | Fields + Lookups + Version sheets | **Canonical** — full field definitions and lookup values for the platform data layer |
| `reso dd/RESO_Data_Dictionary_1.7.xlsx` | Previous DD version | Reference for backward compatibility |
| `qobrix/qobrix_openapi.yaml` | 68,000+ lines OpenAPI 3.0 spec | **Migration source** — current CRM API, use for data migration and capability reference |
| `dash/BlankForm_*.docx` | 6 SIR/Anywhere.com form templates | **Reference** — broker-facing field requirements from Sotheby's International Realty |

## Reference Source Roles

| Source | What It Tells Us | How Sharp Matrix Uses It |
|--------|-----------------|-------------------------|
| **RESO DD 2.0** | Standard field names, types, lookups for real estate data | Canonical data layer — all CDL-Connected apps use these names |
| **Qobrix CRM** | Current entity schema, API patterns, workflow capabilities | Migration source + capability reference (being decommissioned) |
| **SIR / Anywhere.com** | What fields brokers need on listing forms | Field requirements reference — ensures coverage |
| **matrix-apps-template** | Tech stack, auth flow, permissions, RLS patterns | Blueprint for every Matrix App built by Lovable |
| **matrix-hrms** | Real app implementation: domain tables, hooks, workflows | Working example of a Domain-Specific app |
| **mls_2_0** | Data pipeline, ETL, RESO Web API | Data infrastructure — feeds Supabase CDL |
