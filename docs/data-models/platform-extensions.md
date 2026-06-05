# Sharp Matrix Platform Extensions (x_*)

> Fields and lookup values required by Sharp Matrix that do not exist in RESO DD 2.0.
> All extensions follow the `x_` prefix convention ([ADR-023](../architecture/decisions/ADR-023.md), which superseded the former `x_sm_` vendor prefix). The canonical RESO DD 2.0 model lives in [`reso-dd-kb/`](reso-dd-kb/README.md).
> for the governance process.

## Extension Fields — Property Resource

### Financial & Legal

| Extension Field | Data Type | Reason | SIR Source Field | Qobrix Source | Apps |
|----------------|-----------|--------|-----------------|---------------|------|
| x_vat_applicable | Boolean | Cyprus VAT on property — not a RESO concept | +VAT (yes/no) | property.vat_applicable | Broker, Finance |
| x_introducer_fee | Number | Fee paid to party who introduced the deal | Introducer fee | property.introducer_fee | Broker, Finance |
| x_title_deeds | Boolean | Whether title deeds are available (Cyprus legal requirement) | Title deeds availability | property.title_deeds | Broker |
| x_suitable_for_pr | Boolean | Whether the property qualifies buyer for Permanent Residency (Cyprus immigration) | Suitable for PR | property.suitable_for_pr | Broker, Client Portal |
| x_crypto_payment | Boolean | Whether cryptocurrency payment is accepted | Crypto payment possible | property.crypto_payment | Broker, Client Portal |

### Structure & Layout

| Extension Field | Data Type | Reason | SIR Source Field | Qobrix Source | Apps |
|----------------|-----------|--------|-----------------|---------------|------|
| x_uncovered_verandas | Number (sq.m.) | RESO has no separate uncovered veranda field — relevant for Mediterranean properties | Uncovered Verandas (sq.m.) | property.uncovered_verandas | Broker, Client Portal |
| x_roof_garden | Number (sq.m.) | Roof garden area — common in Cyprus high-rises, not in RESO | Roof garden (sq.m.) | property.roof_garden | Broker, Client Portal |
| x_elevator | Boolean | Building has elevator — not a standalone RESO field | Elevator | property.elevator | Broker, Client Portal |
| x_maids_room | Boolean | Maid's/service room — common in luxury Cyprus properties | Maid's room | property.maids_room | Broker, Client Portal |
| x_smart_home | Boolean | Smart home features installed | Smart home | property.smart_home | Broker, Client Portal, Marketing |
| x_year_renovated | Number | Year of last renovation — RESO only has YearBuilt | Year of renovation | property.year_renovated | Broker, Client Portal |
| x_extras | String | Free-text additional features not captured elsewhere | Additional Extras | property.extras | Broker |
| x_heating_medium | String List | Specific heating medium (underfloor, fan coil, etc.) — RESO Heating only covers type | Heating Medium | property.heating_medium | Broker, Client Portal |

### Land & Zoning (Cyprus-specific)

| Extension Field | Data Type | Reason | SIR Source Field | Qobrix Source | Apps |
|----------------|-----------|--------|-----------------|---------------|------|
| x_building_density | Number (%) | Building density percentage — Cyprus town planning regulation | Building density % | property.building_density | Broker |
| x_coverage | Number (%) | Coverage percentage — Cyprus town planning regulation | Coverage % | property.coverage | Broker |
| x_floors_allowed | Number | Maximum floors allowed by zoning | Floors allowed | property.floors_allowed | Broker |
| x_height_allowed | Number (m) | Maximum building height allowed by zoning | Height allowed (m) | property.height_allowed | Broker |

### Contact Extensions

| Extension Field | Data Type | Reason | SIR Source Field | Qobrix Source | Apps |
|----------------|-----------|--------|-----------------|---------------|------|
| x_keyholder_name | String | Property keyholder/representative in Cyprus for absentee owners | Keyholder/Representative in CY | — (custom) | Broker |
| x_keyholder_contact | String | Keyholder phone/email | Telephone/email of keyholder | — | Broker |
| x_privacy_level | String | FR-CON privacy classification (Standard / Private / Ultra-confidential) — drives Pipeline PII visibility; not a RESO DD field, not exported to any outbound channel | Privacy | — (custom) | Pipeline (Broker) |

