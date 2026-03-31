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

Start with **[AGENTS.md](AGENTS.md)** — it contains the reading order and navigation map.

#### Quick Reading Order

1. [AGENTS.md](AGENTS.md) — master navigation
2. [docs/platform/app-template.md](docs/platform/app-template.md) — how to build Matrix Apps
3. [docs/data-models/dash-data-model.md](docs/data-models/dash-data-model.md) — practical field reference
4. [docs/INDEX.md](docs/INDEX.md) — full chapter index

#### Raw URL Pattern

To fetch any file via URL:

```
https://raw.githubusercontent.com/sharpsir-group/matrix-platform-kb/main/{path}
```

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
| **[Zoe AI KB](docs/zoe-ai-assistant-kb/)** | Zoe assistant context — client connect, incident reporting |

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
