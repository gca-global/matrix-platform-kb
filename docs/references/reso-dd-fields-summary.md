# RESO Data Dictionary 2.0 — Fields & Lookups Summary

> **Cheat-sheet only.** This page is the human-friendly summary of the
> ~150 RESO fields Atlas actually consumes today. For the full
> machine-readable corpus (all ~1,745 RESO DD 2.0 fields, ~3,580
> lookup values, per-field Sys% / Org% adoption stats, BEDES
> mappings, change-history dates, and structured KV scraped from
> DDwiki) read [`reso-dd-kb/`](../../reso-dd-kb/README.md). The LLM
> agent reads `reso-dd-kb/AGENTS.md` first, then the relevant
> [`reso-dd-kb/wiki/resources/<Resource>.md`](../../reso-dd-kb/wiki/resources/),
> and clicks the DDwiki link only when it needs deep prose.
>
> Adoption percentages on this page (`Sys%`, `Org%`) come from
> [`reso-dd-kb/raw/field_metadata.csv`](../../reso-dd-kb/raw/field_metadata.csv)
> so the cheat-sheet stays in lock-step with the LLM wiki without
> manual maintenance.

> Source: `reso-dd-kb/raw/RESO_Data_Dictionary_2.0.xlsx`
> Version: DD 2.0, Wiki Date: 04/16/2024, XLSX Created: 2024-10-14

## Resources in RESO DD 2.0

| Resource | Description | Key Fields (examples) |
|----------|-------------|----------------------|
| **Property** | Real estate listings | ListPrice, BedroomsTotal, BathroomsFull, City, StateOrProvince, PostalCode, PropertyType, PropertySubType, StandardStatus, ListingContractDate, DaysOnMarket, YearBuilt, LivingArea, LotSizeArea |
| **Member** | Agents/brokers | MemberFirstName, MemberLastName, MemberEmail, MemberMlsId, MemberStatus |
| **Office** | Brokerage offices | OfficeName, OfficePhone, OfficeAddress1, OfficeMlsId |
| **Contacts** | Client records | ContactFirstName, ContactLastName, ContactEmail, ContactPhone |
| **Teams** | Agent teams | TeamName, TeamLead, TeamMemberCount |
| **OpenHouse** | Open house events | OpenHouseDate, OpenHouseStartTime, OpenHouseEndTime |
| **Media** | Listing media | MediaURL, MediaType, MediaCategory, MediaModificationTimestamp |
| **HistoryTransactional** | Transaction history | ClosePrice, CloseDate, ListPrice |
| **ShowingAppointment** | Showings | ShowingDate, ShowingStartTime, ShowingAgentMlsId |
| **Prospecting** | Lead tracking | ProspectingStatus |

## Key Property Fields for Cyprus Real Estate

### Identification & Status
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| ListingId | String | Unique listing identifier | — | 100% |
| ListingKey | String | System key | — | 98% |
| StandardStatus | Lookup | Active, Pending, Closed, Withdrawn, Expired, ComingSoon | — | 94% |
| PropertyType | Lookup | Residential, ResidentialLease, ResidentialIncome, Commercial, CommercialLease, Farm | — | 99% |
| PropertySubType | Lookup | Apartment, Condominium, SingleFamilyResidence, Townhouse, Villa, etc. | 95% | 95% |
| ListingContractDate | Date | Date listing agreement signed | 100% | 97% |
| ExpirationDate | Date | Listing expiration | 80% | 59% |
| DaysOnMarket | Number | Days on market (calculated) | 75% | 90% |

### Pricing
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| ListPrice | Number | Listing price | — | 100% |
| OriginalListPrice | Number | Original asking price | 85% | 91% |
| ClosePrice | Number | Final sale price | 90% | 90% |
| PriceChangeTimestamp | Timestamp | Last price change | 80% | 75% |

### Location
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| StreetNumber | String | Street number | 95% | 95% |
| StreetName | String | Street name | 95% | 98% |
| City | String | City | 90% | 98% |
| StateOrProvince | String | State/Province | 100% | 98% |
| PostalCode | String | Postal/ZIP code | 100% | 98% |
| Country | String | Country (ISO) | 80% | 54% |
| Latitude | Number | GPS latitude | 90% | 97% |
| Longitude | Number | GPS longitude | 90% | 97% |

### Structure
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| BedroomsTotal | Number | Total bedrooms | 100% | 98% |
| BathroomsFull | Number | Full bathrooms | 100% | 89% |
| BathroomsHalf | Number | Half bathrooms | 95% | 85% |
| BathroomsTotalInteger | Number | Total bathrooms | 85% | 82% |
| LivingArea | Number | Living area | — | 78% |
| LivingAreaUnits | Lookup | SqFt, SqM | 80% | 51% |
| BuildingAreaTotal | Number | Total building area | 90% | 86% |
| LotSizeArea | Number | Lot/plot size | 95% | 86% |
| StoriesTotal | Number | Total stories in building | 75% | 20% |
| Stories | Number | Number of stories/floors | 70% | 56% |
| YearBuilt | Number | Year constructed | 100% | 98% |
| Furnished | Lookup | Furnished, PartiallyFurnished, Unfurnished | 45% | 37% |

