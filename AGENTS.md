# Sharp Matrix Platform — Agent Knowledge Map

> This file is the **table of contents** for the Sharp Matrix Platform knowledge base.
> It is deliberately short. Each pointer leads to a deeper source of truth in `docs/`.
> When working in this repository, read this file first, then navigate to the relevant chapter.

## For Lovable — Start Here

Before building ANY Matrix App:

1. Read `docs/platform/app-template.md` — how apps are built (dual-Supabase, SSO, permissions, RLS, UI patterns)
2. Determine app type: **CDL-Connected** (Dash tables) or **Domain-Specific** (own tables)
3. If CDL-Connected: read `docs/data-models/dash-data-model.md` for field names (practical core)
4. Read the relevant `docs/business-processes/` doc for your feature's workflow logic
5. For syndication/exports: use the RESO mapping column in `dash-data-model.md`
6. For SSO security: read `/home/bitnami/matrix-platform-foundation/SECURITY_MODEL.md`

## Platform Identity

**Sharp Matrix** is the multi-app digital platform for **Sharp Sotheby's International Realty** —
luxury real estate brokerage operating in Cyprus, Hungary, and Kazakhstan.

**Built with**: Lovable (app builder) + Supabase (CDL / system of record) + Databricks (DWH / ETL).
**Practical data model**: Dash/Anywhere.com — CDL-Connected apps use Dash field names.
**Interop standard**: RESO DD 2.0 — used for syndication and external APIs.
**App template**: `matrix-apps-template` — defines stack, auth, permissions, UI patterns.
**Strategic goal**: Matrix Apps replace Qobrix CRM. Dash flips from pull to push (syndication).

## Knowledge Base Structure

```
docs/
├── platform/
│   ├── index.md                      ← Platform overview & three-platform architecture
│   ├── app-template.md              ← How to build Matrix Apps (Lovable must read first)
│   ├── mls-datamart.md              ← MLS 2.0 data pipeline & phased migration roadmap
│   ├── ecosystem-architecture.md     ← Full ecosystem: channels, apps, data, AI/ML
│   └── app-catalog.md               ← All platform apps: purpose, users, RESO resources
├── INDEX.md                          ← Master index with chapter summaries
├── ARCHITECTURE.md                   ← System architecture & technology map
├── vision/
│   ├── index.md                      ← Vision chapter index
│   ├── digital-strategy-2026-2028.md ← Digital strategy: 3 markets, 7 phases, KPIs
│   ├── ai-driven-sales-model.md      ← AI-driven sales management model (16 elements)
│   └── core-beliefs.md              ← Operating principles & design philosophy
├── data-models/
│   ├── index.md                      ← Data models chapter index (Dash-first hierarchy)
│   ├── dash-data-model.md           ← Dash/Anywhere.com practical data model (START HERE)
│   ├── reso-dd-overview.md           ← RESO DD 2.0 — interop standard for syndication
│   ├── reso-canonical-schema.md      ← Which RESO resources/fields map to Dash
│   ├── platform-extensions.md        ← All x_sm_* fields not in Dash or RESO DD
│   ├── etl-pipeline.md              ← Bronze/Silver/Gold ETL pipeline architecture
│   ├── reso-web-api.md              ← RESO Web API (OData 4.0) endpoint reference
│   ├── qobrix-data-model.md          ← Qobrix CRM reference & migration source
│   └── property-field-mapping.md     ← Field mapping: Dash ↔ RESO ↔ Qobrix ↔ SIR
├── business-processes/
│   ├── index.md                      ← Business processes chapter index
│   ├── listing-pipeline.md           ← Seller-side pipeline (8 stages)
│   ├── sales-pipeline.md             ← Buyer-side pipeline (8 stages)
│   ├── lead-qualification.md         ← MQL → SQL qualification with BANT
│   ├── follow-up-vs-active-sales.md  ← Nurturing vs active deal boundary
│   └── listing-checklist.md          ← Operational checklists (broker/marketing/finance)
├── product-specs/
│   ├── index.md                      ← Product specs chapter index
│   ├── sir-listing-forms.md          ← SIR/Anywhere.com form field specifications
│   ├── broker-dashboard.md           ← AI-powered broker dashboard design
│   └── manager-kanban.md             ← Manager pipeline & Kanban views
├── references/
│   ├── index.md                      ← References chapter index
│   ├── qobrix-api-summary.md         ← Qobrix OpenAPI resource catalog
│   └── reso-dd-fields-summary.md     ← RESO DD 2.0 field & lookup summary
```

