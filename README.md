<p align="center">
  <a href="https://sharpsir.group">
    <img src="https://raw.githubusercontent.com/sharpsir-group/.github/main/brand/logo-blue.png" alt="Sharp Sotheby's International Realty" width="400" />
  </a>
</p>

<h3 align="center">Matrix Platform Knowledge Base</h3>

<p align="center">
  LLM-readable knowledge base for the Sharp Matrix digital platform — architecture, data models,<br />
  business processes, and RESO DD mapping for luxury real estate brokerage.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/RESO_DD_2.0-1A1A2E?style=flat&logoColor=white" alt="RESO" />
  <img src="https://img.shields.io/badge/OData_4.0-0078D4?style=flat&logo=odata&logoColor=white" alt="OData" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat&logo=supabase&logoColor=white" alt="Supabase" />
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white" alt="Databricks" />
  <img src="https://img.shields.io/badge/React_18-61DAFB?style=flat&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Lovable-FF6B6B?style=flat&logo=heart&logoColor=white" alt="Lovable" />
  <img src="https://img.shields.io/badge/shadcn/ui-000000?style=flat&logo=shadcnui&logoColor=white" alt="shadcn/ui" />
  <img src="https://img.shields.io/badge/OAuth_2.0_+_PKCE-EB5424?style=flat&logo=auth0&logoColor=white" alt="OAuth" />
  <img src="https://img.shields.io/badge/Delta_Lake-003366?style=flat&logo=delta&logoColor=white" alt="Delta Lake" />
</p>

---

### What Is This?

This repository is the **single source of truth** for everything about the Sharp Matrix platform. It's designed to be consumed by both humans and LLMs — every doc is structured for quick navigation, deep linking, and AI-assisted development.

Whether you're building a new Matrix App, mapping RESO fields, or understanding how the 24-app ecosystem fits together — start here.

### For AI Agents (Lovable, Cursor, Copilot)

Start with **[AGENTS.md](AGENTS.md)** — it contains the reading order and navigation map for building and extending Matrix Apps.

#### Quick Reading Order

1. [AGENTS.md](AGENTS.md) — master navigation
2. [docs/platform/app-template.md](docs/platform/app-template.md) — how to build Matrix Apps
3. [docs/data-models/dash-data-model.md](docs/data-models/dash-data-model.md) — practical field reference
4. [docs/INDEX.md](docs/INDEX.md) — full chapter index

#### Raw URL Pattern

```
https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/{path}
```

### For Zoe — Our First AI Employee

**Zoe** is Sharp Matrix's AI-powered assistant — not a chatbot, but a full-time digital colleague who fills multiple roles across the organization:

| Role | What Zoe Does |
|---|---|
| **1st Line Tech Support** | Helps brokers, managers, and staff troubleshoot platform issues, guides incident reporting |
| **Onboarding Assistant** | Walks new employees through Sharp Matrix apps, explains workflows, answers "how do I…?" questions |
| **Sales Coach** | Provides brokers with next-best-action suggestions, lead qualification tips, and deal pipeline insights |
| **Operations Guide** | Explains cross-app workflows — client lifecycle, daily routines by role, data flow between apps |
| **Platform Expert** | Knows every app, every field, every business process — from Client Connect to Financial Management |

Zoe's knowledge base lives in [`docs/zoe-ai-assistant-kb/`](docs/zoe-ai-assistant-kb/) — 15 structured documents covering all platform apps, designed for RAG retrieval:

| Document | Covers |
|---|---|
| [platform-overview.md](docs/zoe-ai-assistant-kb/platform-overview.md) | All apps at a glance, getting started, cross-app troubleshooting |
| [client-connect.md](docs/zoe-ai-assistant-kb/client-connect.md) | Client registration, verification, MLS duplicates, approval workflow |
| [pipeline.md](docs/zoe-ai-assistant-kb/pipeline.md) | Leads, deal pipeline, contacts, MLS data, M365 email/calendar |
| [comms.md](docs/zoe-ai-assistant-kb/comms.md) | WhatsApp messaging, templates, campaigns, AI replies |
| [hrms.md](docs/zoe-ai-assistant-kb/hrms.md) | Employee directory, vacations, onboarding/offboarding, performance |
| [itsm.md](docs/zoe-ai-assistant-kb/itsm.md) | IT service desk, assets, software licenses, vendors |
| [financial-management.md](docs/zoe-ai-assistant-kb/financial-management.md) | Monthly/annual reporting, budgeting, planning, CORE allocation |
| [cross-app-workflows.md](docs/zoe-ai-assistant-kb/cross-app-workflows.md) | Client lifecycle, daily routines by role, data flow between apps |
| [incident-reporting.md](docs/zoe-ai-assistant-kb/incident-reporting.md) | How to report an incident — severity guide, escalation path |
| [second-line-tech-reference.md](docs/zoe-ai-assistant-kb/second-line-tech-reference.md) | Architecture deep-dive for 2nd line support analysts |
| [kb-generation-guide.md](docs/zoe-ai-assistant-kb/kb-generation-guide.md) | How to generate a KB article for any new Matrix app |

