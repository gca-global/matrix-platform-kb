# Property

Fields commonly used in a Multiple Listing Service (MLS) listing.

**RESO DD 2.0** — 652 fields · last revised 9/10/2019 · [dd.reso.org](https://dd.reso.org/DD2.0/Property/)

**Adoption** — weighted Org%: **39%** across 624 measured fields (median 32%, avg 39%).

## Groups

- **Business** — 17 fields
- **Characteristics** — 51 fields
- **Equipment** — 3 fields
- **Farming** — 12 fields
- **Financial** — 37 fields
- **HOA** — 11 fields
- **Listing** — 26 fields
- **Listing, Dates** — 3 fields
- **Listing, Media** — 1 fields
- **Listing,AgentOffice,BuyerAgent** — 28 fields
- **Listing,AgentOffice,BuyerOffice** — 10 fields
- **Listing,AgentOffice,BuyerTeam** — 1 fields
- **Listing,AgentOffice,CoBuyerAgent** — 27 fields
- **Listing,AgentOffice,CoBuyerOffice** — 11 fields
- **Listing,AgentOffice,CoListAgent** — 27 fields
- **Listing,AgentOffice,CoListOffice** — 11 fields
- **Listing,AgentOffice,ListAgent** — 27 fields
- **Listing,AgentOffice,ListOffice** — 12 fields
- **Listing,AgentOffice,ListTeam** — 1 fields
- **Listing,AgentOffice,Team** — 4 fields
- **Listing,Closing** — 8 fields
- **Listing,Compensation** — 9 fields
- **Listing,Contract** — 8 fields
- **Listing,Dates** — 26 fields
- **Listing,Marketing** — 8 fields
- **Listing,Media** — 8 fields
- **Listing,Price** — 5 fields
- **Listing,Remarks** — 4 fields
- **Listing,Showing** — 18 fields
- **Location** — 21 fields
- **Location,Address** — 19 fields
- **Location,Area** — 7 fields
- **Location,GIS** — 9 fields
- **Location,School** — 6 fields
- **OccupantOwner** — 5 fields
- **Other** — 4 fields
- **Structure** — 101 fields
- **Structure,Performance,GreenMarketing** — 7 fields
- **Structure,Performance,GreenVerification** — 3 fields
- **Structure,Rooms** — 3 fields
- **Tax** — 22 fields
- **UnitTypes** — 2 fields
- **Utilities** — 29 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `AboveGradeFinishedArea` | Number | Structure |  | 34% | The finished area within the structure that is at or above the surface of the ground. | [link](https://dd.reso.org/DD2.0/Property/AboveGradeFinishedArea/) |
| `AboveGradeFinishedAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 9% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/AboveGradeFinishedAreaSource/) |
| `AboveGradeFinishedAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 12% | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/AboveGradeFinishedAreaUnits/) |
| `AboveGradeUnfinishedArea` | Number | Structure |  | 4% | The unfinished area within the structure that is at or above the surface of the ground. | [link](https://dd.reso.org/DD2.0/Property/AboveGradeUnfinishedArea/) |
| `AboveGradeUnfinishedAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 0% | The source of the measurements of the unfinished area above grade. | [link](https://dd.reso.org/DD2.0/Property/AboveGradeUnfinishedAreaSource/) |
| `AboveGradeUnfinishedAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 1% | A pick list of the unit of measurement for the unfinished area above grade (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/AboveGradeUnfinishedAreaUnits/) |
| `AccessCode` | String | Listing, Showing |  | 9% | The code to gain access through the secured gate for a property located behind an unmanned security gate such as in a gated community. | [link](https://dd.reso.org/DD2.0/Property/AccessCode/) |
| `AccessibilityFeatures` | String List, Multi | Structure | [AccessibilityFeatures](#accessibilityfeatures) | 73% | A list or description of the accessibility features included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/AccessibilityFeatures/) |
| `ActivationDate` | Date | Listing, Dates |  | 18% | Indicates when the listing agent intends to change the property to the Active status. | [link](https://dd.reso.org/DD2.0/Property/ActivationDate/) |
| `AdditionalParcelsDescription` | String | Tax |  | 24% | If additional parcels are included in the sale, a list of those parcel's IDs separated by commas. | [link](https://dd.reso.org/DD2.0/Property/AdditionalParcelsDescription/) |
| `AdditionalParcelsYN` | Boolean | Tax |  | 20% | Indicates whether or not more than one parcel or lot is included in the sale. | [link](https://dd.reso.org/DD2.0/Property/AdditionalParcelsYN/) |
| `AnchorsCoTenants` | String | Characteristics |  | 5% | The main or most notable tenants as well as other tenants of the shopping center or mall in which the commercial property is located. | [link](https://dd.reso.org/DD2.0/Property/AnchorsCoTenants/) |
| `Appliances` | String List, Multi | Equipment | [Appliances](#appliances) | 89% | A list of the appliances that will be included in the sale/lease of the property. | [link](https://dd.reso.org/DD2.0/Property/Appliances/) |
| `ArchitecturalStyle` | String List, Multi | Structure | [ArchitecturalStyle](#architecturalstyle) | 90% | A list describing the style of the structure (e.g., Victorian, Ranch, Craftsman). | [link](https://dd.reso.org/DD2.0/Property/ArchitecturalStyle/) |
| `AssociationAmenities` | String List, Multi | HOA | [AssociationAmenities](#associationamenities) | 56% | The amenities provided by the homeowner association, mobile park or complex (e.g., pool, clubhouse). | [link](https://dd.reso.org/DD2.0/Property/AssociationAmenities/) |
| `AssociationFee` | Number | HOA |  | 82% | A fee paid by the homeowner to the homeowner association that is used for upkeep of common areas, the neighborhood or other association-related benefits. | [link](https://dd.reso.org/DD2.0/Property/AssociationFee/) |
| `AssociationFee2` | Number | HOA |  | 23% | A fee paid by the homeowner to the second of two homeowner associations that is used for upkeep of common areas, the neighborhood or other association-related benefits. | [link](https://dd.reso.org/DD2.0/Property/AssociationFee2/) |
| `AssociationFee2Frequency` | String List, Single | HOA | [FeeFrequency](#feefrequency) | 18% | The frequency the association fee is paid (e.g., weekly, monthly, annually, bimonthly, one time). | [link](https://dd.reso.org/DD2.0/Property/AssociationFee2Frequency/) |
| `AssociationFeeFrequency` | String List, Single | HOA | [FeeFrequency](#feefrequency) | 72% | The frequency the association fee is paid (e.g., weekly, monthly, annually, bimonthly, one time). | [link](https://dd.reso.org/DD2.0/Property/AssociationFeeFrequency/) |
| `AssociationFeeIncludes` | String List, Multi | HOA | [AssociationFeeIncludes](#associationfeeincludes) | 59% | The services included with the association fee (e.g., landscaping, trash, water). | [link](https://dd.reso.org/DD2.0/Property/AssociationFeeIncludes/) |
| `AssociationName` | String | HOA |  | 30% | The name of the homeowner association. | [link](https://dd.reso.org/DD2.0/Property/AssociationName/) |
| `AssociationName2` | String | HOA |  | 8% | The name of the second of two homeowner associations. | [link](https://dd.reso.org/DD2.0/Property/AssociationName2/) |
| `AssociationPhone` | String | HOA |  | 28% | The phone number of the homeowner association. | [link](https://dd.reso.org/DD2.0/Property/AssociationPhone/) |
| `AssociationPhone2` | String | HOA |  | 5% | The phone number of the second of two homeowner associations. | [link](https://dd.reso.org/DD2.0/Property/AssociationPhone2/) |
| `AssociationYN` | Boolean | HOA |  | 78% | Indicates whether there is a homeowner association. | [link](https://dd.reso.org/DD2.0/Property/AssociationYN/) |
| `AttachedGarageYN` | Boolean | Structure |  | 79% | A flag indicating whether or not the garage is attached to the dwelling. | [link](https://dd.reso.org/DD2.0/Property/AttachedGarageYN/) |
| `AttributionContact` | String | Listing, AgentOffice, ListOffice |  | 37% | A text field to convey a specific contact phone number or email address for the listing firm. | [link](https://dd.reso.org/DD2.0/Property/AttributionContact/) |
| `AvailabilityDate` | Date | Listing, Closing |  | 57% | The date the property will be available for possession/occupation. | [link](https://dd.reso.org/DD2.0/Property/AvailabilityDate/) |
| `AvailableLeaseType` | String List, Multi | Characteristics | [ExistingLeaseType](#existingleasetype) | 3% | Information about the available types of lease for the property (i.e., Net, NNN, NN, Gross, Absolute Net, Escalation Clause, Ground Lease, etc.). | [link](https://dd.reso.org/DD2.0/Property/AvailableLeaseType/) |
| `BackOnMarketDate` | Date | Listing, Dates |  | 8% | The date a listing, which had previously gone off market, went back to being on market. | [link](https://dd.reso.org/DD2.0/Property/BackOnMarketDate/) |
| `Basement` | String List, Multi | Structure | [Basement](#basement) | 71% | A list of information and features about the basement (i.e., None/Slab, Finished, Partially Finished, Crawl Space, Dirt, Outside Entrance, Radon Mitigation). | [link](https://dd.reso.org/DD2.0/Property/Basement/) |
| `BasementYN` | Boolean | Structure |  | 33% | Indicates whether or not the property has a basement. | [link](https://dd.reso.org/DD2.0/Property/BasementYN/) |
| `BathroomsFull` | Number | Structure |  | 94% | A room containing all four of the four elements constituting a bath: toilet, sink, bathtub, shower head (in tub or stall). | [link](https://dd.reso.org/DD2.0/Property/BathroomsFull/) |
| `BathroomsHalf` | Number | Structure |  | 89% | A room containing two of the four elements constituting a bath: toilet, sink, bathtub, shower head (in a tub or stall). | [link](https://dd.reso.org/DD2.0/Property/BathroomsHalf/) |
| `BathroomsOneQuarter` | Number | Structure |  | 10% | A room containing one of the four elements constituting a bath: toilet, sink, bathtub, shower head (in tub or stall). | [link](https://dd.reso.org/DD2.0/Property/BathroomsOneQuarter/) |
| `BathroomsPartial` | Number | Structure |  | 8% | The number of partial bathrooms in the property being sold/leased. | [link](https://dd.reso.org/DD2.0/Property/BathroomsPartial/) |
| `BathroomsThreeQuarter` | Number | Structure |  | 29% | A room containing three of the four elements constituting a bath: toilet, sink, bathtub, shower head (in a tub or stall). | [link](https://dd.reso.org/DD2.0/Property/BathroomsThreeQuarter/) |
| `BathroomsTotalInteger` | Number | Structure |  | 93% | The total number of bathrooms in the property as an integer (full bathrooms; halves counted in BathroomsHalf). | [link](https://dd.reso.org/DD2.0/Property/BathroomsTotalInteger/) |
| `BedroomsPossible` | Number | Structure |  | 8% | The sum of BedroomsTotal plus other rooms that may be used as a bedroom but are not defined as a bedroom per local policy. | [link](https://dd.reso.org/DD2.0/Property/BedroomsPossible/) |
| `BedroomsTotal` | Number | Structure |  | 100% | The total number of bedrooms in the property. | [link](https://dd.reso.org/DD2.0/Property/BedroomsTotal/) |
| `BelowGradeFinishedArea` | Number | Structure |  | 44% | The finished area within the structure that is below ground. | [link](https://dd.reso.org/DD2.0/Property/BelowGradeFinishedArea/) |
| `BelowGradeFinishedAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 8% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/BelowGradeFinishedAreaSource/) |
| `BelowGradeFinishedAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 15% | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/BelowGradeFinishedAreaUnits/) |
| `BelowGradeUnfinishedArea` | Number | Structure |  | 6% | The unfinished area within the structure that is below ground. | [link](https://dd.reso.org/DD2.0/Property/BelowGradeUnfinishedArea/) |
| `BelowGradeUnfinishedAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 0% | The source of the measurements of the unfinished area below grade. | [link](https://dd.reso.org/DD2.0/Property/BelowGradeUnfinishedAreaSource/) |
| `BelowGradeUnfinishedAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 1% | A pick list of the unit of measurement for the unfinished area below grade (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/BelowGradeUnfinishedAreaUnits/) |
| `BodyType` | String List, Multi | Structure | [BodyType](#bodytype) | 42% | The type of mobile home. | [link](https://dd.reso.org/DD2.0/Property/BodyType/) |
| `BuilderModel` | String | Structure |  | 13% | The model name or model number of the builder's plan for the property (project / development name). | [link](https://dd.reso.org/DD2.0/Property/BuilderModel/) |
| `BuilderName` | String | Structure |  | 35% | The name of the builder of the property (developer / seller company for new builds). | [link](https://dd.reso.org/DD2.0/Property/BuilderName/) |
| `BuildingAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 47% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/BuildingAreaSource/) |
| `BuildingAreaTotal` | Number | Structure |  | 88% | The total area of the structure, including both finished and unfinished areas. | [link](https://dd.reso.org/DD2.0/Property/BuildingAreaTotal/) |
| `BuildingAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 40% | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/BuildingAreaUnits/) |
| `BuildingFeatures` | String List, Multi | Structure | BuildingFeatures | 62% | The features or amenities of the building or business park. | [link](https://dd.reso.org/DD2.0/Property/BuildingFeatures/) |
| `BuildingName` | String | Structure |  | 26% | The name of the building or business park. | [link](https://dd.reso.org/DD2.0/Property/BuildingName/) |
| `BusinessName` | String | Business |  | 45% | The name of the business being sold. | [link](https://dd.reso.org/DD2.0/Property/BusinessName/) |
| `BusinessType` | String List, Multi | Business | [BusinessType](#businesstype) | 67% | The type of business being sold (e.g., Retail, Wholesale, Grocery, Food & Bev). | [link](https://dd.reso.org/DD2.0/Property/BusinessType/) |
| `BuyerAgent` | Resource | Listing, AgentOffice, BuyerAgent |  |  | The buyer's agent involved in the transaction. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgent/) |
| `BuyerAgentAOR` | String List, Single | Listing, AgentOffice, BuyerAgent | AOR | 21% | The buyer agent's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentAOR/) |
| `BuyerAgentDesignation` | String List, Multi | Listing, AgentOffice, BuyerAgent | [BuyerAgentDesignation](#buyeragentdesignation) | 30% | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completi… | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentDesignation/) |
| `BuyerAgentDirectPhone` | String | Listing, AgentOffice, BuyerAgent |  | 53% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentDirectPhone/) |
| `BuyerAgentEmail` | String | Listing, AgentOffice, BuyerAgent |  | 81% | The email address of the buyer's agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentEmail/) |
| `BuyerAgentFax` | String | Listing, AgentOffice, BuyerAgent |  | 43% | The North American 10-digit fax numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentFax/) |
| `BuyerAgentFirstName` | String | Listing, AgentOffice, BuyerAgent |  | 81% | The first name of the buyer's agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentFirstName/) |
| `BuyerAgentFullName` | String | Listing, AgentOffice, BuyerAgent |  | 81% | The first, middle and last name of the buyer's agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentFullName/) |
| `BuyerAgentHomePhone` | String | Listing, AgentOffice, BuyerAgent |  | 35% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentHomePhone/) |
| `BuyerAgentKey` | String | Listing, AgentOffice, BuyerAgent |  | 70% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentKey/) |
| `BuyerAgentLastName` | String | Listing, AgentOffice, BuyerAgent |  | 80% | The last name of the buyer's agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentLastName/) |
| `BuyerAgentMiddleName` | String | Listing, AgentOffice, BuyerAgent |  | 58% | The middle name of the buyer's agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentMiddleName/) |
| `BuyerAgentMlsId` | String | Listing, AgentOffice, BuyerAgent |  | 88% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentMlsId/) |
| `BuyerAgentMobilePhone` | String | Listing, AgentOffice, BuyerAgent |  | 53% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentMobilePhone/) |
| `BuyerAgentNamePrefix` | String | Listing, AgentOffice, BuyerAgent |  | 0% | The prefix to the name (e.g., Dr., Mr., Ms.). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentNamePrefix/) |
| `BuyerAgentNameSuffix` | String | Listing, AgentOffice, BuyerAgent |  | 1% | The suffix to the name (e.g., Esq., Jr., III). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentNameSuffix/) |
| `BuyerAgentNationalAssociationId` | String | Listing, AgentOffice, BuyerAgent |  | 1% | The national association ID of the buyer's agent (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentNationalAssociationId/) |
| `BuyerAgentOfficePhone` | String | Listing, AgentOffice, BuyerAgent |  | 61% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentOfficePhone/) |
| `BuyerAgentOfficePhoneExt` | String | Listing, AgentOffice, BuyerAgent |  | 34% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentOfficePhoneExt/) |
| `BuyerAgentPager` | String | Listing, AgentOffice, BuyerAgent |  | 18% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentPager/) |
| `BuyerAgentPreferredPhone` | String | Listing, AgentOffice, BuyerAgent |  | 72% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentPreferredPhone/) |
| `BuyerAgentPreferredPhoneExt` | String | Listing, AgentOffice, BuyerAgent |  | 30% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentPreferredPhoneExt/) |
| `BuyerAgentStateLicense` | String | Listing, AgentOffice, BuyerAgent |  | 54% | The license of the buyer agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentStateLicense/) |
| `BuyerAgentTollFreePhone` | String | Listing, AgentOffice, BuyerAgent |  | 25% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentTollFreePhone/) |
| `BuyerAgentURL` | String | Listing, AgentOffice, BuyerAgent |  | 72% | The website Uniform Resource Identifier (URI) of the buyers agent. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentURL/) |
| `BuyerAgentVoiceMail` | String | Listing, AgentOffice, BuyerAgent |  | 15% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentVoiceMail/) |
| `BuyerAgentVoiceMailExt` | String | Listing, AgentOffice, BuyerAgent |  | 3% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/BuyerAgentVoiceMailExt/) |
| `BuyerBrokerageCompensation` | String | Listing, Compensation |  | 5% | The total compensation to be paid to the buyer's brokerage for this sale, expressed as either a percentage or a constant currency amount. | [link](https://dd.reso.org/DD2.0/Property/BuyerBrokerageCompensation/) |
| `BuyerBrokerageCompensationType` | String List, Single | Listing, Compensation | [CompensationType](#compensationtype) | 3% | A list of types to clarify the value entered in the BuyerBrokerageCompensation field. | [link](https://dd.reso.org/DD2.0/Property/BuyerBrokerageCompensationType/) |
| `BuyerFinancing` | String List, Multi | Listing, Closing | [BuyerFinancing](#buyerfinancing) | 53% | A list of options that describe the type of financing used. | [link](https://dd.reso.org/DD2.0/Property/BuyerFinancing/) |
| `BuyerOffice` | Resource | Listing, AgentOffice, BuyerAgent |  |  | The buyer agent's office. | [link](https://dd.reso.org/DD2.0/Property/BuyerOffice/) |
| `BuyerOfficeAOR` | String List, Single | Listing, AgentOffice, BuyerOffice | AOR | 24% | The buyer's office's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeAOR/) |
| `BuyerOfficeEmail` | String | Listing, AgentOffice, BuyerOffice |  | 79% | The email address of the buyer's office. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeEmail/) |
| `BuyerOfficeFax` | String | Listing, AgentOffice, BuyerOffice |  | 55% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeFax/) |
| `BuyerOfficeKey` | String | Listing, AgentOffice, BuyerOffice |  | 84% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeKey/) |
| `BuyerOfficeMlsId` | String | Listing, AgentOffice, BuyerOffice |  | 91% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeMlsId/) |
| `BuyerOfficeName` | String | Listing, AgentOffice, BuyerOffice |  | 90% | The legal name of the brokerage representing the buyer. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeName/) |
| `BuyerOfficeNationalAssociationId` | String | Listing, AgentOffice, BuyerOffice |  | 1% | The national association ID of the buyer's office (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeNationalAssociationId/) |
| `BuyerOfficePhone` | String | Listing, AgentOffice, BuyerOffice |  | 81% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficePhone/) |
| `BuyerOfficePhoneExt` | String | Listing, AgentOffice, BuyerOffice |  | 18% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficePhoneExt/) |
| `BuyerOfficeURL` | String | Listing, AgentOffice, BuyerOffice |  | 72% | The website Uniform Resource Identifier (URI) for the buyers office. | [link](https://dd.reso.org/DD2.0/Property/BuyerOfficeURL/) |
| `BuyerTeam` | Resource | Listing, AgentOffice, BuyerTeam |  |  | Two or more agents working on the buyer agent's team. | [link](https://dd.reso.org/DD2.0/Property/BuyerTeam/) |
| `BuyerTeamKey` | String | Listing, AgentOffice, Team |  | 3% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/BuyerTeamKey/) |
| `BuyerTeamName` | String | Listing, AgentOffice, Team |  | 6% | The name of the team representing the buyer. | [link](https://dd.reso.org/DD2.0/Property/BuyerTeamName/) |
| `CableTvExpense` | Number | Financial |  | 4% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/CableTvExpense/) |
| `CancellationDate` | Date | Listing, Dates |  | 23% | The date that the listing contract between the seller and listing agent was canceled. | [link](https://dd.reso.org/DD2.0/Property/CancellationDate/) |
| `CapRate` | Number | Financial |  | 32% | The equivalent to the return on investment you would receive if you pay cash for a property. | [link](https://dd.reso.org/DD2.0/Property/CapRate/) |
| `CarportSpaces` | Number | Structure |  | 48% | The number of carport spaces included in the sale. | [link](https://dd.reso.org/DD2.0/Property/CarportSpaces/) |
| `CarportYN` | Boolean | Structure |  | 68% | A flag indicating that the listing has a carport. | [link](https://dd.reso.org/DD2.0/Property/CarportYN/) |
| `CarrierRoute` | String | Location, Address |  | 1% | The group of addresses to which the U.S. | [link](https://dd.reso.org/DD2.0/Property/CarrierRoute/) |
| `City` | String List, Single | Location, Address | City | 98% | The city in which the property is located. | [link](https://dd.reso.org/DD2.0/Property/City/) |
| `CityRegion` | String | Location, Area |  | 7% | A subsection or area of a defined city (e.g., SOHO in New York, NY; Ironbound in Newark, NJ; Inside the Beltway). | [link](https://dd.reso.org/DD2.0/Property/CityRegion/) |
| `CloseDate` | Date | Listing, Dates |  | 87% | With for-sale listings, this is the date the purchase agreement was fulfilled. | [link](https://dd.reso.org/DD2.0/Property/CloseDate/) |
| `ClosePrice` | Number | Listing, Price |  | 83% | The amount of money paid by the purchaser to the seller for the property under the agreement. | [link](https://dd.reso.org/DD2.0/Property/ClosePrice/) |
| `CoBuyerAgent` | Resource | Listing, AgentOffice, CoBuyerAgent |  |  | The co-buyer's agent involved in the transaction. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgent/) |
| `CoBuyerAgentAOR` | String List, Single | Listing, AgentOffice, CoBuyerAgent | AOR | 17% | The co-buyer agent's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentAOR/) |
| `CoBuyerAgentDesignation` | String List, Multi | Listing, AgentOffice, CoBuyerAgent | [CoBuyerAgentDesignation](#cobuyeragentdesignation) | 29% | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completi… | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentDesignation/) |
| `CoBuyerAgentDirectPhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 44% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentDirectPhone/) |
| `CoBuyerAgentEmail` | String | Listing, AgentOffice, CoBuyerAgent |  | 71% | The email address of the buyer's co-agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentEmail/) |
| `CoBuyerAgentFax` | String | Listing, AgentOffice, CoBuyerAgent |  | 39% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentFax/) |
| `CoBuyerAgentFirstName` | String | Listing, AgentOffice, CoBuyerAgent |  | 69% | The first name of the buyer's co-agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentFirstName/) |
| `CoBuyerAgentFullName` | String | Listing, AgentOffice, CoBuyerAgent |  | 71% | The first, middle and last name of the buyer's co-agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentFullName/) |
| `CoBuyerAgentHomePhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 24% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentHomePhone/) |
| `CoBuyerAgentKey` | String | Listing, AgentOffice, CoBuyerAgent |  | 63% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentKey/) |
| `CoBuyerAgentLastName` | String | Listing, AgentOffice, CoBuyerAgent |  | 69% | The last name of the buyer's co-agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentLastName/) |
| `CoBuyerAgentMiddleName` | String | Listing, AgentOffice, CoBuyerAgent |  | 50% | The middle name of the buyer's co-agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentMiddleName/) |
| `CoBuyerAgentMlsId` | String | Listing, AgentOffice, CoBuyerAgent |  | 74% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentMlsId/) |
| `CoBuyerAgentMobilePhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 49% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentMobilePhone/) |
| `CoBuyerAgentNamePrefix` | String | Listing, AgentOffice, CoBuyerAgent |  | 0% | The prefix to the name (e.g., Dr., Mr., Ms.). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentNamePrefix/) |
| `CoBuyerAgentNameSuffix` | String | Listing, AgentOffice, CoBuyerAgent |  | 1% | The suffix to the name (e.g., Esq., Jr., III). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentNameSuffix/) |
| `CoBuyerAgentNationalAssociationId` | String | Listing, AgentOffice, CoBuyerAgent |  | 0% | The national association ID of the co-buyer's agent (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentNationalAssociationId/) |
| `CoBuyerAgentOfficePhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 53% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentOfficePhone/) |
| `CoBuyerAgentOfficePhoneExt` | String | Listing, AgentOffice, CoBuyerAgent |  | 25% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentOfficePhoneExt/) |
| `CoBuyerAgentPager` | String | Listing, AgentOffice, CoBuyerAgent |  | 11% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentPager/) |
| `CoBuyerAgentPreferredPhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 63% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentPreferredPhone/) |
| `CoBuyerAgentPreferredPhoneExt` | String | Listing, AgentOffice, CoBuyerAgent |  | 18% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentPreferredPhoneExt/) |
| `CoBuyerAgentStateLicense` | String | Listing, AgentOffice, CoBuyerAgent |  | 51% | The license of the co-buyers' agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentStateLicense/) |
| `CoBuyerAgentTollFreePhone` | String | Listing, AgentOffice, CoBuyerAgent |  | 15% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentTollFreePhone/) |
| `CoBuyerAgentURL` | String | Listing, AgentOffice, CoBuyerAgent |  | 60% | The website Uniform Resource Identifier (URI) of the co-buyers agent. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentURL/) |
| `CoBuyerAgentVoiceMail` | String | Listing, AgentOffice, CoBuyerAgent |  | 11% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentVoiceMail/) |
| `CoBuyerAgentVoiceMailExt` | String | Listing, AgentOffice, CoBuyerAgent |  | 1% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerAgentVoiceMailExt/) |
| `CoBuyerOffice` | Resource | Listing, AgentOffice, CoBuyerOffice |  |  | The co-buyer agent's office. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOffice/) |
| `CoBuyerOfficeAOR` | String List, Single | Listing, AgentOffice, CoBuyerOffice | AOR | 16% | The co-buyer's office's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeAOR/) |
| `CoBuyerOfficeEmail` | String | Listing, AgentOffice, CoBuyerOffice |  | 64% | The email address of the buyer's co-office. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeEmail/) |
| `CoBuyerOfficeFax` | String | Listing, AgentOffice, CoBuyerOffice |  | 46% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeFax/) |
| `CoBuyerOfficeKey` | String | Listing, AgentOffice, CoBuyerOffice |  | 63% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeKey/) |
| `CoBuyerOfficeMlsId` | String | Listing, AgentOffice, CoBuyerOffice |  | 74% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeMlsId/) |
| `CoBuyerOfficeName` | String | Listing, AgentOffice, CoBuyerOffice |  | 74% | The legal name of the brokerage co-representing the buyer. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeName/) |
| `CoBuyerOfficeNationalAssociationId` | String | Listing, AgentOffice, CoBuyerOffice |  | 0% | The national association ID of the co-buyer's office (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeNationalAssociationId/) |
| `CoBuyerOfficePhone` | String | Listing, AgentOffice, CoBuyerOffice |  | 67% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficePhone/) |
| `CoBuyerOfficePhoneExt` | String | Listing, AgentOffice, CoBuyerOffice |  | 6% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficePhoneExt/) |
| `CoBuyerOfficeURL` | String | Listing, AgentOffice, CoBuyerOffice |  | 58% | The website Uniform Resource Identifier (URI) for the co-buyer's office. | [link](https://dd.reso.org/DD2.0/Property/CoBuyerOfficeURL/) |
| `CoListAgent` | Resource | Listing, AgentOffice, CoListAgent |  |  | The co-listing agent involved in the transaction. | [link](https://dd.reso.org/DD2.0/Property/CoListAgent/) |
| `CoListAgentAOR` | String List, Single | Listing, AgentOffice, CoListAgent | AOR | 24% | The Co-listing Agent's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentAOR/) |
| `CoListAgentDesignation` | String List, Multi | Listing, AgentOffice, CoListAgent | [CoListAgentDesignation](#colistagentdesignation) | 29% | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® and each affiliated group upon completion of … | [link](https://dd.reso.org/DD2.0/Property/CoListAgentDesignation/) |
| `CoListAgentDirectPhone` | String | Listing, AgentOffice, CoListAgent |  | 57% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentDirectPhone/) |
| `CoListAgentEmail` | String | Listing, AgentOffice, CoListAgent |  | 81% | The email address of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentEmail/) |
| `CoListAgentFax` | String | Listing, AgentOffice, CoListAgent |  | 46% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentFax/) |
| `CoListAgentFirstName` | String | Listing, AgentOffice, CoListAgent |  | 79% | The first name of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentFirstName/) |
| `CoListAgentFullName` | String | Listing, AgentOffice, CoListAgent |  | 80% | The first, middle and last name of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentFullName/) |
| `CoListAgentHomePhone` | String | Listing, AgentOffice, CoListAgent |  | 36% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentHomePhone/) |
| `CoListAgentKey` | String | Listing, AgentOffice, CoListAgent |  | 75% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentKey/) |
| `CoListAgentLastName` | String | Listing, AgentOffice, CoListAgent |  | 79% | The last name of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentLastName/) |
| `CoListAgentMiddleName` | String | Listing, AgentOffice, CoListAgent |  | 62% | The middle name of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentMiddleName/) |
| `CoListAgentMlsId` | String | Listing, AgentOffice, CoListAgent |  | 86% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentMlsId/) |
| `CoListAgentMobilePhone` | String | Listing, AgentOffice, CoListAgent |  | 58% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentMobilePhone/) |
| `CoListAgentNamePrefix` | String | Listing, AgentOffice, CoListAgent |  | 0% | The prefix to the name (e.g., Dr., Mr., Ms.). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentNamePrefix/) |
| `CoListAgentNameSuffix` | String | Listing, AgentOffice, CoListAgent |  | 1% | The suffix to the name (e.g., Esq., Jr., III). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentNameSuffix/) |
| `CoListAgentNationalAssociationId` | String | Listing, AgentOffice, CoListAgent |  | 20% | The national association ID of the co-listing agent (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentNationalAssociationId/) |
| `CoListAgentOfficePhone` | String | Listing, AgentOffice, CoListAgent |  | 64% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentOfficePhone/) |
| `CoListAgentOfficePhoneExt` | String | Listing, AgentOffice, CoListAgent |  | 32% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentOfficePhoneExt/) |
| `CoListAgentPager` | String | Listing, AgentOffice, CoListAgent |  | 15% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentPager/) |
| `CoListAgentPreferredPhone` | String | Listing, AgentOffice, CoListAgent |  | 73% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentPreferredPhone/) |
| `CoListAgentPreferredPhoneExt` | String | Listing, AgentOffice, CoListAgent |  | 24% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentPreferredPhoneExt/) |
| `CoListAgentStateLicense` | String | Listing, AgentOffice, CoListAgent |  | 58% | The license of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentStateLicense/) |
| `CoListAgentTollFreePhone` | String | Listing, AgentOffice, CoListAgent |  | 20% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentTollFreePhone/) |
| `CoListAgentURL` | String | Listing, AgentOffice, CoListAgent |  | 72% | The website Uniform Resource Identifier (URI) of the co-listing agent. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentURL/) |
| `CoListAgentVoiceMail` | String | Listing, AgentOffice, CoListAgent |  | 11% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListAgentVoiceMail/) |
| `CoListAgentVoiceMailExt` | String | Listing, AgentOffice, CoListAgent |  | 1% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoListAgentVoiceMailExt/) |
| `CoListOffice` | Resource | Listing, AgentOffice, CoListOffice |  |  | The co-listing agent's office. | [link](https://dd.reso.org/DD2.0/Property/CoListOffice/) |
| `CoListOfficeAOR` | String List, Single | Listing, AgentOffice, CoListOffice | AOR | 27% | The co-listing office's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeAOR/) |
| `CoListOfficeEmail` | String | Listing, AgentOffice, CoListOffice |  | 75% | The email address of the co-listing office. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeEmail/) |
| `CoListOfficeFax` | String | Listing, AgentOffice, CoListOffice |  | 49% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeFax/) |
| `CoListOfficeKey` | String | Listing, AgentOffice, CoListOffice |  | 73% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeKey/) |
| `CoListOfficeMlsId` | String | Listing, AgentOffice, CoListOffice |  | 86% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeMlsId/) |
| `CoListOfficeName` | String | Listing, AgentOffice, CoListOffice |  | 85% | The legal name of the brokerage co-representing the seller. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeName/) |
| `CoListOfficeNationalAssociationId` | String | Listing, AgentOffice, CoListOffice |  | 1% | The national association ID of the co-listing office (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeNationalAssociationId/) |
| `CoListOfficePhone` | String | Listing, AgentOffice, CoListOffice |  | 78% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/CoListOfficePhone/) |
| `CoListOfficePhoneExt` | String | Listing, AgentOffice, CoListOffice |  | 8% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficePhoneExt/) |
| `CoListOfficeURL` | String | Listing, AgentOffice, CoListOffice |  | 69% | The website Uniform Resource Identifier (URI) for the co-listing office. | [link](https://dd.reso.org/DD2.0/Property/CoListOfficeURL/) |
| `CommonInterest` | String List, Single | Listing, Contract | [CommonInterest](#commoninterest) | 12% | A type of ownership in a property that is composed of an individual lot or unit and a share of the ownership or use of common areas. | [link](https://dd.reso.org/DD2.0/Property/CommonInterest/) |
| `CommonWalls` | String List, Multi | Structure | [CommonWalls](#commonwalls) | 25% | A multi-select list with options like 1 Common Wall, 2 Common Walls, No Common Walls, No One Above, No One Below. | [link](https://dd.reso.org/DD2.0/Property/CommonWalls/) |
| `CommunityFeatures` | String List, Multi | Characteristics | [CommunityFeatures](#communityfeatures) | 63% | A list of features related to or available within the community. | [link](https://dd.reso.org/DD2.0/Property/CommunityFeatures/) |
| `CompSaleYN` | Boolean | Listing |  | 3% | Indicates whether or not this sale was entered for comparative purposes. | [link](https://dd.reso.org/DD2.0/Property/CompSaleYN/) |
| `CompensationComments` | String | Listing, Compensation |  | 1% | A textual description of the compensation involved in the transaction. | [link](https://dd.reso.org/DD2.0/Property/CompensationComments/) |
| `Concessions` | String List, Single | Listing, Closing | [Concessions](#concessions) | 39% | Indicates whether or not there are concessions included in the sales agreement (i.e., Yes, No or Call Listing Agent). | [link](https://dd.reso.org/DD2.0/Property/Concessions/) |
| `ConcessionsAmount` | Number | Listing, Closing |  | 37% | The dollar amount of the concessions. | [link](https://dd.reso.org/DD2.0/Property/ConcessionsAmount/) |
| `ConcessionsComments` | String | Listing, Closing |  | 40% | The comments describing the concessions made by the buyer or the seller. | [link](https://dd.reso.org/DD2.0/Property/ConcessionsComments/) |
| `ConstructionMaterials` | String List, Multi | Structure | [ConstructionMaterials](#constructionmaterials) | 89% | A list of the materials that were used in the construction of the property. | [link](https://dd.reso.org/DD2.0/Property/ConstructionMaterials/) |
| `ContinentRegion` | String | Location, Area |  | 0% | A subsection or area of a continent (e.g., Southern Europe, Scandinavia). | [link](https://dd.reso.org/DD2.0/Property/ContinentRegion/) |
| `Contingency` | String | Listing, Closing |  | 43% | A list of contingencies that must be satisfied in order to complete the transaction. | [link](https://dd.reso.org/DD2.0/Property/Contingency/) |
| `ContingentDate` | Date | Listing, Dates |  | 36% | The date an offer was made with a contingency. | [link](https://dd.reso.org/DD2.0/Property/ContingentDate/) |
| `ContractStatusChangeDate` | Date | Listing, Dates |  | 72% | The date of the listing's contractual status change. | [link](https://dd.reso.org/DD2.0/Property/ContractStatusChangeDate/) |
| `Cooling` | String List, Multi | Structure | [Cooling](#cooling) | 90% | A list describing the cooling or air conditioning features of the property. | [link](https://dd.reso.org/DD2.0/Property/Cooling/) |
| `CoolingYN` | Boolean | Structure |  | 81% | Indicates whether or not the property has some form of cooling or air conditioning. | [link](https://dd.reso.org/DD2.0/Property/CoolingYN/) |
| `CopyrightNotice` | String | Listing |  | 1% | A notice of the legal rights of the owner of the information or data. | [link](https://dd.reso.org/DD2.0/Property/CopyrightNotice/) |
| `Country` | String List, Single | Location, Address | [Country](#country) | 41% | The country in which the property is located, as an ISO country code. | [link](https://dd.reso.org/DD2.0/Property/Country/) |
| `CountryRegion` | String | Location, Area |  | 1% | A subsection or area of a defined country (e.g., Napa Valley in the U.S., the Amalfi Coast in Italy). | [link](https://dd.reso.org/DD2.0/Property/CountryRegion/) |
| `CountyOrParish` | String List, Single | Location, Address | CountyOrParish | 95% | The county, parish or other regional authority. | [link](https://dd.reso.org/DD2.0/Property/CountyOrParish/) |
| `CoveredSpaces` | Number | Structure |  | 42% | The total number of garage and carport spaces. | [link](https://dd.reso.org/DD2.0/Property/CoveredSpaces/) |
| `CropsIncludedYN` | Boolean | Farming |  | 8% | Indicates whether or not crops are included in the sale of the property. | [link](https://dd.reso.org/DD2.0/Property/CropsIncludedYN/) |
| `CrossStreet` | String | Location, GIS |  | 25% | The nearest cross streets to the property. | [link](https://dd.reso.org/DD2.0/Property/CrossStreet/) |
| `CultivatedArea` | Number | Farming |  | 22% | The measurement or percentage of the property that has been cultivated. | [link](https://dd.reso.org/DD2.0/Property/CultivatedArea/) |
| `CumulativeDaysOnMarket` | Number | Listing, Dates |  | 60% | The cumulative number of days the property is on market, as defined by the MLS business rules. | [link](https://dd.reso.org/DD2.0/Property/CumulativeDaysOnMarket/) |
| `CurrentFinancing` | String List, Multi | Listing, Contract | [CurrentFinancing](#currentfinancing) | 26% | A list of options that describe the type of financing that the seller currently has in place for the property being sold (i.e., Cash, FHA Loan, etc.). | [link](https://dd.reso.org/DD2.0/Property/CurrentFinancing/) |
| `CurrentUse` | String List, Multi | Characteristics | [CurrentOrPossibleUse](#currentorpossibleuse) | 63% | A list of the type(s) of current use of the property. | [link](https://dd.reso.org/DD2.0/Property/CurrentUse/) |
| `DOH1` | String | Structure |  | 8% | The Department of Housing decal number for the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/DOH1/) |
| `DOH2` | String | Structure |  | 4% | The Department of Housing decal number for the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/DOH2/) |
| `DOH3` | String | Structure |  | 3% | The Department of Housing decal number for the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/DOH3/) |
| `DaysInMls` | Number | Listing, Dates |  |  | The number of days the listing was on market within the MLS system. | [link](https://dd.reso.org/DD2.0/Property/DaysInMls/) |
| `DaysOnMarket` | Number | Listing, Dates |  | 94% | The number of days the listing is on market, as defined by the MLS business rules. | [link](https://dd.reso.org/DD2.0/Property/DaysOnMarket/) |
| `DaysOnSite` | Number | Listing, Dates |  |  | The number of days the listing appeared on the given site, typically a public portal. | [link](https://dd.reso.org/DD2.0/Property/DaysOnSite/) |
| `DevelopmentStatus` | String List, Multi | Characteristics | [DevelopmentStatus](#developmentstatus) | 28% | The development phase of the property. | [link](https://dd.reso.org/DD2.0/Property/DevelopmentStatus/) |
| `DirectionFaces` | String List, Single | Structure | [DirectionFaces](#directionfaces) | 24% | The compass direction that the main entrance to the building faces (e.g., North, South, East, West, Northeast, Southwest). | [link](https://dd.reso.org/DD2.0/Property/DirectionFaces/) |
| `Directions` | String | Location, GIS |  | 95% | Driving directions to the property. | [link](https://dd.reso.org/DD2.0/Property/Directions/) |
| `Disclaimer` | String | Listing |  | 8% | Text that serves as the negation or limitation of the rights under a warranty given by a seller to a buyer. | [link](https://dd.reso.org/DD2.0/Property/Disclaimer/) |
| `Disclosures` | String List, Multi | Listing, Contract | Disclosures | 52% | Legal or pertinent information that should be disclosed to potential buyer's agents. | [link](https://dd.reso.org/DD2.0/Property/Disclosures/) |
| `DistanceToBusComments` | String | Location |  | 3% | A textual description of the distance to local bus stops. | [link](https://dd.reso.org/DD2.0/Property/DistanceToBusComments/) |
| `DistanceToBusNumeric` | Number | Location |  | 1% | The numeric distance from the property to the nearest bus stop. | [link](https://dd.reso.org/DD2.0/Property/DistanceToBusNumeric/) |
| `DistanceToBusUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToBusUnits/) |
| `DistanceToElectricComments` | String | Utilities |  | 8% | Provides details about the property's access to serviceable electrical utility and the distance to it. | [link](https://dd.reso.org/DD2.0/Property/DistanceToElectricComments/) |
| `DistanceToElectricNumeric` | Number | Utilities |  | 1% | The numeric distance from the property to the electrical utility. | [link](https://dd.reso.org/DD2.0/Property/DistanceToElectricNumeric/) |
| `DistanceToElectricUnits` | String List, Single | Utilities | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToElectricUnits/) |
| `DistanceToFreewayComments` | String | Location |  | 2% | A textual description of the distance to freeways. | [link](https://dd.reso.org/DD2.0/Property/DistanceToFreewayComments/) |
| `DistanceToFreewayNumeric` | Number | Location |  | 2% | The numeric distance from the property to the nearest freeway. | [link](https://dd.reso.org/DD2.0/Property/DistanceToFreewayNumeric/) |
| `DistanceToFreewayUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToFreewayUnits/) |
| `DistanceToGasComments` | String | Utilities |  | 5% | Provides details about the property's access to serviceable natural gas utility and the distance to it. | [link](https://dd.reso.org/DD2.0/Property/DistanceToGasComments/) |
| `DistanceToGasNumeric` | Number | Utilities |  | 1% | The numeric distance from the property to the gas utility. | [link](https://dd.reso.org/DD2.0/Property/DistanceToGasNumeric/) |
| `DistanceToGasUnits` | String List, Single | Utilities | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToGasUnits/) |
| `DistanceToPhoneServiceComments` | String | Utilities |  | 5% | Provides details about the property's access to phone service and the distance to it. | [link](https://dd.reso.org/DD2.0/Property/DistanceToPhoneServiceComments/) |
| `DistanceToPhoneServiceNumeric` | Number | Utilities |  | 0% | The numeric distance from the property to the phone utility. | [link](https://dd.reso.org/DD2.0/Property/DistanceToPhoneServiceNumeric/) |
| `DistanceToPhoneServiceUnits` | String List, Single | Utilities | [LinearUnits](#linearunits) | 0% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToPhoneServiceUnits/) |
| `DistanceToPlaceofWorshipComments` | String | Location |  | 1% | A textual description of the distance to local places of worship. | [link](https://dd.reso.org/DD2.0/Property/DistanceToPlaceofWorshipComments/) |
| `DistanceToPlaceofWorshipNumeric` | Number | Location |  | 1% | The numeric distance from the property to the nearest place of worship. | [link](https://dd.reso.org/DD2.0/Property/DistanceToPlaceofWorshipNumeric/) |
| `DistanceToPlaceofWorshipUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToPlaceofWorshipUnits/) |
| `DistanceToSchoolBusComments` | String | Location |  | 1% | Distance from the property to the nearest school bus pickup point. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolBusComments/) |
| `DistanceToSchoolBusNumeric` | Number | Location |  | 1% | The numeric distance from the property to the nearest school bus pickup point. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolBusNumeric/) |
| `DistanceToSchoolBusUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolBusUnits/) |
| `DistanceToSchoolsComments` | String | Location |  | 2% | A textual description of the distance to local schools. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolsComments/) |
| `DistanceToSchoolsNumeric` | Number | Location |  | 2% | The numeric distance from the property to the nearest school. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolsNumeric/) |
| `DistanceToSchoolsUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 2% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToSchoolsUnits/) |
| `DistanceToSewerComments` | String | Utilities |  | 6% | Provides details about the property's access to sewer or septic service and the distance to it. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSewerComments/) |
| `DistanceToSewerNumeric` | Number | Utilities |  | 1% | The numeric distance from the property to the sewer utility. | [link](https://dd.reso.org/DD2.0/Property/DistanceToSewerNumeric/) |
| `DistanceToSewerUnits` | String List, Single | Utilities | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToSewerUnits/) |
| `DistanceToShoppingComments` | String | Location |  | 3% | A description of the distance to primary shopping sources, such as groceries, gasoline, clothing or department stores. | [link](https://dd.reso.org/DD2.0/Property/DistanceToShoppingComments/) |
| `DistanceToShoppingNumeric` | Number | Location |  | 1% | The numeric distance from the property to the nearest shopping. | [link](https://dd.reso.org/DD2.0/Property/DistanceToShoppingNumeric/) |
| `DistanceToShoppingUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToShoppingUnits/) |
| `DistanceToStreetComments` | String | Location |  | 2% | Provides details about the property's access to a maintained road or street adjacent to the lot, conditions of access and distance to a maintained road. | [link](https://dd.reso.org/DD2.0/Property/DistanceToStreetComments/) |
| `DistanceToStreetNumeric` | Number | Location |  | 1% | The numeric distance from the property to the street. | [link](https://dd.reso.org/DD2.0/Property/DistanceToStreetNumeric/) |
| `DistanceToStreetUnits` | String List, Single | Location | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToStreetUnits/) |
| `DistanceToWaterComments` | String | Utilities |  | 7% | Provides details about the property's access to serviceable water utility and the distance to it. | [link](https://dd.reso.org/DD2.0/Property/DistanceToWaterComments/) |
| `DistanceToWaterNumeric` | Number | Utilities |  | 1% | The numeric distance from the property to the water utility. | [link](https://dd.reso.org/DD2.0/Property/DistanceToWaterNumeric/) |
| `DistanceToWaterUnits` | String List, Single | Utilities | [LinearUnits](#linearunits) | 1% | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). | [link](https://dd.reso.org/DD2.0/Property/DistanceToWaterUnits/) |
| `DocumentStatus` | String List, Single | Listing, Media | [DocumentStatus](#documentstatus) |  | The statuses a document could be in during a transaction. | [link](https://dd.reso.org/DD2.0/Property/DocumentStatus/) |
| `DocumentsAvailable` | String List, Multi | Listing, Media | DocumentsAvailable | 72% | A list of the documents available for the property. | [link](https://dd.reso.org/DD2.0/Property/DocumentsAvailable/) |
| `DocumentsChangeTimestamp` | Timestamp | Listing, Media |  | 78% | The system-generated timestamp of when the last update or change to the documents for this listing was made. | [link](https://dd.reso.org/DD2.0/Property/DocumentsChangeTimestamp/) |
| `DocumentsCount` | Number | Listing, Media |  | 86% | The total number of documents or supplements included with the listing. | [link](https://dd.reso.org/DD2.0/Property/DocumentsCount/) |
| `DoorFeatures` | String List, Multi | Structure | [DoorFeatures](#doorfeatures) | 51% | A list of features or description of the doors included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/DoorFeatures/) |
| `DualOrVariableRateCommissionYN` | Boolean | Listing, Compensation |  | 1% | A commission arrangement in which the seller agrees to pay a specified commission to the listing broker if the property is sold through the efforts of a cooperating broker. | [link](https://dd.reso.org/DD2.0/Property/DualOrVariableRateCommissionYN/) |
| `Electric` | String List, Multi | Utilities | [Electric](#electric) | 66% | A list of electric-service related features of the property (e.g., 110 Volt, 3 Phase, 220 Volt, RV Hookup). | [link](https://dd.reso.org/DD2.0/Property/Electric/) |
| `ElectricExpense` | Number | Financial |  | 23% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/ElectricExpense/) |
| `ElectricOnPropertyYN` | Boolean | Utilities |  | 33% | Indicates whether or not the property currently has electrical utility available on the property. | [link](https://dd.reso.org/DD2.0/Property/ElectricOnPropertyYN/) |
| `ElementarySchool` | String List, Single | Location, School | ElementarySchool | 56% | The name of the primary school having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/ElementarySchool/) |
| `ElementarySchoolDistrict` | String List, Single | Location, School | ElementarySchoolDistrict | 28% | The name of the elementary school district having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/ElementarySchoolDistrict/) |
| `Elevation` | Number | Location, GIS |  | 8% | The elevation of the property in relation to sea level. | [link](https://dd.reso.org/DD2.0/Property/Elevation/) |
| `ElevationUnits` | String List, Single | Location, GIS | [LinearUnits](#linearunits) | 3% | A pick list of the unit of measurement used in the Elevation field (i.e., Feet, Meters). | [link](https://dd.reso.org/DD2.0/Property/ElevationUnits/) |
| `EntryLevel` | Number | Structure |  | 24% | A numeric field that describes the level within the structure, single-family residence (SFR) or a unit in a building, where the main entry to the dwelling is located. | [link](https://dd.reso.org/DD2.0/Property/EntryLevel/) |
| `EntryLocation` | String | Structure |  | 18% | A description of the main entry way to the property (e.g., elevator, ground level w/ steps, ground level w/o steps, top level). | [link](https://dd.reso.org/DD2.0/Property/EntryLocation/) |
| `Exclusions` | String | Listing, Contract |  | 32% | Elements of the property that will not be included in the sale (e.g., chandeliers removed prior to close). | [link](https://dd.reso.org/DD2.0/Property/Exclusions/) |
| `ExistingLeaseType` | String List, Multi | Financial | [ExistingLeaseType](#existingleasetype) | 43% | Information about the status of the existing lease on the property (i.e., Net, NNN, NN, Gross, Absolute Net, Escalation Clause, Ground Lease). | [link](https://dd.reso.org/DD2.0/Property/ExistingLeaseType/) |
| `ExpirationDate` | Date | Listing, Dates |  | 65% | The date when the listing agreement will expire. | [link](https://dd.reso.org/DD2.0/Property/ExpirationDate/) |
| `ExteriorFeatures` | String List, Multi | Structure | [ExteriorFeatures](#exteriorfeatures) | 85% | A list of features or a description of the exterior of the property included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/ExteriorFeatures/) |
| `FarmCreditServiceInclYN` | Boolean | Farming |  | 1% | Indicates whether or not Farm Credit Service shares are included in the price of the property. | [link](https://dd.reso.org/DD2.0/Property/FarmCreditServiceInclYN/) |
| `FarmLandAreaSource` | String List, Single | Farming | [AreaSource](#areasource) | 1% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/FarmLandAreaSource/) |
| `FarmLandAreaUnits` | String List, Single | Farming | [AreaUnits](#areaunits) | 11% | A pick list of the unit of measurement for the area (i.e., Square Feet, Square Meters, Acres, etc.). | [link](https://dd.reso.org/DD2.0/Property/FarmLandAreaUnits/) |
| `Fencing` | String List, Multi | Characteristics | [Fencing](#fencing) | 78% | A list of types of fencing found at the property being sold. | [link](https://dd.reso.org/DD2.0/Property/Fencing/) |
| `FhaEligibility` | String List, Single | Listing, Closing | [FhaEligibility](#fhaeligibility) |  | The status of the property's FHA eligibility. | [link](https://dd.reso.org/DD2.0/Property/FhaEligibility/) |
| `FinancialDataSource` | String List, Multi | Financial | [FinancialDataSource](#financialdatasource) | 12% | The source of the rental information (e.g., Accountant, Owner). | [link](https://dd.reso.org/DD2.0/Property/FinancialDataSource/) |
| `FireplaceFeatures` | String List, Multi | Structure | [FireplaceFeatures](#fireplacefeatures) | 81% | A list of features or a description of the fireplace(s) included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/FireplaceFeatures/) |
| `FireplaceYN` | Boolean | Structure |  | 78% | Does the property include a fireplace. | [link](https://dd.reso.org/DD2.0/Property/FireplaceYN/) |
| `FireplacesTotal` | Number | Structure |  | 53% | Indicates whether or not the property includes a fireplace. | [link](https://dd.reso.org/DD2.0/Property/FireplacesTotal/) |
| `Flooring` | String List, Multi | Structure | [Flooring](#flooring) | 84% | A list of the type(s) of flooring found within the property. | [link](https://dd.reso.org/DD2.0/Property/Flooring/) |
| `FoundationArea` | Number | Structure |  | 4% | The area or dimensions of the footprint of the structure on the lot. | [link](https://dd.reso.org/DD2.0/Property/FoundationArea/) |
| `FoundationDetails` | String List, Multi | Structure | [FoundationDetails](#foundationdetails) | 78% | A list of the type(s) of foundation on which the property sits. | [link](https://dd.reso.org/DD2.0/Property/FoundationDetails/) |
| `FrontageLength` | String | Characteristics |  | 29% | A textual description of the length of the frontages selected in the Frontage Type field. | [link](https://dd.reso.org/DD2.0/Property/FrontageLength/) |
| `FrontageType` | String List, Multi | Characteristics | [FrontageType](#frontagetype) | 35% | A pick list of types of frontage (i.e., Oceanfront, Lakefront, Golf Course, etc.). | [link](https://dd.reso.org/DD2.0/Property/FrontageType/) |
| `FuelExpense` | Number | Financial |  | 17% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/FuelExpense/) |
| `Furnished` | String List, Single | Characteristics | [Furnished](#furnished) | 54% | The property being leased is furnished, unfurnished or partially furnished. | [link](https://dd.reso.org/DD2.0/Property/Furnished/) |
| `FurnitureReplacementExpense` | Number | Financial |  | 1% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/FurnitureReplacementExpense/) |
| `GarageSpaces` | Number | Structure |  | 84% | The number of spaces in the garage(s). | [link](https://dd.reso.org/DD2.0/Property/GarageSpaces/) |
| `GarageYN` | Boolean | Structure |  | 82% | A flag that indicates whether or not the listing has a garage. | [link](https://dd.reso.org/DD2.0/Property/GarageYN/) |
| `GardenerExpense` | Number | Financial |  | 5% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/GardenerExpense/) |
| `GrazingPermitsBlmYN` | Boolean | Farming |  | 1% | Indicates whether or not the property owner has grazing permits from the Bureau of Land Management. | [link](https://dd.reso.org/DD2.0/Property/GrazingPermitsBlmYN/) |
| `GrazingPermitsForestServiceYN` | Boolean | Farming |  | 1% | Indicates whether or not the property owner has grazing permits from the Forestry Service. | [link](https://dd.reso.org/DD2.0/Property/GrazingPermitsForestServiceYN/) |
| `GrazingPermitsPrivateYN` | Boolean | Farming |  | 2% | Indicates whether or not the property owner has private grazing permits. | [link](https://dd.reso.org/DD2.0/Property/GrazingPermitsPrivateYN/) |
| `GreenBuildingVerification` | Collection | Structure, Performance, GreenVerification |  |  | A collection of verifications or certifications awarded to a new or pre-existing residential or commercial structure (e.g., LEED, Energy Star, ICC-700). | [link](https://dd.reso.org/DD2.0/Property/GreenBuildingVerification/) |
| `GreenBuildingVerificationType` | String List, Multi | Structure, Performance, GreenVerification | [GreenBuildingVerificationType](#greenbuildingverificationtype) | 23% | The name of the verification or certification awarded to a new or pre-existing residential or commercial structure (e.g., LEED, ENERGY STAR, ICC-700). | [link](https://dd.reso.org/DD2.0/Property/GreenBuildingVerificationType/) |
| `GreenEnergyEfficient` | String List, Multi | Structure, Performance, GreenMarketing | [GreenEnergyEfficient](#greenenergyefficient) | 47% | A pick list of general green attributes such as energy efficient doors or appliances without naming specific elements with ratings that may wane over time. | [link](https://dd.reso.org/DD2.0/Property/GreenEnergyEfficient/) |
| `GreenEnergyGeneration` | String List, Multi | Structure, Performance, GreenMarketing | [GreenEnergyGeneration](#greenenergygeneration) | 39% | The methods of generating power that are included in the sale or lease. | [link](https://dd.reso.org/DD2.0/Property/GreenEnergyGeneration/) |
| `GreenIndoorAirQuality` | String List, Multi | Structure, Performance, GreenMarketing | [GreenIndoorAirQuality](#greenindoorairquality) | 19% | A pick list of indoor air quality measures without naming specific elements with ratings that may wane over time. | [link](https://dd.reso.org/DD2.0/Property/GreenIndoorAirQuality/) |
| `GreenLocation` | String List, Multi | Structure, Performance, GreenMarketing | GreenLocation | 3% | A pick list describing efficiencies involved with the property's location such as walkability or transportation proximity without naming specific elements with ratings that may wane over time. | [link](https://dd.reso.org/DD2.0/Property/GreenLocation/) |
| `GreenSustainability` | String List, Multi | Structure, Performance, GreenMarketing | [GreenSustainability](#greensustainability) | 13% | A pick list of sustainable elements used in the construction of the structure without naming specific elements with ratings that may wane over time. | [link](https://dd.reso.org/DD2.0/Property/GreenSustainability/) |
| `GreenVerificationYN` | Boolean | Structure, Performance, GreenVerification |  | 1% | A flag indicating that the listing has a Green Verification. | [link](https://dd.reso.org/DD2.0/Property/GreenVerificationYN/) |
| `GreenWaterConservation` | String List, Multi | Structure, Performance, GreenMarketing | [GreenWaterConservation](#greenwaterconservation) | 28% | A pick list of general water conserving attributes of the property such as landscaping or reclamation without naming specific elements with ratings that may wane over time. | [link](https://dd.reso.org/DD2.0/Property/GreenWaterConservation/) |
| `GrossIncome` | Number | Financial |  | 65% | The actual current income from rent and all other revenue-generating sources. | [link](https://dd.reso.org/DD2.0/Property/GrossIncome/) |
| `GrossLivingAreaAnsi` | Number | Structure |  |  | The total livable area with the structure as measured using American National Standards Institute (ANSI) measurement guidelines. | [link](https://dd.reso.org/DD2.0/Property/GrossLivingAreaAnsi/) |
| `GrossScheduledIncome` | Number | Financial |  | 26% | The maximum amount of annual rent collected if the property were 100% occupied all year and all tenants paid their rent. | [link](https://dd.reso.org/DD2.0/Property/GrossScheduledIncome/) |
| `HabitableResidenceYN` | Boolean | Structure |  | 12% | Indicates whether or not the property includes a structure that can be lived in. | [link](https://dd.reso.org/DD2.0/Property/HabitableResidenceYN/) |
| `Heating` | String List, Multi | Structure | [Heating](#heating) | 90% | A list describing the heating features of the property. | [link](https://dd.reso.org/DD2.0/Property/Heating/) |
| `HeatingYN` | Boolean | Structure |  | 81% | Indicates whether or not the property has heating. | [link](https://dd.reso.org/DD2.0/Property/HeatingYN/) |
| `HighSchool` | String List, Single | Location, School | HighSchool | 53% | The name of the high school having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/HighSchool/) |
| `HighSchoolDistrict` | String List, Single | Location, School | HighSchoolDistrict | 47% | The name of the high school district having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/HighSchoolDistrict/) |
| `HistoryTransactional` | Collection | Listing |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/Property/HistoryTransactional/) |
| `HomeWarrantyYN` | Boolean | Listing |  | 49% | Indicates whether or not a home warranty is included in the sale of the property. | [link](https://dd.reso.org/DD2.0/Property/HomeWarrantyYN/) |
| `HorseAmenities` | String List, Multi | Characteristics | [HorseAmenities](#horseamenities) | 40% | A list of horse amenities on the lot or in the community. | [link](https://dd.reso.org/DD2.0/Property/HorseAmenities/) |
| `HorseYN` | Boolean | Characteristics |  | 44% | Indicates whether or not the property allows for the raising of horses. | [link](https://dd.reso.org/DD2.0/Property/HorseYN/) |
| `HoursDaysOfOperation` | String List, Multi | Business | [HoursDaysOfOperation](#hoursdaysofoperation) | 6% | A simplified enumerated list of the days and hours of operation of the business being sold (e.g., Open 24 Hours, Open Seven Days). | [link](https://dd.reso.org/DD2.0/Property/HoursDaysOfOperation/) |
| `HoursDaysOfOperationDescription` | String | Business |  | 5% | A detailed description of the hours and days the business being sold is open for business. | [link](https://dd.reso.org/DD2.0/Property/HoursDaysOfOperationDescription/) |
| `Inclusions` | String | Listing, Contract |  | 48% | Portable elements of the property that will be included in the sale. | [link](https://dd.reso.org/DD2.0/Property/Inclusions/) |
| `IncomeIncludes` | String List, Multi | Financial | [IncomeIncludes](#incomeincludes) | 9% | A list of income sources included in the GrossScheduledIncome and GrossIncome (e.g., Laundry, Parking, Recreation, Storage). | [link](https://dd.reso.org/DD2.0/Property/IncomeIncludes/) |
| `InsuranceExpense` | Number | Financial |  | 44% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/InsuranceExpense/) |
| `InteriorFeatures` | String List, Multi | Structure | [InteriorOrRoomFeatures](#interiororroomfeatures) | 88% | A list of features or a description of the interior of the property included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/InteriorFeatures/) |
| `InternetAddressDisplayYN` | Boolean | Listing, Marketing |  | 98% | Indicates whether or not the seller has allowed the listing address to be displayed on Internet sites. | [link](https://dd.reso.org/DD2.0/Property/InternetAddressDisplayYN/) |
| `InternetAutomatedValuationDisplayYN` | Boolean | Listing, Marketing |  | 90% | Indicates whether or not the seller allows the listing to be displayed with an automated valuation model (AVM) on Internet sites. | [link](https://dd.reso.org/DD2.0/Property/InternetAutomatedValuationDisplayYN/) |
| `InternetConsumerCommentYN` | Boolean | Listing, Marketing |  | 89% | Indicates whether or not the seller allows a comment or blog system to be attached to the listing on Internet sites. | [link](https://dd.reso.org/DD2.0/Property/InternetConsumerCommentYN/) |
| `InternetEntireListingDisplayYN` | Boolean | Listing, Marketing |  | 96% | Indicates whether or not the seller has allowed the listing to be displayed on Internet sites. | [link](https://dd.reso.org/DD2.0/Property/InternetEntireListingDisplayYN/) |
| `IrrigationSource` | String List, Multi | Utilities | IrrigationSource | 22% | The source which the property receives its water for irrigation. | [link](https://dd.reso.org/DD2.0/Property/IrrigationSource/) |
| `IrrigationWaterRightsAcres` | Number | Utilities |  | 5% | The number of acres allowed under the property's water rights. | [link](https://dd.reso.org/DD2.0/Property/IrrigationWaterRightsAcres/) |
| `IrrigationWaterRightsYN` | Boolean | Utilities |  | 11% | Indicates whether or not the property includes water rights for irrigation. | [link](https://dd.reso.org/DD2.0/Property/IrrigationWaterRightsYN/) |
| `LaborInformation` | String List, Multi | Business | [LaborInformation](#laborinformation) | 4% | Information about labor laws that are applicable to the business being sold (i.e., Union, Non-Union, Employee License Required). | [link](https://dd.reso.org/DD2.0/Property/LaborInformation/) |
| `LandLeaseAmount` | Number | Characteristics |  | 17% | When the land is not included in the sale, but is leased, the amount of the lease. | [link](https://dd.reso.org/DD2.0/Property/LandLeaseAmount/) |
| `LandLeaseAmountFrequency` | String List, Single | Characteristics | [FeeFrequency](#feefrequency) | 7% | The frequency in which the land lease fee is paid when the land is not included in the sale but is leased. | [link](https://dd.reso.org/DD2.0/Property/LandLeaseAmountFrequency/) |
| `LandLeaseExpirationDate` | Date | Characteristics |  | 5% | The expiration date of the land lease when the land is not included in the sale but is leased. | [link](https://dd.reso.org/DD2.0/Property/LandLeaseExpirationDate/) |
| `LandLeaseYN` | Boolean | Characteristics |  | 36% | The land is not included in the sale and a lease exists. | [link](https://dd.reso.org/DD2.0/Property/LandLeaseYN/) |
| `Latitude` | Number | Location, GIS |  | 96% | The geographic latitude of the property in decimal degrees. | [link](https://dd.reso.org/DD2.0/Property/Latitude/) |
| `LaundryFeatures` | String List, Multi | Characteristics | [LaundryFeatures](#laundryfeatures) | 75% | Add this pick list of features and locations where the laundry is located in the property being sold (i.e., Gas Dryer Hookup, In Kitchen, In Garage, etc.). | [link](https://dd.reso.org/DD2.0/Property/LaundryFeatures/) |
| `LeasableArea` | Number | Structure |  | 22% | The area that may be leased within the commercial property. | [link](https://dd.reso.org/DD2.0/Property/LeasableArea/) |
| `LeasableAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 9% | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/LeasableAreaUnits/) |
| `LeaseAmount` | Number | Business |  | 26% | The current lease amount of the property as a single value or a periodic payment per LeaseAmountFrequency. | [link](https://dd.reso.org/DD2.0/Property/LeaseAmount/) |
| `LeaseAmountFrequency` | String List, Single | Business | [FeeFrequency](#feefrequency) | 15% | The frequency of the lease amount. | [link](https://dd.reso.org/DD2.0/Property/LeaseAmountFrequency/) |
| `LeaseAssignableYN` | Boolean | Business |  | 6% | Indicates whether or not the lease at the current location of the business can be assigned to another party. | [link](https://dd.reso.org/DD2.0/Property/LeaseAssignableYN/) |
| `LeaseConsideredYN` | Boolean | Listing |  | 33% | A flag indicating that the seller would consider leasing the property in addition to a sale. | [link](https://dd.reso.org/DD2.0/Property/LeaseConsideredYN/) |
| `LeaseExpiration` | Date | Business |  | 18% | The expiration date of the lease for the current location of the business. | [link](https://dd.reso.org/DD2.0/Property/LeaseExpiration/) |
| `LeaseRenewalCompensation` | String List, Multi | Listing, Compensation | [LeaseRenewalCompensation](#leaserenewalcompensation) | 5% | A list of compensations other than the original selling office compensation (i.e., Paid on Renewal, Paid on Tenant Purchase, No Renewal Commission, Call Listing Office, etc.). | [link](https://dd.reso.org/DD2.0/Property/LeaseRenewalCompensation/) |
| `LeaseRenewalOptionYN` | Boolean | Business |  | 14% | Indicates whether or not there is an option to renew the lease at the current location of the business. | [link](https://dd.reso.org/DD2.0/Property/LeaseRenewalOptionYN/) |
| `LeaseTerm` | String List, Single | Characteristics | [LeaseTerm](#leaseterm) | 57% | A pick list of lengths that represent the length of the lease (e.g., Weekly, Month to Month, 6-Month Lease, 12-Month Lease, 2-Year Lease). | [link](https://dd.reso.org/DD2.0/Property/LeaseTerm/) |
| `Levels` | String List, Multi | Structure | [Levels](#levels) | 78% | The number of levels in the property being sold (e.g., One, Two, Three or More, Multi/Split). | [link](https://dd.reso.org/DD2.0/Property/Levels/) |
| `License1` | String | Structure |  | 7% | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. | [link](https://dd.reso.org/DD2.0/Property/License1/) |
| `License2` | String | Structure |  | 4% | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. | [link](https://dd.reso.org/DD2.0/Property/License2/) |
| `License3` | String | Structure |  | 2% | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. | [link](https://dd.reso.org/DD2.0/Property/License3/) |
| `LicensesExpense` | Number | Financial |  | 6% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/LicensesExpense/) |
| `ListAOR` | String List, Single | Listing | AOR | 32% | The responsible board or association of REALTORS® for this listing. | [link](https://dd.reso.org/DD2.0/Property/ListAOR/) |
| `ListAgent` | Resource | Listing, AgentOffice, ListAgent |  |  | The listing agent involved in the transaction. | [link](https://dd.reso.org/DD2.0/Property/ListAgent/) |
| `ListAgentAOR` | String List, Single | Listing, AgentOffice, ListAgent | AOR | 32% | The listing agent's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/ListAgentAOR/) |
| `ListAgentDesignation` | String List, Multi | Listing, AgentOffice, ListAgent | [ListAgentDesignation](#listagentdesignation) | 30% | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completi… | [link](https://dd.reso.org/DD2.0/Property/ListAgentDesignation/) |
| `ListAgentDirectPhone` | String | Listing, AgentOffice, ListAgent |  | 59% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentDirectPhone/) |
| `ListAgentEmail` | String | Listing, AgentOffice, ListAgent |  | 89% | The email address of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentEmail/) |
| `ListAgentFax` | String | Listing, AgentOffice, ListAgent |  | 47% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentFax/) |
| `ListAgentFirstName` | String | Listing, AgentOffice, ListAgent |  | 93% | The first name of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentFirstName/) |
| `ListAgentFullName` | String | Listing, AgentOffice, ListAgent |  | 91% | The full name of the listing agent of record. | [link](https://dd.reso.org/DD2.0/Property/ListAgentFullName/) |
| `ListAgentHomePhone` | String | Listing, AgentOffice, ListAgent |  | 41% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentHomePhone/) |
| `ListAgentKey` | String | Listing, AgentOffice, ListAgent |  | 78% | A system-unique identifier for the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentKey/) |
| `ListAgentLastName` | String | Listing, AgentOffice, ListAgent |  | 93% | The last name of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentLastName/) |
| `ListAgentMiddleName` | String | Listing, AgentOffice, ListAgent |  | 65% | The middle name of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentMiddleName/) |
| `ListAgentMlsId` | String | Listing, AgentOffice, ListAgent |  | 96% | The local, well-known identifier for the member. | [link](https://dd.reso.org/DD2.0/Property/ListAgentMlsId/) |
| `ListAgentMobilePhone` | String | Listing, AgentOffice, ListAgent |  | 59% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentMobilePhone/) |
| `ListAgentNamePrefix` | String | Listing, AgentOffice, ListAgent |  | 0% | The prefix to the name (e.g., Dr., Mr., Ms.). | [link](https://dd.reso.org/DD2.0/Property/ListAgentNamePrefix/) |
| `ListAgentNameSuffix` | String | Listing, AgentOffice, ListAgent |  | 1% | The suffix to the name (e.g., Esq., Jr., III). | [link](https://dd.reso.org/DD2.0/Property/ListAgentNameSuffix/) |
| `ListAgentNationalAssociationId` | String | Listing, AgentOffice, ListAgent |  | 21% | The national association ID of the listing agent (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/ListAgentNationalAssociationId/) |
| `ListAgentOfficePhone` | String | Listing, AgentOffice, ListAgent |  | 67% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentOfficePhone/) |
| `ListAgentOfficePhoneExt` | String | Listing, AgentOffice, ListAgent |  | 36% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/Property/ListAgentOfficePhoneExt/) |
| `ListAgentPager` | String | Listing, AgentOffice, ListAgent |  | 19% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentPager/) |
| `ListAgentPreferredPhone` | String | Listing, AgentOffice, ListAgent |  | 81% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentPreferredPhone/) |
| `ListAgentPreferredPhoneExt` | String | Listing, AgentOffice, ListAgent |  | 33% | The extension of the given phone number (if applicable). | [link](https://dd.reso.org/DD2.0/Property/ListAgentPreferredPhoneExt/) |
| `ListAgentStateLicense` | String | Listing, AgentOffice, ListAgent |  | 60% | The license of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentStateLicense/) |
| `ListAgentTollFreePhone` | String | Listing, AgentOffice, ListAgent |  | 25% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentTollFreePhone/) |
| `ListAgentURL` | String | Listing, AgentOffice, ListAgent |  | 78% | The website Uniform Resource Identifier (URI) of the listing agent. | [link](https://dd.reso.org/DD2.0/Property/ListAgentURL/) |
| `ListAgentVoiceMail` | String | Listing, AgentOffice, ListAgent |  | 15% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListAgentVoiceMail/) |
| `ListAgentVoiceMailExt` | String | Listing, AgentOffice, ListAgent |  | 2% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/ListAgentVoiceMailExt/) |
| `ListOffice` | Resource | Listing, AgentOffice, ListOffice |  |  | The listing agent's office. | [link](https://dd.reso.org/DD2.0/Property/ListOffice/) |
| `ListOfficeAOR` | String List, Single | Listing, AgentOffice, ListOffice | AOR | 29% | The listing office's board or association of REALTORS®. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeAOR/) |
| `ListOfficeEmail` | String | Listing, AgentOffice, ListOffice |  | 84% | The email address of the listing office. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeEmail/) |
| `ListOfficeFax` | String | Listing, AgentOffice, ListOffice |  | 59% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListOfficeFax/) |
| `ListOfficeKey` | String | Listing, AgentOffice, ListOffice |  | 94% | The unique identifier of the brokerage Office responsible for marketing the listing. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeKey/) |
| `ListOfficeMlsId` | String | Listing, AgentOffice, ListOffice |  | 97% | The local, well-known identifier. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeMlsId/) |
| `ListOfficeName` | String | Listing, AgentOffice, ListOffice |  | 97% | The legal name of the brokerage representing the seller. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeName/) |
| `ListOfficeNationalAssociationId` | String | Listing, AgentOffice, ListOffice |  | 1% | The national association ID of the listing office (e.g., the NRDS number in the U.S.). | [link](https://dd.reso.org/DD2.0/Property/ListOfficeNationalAssociationId/) |
| `ListOfficePhone` | String | Listing, AgentOffice, ListOffice |  | 88% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ListOfficePhone/) |
| `ListOfficePhoneExt` | String | Listing, AgentOffice, ListOffice |  | 18% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/ListOfficePhoneExt/) |
| `ListOfficeURL` | String | Listing, AgentOffice, ListOffice |  | 79% | The website Uniform Resource Identifier (URI) for the listing office. | [link](https://dd.reso.org/DD2.0/Property/ListOfficeURL/) |
| `ListPrice` | Number | Listing, Price |  | 100% | The current price of the property as listed by the seller. | [link](https://dd.reso.org/DD2.0/Property/ListPrice/) |
| `ListPriceLow` | Number | Listing, Price |  | 14% | The lower price used for Value Range Pricing. | [link](https://dd.reso.org/DD2.0/Property/ListPriceLow/) |
| `ListTeam` | Resource | Listing, AgentOffice, ListTeam |  |  | Two or more agents working on the listing agent's team. | [link](https://dd.reso.org/DD2.0/Property/ListTeam/) |
| `ListTeamKey` | String | Listing, AgentOffice, Team |  | 4% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/Property/ListTeamKey/) |
| `ListTeamName` | String | Listing, AgentOffice, Team |  | 11% | The name of the team representing the seller. | [link](https://dd.reso.org/DD2.0/Property/ListTeamName/) |
| `ListingAgreement` | String List, Single | Listing | [ListingAgreement](#listingagreement) | 69% | The type of contractual relationship between the listing agent and the seller. | [link](https://dd.reso.org/DD2.0/Property/ListingAgreement/) |
| `ListingContractDate` | Date | Listing, Dates |  | 98% | The effective date of the agreement between the seller and the seller's broker. | [link](https://dd.reso.org/DD2.0/Property/ListingContractDate/) |
| `ListingId` | String | Listing |  | 100% | The well-known identifier for the listing, also known as the MLS number. | [link](https://dd.reso.org/DD2.0/Property/ListingId/) |
| `ListingKey` | String | Listing |  | 98% | A system-unique identifier for the listing. | [link](https://dd.reso.org/DD2.0/Property/ListingKey/) |
| `ListingService` | String List, Single | Listing | [ListingService](#listingservice) | 39% | The level of service the listing broker is providing to the seller. | [link](https://dd.reso.org/DD2.0/Property/ListingService/) |
| `ListingTerms` | String List, Multi | Listing, Contract | [ListingTerms](#listingterms) | 78% | Terms of the listing such as Lien Release, Subject to Court Approval or Owner Will Carry. | [link](https://dd.reso.org/DD2.0/Property/ListingTerms/) |
| `ListingURL` | String | Listing |  | 3% | Provides a link to the specific listing on a brokerage website, agent website or other public-facing source. | [link](https://dd.reso.org/DD2.0/Property/ListingURL/) |
| `ListingURLDescription` | String List, Single | Listing | [ListingURLDescription](#listingurldescription) |  | A pick list of options showing where the listing URL resides (i.e., Brokerage Website, Agent Website, etc.). | [link](https://dd.reso.org/DD2.0/Property/ListingURLDescription/) |
| `LivingArea` | Number | Structure |  | 78% | The total interior living area of the property, measured in LivingAreaUnits (typically SquareMeters or SquareFeet). | [link](https://dd.reso.org/DD2.0/Property/LivingArea/) |
| `LivingAreaSource` | String List, Single | Structure | [AreaSource](#areasource) | 51% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/LivingAreaSource/) |
| `LivingAreaUnits` | String List, Single | Structure | [AreaUnits](#areaunits) | 39% | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). | [link](https://dd.reso.org/DD2.0/Property/LivingAreaUnits/) |
| `LockBoxLocation` | String | Listing, Showing |  | 22% | A field describing the location of the lockbox. | [link](https://dd.reso.org/DD2.0/Property/LockBoxLocation/) |
| `LockBoxSerialNumber` | String | Listing, Showing |  | 24% | The serial number of the lockbox placed on the property. | [link](https://dd.reso.org/DD2.0/Property/LockBoxSerialNumber/) |
| `LockBoxType` | String List, Multi | Listing, Showing | [LockBoxType](#lockboxtype) | 39% | A field describing the type of lockbox. | [link](https://dd.reso.org/DD2.0/Property/LockBoxType/) |
| `Longitude` | Number | Location, GIS |  | 96% | The geographic longitude of the property in decimal degrees. | [link](https://dd.reso.org/DD2.0/Property/Longitude/) |
| `LotDimensionsSource` | String List, Single | Characteristics | [LotDimensionsSource](#lotdimensionssource) | 6% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/LotDimensionsSource/) |
| `LotFeatures` | String List, Multi | Characteristics | [LotFeatures](#lotfeatures) | 84% | A list of features or a description of the lot included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/LotFeatures/) |
| `LotSizeAcres` | Number | Characteristics |  | 97% | The total acres of the lot. | [link](https://dd.reso.org/DD2.0/Property/LotSizeAcres/) |
| `LotSizeArea` | Number | Characteristics |  | 90% | The total area of the lot. | [link](https://dd.reso.org/DD2.0/Property/LotSizeArea/) |
| `LotSizeDimensions` | String | Characteristics |  | 82% | The dimensions of the lot minimally represented as length and width (i.e. | [link](https://dd.reso.org/DD2.0/Property/LotSizeDimensions/) |
| `LotSizeSource` | String List, Single | Characteristics | [LotSizeSource](#lotsizesource) | 24% | The source of the measurements. | [link](https://dd.reso.org/DD2.0/Property/LotSizeSource/) |
| `LotSizeSquareFeet` | Number | Characteristics |  | 88% | The size of the lot in square feet (in CDL we honor LotSizeUnits and accept SquareMeters too). | [link](https://dd.reso.org/DD2.0/Property/LotSizeSquareFeet/) |
| `LotSizeUnits` | String List, Single | Characteristics | [LotSizeUnits](#lotsizeunits) | 88% | The unit of measurement for LotSizeArea (RESO AreaUnits lookup): SquareMeters, SquareFeet, Acres, Hectares, etc. | [link](https://dd.reso.org/DD2.0/Property/LotSizeUnits/) |
| `MLSAreaMajor` | String List, Single | Location, Area | MLSAreaMajor | 76% | The major marketing area name, as defined by the MLS or other nongovernmental organization. | [link](https://dd.reso.org/DD2.0/Property/MLSAreaMajor/) |
| `MLSAreaMinor` | String List, Single | Location, Area | MLSAreaMinor | 42% | The minor/submarketing area name, as defined by the MLS or other nongovernmental organization. | [link](https://dd.reso.org/DD2.0/Property/MLSAreaMinor/) |
| `MainLevelBathrooms` | Number | Structure |  | 17% | The number of bathrooms located on the main or entry level of the property. | [link](https://dd.reso.org/DD2.0/Property/MainLevelBathrooms/) |
| `MainLevelBedrooms` | Number | Structure |  | 21% | The number of bedrooms located on the main or entry level of the property. | [link](https://dd.reso.org/DD2.0/Property/MainLevelBedrooms/) |
| `MaintenanceExpense` | Number | Financial |  | 36% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/MaintenanceExpense/) |
| `MajorChangeTimestamp` | Timestamp | Listing, Dates |  | 60% | The timestamp of the last major change on the listing (see also MajorChangeType). | [link](https://dd.reso.org/DD2.0/Property/MajorChangeTimestamp/) |
| `MajorChangeType` | String List, Single | Listing, Dates | [ChangeType](#changetype) | 59% | A description of the last major change on the listing (i.e., Price Reduction, Back on Market). | [link](https://dd.reso.org/DD2.0/Property/MajorChangeType/) |
| `Make` | String | Structure |  | 17% | The make of the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/Make/) |
| `ManagerExpense` | Number | Financial |  | 15% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/ManagerExpense/) |
| `MapCoordinate` | String | Location, GIS |  | 7% | A map coordinate for the property, as determined by local custom. | [link](https://dd.reso.org/DD2.0/Property/MapCoordinate/) |
| `MapCoordinateSource` | String | Location, GIS |  | 4% | The name of the map or map book publisher. | [link](https://dd.reso.org/DD2.0/Property/MapCoordinateSource/) |
| `MapURL` | String | Location, GIS |  | 0% | A Uniform Resource Identifier (URI) to a map of the property. | [link](https://dd.reso.org/DD2.0/Property/MapURL/) |
| `Media` | Collection | Listing, Media |  | 31% | The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. | [link](https://dd.reso.org/DD2.0/Property/Media/) |
| `MiddleOrJuniorSchool` | String List, Single | Location, School | MiddleOrJuniorSchool | 52% | The name of the junior or middle school having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/MiddleOrJuniorSchool/) |
| `MiddleOrJuniorSchoolDistrict` | String List, Single | Location, School | MiddleOrJuniorSchoolDistrict | 25% | The name of the junior or middle school district having a catchment area that includes the associated property. | [link](https://dd.reso.org/DD2.0/Property/MiddleOrJuniorSchoolDistrict/) |
| `MlsStatus` | String List, Single | Listing | MlsStatus | 97% | A local or regional status that is well known by business users. | [link](https://dd.reso.org/DD2.0/Property/MlsStatus/) |
| `MobileDimUnits` | String List, Single | Structure | [LinearUnits](#linearunits) | 2% | A pick list of the unit of linear measurement (e.g., Feet, Meters, Yards, Kilometers, Miles). | [link](https://dd.reso.org/DD2.0/Property/MobileDimUnits/) |
| `MobileHomeRemainsYN` | Boolean | Characteristics |  | 3% | Indicates whether or not the mobile home is to remain and be included in the sale of the property. | [link](https://dd.reso.org/DD2.0/Property/MobileHomeRemainsYN/) |
| `MobileLength` | Number | Structure |  | 11% | The length of the mobile/manufactured home. | [link](https://dd.reso.org/DD2.0/Property/MobileLength/) |
| `MobileWidth` | Number | Structure |  | 11% | The width of the mobile/manufactured home. | [link](https://dd.reso.org/DD2.0/Property/MobileWidth/) |
| `Model` | String | Structure |  | 21% | The model of the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/Model/) |
| `ModificationTimestamp` | Timestamp | Listing, Dates |  | 100% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/Property/ModificationTimestamp/) |
| `NetOperatingIncome` | Number | Financial |  | 61% | The net operating income is the revenue from a property after operating expenses have been deducted but before deducting income taxes and financing expenses (interest and principal payments). | [link](https://dd.reso.org/DD2.0/Property/NetOperatingIncome/) |
| `NewConstructionYN` | Boolean | Structure |  | 72% | A flag indicating that the property has never been previously occupied. | [link](https://dd.reso.org/DD2.0/Property/NewConstructionYN/) |
| `NewTaxesExpense` | Number | Financial |  | 14% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/NewTaxesExpense/) |
| `NumberOfBuildings` | Number | Characteristics |  | 44% | The total number of separate buildings included in the income property. | [link](https://dd.reso.org/DD2.0/Property/NumberOfBuildings/) |
| `NumberOfFullTimeEmployees` | Number | Business |  | 10% | The current number of individuals employed by the business on a full-time basis. | [link](https://dd.reso.org/DD2.0/Property/NumberOfFullTimeEmployees/) |
| `NumberOfLots` | Number | Characteristics |  | 21% | The total number of lots on the property or included in the sale. | [link](https://dd.reso.org/DD2.0/Property/NumberOfLots/) |
| `NumberOfPads` | Number | Characteristics |  | 4% | The number of pads or spaces in the mobile home park. | [link](https://dd.reso.org/DD2.0/Property/NumberOfPads/) |
| `NumberOfPartTimeEmployees` | Number | Business |  | 7% | The current number of individuals employed by the business on a part-time basis. | [link](https://dd.reso.org/DD2.0/Property/NumberOfPartTimeEmployees/) |
| `NumberOfSeparateElectricMeters` | Number | Utilities |  | 14% | The total number of separate electric meters on the property. | [link](https://dd.reso.org/DD2.0/Property/NumberOfSeparateElectricMeters/) |
| `NumberOfSeparateGasMeters` | Number | Utilities |  | 12% | The total number of separate gas meters on the property. | [link](https://dd.reso.org/DD2.0/Property/NumberOfSeparateGasMeters/) |
| `NumberOfSeparateWaterMeters` | Number | Utilities |  | 13% | The total number of separate water meters on the property. | [link](https://dd.reso.org/DD2.0/Property/NumberOfSeparateWaterMeters/) |
| `NumberOfUnitsInCommunity` | Number | Characteristics |  | 21% | The total number of units in the building, complex or community. | [link](https://dd.reso.org/DD2.0/Property/NumberOfUnitsInCommunity/) |
| `NumberOfUnitsLeased` | Number | Financial |  | 10% | The total number of units currently under a lease agreement. | [link](https://dd.reso.org/DD2.0/Property/NumberOfUnitsLeased/) |
| `NumberOfUnitsMoMo` | Number | Financial |  | 3% | The total number of units leasable month to month. | [link](https://dd.reso.org/DD2.0/Property/NumberOfUnitsMoMo/) |
| `NumberOfUnitsTotal` | Number | Characteristics |  | 84% | Total number of units included in the income property, occupied or unoccupied. | [link](https://dd.reso.org/DD2.0/Property/NumberOfUnitsTotal/) |
| `NumberOfUnitsVacant` | Number | Financial |  | 6% | The number of units currently vacant. | [link](https://dd.reso.org/DD2.0/Property/NumberOfUnitsVacant/) |
| `OccupantName` | String | OccupantOwner |  | 25% | The full name of the current occupant of the Property. | [link](https://dd.reso.org/DD2.0/Property/OccupantName/) |
| `OccupantPhone` | String | OccupantOwner |  | 12% | The current occupant's contact phone number. | [link](https://dd.reso.org/DD2.0/Property/OccupantPhone/) |
| `OccupantType` | String List, Single | OccupantOwner | [OccupantType](#occupanttype) | 62% | A single-value lookup describing who currently occupies the Property: Owner \| Tenant \| Vacant. | [link](https://dd.reso.org/DD2.0/Property/OccupantType/) |
| `OffMarketDate` | Date | Listing, Dates |  | 83% | The date the listing was taken off market. | [link](https://dd.reso.org/DD2.0/Property/OffMarketDate/) |
| `OffMarketTimestamp` | Timestamp | Listing, Dates |  | 32% | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to an off-market status (not Active or Backup) | [link](https://dd.reso.org/DD2.0/Property/OffMarketTimestamp/) |
| `OnMarketDate` | Date | Listing, Dates |  | 65% | The date the listing was placed on market. | [link](https://dd.reso.org/DD2.0/Property/OnMarketDate/) |
| `OnMarketTimestamp` | Timestamp | Listing, Dates |  | 8% | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to Active or Backup. | [link](https://dd.reso.org/DD2.0/Property/OnMarketTimestamp/) |
| `OpenHouse` | Collection | Listing |  |  | The OpenHouse resource describes a scheduled event during which a Property is open for public or broker viewing. | [link](https://dd.reso.org/DD2.0/Property/OpenHouse/) |
| `OpenHouseModificationTimestamp` | Timestamp | Listing |  |  | A system-generated timestamp of when the last update or change to the open house information for this listing was made. | [link](https://dd.reso.org/DD2.0/Property/OpenHouseModificationTimestamp/) |
| `OpenParkingSpaces` | Number | Structure |  | 18% | The number of open or uncovered parking spaces included in the sale. | [link](https://dd.reso.org/DD2.0/Property/OpenParkingSpaces/) |
| `OpenParkingYN` | Boolean | Structure |  | 40% | A flag indicating that any parking spaces associated with the property are not covered by a roof. | [link](https://dd.reso.org/DD2.0/Property/OpenParkingYN/) |
| `OperatingExpense` | Number | Financial |  | 54% | The costs associated with the operation and maintenance of an income-producing property. | [link](https://dd.reso.org/DD2.0/Property/OperatingExpense/) |
| `OperatingExpenseIncludes` | String List, Multi | Financial | [OperatingExpenseIncludes](#operatingexpenseincludes) | 22% | When individual expense fields are not used and only a total is entered, this lists the expenses that are included in the OperatingExpense field. | [link](https://dd.reso.org/DD2.0/Property/OperatingExpenseIncludes/) |
| `OriginalEntryTimestamp` | Timestamp | Listing, Dates |  | 94% | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing was entered and made visible to members of the MLS. | [link](https://dd.reso.org/DD2.0/Property/OriginalEntryTimestamp/) |
| `OriginalListPrice` | Number | Listing, Price |  | 94% | The original listing price of the property as it was first listed. | [link](https://dd.reso.org/DD2.0/Property/OriginalListPrice/) |
| `OriginatingSystem` | Resource | Listing |  |  | The originating system of the Property record. | [link](https://dd.reso.org/DD2.0/Property/OriginatingSystem/) |
| `OriginatingSystemID` | String | Listing |  | 70% | The OUID Resource's OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/Property/OriginatingSystemID/) |
| `OriginatingSystemKey` | String | Listing |  | 90% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/Property/OriginatingSystemKey/) |
| `OriginatingSystemName` | String | Listing |  | 95% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/Property/OriginatingSystemName/) |
| `OtherEquipment` | String List, Multi | Equipment | [OtherEquipment](#otherequipment) | 71% | A list of other equipment that will be included in the sale of the property. | [link](https://dd.reso.org/DD2.0/Property/OtherEquipment/) |
| `OtherExpense` | Number | Financial |  | 28% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/OtherExpense/) |
| `OtherParking` | String | Structure |  | 16% | Other types of parking available to, or part of, the property. | [link](https://dd.reso.org/DD2.0/Property/OtherParking/) |
| `OtherStructures` | String List, Multi | Structure | [OtherStructures](#otherstructures) | 77% | A list of structures other than the main dwelling (e.g., Guest House, Barn, Shed). | [link](https://dd.reso.org/DD2.0/Property/OtherStructures/) |
| `OwnerName` | String | OccupantOwner |  | 77% | The full legal name of the Property owner. | [link](https://dd.reso.org/DD2.0/Property/OwnerName/) |
| `OwnerPays` | String List, Multi | Financial | [OwnerPays](#ownerpays) | 53% | A list of expenses for the property paid for by the owner as opposed to the tenant (e.g., Water, Trash, Electric). | [link](https://dd.reso.org/DD2.0/Property/OwnerPays/) |
| `OwnerPhone` | String | OccupantOwner |  | 42% | The Property owner's contact phone number. | [link](https://dd.reso.org/DD2.0/Property/OwnerPhone/) |
| `Ownership` | String | Listing, Contract |  | 25% | Free-text description of the legal ownership type of the Property: Sole Owner, Trust, Corporation, LLC, Joint Tenancy, etc. | [link](https://dd.reso.org/DD2.0/Property/Ownership/) |
| `OwnershipType` | String List, Single | Business | [OwnershipType](#ownershiptype) | 22% | The current type of ownership of the business being sold (e.g., Corporation, LLC, Sole Proprietor, Partnership). | [link](https://dd.reso.org/DD2.0/Property/OwnershipType/) |
| `ParcelNumber` | String | Tax |  | 88% | A number used to uniquely identify a parcel or lot. | [link](https://dd.reso.org/DD2.0/Property/ParcelNumber/) |
| `ParkManagerName` | String | Characteristics |  | 6% | The name of the manager of the mobile home park. | [link](https://dd.reso.org/DD2.0/Property/ParkManagerName/) |
| `ParkManagerPhone` | String | Characteristics |  | 6% | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | [link](https://dd.reso.org/DD2.0/Property/ParkManagerPhone/) |
| `ParkName` | String | Characteristics |  | 13% | The name of the mobile home park or corporate/commercial park. | [link](https://dd.reso.org/DD2.0/Property/ParkName/) |
| `ParkingFeatures` | String List, Multi | Structure | [ParkingFeatures](#parkingfeatures) | 86% | A list of features about or a description of the parking included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/ParkingFeatures/) |
| `ParkingTotal` | Number | Structure |  | 72% | The total number of parking spaces included in the sale. | [link](https://dd.reso.org/DD2.0/Property/ParkingTotal/) |
| `PastureArea` | Number | Farming |  | 19% | A measurement or percentage of the property that has been allocated as pasture or grazing area. | [link](https://dd.reso.org/DD2.0/Property/PastureArea/) |
| `PatioAndPorchFeatures` | String List, Multi | Structure | [PatioAndPorchFeatures](#patioandporchfeatures) | 76% | A list of features about or a description of the patio or porch included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/PatioAndPorchFeatures/) |
| `PendingTimestamp` | Timestamp | Listing, Dates |  | 74% | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to Pending. | [link](https://dd.reso.org/DD2.0/Property/PendingTimestamp/) |
| `PestControlExpense` | Number | Financial |  | 3% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/PestControlExpense/) |
| `PetsAllowed` | String List, Multi | Characteristics | [PetsAllowed](#petsallowed) | 65% | Indicates whether or not pets are allowed at the property being leased, usually as a list of yes, no and more detailed restrictions/allowances. | [link](https://dd.reso.org/DD2.0/Property/PetsAllowed/) |
| `PhotosChangeTimestamp` | Timestamp | Listing, Media |  | 97% | A system-generated timestamp of when the last update or change to the photos for this listing was made. | [link](https://dd.reso.org/DD2.0/Property/PhotosChangeTimestamp/) |
| `PhotosCount` | Number | Listing, Media |  | 99% | The total number of pictures or photos included with the listing. | [link](https://dd.reso.org/DD2.0/Property/PhotosCount/) |
| `PoolExpense` | Number | Financial |  | 1% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/PoolExpense/) |
| `PoolFeatures` | String List, Multi | Characteristics | [PoolFeatures](#poolfeatures) | 79% | A list of features about or a description of a pool included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/PoolFeatures/) |
| `PoolPrivateYN` | Boolean | Characteristics |  | 41% | The property has a privately owned pool that is included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/PoolPrivateYN/) |
| `Possession` | String List, Multi | Listing, Closing | [Possession](#possession) | 74% | A list defining when possession will occur (i.e., COE, COE+1, etc.). | [link](https://dd.reso.org/DD2.0/Property/Possession/) |
| `PossibleUse` | String List, Multi | Characteristics | [CurrentOrPossibleUse](#currentorpossibleuse) | 49% | A list of the type(s) of possible or best uses of the property. | [link](https://dd.reso.org/DD2.0/Property/PossibleUse/) |
| `PostalCity` | String List, Single | Location, Address | PostalCity | 29% | The official city per the U.S. | [link](https://dd.reso.org/DD2.0/Property/PostalCity/) |
| `PostalCode` | String | Location, Address |  | 99% | The postal code in which the property is located. | [link](https://dd.reso.org/DD2.0/Property/PostalCode/) |
| `PostalCodePlus4` | String | Location, Address |  | 53% | The last four digits of a nine-digit U.S. | [link](https://dd.reso.org/DD2.0/Property/PostalCodePlus4/) |
| `PowerProduction` | Collection | Utilities |  |  | A collection of the types of power production system(s) available on the property. | [link](https://dd.reso.org/DD2.0/Property/PowerProduction/) |
| `PowerProductionType` | String List, Multi | Utilities | [PowerProductionType](#powerproductiontype) | 12% | A list of the types of power production systems available on the property. | [link](https://dd.reso.org/DD2.0/Property/PowerProductionType/) |
| `PowerProductionYN` | Boolean | Utilities |  | 0% | A flag indicating that the listing has a Power Production system. | [link](https://dd.reso.org/DD2.0/Property/PowerProductionYN/) |
| `PreviousListPrice` | Number | Listing, Price |  | 63% | The most recent previous list price of the listing. | [link](https://dd.reso.org/DD2.0/Property/PreviousListPrice/) |
| `PriceChangeTimestamp` | Timestamp | Listing, Dates |  | 90% | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing's price was last changed. | [link](https://dd.reso.org/DD2.0/Property/PriceChangeTimestamp/) |
| `PrivateOfficeRemarks` | String | Listing, Remarks |  | 20% | A Remarks field that is only visible to members of the same offices as the listing agent. | [link](https://dd.reso.org/DD2.0/Property/PrivateOfficeRemarks/) |
| `PrivateRemarks` | String | Listing, Remarks |  | 90% | Remarks that may contain security or proprietary information and should be restricted from public view. | [link](https://dd.reso.org/DD2.0/Property/PrivateRemarks/) |
| `ProfessionalManagementExpense` | Number | Financial |  | 18% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/ProfessionalManagementExpense/) |
| `PropertyAttachedYN` | Boolean | Structure |  | 39% | Indicates whether or not the primary structure is attached to another structure that is not included in the sale (i.e., one unit of a duplex). | [link](https://dd.reso.org/DD2.0/Property/PropertyAttachedYN/) |
| `PropertyCondition` | String List, Multi | Structure | [PropertyCondition](#propertycondition) | 63% | A list of property conditions describing the state of the property. | [link](https://dd.reso.org/DD2.0/Property/PropertyCondition/) |
| `PropertySubType` | String List, Single |  | [PropertySubType](#propertysubtype) | 95% | A more specific classification of the property within PropertyType (e.g. | [link](https://dd.reso.org/DD2.0/Property/PropertySubType/) |
| `PropertyTimeZoneName` | String List, Single | Listing, Dates | [IanaTimeZoneValues](#ianatimezonevalues) | 1% | The standard name of the property time zone, as provided by the IANA tz database. | [link](https://dd.reso.org/DD2.0/Property/PropertyTimeZoneName/) |
| `PropertyTimeZoneObservesDstYN` | Boolean | Listing, Dates |  |  | Indicates whether the property is in a time zone that observes Daylight Savings Time (DST). | [link](https://dd.reso.org/DD2.0/Property/PropertyTimeZoneObservesDstYN/) |
| `PropertyTimeZoneStandardOffset` | Number | Listing, Dates |  |  | The time zone offset is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. | [link](https://dd.reso.org/DD2.0/Property/PropertyTimeZoneStandardOffset/) |
| `PropertyType` | String List, Single |  | [PropertyType](#propertytype) | 99% | The high-level classification of the property: Residential, ResidentialIncome, ResidentialLease, CommercialSale, CommercialLease, Land, ManufacturedInPark, BusinessOpportunity, Farm. | [link](https://dd.reso.org/DD2.0/Property/PropertyType/) |
| `PublicRemarks` | String | Listing, Remarks |  | 99% | The publicly visible marketing description of the property, intended for consumer-facing portals and the IDX feed. | [link](https://dd.reso.org/DD2.0/Property/PublicRemarks/) |
| `PublicSurveyRange` | String | Tax |  | 14% | The range identified by the Public Land Survey System (PLSS). | [link](https://dd.reso.org/DD2.0/Property/PublicSurveyRange/) |
| `PublicSurveySection` | String | Tax |  | 18% | The section identified by the Public Land Survey System (PLSS). | [link](https://dd.reso.org/DD2.0/Property/PublicSurveySection/) |
| `PublicSurveyTownship` | String | Tax |  | 13% | The township identified by the Public Land Survey System (PLSS). | [link](https://dd.reso.org/DD2.0/Property/PublicSurveyTownship/) |
| `PurchaseContractDate` | Date | Listing, Dates |  | 84% | With for-sale listings, this represents the date an offer was accepted and the listing was no longer on market. | [link](https://dd.reso.org/DD2.0/Property/PurchaseContractDate/) |
| `RVParkingDimensions` | String | Structure |  | 3% | The dimensions of the RV parking area minimally represented as length and width (i.e., 25' x 18') or a measurement of all sides of the polygon representing the usable RV parking space (i.e., 33' x 15'… | [link](https://dd.reso.org/DD2.0/Property/RVParkingDimensions/) |
| `RangeArea` | Number | Farming |  | 3% | The measurement or percentage of the property that has been allocated as range. | [link](https://dd.reso.org/DD2.0/Property/RangeArea/) |
| `RentControlYN` | Boolean | Financial |  | 4% | Indicates whether or not the property is in a rent-control area. | [link](https://dd.reso.org/DD2.0/Property/RentControlYN/) |
| `RentIncludes` | String List, Multi | Financial | [RentIncludes](#rentincludes) | 39% | A list of services or items that the tenant is not responsible to pay. | [link](https://dd.reso.org/DD2.0/Property/RentIncludes/) |
| `RoadFrontageType` | String List, Multi | Characteristics | [RoadFrontageType](#roadfrontagetype) | 72% | A pick list of types of road frontage (i.e., County, Freeway, Interstate, None). | [link](https://dd.reso.org/DD2.0/Property/RoadFrontageType/) |
| `RoadResponsibility` | String List, Multi | Characteristics | [RoadResponsibility](#roadresponsibility) | 36% | The person or entity responsible for road maintenance (e.g., City, County, Private). | [link](https://dd.reso.org/DD2.0/Property/RoadResponsibility/) |
| `RoadSurfaceType` | String List, Multi | Characteristics | [RoadSurfaceType](#roadsurfacetype) | 74% | A pick list of types of road surfaces in use to access the property. | [link](https://dd.reso.org/DD2.0/Property/RoadSurfaceType/) |
| `Roof` | String List, Multi | Structure | [Roof](#roof) | 89% | A list describing the roof style type (e.g., Spanish Tile, Composite, Shake). | [link](https://dd.reso.org/DD2.0/Property/Roof/) |
| `RoomType` | String List, Multi | Structure, Rooms | [RoomType](#roomtype) | 25% | A single-value lookup describing the type of room: Bedroom \| Bathroom \| Kitchen \| LivingRoom \| DiningRoom \| Office \| Laundry \| Bonus \| ... | [link](https://dd.reso.org/DD2.0/Property/RoomType/) |
| `Rooms` | Collection | Structure, Rooms |  | 1% | A collection of types of rooms and details/features about the given room. | [link](https://dd.reso.org/DD2.0/Property/Rooms/) |
| `RoomsTotal` | Number | Structure, Rooms |  | 67% | The number of rooms in a dwelling. | [link](https://dd.reso.org/DD2.0/Property/RoomsTotal/) |
| `SeatingCapacity` | Number | Business |  | 8% | The seating capacity of the business being sold. | [link](https://dd.reso.org/DD2.0/Property/SeatingCapacity/) |
| `SecurityFeatures` | String List, Multi | Equipment | [SecurityFeatures](#securityfeatures) | 74% | A list describing the security features included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/SecurityFeatures/) |
| `SeniorCommunityYN` | Boolean | Characteristics |  | 34% | Indicates whether or not a community is a senior community. | [link](https://dd.reso.org/DD2.0/Property/SeniorCommunityYN/) |
| `SerialU` | String | Structure |  | 17% | The serial number of the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/SerialU/) |
| `SerialX` | String | Structure |  | 6% | The serial number of the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/SerialX/) |
| `SerialXX` | String | Structure |  | 4% | The serial number of the mobile or manufactured home. | [link](https://dd.reso.org/DD2.0/Property/SerialXX/) |
| `Sewer` | String List, Multi | Utilities | [Sewer](#sewer) | 87% | A list describing the sewer or septic features of a property. | [link](https://dd.reso.org/DD2.0/Property/Sewer/) |
| `ShowingAdvanceNotice` | Number | Listing, Showing |  | 10% | The hours of advance notice required to schedule a showing. | [link](https://dd.reso.org/DD2.0/Property/ShowingAdvanceNotice/) |
| `ShowingAttendedYN` | Boolean | Listing, Showing |  | 13% | Indicates whether or not this home requires an attended showing (i.e., Yes = licensed agent representing the seller must be present during showing). | [link](https://dd.reso.org/DD2.0/Property/ShowingAttendedYN/) |
| `ShowingConsiderations` | String List, Multi | Listing, Showing | [ShowingConsiderations](#showingconsiderations) | 9% | A pick list of conditions that may require caution or further consideration, such as bringing someone with you, when showing the property (i.e., Electricity Not On, Inconsistent Cell Service, No Exter… | [link](https://dd.reso.org/DD2.0/Property/ShowingConsiderations/) |
| `ShowingContactName` | String | Listing, Showing |  | 12% | The name of the contact for the showing of the listed property. | [link](https://dd.reso.org/DD2.0/Property/ShowingContactName/) |
| `ShowingContactPhone` | String | Listing, Showing |  | 29% | A telephone number that should be called to arrange showing the property. | [link](https://dd.reso.org/DD2.0/Property/ShowingContactPhone/) |
| `ShowingContactPhoneExt` | String | Listing, Showing |  | 2% | The extension of the given phone number, if applicable. | [link](https://dd.reso.org/DD2.0/Property/ShowingContactPhoneExt/) |
| `ShowingContactType` | String List, Multi | Listing, Showing | [ShowingContactType](#showingcontacttype) | 14% | The type of contact for the showing (i.e., Agent, Broker, Seller). | [link](https://dd.reso.org/DD2.0/Property/ShowingContactType/) |
| `ShowingDays` | String List, Multi | Listing, Showing | ShowingDays | 2% | The days of the week that the property is available for showing (i.e., Sundays, Mondays, Tuesdays, Wednesdays, Thursdays, Fridays, Saturdays). | [link](https://dd.reso.org/DD2.0/Property/ShowingDays/) |
| `ShowingEndTime` | Timestamp | Listing, Showing |  | 1% | From the days selected in the ShowingDays field, the end time that the property is available for showing. | [link](https://dd.reso.org/DD2.0/Property/ShowingEndTime/) |
| `ShowingInstructions` | String | Listing, Showing |  | 83% | Remarks that detail the seller's instructions for showing the subject property. | [link](https://dd.reso.org/DD2.0/Property/ShowingInstructions/) |
| `ShowingRequirements` | String List, Multi | Listing, Showing | [ShowingRequirements](#showingrequirements) | 28% | A pick list of types of notice required to see the home (i.e., Appointment Required, Courtesy Call Only, Go Direct, etc.). | [link](https://dd.reso.org/DD2.0/Property/ShowingRequirements/) |
| `ShowingServiceName` | String List, Single | Listing, Showing | [ShowingServiceName](#showingservicename) | 1% | The name of the showing service used to request showings on the listing. | [link](https://dd.reso.org/DD2.0/Property/ShowingServiceName/) |
| `ShowingStartTime` | Timestamp | Listing, Showing |  | 1% | From the days selected in the ShowingDays field, the start time that the property is available for showing. | [link](https://dd.reso.org/DD2.0/Property/ShowingStartTime/) |
| `SignOnPropertyYN` | Boolean | Listing, Marketing |  | 34% | Indicates whether or not there a sign on the property. | [link](https://dd.reso.org/DD2.0/Property/SignOnPropertyYN/) |
| `SimpleDaysOnMarket` | Number | Listing, Dates |  | 0% | A simplified version of days on market (DOM) where the calculation is a simple start and end, such as the difference between the listing input or contract date and the date of sale. | [link](https://dd.reso.org/DD2.0/Property/SimpleDaysOnMarket/) |
| `Skirt` | String List, Multi | Structure | [Skirt](#skirt) | 12% | A list of types of mobile home skirting. | [link](https://dd.reso.org/DD2.0/Property/Skirt/) |
| `SocialMedia` | Collection | Listing |  |  | A collection of social media items related to the Property record. | [link](https://dd.reso.org/DD2.0/Property/SocialMedia/) |
| `SourceSystem` | Resource | Listing |  |  | The source system of the Property record. | [link](https://dd.reso.org/DD2.0/Property/SourceSystem/) |
| `SourceSystemID` | String | Listing |  | 58% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/Property/SourceSystemID/) |
| `SourceSystemKey` | String | Listing |  | 83% | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/Property/SourceSystemKey/) |
| `SourceSystemName` | String | Listing |  | 39% | The name of the immediate record provider. | [link](https://dd.reso.org/DD2.0/Property/SourceSystemName/) |
| `SpaFeatures` | String List, Multi | Characteristics | [SpaFeatures](#spafeatures) | 62% | A list of features or a description of the spa included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/SpaFeatures/) |
| `SpaYN` | Boolean | Characteristics |  | 53% | Indicates whether or not the property has a spa. | [link](https://dd.reso.org/DD2.0/Property/SpaYN/) |
| `SpecialLicenses` | String List, Multi | Business | [SpecialLicenses](#speciallicenses) | 13% | Special licenses required/used by the business being sold (e.g., Beer/Wine, Class H, Professional, Gambling, None). | [link](https://dd.reso.org/DD2.0/Property/SpecialLicenses/) |
| `SpecialListingConditions` | String List, Multi | Listing, Contract | [SpecialListingConditions](#speciallistingconditions) | 74% | A list of options that describe the type of sale (e.g., Standard, REO, Short Sale, Probate, Auction, NOD) at the time of listing. | [link](https://dd.reso.org/DD2.0/Property/SpecialListingConditions/) |
| `StandardStatus` | String List, Single | Listing | [StandardStatus](#standardstatus) | 94% | The MLS-defined statuses normalized into a common set. | [link](https://dd.reso.org/DD2.0/Property/StandardStatus/) |
| `StartShowingDate` | Date | Listing, Showing |  | 6% | The date the listing agent/broker expects to start showing the property. | [link](https://dd.reso.org/DD2.0/Property/StartShowingDate/) |
| `StateOrProvince` | String List, Single | Location, Address | [StateOrProvince](#stateorprovince) | 99% | The state or province in which the property is located. | [link](https://dd.reso.org/DD2.0/Property/StateOrProvince/) |
| `StateRegion` | String | Location, Area |  | 1% | A subsection or area of a defined state or province (e.g., Florida Keys, Hudson Valley in New York, Silicon Valley in California). | [link](https://dd.reso.org/DD2.0/Property/StateRegion/) |
| `StatusChangeTimestamp` | Timestamp | Listing, Dates |  | 68% | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing's status was last changed. | [link](https://dd.reso.org/DD2.0/Property/StatusChangeTimestamp/) |
| `Stories` | Number | Structure |  | 71% | The number of floors in the property being sold. | [link](https://dd.reso.org/DD2.0/Property/Stories/) |
| `StoriesTotal` | Number | Structure |  | 35% | The total number of floors in the building. | [link](https://dd.reso.org/DD2.0/Property/StoriesTotal/) |
| `StreetAdditionalInfo` | String | Location, Address |  | 23% | Information other than a prefix or suffix for the street portion of a postal address. | [link](https://dd.reso.org/DD2.0/Property/StreetAdditionalInfo/) |
| `StreetDirPrefix` | String List, Single | Location, Address | [StreetDirection](#streetdirection) | 88% | The direction indicator that precedes the listed property's street name. | [link](https://dd.reso.org/DD2.0/Property/StreetDirPrefix/) |
| `StreetDirSuffix` | String List, Single | Location, Address | [StreetDirection](#streetdirection) | 50% | The direction indicator that follows a listed property's street address. | [link](https://dd.reso.org/DD2.0/Property/StreetDirSuffix/) |
| `StreetName` | String | Location, Address |  | 99% | The street name portion of a listed property's street address. | [link](https://dd.reso.org/DD2.0/Property/StreetName/) |
| `StreetNumber` | String | Location, Address |  | 99% | The street number portion of a listed property's street address. | [link](https://dd.reso.org/DD2.0/Property/StreetNumber/) |
| `StreetNumberNumeric` | Number | Location, Address |  | 73% | The integer portion of the street number. | [link](https://dd.reso.org/DD2.0/Property/StreetNumberNumeric/) |
| `StreetSuffix` | String List, Single | Location, Address | StreetSuffix | 72% | The suffix portion of a listed property's street address. | [link](https://dd.reso.org/DD2.0/Property/StreetSuffix/) |
| `StreetSuffixModifier` | String | Location, Address |  | 4% | Allows for the entry of a unique street suffix that was not found in the Street Suffix pick list or to extend or prefix the suffix. | [link](https://dd.reso.org/DD2.0/Property/StreetSuffixModifier/) |
| `StructureType` | String List, Multi | Structure | [StructureType](#structuretype) | 63% | The type of structure that the property completely or partially encompasses. | [link](https://dd.reso.org/DD2.0/Property/StructureType/) |
| `SubAgencyCompensation` | String | Listing, Compensation |  | 28% | The total commission to be paid to the subagency, expressed as either a percentage or a constant currency amount. | [link](https://dd.reso.org/DD2.0/Property/SubAgencyCompensation/) |
| `SubAgencyCompensationType` | String List, Single | Listing, Compensation | [CompensationType](#compensationtype) | 23% | A list of types to clarify the value entered in the SubAgencyCompensation field. | [link](https://dd.reso.org/DD2.0/Property/SubAgencyCompensationType/) |
| `SubdivisionName` | String | Location, Area |  | 90% | A neighborhood, community, complex or builder tract. | [link](https://dd.reso.org/DD2.0/Property/SubdivisionName/) |
| `SuppliesExpense` | Number | Financial |  | 7% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/SuppliesExpense/) |
| `SyndicateTo` | String List, Multi | Listing, Marketing | [SyndicateTo](#syndicateto) | 16% | When permitted by the broker, the options made by the agent on behalf of the seller, where they would like their listings syndicated (e.g., Zillow, Trulia, Realtor.com, Homes.com). | [link](https://dd.reso.org/DD2.0/Property/SyndicateTo/) |
| `SyndicationRemarks` | String | Listing, Remarks |  | 11% | For MLSs that host a separate "Public Remarks" for syndication purposes, this field should be defaulted to contain public remarks. | [link](https://dd.reso.org/DD2.0/Property/SyndicationRemarks/) |
| `TaxAnnualAmount` | Number | Tax |  | 86% | The annual property tax amount as of the last assessment made by the taxing authority. | [link](https://dd.reso.org/DD2.0/Property/TaxAnnualAmount/) |
| `TaxAnnualAmountPerLivingAreaUnit` | Number | Tax |  |  | The annual property tax amount as of the last assessment made by the taxing authority divided by the property’s living area. | [link](https://dd.reso.org/DD2.0/Property/TaxAnnualAmountPerLivingAreaUnit/) |
| `TaxAnnualAmountPerSquareFoot` | Number | Tax |  |  | The annual property tax amount as of the last assessment made by the taxing authority divided by the property’s living area square footage. | [link](https://dd.reso.org/DD2.0/Property/TaxAnnualAmountPerSquareFoot/) |
| `TaxAssessedValue` | Number | Tax |  | 31% | The property value as of the last assessment made by the taxing authority. | [link](https://dd.reso.org/DD2.0/Property/TaxAssessedValue/) |
| `TaxBlock` | String | Tax |  | 28% | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. | [link](https://dd.reso.org/DD2.0/Property/TaxBlock/) |
| `TaxBookNumber` | String | Tax |  | 11% | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. | [link](https://dd.reso.org/DD2.0/Property/TaxBookNumber/) |
| `TaxLegalDescription` | String | Tax |  | 63% | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. | [link](https://dd.reso.org/DD2.0/Property/TaxLegalDescription/) |
| `TaxLot` | String | Tax |  | 36% | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. | [link](https://dd.reso.org/DD2.0/Property/TaxLot/) |
| `TaxMapNumber` | String | Tax |  | 14% | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. | [link](https://dd.reso.org/DD2.0/Property/TaxMapNumber/) |
| `TaxOtherAnnualAssessmentAmount` | Number | Tax |  | 15% | Any other annual taxes, not including the tax reported in the TaxAmount field, as of the last assessment made by the taxing authority. | [link](https://dd.reso.org/DD2.0/Property/TaxOtherAnnualAssessmentAmount/) |
| `TaxParcelLetter` | String | Tax |  | 3% | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. | [link](https://dd.reso.org/DD2.0/Property/TaxParcelLetter/) |
| `TaxStatusCurrent` | String List, Multi | Tax | [TaxStatusCurrent](#taxstatuscurrent) | 3% | The current tax status of the mobile home in cases where the land or space is included in the sale. | [link](https://dd.reso.org/DD2.0/Property/TaxStatusCurrent/) |
| `TaxTract` | String | Tax |  | 8% | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. | [link](https://dd.reso.org/DD2.0/Property/TaxTract/) |
| `TaxYear` | Number | Tax |  | 65% | The year in which the last assessment of the property value/tax was made. | [link](https://dd.reso.org/DD2.0/Property/TaxYear/) |
| `TenantPays` | String List, Multi | Financial | [TenantPays](#tenantpays) | 63% | A list of services or items that the tenant is responsible to pay. | [link](https://dd.reso.org/DD2.0/Property/TenantPays/) |
| `Topography` | String | Characteristics |  | 55% | The state of the surface of the land included with the property (i.e., flat, rolling, etc.). | [link](https://dd.reso.org/DD2.0/Property/Topography/) |
| `TotalActualRent` | Number | Financial |  | 36% | Total actual rent currently being collected from tenants of the income property. | [link](https://dd.reso.org/DD2.0/Property/TotalActualRent/) |
| `Township` | String | Location, Address |  | 23% | A subdivision of the county. | [link](https://dd.reso.org/DD2.0/Property/Township/) |
| `TransactionBrokerCompensation` | String | Listing, Compensation |  | 23% | The total commission to be paid to the transaction facilitator, expressed as either a percentage or a constant currency amount. | [link](https://dd.reso.org/DD2.0/Property/TransactionBrokerCompensation/) |
| `TransactionBrokerCompensationType` | String List, Single | Listing, Compensation | [CompensationType](#compensationtype) | 19% | A list of types to clarify the value entered in the TransactionBrokerCompensation field. | [link](https://dd.reso.org/DD2.0/Property/TransactionBrokerCompensationType/) |
| `TrashExpense` | Number | Financial |  | 17% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/TrashExpense/) |
| `UnitNumber` | String | Location, Address |  | 79% | A text field containing the unit number or portion of a larger building or complex that should appear following the street suffix or, if it exists, the street suffix direction in the street address (e… | [link](https://dd.reso.org/DD2.0/Property/UnitNumber/) |
| `UnitTypeType` | String List, Multi | UnitTypes | [UnitTypeType](#unittypetype) | 4% | A single-value lookup describing the unit type: Apartments \| Studio \| Loft \| Penthouse \| 1 Bedroom \| 2 Bedroom \| 3 Bedroom \| 4 Bedroom Or More \| Efficiency \| Manager's Unit. | [link](https://dd.reso.org/DD2.0/Property/UnitTypeType/) |
| `UnitTypes` | Collection | UnitTypes |  | 0% | A collection of types of units included in the income (multifamily) property. | [link](https://dd.reso.org/DD2.0/Property/UnitTypes/) |
| `UnitsFurnished` | String List, Single | Characteristics | [UnitsFurnished](#unitsfurnished) | 6% | States whether or not the units are furnished (i.e., All Units, Varies By Unit, None). | [link](https://dd.reso.org/DD2.0/Property/UnitsFurnished/) |
| `UniversalPropertyId` | String |  |  | 23% | The RESO Universal Property Identifier (UPI) is a unique identifier for all real property in the U.S. | [link](https://dd.reso.org/DD2.0/Property/UniversalPropertyId/) |
| `UniversalPropertySubId` | String |  |  | 0% | A unique identifier for all subsets or shares of real property in the U.S. | [link](https://dd.reso.org/DD2.0/Property/UniversalPropertySubId/) |
| `UnparsedAddress` | String | Location, Address |  | 92% | The full street address of the property as a single, unparsed string. | [link](https://dd.reso.org/DD2.0/Property/UnparsedAddress/) |
| `Utilities` | String List, Multi | Utilities | [Utilities](#utilities) | 88% | A list of the utilities for the property being sold/leased. | [link](https://dd.reso.org/DD2.0/Property/Utilities/) |
| `VacancyAllowance` | Number | Financial |  | 7% | An estimate of the amount of rent that may be foregone because of unoccupied units. | [link](https://dd.reso.org/DD2.0/Property/VacancyAllowance/) |
| `VacancyAllowanceRate` | Number | Financial |  | 17% | An estimate of the percent of rent that may be foregone because of unoccupied units. | [link](https://dd.reso.org/DD2.0/Property/VacancyAllowanceRate/) |
| `Vegetation` | String List, Multi | Farming | [Vegetation](#vegetation) | 35% | A list of the type(s) of residential vegetation on the property (not farm crops). | [link](https://dd.reso.org/DD2.0/Property/Vegetation/) |
| `VideosChangeTimestamp` | Timestamp | Listing, Media |  | 43% | A system-generated timestamp of when the last update or change to the videos for this listing was made. | [link](https://dd.reso.org/DD2.0/Property/VideosChangeTimestamp/) |
| `VideosCount` | Number | Listing, Media |  | 44% | The total number of videos or virtual tours included with the listing. | [link](https://dd.reso.org/DD2.0/Property/VideosCount/) |
| `View` | String List, Multi | Characteristics | [View](#view) | 63% | A view as seen from the listed property. | [link](https://dd.reso.org/DD2.0/Property/View/) |
| `ViewYN` | Boolean | Characteristics |  | 51% | The property has a view. | [link](https://dd.reso.org/DD2.0/Property/ViewYN/) |
| `VirtualTourURLBranded` | String | Listing, Marketing |  | 49% | A text field that holds the Uniform Resource Locator (URL) for a branded virtual tour of the property. | [link](https://dd.reso.org/DD2.0/Property/VirtualTourURLBranded/) |
| `VirtualTourURLUnbranded` | String | Listing, Marketing |  | 92% | A link to an unbranded virtual tour of the property (does NOT carry brokerage branding). | [link](https://dd.reso.org/DD2.0/Property/VirtualTourURLUnbranded/) |
| `WalkScore` | Number | Structure, Performance, GreenMarketing |  | 3% | A walkability index based on the time to walk from a property to nearby essentials such as grocery stores, schools, churches, etc. | [link](https://dd.reso.org/DD2.0/Property/WalkScore/) |
| `WaterBodyName` | String | Characteristics |  | 33% | The name, if known, of the body of water on which the property is located (e.g., lake name, river name, ocean name, sea name, canal name). | [link](https://dd.reso.org/DD2.0/Property/WaterBodyName/) |
| `WaterSewerExpense` | Number | Financial |  | 24% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/WaterSewerExpense/) |
| `WaterSource` | String List, Multi | Utilities | [WaterSource](#watersource) | 86% | A list of the source(s) of water for the property. | [link](https://dd.reso.org/DD2.0/Property/WaterSource/) |
| `WaterfrontFeatures` | String List, Multi | Characteristics | [WaterfrontFeatures](#waterfrontfeatures) | 71% | The features of the waterfront on which the property is located. | [link](https://dd.reso.org/DD2.0/Property/WaterfrontFeatures/) |
| `WaterfrontYN` | Boolean | Characteristics |  | 72% | The property is on a waterfront. | [link](https://dd.reso.org/DD2.0/Property/WaterfrontYN/) |
| `WindowFeatures` | String List, Multi | Structure | [WindowFeatures](#windowfeatures) | 76% | A list of features or a description of the windows included in the sale/lease. | [link](https://dd.reso.org/DD2.0/Property/WindowFeatures/) |
| `WithdrawnDate` | Date | Listing, Dates |  | 66% | The date that the listing was withdrawn from the market. | [link](https://dd.reso.org/DD2.0/Property/WithdrawnDate/) |
| `WoodedArea` | Number | Farming |  | 26% | A measurement or percentage of the property that is wooded or forest. | [link](https://dd.reso.org/DD2.0/Property/WoodedArea/) |
| `WorkmansCompensationExpense` | Number | Financial |  | 1% | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. | [link](https://dd.reso.org/DD2.0/Property/WorkmansCompensationExpense/) |
| `YearBuilt` | Number | Structure |  | 99% | The year the property was originally constructed. | [link](https://dd.reso.org/DD2.0/Property/YearBuilt/) |
| `YearBuiltDetails` | String | Structure |  | 16% | A description of the details behind the year the structure was built. | [link](https://dd.reso.org/DD2.0/Property/YearBuiltDetails/) |
| `YearBuiltEffective` | Number | Structure |  | 18% | The effective year built. | [link](https://dd.reso.org/DD2.0/Property/YearBuiltEffective/) |
| `YearBuiltSource` | String List, Single | Structure | [YearBuiltSource](#yearbuiltsource) | 17% | A list of sources of the year built (e.g., Appraiser, Assessor, Builder, Estimated). | [link](https://dd.reso.org/DD2.0/Property/YearBuiltSource/) |
| `YearEstablished` | Number | Business |  | 16% | The year the business being sold was established. | [link](https://dd.reso.org/DD2.0/Property/YearEstablished/) |
| `YearsCurrentOwner` | Number | Business |  | 7% | The number of years the current owner has had possession of the business. | [link](https://dd.reso.org/DD2.0/Property/YearsCurrentOwner/) |
| `Zoning` | String | Tax |  | 63% | A division of the city or county into areas of different permissible land uses. | [link](https://dd.reso.org/DD2.0/Property/Zoning/) |
| `ZoningDescription` | String | Tax |  | 59% | A list of descriptions of the zoning of the property. | [link](https://dd.reso.org/DD2.0/Property/ZoningDescription/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>AboveGradeFinishedArea</code></summary>

  - **BEDES:** Location = "Above grade" Finished Status = "Finished" Area = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Área Completada por Encima del Piso
  - **French-Canadian Name:** Superficie finie au-dessus du niveau du sol
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AboveGradeFinishedAreaSource</code></summary>

  - **BEDES:** Origin = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Fuente del Área Completada por Encima del Piso
  - **French-Canadian Name:** Source des mesures de la superficie finie au-dessus du niveau du sol
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AboveGradeFinishedAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Unidades de Área Completada por Encima del Piso
  - **French-Canadian Name:** Unité de mesure de la superficie finie au-dessus du niveau du sol
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AboveGradeUnfinishedArea</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AboveGradeUnfinishedAreaSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AboveGradeUnfinishedAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AccessCode</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Código de Acceso
  - **French-Canadian Name:** Code d’accès
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AccessibilityFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Características de Accesibilidad
  - **French-Canadian Name:** Caractéristiques de l’accessibilité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>ActivationDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 5/21/2020
  - **Revision Date:** 5/21/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AdditionalParcelsDescription</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Descripción Adicional de Parcelas
  - **French-Canadian Name:** Description des parcelles additionnelles
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AdditionalParcelsYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Parcelas Adicionales SN
  - **French-Canadian Name:** Parcelles additionnelles O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AnchorsCoTenants</code></summary>

  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Co Inquilinos Ancla
  - **French-Canadian Name:** Magasins piliers colocataires
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Appliances</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Electrodomésticos
  - **French-Canadian Name:** Appareils électroménagers
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ArchitecturalStyle</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Estilo Arquitectónico
  - **French-Canadian Name:** Style architectural
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AssociationAmenities</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Servicios de la Asociación
  - **French-Canadian Name:** Commodités offertes par l’association
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationFee</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Tarifa de Asociación
  - **French-Canadian Name:** Frais payés à l’association
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationFee2</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Tarifa de Asociación2
  - **French-Canadian Name:** Frais payés à l’association 2
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationFee2Frequency</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Frecuencia de Tarifa de Asociación2
  - **French-Canadian Name:** Fréquence de paiement des frais à l’association 2
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationFeeFrequency</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Frecuencia de Tarifa de Asociación
  - **French-Canadian Name:** Fréquence de paiement des frais à l’association
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationFeeIncludes</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Inclusiones de Tarifa de Asociación
  - **French-Canadian Name:** Compris dans les frais payés à l’association
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Nombre de Asociación
  - **French-Canadian Name:** Nom de l’association
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationName2</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Nombre de Asociación2
  - **French-Canadian Name:** Nom de l’association 2
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Teléfono de la Asociación
  - **French-Canadian Name:** Numéro de téléphone de l’association
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationPhone2</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Teléfono de la Asociación2
  - **French-Canadian Name:** Numéro de téléphone de l’association 2
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AssociationYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI
  - **Status:** Active
  - **Spanish Name:** Asociación SN
  - **French-Canadian Name:** Association O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AttachedGarageYN</code></summary>

  - **BEDES:** Location = "Garage"If AttachedGarageYN == 'Y' then Vertical Surroundings = "Attached", Else Vertical Surroundings = "Stand-alone"
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Garaje Adjunto SN
  - **French-Canadian Name:** Garage attenant O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>AttributionContact</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 4/26/2022
  - **Revision Date:** 4/26/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>AvailabilityDate</code></summary>

  - **Property Types:** RLSE , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Fecha de Disponibilidad
  - **French-Canadian Name:** Date de disponibilité
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>AvailableLeaseType</code></summary>

  - **Property Types:** COML
  - **Status:** Active
  - **Status Change Date:** 4/22/2020
  - **Revision Date:** 4/22/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BackOnMarketDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Basement</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Sótano
  - **French-Canadian Name:** Sous-sol
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BasementYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Sótano Si or No
  - **French-Canadian Name:** Sous-sol O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>BathroomsFull</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños Completos
  - **French-Canadian Name:** Salles de bains complètes
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>BathroomsHalf</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños Medios
  - **French-Canadian Name:** Demi-salles de bains
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>BathroomsOneQuarter</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños un Cuarto
  - **French-Canadian Name:** Quarts de salles de bains
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BathroomsPartial</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños Parciales
  - **French-Canadian Name:** Salles de bains partielles
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>BathroomsThreeQuarter</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños Tres Cuartos
  - **French-Canadian Name:** Trois-quarts de salles de bains
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BathroomsTotalInteger</code></summary>

  - **BEDES:** Spatial Unit Type = "Restroom" Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Baños Integral Total
  - **French-Canadian Name:** Salles de bains totales
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>BedroomsPossible</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Habitaciones Posibles
  - **French-Canadian Name:** Chambres à coucher possibles
  - **Status Change Date:** 9/2/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BedroomsTotal</code></summary>

  - **BEDES:** Spatial Unit Type = "Bedroom"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Habitaciones Total
  - **French-Canadian Name:** Chambres à coucher totales
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BelowGradeFinishedArea</code></summary>

  - **BEDES:** Location = "Below grade"Finished Status = "Finished"Area = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Área Completada por Encima del Piso
  - **French-Canadian Name:** Superficie finie au-dessous du niveau du sol
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BelowGradeFinishedAreaSource</code></summary>

  - **BEDES:** Origin = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Fuente del Área Completada por Encima del Piso
  - **French-Canadian Name:** Source des mesures de la superficie finie au-dessous du niveau du sol
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BelowGradeFinishedAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Unidades de Área Completada por Encima del Piso
  - **French-Canadian Name:** Unité de mesure de la superficie finie au-dessous du niveau du sol
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BelowGradeUnfinishedArea</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BelowGradeUnfinishedAreaSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BelowGradeUnfinishedAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 2/21/2019
  - **Revision Date:** 2/21/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BodyType</code></summary>

  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Tipo de Conjunto
  - **French-Canadian Name:** Type de maison mobile
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuilderModel</code></summary>

  - **BEDES:** Builder Model = [value]
  - **Property Types:** RESI , RLSE , RINC , FARM
  - **Status:** Active
  - **Spanish Name:** Modelo Constructor
  - **French-Canadian Name:** Modèle du constructeur
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuilderName</code></summary>

  - **BEDES:** Contact Label = "Builder"Company Name = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Nombre Constructor
  - **French-Canadian Name:** Nom du constructeur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuildingAreaSource</code></summary>

  - **BEDES:** Origin = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Fuente de Área de Construcción
  - **French-Canadian Name:** Source des mesures de la superficie en construction
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuildingAreaTotal</code></summary>

  - **BEDES:** Interval Measure = "Total"Premises Level = "Building"Area = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Área Total de Construcción
  - **French-Canadian Name:** Superficie totale en construction
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuildingAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Unidades de Área de Construcción
  - **French-Canadian Name:** Unité de mesure de la superficie en construction
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuildingFeatures</code></summary>

  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Características de Construcción
  - **French-Canadian Name:** Caractéristiques du bâtiment
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuildingName</code></summary>

  - **BEDES:** Premises Level = "Building"Identifier Label = "Name"Identifier = [value]
  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Nombre de Edificio
  - **French-Canadian Name:** Nom du bâtiment
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BusinessName</code></summary>

  - **BEDES:** Contact Label = "Business"Company Name = [value]
  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Negocio
  - **French-Canadian Name:** Nom de l’entreprise
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BusinessType</code></summary>

  - **BEDES:** Contact Label = "Business" Occupancy Classification = [value]
  - **Property Types:** COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Negocio
  - **French-Canadian Name:** Type d’entreprise
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgent</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/7/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>BuyerAgentAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Agente Comprandor de AOR
  - **French-Canadian Name:** Chambre/association immobilière du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentDesignation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Denominación de Agente Comprador
  - **French-Canadian Name:** Titre du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>BuyerAgentDirectPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Directo de Agente Comprador
  - **French-Canadian Name:** Numéro de téléphone direct du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Agente Comprador
  - **French-Canadian Name:** Courriel du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Agente Comprador
  - **French-Canadian Name:** Numéro de télécopieur du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentFirstName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Agente Comprador
  - **French-Canadian Name:** Prénom du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentFullName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre Completo de Agente Comprador
  - **French-Canadian Name:** Nom complet du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentHomePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Casa de Agente Comprador
  - **French-Canadian Name:** Numéro de téléphone du domicile du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Agente Comprador
  - **French-Canadian Name:** Clé du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentLastName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Apellido de Agente Comprador
  - **French-Canadian Name:** Nom de famille du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentMiddleName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Segundo Nombre de Agente Comprador
  - **French-Canadian Name:** Deuxième prénom du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Agente Comprador
  - **French-Canadian Name:** ID MLS du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentMobilePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Móvil de Agente Comprador
  - **French-Canadian Name:** Numéro de cellulaire du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentNamePrefix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Prefijo de Agente Comprador
  - **French-Canadian Name:** Titre de civilité du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentNameSuffix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo de Agente Comprador
  - **French-Canadian Name:** Suffixe du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BuyerAgentOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho de Agente Comprador
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Agente Comprador
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentPager</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buscapersonas de Agente Comprador
  - **French-Canadian Name:** Numéro de pagette du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentPreferredPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Preferido de Agente Comprador
  - **French-Canadian Name:** Numéro de téléphone préféré du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentPreferredPhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Teléfono Preferido de Agente Comprador
  - **French-Canadian Name:** Poste téléphonique préféré du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentStateLicense</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Agente Comprador
  - **French-Canadian Name:** Permis délivré par l’état du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentTollFreePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Gratuito de Agente Comprador
  - **French-Canadian Name:** Numéro de téléphone sans frais du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Agente Comprador
  - **French-Canadian Name:** URL du site Web du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentVoiceMail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buzón de Voz de Agente Comprador
  - **French-Canadian Name:** Messagerie vocale du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerAgentVoiceMailExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ext de Buzón de Voz de Agente Comprador
  - **French-Canadian Name:** Poste de la messagerie vocale du courtier ou agent de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerBrokerageCompensation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 2/20/2020
  - **Revision Date:** 2/20/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BuyerBrokerageCompensationType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 2/20/2020
  - **Revision Date:** 2/20/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BuyerFinancing</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Financiamiento de Comprador
  - **French-Canadian Name:** Financement de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOffice</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/8/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>BuyerOfficeAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Despacho de Comprador de AOR
  - **French-Canadian Name:** Chambre/association immobilière du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Despacho de Comprador
  - **French-Canadian Name:** Courriel du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Despacho de Comprador
  - **French-Canadian Name:** Numéro de télécopieur du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho de Comprador
  - **French-Canadian Name:** Clé du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho de Comprador
  - **French-Canadian Name:** ID MLS du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Despacho de Comprador
  - **French-Canadian Name:** Nom du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>BuyerOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho de Comprador
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Despacho de Comprador
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerOfficeURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Despacho de Comprador
  - **French-Canadian Name:** URL du site Web du bureau du courtier ou agent de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>BuyerTeam</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/15/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>BuyerTeamKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Equipo Comprador
  - **French-Canadian Name:** Clé de l’équipe du courtier ou agent de l’acheteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>BuyerTeamName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Equipo Comprador
  - **French-Canadian Name:** Nom de l’équipe du courtier ou agent de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>CableTvExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto de TV por Cable
  - **French-Canadian Name:** Dépenses en télévision par câble
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CancellationDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Cancelación
  - **French-Canadian Name:** Date d’annulation
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CapRate</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tasa Máxima
  - **French-Canadian Name:** Taux de capitalisation
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CarportSpaces</code></summary>

  - **BEDES:** Premises Enclosure = "Non enclosed"Spatial Unit Type = "Parking space"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Espacios de Garaje
  - **French-Canadian Name:** Abris d’auto
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CarportYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Garaje SN
  - **French-Canadian Name:** Abris d’auto O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CarrierRoute</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ruta Transportista
  - **French-Canadian Name:** Itinéraire de transport
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>City</code></summary>

  - **BEDES:** City = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ciudad
  - **French-Canadian Name:** Ville
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>CityRegion</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ciudad Región
  - **French-Canadian Name:** Quartier de la ville
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>CloseDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Cierre
  - **French-Canadian Name:** Date de clôture
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ClosePrice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Precio de Cierre
  - **French-Canadian Name:** Prix de clôture
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgent</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/9/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>CoBuyerAgentAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Agente Co-Comprandor de AOR
  - **French-Canadian Name:** Chambre/association immobilière du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentDesignation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Denominación de Agente Co-Comprador
  - **French-Canadian Name:** Titre du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>CoBuyerAgentDirectPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Directo de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone direct du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Agente Co-Comprador
  - **French-Canadian Name:** Courriel du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de télécopieur du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentFirstName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Agente Co-Comprador
  - **French-Canadian Name:** Prénom du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentFullName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre Completo de Agente Co-Comprador
  - **French-Canadian Name:** Nom complet du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentHomePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Casa de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone du domicile du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Agente Co-Comprador
  - **French-Canadian Name:** Clé du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentLastName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Apellido de Agente Co-Comprador
  - **French-Canadian Name:** Nom de famille du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentMiddleName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Segundo Nombre de Agente Co-Comprador
  - **French-Canadian Name:** Deuxième prénom du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Agente Co-Comprador
  - **French-Canadian Name:** ID MLS du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentMobilePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Móvil de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de cellulaire du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentNamePrefix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Prefijo de Agente Co-Comprador
  - **French-Canadian Name:** Titre de civilité du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentNameSuffix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo de Agente Co-Comprador
  - **French-Canadian Name:** Suffixe du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CoBuyerAgentOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Despacho de Agente Co-Comprador
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentPager</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buscapersonas de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de pagette du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentPreferredPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Preferido de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone préféré du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentPreferredPhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Teléfono Preferido de Agente Co-Comprador
  - **French-Canadian Name:** Poste téléphonique préféré du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentStateLicense</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Agente Co-Comprador
  - **French-Canadian Name:** Permis délivré par l’état du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentTollFreePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Gratuito de Agente Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone sans frais du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Agente Co-Comprador
  - **French-Canadian Name:** URL du site Web du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentVoiceMail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buzón de Voz de Agente Co-Comprador
  - **French-Canadian Name:** Messagerie vocale du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerAgentVoiceMailExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ext de Buzón de Voz de Agente Co-Comprador
  - **French-Canadian Name:** Poste de la messagerie vocale du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOffice</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/10/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>CoBuyerOfficeAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Despacho de Co-Comprador de AOR
  - **French-Canadian Name:** Chambre/association immobilière du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Despacho de Co-Comprador
  - **French-Canadian Name:** Courriel du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Despacho de Co-Comprador
  - **French-Canadian Name:** Numéro de télécopieur du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho de Co-Comprador
  - **French-Canadian Name:** Clé du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho de Co-Comprador
  - **French-Canadian Name:** ID MLS du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Despacho de Co-Comprador
  - **French-Canadian Name:** Nom du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CoBuyerOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho de Co-Comprador
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Despacho de Co-Comprador
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoBuyerOfficeURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Despacho de Co-Comprador
  - **French-Canadian Name:** URL du site Web du bureau du courtier ou agent associé de l’acheteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgent</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/11/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>CoListAgentAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Agente Co-Enlistado de AOR
  - **French-Canadian Name:** Chambre/association immobilière du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentDesignation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Denominación de Agente Co-Enlistado
  - **French-Canadian Name:** Titre du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>CoListAgentDirectPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Directo de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone direct du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Agente Co-Enlistado
  - **French-Canadian Name:** Courriel du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de télécopieur du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentFirstName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Agente Co-Enlistado
  - **French-Canadian Name:** Prénom du courtier ou agent co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentFullName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre Completo de Agente Co-Enlistado
  - **French-Canadian Name:** Nom complet du courtier ou agent co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentHomePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Casa de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone du domicile du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Agente Co-Enlistado
  - **French-Canadian Name:** Clé du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentLastName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Apellido de Agente Co-Enlistado
  - **French-Canadian Name:** Nom de famille du courtier ou agent co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentMiddleName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Segundo Nombre de Agente Co-Enlistado
  - **French-Canadian Name:** Deuxième prénom du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Agente Co-Enlistado
  - **French-Canadian Name:** ID MLS du courtier ou agent co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentMobilePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Móvil de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de cellulaire du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentNamePrefix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Prefijo de Agente Co-Enlistado
  - **French-Canadian Name:** Titre de civilité du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentNameSuffix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo de Agente Co-Enlistado
  - **French-Canadian Name:** Suffixe du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CoListAgentOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Oficina de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Agente Co-Enlistado
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent co-inscripteur
  - **Status Change Date:** 1/13/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentPager</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buscapersonas de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de pagette du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentPreferredPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Preferido de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone préféré du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentPreferredPhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Teléfono Preferido de Agente Co-Enlistado
  - **French-Canadian Name:** Poste téléphonique préféré du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentStateLicense</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Agente Co-Enlistado
  - **French-Canadian Name:** Permis délivré par l’état du courtier ou agent co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentTollFreePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Gratuito de Agente Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone sans frais du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Agente Co-Enlistado
  - **French-Canadian Name:** URL du site Web du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentVoiceMail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buzón de Voz de Agente Co-Enlistado
  - **French-Canadian Name:** Messagerie vocale du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListAgentVoiceMailExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ext de Buzón de Voz de Agente Co-Enlistado
  - **French-Canadian Name:** Poste de la messagerie vocale du courtier ou agent co-inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOffice</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/12/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>CoListOfficeAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Despacho de Co-Enlistado de AOR
  - **French-Canadian Name:** Chambre/association immobilière du bureau co-inscripteur
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Despacho de Co-Enlistado
  - **French-Canadian Name:** Courriel du bureau co-inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Despacho de Co-Enlistado
  - **French-Canadian Name:** Numéro de télécopieur du bureau co-inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho de Co-Enlistado
  - **French-Canadian Name:** Clé du bureau co-inscripteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho de Co-Enlistado
  - **French-Canadian Name:** ID MLS du bureau co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>CoListOfficeName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Despacho de Co-Enlistado
  - **French-Canadian Name:** Nom du bureau co-inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CoListOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho de Co-Enlistado
  - **French-Canadian Name:** Numéro de téléphone du bureau co-inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Despacho de Co-Enlistado
  - **French-Canadian Name:** Poste téléphonique du bureau co-inscripteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoListOfficeURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Despacho de Co-Enlistado
  - **French-Canadian Name:** URL du site Web du bureau co-inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CommonInterest</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Interés Común
  - **French-Canadian Name:** Intérêt commun
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>CommonWalls</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Paredes Comunales
  - **French-Canadian Name:** Murs mitoyens
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CommunityFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Comunidad
  - **French-Canadian Name:** Caractéristiques de la collectivité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CompSaleYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 11/14/2018
  - **Revision Date:** 11/14/2018
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>CompensationComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 8/18/2022
  - **Revision Date:** 8/18/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Concessions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Concesiones
  - **French-Canadian Name:** Concessions
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ConcessionsAmount</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Monto de Concesiones
  - **French-Canadian Name:** Valeur des concessions
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ConcessionsComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios de Concesiones
  - **French-Canadian Name:** Commentaires relatifs aux concessions
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ConstructionMaterials</code></summary>

  - **BEDES:** Material = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Materiales de Concesiones
  - **French-Canadian Name:** Matériaux de construction
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ContinentRegion</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Región Continente
  - **French-Canadian Name:** Région du continent
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>Contingency</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Contingencia
  - **French-Canadian Name:** Conditions
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ContingentDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Fecha de Contingencia
  - **French-Canadian Name:** Date associée aux conditions
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ContractStatusChangeDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Cambio de Fecha de Estado de Contrato
  - **French-Canadian Name:** Date du changement de statut contractuel
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Cooling</code></summary>

  - **BEDES:** Cooling Type = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Climatización
  - **French-Canadian Name:** Refroidissement
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CoolingYN</code></summary>

  - **BEDES:** Conditioning Status = "Cooled" Conditioning Status = "Uncooled"
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Climatización SN
  - **French-Canadian Name:** Appareils de refroidissement O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CopyrightNotice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Aviso de Derechos de Autor
  - **French-Canadian Name:** Avis de droit d’auteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>Country</code></summary>

  - **BEDES:** Country Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** País
  - **French-Canadian Name:** Pays
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CountryRegion</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** País Región
  - **French-Canadian Name:** Région du pays
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>CountyOrParish</code></summary>

  - **BEDES:** County = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Condado o Distrito
  - **French-Canadian Name:** Comté ou paroisse
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>CoveredSpaces</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Espacios Cubiertos
  - **French-Canadian Name:** Espaces couverts
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CropsIncludedYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Cultivos Incluidos SN
  - **French-Canadian Name:** Cultures incluses O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CrossStreet</code></summary>

  - **BEDES:** Corner Of = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Calle Transversal
  - **French-Canadian Name:** Rue transversale
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CultivatedArea</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Área Cultivada
  - **French-Canadian Name:** Superficie cultivée
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>CumulativeDaysOnMarket</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Días Acumulados en el Mercado
  - **French-Canadian Name:** Jours cumulatifs sur le marché
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>CurrentFinancing</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Financiación Actual
  - **French-Canadian Name:** Financement actuel
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>CurrentUse</code></summary>

  - **Property Types:** LAND
  - **Status:** Active
  - **Spanish Name:** Uso Actual
  - **French-Canadian Name:** Utilisation actuelle
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>DOH1</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** DOH 1
  - **French-Canadian Name:** Department of Housing 1
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DOH2</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** DOH 2
  - **French-Canadian Name:** Department of Housing 2
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DOH3</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** DOH 3
  - **French-Canadian Name:** Department of Housing 3
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DaysInMls</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 9/10/2019
  - **Revision Date:** 9/10/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>DaysOnMarket</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Días en el Mercado
  - **French-Canadian Name:** Jours sur le marché
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DaysOnSite</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 9/10/2019
  - **Revision Date:** 9/10/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>DevelopmentStatus</code></summary>

  - **Property Types:** LAND
  - **Status:** Active
  - **Spanish Name:** Estado de Desarrollo
  - **French-Canadian Name:** Stade de développement
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>DirectionFaces</code></summary>

  - **BEDES:** Location = "Public entrance"Cardinal Orientation = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Orientación de Superficies
  - **French-Canadian Name:** Orientation du bâtiment
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Directions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Orientaciones
  - **French-Canadian Name:** Directions routières
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Disclaimer</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Aviso Legal
  - **French-Canadian Name:** Avis de non-responsabilité
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Disclosures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Divulgaciones
  - **French-Canadian Name:** Informations divulguées
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToBusComments</code></summary>

  - **BEDES:** Distance To Public Transportation = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Bus
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et l’arrêt d’autobus
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToBusNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Númerico Distancia a Bus
  - **French-Canadian Name:** Distance entre la propriété et l’arrêt d’autobus
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToBusUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Bus
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et l’arrêt d’autobus
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToElectricComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Electricidad
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le service public d’électricité
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToElectricNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Electricidad
  - **French-Canadian Name:** Distance entre la propriété et le service public d’électricité
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToElectricUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Electricidad
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le service public d’électricité
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToFreewayComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Autopista
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et l’autoroute
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToFreewayNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Autopista
  - **French-Canadian Name:** Distance entre la propriété et l’autoroute
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToFreewayUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Autopista
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et l’autoroute
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToGasComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Gasolinera
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le service public de gaz naturel
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToGasNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Númerico Distancia a Gasolinera
  - **French-Canadian Name:** Distance entre la propriété et le service public de gaz naturel
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToGasUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Gasolinera
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le service public de gaz naturel
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToPhoneServiceComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Servicios Telefónicos
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le service public de téléphone
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToPhoneServiceNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Servicios Telefónicos
  - **French-Canadian Name:** Distance entre la propriété et le service public de téléphone
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToPhoneServiceUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Servicios Telefónicos
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le service public de téléphone
  - **Status Change Date:** 1/24/2019
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToPlaceofWorshipComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Templo Religioso
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le lieu de culte
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToPlaceofWorshipNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Templo Religioso
  - **French-Canadian Name:** Distance entre la propriété et le lieu de culte
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToPlaceofWorshipUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Templo Religioso
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le lieu de culte
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSchoolBusComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Bus Escolar
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et l’arrêt d’autobus scolaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToSchoolBusNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Númerico Distancia a Bus Escolar
  - **French-Canadian Name:** Distance entre la propriété et l’arrêt d’autobus scolaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSchoolBusUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Bus Escolar
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et l’arrêt d’autobus scolaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSchoolsComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Escuelas
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et l’école
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToSchoolsNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Númerico Distancia a Escuelas
  - **French-Canadian Name:** Distance entre la propriété et l’école
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSchoolsUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Escuelas
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et l’école
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSewerComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Alcantarillado
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le service public d’égout
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToSewerNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Alcantarillado
  - **French-Canadian Name:** Distance entre la propriété et le service public d’égout
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToSewerUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Alcantarillado
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le service public d’égout
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToShoppingComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Centro Comercial
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le centre commercial
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToShoppingNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Centro Comercial
  - **French-Canadian Name:** Distance entre la propriété et le centre commercial
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToShoppingUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Centro Comercial
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le centre commercial
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToStreetComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Calle
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et la rue
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToStreetNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Calle
  - **French-Canadian Name:** Distance entre la propriété et la rue
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToStreetUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Calle
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et la rue
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToWaterComments</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentarios Distancia a Agua
  - **French-Canadian Name:** Commentaires relatifs à la distance entre la propriété et le service public d’eau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DistanceToWaterNumeric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Numérico Distancia a Agua
  - **French-Canadian Name:** Distance entre la propriété et le service public d’eau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DistanceToWaterUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades Distancia a Agua
  - **French-Canadian Name:** Unité de mesure de la distance entre la propriété et le service public d’eau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>DocumentStatus</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status Change Date:** 2/24/2022
  - **Revision Date:** 2/24/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>DocumentsAvailable</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , BUSO
  - **Status:** Active
  - **Spanish Name:** Documentos Disponibles
  - **French-Canadian Name:** Documents disponibles
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DocumentsChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Cambio de Documentos
  - **French-Canadian Name:** Heure et date de la mise à jour des documents
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DocumentsCount</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Conteo de Documentos
  - **French-Canadian Name:** Nombre de documents
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DoorFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Puerta
  - **French-Canadian Name:** Caractéristiques des portes
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>DualOrVariableRateCommissionYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 2/20/2020
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Electric</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Electricidad
  - **French-Canadian Name:** Électricité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ElectricExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Gasto Eléctrico
  - **French-Canadian Name:** Dépenses en électricité
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ElectricOnPropertyYN</code></summary>

  - **Property Types:** LAND , FARM
  - **Status:** Active
  - **Spanish Name:** Electricidad en la Propiedad SN
  - **French-Canadian Name:** Électricité sur la propriété O/N
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ElementarySchool</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Escuela Primaria
  - **French-Canadian Name:** École élémentaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ElementarySchoolDistrict</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Distrito de Escuela Primaria
  - **French-Canadian Name:** District de l’école élémentaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Elevation</code></summary>

  - **BEDES:** Elevation = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Elevación
  - **French-Canadian Name:** Élévation
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ElevationUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Unidades de Elevación
  - **French-Canadian Name:** Unité de mesure de l’élévation
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>EntryLevel</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Nivel de Entrada
  - **French-Canadian Name:** Étage où est située de la porte d’entrée
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>EntryLocation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Ubicación de Entrada
  - **French-Canadian Name:** Emplacement de la porte d’entrée
  - **Status Change Date:** 5/21/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Exclusions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Exclusiones
  - **French-Canadian Name:** Exclusions
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ExistingLeaseType</code></summary>

  - **Property Types:** RINC , COMS
  - **Status:** Active
  - **French-Canadian Name:** Type de bail existant
  - **Status Change Date:** 4/22/2020
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ExpirationDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Expiración
  - **French-Canadian Name:** Date d’expiration
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ExteriorFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características Externas
  - **French-Canadian Name:** Caractéristiques de l’extérieur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FarmCreditServiceInclYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Servicio de Crédito Agrícola Incluido SN
  - **French-Canadian Name:** Farm Credit Services of America inclus O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FarmLandAreaSource</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Fuente de Área de Tierra Agrícola
  - **French-Canadian Name:** Source des mesures de la terre agricole
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FarmLandAreaUnits</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Unidades de Área de Tierra Agrícola
  - **French-Canadian Name:** Unité de mesure de la terre agricole
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Fencing</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Cercado
  - **French-Canadian Name:** Clôture
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>FhaEligibility</code></summary>

  - **Property Types:** RESI , MOBI
  - **Status:** Active
  - **Status Change Date:** 11/17/2016
  - **Revision Date:** 11/17/2016
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>FinancialDataSource</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Fuente de Información Financiera
  - **French-Canadian Name:** Source des données financières
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FireplaceFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Chimenea
  - **French-Canadian Name:** Caractéristiques du foyer
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FireplaceYN</code></summary>

  - **BEDES:** Heating Type = "Fireplace"
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Chimenea SN
  - **French-Canadian Name:** Foyer O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FireplacesTotal</code></summary>

  - **BEDES:** Heating Type = "Fireplace"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Total de Chimeneas
  - **French-Canadian Name:** Foyers totaux
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Flooring</code></summary>

  - **BEDES:** Location = "Interior" Opaque Surface = "Floor" Finish = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Piso
  - **French-Canadian Name:** Revêtement de sol
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FoundationArea</code></summary>

  - **BEDES:** Floor Area Qualifier = "Footprint"Area = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Área de Cimientos
  - **French-Canadian Name:** Dimensions des fondations
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FoundationDetails</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Detalle de Cimientos
  - **French-Canadian Name:** Type de fondations
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FrontageLength</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Longitud de Fachada
  - **French-Canadian Name:** Longueur de la façade
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>FrontageType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Fachada
  - **French-Canadian Name:** Type de façade
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>FuelExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Gasto de Gasolina
  - **French-Canadian Name:** Dépenses en carburant
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Furnished</code></summary>

  - **Property Types:** RLSE
  - **Status:** Active
  - **Spanish Name:** Amueblado
  - **French-Canadian Name:** Meublé
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>FurnitureReplacementExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto de Reemplazo de Muebles
  - **French-Canadian Name:** Dépenses en remplacement de mobilier
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GarageSpaces</code></summary>

  - **BEDES:** Location = "Garage"Spatial Unit Type = "Parking space"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Espacios de Garaje
  - **French-Canadian Name:** Garages
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GarageYN</code></summary>

  - **BEDES:** Location = "Garage"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Garaje SN
  - **French-Canadian Name:** Garage O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GardenerExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto de Jardinero
  - **French-Canadian Name:** Dépenses en jardinage
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GrazingPermitsBlmYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Permisos de Pastoreo BLM SN
  - **French-Canadian Name:** Permis de pâturage du Bureau of Land Management O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GrazingPermitsForestServiceYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Permisos de Pastoreo Servicio Forestal SN
  - **French-Canadian Name:** Permis de pâturage du Forest Service O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GrazingPermitsPrivateYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Permisos de Pastoreo Privado SN
  - **French-Canadian Name:** Permis de pâturage privé O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenBuildingVerification</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Verificación de Edificio Verde
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>GreenBuildingVerificationType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tipo de Verificación de Edificio Verde
  - **French-Canadian Name:** Certification environnementale du bâtiment
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>GreenEnergyEfficient</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Energía Verde Eficiente
  - **French-Canadian Name:** Efficacité énergétique verte
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenEnergyGeneration</code></summary>

  - **BEDES:** Energy Generation Technology = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Generación de Energía Verde
  - **French-Canadian Name:** Génération d’énergie verte
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenIndoorAirQuality</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Calidad de Aire Interior Verde
  - **French-Canadian Name:** Mesures environnementales de la qualité de l’air à l’intérieur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenLocation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Ubicación Verde
  - **French-Canadian Name:** Emplacement vert
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenSustainability</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Sostenibilidad Verde
  - **French-Canadian Name:** Durabilité environnementale
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GreenVerificationYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 9/10/2019
  - **Revision Date:** 9/10/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>GreenWaterConservation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Conservación Ecológica de Agua
  - **French-Canadian Name:** Mesures environnementales de conservation des eaux
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GrossIncome</code></summary>

  - **Property Types:** RINC , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ingreso Bruto
  - **French-Canadian Name:** Revenu brut
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>GrossLivingAreaAnsi</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 4/26/2022
  - **Revision Date:** 4/26/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>GrossScheduledIncome</code></summary>

  - **Property Types:** RINC , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ingreso Bruto Programado
  - **French-Canadian Name:** Revenu brut prévu
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HabitableResidenceYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Residencia Habitable SN
  - **French-Canadian Name:** Résidence habitable O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Heating</code></summary>

  - **BEDES:** Heating Type = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Calefacción
  - **French-Canadian Name:** Chauffage
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HeatingYN</code></summary>

  - **BEDES:** Conditioning Status = "Heated"
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Calefacción SN
  - **French-Canadian Name:** Chauffage O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HighSchool</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Escuela Secundaria
  - **French-Canadian Name:** École secondaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HighSchoolDistrict</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Distrito de Escuela Secundaria
  - **French-Canadian Name:** District de l’école secondaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/20/2022
  - **Revision Date:** 1/20/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>HomeWarrantyYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Garantía Inmobiliaria SN
  - **French-Canadian Name:** Garantie habitation O/N
  - **Status Change Date:** 8/25/2023
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>HorseAmenities</code></summary>

  - **Property Types:** RESI , RLSE , LAND
  - **Status:** Active
  - **Spanish Name:** Servicios Equinos
  - **French-Canadian Name:** Commodités pour chevaux
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HorseYN</code></summary>

  - **Property Types:** RESI , RLSE , LAND
  - **Status:** Active
  - **Spanish Name:** Caballo SN
  - **French-Canadian Name:** Chevaux O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HoursDaysOfOperation</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Horas Días de Operación
  - **French-Canadian Name:** Jours/heures d’exploitation
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>HoursDaysOfOperationDescription</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Descripción de Horas Días de Operación
  - **French-Canadian Name:** Détails sur les jours/heures d’exploitation
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>Inclusions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Inclusiones
  - **French-Canadian Name:** Inclusions
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>IncomeIncludes</code></summary>

  - **Property Types:** RINC , LAND
  - **Status:** Active
  - **Spanish Name:** Inclusiones de Ingreso
  - **French-Canadian Name:** Compris dans le revenu
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>InsuranceExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Gasto Seguro
  - **French-Canadian Name:** Dépenses en assurance
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>InteriorFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características Internas
  - **French-Canadian Name:** Caractéristiques de l’intérieur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>InternetAddressDisplayYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Visualización de Dirección de Internet SN
  - **French-Canadian Name:** Affichage de l’adresse de l’inscription sur Internet O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>InternetAutomatedValuationDisplayYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Visualización de Valuación Automática de Internet SN
  - **French-Canadian Name:** Affichage de l’évaluation automatisée de l’inscription sur Internet O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>InternetConsumerCommentYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Comentario de Consumidor de Internet SN
  - **French-Canadian Name:** Affichage des commentaires des consommateurs sur l’inscription sur Internet O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>InternetEntireListingDisplayYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Visualización de Listado Completo de Internet SN
  - **French-Canadian Name:** Affichage de l’inscription en entier sur Internet O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>IrrigationSource</code></summary>

  - **Property Types:** LAND , FARM
  - **Status:** Active
  - **Spanish Name:** Fuente de Irrigación
  - **French-Canadian Name:** Source d’irrigation
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>IrrigationWaterRightsAcres</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Derechos de Agua de Riego Hectáreas
  - **French-Canadian Name:** Acres pouvant être irrigués en vertu des droits relatifs à l’eau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>IrrigationWaterRightsYN</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Derechos de Agua de Riego SN
  - **French-Canadian Name:** Droits relatifs à l’eau O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>LaborInformation</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Información Laboral
  - **French-Canadian Name:** Information sur les lois sur le travail
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>LandLeaseAmount</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Monto de Arrendamiento de Tierra
  - **French-Canadian Name:** Montant du loyer
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LandLeaseAmountFrequency</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Frecuencia de Monto de Arrendamiento de Tierra
  - **French-Canadian Name:** Fréquence des paiements du loyer
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LandLeaseExpirationDate</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Expiración de Arrendamiento de Tierra
  - **French-Canadian Name:** Date d’expiration du bail foncier
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LandLeaseYN</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Arrendamiento de Tierra SN
  - **French-Canadian Name:** Bail foncier O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Latitude</code></summary>

  - **BEDES:** Latitude = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Latitud
  - **French-Canadian Name:** Latitude
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LaundryFeatures</code></summary>

  - **BEDES:** Laundry Appliance Type = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Características de Lavandería
  - **French-Canadian Name:** Caractéristiques de la buanderie
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeasableArea</code></summary>

  - **BEDES:** Floor Area Qualifier = "Rentable"Area = [value]
  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Área Arrendable
  - **French-Canadian Name:** Superficie locative
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeasableAreaUnits</code></summary>

  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Unidades de Área Arrendable
  - **French-Canadian Name:** Mesures de la superficie locative
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseAmount</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Monto de Arrendamiento
  - **French-Canadian Name:** Montant du loyer
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseAmountFrequency</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Frecuencia de Monto de Arrendamiento
  - **French-Canadian Name:** Fréquence des paiements du loyer
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseAssignableYN</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Arrendamiento Asignable SN
  - **French-Canadian Name:** Bail transférable O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseConsideredYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Arrendamiento Considerado SN
  - **French-Canadian Name:** Location envisagée O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseExpiration</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Vencimiento de Arrendamiento
  - **French-Canadian Name:** Date d’expiration du bail
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseRenewalCompensation</code></summary>

  - **Property Types:** RLSE
  - **Status:** Active
  - **Spanish Name:** Compensación por Renovación de Arrendamiento
  - **French-Canadian Name:** Rémunération pour le renouvellement du bail
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseRenewalOptionYN</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Opción de Renovación de Arrendamiento SN
  - **French-Canadian Name:** Option de renouvellement du bail O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LeaseTerm</code></summary>

  - **Property Types:** RLSE
  - **Status:** Active
  - **Spanish Name:** Plazo de Arrendamiento
  - **French-Canadian Name:** Modalités du bail
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Levels</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Niveles
  - **French-Canadian Name:** Étages
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>License1</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Licencia 1
  - **French-Canadian Name:** Permis 1
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>License2</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Licencia 2
  - **French-Canadian Name:** Permis 2
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>License3</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Licencia 3
  - **French-Canadian Name:** Permis 3
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LicensesExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Costo Licencias
  - **French-Canadian Name:** Dépenses relatives aux permis
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAOR</code></summary>

  - **BEDES:** Contact Label = "Association of Realtors"Company Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Listado de AOR
  - **French-Canadian Name:** Chambre/association immobilière responsable de l’inscription
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgent</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/13/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListAgentAOR</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Contact Label = "Association of Realtors" Company Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Agente Enlistado de AOR
  - **French-Canadian Name:** Chambre/association immobilière du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentDesignation</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Credential = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Denominación de Agente Enlistado
  - **French-Canadian Name:** Titre du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>ListAgentDirectPhone</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Direct" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Directo de Agente Enlistado
  - **French-Canadian Name:** Numéro de téléphone direct du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentEmail</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Email Address = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Agente Enlistado
  - **French-Canadian Name:** Courriel du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListAgentFax</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Fax" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Agente Enlistado
  - **French-Canadian Name:** Numéro de télécopieur du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentFirstName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Agente Enlistado
  - **French-Canadian Name:** Prénom du courtier ou agent inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentFullName</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Full Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre Completo de Agente Enlistado
  - **French-Canadian Name:** Nom complet du courtier ou agent inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListAgentHomePhone</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Home" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Casa de Agente Enlistado
  - **French-Canadian Name:** Numéro de téléphone du domicile du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentKey</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Contact ID = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Agente Enlistado
  - **French-Canadian Name:** Clé du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListAgentLastName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Apellido de Agente Enlistado
  - **French-Canadian Name:** Nom de famille du courtier ou agent inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentMiddleName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Segundo Nombre de Agente Enlistado
  - **French-Canadian Name:** Deuxième prénom du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Agente Enlistado
  - **French-Canadian Name:** ID MLS du courtier ou agent inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListAgentMobilePhone</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Mobile" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Móvil de Agente Enlistado
  - **French-Canadian Name:** Numéro de cellulaire du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentNamePrefix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Prefijo de Agente Enlistado
  - **French-Canadian Name:** Titre de civilité du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentNameSuffix</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo de Agente Enlistado
  - **French-Canadian Name:** Suffixe du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListAgentOfficePhone</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Work" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Oficina de Agente Enlistado
  - **French-Canadian Name:** Numéro de téléphone du bureau du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentOfficePhoneExt</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Work" Telephone Extension = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Agente Enlistado
  - **French-Canadian Name:** Poste téléphonique du bureau du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentPager</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Telephone Number Label = "Pager" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buscapersonas de Agente Enlistado
  - **French-Canadian Name:** Numéro de pagette du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentPreferredPhone</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Priority = "Primary" Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Preferido de Agente Enlistado
  - **French-Canadian Name:** Numéro de téléphone préféré du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentPreferredPhoneExt</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Priority = "Primary" Telephone Extension = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión de Teléfono Preferido de Agente Enlistado
  - **French-Canadian Name:** Poste téléphonique préféré du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentStateLicense</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Credential Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Agente Enlistado
  - **French-Canadian Name:** Permis délivré par l’état du courtier ou agent inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentTollFreePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono Gratuito de Agente Enlistado
  - **French-Canadian Name:** Numéro de téléphone sans frais du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentURL</code></summary>

  - **BEDES:** Contact Label = "Real estate agent" Contact URL = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Agente Enlistado
  - **French-Canadian Name:** URL du site Web du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentVoiceMail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Buzón de Voz de Agente Enlistado
  - **French-Canadian Name:** Messagerie vocale du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListAgentVoiceMailExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ext de Buzón de Voz de Agente Enlistado
  - **French-Canadian Name:** Poste de la messagerie vocale du courtier ou agent inscripteur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOffice</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/14/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListOfficeAOR</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Despacho Enlistado de AOR
  - **French-Canadian Name:** Chambre/association immobilière du bureau inscripteur
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOfficeEmail</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Email de Despacho Enlistado
  - **French-Canadian Name:** Courriel du bureau inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOfficeFax</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fax de Despacho Enlistado
  - **French-Canadian Name:** Numéro de télécopieur du bureau inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOfficeKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Despacho Enlistado
  - **French-Canadian Name:** Clé du bureau inscripteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListOfficeMlsId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de MLS de Despacho Enlistado
  - **French-Canadian Name:** ID MLS du bureau inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListOfficeName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Despacho Enlistado
  - **French-Canadian Name:** Nom du bureau inscripteur
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOfficeNationalAssociationId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2020
  - **Revision Date:** 1/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListOfficePhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Despacho Enlistado
  - **French-Canadian Name:** Numéro de téléphone du bureau inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListOfficePhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Extensión Telefónica de Despacho Enlistado
  - **French-Canadian Name:** Poste téléphonique du bureau inscripteur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListOfficeURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL de Despacho Enlistado
  - **French-Canadian Name:** URL du site Web bureau inscripteur
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListPrice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Precio de Venta
  - **French-Canadian Name:** Prix de l’inscription
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ListPriceLow</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Precio de Venta Más Bajo
  - **French-Canadian Name:** Prix inférieur de l’inscription
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListTeam</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/16/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListTeamKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Equipo de Ventas
  - **French-Canadian Name:** Clé de l’équipe du vendeur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ListTeamName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Equipo de Ventas
  - **French-Canadian Name:** Nom de l’équipe du vendeur
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ListingAgreement</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Acuerdo de Venta
  - **French-Canadian Name:** Contrat de courtage
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListingContractDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Contrato de Venta
  - **French-Canadian Name:** Date du contrat de courtage
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListingId</code></summary>

  - **BEDES:** Identifier Label = "Listing"Identifier = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID de Listado
  - **French-Canadian Name:** ID de l’inscription
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>ListingKey</code></summary>

  - **BEDES:** Identifier Label = "Listing"Subaddress Type = "Key"Identifier = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Listado
  - **French-Canadian Name:** Clé de l’inscription
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 1/9/2022
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>ListingService</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Servicio de Listado
  - **French-Canadian Name:** Service offert
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListingTerms</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Términos de Listado
  - **French-Canadian Name:** Modalités de l’inscription
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ListingURL</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2019
  - **Revision Date:** 1/17/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ListingURLDescription</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/17/2019
  - **Revision Date:** 1/17/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>LivingArea</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Área Habitable
  - **French-Canadian Name:** Superficie habitable
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LivingAreaSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Fuente de Área Habitable
  - **French-Canadian Name:** Source des mesures de la superficie habitable
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LivingAreaUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Unidades de Área Habitable
  - **French-Canadian Name:** Unité de mesure de la superficie habitable
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LockBoxLocation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ubicación de Caja de Seguridad
  - **French-Canadian Name:** Emplacement de la boîte à clés
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LockBoxSerialNumber</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Serie de Caja de Seguridad
  - **French-Canadian Name:** Numéro de série de la boîte à clés
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LockBoxType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Caja de Seguridad
  - **French-Canadian Name:** Type de boîte à clés
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Longitude</code></summary>

  - **BEDES:** Longitude = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Longitud
  - **French-Canadian Name:** Longitude
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LotDimensionsSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fuente de Dimensiones de Lote
  - **French-Canadian Name:** Source des dimensions du terrain
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>LotFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Lote
  - **French-Canadian Name:** Caractéristiques du terrain
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LotSizeAcres</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tamaño en Hectáreas de Lote
  - **French-Canadian Name:** Nombre d’acres du terrain
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>LotSizeArea</code></summary>

  - **BEDES:** Spatial Unit Type = "Lot"Area = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Área de Tamaño de Lote
  - **French-Canadian Name:** Superficie du terrain
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LotSizeDimensions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Dimensiones de Tamaño de Lote
  - **French-Canadian Name:** Dimensions du terrain
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LotSizeSource</code></summary>

  - **BEDES:** Spatial Unit Type = "Lot"Origin = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fuente de Tamaño de Lote
  - **French-Canadian Name:** Source des dimensions du terrain
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>LotSizeSquareFeet</code></summary>

  - **BEDES:** Spatial Unit Type = "Lot"Area = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tamaño de Lote en Pies Cuadrados
  - **French-Canadian Name:** Superficie du terrain en pieds carrés
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>LotSizeUnits</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Unidades de Tamaño de Lote
  - **French-Canadian Name:** Unité de mesure de la superficie du terrain
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MLSAreaMajor</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Área Mayor MLS
  - **French-Canadian Name:** Secteur principal du MLS
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MLSAreaMinor</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Área Menor MLS
  - **French-Canadian Name:** Secteur secondaire du MLS
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MainLevelBathrooms</code></summary>

  - **BEDES:** Location = "Ground floor"Spatial Unit Type = "Restroom"Quantity = [value]
  - **Property Types:** RESI , RLSE
  - **Status:** Active
  - **Spanish Name:** Baños Piso Principal
  - **French-Canadian Name:** Salles de bains au rez-de-chaussée
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>MainLevelBedrooms</code></summary>

  - **BEDES:** Location = "Ground floor"Spatial Unit Type = "Bedroom"Quantity = [value]
  - **Property Types:** RESI , RLSE
  - **Status:** Active
  - **Spanish Name:** Habitaciones Piso Principal
  - **French-Canadian Name:** Chambres à coucher au rez-de-chaussée
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>MaintenanceExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Costo Mantenimiento
  - **French-Canadian Name:** Dépenses en entretien
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MajorChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Cambio Principal
  - **French-Canadian Name:** Heure et date de la mise à jour importante
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MajorChangeType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Cambio Principal
  - **French-Canadian Name:** Type de mise à jour importante
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Make</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Make = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Marca
  - **French-Canadian Name:** Marque
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ManagerExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto Administración
  - **French-Canadian Name:** Dépenses en gestion
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MapCoordinate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Coordenadas en Mapa
  - **French-Canadian Name:** Coordonnées cartographiques
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MapCoordinateSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fuente de Coordenadas en Mapa
  - **French-Canadian Name:** Source des coordonnées cartographiques
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MapURL</code></summary>

  - **BEDES:** MapURL = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** URL Mapa
  - **French-Canadian Name:** URL de la carte
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Media</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/21/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MiddleOrJuniorSchool</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Escuela Media o Intermedia
  - **French-Canadian Name:** École intermédiaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MiddleOrJuniorSchoolDistrict</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Distrito de Escuela Media o Intermedia
  - **French-Canadian Name:** District de l’école intermédiaire
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MlsStatus</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Estado de MLS
  - **French-Canadian Name:** Statut MLS
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>MobileDimUnits</code></summary>

  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Unidades de Dimensión Móvil
  - **French-Canadian Name:** Unité de mesure linéaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MobileHomeRemainsYN</code></summary>

  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Restos Casa Móvil SN
  - **French-Canadian Name:** Maison mobile incluse O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MobileLength</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Length = [value]
  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Longitud Móvil
  - **French-Canadian Name:** Longueur de la maison mobile
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>MobileWidth</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Width = [value]
  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Anchura Móvil
  - **French-Canadian Name:** Largeur de la maison mobile
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Model</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Model Number = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Modelo
  - **French-Canadian Name:** Modèle
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **BEDES:** Date Status = "Modified"Date = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **French-Canadian Name:** Heure et date de la modification
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NetOperatingIncome</code></summary>

  - **Property Types:** RINC , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ingreso Operativo Neto
  - **French-Canadian Name:** Résultat net d’exploitation
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NewConstructionYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Nueva Construcción SN
  - **French-Canadian Name:** Nouvelle construction O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NewTaxesExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto Nuevos Impuestos
  - **French-Canadian Name:** Nouvelles dépenses fiscales
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfBuildings</code></summary>

  - **BEDES:** Spatial Unit Type = "Building"Quantity = [value]
  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Número de Edificios
  - **French-Canadian Name:** Nombre de bâtiments
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfFullTimeEmployees</code></summary>

  - **BEDES:** Occupant Quantity Type = "Full time equivalent workers"Quantity = [value]
  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Empleados Tiempo Completo
  - **French-Canadian Name:** Nombre d’employés à temps plein
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfLots</code></summary>

  - **BEDES:** Spatial Unit Type = "Lot"Quantity = [value]
  - **Property Types:** LAND
  - **Status:** Active
  - **Spanish Name:** Número de Lotes
  - **French-Canadian Name:** Nombre de lots
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfPads</code></summary>

  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Número de Apartamentos
  - **French-Canadian Name:** Nombre d’emplacements
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfPartTimeEmployees</code></summary>

  - **BEDES:** Occupant Quantity Type = "Part time workers"Quantity = [value]
  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Empleados Tiempo Parcial
  - **French-Canadian Name:** Nombre d’employés à temps partiel
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfSeparateElectricMeters</code></summary>

  - **BEDES:** Resource = "Electricity"Control Technology = "Meter"Quantity = [value]
  - **Property Types:** RINC , FARM
  - **Status:** Active
  - **Spanish Name:** Número de Medidores Eléctricos Individuales
  - **French-Canadian Name:** Nombre de compteurs électriques séparés
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfSeparateGasMeters</code></summary>

  - **BEDES:** Resource = "Natural gas"Control Technology = "Meter"Quantity = [value]
  - **Property Types:** RINC , FARM
  - **Status:** Active
  - **Spanish Name:** Número de Medidores de Gas Individuales
  - **French-Canadian Name:** Nombre de compteurs de gaz séparés
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfSeparateWaterMeters</code></summary>

  - **BEDES:** Resource = "Water"Control Technology = "Meter"Quantity = [value]
  - **Property Types:** RINC , FARM
  - **Status:** Active
  - **Spanish Name:** Número de Medidores de Agua Individuales
  - **French-Canadian Name:** Nombre de compteurs d’eau séparés
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfUnitsInCommunity</code></summary>

  - **BEDES:** Spatial Unit Type = "Unit"Quantity = [value]
  - **Property Types:** RESI , RLSE
  - **Status:** Active
  - **Spanish Name:** Número de Unidades en Comunidad
  - **French-Canadian Name:** Nombre d’unités dans la communauté
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfUnitsLeased</code></summary>

  - **BEDES:** Ownership Status = "Leased"Spatial Unit Type = "Apartment unit"Quantity = [value]
  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Número de Unidades Arrendadas
  - **French-Canadian Name:** Nombre d’unités sous contrat de location
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfUnitsMoMo</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Número de Unidades Mo Mo
  - **French-Canadian Name:** Nombre d’unités pouvant être louées au mois
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfUnitsTotal</code></summary>

  - **BEDES:** Spatial Unit Type = "Unit"Quantity = [value]
  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Número de Unidades Totales
  - **French-Canadian Name:** Nombre d’unités
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>NumberOfUnitsVacant</code></summary>

  - **BEDES:** Occupied Status = "Vacant"Spatial Unit Type = "Apartment unit"Quantity = [value]
  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Número de Unidades Disponibles
  - **French-Canadian Name:** Nombre d’unités inoccupées
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OccupantName</code></summary>

  - **BEDES:** Contact Label = "Occupant"Full Name = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Nombre de Ocupante
  - **French-Canadian Name:** Nom de l’occupant
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OccupantPhone</code></summary>

  - **BEDES:** Contact Label = "Occupant"Telephone Number = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Teléfono de Ocupante
  - **French-Canadian Name:** Numéro de téléphone de l’occupant
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OccupantType</code></summary>

  - **BEDES:** Occupied Status = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Tipo de Ocupante
  - **French-Canadian Name:** Type d’occupant
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OffMarketDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Retiro del Mercado
  - **French-Canadian Name:** Date de retrait du marché
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OffMarketTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Fuera del Mercado
  - **French-Canadian Name:** Heure et date du retrait du marché
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OnMarketDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Lanzamiento al Mercado
  - **French-Canadian Name:** Date de l’entrée sur le marché
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OnMarketTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Lanzamiento al Mercado
  - **French-Canadian Name:** Heure et date de l’entrée sur le marché
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OpenHouse</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/23/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OpenHouseModificationTimestamp</code></summary>

  - **Status:** Active
  - **Status Change Date:** 10/24/2023
  - **Revision Date:** 10/24/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OpenParkingSpaces</code></summary>

  - **BEDES:** Premises Enclosure = "Open"Spatial Unit Type = "Parking space"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Espacios Abiertos de Estacionamiento
  - **French-Canadian Name:** Espaces de stationnement non couverts
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OpenParkingYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Estacionamiento Abierto SN
  - **French-Canadian Name:** Stationnement non couvert O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OperatingExpense</code></summary>

  - **Property Types:** RINC , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Gasto Operativo
  - **French-Canadian Name:** Dépenses d’exploitation
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OperatingExpenseIncludes</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto Operativo Incluye
  - **French-Canadian Name:** Compris dans les dépenses d’exploitation
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **BEDES:** Date Status = "Created"Date = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **French-Canadian Name:** Heure et date de l’entrée originale
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginalListPrice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Precio Original de Listado
  - **French-Canadian Name:** Prix initial de l’inscription
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID Sistema de Origen
  - **French-Canadian Name:** ID du système d’origine
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave de Sistema de Origen
  - **French-Canadian Name:** Clé du système d’origine
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **French-Canadian Name:** Nom du système d’origine
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OtherEquipment</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Otro Equipo
  - **French-Canadian Name:** Autres équipements
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OtherExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Otro Gasto
  - **French-Canadian Name:** Autres dépenses
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OtherParking</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Otro Estacionamiento
  - **French-Canadian Name:** Autres espaces de stationnement
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OtherStructures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Otras Estructuras
  - **French-Canadian Name:** Autres structures
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>OwnerName</code></summary>

  - **BEDES:** Contact Label = "Owner"Full Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre del Propietario
  - **French-Canadian Name:** Nom du propriétaire
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OwnerPays</code></summary>

  - **Property Types:** RLSE , RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Pago del Propietario
  - **French-Canadian Name:** Payé par le propriétaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OwnerPhone</code></summary>

  - **BEDES:** Contact Label = "Owner"Telephone Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono del Propietario
  - **French-Canadian Name:** Numéro de téléphone du propriétaire
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Ownership</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Propiedad
  - **French-Canadian Name:** Propriété
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>OwnershipType</code></summary>

  - **BEDES:** Contact Label = "Business"Ownership = [value]
  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Propiedad
  - **French-Canadian Name:** Type de propriété
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ParcelNumber</code></summary>

  - **BEDES:** Identifier Label = "Assessor parcel number"Identifier = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Número de Parcela
  - **French-Canadian Name:** Numéro de parcelle
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ParkManagerName</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Premises Level = 'Site"Contact Label = "Property manager"Contact Name = [value]
  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Nombre Gerente de Parque
  - **French-Canadian Name:** Nom du gestionnaire du parc
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ParkManagerPhone</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Premises Level = 'Site"Contact Label = "Property manager"Telephone Number = [value]
  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Teléfono Gerente de Parque
  - **French-Canadian Name:** Numéro de téléphone du gestionnaire du parc
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ParkName</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Premises Level = 'Site"Identifier Label = "Name"Identifier = [value]
  - **Property Types:** MOBI , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Nombre de Parque
  - **French-Canadian Name:** Nom du parc
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ParkingFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Estacionamiento
  - **French-Canadian Name:** Caractéristiques du stationnement
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ParkingTotal</code></summary>

  - **BEDES:** Interval Measure = "Total"Spatial Unit Type = "Parking space"Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Total de Estacionamiento
  - **French-Canadian Name:** Espaces de stationnement totaux
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PastureArea</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Área de Pasto
  - **French-Canadian Name:** Superficie allouée au pâturage
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PatioAndPorchFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Patio Y Porche
  - **French-Canadian Name:** Caractéristiques du patio/de la véranda
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PendingTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Pendiente
  - **French-Canadian Name:** Heure et date où le statut En attente a été sélectionné
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PestControlExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto Control de Plagas
  - **French-Canadian Name:** Dépenses relatives à la lutte antiparasitaire
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PetsAllowed</code></summary>

  - **Property Types:** RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Se Permiten Mascotas
  - **French-Canadian Name:** Animaux permis
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>PhotosChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Cambio de Fotografías
  - **French-Canadian Name:** Heure et date de la mise à jour des photos
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>PhotosCount</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Conteo de Fotografías
  - **French-Canadian Name:** Nombre de photos
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PoolExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto de Piscina
  - **French-Canadian Name:** Dépenses relatives à la piscine
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PoolFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Piscina
  - **French-Canadian Name:** Caractéristiques de la piscine
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PoolPrivateYN</code></summary>

  - **BEDES:** Water Feature Type = "Pool"
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Piscina Privada SN
  - **French-Canadian Name:** Piscine privée O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Possession</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Posesión
  - **French-Canadian Name:** Prise de possession
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PossibleUse</code></summary>

  - **Property Types:** LAND
  - **Status:** Active
  - **Spanish Name:** Uso Posible
  - **French-Canadian Name:** Utilisation possible
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>PostalCity</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ciudad Postal
  - **French-Canadian Name:** Ville postale
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PostalCode</code></summary>

  - **BEDES:** ZIP Code = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Código Postal
  - **French-Canadian Name:** Code postal
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PostalCodePlus4</code></summary>

  - **BEDES:** ZIP Plus 4 = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Código Postal Más 4
  - **French-Canadian Name:** Code postal +4
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>PowerProduction</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Producción de Energía
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>PowerProductionType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tipo de Producción de Energía
  - **French-Canadian Name:** Type de système production d’énergie
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>PowerProductionYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 1/10/2019
  - **Revision Date:** 1/10/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PreviousListPrice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Precio Anterior de Listado
  - **French-Canadian Name:** Prix antérieur de l’inscription
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PriceChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Cambio de Precio
  - **French-Canadian Name:** Heure et date de la mise à jour du prix de l’inscription
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PrivateOfficeRemarks</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Observaciones de Oficina Privada
  - **French-Canadian Name:** Commentaires privés du bureau
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PrivateRemarks</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Observaciones Privadas
  - **French-Canadian Name:** Commentaires privés
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ProfessionalManagementExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Costo de Administración Profesional
  - **French-Canadian Name:** Dépenses en gestion professionnelle
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PropertyAttachedYN</code></summary>

  - **BEDES:** If (PropertyAttachedYN == true) Vertical Surroundings = "Attached" Else Vertical Surroundings = "Unknown"
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Propiedad Adjunta SN
  - **French-Canadian Name:** Propriété attenante O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PropertyCondition</code></summary>

  - **BEDES:** Identifier Label = "Premises"Condition = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Condición de la Propiedad
  - **French-Canadian Name:** Condition de la propriété
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>PropertySubType</code></summary>

  - **Property Types:** RESI , RLSE , MOBI , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Subtipo de Propiedad
  - **French-Canadian Name:** Sous-type de propriété
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>PropertyTimeZoneName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 3/17/2022
  - **Revision Date:** 10/11/2024
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PropertyTimeZoneObservesDstYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 3/17/2022
  - **Revision Date:** 3/17/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PropertyTimeZoneStandardOffset</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Status Change Date:** 3/17/2022
  - **Revision Date:** 3/17/2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>PropertyType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Propiedad
  - **French-Canadian Name:** Type de propriété
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PublicRemarks</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Observaciones Públicas
  - **French-Canadian Name:** Commentaires publics
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>PublicSurveyRange</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Rango de Estudio de Terreno
  - **French-Canadian Name:** Rangée selon le Public Land Survey System
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PublicSurveySection</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Estudio de Terreno de Sección
  - **French-Canadian Name:** Section selon le Public Land Survey System
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PublicSurveyTownship</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Estudio de Terreno de Municipio
  - **French-Canadian Name:** Comté selon le Public Land Survey System
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>PurchaseContractDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Contrato de Compra
  - **French-Canadian Name:** Date du contrat d’achat
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>RVParkingDimensions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Dimensiones de Estacionamiento de Vehículo Recreativo
  - **French-Canadian Name:** Dimensions de l’espace de stationnement pour VR
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>RangeArea</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Rango de Área
  - **French-Canadian Name:** Superficie de la rangée
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>RentControlYN</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Control de Alquiler SN
  - **French-Canadian Name:** Contrôle des loyers O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>RentIncludes</code></summary>

  - **Property Types:** RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Alquiler Incluye
  - **French-Canadian Name:** Compris dans le loyer
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>RoadFrontageType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Tipo de Fachada Vial
  - **French-Canadian Name:** Type de façade de la route
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>RoadResponsibility</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Responsabilidad Vial
  - **French-Canadian Name:** Responsable de l’entretien de la route
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>RoadSurfaceType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Tipo de Superficie Vial
  - **French-Canadian Name:** Type de surface de la route
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>Roof</code></summary>

  - **BEDES:** Location = "Roof"Finish = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tejado
  - **French-Canadian Name:** Toiture
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>RoomType</code></summary>

  - **BEDES:** Premises Level = "Space" Occupancy Classification = [value]
  - **Property Types:** RESI , RLSE , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Tipo de Habitación
  - **French-Canadian Name:** Type de pièce
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>Rooms</code></summary>

  - **Property Types:** RESI , RLSE , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Habitaciones
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomsTotal</code></summary>

  - **BEDES:** Spatial Unit Type = "Room" Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Total Habitaciones
  - **French-Canadian Name:** Pièces totales
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SeatingCapacity</code></summary>

  - **BEDES:** Occupant Quantity Type = "Capacity"Quantity = [vale]
  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Asientos
  - **French-Canadian Name:** Nombre de places
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SecurityFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Características de Seguridad
  - **French-Canadian Name:** Caractéristiques de la sécurité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SeniorCommunityYN</code></summary>

  - **BEDES:** If (SeniorCommunityYN == true) Occupant Type = "Independent seniors community" Else Occupant Type = "Unknown"
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Comunidad de Tercera Edad SN
  - **French-Canadian Name:** Communauté de personnes âgées O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SerialU</code></summary>

  - **BEDES:** Occupancy Classification = "Manufactured home"Serial Number = [value]
  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Serie U
  - **French-Canadian Name:** Numéro de série U
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SerialX</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Serie X
  - **French-Canadian Name:** Numéro de série X
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SerialXX</code></summary>

  - **Property Types:** RESI , RLSE , MOBI
  - **Status:** Active
  - **Spanish Name:** Serie XX
  - **French-Canadian Name:** Numéro de série XX
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Sewer</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Alcantarillado
  - **French-Canadian Name:** Égout
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>ShowingAdvanceNotice</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Aviso Previo Exhibición
  - **French-Canadian Name:** Préavis relatif à une visite
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ShowingAttendedYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Asistencia Exhibición SN
  - **French-Canadian Name:** Visite supervisée O/N
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ShowingConsiderations</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 8/17/2023
  - **Revision Date:** 8/18/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingContactName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Contacto Exhibición
  - **French-Canadian Name:** Nom du contact pour la visite
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ShowingContactPhone</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Teléfono de Contacto Exhibición
  - **French-Canadian Name:** Numéro de téléphone du contact pour la visite
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ShowingContactPhoneExt</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Ext Telefónica de Contacto Exhibición
  - **French-Canadian Name:** Poste téléphonique du contact pour la visite
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ShowingContactType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Contacto Exhibición
  - **French-Canadian Name:** Type de contact pour la visite
  - **Status Change Date:** 11/19/2013
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ShowingDays</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Días de Exhibición
  - **French-Canadian Name:** Jours de visite
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ShowingEndTime</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Hora de Finalización de Exhibición
  - **French-Canadian Name:** Heure de fin de la visite
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ShowingInstructions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Instrucciones de Exhibición
  - **French-Canadian Name:** Instructions relatives à la visite
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ShowingRequirements</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Requisitos de Exhibición
  - **French-Canadian Name:** Exigences relatives à la visite
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ShowingServiceName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 8/17/2023
  - **Revision Date:** 8/18/2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ShowingStartTime</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Hora de Inicio de Exhibición
  - **French-Canadian Name:** Heure de début de la visite
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>SignOnPropertyYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Propiedad con Letrero SN
  - **French-Canadian Name:** Pancarte sur la propriété O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SimpleDaysOnMarket</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 1/10/2019
  - **Revision Date:** 1/10/2019
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Skirt</code></summary>

  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Rodeo
  - **French-Canadian Name:** Jupe
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SocialMedia</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/22/2022
  - **Revision Date:** 4/4/2023
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/17/2022
  - **Revision Date:** 2/10/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID Sistema Fuente
  - **French-Canadian Name:** ID du système source
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Clave Sistema Fuente
  - **French-Canadian Name:** Clé du système source
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre Sistema Fuente
  - **French-Canadian Name:** Nom du système source
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SpaFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Spa
  - **French-Canadian Name:** Caractéristiques du spa
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SpaYN</code></summary>

  - **BEDES:** Water Feature Type = "Hot tub"
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Spa SN
  - **French-Canadian Name:** Spa O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SpecialLicenses</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Licencias Especiales
  - **French-Canadian Name:** Permis particulier
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SpecialListingConditions</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Condiciones Especiales de Listado
  - **French-Canadian Name:** Conditions particulières
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StandardStatus</code></summary>

  - **BEDES:** Identifier Label = "Listing" Account Status = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Estado Estándar
  - **French-Canadian Name:** Statut standard
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>StartShowingDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Status Change Date:** 5/21/2020
  - **Revision Date:** 5/21/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>StateOrProvince</code></summary>

  - **BEDES:** State = [state code]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Estado o Provincia
  - **French-Canadian Name:** État ou province
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StateRegion</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Estado Región
  - **French-Canadian Name:** Région de l’état
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>StatusChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Cambio de Estado
  - **French-Canadian Name:** Heure et date de la mise à jour du statut
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Stories</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Pisos
  - **French-Canadian Name:** Étages
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StoriesTotal</code></summary>

  - **BEDES:** Spatial Unit Type = "Building" Spatial Unit Type = "Floor" Quantity = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Total Pisos
  - **French-Canadian Name:** Nombre d’étages
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetAdditionalInfo</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Información Adicional de Calle
  - **French-Canadian Name:** Autre information sur la rue
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetDirPrefix</code></summary>

  - **BEDES:** Street Name Pre Directional = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Prefijo Dirección de Calle
  - **French-Canadian Name:** Point cardinal apposé en préfixe
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetDirSuffix</code></summary>

  - **BEDES:** Street Name Post Directional = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo Dirección de Calle
  - **French-Canadian Name:** Point cardinal apposé en suffixe
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetName</code></summary>

  - **BEDES:** Street Name = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Calle
  - **French-Canadian Name:** Nom de la rue
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetNumber</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Calle
  - **French-Canadian Name:** Numéro de la rue
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>StreetNumberNumeric</code></summary>

  - **BEDES:** Address Number = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Calle en Números
  - **French-Canadian Name:** Numéro de la rue en chiffres
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetSuffix</code></summary>

  - **BEDES:** Street Name Post Type = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Sufijo de Calle
  - **French-Canadian Name:** Suffixe de la rue
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StreetSuffixModifier</code></summary>

  - **BEDES:** Street Name Post Modifier = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Modificador de Sufijo de Calle
  - **French-Canadian Name:** Autres suffixes
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>StructureType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Estructura
  - **French-Canadian Name:** Type de structure
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SubAgencyCompensation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Compensación de Subagencia
  - **French-Canadian Name:** Rémunération de l’agence secondaire
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SubAgencyCompensationType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Compensación de Subagencia
  - **French-Canadian Name:** Type de rémunération de l’agence secondaire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SubdivisionName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Subdivisión
  - **French-Canadian Name:** Nom de la sous-division
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SuppliesExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gasto Suministros
  - **French-Canadian Name:** Dépenses en fournitures
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>SyndicateTo</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Redifundir a
  - **French-Canadian Name:** Afficher sur
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SyndicationRemarks</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Observaciones de Redifusión
  - **French-Canadian Name:** Commentaires sur l’affichage
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxAnnualAmount</code></summary>

  - **BEDES:** Tax Annual Amount = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Monto Anual de Impuestos
  - **French-Canadian Name:** Montant annuel des taxes
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxAnnualAmountPerLivingAreaUnit</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 12/17/2020
  - **Revision Date:** 12/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TaxAnnualAmountPerSquareFoot</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Status Change Date:** 12/17/2020
  - **Revision Date:** 12/17/2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>TaxAssessedValue</code></summary>

  - **BEDES:** Tax Annual Amount = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Valor Tasado de Impuestos
  - **French-Canadian Name:** Valeur estimée des taxes
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxBlock</code></summary>

  - **BEDES:** Identifier Label = "Tax block"Identifier = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Bloque de Impuestos
  - **French-Canadian Name:** Taxes foncières - Bloc
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxBookNumber</code></summary>

  - **BEDES:** Identifier Label = "Tax book number"Identifier = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Número de Libro de Impuestos
  - **French-Canadian Name:** Taxes foncières - Numéro dans les livres
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxLegalDescription</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Descripción Legal de Impuestos
  - **French-Canadian Name:** Taxes foncières - Description cadastrale
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxLot</code></summary>

  - **BEDES:** Identifier Label = "Tax lot"Identifier = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Lote de Impuestos
  - **French-Canadian Name:** Taxes foncières - Lot
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxMapNumber</code></summary>

  - **BEDES:** Identifier Label = "Tax map number"Identifier = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Número de Mapa de Impuestos
  - **French-Canadian Name:** Taxes foncières - Numéro sur la carte
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxOtherAnnualAssessmentAmount</code></summary>

  - **BEDES:** Tax Other Assessment Amount = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Otro Monto de Evaluación Anual de Impuestos
  - **French-Canadian Name:** Taxes foncières - Autres évaluations annuelles
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxParcelLetter</code></summary>

  - **BEDES:** Identifier Label = "Tax parcel letter"Identifier = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Carta de Parcela de Impuestos
  - **French-Canadian Name:** Taxes foncières - Lettre de la parcelle
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxStatusCurrent</code></summary>

  - **BEDES:** Tax Status Current = [value]
  - **Property Types:** MOBI
  - **Status:** Active
  - **Spanish Name:** Estado Actual de Impuestos
  - **French-Canadian Name:** Taxes foncières - Statut actuel
  - **Status Change Date:** 8/8/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>TaxTract</code></summary>

  - **BEDES:** Identifier Label = "Tax tract"Identifier = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tracto Fiscal
  - **French-Canadian Name:** Taxes foncières - Lotissement
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TaxYear</code></summary>

  - **BEDES:** Tax Year = [value]
  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Año Fiscal
  - **French-Canadian Name:** Taxes foncières - Année
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TenantPays</code></summary>

  - **Property Types:** RLSE , RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Arrendatario Paga
  - **French-Canadian Name:** Payé par le locataire
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Topography</code></summary>

  - **Property Types:** LAND , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Topografía
  - **French-Canadian Name:** Topographie
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TotalActualRent</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Alquiler Real Total
  - **French-Canadian Name:** Total actuel des loyers
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Township</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Municipio
  - **French-Canadian Name:** Canton
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TransactionBrokerCompensation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Compensación de Corredor de Transacciones
  - **French-Canadian Name:** Rémunération versée au courtier ou agent responsable de la transaction
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TransactionBrokerCompensationType</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tipo de Compensación de Corredor de Transacción
  - **French-Canadian Name:** Type de rémunération versée au courtier ou agent responsable de la transaction
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>TrashExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Gasto Desechos
  - **French-Canadian Name:** Dépenses relatives à la collecte des ordures
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>UnitNumber</code></summary>

  - **BEDES:** Subaddress Type = "Unit"Subaddress Identifier = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Número de Unidad
  - **French-Canadian Name:** Numéro d’unité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>UnitTypeType</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tipo de Unidad
  - **French-Canadian Name:** Type de type d’unité
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>UnitTypes</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tipos de Unidades
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 5/24/2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UnitsFurnished</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Unidades Amuebladas
  - **French-Canadian Name:** Unités meublées
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>UniversalPropertyId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** ID Universal de Propiedad
  - **French-Canadian Name:** Identifiant universel de propriété
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>UniversalPropertySubId</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **French-Canadian Name:** Sous-identifiant universel de propriété
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>UnparsedAddress</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Dirección No Analizada
  - **French-Canadian Name:** Adresse non segmentée
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>Utilities</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Servicios Públicos
  - **French-Canadian Name:** Services publics
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>VacancyAllowance</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Concesión de Vacantes
  - **French-Canadian Name:** Provision pour unités inoccupées
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>VacancyAllowanceRate</code></summary>

  - **Property Types:** COMS , COML
  - **Status:** Active
  - **Spanish Name:** Tasa de Concesión de Vacantes
  - **French-Canadian Name:** Taux de la provision pour unités inoccupées
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Vegetation</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Vegetación
  - **French-Canadian Name:** Végétation
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 3/27/2026

</details>

<details><summary><code>VideosChangeTimestamp</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Cambio de Videos
  - **French-Canadian Name:** Heure et date de la mise à jour de la vidéo
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>VideosCount</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Conteo de Videos
  - **French-Canadian Name:** Nombre de vidéos
  - **Status Change Date:** 4/20/2012
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>View</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Vista
  - **French-Canadian Name:** Vue
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ViewYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Vista SN
  - **French-Canadian Name:** Vue O/N
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>VirtualTourURLBranded</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tour Virtual con URL con Marca
  - **French-Canadian Name:** URL de la visite virtuelle avec marque
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>VirtualTourURLUnbranded</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Tour Virtual con URL sin Marca
  - **French-Canadian Name:** URL de la visite virtuelle sans marque
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>WalkScore</code></summary>

  - **BEDES:** Walking Score = [value]
  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Puntaje Caminatas
  - **French-Canadian Name:** Indice WalkScore
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WaterBodyName</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Nombre de Masa de Agua
  - **French-Canadian Name:** Nom du plan d’eau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WaterSewerExpense</code></summary>

  - **Property Types:** RINC , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Gasto Alcantarillado
  - **French-Canadian Name:** Dépenses relatives à l’eau et aux égouts
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WaterSource</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Fuente de Agua
  - **French-Canadian Name:** Source d’eau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WaterfrontFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Características de Frente Marítimo
  - **French-Canadian Name:** Caractéristiques du bord de l’eau
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>WaterfrontYN</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Frente Marítimo SN
  - **French-Canadian Name:** Bord de l’eau O/N
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WindowFeatures</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Características de Ventana
  - **French-Canadian Name:** Caractéristiques des fenêtres
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WithdrawnDate</code></summary>

  - **Property Types:** RESI , RLSE , RINC , LAND , MOBI , FARM , COMS , COML , BUSO
  - **Status:** Active
  - **Spanish Name:** Fecha de Retiro
  - **French-Canadian Name:** Date de retrait
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 4/4/2023

</details>

<details><summary><code>WoodedArea</code></summary>

  - **Property Types:** FARM
  - **Status:** Active
  - **Spanish Name:** Área de Bosques
  - **French-Canadian Name:** Zone boisée
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>WorkmansCompensationExpense</code></summary>

  - **Property Types:** RINC
  - **Status:** Active
  - **Spanish Name:** Gastos de Seguro de Compensación del Trabajador
  - **French-Canadian Name:** Dépenses d’indemnisation pour accidents du travail
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>YearBuilt</code></summary>

  - **BEDES:** Construction Status = "Completed"Construction Status Date = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Año de Construcción
  - **French-Canadian Name:** Année de construction
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 8/25/2023

</details>

<details><summary><code>YearBuiltDetails</code></summary>

  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Detalles de Año de Construcción
  - **French-Canadian Name:** Détails relatifs à l’année de construction
  - **Status Change Date:** 11/9/2011
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>YearBuiltEffective</code></summary>

  - **BEDES:** Action Category = "Major remodel"Implementation Status = "Completed"Implementation Status Date = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Año de Construcción Efectivo
  - **French-Canadian Name:** Année où la structure a été rebâtie ou rénovée
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>YearBuiltSource</code></summary>

  - **BEDES:** Origin = [value]
  - **Property Types:** RESI , RLSE , RINC , MOBI , FARM
  - **Status:** Active
  - **Spanish Name:** Año de Construcción
  - **French-Canadian Name:** Source de l’année de construction
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>YearEstablished</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Año de Establecimiento
  - **French-Canadian Name:** Année de création de l’entreprise
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>YearsCurrentOwner</code></summary>

  - **Property Types:** BUSO
  - **Status:** Active
  - **Spanish Name:** Años de Posesión Actual
  - **French-Canadian Name:** Nombre d’années en tant que propriétaire
  - **Status Change Date:** 7/3/2014
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>Zoning</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Zonificación
  - **French-Canadian Name:** Zonage
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

<details><summary><code>ZoningDescription</code></summary>

  - **Property Types:** RESI , RINC , LAND , MOBI , FARM , COMS , COML
  - **Status:** Active
  - **Spanish Name:** Descripción de Zonificación
  - **French-Canadian Name:** Description du zonage
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 6/17/2021

</details>

## Lookups

### AccessibilityFeatures

35 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/AccessibilityFeatures/)

| Value | Definition |
|---|---|
| `Accessible Approach with Ramp` | A minimum of one entrance to the structure with a clear, evenly paved walkway from a parking or pedestrian arrival area. |
| `Accessible Bedroom` | Bedroom has adequate turnaround of 60" or other approved turnaround configuration. |
| `Accessible Central Living Area` | Hard surface flooring or low-pile carpet, securely attached along edges. |
| `Accessible Closets` | Closet doors are 32” clearance throughout the central living area. |
| `Accessible Common Area` | Common area, used for entertaining guests, level, with 36" passage through and around the space. |
| `Accessible Doors` | Minimum 32" clear passage; levered handle; threshold, if present, maximum 1/2" but beveled on both sides when over 1/4". |
| `Accessible Electrical and Environmental Controls` | Thermostats and security system controls located on floor with central living area. |
| `Accessible Elevator Installed` | Elevator with minimum 32" door and minimum 36" x 48" turning radius. |
| `Accessible Entrance` | Entrance door is a minimum of 32" wide; threshold, when present, maximum 1/2" but when over 1/4" is beveled on both sides. |
| `Accessible for Hearing-Impairment` | Home is wired for flashing lights and/or vibrating smoke alarm, door bell or other alerting features. |
| `Accessible Full Bath` | Bathroom has adequate turnaround: 60" or other approved turnaround configuration. |
| `Accessible Hallway(s)` | Hallway is a minimum of 36", preferred 42", wide (or adequate alternative based on individual configuration). |
| `Accessible Kitchen` | 40" clear turn-around, or 36" clear with clear under-counter space for T-turn space in kitchen, unimpeded by fixtures. |
| `Accessible Kitchen Appliances` | Stove controls in front or side, at counter top height; oven with side-access door at counter level; microwave is at counter level. |
| `Accessible Stairway` | Handrails on both sides of stairs, extended when possible, with shear force of 250 pounds. |
| `Accessible Washer/Dryer` | Raised clothes washer and/or dryer, front controls, side opening, both open to center. |
| `Adaptable Bathroom Walls` | Reinforced main bathroom walls, including bath or shower, to permit installation of grab bars (with shear force of 250 pounds) and/or fixtures in the future. |
| `Adaptable For Elevator` | Stacked closets in a multistory house for possible future conversion to an elevator. |
| `Ceiling Track` | Track installed in ceiling for lift chair (Hoyer lift). |
| `Central Living Area` | Includes common area; hallway(s); full or three-quarters bathroom; kitchen; at least one bedroom; access to environmental controls; and access to floors above main floor, if necessary. |
| `Common Area` | The portion of the home near accessible entrance, used for entertaining guests. |
| `Customized Wheelchair Accessible` | Customized accessibility for specific size or style of wheelchair or scooter. |
| `Electronic Environmental Controls` | Programmable electronic controls for thermostat, lights, security system and automatic doors. |
| `Enhanced Accessible` | The central living area is fully accessible for lifelong living by all residents, no matter their ability. |
| `Exterior Wheelchair Lift` | A mechanical wheelchair lift is installed outside the home to facilitate barrier-free approach. |
| `Grip-Accessible Features` | All doors, faucets and other mechanisms throughout the central living area are lever, hands-free or another style that can be controlled with a closed hand, clenched fist or weak hands. |
| `Reinforced Floors` | Reinforced floors for bariatric needs, power wheelchairs, therapeutic tub or heavy medical equipment. |
| `Safe Emergency Egress from Home` | A minimum of two, no-step, accessible egresses from central living area. |
| `Smart Technology` | Smart Home (computer-controlled) and/or smart products (e.g., voice-activated controls, voice reminder, remote monitoring of individuals with dementia). |
| `Stair Lift` | A professionally installed motorized rail to climb an interior or exterior stairway. |
| `Standby Generator` | Backup generator for refrigeration of medications, life-sustaining medical equipment or essential room temperature control. |
| `Therapeutic Whirlpool` | Therapeutic whirlpool, properly installed. |
| `Visitable` | A person in a wheelchair can easily enter the home and access the main common area. |
| `Visitor Bathroom` | The bathroom that is closest to the common area, minimum half bath. |
| `Walker-Accessible Stairs` | Treads are minimum 25" deep, with maximum 4" rise and minimum 36" wide. |

### Appliances

75 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Appliances/)

| Value | Definition |
|---|---|
| `Bar Fridge` | A refrigerator that is sized and/or built to be part of a bar. |
| `Built-In Electric Oven` | A built-in electric oven. |
| `Built-In Electric Range` | A built-in electric range. |
| `Built-In Freezer` | A built-in freezer. |
| `Built-In Gas Oven` | A built-in gas oven |
| `Built-In Gas Range` | A built-in gas range. |
| `Built-In Range` | A built-in range where the fuel type is not specified. |
| `Built-In Refrigerator` | A built-in refrigerator |
| `Convection Oven` | An oven that has fans to circulate air around food. |
| `Cooktop` | A kitchen stove or cooker; a kitchen appliance designed for the purpose of cooking food. |
| `Dishwasher` | A dishwasher is a mechanical device for cleaning dishware and cutlery. |
| `Disposal` | A garbage disposal unit (also known as a garbage disposal, waste disposal unit, garbage disposer or garburator (in Canada)) is a device, usually electrically powered, installed under a kitchen sink between the sink's drain and the trap. |
| `Double Oven` | A built-in oven fixture that has either two ovens, or one oven and one microwave oven. |
| `Down Draft` | A vent that is part of the surface of a cooktop that has a fan which sucks cooking fumes/smoke down. |
| `Dryer` | A clothes dryer. |
| `Electric Cooktop` | A cooktop or stove that produces heat by way of electricity rather than gas. |
| `Electric Oven` | An oven that is heated by electricity, typically by way of heating coils. |
| `Electric Range` | An oven and cooktop that generates heat by way of electricity. |
| `Electric Water Heater` | A water heater that heats the water by way of electricity. |
| `ENERGY STAR Qualified Appliances` | The property includes qualified ENERGY STAR appliances. |
| `ENERGY STAR Qualified Dishwasher` | The property includes a qualified ENERGY STAR dishwasher. |
| `ENERGY STAR Qualified Dryer` | The property includes a qualified ENERGY STAR clothes dryer. |
| `ENERGY STAR Qualified Freezer` | The property includes a qualified ENERGY STAR freezer. |
| `ENERGY STAR Qualified Refrigerator` | The property includes a qualified ENERGY STAR refrigerator. |
| `ENERGY STAR Qualified Washer` | The property includes a qualified ENERGY STAR clothes washer. |
| `ENERGY STAR Qualified Water Heater` | The property includes a qualified ENERGY STAR water heater. |
| `Exhaust Fan` | The cooktop has an exhaust fan. |
| `Free-Standing Electric Oven` | The oven is freestanding, not built-in, and uses electricity to produce heat. |
| `Free-Standing Electric Range` | The range is freestanding, not built-in, and uses electricity to produce heat for its oven and cooktop. |
| `Free-Standing Freezer` | The freezer is freestanding and not built-in. |
| `Free-Standing Gas Oven` | The oven is freestanding, not built-in, and uses gas to produce heat. |
| `Free-Standing Gas Range` | The range is freestanding, not built-in, and uses gas to produce heat for its oven and cooktop. |
| `Free-Standing Range` | The range is freestanding, not built-in. |
| `Free-Standing Refrigerator` | The refrigerator is freestanding, not built-in. |
| `Freezer` | The property includes a freezer. |
| `Gas Cooktop` | A cooktop or stove that produces heat by way of gas rather than electricity. |
| `Gas Oven` | An oven that is heated by gas. |
| `Gas Range` | An oven and cooktop that generates heat by way of gas. |
| `Gas Water Heater` | A water heater that heats the water with gas. |
| `Heat Pump Water Heater` | A water heater that uses electricity to move heat from one place to another instead of generating heat directly. |
| `Humidifier` | The property includes a humidity-control device or system. |
| `Ice Maker` | The property includes an ice maker. |
| `Indoor Grill` | The property has an indoor grill. |
| `Induction Cooktop` | The electric cooktop is based on magnetic induction rather than heating coils. |
| `Instant Hot Water` | The property has a circulatory or instant hot water system. |
| `Microwave` | The property includes a microwave. |
| `None` | The property includes no appliances. |
| `Other` | The property includes appliances other than those available on this list. |
| `Oven` | The property includes an oven. |
| `Plumbed For Ice Maker` | The property has plumbing for an ice maker. |
| `Portable Dishwasher` | The property includes a portable dishwasher. |
| `Propane Cooktop` | The gas cooktop uses propane as its fuel and either has a local tank or runs on a housewide propane system. |
| `Range` | The property includes a range, which is a single unit that has both an oven and a cooktop. |
| `Range Hood` | The range has a hooded exhaust. |
| `Refrigerator` | The property includes a refrigerator. |
| `Self Cleaning Oven` | The oven included with the property has a self-cleaning feature. |
| `Smart Appliance(s)` | Appliances that have convenience and energy saving aspects. |
| `Solar Hot Water` | The hot water heater has either a passive or active solar component. |
| `Stainless Steel Appliance(s)` | Some or all of the appliances included in the property are stainless steel. |
| `Tankless Water Heater` | A tankless water heater is included with the property. |
| `Trash Compactor` | The property has a trash compactor. |
| `Vented Exhaust Fan` | The cooktop has an exhaust fan that is vented. |
| `Warming Drawer` | The property has a warming drawer. |
| `Washer` | The property includes a clothes washer. |
| `Washer/Dryer` | The property includes a clothes washer and dryer. |
| `Washer/Dryer Stacked` | The property has a stacked clothes washer and dryer. |
| `Water Heater` | The property has a water heater. |
| `Water Purifier` | The property has a water purifier. |
| `Water Purifier Owned` | The property has a water purifier that is owned and not rented/leased. |
| `Water Purifier Rented` | The property has a water purifier that is on a rental or lease agreement. |
| `Water Softener` | The property has a water-softening system. |
| `Water Softener Owned` | The property has a water-softening system that is owned and not rented/leased. |
| `Water Softener Rented` | The property has a water-softening system that is on a rental or lease agreement. |
| `Wine Cooler` | The property includes a wine cooler. |
| `Wine Refrigerator` | The property includes a wine refrigerator. |

### ArchitecturalStyle

44 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ArchitecturalStyle/)

| Value | Definition |
|---|---|
| `A-Frame` | An architectural style that generally features four walls extending up from the foundation and a steeply pitched roof that reaches near the ground, creating an overall shape of the letter “A” or a tri… |
| `Art Deco` | An architectural style that generally includes decorative windows, spires or other tower-like structures and facades with vertical lines and other ornamental geometric patterns. |
| `Barndominium` | An architectural style that is typically a metal pole barn or other barn-like structure with a living area that encompasses a portion of or the entire building. |
| `Berm` | An architectural style built partially or entirely below grade, with earthen material (i.e., dirt, grass) covering at least one or more walls. |
| `Bungalow` | An architectural style (also known as cottage) that is generally small with a single story or partial second story that has an overhanging, sloped roof and covered porch. |
| `Cabin` | An architectural style that is generally small in size with a simple floor plan and built with mostly natural materials. |
| `Cape Cod` | An architectural style that is generally framed rectangularly, includes one and a half or two stories of height, has a centered front door, and is built with a moderately steeply-pitched, gabled roof. |
| `Colonial` | An architectural style that is generally framed rectangularly, includes two or three stories in height, and is built with a brick, stone or wood facade and steeply-pitched, gabled roof. |
| `Contemporary` | An architectural style that generally includes large windows, natural construction elements, geometric shapes and minimalistic elements. |
| `Craftsman` | An architectural style (also known as arts and crafts) that generally is one or one and a half stories in height, has wood siding or shaker shingles, includes covered porches with exposed beams or columns, and is built with low-pitched, gabled roofs. |
| `Creole` | A prominent architectural style in the Southern United States, particularly the state of Louisiana, that is generally one to one and a half stories in height and includes full front porches and high, gabled roofs with a ridge parallel to the road it fronts. |
| `Dome` | An architectural style (also known as geodesic) that generally takes the shape of a sphere or spherical ellipsoid and has a shell-type framework. |
| `Dutch Colonial` | An architectural style that generally has steep, broken-pitched, gambrel roofs that contain at least one dormer window. |
| `Farmhouse` | An architectural style that is generally one and a half or two stories in height, asymmetrical in design, and built with central chimneys and large porches that sometimes cover multiple sides of the home. |
| `Federal` | An architectural style that is generally square or rectangular, emphasizing balance and symmetry, and has a brick exterior, typically without a porch. |
| `French Provincial` | An architectural style that is generally multi-story with a brick or stucco exterior, slate roof and tall, slender windows. |
| `Georgian` | An architectural style that is generally symmetrical with two or three stories in height and a brick or stone exterior with regularly spaced windows. |
| `Gothic Revival` | An architectural style that generally emphasizes decorative elements, arch designs in windows and doorways, and steeply pitched, pointed and gabled roofs. |
| `Greek Revival` | An architectural style that generally includes a plaster or stucco exterior with tall columns and framed, dormer windows. |
| `Italianate` | An architectural style that is generally two to four stories in height with gently sloping, hipped roofs and tall, narrow or arched windows. |
| `Mediterranean` | An architectural style that generally features a blend of Spanish Revival and Italian Renaissance architecture with stucco exterior, red clay or tile roofs, decorative archways, wrought ironwork in balconies and window grilles, and an incorporation of outdoor living spaces. |
| `Mid-Century Modern` | An architectural style that is generally asymmetrical and split-level or one story in height with large or floor-to-ceiling windows. |
| `Modern` | An architectural style similar to mid-century modern that emphasizes function over form, straight lines and geometric shapes while keeping purely decorative aspects to a minimum. |
| `Monterey` | An architectural style that is generally two stories in height with large porches, full-length balconies, hipped roofs and tall, double-hung windows. |
| `National` | An architectural style that is generally utilitarian, rectangular in shape and built with gabled or pyramidal roofs. |
| `Neoclassical` | An architectural style that generally emphasizes symmetry and often features large columns, decorative doorways and evenly spaced, divided pane windows. |
| `Other` | The architectural style is something other than the options provided. |
| `Prairie` | An architectural style that is generally asymmetrical and emphasizes horizontal lines, handmade woodwork, metalwork and art glass. |
| `Pueblo` | An architectural style (also known as Southwestern or adobe) that is generally constructed of adobe, which may be covered by stucco, with an emphasis on natural, earth-tone materials. |
| `Queen Anne` | An architectural style that is generally asymmetrical with round or polygonal towers or turrets, large wrap-around porches, and steeply pitched, gabled, slate roofs. |
| `Raised Ranch` | An architectural style (also known as bi-level or split foyer) with designed living space below grade that generally have two full levels of living space with a short set of stairs leading up and down from inside the entrance to the home. |
| `Ranch` | An architectural style that is generally one story in height, low to the ground and built with low-pitched roofs and attached, front-facing garages. |
| `Regency` | An architectural style similar to Georgian that is generally two or three stories in height and symmetrical with a painted stucco façade and built with large columns supporting a covered entryway. |
| `Rustic` | An architectural style that is generally built mostly with wood, stone and other natural materials that create a naturally aged and rough look. |
| `Saltbox` | An architectural style originating in New England that is generally two stories in height in the front and one in the rear with a gable roof. |
| `See Remarks` | See remarks for information about the architectural style of the home. |
| `Shingle` | An architectural style that is generally asymmetrical with shingle-covered exteriors, wide porches and steeply pitched roofs. |
| `Shotgun` | An architectural style that is generally one story in height, rectangular, long and narrow with gabled roofs. |
| `Spanish` | An architectural style that is most common in the Southwestern United States and generally has a stucco exterior with liberal use of wood and tile. |
| `Split Level` | An architectural style (also known as trilevel or quad level) that is generally asymmetrical and has facades with minimal decorative elements. |
| `Stick` | An architectural style related to Victorian that is generally asymmetrical with two to three stories of height and a highly decorative shingle or clapboard exterior that may include towers and an emphasis on geometric patterns. |
| `Traditional` | An architectural style that uses several different exterior materials, has simple triangular rooflines, includes regularly spaced and sized windows, and is complemented by large, covered porches. |
| `Tudor` | An architectural style that is generally asymmetrical that has a brick or stone exterior with wood accents and is characterized by steeply pitched, gabled roofs, casement windows and arched doorways. |
| `Victorian` | An architectural style that is generally two to three stories in height with asymmetrical or complex shapes and highly decorative ornamentation such as brackets, spindles and patterned shingles. |

### AreaSource

9 values · used by 8 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/AreaSource/)

| Value | Definition |
|---|---|
| `Appraiser` | An appraiser provided the measurement of the area. |
| `Assessor` | The assessor provided the measurement of the area. |
| `Builder` | The builder provided the measurement of the area. |
| `Estimated` | The measurement of the area is an estimate. |
| `Other` | The measurement of the area was provided by another party not listed. |
| `Owner` | The owner provided the measurement of the area. |
| `Plans` | The measurement of the area was taken from building plans. |
| `Public Records` | The measurement of the area was received from public records. |
| `See Remarks` | See remarks for information about the source of the area measurement. |

### AreaUnits

2 values · used by 9 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/AreaUnits/)

| Value | Definition |
|---|---|
| `Square Feet` | The value reported in the related Area field is in square feet. |
| `Square Meters` | The value reported in the related Area field is in square meters. |

### AssociationAmenities

76 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/AssociationAmenities/)

| Value | Definition |
|---|---|
| `Airport/Runway` | The homeowner association includes access or some service related to an airport or runway. |
| `Barbecue` | The homeowner association includes use of or access to a barbecue. |
| `Basketball Court` | The homeowner association includes use of or access to a basketball court. |
| `Beach Access` | The homeowner association includes access to a beach. |
| `Beach Rights` | The homeowner association includes use of a beach that has beach rights restrictions. |
| `Billiard Room` | The homeowner association includes use of or access to a billiard room. |
| `Boat Dock` | The homeowner association includes use of or access to a boat dock. |
| `Boat Slip` | The homeowner association includes use of or access to a boat slip. |
| `Boating` | The homeowner association includes use of or access to boating. |
| `Cabana` | The homeowner association includes use of or access to a cabana. |
| `Cable TV` | The homeowner association includes cable-based services. |
| `Car Wash Area` | The homeowner association includes use of or access to an area to wash your car. |
| `Clubhouse` | The homeowner association includes use of or access to a clubhouse. |
| `Coin Laundry` | The homeowner association includes use of or access to a coin laundry. |
| `Concierge` | The homeowner association includes use of or access to a concierge service. |
| `Day Care` | The homeowner association includes use of or access to a day care service. |
| `Dog Park` | The homeowner association includes use of or access to a dog park. |
| `Dry Dock` | The homeowner association includes use of or access to a dry dock. |
| `Electricity` | The homeowner association includes electricity. |
| `Elevator(s)` | The homeowner association includes use of or access to an elevator or elevators. |
| `Exercise Course` | The homeowner association includes use of or access to an exercise course. |
| `Fitness Center` | The homeowner association includes use of or access to a fitness center. |
| `Game Court Exterior` | The homeowner association includes use of or access to an outdoors game court. |
| `Game Court Interior` | The homeowner association includes use of or access to an indoors game court. |
| `Game Room` | The homeowner association includes use of or access to a game room. |
| `Gas` | The homeowner association includes natural gas. |
| `Gated` | The homeowner association property/area is gated. |
| `Golf Course` | The homeowner association includes use of or access to a golf course. |
| `Hot Water` | The homeowner association includes hot water. |
| `Indoor Pool` | The homeowner association includes use of or access to an indoor pool. |
| `Insurance` | The homeowner association includes insurance. |
| `Jogging Path` | The homeowner association includes use of or access to a jogging path. |
| `Landscaping` | The homeowner association includes landscaping. |
| `Laundry` | The homeowner association includes laundry. |
| `Maid service` | The homeowner association includes use of or access to a maid service. |
| `Maintenance` | The homeowner association includes maintenance. |
| `Maintenance Grounds` | The homeowner association includes grounds maintenance. |
| `Maintenance Structure` | The homeowner association includes building maintenance. |
| `Management` | The homeowner association includes management services. |
| `Marina` | The homeowner association includes use of or access to a marina. |
| `Meeting Room` | The homeowner association includes use of or access to a meeting room. |
| `None` | The homeowner association has no amenities. |
| `Other` | The homeowner association includes amenities not included on this list. |
| `Park` | The homeowner association includes use of or access to a park. |
| `Parking` | The homeowner association includes use of or access to parking. |
| `Party Room` | The homeowner association includes use of or access to a party room. |
| `Picnic Area` | The homeowner association includes use of or access to a picnic area. |
| `Playground` | The homeowner association includes use of or access to a playground. |
| `Pond Seasonal` | The homeowner association includes seasonal use of or access to a pond. |
| `Pond Year Round` | The homeowner association includes use of or access to a pond all year long. |
| `Pool` | The homeowner association includes use of or access to a pool. |
| `Powered Boats Allowed` | The homeowner association allows the use of powered boats. |
| `Racquetball` | The homeowner association includes use of or access to a racquetball court or courts. |
| `Recreation Facilities` | The homeowner association includes use of or access to recreation facilities. |
| `Recreation Room` | The homeowner association includes use of or access to a recreation room. |
| `Roof Deck` | The homeowner association includes use of or access to a roof deck. |
| `RV Parking` | The homeowner association includes use of or access to recreational vehicle (RV) parking. |
| `RV/Boat Storage` | The homeowner association includes use of or access to recreational vehicle (RV) and/or boat storage. |
| `Sauna` | The homeowner association includes use of or access to a sauna. |
| `Security` | The homeowner association includes security services. |
| `Service Elevator(s)` | The homeowner association includes use of or access to a service elevator or elevators. |
| `Shuffleboard Court` | The homeowner association includes use of or access to a shuffleboard court. |
| `Ski Accessible` | The homeowner association includes access to skiing. |
| `Snow Removal` | The homeowner association includes snow removal. |
| `Spa/Hot Tub` | The homeowner association includes use of or access to a spa and/or hot tub. |
| `Sport Court` | The homeowner association includes use of or access to a sport court. |
| `Stable(s)` | The homeowner association includes use of or access to a horse stable. |
| `Storage` | The homeowner association includes storage space. |
| `Stream Seasonal` | The homeowner association includes seasonal use of or access to a stream. |
| `Stream Year Round` | The homeowner association includes use of or access to a stream all year long. |
| `Taxes` | The homeowner association includes taxes. |
| `Tennis Court(s)` | The homeowner association includes use of or access to a tennis court. |
| `Trail(s)` | The homeowner association includes use of or access to a trail. |
| `Trash` | The homeowner association includes trash service. |
| `Water` | The homeowner association includes water. |
| `Workshop Area` | The homeowner association includes use of or access to a workshop area. |

### AssociationFeeIncludes

15 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/AssociationFeeIncludes/)

| Value | Definition |
|---|---|
| `Cable TV` | Cable TV is included in the fee paid to the homeowner association. |
| `Earthquake Insurance` | Earthquake insurance is included in the fee paid to the homeowner association. |
| `Electricity` | Electricity is included in the fee paid to the homeowner association. |
| `Gas` | Gas is included in the fee paid to the homeowner association. |
| `Insurance` | Insurance is included in the fee paid to the homeowner association. |
| `Internet` | Internet access is included with the homeowner association dues paid by the owner. |
| `Maintenance Grounds` | Maintenance of the grounds includes lawns and common areas but not exterior structures. |
| `Maintenance Structure` | Maintenance of the exterior of the structure includes roofing, walls, exterior structures but does not include the grounds. |
| `Pest Control` | Pest control is included in the fee paid to the association. |
| `Security` | Security is included in the fee paid to the association. |
| `Sewer` | Sewer is included in the fee paid to the association. |
| `Snow Removal` | Snow removal is included in the fee paid to the association. |
| `Trash` | Trash is included in the fee paid to the association. |
| `Utilities` | Utilities are included in the fee paid to the association. |
| `Water` | Water is included in the fee paid to the association. |

### Basement

24 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Basement/)

| Value | Definition |
|---|---|
| `Apartment` | The basement is set up as an apartment living space. |
| `Bath/Stubbed` | The basement is stubbed for a bathroom. |
| `Block` | The basement has block construction. |
| `Concrete` | The basement has a concrete floor and/or walls. |
| `Crawl Space` | The basement is/has a crawl space. |
| `Daylight` | The basement has natural lighting. |
| `Dirt Floor` | The basement has a dirt floor. |
| `Exterior Entry` | The basement has an exterior entry. |
| `Finished` | The basement is finished to a given standard of completion (e.g., underlayment and flooring; walls framed, insulated, drywalled and painted). |
| `French Drain` | The basement has a French drain. |
| `Full` | The basement fills the entire space under the house. |
| `Full Exposure` | The basement of the home has a full-wall, standard-sized windows and a door to the outside at or above ground level. |
| `Interior Entry` | The basement has an interior entry. |
| `No Exposure` | The basement of the home is below ground without full-sized windows or a door to the outside. |
| `None` | The property has no basement. |
| `Other` | The basement has features or attributes other than those listed in this field. |
| `Partial` | The basement partially fills the space under the house. |
| `Partial Exposure` | The basement of the home is roughly halfway below ground level and has at least one full-sized window but without a door to the outside. |
| `Partially Finished` | The basement is partially finished. |
| `Storage Space` | The basement has storage space. |
| `Sump Pump` | The basement has a sump pump. |
| `Unfinished` | The basement is unfinished. |
| `Walk-Out Access` | A structure where the basement space is directly accessible from the outside with the entryway level with the ground. |
| `Walk-Up Access` | A structure where the basement space is directly accessible from the outside with the entryway below ground and usually exterior stairs leading up to the ground level. |

### BodyType

7 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/BodyType/)

| Value | Definition |
|---|---|
| `Double Wide` | The body/structure type of the mobile/manufacture home is a double-wide. |
| `Expando` | The body/structure type of the mobile/manufacture home is an expando. |
| `Other` | A body type is not included on this list. |
| `Quad Wide` | The body/structure type of the mobile/manufacture home is a quad. |
| `See Remarks` | The body/structure type of the mobile/manufacture home is described by additional remarks. |
| `Single Wide` | The body/structure type of the mobile/manufacture home is a single-wide. |
| `Triple Wide` | The body/structure type of the mobile/manufacture home is a triple-wide. |

### BusinessType

109 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/BusinessType/)

| Value | Definition |
|---|---|
| `Accounting` | The listing is for an accounting business. |
| `Administrative and Support` | The listing is for an administrative and support business. |
| `Advertising` | The listing is for an advertising business. |
| `Agriculture` | The listing is for an agriculture business. |
| `Animal Grooming` | The listing is for an animal grooming business. |
| `Appliances` | The listing is for an appliances business. |
| `Aquarium Supplies` | The listing is for an aquarium supplies business. |
| `Arts and Entertainment` | The listing is for an arts and entertainment business. |
| `Athletic` | The listing is for an athletic business. |
| `Auto Body` | The listing is for an auto body business. |
| `Auto Dealer` | The listing is for an auto dealer business. |
| `Auto Glass` | The listing is for an auto glass business. |
| `Auto Parts` | The listing is for an auto parts business. |
| `Auto Rent/Lease` | The listing is for an auto rent/lease business. |
| `Auto Repair-Specialty` | The listing is for an auto repair specialty business. |
| `Auto Service` | The listing is for an auto service business. |
| `Auto Stereo/Alarm` | The listing is for an auto stereo/alarm business. |
| `Auto Tires` | The listing is for an auto tires business. |
| `Auto Wrecking` | The listing is for an auto wrecking business. |
| `Bakery` | The listing is for a bakery business. |
| `Bar/Tavern/Lounge` | The listing is for a bar/tavern/lounge business. |
| `Barber/Beauty` | The listing is for a barber/beauty business. |
| `Bed & Breakfast` | The listing is for a bed & breakfast business. |
| `Books/Cards/Stationary` | The listing is for a books/cards/stationary business. |
| `Butcher` | The listing is for a butcher business. |
| `Cabinets` | The listing is for a cabinets business. |
| `Candy/Cookie` | The listing is for a candy/cookie business. |
| `Car Wash` | The listing is for a car wash business. |
| `Carpet/Tile` | The listing is for a carpet/tile business. |
| `Child Care` | The listing is for a child care business. |
| `Church` | The listing is for a church business. |
| `Clothing` | The listing is for a clothing business. |
| `Commercial` | The listing is for a commercial business. |
| `Computer` | The listing is for a computer business. |
| `Construction/Contractor` | The listing is for a construction/contractor business. |
| `Convalescent` | The listing is for a convalescent business. |
| `Convenience Store` | The listing is for a convenience store business. |
| `Dance Studio` | The listing is for a dance studio business. |
| `Decorator` | The listing is for a decorator business. |
| `Deli/Catering` | The listing is for a deli/catering business. |
| `Dental` | The listing is for a dental business. |
| `Distribution` | The listing is for a distribution business. |
| `Doughnut` | The listing is for a doughnut business. |
| `Drugstore` | The listing is for a drugstore business. |
| `Dry Cleaner` | The listing is for a dry cleaner business. |
| `Education/School` | The listing is for an education/school business. |
| `Electronics` | The listing is for an electronics business. |
| `Employment` | The listing is for an employment business. |
| `Farm` | The listing is for a farm business. |
| `Fast Food` | The listing is for a fast food business. |
| `Financial` | The listing is for a financial business. |
| `Fitness` | The listing is for a fitness business. |
| `Florist/Nursery` | The listing is for a florist/nursery business. |
| `Food & Beverage` | The listing is for a food & beverage business. |
| `Forest Reserve` | The listing is for a forest reserve business. |
| `Franchise` | The listing is for a franchise business. |
| `Furniture` | The listing is for a furniture business. |
| `Gas Station` | The listing is for a gas station business. |
| `Gift Shop` | The listing is for a gift shop business. |
| `Grocery` | The listing is for a grocery business. |
| `Hardware` | The listing is for a hardware business. |
| `Health Food` | The listing is for a health food business. |
| `Health Services` | The listing is for a health services business. |
| `Hobby` | The listing is for a hobby business. |
| `Home Cleaner` | The listing is for a home cleaner business. |
| `Hospitality` | The listing is for a hospitality business. |
| `Hotel/Motel` | The listing is for a hotel/motel business. |
| `Ice Cream/Frozen Yogurt` | The listing is for an ice cream/frozen yogurt business. |
| `Industrial` | The listing is for an industrial business. |
| `Jewelry` | The listing is for a jewelry business. |
| `Landscaping` | The listing is for a landscaping business. |
| `Laundromat` | The listing is for a laundromat business. |
| `Liquor Store` | The listing is for a liquor store business. |
| `Locksmith` | The listing is for a locksmith business. |
| `Manufacturing` | The listing is for a manufacturing business. |
| `Medical` | The listing is for a medical business. |
| `Mixed` | The listing is for a mixed business. |
| `Mobile/Trailer Park` | The listing is for a mobile/trailer park business. |
| `Music` | The listing is for a music business. |
| `Nursing Home` | The listing is for a nursing home business. |
| `Office Supply` | The listing is for an office supply business. |
| `Other` | The listing is for a business not readily categorized into another business type. |
| `Paints` | The listing is for a paint business. |
| `Parking` | The listing is for a parking business. |
| `Pet Store` | The listing is for a pet store business. |
| `Photographer` | The listing is for a photography business. |
| `Pizza` | The listing is for a pizza business. |
| `Printing` | The listing is for a printing business. |
| `Professional Service` | The listing is for a professional service business. |
| `Professional/Office` | The listing is for a professional/office business. |
| `Real Estate` | The listing is for a real estate business. |
| `Recreation` | The listing is for a recreation business. |
| `Rental` | The listing is for a rental business. |
| `Residential` | The listing is for a residential business. |
| `Restaurant` | The listing is for a restaurant business. |
| `Retail` | The listing is for a retail business. |
| `Saddlery/Harness` | The listing is for a saddlery/harness business. |
| `Sporting Goods` | The listing is for a sporting goods business. |
| `Storage` | The listing is for a storage business. |
| `Toys` | The listing is for a toy business. |
| `Transportation` | The listing is for a transportation business. |
| `Travel` | The listing is for a travel business. |
| `Upholstery` | The listing is for an upholstery business. |
| `Utility` | The listing is for a utility business. |
| `Variety` | The listing is for a variety business. |
| `Video` | The listing is for a video business. |
| `Wallpaper` | The listing is for a wallpaper business. |
| `Warehouse` | The listing is for a warehouse business. |
| `Wholesale` | The listing is for a wholesale business. |

### BuyerAgentDesignation

27 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/BuyerAgentDesignation/)

| Value | Definition |
|---|---|
| `Accredited Buyer's Representative / ABR` | The Accredited Buyer’s Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| `Accredited Land Consultant / ALC` | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| `At Home With Diversity / AHWD` | Learn to work effectively with and within today’s diverse real estate market. |
| `Certified Commercial Investment Member / CCIM` | The Certified Commercial Investment Member (CCIM) designation is commercial real estate’s global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| `Certified Distressed Property Expert / CDPE` | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today’s turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| `Certified International Property Specialist / CIPS` | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| `Certified Property Manager / CPM` | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| `Certified Real Estate Brokerage Manager / CRB` | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| `Certified Real Estate Team Specialist / C-RETS` | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| `Certified Residential Specialist / CRS` | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| `Counselor of Real Estate / CRE` | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| `e-PRO` | NAR's e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |
| `General Accredited Appraiser / GAA` | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Graduate, REALTOR Institute / GRI` | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| `Military Relocation Professional / MRP` | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| `NAR's Green Designation / GREEN` | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| `Performance Management Network / PMN` | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| `Pricing Strategy Advisor / PSA` | Enhance your skills in pricing properties, creating CMAs (comparative market analyses), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| `Real Estate Negotiation Expert / RENE` | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| `REALTOR Association Certified Executive / RCE` | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| `Residential Accredited Appraiser / RAA` | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Resort & Second-Home Property Specialist / RSPS` | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| `Seller Representative Specialist / SRS` | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| `Seniors Real Estate Specialist / SRES` | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| `Short Sales & Foreclosure Resource / SFR` | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| `Society of Industrial and Office REALTORS / SIOR` | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| `Transnational Referral Certification / TRC` | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |

### BuyerFinancing

13 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/BuyerFinancing/)

| Value | Definition |
|---|---|
| `Assumed` | The buyer assumed a current form of financing. |
| `Cash` | The buyer paid cash for the property. |
| `Contract` | The purchase of a property involves an agreement to perform services, provide product, share income or some other determined method of payment for the property. |
| `Conventional` | The buyer is using conventional financing to purchase the home. |
| `FHA` | A loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `FHA 203(b)` | The basic home mortgage loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `FHA 203(k)` | A loan for the rehabilitation and repair of a single-family residence from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `Other` | The buyer is using another form of financing that is not included among the options provided on this list. |
| `Private` | Financing is provided by a private party. |
| `Seller Financing` | The seller is providing financing to the buyer. |
| `Trust Deed` | Financing where title of the property is placed with a trustee who secures payment of the loan for a beneficiary. |
| `USDA` | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| `VA` | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

### ChangeType

13 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ChangeType/)

| Value | Definition |
|---|---|
| `Active` | The change to the listing was a change of status to Active. |
| `Active Under Contract` | The change to the listing was a change of status to Active Under Contract. |
| `Back On Market` | The change to the listing was a change of status to Back On Market. |
| `Canceled` | The change to the listing was a change of status to Canceled. |
| `Closed` | The change to the listing was a change of status to Closed. |
| `Coming Soon` | The change to the listing was a change of status to Coming Soon. |
| `Deleted` | The change to the listing was a change of status to Deleted. |
| `Expired` | The change to the listing was a change of status to Expired. |
| `Hold` | The change to the listing was a change of status to Hold. |
| `New Listing` | The listing is new and hasn't had any status or price changes since its original input. |
| `Pending` | The change to the listing was a change of status to Pending. |
| `Price Change` | The change to the listing was a change to the ListPrice. |
| `Withdrawn` | The change to the listing was a change of status to Withdrawn. |

### CoBuyerAgentDesignation

27 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CoBuyerAgentDesignation/)

| Value | Definition |
|---|---|
| `Accredited Buyer's Representative / ABR` | The Accredited Buyer’s Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| `Accredited Land Consultant / ALC` | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| `At Home With Diversity / AHWD` | Learn to work effectively with and within today’s diverse real estate market. |
| `Certified Commercial Investment Member / CCIM` | The Certified Commercial Investment Member (CCIM) designation is commercial real estate’s global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| `Certified Distressed Property Expert / CDPE` | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today’s turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| `Certified International Property Specialist / CIPS` | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| `Certified Property Manager / CPM` | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| `Certified Real Estate Brokerage Manager / CRB` | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| `Certified Real Estate Team Specialist / C-RETS` | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| `Certified Residential Specialist / CRS` | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| `Counselor of Real Estate / CRE` | The Counselors of Real Estate® is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| `e-PRO` | NAR's e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |
| `General Accredited Appraiser / GAA` | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Graduate, REALTOR Institute / GRI` | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| `Military Relocation Professional / MRP` | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| `NAR's Green Designation / GREEN` | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| `Performance Management Network / PMN` | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| `Pricing Strategy Advisor / PSA` | Enhance your skills in pricing properties, creating CMAs (comparative market analyses), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| `Real Estate Negotiation Expert / RENE` | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| `REALTOR Association Certified Executive / RCE` | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| `Residential Accredited Appraiser / RAA` | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Resort & Second-Home Property Specialist / RSPS` | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| `Seller Representative Specialist / SRS` | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| `Seniors Real Estate Specialist / SRES` | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| `Short Sales & Foreclosure Resource / SFR` | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| `Society of Industrial and Office REALTORS / SIOR` | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| `Transnational Referral Certification / TRC` | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |

### CoListAgentDesignation

27 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CoListAgentDesignation/)

| Value | Definition |
|---|---|
| `Accredited Buyer's Representative / ABR` | The Accredited Buyer’s Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| `Accredited Land Consultant / ALC` | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| `At Home With Diversity / AHWD` | Learn to work effectively with and within today’s diverse real estate market. |
| `Certified Commercial Investment Member / CCIM` | The Certified Commercial Investment Member (CCIM) designation is commercial real estate’s global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| `Certified Distressed Property Expert / CDPE` | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today’s turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| `Certified International Property Specialist / CIPS` | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| `Certified Property Manager / CPM` | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| `Certified Real Estate Brokerage Manager / CRB` | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| `Certified Real Estate Team Specialist / C-RETS` | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| `Certified Residential Specialist / CRS` | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| `Counselor of Real Estate / CRE` | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| `e-PRO` | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |
| `General Accredited Appraiser / GAA` | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Graduate, REALTOR Institute / GRI` | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| `Military Relocation Professional / MRP` | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| `NAR's Green Designation / GREEN` | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| `Performance Management Network / PMN` | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| `Pricing Strategy Advisor / PSA` | Enhance your skills in pricing properties, creating CMAs (comparative market analyses), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| `Real Estate Negotiation Expert / RENE` | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| `REALTOR Association Certified Executive / RCE` | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| `Residential Accredited Appraiser / RAA` | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Resort & Second-Home Property Specialist / RSPS` | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| `Seller Representative Specialist / SRS` | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| `Seniors Real Estate Specialist / SRES` | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| `Short Sales & Foreclosure Resource / SFR` | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| `Society of Industrial and Office REALTORS / SIOR` | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| `Transnational Referral Certification / TRC` | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |

### CommonInterest

6 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CommonInterest/)

| Value | Definition |
|---|---|
| `Community Apartment` | Ownership interest where purchaser receives a partial/fractional interest in the land coupled with the right of exclusive occupancy of an apartment located thereon. |
| `Condominium` | Ownership of an individual unit where each homeowner only owns their individual unit space and an undivided share in the ownership of common areas or in a common homeowner association (HOA). |
| `None` | Ownership of an entire parcel or lot that is not in a common-interest development (CID) or not held subject to any other common interest rights. |
| `Planned Development` | Ownership consisting of an individual lot or parcel, generally including the ownership of the land and any structures on the individual lot or parcel. |
| `Stock Cooperative` | Ownership of an interest in a corporation which is formed primarily for the purpose of holding title to improved real property, either in fee simple or for a term of years. |
| `Timeshare` | Ownership in a time period or a point system granting possession rights to a unit or occupancy rights at a property. |

### CommonWalls

6 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CommonWalls/)

| Value | Definition |
|---|---|
| `1 Common Wall` | The dwelling being sold has one common wall with another property that is not part of the sale. |
| `2+ Common Walls` | The dwelling being sold has two or more common walls with another property that is not part of the sale. |
| `End Unit` | The dwelling being sold has one or more common walls with another property that is not part of the sale and is at the end of a row of units. |
| `No Common Walls` | The dwelling being sold has no attached structures that are not part of the sale. |
| `No One Above` | The property is attached to another dwelling that is not part of the sale, but there is no unit above the one being sold. |
| `No One Below` | The property is attached to another dwelling that is not part of the sale, but there is no unit below the one being sold. |

### CommunityFeatures

21 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CommunityFeatures/)

| Value | Definition |
|---|---|
| `Airport/Runway` | The community has an airport or runway. |
| `Clubhouse` | The community has a clubhouse. |
| `Curbs` | The community streets have curbs. |
| `Fishing` | The community has places to go fishing. |
| `Fitness Center` | The community has a fitness center. |
| `Gated` | The community is gated. |
| `Golf` | The community has golfing. |
| `Lake` | The community has a lake. |
| `None` | The community includes no additional features. |
| `Other` | The community has features beyond those listed in this field. |
| `Park` | The community has a park. |
| `Pickleball` | The community has a pickleball court. |
| `Playground` | The community has a playground. |
| `Pool` | The community has a pool. |
| `Racquetball` | The community has racquetball facilities. |
| `Restaurant` | The community has a restaurant. |
| `Sidewalks` | The community streets have sidewalks. |
| `Stable(s)` | The community has one or more horse stables. |
| `Street Lights` | The community streets have lighting. |
| `Suburban` | The community is a suburban setting. |
| `Tennis Court(s)` | The community has one or more tennis courts. |

### CompensationType

4 values · used by 3 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CompensationType/)

| Value | Definition |
|---|---|
| `$` | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) as a dollar amount of the gross compensation. |
| `%` | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) as a percentage of the gross compensation. |
| `Other` | A compensation type not included on this list. |
| `See Remarks` | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) is something other than % or $ or is a special combination of $, % and other compensation types. |

### Concessions

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Concessions/)

| Value | Definition |
|---|---|
| `Call Listing Agent` | Call the listing agent for information about concessions made/offered by the seller. |
| `No` | There are no concessions included with this listing. |
| `Yes` | There are concessions that are part of the listing/sale. |

### ConstructionMaterials

54 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ConstructionMaterials/)

| Value | Definition |
|---|---|
| `Adobe` | The structure was made wholly or partly with adobe. |
| `Aluminum Siding` | The structure was made wholly or partly with aluminum siding. |
| `Asbestos` | The structure includes asbestos as a construction material. |
| `Asphalt` | The structure was made wholly or partly with asphalt. |
| `Attic/Crawl Hatchway(s) Insulated` | When not insulated, a home’s attic hatch or crawlspace hatch creates one of the biggest gaps in the building envelope, increasing heat loss in winter and heat gain in summer, while making indoor living areas uncomfortable. |
| `Batts Insulation` | Rolls and batts, or blankets, are flexible products made from mineral fibers such as fiberglass, rock wool, cotton or wool. |
| `Block` | The structure was made wholly or partly with block. |
| `Blown-In Insulation` | Blown-in or loose-fill insulation is usually made of fiberglass, rock wool or cellulose in the form of loose fibers or fiber pellets installed using special pneumatic equipment. |
| `Board & Batten Siding` | The structure was made wholly or partly with board & batten siding. |
| `Brick` | The structure was made wholly or partly with brick. |
| `Brick Veneer` | The structure was made wholly or partly with brick veneer. |
| `Cedar` | The structure was made wholly or partly with cedar. |
| `Cement Siding` | The structure was made wholly or partly with cement siding. |
| `Clapboard` | The structure was made wholly or partly with clapboard. |
| `Concrete` | The structure was made wholly or partly with concrete. |
| `Ducts Professionally Air-Sealed` | The structure was made wholly or partly with ducts professionally air-sealed. |
| `Exterior Duct-Work is Insulated` | U.S. |
| `Fiber Cement` | The structure was made wholly or partly with fiber cement. |
| `Fiberglass Siding` | The structure was made wholly or partly with fiberglass siding. |
| `Foam Insulation` | Spray foam or foam-in-place insulation can be sprayed into walls, on attic surfaces, or under floors to insulate and reduce air leakage. |
| `Frame` | The structure includes a frame. |
| `Glass` | The structure was made wholly or partly with glass. |
| `HardiPlank Type` | The structure includes HardiPlank® siding as a construction material. |
| `ICAT Recessed Lighting` | ICAT (Insulation Contact Air Tight) recessed light fixtures are rated both to safely come in contact with insulation and are better airsealed. |
| `ICFs (Insulated Concrete Forms)` | The structure was made wholly or partly with insulated concrete forms. |
| `Lap Siding` | The structure was made wholly or partly with lap siding. |
| `Log` | The structure was made wholly or partly with log. |
| `Log Siding` | The structure was made wholly or partly with log siding. |
| `Low VOC Insulation` | Volatile organic compounds (VOCs) are emitted as gases from certain solids or liquids. |
| `Masonite` | The structure was made wholly or partly with Masonite. |
| `Metal Siding` | The structure was made wholly or partly with metal siding. |
| `Natural Building` | The structure was made wholly or partly with natural building. |
| `Other` | The structure was made wholly or partly with other construction materials. |
| `Plaster` | The structure was made wholly or partly with plaster. |
| `Radiant Barrier` | The structure was made wholly or partly with radiant barrier. |
| `Rammed Earth` | The structure was made wholly or partly with rammed earth. |
| `Recycled/Bio-Based Insulation` | Insulation can be made from natural or recycled materials ranging from paper to soy to denim, using sustainable materials to improve energy efficiency. |
| `Redwood Siding` | The structure was made wholly or partly with redwood siding. |
| `See Remarks` | See remarks for more information about what the structure was wholly or partly made of. |
| `Shake Siding` | The structure was made wholly or partly with shake siding. |
| `Shingle Siding` | The structure was made wholly or partly with shingle siding. |
| `Slump Block` | The structure was made wholly or partly with slump block. |
| `Spray Foam Insulation` | The structure was made wholly or partly with spray foam insulation. |
| `Steel Frame` | The framing of the structure is made of cold-formed steel (CFS). |
| `Steel Siding` | The structure was made wholly or partly with steel siding. |
| `Stone` | The structure was made wholly or partly with stone. |
| `Stone Veneer` | The structure was made wholly or partly with stone veneer. |
| `Straw` | The structure was made wholly or partly with straw. |
| `Stucco` | The structure was made wholly or partly with stucco. |
| `Synthetic Stucco` | The structure was made wholly or partly with synthetic stucco. |
| `Unknown` | It is unknown what the structure was wholly or partly made of. |
| `Vertical Siding` | The structure was made wholly or partly with vertical siding. |
| `Vinyl Siding` | The structure was made wholly or partly with vinyl siding. |
| `Wood Siding` | The structure was made wholly or partly with wood siding. |

### Cooling

24 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Cooling/)

| Value | Definition |
|---|---|
| `Attic Fan` | The property has an attic fan. |
| `Ceiling Fan(s)` | The property has one or more ceiling fans. |
| `Central Air` | The property has central air conditioning. |
| `Dual` | The cooling system has two units. |
| `Ductless` | The cooling system does not have ducted or a wall/window-type unit. |
| `Electric` | The cooling system is powered by electricity. |
| `ENERGY STAR Qualified Equipment` | The cooling system is qualified as ENERGY STAR. |
| `Evaporative Cooling` | The cooling system works by way of water evaporation rather than a compressor and coolant. |
| `Exhaust Fan` | The structure has an exhaust fan. |
| `Gas` | The cooling system is powered by gas. |
| `Geothermal` | The cooling system runs on a geothermal source. |
| `Heat Pump` | A system that exchanges heat between a warm and cool space. |
| `Humidity Control` | The cooling system includes humidity control. |
| `Multi Units` | The cooling system includes more than one unit. |
| `None` | The property includes no cooling system. |
| `Other` | The cooling system is different or has features that are not included on this list. |
| `Roof Turbine(s)` | The cooling system utilizes a roof turbine. |
| `Separate Meters` | The cooling system has separate meters for its multiple units/zones. |
| `Varies by Unit` | The cooling equipment varies by unit. |
| `Wall Unit(s)` | The cooling system is stand alone and mounted in an opening in an outer wall. |
| `Wall/Window Unit(s)` | The cooling system is mounted in an opening in the wall or in a window. |
| `Whole House Fan` | The property has a whole house fan. |
| `Window Unit(s)` | The cooling system is window mounted. |
| `Zoned` | The cooling system has more than one zone. |

### Country

246 values · used by 12 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Country/)

| Value | Definition |
|---|---|
| `AD` | Andorra is the country in which the individual, entity or property is located. |
| `AE` | United Arab Emirates is the country in which the individual, entity or property is located. |
| `AF` | Afghanistan is the country in which the individual, entity or property is located. |
| `AG` | Antigua Barbuda is the country in which the individual, entity or property is located. |
| `AI` | Anguilla is the country in which the individual, entity or property is located. |
| `AL` | Albania is the country in which the individual, entity or property is located. |
| `AM` | Armenia is the country in which the individual, entity or property is located. |
| `AN` | Netherlands Antilles is the country in which the individual, entity or property is located. |
| `AO` | Angola is the country in which the individual, entity or property is located. |
| `AQ` | Antarctica is the country in which the individual, entity or property is located. |
| `AR` | Argentina is the country in which the individual, entity or property is located. |
| `AS` | American Samoa is the country in which the individual, entity or property is located. |
| `AT` | Austria is the country in which the individual, entity or property is located. |
| `AU` | Australia is the country in which the individual, entity or property is located. |
| `AW` | Aruba is the country in which the individual, entity or property is located. |
| `AX` | Aland Islands is the country in which the individual, entity or property is located. |
| `AZ` | Azerbaijan is the country in which the individual, entity or property is located. |
| `BA` | Bosnia Herzegovina is the country in which the individual, entity or property is located. |
| `BB` | Barbados is the country in which the individual, entity or property is located. |
| `BD` | Bangladesh is the country in which the individual, entity or property is located. |
| `BE` | Belgium is the country in which the individual, entity or property is located. |
| `BF` | Burkina Faso is the country in which the individual, entity or property is located. |
| `BG` | Bulgaria is the country in which the individual, entity or property is located. |
| `BH` | Bahrain is the country in which the individual, entity or property is located. |
| `BI` | Burundi is the country in which the individual, entity or property is located. |
| `BJ` | Benin is the country in which the individual, entity or property is located. |
| `BL` | Saint Barthelemy is the country in which the individual, entity or property is located. |
| `BM` | Bermuda is the country in which the individual, entity or property is located. |
| `BN` | Brunei Darussalam is the country in which the individual, entity or property is located. |
| `BO` | Bolivia is the country in which the individual, entity or property is located. |
| `BR` | Brazil is the country in which the individual, entity or property is located. |
| `BS` | Bahamas is the country in which the individual, entity or property is located. |
| `BT` | Bhutan is the country in which the individual, entity or property is located. |
| `BV` | Bouvet Island is the country in which the individual, entity or property is located. |
| `BW` | Botswana is the country in which the individual, entity or property is located. |
| `BY` | Belarus is the country in which the individual, entity or property is located. |
| `BZ` | Belize is the country in which the individual, entity or property is located. |
| `CA` | Canada is the country in which the individual, entity or property is located. |
| `CC` | Cocos (Keeling) Islands is the country in which the individual, entity or property is located. |
| `CD` | Congo Democratic Republic is the country in which the individual, entity or property is located. |
| `CF` | Central African Republic is the country in which the individual, entity or property is located. |
| `CG` | Congo is the country in which the individual, entity or property is located. |
| `CH` | Switzerland is the country in which the individual, entity or property is located. |
| `CI` | Cote d'Ivoire is the country in which the individual, entity or property is located. |
| `CK` | Cook Islands is the country in which the individual, entity or property is located. |
| `CL` | Chile is the country in which the individual, entity or property is located. |
| `CM` | Cameroon is the country in which the individual, entity or property is located. |
| `CN` | China is the country in which the individual, entity or property is located. |
| `CO` | Colombia is the country in which the individual, entity or property is located. |
| `CR` | Costa Rica is the country in which the individual, entity or property is located. |
| `CU` | Cuba is the country in which the individual, entity or property is located. |
| `CV` | Cabo Verde is the country in which the individual, entity or property is located. |
| `CX` | Christmas Island is the country in which the individual, entity or property is located. |
| `CY` | Cyprus is the country in which the individual, entity or property is located. |
| `CZ` | Czechia is the country in which the individual, entity or property is located. |
| `DE` | Germany is the country in which the individual, entity or property is located. |
| `DJ` | Djibouti is the country in which the individual, entity or property is located. |
| `DK` | Denmark is the country in which the individual, entity or property is located. |
| `DM` | Dominica is the country in which the individual, entity or property is located. |
| `DO` | Dominican Republic is the country in which the individual, entity or property is located. |
| `DZ` | Algeria is the country in which the individual, entity or property is located. |
| `EC` | Ecuador is the country in which the individual, entity or property is located. |
| `EE` | Estonia is the country in which the individual, entity or property is located. |
| `EG` | Egypt is the country in which the individual, entity or property is located. |
| `EH` | Western Sahara is the country in which the individual, entity or property is located. |
| `ER` | Eritrea is the country in which the individual, entity or property is located. |
| `ES` | Spain is the country in which the individual, entity or property is located. |
| `ET` | Ethiopia is the country in which the individual, entity or property is located. |
| `FI` | Finland is the country in which the individual, entity or property is located. |
| `FJ` | Fiji is the country in which the individual, entity or property is located. |
| `FK` | Falkland Islands is the country in which the individual, entity or property is located. |
| `FM` | Micronesia is the country in which the individual, entity or property is located. |
| `FO` | Faroe Islands is the country in which the individual, entity or property is located. |
| `FR` | France is the country in which the individual, entity or property is located. |
| `GA` | Gabon is the country in which the individual, entity or property is located. |
| `GB` | United Kingdom is the country in which the individual, entity or property is located. |
| `GD` | Grenada is the country in which the individual, entity or property is located. |
| `GE` | Georgia is the country in which the individual, entity or property is located. |
| `GF` | French Guiana is the country in which the individual, entity or property is located. |
| `GG` | Guernsey is the country in which the individual, entity or property is located. |
| `GH` | Ghana is the country in which the individual, entity or property is located. |
| `GI` | Gibraltar is the country in which the individual, entity or property is located. |
| `GL` | Greenland is the country in which the individual, entity or property is located. |
| `GM` | Gambia is the country in which the individual, entity or property is located. |
| `GN` | Guinea is the country in which the individual, entity or property is located. |
| `GP` | Guadeloupe is the country in which the individual, entity or property is located. |
| `GQ` | Equatorial Guinea is the country in which the individual, entity or property is located. |
| `GR` | Greece is the country in which the individual, entity or property is located. |
| `GS` | South Georgia is the country in which the individual, entity or property is located. |
| `GT` | Guatemala is the country in which the individual, entity or property is located. |
| `GU` | Guam is the country in which the individual, entity or property is located. |
| `GW` | Guinea-Bissau is the country in which the individual, entity or property is located. |
| `GY` | Guyana is the country in which the individual, entity or property is located. |
| `HK` | Hong Kong is the country in which the individual, entity or property is located. |
| `HM` | Heard And McDonald Islands is the country in which the individual, entity or property is located. |
| `HN` | Honduras is the country in which the individual, entity or property is located. |
| `HR` | Croatia is the country in which the individual, entity or property is located. |
| `HT` | Haiti is the country in which the individual, entity or property is located. |
| `HU` | Hungary is the country in which the individual, entity or property is located. |
| `ID` | Indonesia is the country in which the individual, entity or property is located. |
| `IE` | Ireland is the country in which the individual, entity or property is located. |
| `IL` | Israel is the country in which the individual, entity or property is located. |
| `IM` | Isle Of Man is the country in which the individual, entity or property is located. |
| `IN` | India is the country in which the individual, entity or property is located. |
| `IO` | British Indian Ocean Territory is the country in which the individual, entity or property is located. |
| `IQ` | Iraq is the country in which the individual, entity or property is located. |
| `IR` | Iran is the country in which the individual, entity or property is located. |
| `IS` | Iceland is the country in which the individual, entity or property is located. |
| `IT` | Italy is the country in which the individual, entity or property is located. |
| `JE` | Jersey is the country in which the individual, entity or property is located. |
| `JM` | Jamaica is the country in which the individual, entity or property is located. |
| `JO` | Jordan is the country in which the individual, entity or property is located. |
| `JP` | Japan is the country in which the individual, entity or property is located. |
| `KE` | Kenya is the country in which the individual, entity or property is located. |
| `KG` | Kyrgyzstan is the country in which the individual, entity or property is located. |
| `KH` | Cambodia is the country in which the individual, entity or property is located. |
| `KI` | Kiribati is the country in which the individual, entity or property is located. |
| `KM` | Comoros is the country in which the individual, entity or property is located. |
| `KN` | Saint Kitts And Nevis is the country in which the individual, entity or property is located. |
| `KP` | North Korea, officially named the Democratic People's Republic of Korea, is the country in which the individual, entity or property is located. |
| `KR` | South Korea, officially named the Republic of Korea, is the country in which the individual, entity or property is located. |
| `KW` | Kuwait is the country in which the individual, entity or property is located. |
| `KY` | Cayman Islands is the country in which the individual, entity or property is located. |
| `KZ` | Kazakhstan is the country in which the individual, entity or property is located. |
| `LA` | Lao is the country in which the individual, entity or property is located. |
| `LB` | Lebanon is the country in which the individual, entity or property is located. |
| `LC` | Saint Lucia is the country in which the individual, entity or property is located. |
| `LI` | Liechtenstein is the country in which the individual, entity or property is located. |
| `LK` | Sri Lanka is the country in which the individual, entity or property is located. |
| `LR` | Liberia is the country in which the individual, entity or property is located. |
| `LS` | Lesotho is the country in which the individual, entity or property is located. |
| `LT` | Lithuania is the country in which the individual, entity or property is located. |
| `LU` | Luxembourg is the country in which the individual, entity or property is located. |
| `LV` | Latvia is the country in which the individual, entity or property is located. |
| `LY` | Libyan Arab Jamahiriya is the country in which the individual, entity or property is located. |
| `MA` | Morocco is the country in which the individual, entity or property is located. |
| `MC` | Monaco is the country in which the individual, entity or property is located. |
| `MD` | Moldova is the country in which the individual, entity or property is located. |
| `ME` | Montenegro is the country in which the individual, entity or property is located. |
| `MF` | Saint Martin is the country in which the individual, entity or property is located. |
| `MG` | Madagascar is the country in which the individual, entity or property is located. |
| `MH` | Marshall Islands is the country in which the individual, entity or property is located. |
| `MK` | Macedonia is the country in which the individual, entity or property is located. |
| `ML` | Mali is the country in which the individual, entity or property is located. |
| `MM` | Myanmar is the country in which the individual, entity or property is located. |
| `MN` | Mongolia is the country in which the individual, entity or property is located. |
| `MO` | Macao is the country in which the individual, entity or property is located. |
| `MP` | Northern Mariana Islands is the country in which the individual, entity or property is located. |
| `MQ` | Martinique is the country in which the individual, entity or property is located. |
| `MR` | Mauritania is the country in which the individual, entity or property is located. |
| `MS` | Montserrat is the country in which the individual, entity or property is located. |
| `MT` | Malta is the country in which the individual, entity or property is located. |
| `MU` | Mauritius is the country in which the individual, entity or property is located. |
| `MV` | Maldives is the country in which the individual, entity or property is located. |
| `MW` | Malawi is the country in which the individual, entity or property is located. |
| `MX` | Mexico is the country in which the individual, entity or property is located. |
| `MY` | Malaysia is the country in which the individual, entity or property is located. |
| `MZ` | Mozambique is the country in which the individual, entity or property is located. |
| `NA` | Namibia is the country in which the individual, entity or property is located. |
| `NC` | New Caledonia is the country in which the individual, entity or property is located. |
| `NE` | Niger is the country in which the individual, entity or property is located. |
| `NF` | Norfolk Island is the country in which the individual, entity or property is located. |
| `NG` | Nigeria is the country in which the individual, entity or property is located. |
| `NI` | Nicaragua is the country in which the individual, entity or property is located. |
| `NL` | Netherlands is the country in which the individual, entity or property is located. |
| `NP` | Nepal is the country in which the individual, entity or property is located. |
| `NR` | Nauru is the country in which the individual, entity or property is located. |
| `NU` | Niue is the country in which the individual, entity or property is located. |
| `NZ` | New Zealand is the country in which the individual, entity or property is located. |
| `OM` | Oman is the country in which the individual, entity or property is located. |
| `OT` | The country in which the individual, entity or property is located is something other than what is covered by ISO standard 3166 |
| `PA` | Panama is the country in which the individual, entity or property is located. |
| `PE` | Peru is the country in which the individual, entity or property is located. |
| `PF` | French Polynesia is the country in which the individual, entity or property is located. |
| `PG` | Papua New Guinea is the country in which the individual, entity or property is located. |
| `PH` | Philippines is the country in which the individual, entity or property is located. |
| `PK` | Pakistan is the country in which the individual, entity or property is located. |
| `PL` | Poland is the country in which the individual, entity or property is located. |
| `PM` | Saint Pierre And Miquelon is the country in which the individual, entity or property is located. |
| `PN` | Pitcairn is the country in which the individual, entity or property is located. |
| `PR` | Puerto Rico is the country in which the individual, entity or property is located. |
| `PS` | Palestinian Territory is the country in which the individual, entity or property is located. |
| `PT` | Portugal is the country in which the individual, entity or property is located. |
| `PW` | Palau is the country in which the individual, entity or property is located. |
| `PY` | Paraguay is the country in which the individual, entity or property is located. |
| `QA` | Qatar is the country in which the individual, entity or property is located. |
| `RE` | Reunion is the country in which the individual, entity or property is located. |
| `RO` | Romania is the country in which the individual, entity or property is located. |
| `RS` | Serbia is the country in which the individual, entity or property is located. |
| `RU` | Russian Federation is the country in which the individual, entity or property is located. |
| `RW` | Rwanda is the country in which the individual, entity or property is located. |
| `SA` | Saudi Arabia is the country in which the individual, entity or property is located. |
| `SB` | Solomon Islands is the country in which the individual, entity or property is located. |
| `SC` | Seychelles is the country in which the individual, entity or property is located. |
| `SD` | Sudan is the country in which the individual, entity or property is located. |
| `SE` | Sweden is the country in which the individual, entity or property is located. |
| `SG` | Singapore is the country in which the individual, entity or property is located. |
| `SH` | Saint Helena is the country in which the individual, entity or property is located. |
| `SI` | Slovenia is the country in which the individual, entity or property is located. |
| `SJ` | Svalbard - Jan Mayen is the country in which the individual, entity or property is located. |
| `SK` | Slovakia is the country in which the individual, entity or property is located. |
| `SL` | Sierra Leone is the country in which the individual, entity or property is located. |
| `SM` | San Marino is the country in which the individual, entity or property is located. |
| `SN` | Senegal is the country in which the individual, entity or property is located. |
| `SO` | Somalia is the country in which the individual, entity or property is located. |
| `SR` | Suriname is the country in which the individual, entity or property is located. |
| `ST` | Sao Tome And Principe is the country in which the individual, entity or property is located. |
| `SV` | El Salvador is the country in which the individual, entity or property is located. |
| `SY` | Syrian Arab Republic is the country in which the individual, entity or property is located. |
| `SZ` | Swaziland is the country in which the individual, entity or property is located. |
| `TC` | Turks - Caicos Islands is the country in which the individual, entity or property is located. |
| `TD` | Chad is the country in which the individual, entity or property is located. |
| `TF` | French Southern Territories is the country in which the individual, entity or property is located. |
| `TG` | Togo is the country in which the individual, entity or property is located. |
| `TH` | Thailand is the country in which the individual, entity or property is located. |
| `TJ` | Tajikistan is the country in which the individual, entity or property is located. |
| `TK` | Tokelau is the country in which the individual, entity or property is located. |
| `TL` | Timor-Leste is the country in which the individual, entity or property is located. |
| `TM` | Turkmenistan is the country in which the individual, entity or property is located. |
| `TN` | Tunisia is the country in which the individual, entity or property is located. |
| `TO` | Tonga is the country in which the individual, entity or property is located. |
| `TR` | Türkiye is the country in which the individual, entity or property is located. |
| `TT` | Trinidad - Tobago is the country in which the individual, entity or property is located. |
| `TV` | Tuvalu is the country in which the individual, entity or property is located. |
| `TW` | Taiwan is the country in which the individual, entity or property is located. |
| `TZ` | Tanzania is the country in which the individual, entity or property is located. |
| `UA` | Ukraine is the country in which the individual, entity or property is located. |
| `UG` | Uganda is the country in which the individual, entity or property is located. |
| `UM` | United States Minor Islands is the country in which the individual, entity or property is located. |
| `US` | United States is the country in which the individual, entity or property is located. |
| `UY` | Uruguay is the country in which the individual, entity or property is located. |
| `UZ` | Uzbekistan is the country in which the individual, entity or property is located. |
| `VA` | Holy See (Vatican City) is the country in which the individual, entity or property is located. |
| `VC` | Saint Vincent - Grenadines is the country in which the individual, entity or property is located. |
| `VE` | Venezuela is the country in which the individual, entity or property is located. |
| `VG` | Virgin Islands British is the country in which the individual, entity or property is located. |
| `VI` | Virgin Islands U.S. |
| `VN` | Viet Nam is the country in which the individual, entity or property is located. |
| `VU` | Vanuatu is the country in which the individual, entity or property is located. |
| `WF` | Wallis And Futuna is the country in which the individual, entity or property is located. |
| `WS` | Samoa is the country in which the individual, entity or property is located. |
| `YE` | Yemen is the country in which the individual, entity or property is located. |
| `YT` | Mayotte is the country in which the individual, entity or property is located. |
| `ZA` | South Africa is the country in which the individual, entity or property is located. |
| `ZM` | Zambia is the country in which the individual, entity or property is located. |
| `ZW` | Zimbabwe is the country in which the individual, entity or property is located. |

### CurrentFinancing

15 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CurrentFinancing/)

| Value | Definition |
|---|---|
| `Assumable` | The financing currently in place may be assumed. |
| `Contract` | The purchase of a property involves an agreement to perform services, provide product, share income or some other determined method of payment for the property. |
| `Conventional` | The buyer is using conventional financing to purchase the home. |
| `FHA` | A loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `FHA 203(b)` | The basic home mortgage loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `FHA 203(k)` | A loan for the rehabilitation and repair of a single-family residence from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `Leased Renewables` | A renewable system (i.e., solar or wind) belonging to a third party is installed on a customer’s property at little or no cost to the property owner. |
| `None` | There is no current financing on the property. |
| `Other` | The current owner is using another form of financing that is not included in the options provided on this list. |
| `Power Purchase Agreement` | A renewable system belonging to a third-party is installed on a customer’s property at little or no up-front cost to the property owner. |
| `Private` | Financing is provided by a private party. |
| `Property-Assessed Clean Energy` | Property-assessed clean energy (PACE) is a financing tool for property owners to fund energy or water efficiency or renewable energy installations. |
| `Trust Deed` | Financing where property title is placed with a trustee who secures payment of the loan for a beneficiary. |
| `USDA` | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| `VA` | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

### CurrentOrPossibleUse

43 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/CurrentOrPossibleUse/)

| Value | Definition |
|---|---|
| `Agricultural` | The land is currently used for or could be used for agriculture. |
| `Automotive` | This land is currently used for or could be used for automotive maintenance or repair. |
| `Cattle` | This land is currently used for or could be used for cattle. |
| `Commercial` | This land is currently used for or could be used for commercial purposes. |
| `Dairy` | This land is currently used as or could be used as a dairy farm. |
| `Development` | This land is currently used for or could be used for a new development. |
| `Farm` | This land is currently used as or could be used as a farm. |
| `Fishery` | This land is currently used as or could be used as a fishery. |
| `Grazing` | This land is currently used for or could be used for livestock grazing. |
| `Highway/Tourist Service` | This land is currently used for or could be used for highway/tourist service. |
| `Horses` | This land is currently used for or could be used for horses. |
| `Hunting` | This land is currently used for or could be used for hunting. |
| `Industrial` | This land is currently used for or could be used for industrial purposes. |
| `Investment` | This land is currently used as or could be used as an investment. |
| `Livestock` | This land is currently used for or could be used for livestock. |
| `Manufactured Home` | This land is currently used for or could be used for a manufactured home or homes. |
| `Medical/Dental` | This land is currently used for or could be used for a medical/dental business. |
| `Mini Storage` | This land is currently used for or could be used for a mini storage business. |
| `Mixed Use` | This land is currently used for or could be used for mixed uses. |
| `Multi-Family` | The land is currently used for or could be used for a multifamily dwelling or dwellings. |
| `Nursery` | The land is currently used as or could be used as a nursery. |
| `Office` | This land is currently used as or could be used as office space. |
| `Orchard` | This land is currently used as or could be used as an orchard. |
| `Other` | The land is currently used for or could be used for some use other than those on this list. |
| `Pasture` | This land is currently used as or could be used as a pasture. |
| `Place of Worship` | This land is currently used as or could be used as a place of worship. |
| `Plantable` | This land is currently used as or could be used as a plantable field. |
| `Poultry` | This land is currently used as or could be used as a poultry farm. |
| `Ranch` | This land is currently used as or could be used as a ranch. |
| `Recreational` | This land is currently used for or could be used for recreational purposes. |
| `Residential` | This land is currently used for or could be used for residential purposes. |
| `Retail` | This land is currently used for or could be used for retail purposes. |
| `Row Crops` | This land is currently used for or could be used for row crops. |
| `See Remarks` | See the public or private remarks for details on the current or possible use. |
| `Single Family` | The land is currently used for single-family residence. |
| `Subdevelopment` | This land is currently used for or could be used for a subdevelopment or subdevelopments. |
| `Subdivision` | This land is currently used for or could be used for property subdivisions. |
| `Timber` | This land is currently used for or could be used for timber. |
| `Tree Farm` | This land is currently used as or could be used as a tree farm. |
| `Unimproved` | The land is currently unimproved. |
| `Vacant` | The land is currently vacant. |
| `Vineyard` | This land is currently used as or could be used as a vineyard. |
| `Warehouse` | This land is currently used for or could be used for warehousing. |

### DevelopmentStatus

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/DevelopmentStatus/)

| Value | Definition |
|---|---|
| `Completed` | The development of the land is complete. |
| `Finished Lot(s)` | The development of the land is finished. |
| `Other` | The development status of the land is something other than those options on this list. |
| `Proposed` | The development of the land is in the proposal phase. |
| `Raw Land` | The land is raw and undeveloped. |
| `Rough Grade` | The development of the last is in the rough grade phase. |
| `See Remarks` | See the public or private remarks for details on the development status of the land. |
| `Site Plan Approved` | The site plan has been approved for the development. |
| `Site Plan Filed` | The site plan has been filed for the development. |
| `Under Construction` | There is construction in progress at the development. |

### DirectionFaces

8 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/DirectionFaces/)

| Value | Definition |
|---|---|
| `East` | The front of the structure faces east. |
| `North` | The front of the structure faces north. |
| `Northeast` | The front of the structure faces northeast. |
| `Northwest` | The front of the structure faces northwest. |
| `South` | The front of the structure faces south. |
| `Southeast` | The front of the structure faces southeast. |
| `Southwest` | The front of the structure faces southwest. |
| `West` | The front of the structure faces west. |

### DocumentStatus

16 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/DocumentStatus/)

| Value | Definition |
|---|---|
| `Accepted` | Document has been accepted by a party in the transaction. |
| `Archived` | Document has been archived by a party in the transaction. |
| `Changed` | Document has been changed by a party in the transaction. |
| `Countered` | Document has been countered by either (any) party. |
| `Deleted` | Document has been deleted by a party in the transaction. |
| `Delivered` | Document has been delivered by a party in the transaction. |
| `Finalized` | Document has been finalized by all clients in the transaction. |
| `In Escrow` | Document indicating escrow for the transaction. |
| `Missing` | A placeholder for where a contract requires certain items before execution. |
| `Optional` | Document is optional for the transaction. |
| `Published` | Document has been published by a party in the transaction. |
| `Received` | Document has been received by a party in the transaction. |
| `Rejected` | Document has been rejected by a party in the transaction. |
| `Required` | Document is required for the transaction. |
| `Signed` | Document has been signed by a party in the transaction. |
| `Submitted` | Document has been submitted to cooperating party or parties. |

### DoorFeatures

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/DoorFeatures/)

| Value | Definition |
|---|---|
| `ENERGY STAR Qualified Doors` | The property has a qualified ENERGY STAR door or multiple qualified doors. |
| `French Doors` | The property has doors with glass panes throughout the length of the door. |
| `Mirrored Closet Door(s)` | The property has one or more closet doors that have a mirrored surface. |
| `Sliding Doors` | The property has sliding doors. |
| `Storm Door(s)` | The property has one or more storm doors. |

### Electric

18 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Electric/)

| Value | Definition |
|---|---|
| `100 Amp Service` | The electrical features of the property include 100 amp service. |
| `150 Amp Service` | The electrical features of the property include 150 amp service. |
| `200+ Amp Service` | The electrical features of the property include 200+ amp service. |
| `220 Volts` | The electrical features of the property include 220 volts. |
| `220 Volts For Spa` | The electrical features of the property include 220 volts for spa. |
| `220 Volts in Garage` | The electrical features of the property include 220 volts in garage. |
| `220 Volts in Kitchen` | The electrical features of the property include 220 volts in kitchen. |
| `220 Volts in Laundry` | The electrical features of the property include 220 volts in laundry. |
| `220 Volts in Workshop` | The electrical features of the property include 220 volts in workshop. |
| `440 Volts` | The electrical features of the property include 440 volts. |
| `Circuit Breakers` | The electrical features of the property include circuit breakers. |
| `Energy Storage Device` | A device that captures energy at one time to be used at a later time. |
| `Fuses` | The electrical features of the property include fuses. |
| `Generator` | The electrical features of the property include a generator. |
| `Net Meter` | Net metering is an electric service that allows electricity generated on a consumer’s site ("on-site") to offset that consumer’s use. |
| `Pre-Wired for Renewables` | Indicates the electric infrastructure on the property has been extended to more easily incorporate an on-site electric generation facility in the future. |
| `Ready for Renewables` | Indicates a comprehensive infrastructure is in place on the property to more easily incorporate an on-site electric generation facility in the future. |
| `Underground` | The electrical features of the property include components that are underground. |

### ExistingLeaseType

9 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ExistingLeaseType/)

| Value | Definition |
|---|---|
| `Absolute Net` | Also known as a bondable lease, the tenant carries every risk in addition to the costs of an NNN lease. |
| `CPI Adjustment` | An escalation clause/provision in a lease to adjust the amount paid by the tenant (lessee) where the adjustment will follow the Consumer Price Index (CPI). |
| `Escalation Clause` | A clause or provision in a lease document that set a formula for how rent will increase over time. |
| `Gross` | A lease agreement where the owner (lessor) pays all property changes normal to ownership. |
| `Ground Lease` | Typically a long-term lease of land where the tenant (lessee) has the right to develop or make improvements. |
| `Net` | A lease agreement where the tenant pays the real estate taxes. |
| `NN` | A lease agreement where the tenant pays real estate taxes and building insurance. |
| `NNN` | A lease agreement where the tenant pays real estate taxes, building insurance and maintenance. |
| `Oral` | The terms of the lease are agreed upon orally (not in writing) between the lessee and lessor. |

### ExteriorFeatures

37 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ExteriorFeatures/)

| Value | Definition |
|---|---|
| `Awning(s)` | The property has one or more awnings on its exterior. |
| `Balcony` | The property has an exterior balcony. |
| `Barbecue` | The property has an outdoor barbeque. |
| `Basketball Court` | The property has a basketball court. |
| `Boat Slip` | The property includes a boat slip. |
| `Built-in Barbecue` | The property has a built-in outdoor barbeque. |
| `Courtyard` | The property has a courtyard. |
| `Covered Courtyard` | The property has a covered courtyard. |
| `Dock` | The property includes a dock. |
| `Dog Run` | The property has a dog run. |
| `Electric Grill` | The property has an outdoor electric grill. |
| `Fire Pit` | The property has an outdoor fire pit. |
| `Garden` | The property has a garden. |
| `Gas Grill` | The property has an outdoor gas grill. |
| `Gray Water System` | The property has a gray water (aka greywater or grey water) system. |
| `Kennel` | The property has a kennel. |
| `Lighting` | The property has exterior lighting. |
| `Misting System` | The property has a misting system. |
| `None` | The property has no exterior features. |
| `Other` | The property has exterior features other than those on this list. |
| `Outdoor Grill` | The property has an outdoor grill. |
| `Outdoor Kitchen` | The property has an outdoor kitchen. |
| `Outdoor Shower` | The property has an outdoor shower. |
| `Permeable Paving` | The property has preamble paving that allows fluids to run through the paving to the below ground or channeling. |
| `Playground` | The property has a playground. |
| `Private Entrance` | The property has a private entrance. |
| `Private Yard` | The property has a private yard. |
| `Rain Barrel/Cistern(s)` | The property has a cistern for water collection. |
| `Rain Gutters` | The structure has rain gutters. |
| `RV Hookup` | The property has hookups for recreational vehicles. |
| `Smart Camera(s)/Recording` | A camera or recording control unit that has convenience and energy-saving aspects. |
| `Smart Irrigation` | An irrigation system that has convenience and energy-saving aspects. |
| `Smart Light(s)` | A lighting control unit that has convenience and energy-saving aspects. |
| `Smart Lock(s)` | A locking system that has convenience and safety aspects. |
| `Storage` | The property has external storage. |
| `Tennis Court(s)` | The property has one or more tennis courts. |
| `Uncovered Courtyard` | The property has an uncovered courtyard. |

### FeeFrequency

11 values · used by 4 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FeeFrequency/)

| Value | Definition |
|---|---|
| `Annually` | A fee is paid or received once a year. |
| `Bi-Monthly` | A fee is paid or received every other month. |
| `Bi-Weekly` | A fee is paid or received every other week. |
| `Daily` | A fee is paid or received daily. |
| `Monthly` | A fee is paid or received once a month. |
| `One Time` | A fee is paid or received once and is not reoccurring. |
| `Quarterly` | A fee is paid or received every three months. |
| `Seasonal` | A fee is paid or received seasonally. |
| `Semi-Annually` | A fee is paid or received twice a year. |
| `Semi-Monthly` | A fee is paid or received twice a month, generally on the 1st and 15th, but that may vary. |
| `Weekly` | A fee is paid or received weekly. |

### Fencing

29 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Fencing/)

| Value | Definition |
|---|---|
| `Back Yard` | The backyard is fenced. |
| `Barbed Wire` | The fencing has barbed wire. |
| `Block` | The property has one or more block walls. |
| `Brick` | The property has one or more brick walls. |
| `Chain Link` | The property has chain-link fencing. |
| `Cross Fenced` | The property is cross fenced. |
| `Electric` | The property has electric fencing. |
| `Fenced` | The property is fenced. |
| `Front Yard` | The front yard is fenced. |
| `Full` | The full property is fenced. |
| `Gate` | The fencing has one or more gates. |
| `Invisible` | The property has invisible fencing. |
| `Masonry` | The property has one or more masonry walls. |
| `None` | The property has no fencing. |
| `Other` | The property has a type of fencing that is not included on this list. |
| `Partial` | The property is partially fenced. |
| `Partial Cross` | The property has partial cross fencing. |
| `Perimeter` | The property has a perimeter fence. |
| `Pipe` | The property has pipe fencing. |
| `Privacy` | The property has privacy fencing. |
| `Security` | The property has security fencing. |
| `See Remarks` | See the public or private remarks for details on the fencing. |
| `Slump Stone` | The property has one or more slump stone walls. |
| `Split Rail` | The property has split rail fencing. |
| `Stone` | The property has one or more stone walls. |
| `Vinyl` | The property has vinyl fencing. |
| `Wire` | The property has wire fencing. |
| `Wood` | The property has wooden fencing. |
| `Wrought Iron` | The property has wrought iron fencing. |

### FhaEligibility

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FhaEligibility/)

| Value | Definition |
|---|---|
| `Approved` | This listing is eligible for an FHA loan. |
| `Conditionally Approved` | This listing is eligible for a Federal Housing Administration (FHA) loan as long as some conditions are met. |
| `Rejected` | This listing is not eligible for a Federal Housing Administration (FHA) loan. |
| `Unknown` | Unknown is selected when Federal Housing Administration (FHA) eligibility is not known. |
| `Withdrawn` | Federal Housing Administration (FHA) eligibility has been withdrawn and is no longer applicable. |

### FinancialDataSource

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FinancialDataSource/)

| Value | Definition |
|---|---|
| `Accountant` | The financial data in the listing was provided by an accountant. |
| `Owner` | the financial data in the listing was provided by the owner. |
| `Property Manager` | the financial data in the listing was provided by the property manager. |

### FireplaceFeatures

44 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FireplaceFeatures/)

| Value | Definition |
|---|---|
| `Basement` | There is a fireplace in the basement. |
| `Bath` | The property includes a bathroom fireplace. |
| `Bedroom` | The property has a bedroom fireplace. |
| `Blower Fan` | The fireplace has a blower fan. |
| `Circulating` | The fireplace has a circulation system. |
| `Decorative` | The property has a decorative fireplace. |
| `Den` | The property has a fireplace in the den. |
| `Dining Room` | The property has a fireplace in the dining room. |
| `Double Sided` | The property has a double-sided fireplace. |
| `Electric` | The fireplace is electric. |
| `EPA Certified Wood Stove` | The property has a wood stove certified by the Environmental Protection Agency (EPA). |
| `EPA Qualified Fireplace` | The property has a fireplace certified by the Environmental Protection Agency (EPA). |
| `Factory Built` | The fireplace is factory built and later installed into the property. |
| `Family Room` | There is a fireplace in the family room. |
| `Fire Pit` | The property has a fire pit. |
| `Free Standing` | The fireplace is free standing, rather than built-in. |
| `Gas` | The fireplace burns gas. |
| `Gas Log` | The gas fireplace has a gas log. |
| `Gas Starter` | The fireplace has a gas starter but also burns wood or other fuels. |
| `Glass Doors` | The fireplace has glass doors. |
| `Great Room` | There is a fireplace in the great room. |
| `Heatilator` | The fireplace has a built-in ventilation system used to circulate heat. |
| `Insert` | A fireplace insert is a device inserted into an existing masonry or prefabricated fireplace. |
| `Kitchen` | The property has a fireplace in the kitchen. |
| `Library` | The property has a fireplace in the library. |
| `Living Room` | The property has a fireplace in the living room. |
| `Masonry` | The fireplace is made of masonry. |
| `Master Bedroom` | The property has a fireplace in the primary bedroom. |
| `Metal` | The fireplace is made of metal. |
| `None` | The property has no fireplace. |
| `Other` | The fireplace has features that are not included on this list. |
| `Outside` | The property has an outdoor fireplace. |
| `Pellet Stove` | The property has a stove that burns compressed wood or biomass pellets to generate heat. |
| `Propane` | The fireplace burns propane. |
| `Raised Hearth` | The fireplace has a raised hearth. |
| `Recreation Room` | The property has a fireplace in a recreation room. |
| `Sealed Combustion` | The fireplace has a sealed combustion chamber. |
| `See Remarks` | See the remarks fields for additional information about any fireplace features. |
| `See Through` | The property has a see-through fireplace, usually positioned between two rooms. |
| `Stone` | The property has a fireplace made with stone. |
| `Ventless` | The property has a ventless fireplace. |
| `Wood Burning` | The fireplace is wood burning. |
| `Wood Burning Stove` | The property includes a wood-burning stove. |
| `Zero Clearance` | The property has a zero-clearance fireplace. |

### Flooring

39 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Flooring/)

| Value | Definition |
|---|---|
| `Adobe` | The property includes adobe flooring. |
| `Bamboo` | The property includes bamboo flooring. |
| `Brick` | The property includes brick flooring. |
| `Carpet` | The property includes carpet flooring. |
| `Ceramic Tile` | The property includes ceramic tile flooring. |
| `Clay` | The property includes clay flooring. |
| `Combination` | The property includes combination flooring. |
| `Concrete` | The property includes concrete flooring. |
| `Cork` | The property includes cork flooring. |
| `CRI Green Label Plus Certified Carpet` | The property includes certified CRI Green Label Plus carpet flooring. |
| `Dirt` | The property has dirt flooring. |
| `Engineered Hardwood` | The property includes engineered hardwood flooring, a type of flooring made up of derivative wood products that are manufactured by binding or fixing the strands, particles, fibers, veneers or boards … |
| `FloorScore(r) Certified Flooring` | The property includes FloorScore® certified flooring . |
| `FSC or SFI Certified Source Hardwood` | The property includes certified FSC or SFI source hardwood flooring. |
| `Granite` | The property includes granite flooring. |
| `Hardwood` | The property includes hardwood flooring. |
| `Laminate` | The property includes laminate flooring. |
| `Linoleum` | The property includes linoleum flooring. |
| `Luxury Vinyl` | The property includes luxury vinyl flooring, which is a waterproof and durable flooring that mimics the look of hardwood or stone. |
| `Marble` | The property includes marble flooring. |
| `None` | The property has no flooring. |
| `Other` | The property includes flooring that is not included on this list. |
| `Painted/Stained` | The property includes painted or stained flooring. |
| `Parquet` | The property includes parquet flooring. |
| `Pavers` | The property includes flooring pavers. |
| `Plank` | The property includes plank flooring, which comes in multi-ply, long, narrow strips and is thicker than typical sheet vinyl. |
| `Reclaimed Wood` | The property includes reclaimed wood flooring. |
| `See Remarks` | See the remarks field for additional information about the flooring included with the property. |
| `Simulated Wood` | The property includes simulated wood flooring. |
| `Slate` | The property includes slate flooring. |
| `Softwood` | The property includes softwood flooring. |
| `Stamped` | The property includes stamped flooring. |
| `Stone` | The property includes stone flooring. |
| `Sustainable` | The property includes sustainable flooring. |
| `Terrazzo` | The property includes terrazzo flooring. |
| `Tile` | The property includes tile flooring. |
| `Varies` | The property flooring type varies. |
| `Vinyl` | The property includes vinyl flooring. |
| `Wood` | The property includes wood flooring. |

### FoundationDetails

12 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FoundationDetails/)

| Value | Definition |
|---|---|
| `Block` | The foundation of the property is made wholly or partially of block. |
| `Brick/Mortar` | The foundation of the property is made wholly or partially of brick/mortar. |
| `Combination` | The foundation of the property is made of a combination of materials. |
| `Concrete Perimeter` | The foundation of the property has a concrete perimeter. |
| `None` | There are no details about the foundation of the property. |
| `Other` | A foundation type not included on this list. |
| `Permanent` | The foundation is permanent and not temporary or movable. |
| `Pillar/Post/Pier` | The foundation of the property is made wholly or partially of pillar/post/pier. |
| `Raised` | The foundation of the property is raised. |
| `See Remarks` | See the listing's remarks for details about the foundation. |
| `Slab` | The foundation of the property is made wholly or partially of a concrete slab. |
| `Stone` | The foundation of the property is made wholly or partially of stone. |

### FrontageType

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/FrontageType/)

| Value | Definition |
|---|---|
| `Bay/Harbor` | The property fronts to a bay or harbor. |
| `Golf Course` | The property fronts to a golf course. |
| `Lagoon/Estuary` | The property fronts to a lagoon or estuary. |
| `Lakefront` | The property is on a lakefront. |
| `Oceanfront` | The property is on an oceanfront. |
| `Other` | The frontage of the property is something other than the options on this list. |
| `River` | The property is on a riverfront. |
| `See Remarks` | See the public or private remarks for details on the frontage of the property. |
| `Waterfront` | The property is on a waterfront. |

### Furnished

4 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Furnished/)

| Value | Definition |
|---|---|
| `Furnished` | The dwelling being leased is furnished. |
| `Negotiable` | The property may be furnished or left unfurnished at the lessor's request. |
| `Partially` | The dwelling being leased is partially furnished. |
| `Unfurnished` | The dwelling being leased is not furnished. |

### GreenBuildingVerificationType

18 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenBuildingVerificationType/)

| Value | Definition |
|---|---|
| `Certified Passive House` | Super-insulated new homes that have been built to meet certification requirements demonstrating minimal or no heating and cooling system. |
| `ENERGY STAR Certified Homes` | EPA ENERGY STAR Certified Homes is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to upgrade a new home's energy efficiency beyond minimum code requirements. |
| `EnerPHit` | Super-insulated existing homes that have been remodeled to meet certification requirements demonstrating minimal or no heating and cooling system. |
| `HERS Index Score` | The HERS Index is a nationally recognized scoring system for measuring a home's energy performance in the U.S. |
| `Home Energy Score` | The Home Energy Score, managed by the U.S. |
| `Home Energy Upgrade Certificate of Energy Efficiency Improvements` | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU). |
| `Home Energy Upgrade Certificate of Energy Efficiency Performance` | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU) and provides one or more measures of a home's performance. |
| `Home Performance with ENERGY STAR` | Home Performance with ENERGY STAR (HPwES) offers whole-house solutions to high energy bills and homes with comfort problems. |
| `Indoor airPLUS` | Indoor airPLUS from the U.S. |
| `LEED For Homes` | The U.S. |
| `Living Building Challenge` | The International Living Future Institute third-party certification that proves that a home produces as much or more energy than is used. |
| `NGBS New Construction` | Home Innovation Research Labs certifies homes to the ICC-700 National Green Building Standard (NGBS), which has undergone the full consensus process and received approval from the American National Standards Institute (ANSI). |
| `NGBS Small Projects Remodel` | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| `NGBS Whole-Home Remodel` | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| `Pearl Certification` | Pearl is a national firm that provides third-party certification of high-performing homes (residential, 1-4 units) at various levels. |
| `PHIUS+` | Super-insulated homes that have met certification requirements demonstrating minimal or no heating and cooling system. |
| `WaterSense` | EPA WaterSense is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to ensure a home uses less water while still providing the same level of comfort and convenience. |
| `Zero Energy Ready Home` | DOE Zero Energy Ready Home is a set of optional construction practices and technologies (above minimum code and ENERGY STAR Certified Home requirements) that builders can follow to ensure high-performance homes that are so energy efficient that all or most annual energy consumption can be offset with renewable energy. |

### GreenEnergyEfficient

12 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenEnergyEfficient/)

| Value | Definition |
|---|---|
| `Appliances` | For purposes of marketing, the property has appliances that have some green/efficient rating or quality. |
| `Construction` | For purposes of marketing, the property has construction that has some green/efficient rating or quality. |
| `Doors` | For purposes of marketing, the property has doors that have some green/efficient rating or quality. |
| `Exposure/Shade` | For purposes of marketing, the property has exposure/shade that has some green/efficient rating or quality. |
| `HVAC` | For purposes of marketing, the property has a heating, ventilation and air conditioning system that has some green/efficient rating or quality. |
| `Incentives` | For purposes of marketing, the property has incentives that have some green/efficiency focus. |
| `Insulation` | For purposes of marketing, the property has insulation that has some green/efficient rating or quality. |
| `Lighting` | For purposes of marketing, the property has lighting that has some green/efficient rating or quality. |
| `Roof` | For purposes of marketing, the property has a roof that has some green/efficient rating or quality. |
| `Thermostat` | For purposes of marketing, the property has a thermostat or thermostats that have some green/efficient rating or quality. |
| `Water Heater` | For purposes of marketing, the property has a water heater that has some green/efficient rating or quality. |
| `Windows` | For purposes of marketing, the property has windows that have some green/efficient rating or quality. |

### GreenEnergyGeneration

2 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenEnergyGeneration/)

| Value | Definition |
|---|---|
| `Solar` | A renewable form of onsite power generation. |
| `Wind` | A renewable form of onsite power generation. |

### GreenIndoorAirQuality

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenIndoorAirQuality/)

| Value | Definition |
|---|---|
| `Contaminant Control` | The property has been carefully designed to prevent, monitor and suppress pollution issues. |
| `Integrated Pest Management` | The property is designed for systematic management of pests that uses prevention, exclusion, monitoring and suppression. |
| `Moisture Control` | Every foundation, roof, roofing component, exterior wall, door, skylight and window is designed and maintained to be watertight and free of persistent dampness or moisture. |
| `Ventilation` | Furnaces, water heaters, woodstoves and other devices that employ combustion-burning fuel are vented to the outside in a manner that meets manufacturer specifications to prevent back drafting. |

### GreenSustainability

7 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenSustainability/)

| Value | Definition |
|---|---|
| `Conserving Methods` | Construction is planned to require fewer materials while maintaining structural integrity and may include advanced wall framing as documented in several major green building programs. |
| `Onsite Recycling Center` | Property includes sufficient built-in storage space and/or containers for temporary storage of recyclable materials and/or compost collection. |
| `Recyclable Materials` | The structure includes multiple products that have a significant amount of postconsumer recycled content. |
| `Recycled Materials` | The structure includes multiple products that have a significant amount of postconsumer recycled content. |
| `Regionally-Sourced Materials` | Refers to building materials that were manufactured, extracted, harvested or recovered within 500 miles of the building. |
| `Renewable Materials` | The structure includes materials that are naturally occurring, abundant and/or fast growing. |
| `Salvaged Materials` | The structure incorporates materials that were diverted from a landfill and/or sourced to give an otherwise unused item fresh use as an attached fixture. |

### GreenWaterConservation

6 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/GreenWaterConservation/)

| Value | Definition |
|---|---|
| `Efficient Hot Water Distribution` | Efficient hot water distribution systems are designed to generate hot water using fewer fuel resources and to get hot water to low-flow faucets and fixtures more quickly. |
| `Gray Water System` | The property includes a gray water system. |
| `Green Infrastructure` | A set of strategies and specifically designed systems to manage stormwater runoff through a variety of small, cost-effective landscape features located on a property. |
| `Low-Flow Fixtures` | Toilets, bathroom faucets, showerheads, irrigation controllers and other products can be manufactured to use less water than minimum standards. |
| `Water Recycling` | The property includes a system to reuse stormwater via rain barrels or cisterns for landscaping or to treat and reuse water from bathroom sinks, showers and clothes washing drains for landscape irriga… |
| `Water-Smart Landscaping` | Water-smart landscapes are designed to require less water and fertilizer treatments. |

### Heating

42 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Heating/)

| Value | Definition |
|---|---|
| `Active Solar` | Active solar heating systems use solar energy to heat a fluid - either liquid or air - and then transfer the solar heat directly to the interior space or to a storage system for later use. |
| `Baseboard` | Baseboard heating utilizes convection; as cold air drops from the window, it enters the baseboard heating unit where the air is warmed by heating elements, typically fins. |
| `Ceiling` | A heating unit that is installed into or upon the surface of the ceiling. |
| `Central` | A system where heat is generated in one or more locations in the structure and distributed throughout the structure. |
| `Coal` | The heating system uses coal as its fuel to generate heat. |
| `Coal Stove` | A coal-burning stove that is used for heat. |
| `Ductless` | The heating system does not have ducting like that found in forced-air systems. |
| `Electric` | The heating system utilizes electricity and heating elements such as coils or fins to generate heat. |
| `ENERGY STAR Qualified Equipment` | The heating system is ENERGY STAR qualified. |
| `ENERGY STAR/ACCA RSI Qualified Installation` | The heating system installation was done by a qualified ENERGY STAR or ACCA RSI contractor. |
| `Exhaust Fan` | The property has an exhaust fan. |
| `Fireplace Insert` | The property has a fireplace insert for generating heat. |
| `Fireplace(s)` | The property has one or more fireplaces used to generate heat. |
| `Floor Furnace` | The property has a radiant heating system that is mounted into the floor and distributes heat via convection. |
| `Forced Air` | The property has a forced air system, typically via ducting throughout the structure. |
| `Geothermal` | A geothermal heating system, also known as a ground source heat pump, transfers heat from below ground into the structure. |
| `Gravity` | A gravity heating system, also known as an octopus furnace, is typically a ducted system that doesn't use a fan but rather is designed to allow the heat to rise naturally through the ducts to differen… |
| `Heat Pump` | A system that exchanges heat between a warm and cool space. |
| `Hot Water` | The heating system uses a boiler and pipes to deliver hot water to radiators throughout the dwelling. |
| `Humidity Control` | The heating system has humidity control. |
| `Kerosene` | The heating system uses kerosene as its fuel to generate heat. |
| `Natural Gas` | The heating system uses natural gas as its fuel to generate heat. |
| `None` | The property does not have a heating system. |
| `Oil` | The heating system uses oil as its fuel to generate heat. |
| `Other` | The property has a heating system or features that are not included on this list. |
| `Passive Solar` | Passive solar is a building design where the walls, windows, floors, etc., are made to collect heat and warm the dwelling. |
| `Pellet Stove` | The property has a stove that burns compressed wood or biomass pellets to generate heat. |
| `Propane` | The heating system uses propane as its fuel to generate heat. |
| `Propane Stove` | The property has a stove that burns propane to generate heat. |
| `Radiant` | The heating system uses radiators to release heat within the dwelling. |
| `Radiant Ceiling` | The radiant heating element(s) are located in the ceiling. |
| `Radiant Floor` | The radiant heating element(s) are located in the floor. |
| `See Remarks` | See the remarks fields for additional information about the heating system included with the property. |
| `Separate Meters` | The heating system has multiple units and/or is zoned with separate meters for each zone/unit. |
| `Solar` | The property has a heating system or method that uses an unspecified type of solar heating. |
| `Space Heater` | The property comes with a stand-alone space heater. |
| `Steam` | The heating system uses a boiler and pipes to deliver hot water to radiators throughout the dwelling. |
| `Varies by Unit` | The type of heating or heating features vary from unit to unit. |
| `Wall Furnace` | Typically a ductless system that is built into a wall to deliver to the room in which it's installed. |
| `Wood` | The heating system uses wood as its fuel to generate heat. |
| `Wood Stove` | The property has a stove that burns wood to generate heat. |
| `Zoned` | The heating system is zoned, allowing for independent control of two or more parts of the structure. |

### HorseAmenities

18 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/HorseAmenities/)

| Value | Definition |
|---|---|
| `Arena` | The property allows for horses and has an arena. |
| `Barn` | The property allows horses and has a barn. |
| `Boarding Facilities` | The property has boarding facilities for horses. |
| `Corral(s)` | The property allows horses and has one or more corrals. |
| `Hay Storage` | The property allows horses and has hay storage. |
| `None` | The property either does not allow horses or has no amenities for horses. |
| `Other` | The property has horse amenities other than those on this list. |
| `Paddocks` | The property allows horses and has an enclosed living are for them. |
| `Palpation Chute` | A portion of the livestock chute where the animal is held for examination or other purposes. |
| `Pasture` | The property includes or has access to a pasture for horses. |
| `Riding Trail` | The property includes or has access to a riding trail or riding trails. |
| `Round Pen` | The property includes or has access to a round enclosure used for horse training. |
| `See Remarks` | See the remarks fields for additional information about horse amenities. |
| `Shaving Bin` | The property includes or has access to a storage container for wood shavings that are used as ground cover for horses. |
| `Stable(s)` | The property includes or has access to a horse stable or stables. |
| `Tack Room` | The property includes or has access to a room to store equipment such as saddles, stirrups, bridles, halters, reins, bits, harnesses, martingales, breastplates, etc. |
| `Trailer Storage` | The property includes or has access to a place to store a horse trailer. |
| `Wash Rack` | The property includes or has access to a rack used to confine/restrain a horse for purposes of washing the horse. |

### HoursDaysOfOperation

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/HoursDaysOfOperation/)

| Value | Definition |
|---|---|
| `Evenings Only` | The business being sold is open in the evenings only. |
| `Open 24 Hours` | The business being sold is open 24 hours per day. |
| `Open 7 Days` | The business being sold is open 7 days per week. |
| `Open 8 Hours/Day` | The business being sold is open 8 hours per day. |
| `Open -8 Hours/Day` | The business being sold is open less than 8 hours per day. |
| `Open 8+ Hours/Day` | The business being sold is open more than 8 hours per day. |
| `Open Monday-Friday` | The business being sold is open Monday through Friday. |
| `Open Saturday` | The business being sold is open on Saturdays. |
| `Open Sunday` | The business being sold is open on Sundays. |

### IanaTimeZoneValues

482 values · used by 3 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/IanaTimeZoneValues/)

| Value | Definition |
|---|---|
| `Africa/Abidjan` | The time zone is identified as the Africa/Abidjan time zone from the IANA tz database. |
| `Africa/Accra` | The time zone is identified as the Africa/Accra time zone from the IANA tz database. |
| `Africa/Addis_Ababa` | The time zone is identified as the Africa/Addis_Ababa time zone from the IANA tz database. |
| `Africa/Algiers` | The time zone is identified as the Africa/Algiers time zone from the IANA tz database. |
| `Africa/Asmara` | The time zone is identified as the Africa/Asmara time zone from the IANA tz database. |
| `Africa/Asmera` | The time zone is identified as the Africa/Asmera time zone from the IANA tz database. |
| `Africa/Bamako` | The time zone is identified as the Africa/Bamako time zone from the IANA tz database. |
| `Africa/Bangui` | The time zone is identified as the Africa/Bangui time zone from the IANA tz database. |
| `Africa/Banjul` | The time zone is identified as the Africa/Banjul time zone from the IANA tz database. |
| `Africa/Bissau` | The time zone is identified as the Africa/Bissau time zone from the IANA tz database. |
| `Africa/Blantyre` | The time zone is identified as the Africa/Blantyre time zone from the IANA tz database. |
| `Africa/Brazzaville` | The time zone is identified as the Africa/Brazzaville time zone from the IANA tz database. |
| `Africa/Bujumbura` | The time zone is identified as the Africa/Bujumbura time zone from the IANA tz database. |
| `Africa/Cairo` | The time zone is identified as the Africa/Cairo time zone from the IANA tz database. |
| `Africa/Casablanca` | The time zone is identified as the Africa/Casablanca time zone from the IANA tz database. |
| `Africa/Ceuta` | The time zone is identified as the Africa/Ceuta time zone from the IANA tz database. |
| `Africa/Conakry` | The time zone is identified as the Africa/Conakry time zone from the IANA tz database. |
| `Africa/Dakar` | The time zone is identified as the Africa/Dakar time zone from the IANA tz database. |
| `Africa/Dar_es_Salaam` | The time zone is identified as the Africa/Dar_es_Salaam time zone from the IANA tz database. |
| `Africa/Djibouti` | The time zone is identified as the Africa/Djibouti time zone from the IANA tz database. |
| `Africa/Douala` | The time zone is identified as the Africa/Douala time zone from the IANA tz database. |
| `Africa/El_Aaiun` | The time zone is identified as the Africa/El_Aaiun time zone from the IANA tz database. |
| `Africa/Freetown` | The time zone is identified as the Africa/Freetown time zone from the IANA tz database. |
| `Africa/Gaborone` | The time zone is identified as the Africa/Gaborone time zone from the IANA tz database. |
| `Africa/Harare` | The time zone is identified as the Africa/Harare time zone from the IANA tz database. |
| `Africa/Johannesburg` | The time zone is identified as the Africa/Johannesburg time zone from the IANA tz database. |
| `Africa/Juba` | The time zone is identified as the Africa/Juba time zone from the IANA tz database. |
| `Africa/Kampala` | The time zone is identified as the Africa/Kampala time zone from the IANA tz database. |
| `Africa/Khartoum` | The time zone is identified as the Africa/Khartoum time zone from the IANA tz database. |
| `Africa/Kigali` | The time zone is identified as the Africa/Kigali time zone from the IANA tz database. |
| `Africa/Kinshasa` | The time zone is identified as the Africa/Kinshasa time zone from the IANA tz database. |
| `Africa/Lagos` | The time zone is identified as the Africa/Lagos time zone from the IANA tz database. |
| `Africa/Libreville` | The time zone is identified as the Africa/Libreville time zone from the IANA tz database. |
| `Africa/Lome` | The time zone is identified as the Africa/Lome time zone from the IANA tz database. |
| `Africa/Luanda` | The time zone is identified as the Africa/Luanda time zone from the IANA tz database. |
| `Africa/Lubumbashi` | The time zone is identified as the Africa/Lubumbashi time zone from the IANA tz database. |
| `Africa/Lusaka` | The time zone is identified as the Africa/Lusaka time zone from the IANA tz database. |
| `Africa/Malabo` | The time zone is identified as the Africa/Malabo time zone from the IANA tz database. |
| `Africa/Maputo` | The time zone is identified as the Africa/Maputo time zone from the IANA tz database. |
| `Africa/Maseru` | The time zone is identified as the Africa/Maseru time zone from the IANA tz database. |
| `Africa/Mbabane` | The time zone is identified as the Africa/Mbabane time zone from the IANA tz database. |
| `Africa/Mogadishu` | The time zone is identified as the Africa/Mogadishu time zone from the IANA tz database. |
| `Africa/Monrovia` | The time zone is identified as the Africa/Monrovia time zone from the IANA tz database. |
| `Africa/Nairobi` | The time zone is identified as the Africa/Nairobi time zone from the IANA tz database. |
| `Africa/Ndjamena` | The time zone is identified as the Africa/Ndjamena time zone from the IANA tz database. |
| `Africa/Niamey` | The time zone is identified as the Africa/Niamey time zone from the IANA tz database. |
| `Africa/Nouakchott` | The time zone is identified as the Africa/Nouakchott time zone from the IANA tz database. |
| `Africa/Ouagadougou` | The time zone is identified as the Africa/Ouagadougou time zone from the IANA tz database. |
| `Africa/Porto-Novo` | The time zone is identified as the Africa/Porto-Novo time zone from the IANA tz database. |
| `Africa/Sao_Tome` | The time zone is identified as the Africa/Sao_Tome time zone from the IANA tz database. |
| `Africa/Timbuktu` | The time zone is identified as the Africa/Timbuktu time zone from the IANA tz database. |
| `Africa/Tripoli` | The time zone is identified as the Africa/Tripoli time zone from the IANA tz database. |
| `Africa/Tunis` | The time zone is identified as the Africa/Tunis time zone from the IANA tz database. |
| `Africa/Windhoek` | The time zone is identified as the Africa/Windhoek time zone from the IANA tz database. |
| `America/Adak` | The time zone is identified as the America/Adak time zone from the IANA tz database. |
| `America/Anchorage` | The time zone is identified as the America/Anchorage time zone from the IANA tz database. |
| `America/Anguilla` | The time zone is identified as the America/Anguilla time zone from the IANA tz database. |
| `America/Antigua` | The time zone is identified as the America/Antigua time zone from the IANA tz database. |
| `America/Araguaina` | The time zone is identified as the America/Araguaina time zone from the IANA tz database. |
| `America/Argentina/Buenos_Aires` | The time zone is identified as the America/Argentina/Buenos_Aires time zone from the IANA tz database. |
| `America/Argentina/Catamarca` | The time zone is identified as the America/Argentina/Catamarca time zone from the IANA tz database. |
| `America/Argentina/ComodRivadavia` | The time zone is identified as the America/Argentina/ComodRivadavia time zone from the IANA tz database. |
| `America/Argentina/Cordoba` | The time zone is identified as the America/Argentina/Cordoba time zone from the IANA tz database. |
| `America/Argentina/Jujuy` | The time zone is identified as the America/Argentina/Jujuy time zone from the IANA tz database. |
| `America/Argentina/La_Rioja` | The time zone is identified as the America/Argentina/La_Rioja time zone from the IANA tz database. |
| `America/Argentina/Mendoza` | The time zone is identified as the America/Argentina/Mendoza time zone from the IANA tz database. |
| `America/Argentina/Rio_Gallegos` | The time zone is identified as the America/Argentina/Rio_Gallegos time zone from the IANA tz database. |
| `America/Argentina/Salta` | The time zone is identified as the America/Argentina/Salta time zone from the IANA tz database. |
| `America/Argentina/San_Juan` | The time zone is identified as the America/Argentina/San_Juan time zone from the IANA tz database. |
| `America/Argentina/San_Luis` | The time zone is identified as the America/Argentina/San_Luis time zone from the IANA tz database. |
| `America/Argentina/Tucuman` | The time zone is identified as the America/Argentina/Tucuman time zone from the IANA tz database. |
| `America/Argentina/Ushuaia` | The time zone is identified as the America/Argentina/Ushuaia time zone from the IANA tz database. |
| `America/Aruba` | The time zone is identified as the America/Aruba time zone from the IANA tz database. |
| `America/Asuncion` | The time zone is identified as the America/Asuncion time zone from the IANA tz database. |
| `America/Atikokan` | The time zone is identified as the America/Atikokan time zone from the IANA tz database. |
| `America/Atka` | The time zone is identified as the America/Atka time zone from the IANA tz database. |
| `America/Bahia` | The time zone is identified as the America/Bahia time zone from the IANA tz database. |
| `America/Bahia_Banderas` | The time zone is identified as the America/Bahia_Banderas time zone from the IANA tz database. |
| `America/Barbados` | The time zone is identified as the America/Barbados time zone from the IANA tz database. |
| `America/Belem` | The time zone is identified as the America/Belem time zone from the IANA tz database. |
| `America/Belize` | The time zone is identified as the America/Belize time zone from the IANA tz database. |
| `America/Blanc-Sablon` | The time zone is identified as the America/Blanc-Sablon time zone from the IANA tz database. |
| `America/Boa_Vista` | The time zone is identified as the America/Boa_Vista time zone from the IANA tz database. |
| `America/Bogota` | The time zone is identified as the America/Bogota time zone from the IANA tz database. |
| `America/Boise` | The time zone is identified as the America/Boise time zone from the IANA tz database. |
| `America/Buenos_Aires` | The time zone is identified as the America/Buenos_Aires time zone from the IANA tz database. |
| `America/Cambridge_Bay` | The time zone is identified as the America/Cambridge_Bay time zone from the IANA tz database. |
| `America/Campo_Grande` | The time zone is identified as the America/Campo_Grande time zone from the IANA tz database. |
| `America/Cancun` | The time zone is identified as the America/Cancun time zone from the IANA tz database. |
| `America/Caracas` | The time zone is identified as the America/Caracas time zone from the IANA tz database. |
| `America/Catamarca` | The time zone is identified as the America/Catamarca time zone from the IANA tz database. |
| `America/Cayenne` | The time zone is identified as the America/Cayenne time zone from the IANA tz database. |
| `America/Cayman` | The time zone is identified as the America/Cayman time zone from the IANA tz database. |
| `America/Chicago` | The time zone is identified as the America/Chicago time zone from the IANA tz database. |
| `America/Chihuahua` | The time zone is identified as the America/Chihuahua time zone from the IANA tz database. |
| `America/Ciudad_Juarez` | The time zone is identified as the America/Ciudad_Juarez time zone from the IANA tz database. |
| `America/Coral_Harbour` | The time zone is identified as the America/Coral_Harbour time zone from the IANA tz database. |
| `America/Cordoba` | The time zone is identified as the America/Cordoba time zone from the IANA tz database. |
| `America/Costa_Rica` | The time zone is identified as the America/Costa_Rica time zone from the IANA tz database. |
| `America/Creston` | The time zone is identified as the America/Creston time zone from the IANA tz database. |
| `America/Cuiaba` | The time zone is identified as the America/Cuiaba time zone from the IANA tz database. |
| `America/Curacao` | The time zone is identified as the America/Curacao time zone from the IANA tz database. |
| `America/Danmarkshavn` | The time zone is identified as the America/Danmarkshavn time zone from the IANA tz database. |
| `America/Dawson` | The time zone is identified as the America/Dawson time zone from the IANA tz database. |
| `America/Dawson_Creek` | The time zone is identified as the America/Dawson_Creek time zone from the IANA tz database. |
| `America/Denver` | The time zone is identified as the America/Denver time zone from the IANA tz database. |
| `America/Detroit` | The time zone is identified as the America/Detroit time zone from the IANA tz database. |
| `America/Dominica` | The time zone is identified as the America/Dominica time zone from the IANA tz database. |
| `America/Edmonton` | The time zone is identified as the America/Edmonton time zone from the IANA tz database. |
| `America/Eirunepe` | The time zone is identified as the America/Eirunepe time zone from the IANA tz database. |
| `America/El_Salvador` | The time zone is identified as the America/El_Salvador time zone from the IANA tz database. |
| `America/Ensenada` | The time zone is identified as the America/Ensenada time zone from the IANA tz database. |
| `America/Fort_Nelson` | The time zone is identified as the America/Fort_Nelson time zone from the IANA tz database. |
| `America/Fort_Wayne` | The time zone is identified as the America/Fort_Wayne time zone from the IANA tz database. |
| `America/Fortaleza` | The time zone is identified as the America/Fortaleza time zone from the IANA tz database. |
| `America/Glace_Bay` | The time zone is identified as the America/Glace_Bay time zone from the IANA tz database. |
| `America/Godthab` | The time zone is identified as the America/Godthab time zone from the IANA tz database. |
| `America/Goose_Bay` | The time zone is identified as the America/Goose_Bay time zone from the IANA tz database. |
| `America/Grand_Turk` | The time zone is identified as the America/Grand_Turk time zone from the IANA tz database. |
| `America/Grenada` | The time zone is identified as the America/Grenada time zone from the IANA tz database. |
| `America/Guadeloupe` | The time zone is identified as the America/Guadeloupe time zone from the IANA tz database. |
| `America/Guatemala` | The time zone is identified as the America/Guatemala time zone from the IANA tz database. |
| `America/Guayaquil` | The time zone is identified as the America/Guayaquil time zone from the IANA tz database. |
| `America/Guyana` | The time zone is identified as the America/Guyana time zone from the IANA tz database. |
| `America/Halifax` | The time zone is identified as the America/Halifax time zone from the IANA tz database. |
| `America/Havana` | The time zone is identified as the America/Havana time zone from the IANA tz database. |
| `America/Hermosillo` | The time zone is identified as the America/Hermosillo time zone from the IANA tz database. |
| `America/Indiana/Indianapolis` | The time zone is identified as the America/Indiana/Indianapolis time zone from the IANA tz database. |
| `America/Indiana/Knox` | The time zone is identified as the America/Indiana/Knox time zone from the IANA tz database. |
| `America/Indiana/Marengo` | The time zone is identified as the America/Indiana/Marengo time zone from the IANA tz database. |
| `America/Indiana/Petersburg` | The time zone is identified as the America/Indiana/Petersburg time zone from the IANA tz database. |
| `America/Indiana/Tell_City` | The time zone is identified as the America/Indiana/Tell_City time zone from the IANA tz database. |
| `America/Indiana/Vevay` | The time zone is identified as the America/Indiana/Vevay time zone from the IANA tz database. |
| `America/Indiana/Vincennes` | The time zone is identified as the America/Indiana/Vincennes time zone from the IANA tz database. |
| `America/Indiana/Winamac` | The time zone is identified as the America/Indiana/Winamac time zone from the IANA tz database. |
| `America/Indianapolis` | The time zone is identified as the America/Indianapolis time zone from the IANA tz database. |
| `America/Inuvik` | The time zone is identified as the America/Inuvik time zone from the IANA tz database. |
| `America/Iqaluit` | The time zone is identified as the America/Iqaluit time zone from the IANA tz database. |
| `America/Jamaica` | The time zone is identified as the America/Jamaica time zone from the IANA tz database. |
| `America/Jujuy` | The time zone is identified as the America/Jujuy time zone from the IANA tz database. |
| `America/Juneau` | The time zone is identified as the America/Juneau time zone from the IANA tz database. |
| `America/Kentucky/Louisville` | The time zone is identified as the America/Kentucky/Louisville time zone from the IANA tz database. |
| `America/Kentucky/Monticello` | The time zone is identified as the America/Kentucky/Monticello time zone from the IANA tz database. |
| `America/Knox_IN` | The time zone is identified as the America/Knox_IN time zone from the IANA tz database. |
| `America/Kralendijk` | The time zone is identified as the America/Kralendijk time zone from the IANA tz database. |
| `America/La_Paz` | The time zone is identified as the America/La_Paz time zone from the IANA tz database. |
| `America/Lima` | The time zone is identified as the America/Lima time zone from the IANA tz database. |
| `America/Los_Angeles` | The time zone is identified as the America/Los_Angeles time zone from the IANA tz database. |
| `America/Louisville` | The time zone is identified as the America/Louisville time zone from the IANA tz database. |
| `America/Lower_Princes` | The time zone is identified as the America/Lower_Princes time zone from the IANA tz database. |
| `America/Maceio` | The time zone is identified as the America/Maceio time zone from the IANA tz database. |
| `America/Managua` | The time zone is identified as the America/Managua time zone from the IANA tz database. |
| `America/Manaus` | The time zone is identified as the America/Manaus time zone from the IANA tz database. |
| `America/Marigot` | The time zone is identified as the America/Marigot time zone from the IANA tz database. |
| `America/Martinique` | The time zone is identified as the America/Martinique time zone from the IANA tz database. |
| `America/Matamoros` | The time zone is identified as the America/Matamoros time zone from the IANA tz database. |
| `America/Mazatlan` | The time zone is identified as the America/Mazatlan time zone from the IANA tz database. |
| `America/Mendoza` | The time zone is identified as the America/Mendoza time zone from the IANA tz database. |
| `America/Menominee` | The time zone is identified as the America/Menominee time zone from the IANA tz database. |
| `America/Merida` | The time zone is identified as the America/Merida time zone from the IANA tz database. |
| `America/Metlakatla` | The time zone is identified as the America/Metlakatla time zone from the IANA tz database. |
| `America/Mexico_City` | The time zone is identified as the America/Mexico_City time zone from the IANA tz database. |
| `America/Miquelon` | The time zone is identified as the America/Miquelon time zone from the IANA tz database. |
| `America/Moncton` | The time zone is identified as the America/Moncton time zone from the IANA tz database. |
| `America/Monterrey` | The time zone is identified as the America/Monterrey time zone from the IANA tz database. |
| `America/Montevideo` | The time zone is identified as the America/Montevideo time zone from the IANA tz database. |
| `America/Montreal` | The time zone is identified as the America/Montreal time zone from the IANA tz database. |
| `America/Montserrat` | The time zone is identified as the America/Montserrat time zone from the IANA tz database. |
| `America/Nassau` | The time zone is identified as the America/Nassau time zone from the IANA tz database. |
| `America/New_York` | The time zone is identified as the America/New_York time zone from the IANA tz database. |
| `America/Nipigon` | The time zone is identified as the America/Nipigon time zone from the IANA tz database. |
| `America/Nome` | The time zone is identified as the America/Nome time zone from the IANA tz database. |
| `America/Noronha` | The time zone is identified as the America/Noronha time zone from the IANA tz database. |
| `America/North_Dakota/Beulah` | The time zone is identified as the America/North_Dakota/Beulah time zone from the IANA tz database. |
| `America/North_Dakota/Center` | The time zone is identified as the America/North_Dakota/Center time zone from the IANA tz database. |
| `America/North_Dakota/New_Salem` | The time zone is identified as the America/North_Dakota/New_Salem time zone from the IANA tz database. |
| `America/Nuuk` | The time zone is identified as the America/Nuuk time zone from the IANA tz database. |
| `America/Ojinaga` | The time zone is identified as the America/Ojinaga time zone from the IANA tz database. |
| `America/Panama` | The time zone is identified as the America/Panama time zone from the IANA tz database. |
| `America/Pangnirtung` | The time zone is identified as the America/Pangnirtung time zone from the IANA tz database. |
| `America/Paramaribo` | The time zone is identified as the America/Paramaribo time zone from the IANA tz database. |
| `America/Phoenix` | The time zone is identified as the America/Phoenix time zone from the IANA tz database. |
| `America/Port_of_Spain` | The time zone is identified as the America/Port_of_Spain time zone from the IANA tz database. |
| `America/Port-au-Prince` | The time zone is identified as the America/Port-au-Prince time zone from the IANA tz database. |
| `America/Porto_Acre` | The time zone is identified as the America/Porto_Acre time zone from the IANA tz database. |
| `America/Porto_Velho` | The time zone is identified as the America/Porto_Velho time zone from the IANA tz database. |
| `America/Puerto_Rico` | The time zone is identified as the America/Puerto_Rico time zone from the IANA tz database. |
| `America/Punta_Arenas` | The time zone is identified as the America/Punta_Arenas time zone from the IANA tz database. |
| `America/Rainy_River` | The time zone is identified as the America/Rainy_River time zone from the IANA tz database. |
| `America/Rankin_Inlet` | The time zone is identified as the America/Rankin_Inlet time zone from the IANA tz database. |
| `America/Recife` | The time zone is identified as the America/Recife time zone from the IANA tz database. |
| `America/Regina` | The time zone is identified as the America/Regina time zone from the IANA tz database. |
| `America/Resolute` | The time zone is identified as the America/Resolute time zone from the IANA tz database. |
| `America/Rio_Branco` | The time zone is identified as the America/Rio_Branco time zone from the IANA tz database. |
| `America/Rosario` | The time zone is identified as the America/Rosario time zone from the IANA tz database. |
| `America/Santa_Isabel` | The time zone is identified as the America/Santa_Isabel time zone from the IANA tz database. |
| `America/Santarem` | The time zone is identified as the America/Santarem time zone from the IANA tz database. |
| `America/Santiago` | The time zone is identified as the America/Santiago time zone from the IANA tz database. |
| `America/Santo_Domingo` | The time zone is identified as the America/Santo_Domingo time zone from the IANA tz database. |
| `America/Sao_Paulo` | The time zone is identified as the America/Sao_Paulo time zone from the IANA tz database. |
| `America/Scoresbysund` | The time zone is identified as the America/Scoresbysund time zone from the IANA tz database. |
| `America/Shiprock` | The time zone is identified as the America/Shiprock time zone from the IANA tz database. |
| `America/Sitka` | The time zone is identified as the America/Sitka time zone from the IANA tz database. |
| `America/St_Barthelemy` | The time zone is identified as the America/St_Barthelemy time zone from the IANA tz database. |
| `America/St_Johns` | The time zone is identified as the America/St_Johns time zone from the IANA tz database. |
| `America/St_Kitts` | The time zone is identified as the America/St_Kitts time zone from the IANA tz database. |
| `America/St_Lucia` | The time zone is identified as the America/St_Lucia time zone from the IANA tz database. |
| `America/St_Thomas` | The time zone is identified as the America/St_Thomas time zone from the IANA tz database. |
| `America/St_Vincent` | The time zone is identified as the America/St_Vincent time zone from the IANA tz database. |
| `America/Swift_Current` | The time zone is identified as the America/Swift_Current time zone from the IANA tz database. |
| `America/Tegucigalpa` | The time zone is identified as the America/Tegucigalpa time zone from the IANA tz database. |
| `America/Thule` | The time zone is identified as the America/Thule time zone from the IANA tz database. |
| `America/Thunder_Bay` | The time zone is identified as the America/Thunder_Bay time zone from the IANA tz database. |
| `America/Tijuana` | The time zone is identified as the America/Tijuana time zone from the IANA tz database. |
| `America/Toronto` | The time zone is identified as the America/Toronto time zone from the IANA tz database. |
| `America/Tortola` | The time zone is identified as the America/Tortola time zone from the IANA tz database. |
| `America/Vancouver` | The time zone is identified as the America/Vancouver time zone from the IANA tz database. |
| `America/Virgin` | The time zone is identified as the America/Virgin time zone from the IANA tz database. |
| `America/Whitehorse` | The time zone is identified as the America/Whitehorse time zone from the IANA tz database. |
| `America/Winnipeg` | The time zone is identified as the America/Winnipeg time zone from the IANA tz database. |
| `America/Yakutat` | The time zone is identified as the America/Yakutat time zone from the IANA tz database. |
| `America/Yellowknife` | The time zone is identified as the America/Yellowknife time zone from the IANA tz database. |
| `Antarctica/Casey` | The time zone is identified as the Antarctica/Casey time zone from the IANA tz database. |
| `Antarctica/Davis` | The time zone is identified as the Antarctica/Davis time zone from the IANA tz database. |
| `Antarctica/DumontDUrville` | The time zone is identified as the Antarctica/DumontDUrville time zone from the IANA tz database. |
| `Antarctica/Macquarie` | The time zone is identified as the Antarctica/Macquarie time zone from the IANA tz database. |
| `Antarctica/Mawson` | The time zone is identified as the Antarctica/Mawson time zone from the IANA tz database. |
| `Antarctica/McMurdo` | The time zone is identified as the Antarctica/McMurdo time zone from the IANA tz database. |
| `Antarctica/Palmer` | The time zone is identified as the Antarctica/Palmer time zone from the IANA tz database. |
| `Antarctica/Rothera` | The time zone is identified as the Antarctica/Rothera time zone from the IANA tz database. |
| `Antarctica/South_Pole` | The time zone is identified as the Antarctica/South_Pole time zone from the IANA tz database. |
| `Antarctica/Syowa` | The time zone is identified as the Antarctica/Syowa time zone from the IANA tz database. |
| `Antarctica/Troll` | The time zone is identified as the Antarctica/Troll time zone from the IANA tz database. |
| `Antarctica/Vostok` | The time zone is identified as the Antarctica/Vostok time zone from the IANA tz database. |
| `Arctic/Longyearbyen` | The time zone is identified as the Arctic/Longyearbyen time zone from the IANA tz database. |
| `Asia/Aden` | The time zone is identified as the Asia/Aden time zone from the IANA tz database. |
| `Asia/Almaty` | The time zone is identified as the Asia/Almaty time zone from the IANA tz database. |
| `Asia/Amman` | The time zone is identified as the Asia/Amman time zone from the IANA tz database. |
| `Asia/Anadyr` | The time zone is identified as the Asia/Anadyr time zone from the IANA tz database. |
| `Asia/Aqtau` | The time zone is identified as the Asia/Aqtau time zone from the IANA tz database. |
| `Asia/Aqtobe` | The time zone is identified as the Asia/Aqtobe time zone from the IANA tz database. |
| `Asia/Ashgabat` | The time zone is identified as the Asia/Ashgabat time zone from the IANA tz database. |
| `Asia/Ashkhabad` | The time zone is identified as the Asia/Ashkhabad time zone from the IANA tz database. |
| `Asia/Atyrau` | The time zone is identified as the Asia/Atyrau time zone from the IANA tz database. |
| `Asia/Baghdad` | The time zone is identified as the Asia/Baghdad time zone from the IANA tz database. |
| `Asia/Bahrain` | The time zone is identified as the Asia/Bahrain time zone from the IANA tz database. |
| `Asia/Baku` | The time zone is identified as the Asia/Baku time zone from the IANA tz database. |
| `Asia/Bangkok` | The time zone is identified as the Asia/Bangkok time zone from the IANA tz database. |
| `Asia/Barnaul` | The time zone is identified as the Asia/Barnaul time zone from the IANA tz database. |
| `Asia/Beirut` | The time zone is identified as the Asia/Beirut time zone from the IANA tz database. |
| `Asia/Bishkek` | The time zone is identified as the Asia/Bishkek time zone from the IANA tz database. |
| `Asia/Brunei` | The time zone is identified as the Asia/Brunei time zone from the IANA tz database. |
| `Asia/Calcutta` | The time zone is identified as the Asia/Calcutta time zone from the IANA tz database. |
| `Asia/Chita` | The time zone is identified as the Asia/Chita time zone from the IANA tz database. |
| `Asia/Choibalsan` | The time zone is identified as the Asia/Choibalsan time zone from the IANA tz database. |
| `Asia/Chongqing` | The time zone is identified as the Asia/Chongqing time zone from the IANA tz database. |
| `Asia/Chungking` | The time zone is identified as the Asia/Chungking time zone from the IANA tz database. |
| `Asia/Colombo` | The time zone is identified as the Asia/Colombo time zone from the IANA tz database. |
| `Asia/Dacca` | The time zone is identified as the Asia/Dacca time zone from the IANA tz database. |
| `Asia/Damascus` | The time zone is identified as the Asia/Damascus time zone from the IANA tz database. |
| `Asia/Dhaka` | The time zone is identified as the Asia/Dhaka time zone from the IANA tz database. |
| `Asia/Dili` | The time zone is identified as the Asia/Dili time zone from the IANA tz database. |
| `Asia/Dubai` | The time zone is identified as the Asia/Dubai time zone from the IANA tz database. |
| `Asia/Dushanbe` | The time zone is identified as the Asia/Dushanbe time zone from the IANA tz database. |
| `Asia/Famagusta` | The time zone is identified as the Asia/Famagusta time zone from the IANA tz database. |
| `Asia/Gaza` | The time zone is identified as the Asia/Gaza time zone from the IANA tz database. |
| `Asia/Harbin` | The time zone is identified as the Asia/Harbin time zone from the IANA tz database. |
| `Asia/Hebron` | The time zone is identified as the Asia/Hebron time zone from the IANA tz database. |
| `Asia/Ho_Chi_Minh` | The time zone is identified as the Asia/Ho_Chi_Minh time zone from the IANA tz database. |
| `Asia/Hong_Kong` | The time zone is identified as the Asia/Hong_Kong time zone from the IANA tz database. |
| `Asia/Hovd` | The time zone is identified as the Asia/Hovd time zone from the IANA tz database. |
| `Asia/Irkutsk` | The time zone is identified as the Asia/Irkutsk time zone from the IANA tz database. |
| `Asia/Istanbul` | The time zone is identified as the Asia/Istanbul time zone from the IANA tz database. |
| `Asia/Jakarta` | The time zone is identified as the Asia/Jakarta time zone from the IANA tz database. |
| `Asia/Jayapura` | The time zone is identified as the Asia/Jayapura time zone from the IANA tz database. |
| `Asia/Jerusalem` | The time zone is identified as the Asia/Jerusalem time zone from the IANA tz database. |
| `Asia/Kabul` | The time zone is identified as the Asia/Kabul time zone from the IANA tz database. |
| `Asia/Kamchatka` | The time zone is identified as the Asia/Kamchatka time zone from the IANA tz database. |
| `Asia/Karachi` | The time zone is identified as the Asia/Karachi time zone from the IANA tz database. |
| `Asia/Kashgar` | The time zone is identified as the Asia/Kashgar time zone from the IANA tz database. |
| `Asia/Kathmandu` | The time zone is identified as the Asia/Kathmandu time zone from the IANA tz database. |
| `Asia/Katmandu` | The time zone is identified as the Asia/Katmandu time zone from the IANA tz database. |
| `Asia/Khandyga` | The time zone is identified as the Asia/Khandyga time zone from the IANA tz database. |
| `Asia/Kolkata` | The time zone is identified as the Asia/Kolkata time zone from the IANA tz database. |
| `Asia/Krasnoyarsk` | The time zone is identified as the Asia/Krasnoyarsk time zone from the IANA tz database. |
| `Asia/Kuala_Lumpur` | The time zone is identified as the Asia/Kuala_Lumpur time zone from the IANA tz database. |
| `Asia/Kuching` | The time zone is identified as the Asia/Kuching time zone from the IANA tz database. |
| `Asia/Kuwait` | The time zone is identified as the Asia/Kuwait time zone from the IANA tz database. |
| `Asia/Macao` | The time zone is identified as the Asia/Macao time zone from the IANA tz database. |
| `Asia/Macau` | The time zone is identified as the Asia/Macau time zone from the IANA tz database. |
| `Asia/Magadan` | The time zone is identified as the Asia/Magadan time zone from the IANA tz database. |
| `Asia/Makassar` | The time zone is identified as the Asia/Makassar time zone from the IANA tz database. |
| `Asia/Manila` | The time zone is identified as the Asia/Manila time zone from the IANA tz database. |
| `Asia/Muscat` | The time zone is identified as the Asia/Muscat time zone from the IANA tz database. |
| `Asia/Nicosia` | The time zone is identified as the Asia/Nicosia time zone from the IANA tz database. |
| `Asia/Novokuznetsk` | The time zone is identified as the Asia/Novokuznetsk time zone from the IANA tz database. |
| `Asia/Novosibirsk` | The time zone is identified as the Asia/Novosibirsk time zone from the IANA tz database. |
| `Asia/Omsk` | The time zone is identified as the Asia/Omsk time zone from the IANA tz database. |
| `Asia/Oral` | The time zone is identified as the Asia/Oral time zone from the IANA tz database. |
| `Asia/Phnom_Penh` | The time zone is identified as the Asia/Phnom_Penh time zone from the IANA tz database. |
| `Asia/Pontianak` | The time zone is identified as the Asia/Pontianak time zone from the IANA tz database. |
| `Asia/Pyongyang` | The time zone is identified as the Asia/Pyongyang time zone from the IANA tz database. |
| `Asia/Qatar` | The time zone is identified as the Asia/Qatar time zone from the IANA tz database. |
| `Asia/Qostanay` | The time zone is identified as the Asia/Qostanay time zone from the IANA tz database. |
| `Asia/Qyzylorda` | The time zone is identified as the Asia/Qyzylorda time zone from the IANA tz database. |
| `Asia/Rangoon` | The time zone is identified as the Asia/Rangoon time zone from the IANA tz database. |
| `Asia/Riyadh` | The time zone is identified as the Asia/Riyadh time zone from the IANA tz database. |
| `Asia/Saigon` | The time zone is identified as the Asia/Saigon time zone from the IANA tz database. |
| `Asia/Sakhalin` | The time zone is identified as the Asia/Sakhalin time zone from the IANA tz database. |
| `Asia/Samarkand` | The time zone is identified as the Asia/Samarkand time zone from the IANA tz database. |
| `Asia/Seoul` | The time zone is identified as the Asia/Seoul time zone from the IANA tz database. |
| `Asia/Shanghai` | The time zone is identified as the Asia/Shanghai time zone from the IANA tz database. |
| `Asia/Singapore` | The time zone is identified as the Asia/Singapore time zone from the IANA tz database. |
| `Asia/Srednekolymsk` | The time zone is identified as the Asia/Srednekolymsk time zone from the IANA tz database. |
| `Asia/Taipei` | The time zone is identified as the Asia/Taipei time zone from the IANA tz database. |
| `Asia/Tashkent` | The time zone is identified as the Asia/Tashkent time zone from the IANA tz database. |
| `Asia/Tbilisi` | The time zone is identified as the Asia/Tbilisi time zone from the IANA tz database. |
| `Asia/Tehran` | The time zone is identified as the Asia/Tehran time zone from the IANA tz database. |
| `Asia/Tel_Aviv` | The time zone is identified as the Asia/Tel_Aviv time zone from the IANA tz database. |
| `Asia/Thimbu` | The time zone is identified as the Asia/Thimbu time zone from the IANA tz database. |
| `Asia/Thimphu` | The time zone is identified as the Asia/Thimphu time zone from the IANA tz database. |
| `Asia/Tokyo` | The time zone is identified as the Asia/Tokyo time zone from the IANA tz database. |
| `Asia/Tomsk` | The time zone is identified as the Asia/Tomsk time zone from the IANA tz database. |
| `Asia/Ujung_Pandang` | The time zone is identified as the Asia/Ujung_Pandang time zone from the IANA tz database. |
| `Asia/Ulaanbaatar` | The time zone is identified as the Asia/Ulaanbaatar time zone from the IANA tz database. |
| `Asia/Ulan_Bator` | The time zone is identified as the Asia/Ulan_Bator time zone from the IANA tz database. |
| `Asia/Urumqi` | The time zone is identified as the Asia/Urumqi time zone from the IANA tz database. |
| `Asia/Ust-Nera` | The time zone is identified as the Asia/Ust-Nera time zone from the IANA tz database. |
| `Asia/Vientiane` | The time zone is identified as the Asia/Vientiane time zone from the IANA tz database. |
| `Asia/Vladivostok` | The time zone is identified as the Asia/Vladivostok time zone from the IANA tz database. |
| `Asia/Yakutsk` | The time zone is identified as the Asia/Yakutsk time zone from the IANA tz database. |
| `Asia/Yangon` | The time zone is identified as the Asia/Yangon time zone from the IANA tz database. |
| `Asia/Yekaterinburg` | The time zone is identified as the Asia/Yekaterinburg time zone from the IANA tz database. |
| `Asia/Yerevan` | The time zone is identified as the Asia/Yerevan time zone from the IANA tz database. |
| `Atlantic/Azores` | The time zone is identified as the Atlantic/Azores time zone from the IANA tz database. |
| `Atlantic/Bermuda` | The time zone is identified as the Atlantic/Bermuda time zone from the IANA tz database. |
| `Atlantic/Canary` | The time zone is identified as the Atlantic/Canary time zone from the IANA tz database. |
| `Atlantic/Cape_Verde` | The time zone is identified as the Atlantic/Cape_Verde time zone from the IANA tz database. |
| `Atlantic/Faeroe` | The time zone is identified as the Atlantic/Faeroe time zone from the IANA tz database. |
| `Atlantic/Faroe` | The time zone is identified as the Atlantic/Faroe time zone from the IANA tz database. |
| `Atlantic/Jan_Mayen` | The time zone is identified as the Atlantic/Jan_Mayen time zone from the IANA tz database. |
| `Atlantic/Madeira` | The time zone is identified as the Atlantic/Madeira time zone from the IANA tz database. |
| `Atlantic/Reykjavik` | The time zone is identified as the Atlantic/Reykjavik time zone from the IANA tz database. |
| `Atlantic/South_Georgia` | The time zone is identified as the Atlantic/South_Georgia time zone from the IANA tz database. |
| `Atlantic/St_Helena` | The time zone is identified as the Atlantic/St_Helena time zone from the IANA tz database. |
| `Atlantic/Stanley` | The time zone is identified as the Atlantic/Stanley time zone from the IANA tz database. |
| `Australia/ACT` | The time zone is identified as the Australia/ACT time zone from the IANA tz database. |
| `Australia/Adelaide` | The time zone is identified as the Australia/Adelaide time zone from the IANA tz database. |
| `Australia/Brisbane` | The time zone is identified as the Australia/Brisbane time zone from the IANA tz database. |
| `Australia/Broken_Hill` | The time zone is identified as the Australia/Broken_Hill time zone from the IANA tz database. |
| `Australia/Canberra` | The time zone is identified as the Australia/Canberra time zone from the IANA tz database. |
| `Australia/Currie` | The time zone is identified as the Australia/Currie time zone from the IANA tz database. |
| `Australia/Darwin` | The time zone is identified as the Australia/Darwin time zone from the IANA tz database. |
| `Australia/Eucla` | The time zone is identified as the Australia/Eucla time zone from the IANA tz database. |
| `Australia/Hobart` | The time zone is identified as the Australia/Hobart time zone from the IANA tz database. |
| `Australia/LHI` | The time zone is identified as the Australia/LHI time zone from the IANA tz database. |
| `Australia/Lindeman` | The time zone is identified as the Australia/Lindeman time zone from the IANA tz database. |
| `Australia/Lord_Howe` | The time zone is identified as the Australia/Lord_Howe time zone from the IANA tz database. |
| `Australia/Melbourne` | The time zone is identified as the Australia/Melbourne time zone from the IANA tz database. |
| `Australia/North` | The time zone is identified as the Australia/North time zone from the IANA tz database. |
| `Australia/NSW` | The time zone is identified as the Australia/NSW time zone from the IANA tz database. |
| `Australia/Perth` | The time zone is identified as the Australia/Perth time zone from the IANA tz database. |
| `Australia/Queensland` | The time zone is identified as the Australia/Queensland time zone from the IANA tz database. |
| `Australia/South` | The time zone is identified as the Australia/South time zone from the IANA tz database. |
| `Australia/Sydney` | The time zone is identified as the Australia/Sydney time zone from the IANA tz database. |
| `Australia/Tasmania` | The time zone is identified as the Australia/Tasmania time zone from the IANA tz database. |
| `Australia/Victoria` | The time zone is identified as the Australia/Victoria time zone from the IANA tz database. |
| `Australia/West` | The time zone is identified as the Australia/West time zone from the IANA tz database. |
| `Australia/Yancowinna` | The time zone is identified as the Australia/Yancowinna time zone from the IANA tz database. |
| `Brazil/Acre` | The time zone is identified as the Brazil/Acre time zone from the IANA tz database. |
| `Brazil/DeNoronha` | The time zone is identified as the Brazil/DeNoronha time zone from the IANA tz database. |
| `Brazil/East` | The time zone is identified as the Brazil/East time zone from the IANA tz database. |
| `Brazil/West` | The time zone is identified as the Brazil/West time zone from the IANA tz database. |
| `Canada/Atlantic` | The time zone is identified as the Canada/Atlantic time zone from the IANA tz database. |
| `Canada/Central` | The time zone is identified as the Canada/Central time zone from the IANA tz database. |
| `Canada/Eastern` | The time zone is identified as the Canada/Eastern time zone from the IANA tz database. |
| `Canada/Mountain` | The time zone is identified as the Canada/Mountain time zone from the IANA tz database. |
| `Canada/Newfoundland` | The time zone is identified as the Canada/Newfoundland time zone from the IANA tz database. |
| `Canada/Pacific` | The time zone is identified as the Canada/Pacific time zone from the IANA tz database. |
| `Canada/Saskatchewan` | The time zone is identified as the Canada/Saskatchewan time zone from the IANA tz database. |
| `Canada/Yukon` | The time zone is identified as the Canada/Yukon time zone from the IANA tz database. |

### IncomeIncludes

6 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/IncomeIncludes/)

| Value | Definition |
|---|---|
| `Laundry` | The income amount includes income from laundry facilities. |
| `Parking` | The income amount includes income from parking. |
| `Recreation` | The income amount includes income from charging for recreation facilities. |
| `Rent Only` | The income amount includes income from only the rent charged to the tenants. |
| `RV Storage` | The income amount includes income from charging for RV storage. |
| `Storage` | The income amount includes income from charging for general storage. |

### InteriorOrRoomFeatures

53 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/InteriorOrRoomFeatures/)

| Value | Definition |
|---|---|
| `Bar` | A built-in or movable fixture for the storage, preparation, serving and/or consumption of drinks. |
| `Beamed Ceilings` | A property that has exposed beams across the ceiling of a room or rooms. |
| `Bidet` | A type of sink designed to wash the undercarriage of the human body. |
| `Bookcases` | Shelves for books or other objects that may or may not be built into the property. |
| `Breakfast Bar` | A surface designed for eating, which is typically smaller than a dining table and attached to another kitchen surface. |
| `Built-in Features` | Some features are physically attached to the structure. |
| `Cathedral Ceiling(s)` | A type of vaulted ceiling that is typically higher than normal ceilings and has a slant or curve to reach its uppermost point, which tends to be equal distance from the two shorter walls in the room. |
| `Cedar Closet(s)` | A closet that is partially or fully lined with cedarwood. |
| `Ceiling Fan(s)` | A fan is mounted from the ceiling in a room or multiple rooms. |
| `Central Vacuum` | A built-in vacuum that typically consists of a power/collection unit that is typically installed in a garage or closet, tubing from the power unit to rooms throughout the house and including wall-moun… |
| `Chandelier` | A decorative lighting fixture that typically branches out with several lights (or candles) with other decorative components such as glass, crystal or other reflective or light-enhancing materials. |
| `Coffered Ceiling(s)` | A ceiling with multiple decorative indentations, trays or sunken panels. |
| `Crown Molding` | A decorative trim covering the seam between the ceiling and walls. |
| `Double Vanity` | Bathroom cabinetry with two built-in sinks. |
| `Dry Bar` | A built-in or movable fixture for the storage, preparation, serving and consumption of drinks that does not have a water supply or sink. |
| `Dumbwaiter` | A small elevator, typically for carrying food between floors in a structure. |
| `Eat-in Kitchen` | A kitchen that has been designed to accommodate dining. |
| `Elevator` | A platform or compartment housed within a shaft for raising or lowering people or objects. |
| `Entrance Foyer` | A room or hall at the entrance leading to other parts of the structure. |
| `Granite Counters` | The counters are made of a type of granite stone. |
| `High Ceilings` | The ceiling height is greater than what might be considered a normal celling height. |
| `High Speed Internet` | The property has access to high-speed internet service but may or may not be wired and/or connected to that service. |
| `His and Hers Closets` | The room or rooms have two separate closets. |
| `In-Law Floorplan` | The structure has an area within that has the characteristics of an independent apartment, typically with a living area, kitchen, bedroom and bathroom. |
| `Kitchen Island` | A separate counter surface in a kitchen that is not attached to other surfaces or to a wall. |
| `Laminate Counters` | The counters are covered with a laminate. |
| `Low Flow Plumbing Fixtures` | Some or all of the fixtures are designed to save water. |
| `Master Downstairs` | There is a primary bedroom on the main level of the structure. |
| `Natural Woodwork` | The property or room has features made from real wood. |
| `Open Floorplan` | A generic design term for a floor plan that makes use of large open spaces and avoids the use of small enclosed spaces. |
| `Other` | The room or interior has features other than those included on this list. |
| `Pantry` | A small room or closet where food, dishes and utensils are stored. |
| `Recessed Lighting` | A light fixture installed into a hollow opening in the ceiling. |
| `Sauna` | A small room or separate structure designed to produce heat to induce perspiration with wet steam (often poured over hot stones) or with dry heat. |
| `See Remarks` | See the remarks fields for additional information about the room or interior. |
| `Smart Camera(s)/Recording` | A camera or recording control unit that has convenience and energy-saving aspects. |
| `Smart Home` | A generic term for electronic automation of features such as lighting, heating/cooling, security and other amenities. |
| `Smart Light(s)` | A lighting control unit that has convenience and energy-saving aspects. |
| `Smart Thermostat` | A heating/cooling control unit that has convenience and energy-saving aspects. |
| `Soaking Tub` | A bathtub that is typically deeper and may be shorter than traditional tubs. |
| `Solar Tube(s)` | A reflective tube that extends from a light-gathering surface on the roof of the structure down into a room where the outside light is distributed. |
| `Sound System` | The property includes a sound system that typically includes in-wall wiring and recessed/built-in speakers and a built-in location for the amplifier and other audio equipment. |
| `Stone Counters` | The property or room has counters that are made of some type of stone. |
| `Storage` | The property or room has storage space. |
| `Tile Counters` | The property or room has counters that are made of some type of tile. |
| `Track Lighting` | A type of lighting where the light fixtures are mounted on a track allowing for adjustment of the position of the lights. |
| `Tray Ceiling(s)` | A ceiling with an inverted tray or recessed area, often rectangular, that adds depth and interest. |
| `Vaulted Ceiling(s)` | Derived from the Italian word "volta," is this is typically a high celling with no attic between the ceiling and the roof. |
| `Walk-In Closet(s)` | A closet that is a small room with an entryway. |
| `WaterSense Fixture(s)` | Water fixtures that are backed by independent, third-party certification and meet Environmental Protection Agency (EPA) specifications for water efficiency and performance. |
| `Wet Bar` | Commonly a built-in fixture for the storage, preparation, serving and/or consumption of drinks that has a faucet and sink. |
| `Wired for Data` | The property has been wired for data, typically Category 5 or 6 wiring for the support of Ethernet data communications. |
| `Wired for Sound` | The property has been wired for a built-in sound system. |

### LaborInformation

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LaborInformation/)

| Value | Definition |
|---|---|
| `Employee License Required` | Special licensing is required for employees. |
| `Non-Union` | A labor union is not currently established with the given business. |
| `Union` | A labor union is established with the given business. |

### LaundryFeatures

24 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LaundryFeatures/)

| Value | Definition |
|---|---|
| `Common Area` | Laundry features are in a common area. |
| `Electric Dryer Hookup` | The property has electric clothes dryer connections. |
| `Gas Dryer Hookup` | The property has gas clothes dryer connections. |
| `In Basement` | Laundry features are located in a basement. |
| `In Bathroom` | Laundry features are located in a bathroom. |
| `In Carport` | Laundry features are located in a carport. |
| `In Garage` | Laundry features are located in a garage. |
| `In Hall` | Laundry features are located in a hall. |
| `In Kitchen` | Laundry features are located in a kitchen. |
| `In Unit` | Laundry features are located in a unit. |
| `Inside` | Laundry features are located indoors. |
| `Laundry Chute` | The property has a laundry chute. |
| `Laundry Closet` | The property has a laundry closet. |
| `Laundry Room` | The property has a laundry room. |
| `Lower Level` | Laundry features are located on a lower level. |
| `Main Level` | Laundry features are located on the main level. |
| `Multiple Locations` | Laundry features are located in multiple locations. |
| `None` | There are no laundry features. |
| `Other` | There are laundry features other than those on this list. |
| `Outside` | Laundry features are located outside. |
| `See Remarks` | See remarks for additional information about laundry features. |
| `Sink` | The laundry area has a sink. |
| `Upper Level` | Laundry features are located on an upper level. |
| `Washer Hookup` | The property has a hookups for a clothes washer. |

### LeaseRenewalCompensation

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LeaseRenewalCompensation/)

| Value | Definition |
|---|---|
| `Call Listing Agent` | For details about additional selling office compensation for lease renewals, contact the listing agent. |
| `Call Listing Office` | For details about additional selling office compensation for lease renewals, contact the listing office. |
| `Commission Paid On Tenant Purchase` | Additional commission is paid in the event the tenant purchases the property. |
| `No Renewal Commission` | There is no additional commission if the tenant renews or extends the lease. |
| `Renewal Commission Paid` | There is additional commission paid if the tenant renews the lease. |

### LeaseTerm

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LeaseTerm/)

| Value | Definition |
|---|---|
| `12 Months` | The length of the lease is 12 months. |
| `24 Months` | The length of the lease is 24 months. |
| `6 Months` | The length of the lease is 6 months. |
| `Month To Month` | The length of the lease is month to month. |
| `Negotiable` | The length of the lease is negotiable. |
| `None` | There is no stated term to the lease. |
| `Other` | The term of the lease is something other than is available on this list. |
| `Renewal Option` | The lease has a renewal option. |
| `Short Term Lease` | The lease is short term. |
| `Weekly` | The length of the lease is weekly. |

### Levels

8 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Levels/)

| Value | Definition |
|---|---|
| `Bi-Level` | A bi-level home has two staggered levels. |
| `Multi/Split` | A split-level home (also called a tri-level home) is a style of house in which the floor levels are staggered so that the "main" level of the house (e.g., the level that usually contains the front ent… |
| `One` | The property being sold has one level. |
| `One and One Half` | A 1.5-story house is where the height of any of the walls on the second floor are less than the height of the walls on the first floor. |
| `Quad-Level` | A quad-level home has four staggered levels connected by two or more short sets of stairs. |
| `Three Or More` | The property being sold has three or more levels. |
| `Tri-Level` | A tri-level home has three staggered levels connected by two or more short sets of stairs. |
| `Two` | The property being sold has two levels. |

### LinearUnits

2 values · used by 15 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LinearUnits/)

| Value | Definition |
|---|---|
| `Feet` | The elevation of the property is measured in feet. |
| `Meters` | The elevation of the property is measured in meters. |

### ListAgentDesignation

27 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ListAgentDesignation/)

| Value | Definition |
|---|---|
| `Accredited Buyer's Representative / ABR` | The Accredited Buyer’s Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| `Accredited Land Consultant / ALC` | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| `At Home With Diversity / AHWD` | Learn to work effectively with and within today’s diverse real estate market. |
| `Certified Commercial Investment Member / CCIM` | The Certified Commercial Investment Member (CCIM) designation is commercial real estate’s global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| `Certified Distressed Property Expert / CDPE` | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today’s turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| `Certified International Property Specialist / CIPS` | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| `Certified Property Manager / CPM` | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| `Certified Real Estate Brokerage Manager / CRB` | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| `Certified Real Estate Team Specialist / C-RETS` | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| `Certified Residential Specialist / CRS` | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| `Counselor of Real Estate / CRE` | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| `e-PRO` | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |
| `General Accredited Appraiser / GAA` | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Graduate, REALTOR Institute / GRI` | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| `Military Relocation Professional / MRP` | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| `NAR's Green Designation / GREEN` | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| `Performance Management Network / PMN` | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| `Pricing Strategy Advisor / PSA` | Enhance your skills in pricing properties, creating CMAs (comparative market analyses), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| `Real Estate Negotiation Expert / RENE` | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| `REALTOR Association Certified Executive / RCE` | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| `Residential Accredited Appraiser / RAA` | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| `Resort & Second-Home Property Specialist / RSPS` | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| `Seller Representative Specialist / SRS` | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| `Seniors Real Estate Specialist / SRES` | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| `Short Sales & Foreclosure Resource / SFR` | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| `Society of Industrial and Office REALTORS / SIOR` | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| `Transnational Referral Certification / TRC` | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |

### ListingAgreement

7 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ListingAgreement/)

| Value | Definition |
|---|---|
| `Exclusive Agency` | A contract giving one brokerage firm, for a specified time, the right to sell/lease the property and also allowing the owner, acting alone, to sell/lease the property without paying commission. |
| `Exclusive Right To Lease` | A contract giving the broker the right to collect commission if the property is leased by anyone, including the owner, during the term of the agreement. |
| `Exclusive Right To Sell` | A contract giving the broker the right to collect commission if the property is sold by anyone, including the owner, during the term of the agreement. |
| `Exclusive Right With Exception` | A contract giving the broker the right to collect commission if the property is sold by anyone, including the owner, during the term of the agreement unless some specified exceptions to the agreement … |
| `Net` | A listing in which the broker's commission is the excess of the sale price over an agreed-upon (net) price to the seller; illegal in some states because it can create a conflict of interest for the br… |
| `Open` | Often used for commercial property, a listing given to any number of brokers without liability to compensate any except the one who first secures a buyer who is ready, willing and able to meet the terms of the listing and secures the seller's acceptance. |
| `Probate` | An Exclusive Right To Sell listing agreement that also resides under authority of the local probate code. |

### ListingService

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ListingService/)

| Value | Definition |
|---|---|
| `Entry Only` | The only service provided by the brokerage is the input of the listing into the MLS system. |
| `Full Service` | A full set of services offered by a brokerage. |
| `Limited Service` | A limited set of services offered by a brokerage |

### ListingTerms

26 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ListingTerms/)

| Value | Definition |
|---|---|
| `1031 Exchange` | The seller may be interested in a 1031 exchange as part of the sale. |
| `All Inclusive Trust Deed` | The property is under an all-inclusive trust deed. |
| `Assumable` | The seller is interested in assumable financing. |
| `Cash` | The seller would like a cash sale. |
| `Contract` | The seller may be interested in an agreement to perform services, provide product, share income or some other agreement as the method of payment for the property. |
| `Conventional` | The seller may accept a buyer using conventional financing to purchase the home. |
| `Existing Bonds` | The property for sale has existing bonds. |
| `FHA` | The seller may accept a buyer with a loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| `Land Use Fee` | The listed property has a land use fee. |
| `Lease Back` | The seller may be interested in the simultaneous sale of a property with a lease back to the seller who then becomes the tenant. |
| `Lease Option` | The seller may be interested in selling as a lease option to the buyer. |
| `Lease Purchase` | The seller may be interested in selling as a lease purchase. |
| `Lien Release` | The property for sale may require a lien release. |
| `Owner May Carry` | The seller may be interested in carrying the mortgage note. |
| `Owner Pay Points` | The seller may carry points. |
| `Owner Will Carry` | The seller will carry the mortgage note. |
| `Private Financing Available` | Financing is provided by a private party. |
| `Relocation Property` | The property for sale is a relocation property. |
| `Seller Equity Share` | The seller may be interested in investing in an equity share. |
| `Special Funding` | The seller may be interested in a special funding arrangement. |
| `Submit` | Contact the listing agent for the listing terms. |
| `Trade` | The seller may be interested in a trade arrangement. |
| `Trust Conveyance` | A trust conveyance (to another trustee) may be involved in the sale of the property. |
| `Trust Deed` | The seller may accept financing where title of the property is placed with a trustee who secures payment of the loan for a beneficiary. |
| `USDA Loan` | The seller may accept a loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| `VA Loan` | The seller may accept a loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

### ListingURLDescription

7 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ListingURLDescription/)

| Value | Definition |
|---|---|
| `Agent Website` | A link that directs to the listing on an agent website. |
| `Broker Website` | A link that directs to the listing on a broker website. |
| `Brokerage Website` | A link that directs to the listing on a brokerage website. |
| `Franchisor Website` | A link that directs to the listing on a franchisor website. |
| `MLS Website` | A link that directs to the listing on an MLS website. |
| `Other Website` | A link that directs to the listing on a general website. |
| `Syndication Website` | A link that directs to the listing on a syndication website. |

### LockBoxType

8 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LockBoxType/)

| Value | Definition |
|---|---|
| `Call Listing Office` | Call the listing office for information about accessing the property. |
| `Call Seller Direct` | Call the seller directly to arrange for access to the property. |
| `Combo` | The lockbox on the property is opened via combination. |
| `None` | There is no lockbox on the property. |
| `Other` | A lockbox type is not included on this list. |
| `See Remarks` | See remarks for details about the lockbox and accessing the property. |
| `SentriLock` | The lockbox is from SentriLock and requires a SentriLock key or access code. |
| `Supra` | The lockbox is from Supra and requires a Supra key. |

### LotDimensionsSource

11 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LotDimensionsSource/)

| Value | Definition |
|---|---|
| `Appraiser` | The lot dimensions were provided by an appraiser. |
| `Assessor` | The lot dimensions were provided by an assessor. |
| `Builder` | The lot dimensions were provided by a builder. |
| `Estimated` | The lot dimensions were estimated. |
| `GIS Calculated` | The lot dimensions were calculated by a Geographic Information System (GIS). |
| `Measured` | The lot dimensions were measured. |
| `Other` | The lot dimensions were provided by a source other than those on this list. |
| `Owner` | The lot dimensions were provided by the owner. |
| `Public Records` | The lot dimensions were taken from public records. |
| `See Remarks` | See the public or private remarks for details on the source of the lot dimensions. |
| `Survey` | The lot dimensions were provided by a land survey. |

### LotFeatures

56 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LotFeatures/)

| Value | Definition |
|---|---|
| `Agricultural` | The lot has agricultural features. |
| `Back Yard` | The lot has a backyard. |
| `Bluff` | The lot is on or near a bluff. |
| `City Lot` | The lot is in a city/urban setting. |
| `Cleared` | The lot has been cleared. |
| `Close to Clubhouse` | The lot is located close to a community clubhouse. |
| `Corner Lot` | The lot is located on the corner of an intersection. |
| `Corners Marked` | The corners of the lot have been marked. |
| `Cul-De-Sac` | The lot is located on a street that is closed on one end in a circular shape. |
| `Desert Back` | The back of the lot faces a desert area. |
| `Desert Front` | The front of the lot faces a desert area. |
| `Farm` | The lot is or has characteristics of a farm. |
| `Few Trees` | The lot has a few trees. |
| `Flag Lot` | Named for the shape, a flag lot has a long driveway leading to the property that, together, may have the appearance of a pole and flag. |
| `Front Yard` | The lot has a front yard. |
| `Garden` | The lot has a garden. |
| `Gentle Sloping` | The lot's slop is gentle. |
| `Greenbelt` | the lot is adjacent to a greenbelt. |
| `Interior Lot` | Also referred to as an inside lot, an interior lot faces a street on only one side. |
| `Irregular Lot` | The lot is not a rectangle. |
| `Lake on Lot` | The lot is not waterfront but the lake water feature is part of the lot. |
| `Landscaped` | The lot has been fully or partially landscaped. |
| `Level` | The lot is level/flat. |
| `Many Trees` | The lot has many trees. |
| `Meadow` | The lot has a meadow. |
| `Native Plants` | The lot's landscaping includes native plants. |
| `Near Golf Course` | The lot is near a golf course. |
| `Near Public Transit` | The lot is near public transportation. |
| `On Golf Course` | The lot is directly adjacent to a golf course. |
| `Open Lot` | The lot is open. |
| `Orchard(s)` | The lot includes one or more orchards. |
| `Other` | The lot has features other than those on this list. |
| `Pasture` | The lot includes a pasture. |
| `Paved` | The lot is partially or fully paved. |
| `Pie Shaped Lot` | The lot is shaped like a pie or triangle and is typically narrow at the front and wide at the back. |
| `Pond on Lot` | The lot is not waterfront but the pond water feature is part of the lot. |
| `Private` | The lot is private or has features that provide privacy from adjacent areas such as neighbors or roads. |
| `Rectangular Lot` | Also known as a regular-shaped lot, the lot has a rectangle or square shape. |
| `Rock Outcropping` | Rock features or barriers that transition a grading in the landscape. |
| `Rolling Slope` | The slope of the property varies in a rolling or wavy fashion. |
| `Secluded` | The lot is secluded. |
| `See Remarks` | See the remarks fields for additional information about the lot's features. |
| `Sloped` | The lot is sloped. |
| `Sloped Down` | The lot is sloped down, typically from the perspective of looking at the property from the street. |
| `Sloped Up` | The lot is sloped up, typically from the perspective of looking at the property from the street. |
| `Split Possible` | It may be possible that the lot could be split into two or more parcels. |
| `Sprinklers In Front` | There are irrigation sprinklers on the front of the lot. |
| `Sprinklers In Rear` | There are irrigation sprinklers to the rear of the lot. |
| `Steep Slope` | The lot is sloped steeply. |
| `Subdivided` | The lot has been subdivided into two or more parcels. |
| `Views` | There are views from the lot. |
| `Waterfall` | The lot has a waterfall. |
| `Waterfront` | The lot is located on a waterfront. |
| `Wetlands` | The lot is located near or within wetlands. |
| `Wooded` | The lot is wooded. |
| `Zero Lot Line` | The structure comes up to or very near the property line. |

### LotSizeSource

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LotSizeSource/)

| Value | Definition |
|---|---|
| `Appraiser` | An appraiser provided the measurement of the lot size. |
| `Assessor` | The assessor provided the measurement of the lot size. |
| `Builder` | The builder provided the measurement of the lot size. |
| `Estimated` | The measurement of the lot size is an estimate. |
| `Other` | The measurement of the lot size was provided by another party not listed. |
| `Owner` | The owner provided the measurement of the lot size. |
| `Plans` | The measurement of the lot size was taken from building plans. |
| `Public Records` | The measurement of the lot size was received from public records. |
| `See Remarks` | See remarks for information about the source of the lot size measurement. |

### LotSizeUnits

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/LotSizeUnits/)

| Value | Definition |
|---|---|
| `Acres` | The value reported in the Lot Size Area field is in acres. |
| `Square Feet` | The value reported in the Lot Size Area field is in square feet. |
| `Square Meters` | The value reported in the Lot Size Area field is in square meters. |

### OccupantType

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OccupantType/)

| Value | Definition |
|---|---|
| `Owner` | The occupant is the owner. |
| `Tenant` | The occupant is a tenant. |
| `Vacant` | The property is vacant. |

### OperatingExpenseIncludes

33 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OperatingExpenseIncludes/)

| Value | Definition |
|---|---|
| `Accounting` | The operating expense amount includes accounting costs. |
| `Advertising` | The operating expense amount includes advertising costs. |
| `Association` | The operating expense amount includes association costs. |
| `Cable TV` | The operating expense amount includes cable TV costs. |
| `Capital Improvements` | The operating expense amount includes capital improvements costs. |
| `Depreciation` | The operating expense amount includes depreciation costs. |
| `Equipment Rental` | The operating expense amount includes equipment rental costs. |
| `Fuel` | The operating expense amount includes fuel costs. |
| `Furniture Replacement` | The operating expense amount includes furniture replacement costs. |
| `Gardener` | The operating expense amount includes gardener costs. |
| `Insurance` | The operating expense amount includes insurance costs. |
| `Legal` | The operating expense amount includes legal costs. |
| `Licenses` | The operating expense amount includes license costs. |
| `Maintenance` | The operating expense amount includes maintenance costs. |
| `Maintenance Grounds` | The operating expense amount includes maintenance grounds costs. |
| `Maintenance Structure` | The operating expense amount includes maintenance structure costs. |
| `Manager` | The operating expense amount includes manager costs. |
| `Mortgage/Loans` | The operating expense amount includes mortgage/loan costs. |
| `New Tax` | The operating expense amount includes new tax costs. |
| `Other` | The operating expense amount includes other costs. |
| `Parking` | The operating expense amount includes parking costs. |
| `Pest Control` | The operating expense amount includes pest control costs. |
| `Pool/Spa` | The operating expense amount includes pool/spa costs. |
| `Professional Management` | The operating expense amount includes professional management costs. |
| `Security` | The operating expense amount includes security costs. |
| `Snow Removal` | The operating expense amount includes snow removal costs. |
| `Staff` | The operating expense amount includes staff costs. |
| `Supplies` | The operating expense amount includes supplies costs. |
| `Trash` | The operating expense amount includes trash costs. |
| `Utilities` | The operating expense amount includes utility costs. |
| `Vacancy Allowance` | The operating expense amount includes vacancy allowance costs. |
| `Water/Sewer` | The operating expense amount includes water/sewer costs. |
| `Workmans Compensation` | The operating expense amount includes workman's compensation costs. |

### OtherEquipment

21 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OtherEquipment/)

| Value | Definition |
|---|---|
| `Air Purifier` | The property includes an air purifier. |
| `Call Listing Agent` | Call the listing agent for more information about other equipment included with the property. |
| `Compressor` | The property includes a compressor. |
| `DC Well Pump` | The property includes a DC well pump. |
| `Dehumidifier` | The property includes a dehumidifier. |
| `Farm Equipment` | The property includes farm equipment. |
| `Fuel Tank(s)` | The property includes a fuel tank or fuel tanks. |
| `Generator` | The property includes a generator. |
| `Home Theater` | The property includes a home theater. |
| `Intercom` | The property includes an intercom. |
| `Irrigation Equipment` | The property includes irrigation equipment. |
| `List Available` | A list of other equipment included with the property is available upon request. |
| `Livestock Equipment` | The property includes livestock equipment. |
| `Negotiable` | The other equipment included with the property is negotiable. |
| `None` | There is no other equipment included with the property. |
| `Orchard Equipment` | The property includes orchard equipment. |
| `Other` | The property includes equipment other than what's included on this list. |
| `Rotary Antenna` | The property includes a rotary antenna. |
| `Satellite Dish` | The property includes a satellite dish. |
| `TV Antenna` | The property includes a TV antenna. |
| `Varies by Unit` | The equipment included with the property varies from unit to unit. |

### OtherStructures

33 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OtherStructures/)

| Value | Definition |
|---|---|
| `Airplane Hangar` | The property includes an airplane hangar. |
| `Arena` | The property includes an arena. |
| `Barn(s)` | The property includes a barn or barns. |
| `Boat House` | The property includes a boat house. |
| `Cabana` | The property includes a cabana. |
| `Cave(s)` | The property includes a cave or caves. |
| `Corral(s)` | The property includes a corral or corrals. |
| `Covered Arena` | The property includes a covered arena. |
| `Garage(s)` | The property includes a garage or garages. |
| `Gazebo` | The property includes a gazebo. |
| `Grain Storage` | The property includes grain storage. |
| `Greenhouse` | The property includes a greenhouse. |
| `Guest House` | The property includes a guest house. |
| `Kennel/Dog Run` | The property includes a kennel or dog run. |
| `Mobile Home` | The property includes a mobile home. |
| `None` | The property has no other structures. |
| `Other` | The property includes a structure other than those included on this list. |
| `Outbuilding` | The property includes an outbuilding. |
| `Outdoor Kitchen` | The property includes an outdoor kitchen. |
| `Packing Shed` | The property includes a packing shed. |
| `Pergola` | The property includes a pergola. |
| `Pool House` | The property includes a pool house. |
| `Poultry Coop` | The property includes a poultry coop. |
| `Residence` | The property includes a residence structure. |
| `RV/Boat Storage` | The property includes RV or boat storage. |
| `Second Garage` | The property includes a second garage. |
| `Second Residence` | The property includes a second residence. |
| `See Remarks` | See the public or private remarks for information about other structures on the property. |
| `Shed(s)` | The property includes a shed or sheds. |
| `Stable(s)` | The property includes a stable or stables. |
| `Storage` | The property includes storage. |
| `Tennis Court(s)` | The property includes a tennis court or tennis courts. |
| `Workshop` | The property includes a workshop. |

### OwnerPays

29 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OwnerPays/)

| Value | Definition |
|---|---|
| `All Utilities` | The owner/lessor pays for all utilities. |
| `Association Fees` | The owner/lessor pays for association fees. |
| `Cable TV` | The owner/lessor pays for cable television. |
| `Common Area Maintenance` | The owner/lessor pays for common area maintenance. |
| `Electricity` | The owner/lessor pays for electricity. |
| `Exterior Maintenance` | The owner/lessor pays for exterior maintenance. |
| `Gas` | The owner/lessor pays for gas. |
| `Grounds Care` | The owner/lessor pays for grounds care. |
| `Hot Water` | The owner/lessor pays for hot water. |
| `HVAC Maintenance` | The owner/lessor pays for HVAC maintenance. |
| `Insurance` | The owner/lessor pays for insurance. |
| `Janitorial Service` | The owner/lessor pays for janitorial service. |
| `Management` | The owner/lessor pays for management. |
| `None` | The owner/lessor pays for no utilities, services, etc. |
| `Other` | The owner/lessor pays for items that are not included on this list. |
| `Other Tax` | The owner/lessor pays for other taxes. |
| `Parking Fee` | The owner/lessor pays for parking fees. |
| `Pest Control` | The owner/lessor pays for pest control. |
| `Pool Maintenance` | The owner/lessor pays for pool maintenance. |
| `Repairs` | The owner/lessor pays for repairs. |
| `Roof Maintenance` | The owner/lessor pays for roof maintenance. |
| `Security` | The owner/lessor pays for security. |
| `See Remarks` | See the listing's remarks for details on what the owner/lessor pays for. |
| `Sewer` | The owner/lessor pays for sewer. |
| `Snow Removal` | The owner/lessor pays for snow removal. |
| `Taxes` | The owner/lessor pays for taxes. |
| `Telephone` | The owner/lessor pays for telephone. |
| `Trash Collection` | The owner/lessor pays for trash collection. |
| `Water` | The owner/lessor pays for water. |

### OwnershipType

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/OwnershipType/)

| Value | Definition |
|---|---|
| `Corporation` | The ownership type of the business being sold is a corporation. |
| `LLC` | The ownership type of the business being sold is a limited liability corporation. |
| `Partnership` | The ownership type of the business being sold is a partnership. |
| `Sole Proprietor` | The ownership type of the business being sold is a sole proprietor. |

### ParkingFeatures

72 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ParkingFeatures/)

| Value | Definition |
|---|---|
| `Additional Parking` | The property has additional parking. |
| `Aggregate` | While aggregate is a type of concrete, it is different in application, maintenance and durability. |
| `Alley Access` | The property has alley access. |
| `Asphalt` | The property has asphalt parking. |
| `Assigned` | The property has assigned parking spaces. |
| `Attached` | The property has attached parking. |
| `Attached Carport` | The property has an attached carport. |
| `Basement` | A basement garage is partially or mostly below grade, with its entrance level with the basement floor. |
| `Boat` | The property has a space to park/store a boat. |
| `Carport` | The property has a carport. |
| `Circular Driveway` | The property has a circular driveway. |
| `Common` | The property has common/shared parking. |
| `Community Structure` | The property has a community parking structure. |
| `Concrete` | The property has concrete paved parking. |
| `Converted Garage` | The property has a converted garage. |
| `Covered` | The property has covered parking. |
| `Deck` | The property has a deck for parking. |
| `Deeded` | The property has deeded parking. |
| `Detached` | The property has detached parking. |
| `Detached Carport` | The property has a detached carport. |
| `Direct Access` | The parking has direct access to the property or structure. |
| `Drive Through` | The property has drive-through parking. |
| `Driveway` | The property has a driveway. |
| `Electric Gate` | The property has an electric gate. |
| `Electric Vehicle Charging Station(s)` | The property has one or more electric vehicle charging station. |
| `Enclosed` | The property has enclosed parking. |
| `Garage` | The property has a garage. |
| `Garage Door Opener` | The garage has an automatic garage door opener. |
| `Garage Faces Front` | The property has a garage that faces the front of the property. |
| `Garage Faces Rear` | The property has a garage that faces the rear of the property. |
| `Garage Faces Side` | The property has a garage that faces the side of the property. |
| `Gated` | The property has gated parking. |
| `Golf Cart Garage` | The property has a golf cart garage. |
| `Gravel` | The property has parking on gravel. |
| `Guest` | The property has guest parking. |
| `Heated Garage` | The property has a heated garage. |
| `Inside Entrance` | The property has parking with an inside entrance. |
| `Kitchen Level` | The property has parking at the kitchen level. |
| `Leased` | The property has leased parking. |
| `Lighted` | The property has lighted parking. |
| `No Garage` | The property has no garage. |
| `None` | The property does not include parking or no parking is available. |
| `Off Site` | The property has off-site parking. |
| `Off Street` | The property has off-street parking. |
| `On Site` | The property has on-site parking. |
| `On Street` | The property has on-street parking only. |
| `Open` | The property has open or unassigned parking. |
| `Other` | The property has parking features other than those included on this list. |
| `Outside` | The property has outside parking that is not enclosed. |
| `Oversized` | The property has parking for oversized vehicles. |
| `Parking Lot` | The property has access to a parking lot. |
| `Parking Pad` | The property has a parking pad. |
| `Paved` | The property has paved parking. |
| `Paver Block` | The property has parking on paver blocks. |
| `Permit Required` | Parking at the property or on the street requires a permit. |
| `Private` | The property has private parking. |
| `RV Access/Parking` | The property has access/parking for recreational vehicles. |
| `RV Carport` | The property has a carport for recreational vehicles. |
| `RV Garage` | The property has a garage for recreational vehicles. |
| `RV Gated` | The property has gated parking for recreational vehicles. |
| `Secured` | The property has secure parking. |
| `See Remarks` | See remarks for additional information about parking. |
| `Shared Driveway` | The property has a shared driveway. |
| `Side By Side` | The property has side-by-side parking spaces. |
| `Storage` | The property has storage in the parking area. |
| `Tandem` | The property has tandem parking. |
| `Unassigned` | The property has unassigned or open parking. |
| `Underground` | The property has underground parking. |
| `Unpaved` | The property has parking on an unpaved surface. |
| `Valet` | The property has valet parking available. |
| `Varies by Unit` | The parking varies from unit to unit. |
| `Workshop in Garage` | The property has a workshop in the garage. |

### PatioAndPorchFeatures

16 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PatioAndPorchFeatures/)

| Value | Definition |
|---|---|
| `Awning(s)` | The property has one or more awnings. |
| `Covered` | The property has a covered patio or porch. |
| `Deck` | The property has a deck. |
| `Enclosed` | The property has an enclosed patio or porch. |
| `Front Porch` | The property has a front porch. |
| `Glass Enclosed` | The property has a glass-enclosed patio or porch. |
| `None` | The property has no patio or porch. |
| `Other` | The property has a patio or porch feature other than what's included on this list. |
| `Patio` | The property has a patio. |
| `Porch` | The property has a porch. |
| `Rear Porch` | The property has a rear porch. |
| `Screened` | The property has a screened patio or porch. |
| `See Remarks` | See the remarks fields for more information on the patio or porch features of the property. |
| `Side Porch` | The property has a side porch. |
| `Terrace` | The property has a terrace. |
| `Wrap Around` | The property has wraparound patio or porch. |

### PetsAllowed

8 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PetsAllowed/)

| Value | Definition |
|---|---|
| `Breed Restrictions` | There are breed restrictions on allowed pets. |
| `Call` | Call to inquire about pet restrictions. |
| `Cats OK` | Cats are allowed. |
| `Dogs OK` | Dogs are allowed. |
| `No` | No pets are allowed. |
| `Number Limit` | There is a limit on the number of pets allowed. |
| `Size Limit` | There are size restrictions on allowed pets. |
| `Yes` | All pets are allowed. |

### PoolFeatures

35 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PoolFeatures/)

| Value | Definition |
|---|---|
| `Above Ground` | The pool is above ground. |
| `Association` | The pool is an association pool. |
| `Black Bottom` | The pool has a black bottom. |
| `Cabana` | The pool has a cabana. |
| `Community` | The pool is a community/shared pool. |
| `Diving Board` | The pool has a diving board. |
| `Electric Heat` | The pool is heated by electricity. |
| `ENERGY STAR Qualified pool pump` | The pool has a qualified ENERGY STAR pool pump. |
| `Fenced` | The pool is fenced. |
| `Fiberglass` | The pool is made of or lined with fiberglass. |
| `Filtered` | The pool has a filtration system. |
| `Gas Heat` | The pool is heated by gas. |
| `Gunite` | The pool has a gunite surface. |
| `Heated` | The pool is heated. |
| `In Ground` | The pool is built into the ground. |
| `Indoor` | The pool is indoors or within a structure. |
| `Infinity` | Also named a negative edge, zero edge or infinity edge, an infinity pool has one or more edges where water flows over the edge, creating a visual effect of water with no boundary. |
| `Lap` | The pool is specifically designed for swimming laps. |
| `Liner` | The pool has a liner. |
| `None` | There is no pool included with the property. |
| `Other` | There are pool features other than those included on this list. |
| `Outdoor Pool` | The pool is outdoors. |
| `Pool Cover` | The pool has a cover. |
| `Pool Sweep` | The pool has an automatic sweep or cleaner. |
| `Pool/Spa Combo` | The pool includes a spa. |
| `Private` | The pool is privately owned and/or secluded. |
| `Salt Water` | The pool has a saltwater system. |
| `Screen Enclosure` | The pool has a screened enclosure. |
| `See Remarks` | See the remarks fields for more information about the pool. |
| `Solar Cover` | The pool has a solar cover. |
| `Solar Heat` | The pool has some form of solar heating. |
| `Sport` | The pool has two shallow ends on opposite sides of the pool with a deeper center. |
| `Tile` | The pool is tiled. |
| `Vinyl` | The pool has a vinyl surface. |
| `Waterfall` | The pool has a waterfall. |

### Possession

12 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Possession/)

| Value | Definition |
|---|---|
| `Close Of Escrow` | Possession is passed to the buyer at the close of escrow. |
| `Close Plus 1 Day` | Possession is passed to the buyer one day after the close of escrow. |
| `Close Plus 2 Days` | Possession is passed to the buyer two days after the close of escrow. |
| `Close Plus 3 Days` | Possession is passed to the buyer three days after the close of escrow. |
| `Close Plus 3 to 5 Days` | Possession is passed to the buyer three to five days after the close of escrow. |
| `Close Plus 30 Days` | Possession is passed to the buyer 30 days after the close of escrow. |
| `Negotiable` | Timing of the passing of possession to the buyer is negotiable. |
| `Other` | A type of possession not included on this list. |
| `Rental Agreement` | Possession is stipulated in the rental agreement. |
| `See Remarks` | See the listing/agent remarks for more information on possession. |
| `Seller Rent Back` | Possession is determined by the details of the seller rent-back agreement. |
| `Subject To Tenant Rights` | The terms of the transfer of possession are subject to the rights of the current tenant. |

### PowerProductionType

2 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PowerProductionType/)

| Value | Definition |
|---|---|
| `Photovoltaics` | Solar photovoltaic (PV) devices which generate electricity directly from sunlight via an electronic process that occurs naturally in certain types of material, called semiconductors. |
| `Wind` | Renewable form of onsite power generation. |

### PropertyCondition

5 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PropertyCondition/)

| Value | Definition |
|---|---|
| `Fixer` | The property is in need of moderate or extensive repair. |
| `New Construction` | The property is newly built. |
| `To Be Built` | The property has yet to be built. |
| `Under Construction` | The property is still under construction; building has not been completed. |
| `Updated/Remodeled` | The property has been remodeled or updated is some fashion. |

### PropertySubType

31 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PropertySubType/)

| Value | Definition |
|---|---|
| `Agriculture` | The property is for farming and agricultural activities. |
| `Apartment` | A unit within a wholly owned structure of five or more units. |
| `Boat Slip` | A place where you can tie up a boat or house boat. |
| `Business` | The property is designed for any type of business. |
| `Cabin` | A single-family residence that may have limited utilities. |
| `Condominium` | A unit within a structure where ownership is on a unit-by-unit basis. |
| `Co-Ownership` | Co-ownership indicates that the property is owned by two or more parties in which each party has an equal ownership interest and obtains ownership at the same time. |
| `Deeded Parking` | A parking space (or spaces) that are owned and separate from a residence. |
| `Duplex` | A multifamily structure that has two independent units with a shared wall or ceiling/floor. |
| `Farm` | A place where agricultural and similar activities take place, especially the growing of crops. |
| `Hotel/Motel` | The property is designed for hotel or motel use. |
| `Industrial` | The property is designed for industrial use. |
| `Manufactured Home` | A factory-built house that is transported to the lot. |
| `Manufactured On Land` | A factory-built house that is transported to the lot and sold with the land. |
| `Mixed Use` | The property is designed to be used in more than one way (i.e., office and retail). |
| `Mobile Home` | A factory-built house that is transported to the lot, retains axles and was built prior to June 15, 1976. |
| `Mobile Home Park` | A permanent area for a group of mobile homes, usually with fixed utilities. |
| `Multi Family` | A structure or complex with five or more units that are individual dwellings. |
| `Office` | The property is designed to be used as office space. |
| `Own Your Own` | A unit within a structure where ownership is based on a partial deed and rights to occupy a unit. |
| `Quadruplex` | A multifamily structure with four independent units with shared walls or ceilings/floors. |
| `Ranch` | A place where agricultural and similar activities take place, especially the raising of livestock. |
| `Retail` | The property designed to be used as retail space. |
| `Single Family Residence` | A single family residence on real property. |
| `Stock Cooperative` | A unit within a structure where ownership is based on a share of stock and rights to occupy a unit. |
| `Tenancy in Common` | Tenancy in Common (TIC) indicates that the property is owned by two or more parties in which each party has an ownership interest, which may or may not be equal, and may obtain ownership at different … |
| `Timeshare` | A form of property ownership where a property is held by a number of people, each with the right of possession for a specified time interval. |
| `Townhouse` | A dwelling unit generally having two or more floors and attached to other similar units via party walls. |
| `Triplex` | A multifamily structure with three independent units with shared walls or ceilings/floors. |
| `Unimproved Land` | Commercial land that has not been built upon or improved. |
| `Warehouse` | The property is designed to be used for warehousing. |

### PropertyType

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/PropertyType/)

| Value | Definition |
|---|---|
| `Business Opportunity` | The property type of the listing is Business Opportunity. |
| `Commercial Lease` | The property type of the listing is Commercial Lease. |
| `Commercial Sale` | The property type of the listing is Commercial Sale. |
| `Farm` | The property type of the listing is Farm. |
| `Land` | The property type of the listing is Land. |
| `Manufactured In Park` | The property type of the listing is Manufactured in Park. |
| `Residential` | The property type of the listing is Residential. |
| `Residential Income` | The property type of the listing is Residential Income. |
| `Residential Lease` | The property type of the listing is Residential Lease. |

### RentIncludes

13 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RentIncludes/)

| Value | Definition |
|---|---|
| `All Utilities` | Rent for the dwelling includes all utilities. |
| `Cable TV` | Rent for the dwelling includes cable TV. |
| `Electricity` | Rent for the dwelling includes electricity. |
| `Gardener` | Rent for the dwelling includes gardening services. |
| `Gas` | Rent for the dwelling includes gas. |
| `Internet` | Rent for the dwelling includes Internet service. |
| `Management` | Rent for the dwelling includes management. |
| `None` | Rent for the dwelling does not include other potential costs such as utilities, management, services, etc. |
| `Other` | An item of what rent includes that is not on this list. |
| `See Remarks` | See the listing's remarks for details about things included in the rent. |
| `Sewer` | Rent for the dwelling includes sewer. |
| `Trash Collection` | Rent for the dwelling includes trash collection. |
| `Water` | Rent for the dwelling includes water. |

### RoadFrontageType

13 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RoadFrontageType/)

| Value | Definition |
|---|---|
| `Alley` | The property fronts to an alley. |
| `City Street` | The property fronts to a city street. |
| `County Road` | The property fronts to a county road. |
| `Easement` | The property fronts to an easement. |
| `Freeway` | The property fronts to a freeway. |
| `Highway` | The property fronts to a highway. |
| `Interstate` | The property fronts to an interstate. |
| `None` | The property does not have any road frontage. |
| `Other` | The property fronts to a road other than those on this list. |
| `Private Road` | The property fronts to a private road. |
| `See Remarks` | See public or private remarks for details on the road frontage. |
| `State Road` | The property fronts to a state road. |
| `Unimproved` | The property's road frontage is unimproved. |

### RoadResponsibility

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RoadResponsibility/)

| Value | Definition |
|---|---|
| `Private Maintained Road` | The property's road is privately maintained. |
| `Public Maintained Road` | The property's road is publicly maintained. |
| `Road Maintenance Agreement` | The property has a road maintenance agreement. |

### RoadSurfaceType

11 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RoadSurfaceType/)

| Value | Definition |
|---|---|
| `Alley Paved` | The property's road is a paved alley. |
| `Asphalt` | The property's road is asphalt. |
| `Chip And Seal` | The property's road is chip and seal. |
| `Concrete` | The property's road is concrete. |
| `Dirt` | The property's road is dirt. |
| `Gravel` | The property's road is gravel. |
| `None` | The property has no road. |
| `Other` | The surface type of the property's road is something other than those on this list. |
| `Paved` | The property's road is paved. |
| `See Remarks` | See the public or private remarks for details on the road surface type. |
| `Unimproved` | The property's road is unimproved. |

### Roof

34 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Roof/)

| Value | Definition |
|---|---|
| `Aluminum` | The roof is made wholly or partially of aluminum. |
| `Asbestos Shingle` | The roof is made wholly or partially of asbestos shingles. |
| `Asphalt` | The roof is made wholly or partially of asphalt. |
| `Bahama` | The roof is a Bahama roof. |
| `Barrel` | The roof is a barrel roof. |
| `Bituthene` | The roof is made wholly or partially of Bituthene. |
| `Built-Up` | The roof is wholly or partially a built-up roof system. |
| `Composition` | The roof is made wholly or partially of composition. |
| `Concrete` | The roof is made wholly or partially of concrete. |
| `Copper` | The roof is made wholly or partially of copper. |
| `Elastomeric` | The roof is made wholly or partially of elastomeric. |
| `Fiberglass` | The roof is made wholly or partially of fiberglass. |
| `Flat` | The roof is wholly or partially flat. |
| `Flat Tile` | The roof is made wholly or partially of flat tile. |
| `Foam` | The roof is made wholly or partially of foam. |
| `Green Roof` | The roof is wholly or partially a green roof. |
| `Mansard` | The roof is made wholly or partially of mansard. |
| `Membrane` | The roof is made wholly or partially of membrane. |
| `Metal` | The roof is made wholly or partially of metal. |
| `Mixed` | The roof is made wholly or partially of mixed materials. |
| `None` | The roof materials are unstated, unknown or there are none. |
| `Other` | The roof is made wholly or partially of materials other than those on this list. |
| `Rolled/Hot Mop` | The roof is made wholly or partially of rolled/hot mop. |
| `Rubber` | The roof is made wholly or partially of rubber. |
| `See Remarks` | See the listing's remarks for details on the roof. |
| `Shake` | The roof is made wholly or partially of shake. |
| `Shingle` | The roof is made wholly or partially of shingle. |
| `Slate` | The roof is made wholly or partially of slate. |
| `Spanish Tile` | The roof is made wholly or partially of Spanish tile. |
| `Stone` | The roof is made wholly or partially of stone. |
| `Synthetic` | The roof is made wholly or partially of synthetic materials. |
| `Tar/Gravel` | The roof is made wholly or partially of tar/gravel. |
| `Tile` | The roof is made wholly or partially of tile. |
| `Wood` | The roof is made wholly or partially of wood. |

### RoomType

33 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/RoomType/)

| Value | Definition |
|---|---|
| `Basement` | A floor of a building below ground level. |
| `Bathroom` | The first bathroom, when a primary bathroom is not designated. |
| `Bathroom 1` | The first bathroom, when a primary bathroom is not designated. |
| `Bathroom 2` | The second bathroom. |
| `Bathroom 3` | The third bathroom. |
| `Bathroom 4` | The fourth bathroom. |
| `Bathroom 5` | The fifth bathroom. |
| `Bedroom` | The type of room is a bedroom. |
| `Bedroom 1` | The first bedroom, when a primary bedroom is not designated. |
| `Bedroom 2` | The second bedroom. |
| `Bedroom 3` | The third bedroom. |
| `Bedroom 4` | The fourth bedroom. |
| `Bedroom 5` | The fifth bedroom. |
| `Bonus Room` | A room that can be used for multiple purposes. |
| `Den` | Typically a secluded comfortable room used as a study or entertainment room. |
| `Dining Room` | A room in a home where meals are eaten. |
| `Exercise Room` | A room that is specifically geared to contain exercise equipment. |
| `Family Room` | A comfortable room in a dwelling frequently used for leisure use. |
| `Game Room` | Typically a bonus room that is specifically equipped for game play. |
| `Great Room` | Denotes a room space within an abode which combines the specific functions of several of the more traditional room spaces (e.g., family room, living room, study, etc.) into a singular unified space. |
| `Gym` | A room that, in addition to exercise equipment, has other characteristics of a gymnasium. |
| `Kitchen` | The room used for the preparation and storage of food; cookery. |
| `Laundry` | A utility room specifically used for laundry equipment (washer and dryer). |
| `Library` | A room that is specifically geared to house books and other media typically found in a library. |
| `Living Room` | A room in a private house used for general social and leisure activities. |
| `Loft` | A loft can be an upper story or attic in a building, directly under the roof. |
| `Master Bathroom` | Typically the largest of the bathrooms and attached to the primary bedroom. |
| `Master Bedroom` | Typically the largest of the bedrooms with an attached bathroom. |
| `Media Room` | A room that is specifically geared for the watching of movies, TV or other forms of multimedia. |
| `Office` | A room used for business. |
| `Sauna` | A small room or house designed as a place to experience dry or wet heat sessions, or an establishment with one or more of these and auxiliary facilities. |
| `Utility Room` | A room that usually contains laundry, HVAC (heating, ventilation and air conditioning), water heating or some other utilitarian equipment. |
| `Workshop` | A room containing tools or equipment used for the manufacturing or repair of goods. |

### SecurityFeatures

28 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SecurityFeatures/)

| Value | Definition |
|---|---|
| `24 Hour Security` | The property has 24-hour security. |
| `Building Security` | The property has building security. |
| `Carbon Monoxide Detector(s)` | The property has a carbon monoxide detector or detectors. |
| `Closed Circuit Camera(s)` | The property has a closed-circuit camera or cameras. |
| `Fire Alarm` | The property has a fire alarm or fire alarms. |
| `Fire Escape` | The property has a fire escape. |
| `Fire Sprinkler System` | The property has a fire sprinkler system. |
| `Firewall(s)` | The property has a firewall or firewalls. |
| `Gated Community` | The property is in a gated community. |
| `Gated with Guard` | The property is in a gated community/area with guard service. |
| `Key Card Entry` | The property or community has key card entry. |
| `Other` | The property has security features other than those on this list. |
| `Panic Alarm` | The property has a panic alarm. |
| `Prewired` | The property is prewired for a security system. |
| `Secured Garage/Parking` | The property has a secured garage or parking area. |
| `Security Fence` | The property has a security fence. |
| `Security Gate` | The property has a security gate. |
| `Security Guard` | The property or community has a security guard. |
| `Security Lights` | The property has security lights. |
| `Security Service` | The property has a security service. |
| `Security System` | The property has a security system. |
| `Security System Leased` | The property has a leased security system. |
| `Security System Owned` | The property has an owned security system. |
| `See Remarks` | See the remarks fields for more information about the security features of the property. |
| `Smoke Detector(s)` | The property has a smoke detector or smoke detectors. |
| `Varies By Unit` | The security features vary from unit to unit. |
| `Window Bars` | The property has window bars. |
| `Window Bars with Quick Release` | The property has window bars with a quick-release mechanism. |

### Sewer

15 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Sewer/)

| Value | Definition |
|---|---|
| `Aerobic Septic` | The property has an aerobic septic. |
| `Cesspool` | The property has a cesspool. |
| `Engineered Septic` | The property has an engineered septic. |
| `Holding Tank` | The property has a holding tank. |
| `Mound Septic` | The property has a mound septic. |
| `None` | The property has no sewer, septic or cesspool. |
| `Other` | The property has a system other than sewer, septic or cesspool on this list. |
| `Perc Test On File` | The property has a perc test on file. |
| `Perc Test Required` | The property requires a perc test. |
| `Private Sewer` | The property has a private sewer. |
| `Public Sewer` | The property has a public sewer. |
| `Septic Needed` | The property needs a septic system. |
| `Septic Tank` | The property has a septic tank. |
| `Shared Septic` | The property has a shared septic. |
| `Unknown` | The property's sewer/septic is unknown. |

### ShowingConsiderations

14 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingConsiderations/)

| Value | Definition |
|---|---|
| `Day Sleeper` | The property has a tenant/occupant who sleeps during the day. |
| `Electricity Not On` | The property does not have electricity or the electricity is not turned on. |
| `Inconsistent Cell Service` | There is inconsistent cellular service at the location of the property. |
| `Limited Visibility From Road` | The property has limited visibility from the road. |
| `Minimal Exterior Lighting` | The property has minimal exterior lighting. |
| `Minimal Interior Lighting` | The property has minimal interior lighting. |
| `No Exterior Lighting` | The property has no exterior lighting. |
| `No Heat` | The property does not have an heating system or the heating system is turned off. |
| `No Interior Lighting` | The property has no interior lighting. |
| `Occupied` | The property is currently occupied. |
| `Pet(s) on Premises` | There are currently pets at the property. |
| `Remote Location` | The property is in a remote location. |
| `Security System` | The property has a security system that is a consideration when showing. |
| `See Remarks` | See remarks for more information about showing considerations for the property. |

### ShowingContactType

4 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingContactType/)

| Value | Definition |
|---|---|
| `Agent` | The showing contact is a licensed agent. |
| `Occupant` | The showing contact is the occupant. |
| `Owner` | The showing contact is the owner. |
| `Property Manager` | The showing contact is the property manager. |

### ShowingRequirements

18 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingRequirements/)

| Value | Definition |
|---|---|
| `24 Hour Notice` | A 24-hour notice is required to show the property. |
| `Appointment Only` | Showing of the property is by appointment only. |
| `Call Listing Agent` | Call the listing agent to arrange a showing of the property. |
| `Call Listing Office` | Call the listing office to arrange a showing of the property. |
| `Call Manager` | Call the property manager to arrange a showing of the property. |
| `Call Owner` | Call the property owner to arrange a showing of the property. |
| `Call Tenant` | Call the tenant/occupant directly to arrange a showing of the property. |
| `Combination Lock Box` | The property has a combination lockbox for showing access. |
| `Do Not Show` | Do not show this property. |
| `Email Listing Agent` | Email the listing agent for more information about showing the property. |
| `Key In Office` | The key to access the property for showing must be retrieved from the listing or manager's office. |
| `Lockbox` | The property has an electronic lockbox for showing access. |
| `No Lockbox` | There is no lockbox on the property. |
| `No Sign` | The property has no "for sale" sign. |
| `Restricted Hours` | The times when the property may be shown are restricted. |
| `See Remarks` | See the remarks fields for more information about showing the property. |
| `Showing Service` | A service used by a listing broker to provide showing services of listed properties. |
| `Text Listing Agent` | Text message the listing agent to arrange a showing of the property. |

### ShowingServiceName

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/ShowingServiceName/)

| Value | Definition |
|---|---|
| `Aligned Showings` | Showings for the listing are scheduled through Aligned Showings. |
| `BrokerBay` | Showings for the listing are scheduled through BrokerBay. |
| `Homesnap` | Showings for the listing are scheduled through HomeSnap. |
| `Instashowing` | Showings for the listing are scheduled through Instashowing. |
| `LocalShowing` | Showings for the listing are scheduled through Local Showing. |
| `None` | No showing service is used for the listing. |
| `Other` | Showings for the listing are scheduled through a showing service other than those available on this list. |
| `SentriKey Showing` | Showings for the listing are scheduled through SentriKey Showing. |
| `Showingly` | Showings for the listing are scheduled through Showingly. |
| `ShowingTime` | Showings for the listing are scheduled through ShowingTime. |

### Skirt

19 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Skirt/)

| Value | Definition |
|---|---|
| `Aluminum` | The mobile/manufactured home has a skirt made of aluminum. |
| `Block` | The mobile/manufactured home has a skirt made of block. |
| `Brick` | The mobile/manufactured home has a skirt made of brick. |
| `Combination` | The mobile/manufactured home has a skirt made of a combination of materials. |
| `Concrete` | The mobile/manufactured home has a skirt made of concrete. |
| `Fiberglass` | The mobile/manufactured home has a skirt made of fiberglass. |
| `Frame` | The mobile/manufactured home has a skirt that is framed. |
| `Glass` | The mobile/manufactured home has a skirt made of glass. |
| `Masonite` | The mobile/manufactured home has a skirt made of Masonite. |
| `Metal` | The mobile/manufactured home has a skirt made of metal. |
| `None` | The mobile/manufactured home does not have a skirt. |
| `Other` | The mobile/manufactured home has a skirt made of materials other than those on this list. |
| `Steel` | The mobile/manufactured home has a skirt made of steel. |
| `Stone` | The mobile/manufactured home has a skirt made of stone. |
| `Stucco` | The mobile/manufactured home has a skirt made of stucco. |
| `Synthetic` | The mobile/manufactured home has a skirt made of synthetic materials. |
| `Unknown` | The mobile/manufactured home has a skirt made of unknown materials. |
| `Vinyl` | The mobile/manufactured home has a skirt made of vinyl. |
| `Wood` | The mobile/manufactured home has a skirt made of wood. |

### SpaFeatures

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SpaFeatures/)

| Value | Definition |
|---|---|
| `Above Ground` | The spa is not built into the ground. |
| `Bath` | The bath has a built-in spa or jets. |
| `Community` | The property has access to a community spa. |
| `Fiberglass` | The spa is lined or made of fiberglass. |
| `Gunite` | The spa is lined with gunite. |
| `Heated` | The spa is heated. |
| `In Ground` | The spa is built into the ground. |
| `None` | The property has no spa. |
| `Private` | The spa is privately owned or is secluded. |
| `See Remarks` | See the remarks fields for more information about the spa. |

### SpecialLicenses

13 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SpecialLicenses/)

| Value | Definition |
|---|---|
| `Beer/Wine` | The business being sold uses/requires a beer/wine license. |
| `Class H` | The business being sold uses/requires a Class H license. |
| `Entertainment` | The business being sold uses/requires an entertainment license. |
| `Franchise` | The business being sold uses/requires a franchise license. |
| `Gambling` | The business being sold uses/requires a gambling license. |
| `Liquor` | The business being sold uses/requires a liquor license. |
| `Liquor 5 Years Or Less` | The business being sold uses/requires a liquor license, five years or less. |
| `Liquor 5 Years Or More` | The business being sold uses/requires a liquor license, five years or more. |
| `Liquor-Off Sale` | The business being sold uses/requires a liquor off-sale license. |
| `Liquor-On Sale` | The business being sold uses/requires a liquor on-sale license. |
| `None` | The business being sold uses/requires/has no license. |
| `Other` | The business being sold uses/requires some other license. |
| `Professional` | The business being sold uses/requires a professional license. |

### SpecialListingConditions

12 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SpecialListingConditions/)

| Value | Definition |
|---|---|
| `Auction` | The listing is an auction. |
| `Bankruptcy Property` | The listed property is currently involved in a bankruptcy. |
| `Conservatorship` | Conservatorship is a legal concept in the United States. |
| `HUD Owned` | The listed property is owned and being sold by the U.S. |
| `In Foreclosure` | The listed property is currently in the process of foreclosure. |
| `Notice Of Default` | There is a notice of default on the listed property. |
| `Probate Listing` | The listed property is a probate sale. |
| `Real Estate Owned` | The listed property is currently owned by a bank/lender. |
| `Short Sale` | The listing is a short sale (short pay) and may require bank approval. |
| `Standard` | The listing has none of the other conditions in the Special Listing Conditions field. |
| `Third Party Approval` | A court or other third-party approval is required for the sale to finalize. |
| `Trust` | A three-party fiduciary relationship in which the first party, the trustor or settlor, transfers a property upon the second party for the benefit of the third party, the beneficiary. |

### StandardStatus

11 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/StandardStatus/)

| Value | Definition |
|---|---|
| `Active` | The listing is on market and an offer has not been accepted. |
| `Active Under Contract` | An offer has been accepted but the listing is still on market. |
| `Canceled` | The listing contract has been terminated. |
| `Closed` | The purchase agreement has been fulfilled or the lease agreement has been executed. |
| `Coming Soon` | This is a listing that has not yet been on market but will be on market soon. |
| `Delete` | The listing contract was never valid or there is another reason for the contract to be nullified. |
| `Expired` | The listing contract has expired. |
| `Hold` | A contract exists between the seller and the listing member. |
| `Incomplete` | The listing has not yet been completely entered and is not yet published in the MLS. |
| `Pending` | An offer has been accepted and the listing is no longer on market. |
| `Withdrawn` | The listing has been withdrawn from the market, but a contract still exists between the seller and the listing member. |

### StateOrProvince

65 values · used by 19 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/StateOrProvince/)

| Value | Definition |
|---|---|
| `AB` | The Canadian province in which the listing is located is Alberta. |
| `AK` | The U.S. |
| `AL` | The U.S. |
| `AR` | The U.S. |
| `AZ` | The U.S. |
| `BC` | The Canadian province in which the listing is located is British Columbia. |
| `CA` | The U.S. |
| `CO` | The U.S. |
| `CT` | The U.S. |
| `DC` | The U.S. |
| `DE` | The U.S. |
| `FL` | The U.S. |
| `GA` | The U.S. |
| `HI` | The U.S. |
| `IA` | The U.S. |
| `ID` | The U.S. |
| `IL` | The U.S. |
| `IN` | The U.S. |
| `KS` | The U.S. |
| `KY` | The U.S. |
| `LA` | The U.S. |
| `MA` | The U.S. |
| `MB` | The Canadian province in which the listing is located is Manitoba. |
| `MD` | The U.S. |
| `ME` | The U.S. |
| `MI` | The U.S. |
| `MN` | The U.S. |
| `MO` | The U.S. |
| `MS` | The U.S. |
| `MT` | The U.S. |
| `NB` | The Canadian province in which the listing is located is New Brunswick. |
| `NC` | The U.S. |
| `ND` | The U.S. |
| `NE` | The U.S. |
| `NF` | The Canadian province in which the listing is located is Newfoundland and Labrador. |
| `NH` | The U.S. |
| `NJ` | The U.S. |
| `NM` | The U.S. |
| `NS` | The Canadian province in which the listing is located is Nova Scotia. |
| `NT` | The Canadian territory in which the listing is located is Northwest Territories. |
| `NU` | The Canadian territory in which the listing is located is Nunavut. |
| `NV` | The U.S. |
| `NY` | The U.S. |
| `OH` | The U.S. |
| `OK` | The U.S. |
| `ON` | The Canadian province in which the listing is located is Ontario. |
| `OR` | The U.S. |
| `PA` | The U.S. |
| `PE` | The Canadian province in which the listing is located is Prince Edward Island. |
| `QC` | The Canadian province in which the listing is located is Quebec. |
| `RI` | The U.S. |
| `SC` | The U.S. |
| `SD` | The U.S. |
| `SK` | The Canadian province in which the listing is located is Saskatchewan. |
| `TN` | The U.S. |
| `TX` | The U.S. |
| `UT` | The U.S. |
| `VA` | The U.S. |
| `VI` | The U.S. |
| `VT` | The U.S. |
| `WA` | The U.S. |
| `WI` | The U.S. |
| `WV` | The U.S. |
| `WY` | The U.S. |
| `YT` | The Canadian territory in which the listing is located is Yukon. |

### StreetDirection

8 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/StreetDirection/)

| Value | Definition |
|---|---|
| `E` | The street suffix or prefix direction is east. |
| `N` | The street suffix or prefix direction is north. |
| `NE` | The street suffix or prefix direction is northeast. |
| `NW` | The street suffix or prefix direction is northwest. |
| `S` | The street suffix or prefix direction is south. |
| `SE` | The street suffix or prefix direction is southeast. |
| `SW` | The street suffix or prefix direction is southwest. |
| `W` | The street suffix or prefix direction is west. |

### StructureType

17 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/StructureType/)

| Value | Definition |
|---|---|
| `Cabin` | A single-family residence that may have limited utilities and rooms. |
| `Dock` | A floating or pillar-supported structure over water used to park watercraft. |
| `Duplex` | A multifamily structure with two independent units sharing a common roof. |
| `Flex` | A commercial property that is designed to be used in different ways (e.g., Office, Retail, Warehouse). |
| `Hotel/Motel` | A commercial structure designed to be a hotel or motel. |
| `House` | A single-family residence on real property either attached or detached from another structure. |
| `Industrial` | A commercial structure designed for industrial use. |
| `Manufactured House` | A factory-built house that is transported to a lot. |
| `Mixed Use` | The property is designed to be used in more than one way. |
| `Multi Family` | A structure or complex with five or more units that are individual dwellings. |
| `None` | The property has no structure. |
| `Office` | A commercial structure designed to be used as office space. |
| `Quadruplex` | A multifamily structure with four independent units sharing a common roof. |
| `Retail` | A commercial structure designed to be used for retail space. |
| `Townhouse` | A dwelling unit, generally having two or more floors and attached to other similar units via party walls. |
| `Triplex` | A multifamily structure with three independent units sharing a common roof. |
| `Warehouse` | A commercial structure designed for warehousing. |

### SyndicateTo

4 values · used by 3 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/SyndicateTo/)

| Value | Definition |
|---|---|
| `Homes.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Homes.com. |
| `ListHub` | The broker, or member if permitted by the broker, is allowing their listings to be sent to ListHub.com. |
| `Realtor.com` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Realtor.com. |
| `Zillow/Trulia` | The broker, or member if permitted by the broker, is allowing their listings to be sent to Zillow and Trulia. |

### TaxStatusCurrent

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/TaxStatusCurrent/)

| Value | Definition |
|---|---|
| `Personal` | The tax is based on personal property. |
| `Personal And Real` | The tax is based on both personal and real property. |
| `Real` | The tax is based on real property. |

### TenantPays

29 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/TenantPays/)

| Value | Definition |
|---|---|
| `All Utilities` | The tenant pays for all utilities. |
| `Association Fees` | The tenant pays for association fees. |
| `Cable TV` | The tenant pays for cable TV. |
| `Common Area Maintenance` | The tenant pays for common area maintenance. |
| `Electricity` | The tenant pays for electricity. |
| `Exterior Maintenance` | The tenant pays for exterior maintenance. |
| `Gas` | The tenant pays for gas. |
| `Grounds Care` | The tenant pays for grounds care. |
| `Hot Water` | The tenant pays for hot water. |
| `HVAC Maintenance` | The tenant pays for HVAC maintenance. |
| `Insurance` | The tenant pays for insurance. |
| `Janitorial Service` | The tenant pays for janitorial service. |
| `Management` | The tenant pays for management. |
| `None` | The tenant pays for no other utilities, services, etc. |
| `Other` | The tenant pays for items other than those on this list. |
| `Other Tax` | The tenant pays for other taxes. |
| `Parking Fee` | The tenant pays for parking fees. |
| `Pest Control` | The tenant pays for pest control. |
| `Pool Maintenance` | The tenant pays for pool maintenance. |
| `Repairs` | The tenant pays for repairs. |
| `Roof` | The tenant pays for roof maintenance. |
| `Security` | The tenant pays for security. |
| `See Remarks` | See listing remarks for details on what the tenant pays for. |
| `Sewer` | The tenant pays for sewer. |
| `Snow Removal` | The tenant pays for snow removal. |
| `Taxes` | The tenant pays for taxes. |
| `Telephone` | The tenant pays for telephone. |
| `Trash Collection` | The tenant pays for trash collection. |
| `Water` | The tenant pays for water. |

### UnitTypeType

10 values · used by 2 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/UnitTypeType/)

| Value | Definition |
|---|---|
| `1 Bedroom` | The type of unit has one bedroom. |
| `2 Bedroom` | The type of unit has two bedrooms. |
| `3 Bedroom` | The type of unit has three bedrooms. |
| `4 Bedroom Or More` | The type of unit has four or more bedrooms. |
| `Apartments` | The type of unit is apartments. |
| `Efficiency` | The type of unit is an efficiency. |
| `Loft` | The type of unit is a loft. |
| `Manager's Unit` | The type of unit is a manager's unit. |
| `Penthouse` | The type of unit is a penthouse. |
| `Studio` | The type of unit is a studio. |

### UnitsFurnished

3 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/UnitsFurnished/)

| Value | Definition |
|---|---|
| `All Units` | All of the units in the listed income property are furnished. |
| `None` | None of the units in the listed income property are furnished. |
| `Varies By Unit` | Some of the units in the listing income property are furnished. |

### Utilities

23 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Utilities/)

| Value | Definition |
|---|---|
| `Cable Available` | The property has cable available but is not connected. |
| `Cable Connected` | Cable service is physically connected but not necessarily paid. |
| `Cable Not Available` | Cable is not available in the area of the property. |
| `Electricity Available` | Electricity is available from the public utility but not connected. |
| `Electricity Connected` | Electricity from the public utility is available and connected but not necessarily paid. |
| `Electricity Not Available` | Electricity from the public utility is not available. |
| `Natural Gas Available` | Natural gas is available from the public utility but not connected. |
| `Natural Gas Connected` | Natural gas from the public utility is available and connected but not necessarily paid. |
| `Natural Gas Not Available` | Natural gas from the public utility is not available. |
| `None` | There are no public utilities currently available or connected. |
| `Other` | There are utilities other than those listed. |
| `Phone Available` | The property has telephone service available but is not connected. |
| `Phone Connected` | Telephone service is physically connected but not necessarily paid. |
| `Phone Not Available` | Telephone service is not available in the area of the property. |
| `Propane` | The property has a propane system. |
| `See Remarks` | See remarks for details about the public or other utilities available/installed at the property. |
| `Sewer Available` | Sewer service is available from the public utility but not connected. |
| `Sewer Connected` | Sewer service from the public utility is available and connected but not necessarily paid. |
| `Sewer Not Available` | Sewer service from the public utility is not available. |
| `Underground Utilities` | All or some of the utilities are run underground. |
| `Water Available` | Water service is available from the public utility but not connected. |
| `Water Connected` | Water service from the public utility is available and connected but not necessarily paid. |
| `Water Not Available` | Water service from the public utility is not available. |

### Vegetation

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/Vegetation/)

| Value | Definition |
|---|---|
| `Brush` | The lot has brush. |
| `Cleared` | The lot has been cleared. |
| `Crop(s)` | There are crops on the lot. |
| `Grassed` | The lot is grassed. |
| `Heavily Wooded` | The lot is heavily wooded. |
| `Natural State` | The lot is in its natural state. |
| `Other` | There are other types of vegetation on the lot than those on this list. |
| `Partially Wooded` | The lot is partially wooded. |
| `See Remarks` | See the public or private remarks for details about the vegetation found on the lot. |
| `Wooded` | The lot is wooded. |

### View

38 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/View/)

| Value | Definition |
|---|---|
| `Bay` | The property has a bay view. |
| `Beach` | The property has a beach view. |
| `Bridge(s)` | The property has a view of a bridge or bridges. |
| `Canal` | The property has a canal view. |
| `Canyon` | The property has a canyon view. |
| `City` | The property has a city view. |
| `City Lights` | The property has a view of city lights. |
| `Creek/Stream` | The property has a creek/stream view. |
| `Desert` | The property has a desert view. |
| `Downtown` | The property has a downtown view. |
| `Forest` | The property has a forest view. |
| `Garden` | The property has a garden view. |
| `Golf Course` | The property has a view of a golf course. |
| `Hills` | The property has a view of hills. |
| `Lake` | The property has a lake view. |
| `Marina` | The property has a marina view. |
| `Meadow` | The property has a view of a meadow. |
| `Mountain(s)` | The property has a mountain view. |
| `Neighborhood` | The property has a view of the surrounding neighborhood. |
| `None` | The property has no view. |
| `Ocean` | The property has an ocean view. |
| `Orchard` | The property has a view of the orchard(s). |
| `Other` | The property has a view other than those listed. |
| `Panoramic` | The property has a panoramic view. |
| `Park/Greenbelt` | The property has a park/greenbelt view. |
| `Pasture` | The property has a view of a pasture. |
| `Pond` | The property has a view of a pond. |
| `Pool` | The property has a view of a pool. |
| `Ridge` | The property has a view of a ridge. |
| `River` | The property has a river view. |
| `Rural` | The property has a rural view. |
| `See Remarks` | See the remarks fields for more information about the view from the property. |
| `Skyline` | The property has a skyline view. |
| `Territorial` | The property has a view of the surrounding area. |
| `Trees/Woods` | The property has a view of trees or woods. |
| `Valley` | The property has a view of a valley. |
| `Vineyard` | The property has a view of a vineyard. |
| `Water` | The property has a water view. |

### WaterSource

9 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/WaterSource/)

| Value | Definition |
|---|---|
| `Cistern` | The property's source of water has/includes a cistern. |
| `None` | The property has no current source of water. |
| `Other` | The property has a source of water other than those listed. |
| `Private` | The property's source of water is private. |
| `Public` | The property's source of water is public. |
| `See Remarks` | See the listing's remarks for details on the property's water source. |
| `Shared Well` | The property's source of water has/includes a shared well. |
| `Spring` | The property's source of water has/includes a spring. |
| `Well` | The property's source of water has/includes a well. |

### WaterfrontFeatures

20 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/WaterfrontFeatures/)

| Value | Definition |
|---|---|
| `Bay Access` | The property has access to a bay. |
| `Bayfront` | The property is on a bayfront. |
| `Beach Access` | The property has access to a beach. |
| `Beach Front` | The property is on a beachfront. |
| `Canal Access` | The property has access to a canal. |
| `Canal Front` | The property is located on a canal. |
| `Creek` | The property is either on or near a creek. |
| `Lagoon` | The property is either on or near a lagoon. |
| `Lake Front` | The property is on a lakefront. |
| `Lake Privileges` | The property includes rights to access a lake. |
| `Marina in Community` | This property has a marina in the community. |
| `Navigable Water` | The water can be navigated by water vessels. |
| `Ocean Access` | The property has access to an ocean. |
| `Ocean Front` | The property is on an oceanfront. |
| `Pond` | The property is on or near a pond. |
| `River Access` | The property has access to a river. |
| `River Front` | The property is located on a riverfront. |
| `Seawall` | The property is protected by a seawall or barrier. |
| `Stream` | The property is on or near a stream. |
| `Waterfront` | The property is located on a waterfront. |

### WindowFeatures

21 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/WindowFeatures/)

| Value | Definition |
|---|---|
| `Aluminum Frames` | The windows have aluminum frames. |
| `Bay Window(s)` | The property has one or more bay windows. |
| `Blinds` | The property has window blinds. |
| `Display Window(s)` | The property has one or more windows that would normally be used to display goods or products. |
| `Double Pane Windows` | The property has windows with two panes of glass. |
| `Drapes` | The property has drapes. |
| `ENERGY STAR Qualified Windows` | The property has qualified ENERGY STAR windows. |
| `Garden Window(s)` | The property has one or more garden windows. |
| `Insulated Windows` | The property has insulated windows. |
| `Low-Emissivity Windows` | The property has low-emissivity windows. |
| `Plantation Shutters` | The property has plantation shutters. |
| `Screens` | The property has screens. |
| `Shutters` | The property has shutters. |
| `Skylight(s)` | The property has skylights. |
| `Solar Screens` | The property has solar screens. |
| `Storm Window(s)` | The property has storm windows. |
| `Tinted Windows` | The property has tinted windows. |
| `Triple Pane Windows` | The property has triple-pane windows. |
| `Window Coverings` | The property has window coverings. |
| `Window Treatments` | The property has window treatments. |
| `Wood Frames` | The property has wood-framed windows. |

### YearBuiltSource

8 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/YearBuiltSource/)

| Value | Definition |
|---|---|
| `Appraiser` | An appraiser provided the year built. |
| `Assessor` | The assessor provided the year built. |
| `Builder` | The builder provided the year built. |
| `Estimated` | The year built is an estimate. |
| `Other` | The year built was provided by another party not listed. |
| `Owner` | The owner provided the year built. |
| `Public Records` | The year built was received from public records. |
| `See Remarks` | See remarks for information about the source of the lot size measurement. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
