# Sharp Matrix Platform — Agent Knowledge Map

> Table of contents for the Sharp Matrix Platform knowledge base.
> Deliberately short: each pointer leads to a deeper source of truth.
> Read this first, then navigate to the relevant chapter.

## Platform Identity

**Sharp Matrix** is the **technology platform** powering **Sharp SIR** (Sharp Sotheby's International Realty), a luxury real estate brokerage and SIR-network affiliate currently operating in **Cyprus**, **Hungary**, and **Kazakhstan** (more markets planned). Four module families share the CDL: **CRM** (`matrix-pipeline`, `matrix-comms`, `matrix-client-connect`), **FM** (financial-entries, commissions, deal closings), **HR** (`matrix-hrms`), **MLS** (`matrix-atlas-mls`, `matrix-mls-2-0`, `matrix-cy-website`).

**Built with**: Lovable + Supabase (CDL / system of record) + Databricks (DWH / ETL).
**Practical data model**: RESO DD 2.0 in storage (snake_case canonical names); Dash names projected via `v_dash_*` views.

## For LLMs — Start Here

Before building or modifying any Matrix App:

1. Read `docs/platform/app-template.md` — dual-Supabase, SSO auth, permissions, RLS, UI patterns, token architecture, MLS ingestion, cross-project user display.
2. Determine app type:
   - **CDL-Connected** (listings, contacts, agents, showings) → also read `docs/data-models/cdl-schema.md`, `docs/data-models/dash-data-model.md`, `docs/platform/security-model.md`.
   - **Domain-Specific** (own domain — HR, finance, IT ops) → also read the relevant example repo (see Source Repos below).
3. Read relevant business processes from `docs/business-processes/`.

For the canonical RESO DD 2.0 model (any field, lookup, or FK question), start at `docs/data-models/reso-dd-kb/USAGE.md`. When editing inside that subtree, read its local rules at `docs/data-models/reso-dd-kb/AGENTS.md`.

For new-app auth issues (401/400/403), see `docs/platform/new-app-auth-troubleshooting.md`.

## Subsystem AGENTS.md (local rules)

| Subtree | Local rules |
|---------|-------------|
| `docs/data-models/reso-dd-kb/` | `docs/data-models/reso-dd-kb/AGENTS.md` — phase boundaries, file ownership, mirror politeness, determinism, verification gates |
| `docs/data-models/source-mappings/` | `docs/data-models/source-mappings/AGENTS.md` — phase boundaries, file ownership, hard-fail join gates, determinism |
| `docs/business-processes/canonical-processes/` | `docs/business-processes/canonical-processes/AGENTS.md` — phase boundaries, citation contract, mermaid contract, 5 hard-fail gates |
| `docs/integration/` | `docs/integration/AGENTS.md` — generated per-resource cross-cutting views joining Layers 1–4; emit-only, no hand-edits under `wiki/agent-docs/` |

## Knowledge Base Structure

```
AGENTS.md                              ← This file (TOC, ~110 lines)
README.md
docs/                                   ← KB knowledge layer (system of record)
├── INDEX.md  ARCHITECTURE.md  GOLDEN_PRINCIPLES.md  QUALITY_SCORE.md
├── platform/                          ← App template, security, ops, compliance, app-catalog, ecosystem
├── architecture/                      ← Intelligence layer, data distribution, ADRs
├── data-models/
│   ├── index.md                       ← Data models chapter index (Dash-first hierarchy)
│   ├── dash-data-model.md             ← Dash/Anywhere.com practical field reference
│   ├── reso-dd-kb/                    ← CANONICAL RESO DD 2.0 — start at USAGE.md
│   ├── source-mappings/               ← Dash/Qobrix/SIR -> RESO mapping pipeline
│   ├── cdl-schema.md                  ← Common Data Layer (cross-app data, MLS Sync, lifecycle)
│   ├── etl-pipeline.md                ← Bronze/Silver/Gold ETL
│   ├── property-field-mapping.md      ← Dash ↔ RESO ↔ Qobrix ↔ SIR
│   ├── platform-extensions.md         ← x_sm_* fields not in Dash or RESO DD
│   └── …
├── business-processes/                ← Sharp-SIR pipeline + canonical RESO-aligned process catalogue
│   └── canonical-processes/           ← Vendor-neutral RESO state machines (sibling to Sharp-SIR flavour)
├── integration/                       ← Layer 5: per-resource cross-cutting views (generated)
├── INTEGRATION.md                     ← Master "how the layers compose" navigation aid
├── exec-plans/                        ← Active / completed execution plans, tech-debt tracker
├── product-specs/                     ← Broker dashboard, forms, Kanban, personas
├── references/                        ← API catalogs, integration endpoints
├── vision/                            ← Digital strategy 2026-2028, AI sales model
└── zoe-ai-assistant-kb/               ← Zoe RAG knowledge base
raw/                                    ← Hand-supplied source artifacts
├── dash/                              ← 6 SIR DOCX listing forms
├── qobrix/qobrix_openapi.yaml         ← Qobrix OpenAPI 3.0 spec
├── vision/                            ← Strategy PDFs + ecosystem MMD
└── current-business-practice/         ← Listing checklists (XLSX)
scripts/
└── validate-kb.sh                     ← Mechanical KB validation
```

## Quick Navigation by Task

| If you need to… | Read this |
|---|---|
| Build a new Matrix App (start here) | `docs/platform/app-template.md` |
| Platform / ecosystem / app catalog | `docs/platform/index.md`, `docs/platform/ecosystem-architecture.md`, `docs/platform/app-catalog.md` |
| Strategy, design philosophy, architecture | `docs/vision/digital-strategy-2026-2028.md`, `docs/vision/core-beliefs.md`, `docs/ARCHITECTURE.md` |
| Look up any RESO DD 2.0 resource / field / lookup | `docs/data-models/reso-dd-kb/USAGE.md` |
| When editing inside reso-dd-kb (local rules) | `docs/data-models/reso-dd-kb/AGENTS.md` |
| Canonical RESO DBML / per-resource reference | `docs/data-models/reso-dd-kb/wiki/dbml/canonical.dbml`, `docs/data-models/reso-dd-kb/wiki/agent-docs/resources/<snake>.md` |
| Map a Dash / Qobrix / SIR field to RESO | `docs/data-models/source-mappings/USAGE.md` |
| When editing source-mappings (local rules) | `docs/data-models/source-mappings/AGENTS.md` |
| Look up canonical RESO-aligned MLS process | `docs/business-processes/canonical-processes/USAGE.md` |
| When editing canonical-processes (local rules) | `docs/business-processes/canonical-processes/AGENTS.md` |
| Understand how the four layers compose (data → mapping → canonical process → flavour) | `docs/INTEGRATION.md` |
| Get a one-stop view of "everything about resource X" | `docs/integration/wiki/agent-docs/by_resource/<resource>.md` (start at `docs/integration/wiki/agent-docs/_index.md`) |
| When editing integration/ (local rules) | `docs/integration/AGENTS.md` |
| Dash fields, field mapping, x_sm_* extensions | `docs/data-models/dash-data-model.md`, `docs/data-models/property-field-mapping.md`, `docs/data-models/platform-extensions.md` |
| CDL schema / ETL pipeline / RESO Web API | `docs/data-models/cdl-schema.md`, `docs/data-models/etl-pipeline.md`, `docs/data-models/reso-web-api.md` |
| Auth, roles, permissions, RLS | `docs/platform/security-model.md` |
| ES256 JWT (ADR-011), SSO/CDL Third-Party Auth (ADR-012) | `docs/architecture/decisions/` |
| SSO Edge Function API contracts | `docs/platform/sso-edge-functions.md`, `docs/platform/api-contracts.md` |
| Deploy / operate / perf / mobile / test | `docs/platform/operations.md`, `docs/platform/performance.md`, `docs/platform/mobile-strategy.md`, `docs/platform/testing-strategy.md` |
| Phase-2 AI / Phase-2.5 stewardship roadmaps | `docs/architecture/intelligence-layer.md`, `docs/architecture/data-distribution-and-stewardship.md` |
| Alignment audit / drift / KB methodology | `docs/platform/alignment-audit-playbook.md`, `docs/platform/kb-methodology.md` |
| GDPR, data retention, DSARs | `docs/platform/compliance.md` |
| Engineering invariants, quality grades, exec plans, tech debt | `docs/GOLDEN_PRINCIPLES.md`, `docs/QUALITY_SCORE.md`, `docs/exec-plans/index.md`, `docs/exec-plans/tech-debt-tracker.md` |
| Validate KB structure and links | `scripts/validate-kb.sh` |
| Listing / sales / lead-qual workflow | `docs/business-processes/listing-pipeline.md`, `docs/business-processes/sales-pipeline.md`, `docs/business-processes/lead-qualification.md` |
| Broker dashboard / listing forms / personas | `docs/product-specs/broker-dashboard.md`, `docs/product-specs/sir-listing-forms.md`, `docs/product-specs/personas.md` |
| Qobrix API reference | `docs/references/qobrix-api-summary.md` |
| New app can't auth (401/400/403) | `docs/platform/new-app-auth-troubleshooting.md` |

## For Zoe AI Assistant (1st & 2nd Line Support)

Start at `docs/zoe-ai-assistant-kb/index.md`. For end-user questions, navigate to the relevant app article (`portal.md`, `client-connect.md`, `pipeline.md`, `hrms.md`, `itsm.md`, `financial-management.md`, `comms.md`, `meeting-hub.md`, `platform-sso-auth.md`). For 2nd-line technical questions, see `docs/zoe-ai-assistant-kb/second-line-tech-reference.md`. To author a new article, follow `docs/zoe-ai-assistant-kb/kb-generation-guide.md`.

## Source Repos & Files

| Repo / File | Format | Contents |
|---|---|---|
| `/home/bitnami/matrix-apps-template` | React/TS | App template — dual-Supabase, SSO, permissions, RLS, UI |
| `/home/bitnami/matrix-hrms` | React/TS | HRMS app (Domain-Specific) |
| `/home/bitnami/matrix-pipeline` | React/TS | Pipeline CRM (CDL-Connected) |
| `/home/bitnami/itsm-2-1` | React/TS | ITSM (Domain-Specific) |
| `/home/bitnami/matrix-fm` | React/TS | Financial Management (Domain-Specific) |
| `/home/bitnami/matrix-mls` | React/TS | MLS Listing Management (CDL-Connected) — Cursor-managed, see ADR-013 |
| `/home/bitnami/matrix-atlas-mls` | React/TS | Atlas — MLS Sync admin & Listings Search (CDL-Connected) |
| `/home/bitnami/mls_2_0` | Python/FastAPI | MLS 2.0 pipeline: Databricks ETL + RESO Web API |
| `raw/vision/Sharp-Sothebys-International-Realty.pdf` | PDF | 28-slide digital strategy 2026-2028 |
| `raw/vision/Sarp SIR Platform-2026-02-18-125014.mmd` | Mermaid | Platform ecosystem architecture diagram |
| `raw/vision/AI-driven-model-upravleniya-prodazhami.pdf` | PDF | 16-slide AI-driven sales model |
| `raw/qobrix/qobrix_openapi.yaml` | YAML | Full Qobrix OpenAPI 3.0 spec |
| `docs/data-models/reso-dd-kb/` | Markdown + CSV + DBML | Canonical RESO DD 2.0 (41 resources, 1,745 fields, 222 lookups). Start at `USAGE.md`. |
| `raw/dash/BlankForm_*.docx` | DOCX | SIR/Anywhere.com listing forms (6 types) |
| `raw/current-business-practice/*.xlsx` | XLSX | Listing checklists 2024–2026 |
