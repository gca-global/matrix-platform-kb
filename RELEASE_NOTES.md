---
name: v1.0.0
version: 1.0.0
date: 2026-08-17
---

# Release notes — matrix-platform-kb

**Repo:** [`gca-global/matrix-platform-kb`](https://github.com/gca-global/matrix-platform-kb)  
**Version trail:** GitHub Releases/tags `vX.Y.Z` + this file + [`VERSION`](VERSION).
**Agent rules:** [`AGENTS.md`](AGENTS.md) § Release notes & versioning.

## Unreleased — 2026-08-17

- Moved the GitHub repo to [`gca-global/matrix-platform-kb`](https://github.com/gca-global/matrix-platform-kb). The previous `sharpsir-group/matrix-platform-kb` URL permanently redirects.
- **ADR-038**: ITSM is ES256-only (SSO PostgREST bearer + MCP access-token issuer). Supersedes ADR-032 for the MCP HMAC signing algorithm only; chat-agent/OAuth design stands. Corrects `security-model.md` hybrid table (ITSM already on TPA; remaining HS256 apps are FM / Meeting Hub, etc.).
- Agent release-notes & versioning policy aligned with `matrix-itsm` (SemVer, day-batch PATCH, `scripts/release.sh`).
- Removed third-party AI vendor brand names from chat/AI surfaces; those docs now refer to a generic chat agent / website AI chat.
- Proprietary copyright notice (Sharp SIR + GCA Global) added at agent entry points (`LICENSE`, `AGENTS.md`, `README.md`, `docs/index.md`, `docs/platform/kb-methodology.md`).

## v1.0.0 — 2026-08-17 — Baseline Matrix Platform Knowledge Base

First tracked release. Retrospective baseline snapshot — later tags are deltas from this commit.