## Quick Navigation by Task

| If you need to…                              | Read this                                         |
|----------------------------------------------|---------------------------------------------------|
| Build a new Matrix App (start here)          | `docs/platform/app-template.md`                   |
| Understand the Sharp Matrix platform          | `docs/platform/index.md`                          |
| See the full ecosystem architecture           | `docs/platform/ecosystem-architecture.md`         |
| Understand the data pipeline (MLS 2.0)        | `docs/platform/mls-datamart.md`                   |
| Know which apps exist and what they do        | `docs/platform/app-catalog.md`                    |
| Understand the 2026-2028 strategy & roadmap   | `docs/vision/digital-strategy-2026-2028.md`       |
| Understand the AI-driven sales model          | `docs/vision/ai-driven-sales-model.md`            |
| Know the design philosophy                    | `docs/vision/core-beliefs.md`                     |
| See how systems connect                       | `docs/ARCHITECTURE.md`                            |
| See Dash field names for app development       | `docs/data-models/dash-data-model.md`             |
| Map a property field across systems            | `docs/data-models/property-field-mapping.md`      |
| See which RESO fields map to Dash              | `docs/data-models/reso-canonical-schema.md`       |
| Find or add a platform extension (x_sm_*)     | `docs/data-models/platform-extensions.md`         |
| Understand the ETL pipeline (Bronze→Gold)     | `docs/data-models/etl-pipeline.md`                |
| Use the RESO Web API (OData)                  | `docs/data-models/reso-web-api.md`                |
| Understand Qobrix entities & migration        | `docs/data-models/qobrix-data-model.md`           |
| Understand RESO DD 2.0 (interop standard)      | `docs/data-models/reso-dd-overview.md`            |
| Understand SSO security model                  | `/home/bitnami/matrix-platform-foundation/SECURITY_MODEL.md` |
| Build a listing workflow                      | `docs/business-processes/listing-pipeline.md`     |
| Build a buyer/sales workflow                  | `docs/business-processes/sales-pipeline.md`       |
| Implement lead scoring / qualification        | `docs/business-processes/lead-qualification.md`   |
| Design the broker dashboard UI                | `docs/product-specs/broker-dashboard.md`          |
| Design listing input forms                    | `docs/product-specs/sir-listing-forms.md`         |
| Look up Qobrix API endpoints                  | `docs/references/qobrix-api-summary.md`           |
| Look up RESO standard field names             | `docs/references/reso-dd-fields-summary.md`       |

## Source Repos & Files

| Repo / File | Format | Contents |
|------------|--------|---------|
| `/home/bitnami/matrix-apps-template` | React/TS | App template: dual-Supabase, SSO, permissions, RLS, UI |
| `/home/bitnami/matrix-hrms` | React/TS | Example app: HRMS (25+ tables, 30+ hooks, domain-specific) |
| `/home/bitnami/mls_2_0` | Python/FastAPI | MLS 2.0 pipeline: Databricks ETL + RESO Web API |
| `vision/Sharp-Sothebys-International-Realty.pdf` | PDF | Full 28-slide digital strategy 2026-2028 |
| `vision/Sarp SIR Platform-2026-02-18-125014.mmd` | Mermaid | Platform ecosystem architecture diagram |
| `vision/AI-driven-model-upravleniya-prodazhami.pdf` | PDF | 16-slide AI-driven sales model |
| `qobrix/qobrix_openapi.yaml` | YAML | Full Qobrix OpenAPI 3.0 spec (68K lines) |
| `reso dd/RESO_Data_Dictionary_2.0.xlsx` | XLSX | RESO DD 2.0 (Fields + Lookups) |
| `reso dd/RESO_Data_Dictionary_1.7.xlsx` | XLSX | RESO DD 1.7 (historical reference) |
| `dash/BlankForm_*.docx` | DOCX | SIR/Anywhere.com listing forms (6 types) |
| `current busienss practice/*.xlsx` | XLSX | Listing checklists 2024–2026 |
