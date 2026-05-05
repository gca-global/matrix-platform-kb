# RESO Data Dictionary 2.0 - moved

> This page used to summarise the RESO DD 2.0 XLSX. The XLSX is no
> longer the source of truth.

The canonical RESO DD 2.0 model now lives in [`reso-dd-kb/`](reso-dd-kb/README.md)
(integrated chapter under `docs/data-models/`). It is built from a
verified mirror of `dd.reso.org/DD2.0/` and ships both a DBML schema
and a per-resource markdown reference.

| If you want... | Read |
|---|---|
| an LLM consumption guide | [`reso-dd-kb/USAGE.md`](reso-dd-kb/USAGE.md) |
| the resource catalogue | [`reso-dd-kb/wiki/agent-docs/_index.md`](reso-dd-kb/wiki/agent-docs/_index.md) |
| per-resource field tables | [`reso-dd-kb/wiki/agent-docs/resources/`](reso-dd-kb/wiki/agent-docs/resources/) |
| lookup value tables | [`reso-dd-kb/wiki/agent-docs/lookups.md`](reso-dd-kb/wiki/agent-docs/lookups.md) |
| FK relationships | [`reso-dd-kb/wiki/agent-docs/relationships.md`](reso-dd-kb/wiki/agent-docs/relationships.md) |
| the DBML schema | [`reso-dd-kb/wiki/dbml/canonical.dbml`](reso-dd-kb/wiki/dbml/canonical.dbml) |

For Sharp Matrix's project-specific policy on top of RESO DD (which
resources are used, the `x_sm_*` extension governance), see
[`platform-extensions.md`](platform-extensions.md).