### Platform Overview

```
Matrix Apps ── built from a shared App Template (React + Vite + shadcn/ui)
  │
  ├── CDL-Connected Apps ─── Pipeline, Contact Mgmt, Broker Dashboard
  │      read/write shared RESO DD 2.0 data layer
  │
  ├── Domain-Specific Apps ── HRMS, Financial Mgmt, ITSM
  │      own Supabase databases, shared SSO auth
  │
  └── AI Services ── Zoe Assistant, AI Web Chat, Blog Generator
         context-aware copilots for brokers, managers, and visitors
  │
  ▼
Supabase (CDL + Auth)  ◄──►  Databricks (DWH + ETL)  ◄──►  MLS / Portals
```

**24 apps** in the ecosystem — 11 live, 7 in progress, 6 planned.

### What's Inside

| Section | Contents |
|---|---|
| **[Platform](docs/platform/)** | App template, tech stack, dual-Supabase architecture, MLS datamart |
| **[Data Models](docs/data-models/)** | Dash field reference, RESO interop mapping, ETL pipeline schema |
| **[Business Processes](docs/business-processes/)** | Listing pipeline, sales pipeline, lead qualification workflows |
| **[Product Specs](docs/product-specs/)** | UI specs — dashboards, forms, Kanban boards |
| **[Vision](docs/vision/)** | Digital strategy 2026–2028, AI sales model |
| **[References](docs/references/)** | API catalogs, field summaries, integration endpoints |
| **[Zoe AI KB](docs/zoe-ai-assistant-kb/)** | Zoe's knowledge base — 15 docs covering all apps, workflows, troubleshooting, RAG-ready |

### Repository Structure

```
AGENTS.md                    ← Entry point for LLMs
README.md                    ← This file
docs/
  INDEX.md                   ← Master index with chapter summaries
  ARCHITECTURE.md            ← System architecture
  platform/                  ← Platform overview, app template, MLS datamart
  data-models/               ← Dash data model, RESO interop, ETL pipeline
  business-processes/        ← Listing pipeline, sales pipeline, lead qualification
  product-specs/             ← UI specs: dashboards, forms, Kanban
  vision/                    ← Digital strategy 2026-2028, AI sales model
  references/                ← API catalogs, field summaries
  zoe-ai-assistant-kb/       ← Zoe assistant knowledge base
dash/                        ← SIR/Anywhere.com listing forms (DOCX)
qobrix/                      ← Qobrix OpenAPI spec (YAML)
reso dd/                     ← RESO Data Dictionary spreadsheets (XLSX)
vision/                      ← Strategy PDFs and architecture diagrams
current busienss practice/   ← Operational checklists (XLSX)
```

### Key Concepts

| Concept | Role |
|---|---|
| **Dash/Anywhere.com** | Practical core data model — field names apps use day-to-day |
| **RESO DD 2.0** | Interoperability standard — syndication, external APIs, MLS |
| **Supabase** | Common Data Layer — system of record for all apps |
| **Databricks** | DWH & ETL engine — Bronze/Silver/Gold medallion architecture |
| **Lovable** | AI app builder — all Matrix Apps are generated and maintained here |
| **SSO** | 5-level scope, CRUD permissions, dual-Supabase architecture |
| **CDL** | Common Data Layer — shared RESO-standard tables across CDL-Connected apps |

### Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, TypeScript, shadcn/ui, Tailwind CSS, Radix UI |
| Auth & IAM | OAuth 2.0 + PKCE, custom JWT, HMAC-SHA256, 5-level RBAC |
| Backend | Supabase Edge Functions (Deno), PostgreSQL 15, Row-Level Security |
| Data Standard | RESO DD 2.0 — canonical data layer, OData 4.0 Web API |
| Data Pipeline | Databricks — Medallion ETL (Bronze → Silver → Gold), CDC, Delta Lake |
| AI/ML | LangChain, RAG, semantic search, lead scoring, GPT-4, Claude, Gemini, Qwen3 |
| Channels | WhatsApp (Twilio), Microsoft Graph, SMTP/IMAP |
| Infra | Self-hosted Linux, Apache, PM2, Node.js, Python 3.13 |

### External Resources

- [RESO Data Dictionary 2.0](https://ddwiki.reso.org/display/DDW20/)
- [OData 4.0 Specification](https://www.odata.org/documentation/)
- [Supabase Documentation](https://supabase.com/docs)
- [Databricks Documentation](https://docs.databricks.com/)
- [Lovable Documentation](https://docs.lovable.dev/)

---

<p align="center">
  <sub>Part of the <a href="https://github.com/sharpsir-group"><strong>Sharp Matrix</strong></a> platform · <a href="https://sharpsir.group">sharpsir.group</a></sub>
</p>
