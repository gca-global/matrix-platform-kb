# Chapter 5: Product Specifications — Index

> Per-app product specs. The `matrix-pipeline/` subtree is the only CRM home.

## Documents

| Document | What It Contains |
|----------|-----------------|
| [matrix-pipeline/INDEX.md](matrix-pipeline/INDEX.md) | **Matrix Pipeline 2.0 — CRM LLM Wiki** (single source of truth). 8 wiki pages (overview / architecture / entities / processes / requirements / ai / integration / commission-engine) + `phases.md` 8-week atomic build plan + `cdl-crud-contract.md` + immutable `raw/context-v2.md` BRD. Strictly canonical RESO DD 2.0 with two documented escape hatches: `Referral` entity + CRM-internal Commission Engine. |
| [matrix-stardom.md](matrix-stardom.md) | **Matrix Stardom** — shared prompt workspace: prompt library + curation, scheduled prompt automations (`prompt-scheduler` EF + hourly `pg_cron`), and engagement-driven "Most popular" ranking |
| [client-portal.md](client-portal.md) | **Matrix Portal** — buyer/seller self-service portal spec |
| [marketing-platform.md](marketing-platform.md) | **Matrix Marketing** — campaign management, audience segmentation, distribution, ROI attribution |
| [sir-listing-forms.md](sir-listing-forms.md) | SIR blank-form field specs (reference source for Listing Module → RESO DD field mapping; not a CRM doc) |
| [personalization.md](personalization.md) | **Personalization & recommendation engine** — Phase-4 cross-app feature (visitor profiling, semantic ranking) |

## What lives where

| Concern | Home |
|---|---|
| CRM (Pipeline 2.0) entities, FRs, AI features, phases, CDL contract | `matrix-pipeline/` (this chapter) |
| Canonical RESO state machines (Listing, Showing, Lead-Contact, Transaction, etc.) | [`../business-processes/canonical-processes/`](../business-processes/canonical-processes/USAGE.md) |
| RESO DD 2.0 data model (resources, fields, lookups) | [`../data-models/reso-dd-kb/`](../data-models/reso-dd-kb/USAGE.md) |
| CDL schema (live tables, RLS, MLS ingestion) | [`../data-models/cdl-schema.md`](../data-models/cdl-schema.md) |
| Cross-resource integrated views | [`../integration/`](../integration/USAGE.md) |