### Construction & Development
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| NewConstructionYN | Boolean | Newly constructed AND not previously occupied. Sharp Matrix approximates via `new_build=true` AND non-resale `construction_stage` AND `StandardStatus` not Closed/Withdrawn. See [property-field-mapping.md](../data-models/property-field-mapping.md#construction--development) for the full rule. | 80% | 59% |
| DevelopmentStatus | Lookup Multi (Open) | Development lifecycle: `New Construction`, `Under Construction`, `Proposed`, `Existing`. Lookup is **Open** per [RESO DDwiki](https://ddwiki.reso.org/display/DDW20/DevelopmentStatus+Field) — MLSs may introduce additional land-specific values (`Site Cleared`, `Site Prepared`, `Final Development Plan Completed`, etc.) over time. | 60% | 35% |
| BuilderName | String | Developer / seller company that built the property. | — | 35% |
| BuilderModel | String | Project / development name. | 40% | 9% |
| PropertyCondition | Lookup Multi | Contains `'New Construction'` when `NewConstructionYN = TRUE`. Industry-standard companion flag used by Trestle/Cotality, CRMLS, Bright MLS. | — | 63% |

### Features
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| View | Lookup Multi | City, Garden, Mountain(s), Ocean, Pool | 90% | 66% |
| Heating | Lookup Multi | Central, Electric, Geothermal, HeatPump, NaturalGas, None | 95% | 90% |
| Cooling | Lookup Multi | CentralAir, WallUnit, None | — | 90% |
| Appliances | Lookup Multi | Dishwasher, Dryer, Microwave, Oven, Refrigerator, Washer | 90% | 87% |
| ParkingFeatures | Lookup Multi | AttachedGarage, CoveredParking, OpenParking | 95% | 84% |
| CoveredSpaces | Number | Covered parking count | 55% | 35% |
| OpenParkingSpaces | Number | Open parking count | 55% | 12% |
| PoolPrivateYN | Boolean | Private pool | 75% | 31% |
| PoolFeatures | Lookup Multi | InGround, Communal, Private | — | 79% |
| AssociationAmenities | Lookup Multi | Gym, Sauna, Playground, Pool, etc. | — | 56% |
| WaterfrontFeatures | Lookup Multi | Beach access, waterfront | 75% | 72% |

### Agent & Office
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| ListAgentKey | String | Listing agent ID | 90% | 78% |
| ListAgentFullName | String | Listing agent name | — | 91% |
| ListAgentEmail | String | Listing agent email | 90% | 75% |
| ListOfficeName | String | Listing office name | 95% | 97% |
| ListAgentCommission | Number | Agent commission % | — | — |

### Descriptions
| StandardName | Type | Description | Sys% | Org% |
|-------------|------|-------------|------|------|
| PublicRemarks | String | Public property description | 100% | 98% |
| PrivateRemarks | String | Agent-only notes | 80% | 87% |
| Directions | String | Driving directions | 95% | 91% |

## Key Lookup Categories

| LookupName | # Values | Example Values |
|-----------|----------|----------------|
| PropertyType | 7 | Residential, CommercialSale, CommercialLease, Farm, Land |
| PropertySubType | 50+ | Apartment, Condominium, SingleFamilyResidence, Townhouse, Villa |
| StandardStatus | 8 | Active, ActiveUnderContract, Closed, ComingSoon, Expired, Pending, Withdrawn |
| Country | 200+ | CY, US, GR, GB, RU |
| View | 20+ | City, Garden, Mountain(s), Ocean, Pool, Trees/Woods |
| Heating | 15+ | Central, Electric, Geothermal, HeatPump, NaturalGas, Radiant, None |
| Cooling | 10+ | CentralAir, WallUnit, Evaporation, None |
| Furnished | 3 | Furnished, PartiallyFurnished, Unfurnished |
| ParkingFeatures | 15+ | AttachedGarage, CircularDriveway, CoveredParking, GarageOpener |
| PoolFeatures | 10+ | AboveGround, Community, Gunite, InGround, Private |
| AccessibilityFeatures | 30+ | AccessibleApproachWithRamp, AccessibleBedroom, etc. |
| AreaSource | 10+ | Agent, Appraiser, Assessor, Builder, Estimated, PublicRecords |
| AreaUnits | 2 | SquareFeet, SquareMeters |
| LeadSource | 15+ | Agent, OpenHouse, RealEstateWebsite, Referral, SignOnProperty |

## Data Types Used

| SimpleDataType | Description | Example |
|---------------|-------------|---------|
| String | Text | "Villa Paphos" |
| Number | Numeric (with optional precision) | 850000.00 |
| Boolean | True/False | true |
| Date | Date (YYYY-MM-DD) | 2026-02-18 |
| Timestamp | Date+Time (ISO 8601) | 2026-02-18T10:30:00Z |
| String List, Single | Single picklist selection | "Active" |
| String List, Multi | Multiple picklist selections | ["Ocean", "Mountain(s)"] |