### Showing Extensions

| Extension Field | Data Type | Reason | SIR Source Field | Qobrix Source | Apps |
|----------------|-----------|--------|-----------------|---------------|------|
| x_contact_key | String | Buyer `Contact.ContactKey` attached to a Showing / ShowingAppointment / ShowingRequest. RESO DD 2.0 has no `ShowingContactKey` (Showing models the agent + listing, not a buyer contact) — see [ADR-022](../architecture/decisions/ADR-022.md). Loose witness (no FK); indexed; in the `cdl-read` filterable allow-list; not exported to any outbound RESO/Dash channel. | — (custom) | — (custom) | Pipeline (Broker) |

## Extension Lookup Values — PropertySubType

RESO DD 2.0 `PropertySubType` doesn't cover all Cyprus/Mediterranean property types.
These are registered as platform-specific lookup values:

| Lookup Extension | Maps To | RESO Closest Equivalent | Reason Needed |
|-----------------|---------|------------------------|---------------|
| x_duplex | Duplex Apartment | — | Multi-level apartment unit, not a standalone duplex |
| x_ground_floor | Ground Floor Apartment | — | Ground-level apartment with garden access |
| x_penthouse | Penthouse | — | Top-floor luxury unit (RESO has no specific subtype) |
| x_whole_floor | Whole Floor Apartment | — | Entire building floor as single unit |
| x_semi_detached | Semi-detached Villa | — | Semi-detached house (common in Cyprus) |
| x_mansion | Mansion / Villa | — | Large luxury estate property |
| x_bungalow | Bungalow | — | Single-story house |
| x_maisonette | Maisonette | — | Multi-level within a building (European concept) |
| x_plot | Plot (Building Land) | — | Serviced building plot (distinct from UnimprovedLand) |
| x_plot_settlement | Plot within Settlement | — | Plot within settlement boundaries (Cyprus zoning) |

## Summary Statistics

| Category | Count |
|----------|-------|
| Extension fields (Property) | 16 |
| Extension fields (Contact) | 3 |
| Extension fields (Showing) | 1 |
| Extension lookup values (PropertySubType) | 10 |
| **Total extensions** | **30** |

> Materialized in CDL today (the rest are spec-only): `contacts.x_privacy_level`, and `x_contact_key` on `showings` / `showing` / `showing_request`. All four were renamed from the legacy `x_sm_` prefix by migration `20260605160000_rename_x_sm_extensions_to_x.sql` ([ADR-023](../architecture/decisions/ADR-023.md)).

## Governance Notes

- **Regional scope**: Most extensions are Cyprus-specific or Mediterranean-specific. When Sharp Matrix expands to Hungary and Kazakhstan, additional regional extensions may be needed (e.g., Hungarian land registry fields, Kazakh property registration).
- **Prefix**: The platform extension prefix is `x_` ([ADR-023](../architecture/decisions/ADR-023.md)). It superseded the former vendor-tagged `x_sm_` prefix on 2026-06-05; the four materialized columns were renamed by migration `20260605160000_rename_x_sm_extensions_to_x.sql`. RESO DD 2.0 itself defines no extension prefix — `x_` is the platform's local-field marker and these columns are never emitted to outbound RESO/Dash channels.
- **Retirement**: If a future RESO DD version (e.g., DD 2.1) adds a field that matches an `x_*` extension, the extension should be migrated to the RESO name with a deprecation period.
- **Naming collisions**: Never reuse a retired extension name for a different purpose.

## Cross-Reference

| For | See |
|-----|-----|
| Extension governance rules | This file (`platform-extensions.md`) |
| Full field mapping with extensions flagged | [property-field-mapping.md](property-field-mapping.md) |
| RESO DD 2.0 field reference | [`reso-dd-kb/wiki/agent-docs/_index.md`](reso-dd-kb/wiki/agent-docs/_index.md) |
