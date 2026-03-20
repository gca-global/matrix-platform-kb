# Zoe AI Assistant — Knowledge Base Index

This directory contains the full knowledge base for the **Zoe AI Assistant** — the Sharp Matrix platform's AI-powered support agent.

## Purpose

Zoe serves two audiences with different needs:

### 1st Line Support (End Users)
Help business users (brokers, agents, managers, staff) with:
- How to use Sharp Matrix apps
- Troubleshooting common problems
- Identifying bugs vs. user errors vs. configuration issues
- Suggesting workarounds for known issues
- Guiding incident submission to 2nd line support

### 2nd Line Support (Technical / Operations)
Help support analysts and IT staff with:
- Understanding the technology stack and architecture
- Finding the right deep-dive documentation for investigation
- Qualifying incidents before escalating to 3rd line (dev team)
- Identifying whether an issue is configuration, data, or code

---

## Documents

### 1st Line — End-User Support

| Document | Covers |
|----------|--------|
| [platform-overview.md](platform-overview.md) | What is Sharp Matrix, all apps at a glance, getting started, cross-app troubleshooting, incident reporting, glossary |
| [portal.md](portal.md) | Agency Portal — dashboard, app launcher, stats, AI Advisor, Quick Access |
| [client-connect.md](client-connect.md) | Client Connect — registration, verification, MLS duplicates, approval workflow |
| [meeting-hub.md](meeting-hub.md) | Meeting Hub — appointments, 4 meeting types, analytics, reports |
| [comms.md](comms.md) | Matrix Comms — WhatsApp messaging, conversations, templates, campaigns, AI replies |
| [platform-sso-auth.md](platform-sso-auth.md) | SSO & Authentication — login, roles, permissions, scope, SSO Console |
| [cross-app-workflows.md](cross-app-workflows.md) | Cross-app workflows — client lifecycle, daily routines by role, data flow between apps, scenarios |

### 2nd Line — Technical Reference

| Document | Covers |
|----------|--------|
| [second-line-tech-reference.md](second-line-tech-reference.md) | Technology stack, architecture, database, Edge Functions, links to deep-dive docs |

### Meta

| Document | Covers |
|----------|--------|
| [kb-generation-guide.md](kb-generation-guide.md) | How to generate a support KB article for any new Sharp Matrix app |

---

## RAG Usage Notes

- Each document is self-contained with FAQ, troubleshooting, and escalation sections.
- Section headers are descriptive for semantic search chunking.
- FAQ entries use natural questions that users actually ask.
- Troubleshooting tables use Problem → Cause → Solution format.
- Use `cross-app-workflows.md` when a user asks about data flow between apps, daily routines, or end-to-end client lifecycle.
- Start with `platform-overview.md` for general questions; use app-specific docs for targeted queries.
- Use `second-line-tech-reference.md` when a 2nd line analyst needs architectural context.
