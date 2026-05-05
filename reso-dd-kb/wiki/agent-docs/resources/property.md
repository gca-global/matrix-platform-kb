[index](../_index.md) | [lookups](../lookups.md) | [relationships](../relationships.md) | [USAGE.md](../../../USAGE.md)

# `property` (Property)

> Fields commonly used in a Multiple Listing Service (MLS) listing.

## At a glance

| | |
|---|---|
| **Primary key** | `listing_key` *(override; RESO uses `ListingKey`)* |
| **Fields on dd.reso.org** | 652 |
| **Columns in canonical DBML** | 512 (omits 120 satellite drops + 12 `Resource`-typed + 8 `Collection`-typed) |
| **Foreign keys OUT / IN** | 12 / 10 |
| **Review markers** | 2 |
| **Source** | [https://dd.reso.org/DD2.0/Property/](https://dd.reso.org/DD2.0/Property/) |
| **Last revised upstream** | 9/10/2019 |

## Fields

Columns in their original `dd.reso.org` page order. The `flags` column shows: `pk`, `fk -> target.col` (committed FK), `[REVIEW]` (Phase 2.5 satellite audit flagged for review), `[dropped]` (omitted from the canonical DBML; satellite of the named FK), `[Resource]` / `[Collection]` (no scalar column in DBML; FK companion - see Refs/inverse-1:N below).

| Field | DBML name | Type | Lookup | Description | Flags |
|---|---|---|---|---|---|
| `AboveGradeFinishedArea` | `above_grade_finished_area` | Number |  | The finished area within the structure that is at or above the surface of the ground. |  |
| `AboveGradeFinishedAreaSource` | `above_grade_finished_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements. |  |
| `AboveGradeFinishedAreaUnits` | `above_grade_finished_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). |  |
| `AboveGradeUnfinishedArea` | `above_grade_unfinished_area` | Number |  | The unfinished area within the structure that is at or above the surface of the ground. |  |
| `AboveGradeUnfinishedAreaSource` | `above_grade_unfinished_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements of the unfinished area above grade. |  |
| `AboveGradeUnfinishedAreaUnits` | `above_grade_unfinished_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the unfinished area above grade (e.g., Square Feet, Square Meters). |  |
| `AccessCode` | `access_code` | String |  | The code to gain access through the secured gate for a property located behind an unmanned security gate such as in a gated community. |  |
| `AccessibilityFeatures` | `accessibility_features` | varchar (multi) | [`accessibility_features`](../lookups.md#accessibility_features) | A list or description of the accessibility features included in the sale/lease. |  |
| `ActivationDate` | `activation_date` | Date |  | Indicates when the listing agent intends to change the property to the Active status. |  |
| `AdditionalParcelsDescription` | `additional_parcels_description` | String |  | If additional parcels are included in the sale, a list of those parcel's IDs separated by commas. |  |
| `AdditionalParcelsYN` | `additional_parcels_yn` | Boolean |  | Indicates whether or not more than one parcel or lot is included in the sale. |  |
| `AnchorsCoTenants` | `anchors_co_tenants` | String |  | The main or most notable tenants as well as other tenants of the shopping center or mall in which the commercial property is located. |  |
| `Appliances` | `appliances` | varchar (multi) | [`appliances`](../lookups.md#appliances) | A list of the appliances that will be included in the sale/lease of the property. |  |
| `ArchitecturalStyle` | `architectural_style` | varchar (multi) | [`architectural_style`](../lookups.md#architectural_style) | A list describing the style of the structure (e.g., Victorian, Ranch, Craftsman). |  |
| `AssociationAmenities` | `association_amenities` | varchar (multi) | [`association_amenities`](../lookups.md#association_amenities) | The amenities provided by the homeowner association, mobile park or complex (e.g., pool, clubhouse). |  |
| `AssociationFee` | `association_fee` | Number |  | A fee paid by the homeowner to the homeowner association that is used for upkeep of common areas, the neighborhood or other association-related benefits. |  |
| `AssociationFee2` | `association_fee2` | Number |  | A fee paid by the homeowner to the second of two homeowner associations that is used for upkeep of common areas, the neighborhood or other association-related benefits. |  |
| `AssociationFee2Frequency` | `association_fee2_frequency` | enum | [`fee_frequency`](../lookups.md#fee_frequency) | The frequency the association fee is paid (e.g., weekly, monthly, annually, bimonthly, one time). |  |
| `AssociationFeeFrequency` | `association_fee_frequency` | enum | [`fee_frequency`](../lookups.md#fee_frequency) | The frequency the association fee is paid (e.g., weekly, monthly, annually, bimonthly, one time). |  |
| `AssociationFeeIncludes` | `association_fee_includes` | varchar (multi) | [`association_fee_includes`](../lookups.md#association_fee_includes) | The services included with the association fee (e.g., landscaping, trash, water). |  |
| `AssociationName` | `association_name` | String |  | The name of the homeowner association. |  |
| `AssociationName2` | `association_name2` | String |  | The name of the second of two homeowner associations. |  |
| `AssociationPhone` | `association_phone` | String |  | The phone number of the homeowner association. |  |
| `AssociationPhone2` | `association_phone2` | String |  | The phone number of the second of two homeowner associations. |  |
| `AssociationYN` | `association_yn` | Boolean |  | Indicates whether there is a homeowner association. |  |
| `AttachedGarageYN` | `attached_garage_yn` | Boolean |  | A flag indicating whether or not the garage is attached to the dwelling. |  |
| `AttributionContact` | `attribution_contact` | String |  | A text field to convey a specific contact phone number or email address for the listing firm. |  |
| `AvailabilityDate` | `availability_date` | Date |  | The date the property will be available for possession/occupation. |  |
| `AvailableLeaseType` | `available_lease_type` | varchar (multi) | [`existing_lease_type`](../lookups.md#existing_lease_type) | Information about the available types of lease for the property (i.e., Net, NNN, NN, Gross, Absolute Net, Escalation Clause, Ground Lease, etc.). |  |
| `BackOnMarketDate` | `back_on_market_date` | Date |  | The date a listing, which had previously gone off market, went back to being on market. |  |
| `Basement` | `basement` | varchar (multi) | [`basement`](../lookups.md#basement) | A list of information and features about the basement (i.e., None/Slab, Finished, Partially Finished, Crawl Space, Dirt, Outside Entrance, Radon Mitigation). |  |
| `BasementYN` | `basement_yn` | Boolean |  | Indicates whether or not the property has a basement. |  |
| `BathroomsFull` | `bathrooms_full` | Number |  | A room containing all four of the four elements constituting a bath: toilet, sink, bathtub, shower head (in tub or stall). |  |
| `BathroomsHalf` | `bathrooms_half` | Number |  | A room containing two of the four elements constituting a bath: toilet, sink, bathtub, shower head (in a tub or stall). |  |
| `BathroomsOneQuarter` | `bathrooms_one_quarter` | Number |  | A room containing one of the four elements constituting a bath: toilet, sink, bathtub, shower head (in tub or stall). |  |
| `BathroomsPartial` | `bathrooms_partial` | Number |  | The number of partial bathrooms in the property being sold/leased. |  |
| `BathroomsThreeQuarter` | `bathrooms_three_quarter` | Number |  | A room containing three of the four elements constituting a bath: toilet, sink, bathtub, shower head (in a tub or stall). |  |
| `BathroomsTotalInteger` | `bathrooms_total_integer` | Number |  | The simple sum of the number of bathrooms. |  |
| `BedroomsPossible` | `bedrooms_possible` | Number |  | The sum of BedroomsTotal plus other rooms that may be used as a bedroom but are not defined as a bedroom per local policy. |  |
| `BedroomsTotal` | `bedrooms_total` | Number |  | The total number of bedrooms in the dwelling. |  |
| `BelowGradeFinishedArea` | `below_grade_finished_area` | Number |  | The finished area within the structure that is below ground. |  |
| `BelowGradeFinishedAreaSource` | `below_grade_finished_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements. |  |
| `BelowGradeFinishedAreaUnits` | `below_grade_finished_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). |  |
| `BelowGradeUnfinishedArea` | `below_grade_unfinished_area` | Number |  | The unfinished area within the structure that is below ground. |  |
| `BelowGradeUnfinishedAreaSource` | `below_grade_unfinished_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements of the unfinished area below grade. |  |
| `BelowGradeUnfinishedAreaUnits` | `below_grade_unfinished_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the unfinished area below grade (e.g., Square Feet, Square Meters). |  |
| `BodyType` | `body_type` | varchar (multi) | [`body_type`](../lookups.md#body_type) | The type of mobile home. |  |
| `BuilderModel` | `builder_model` | String |  | The builder's model name or number for the property. |  |
| `BuilderName` | `builder_name` | String |  | The name of the builder of the property or builder's tract. |  |
| `BuildingAreaSource` | `building_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements. |  |
| `BuildingAreaTotal` | `building_area_total` | Number |  | The total area of the structure, including both finished and unfinished areas. |  |
| `BuildingAreaUnits` | `building_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). |  |
| `BuildingFeatures` | `building_features` | varchar (multi) | [`building_features`](../lookups.md#building_features) | The features or amenities of the building or business park. |  |
| `BuildingName` | `building_name` | String |  | The name of the building or business park. |  |
| `BusinessName` | `business_name` | String |  | The name of the business being sold. |  |
| `BusinessType` | `business_type` | varchar (multi) | [`business_type`](../lookups.md#business_type) | The type of business being sold (e.g., Retail, Wholesale, Grocery, Food & Bev). |  |
| `BuyerAgent` | `buyer_agent` | Resource |  | The buyer's agent involved in the transaction. | `[Resource]` |
| `BuyerAgentAOR` | `buyer_agent_aor` | enum | [`aor`](../lookups.md#aor) | The buyer agent's board or association of REALTORS®. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentDesignation` | `buyer_agent_designation` | varchar (multi) | [`buyer_agent_designation`](../lookups.md#buyer_agent_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completion of required courses. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentDirectPhone` | `buyer_agent_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentEmail` | `buyer_agent_email` | String |  | The email address of the buyer's agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentFax` | `buyer_agent_fax` | String |  | The North American 10-digit fax numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentFirstName` | `buyer_agent_first_name` | String |  | The first name of the buyer's agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentFullName` | `buyer_agent_full_name` | String |  | The first, middle and last name of the buyer's agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentHomePhone` | `buyer_agent_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentKey` | `buyer_agent_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `BuyerAgentLastName` | `buyer_agent_last_name` | String |  | The last name of the buyer's agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentMiddleName` | `buyer_agent_middle_name` | String |  | The middle name of the buyer's agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentMlsId` | `buyer_agent_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentMobilePhone` | `buyer_agent_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentNamePrefix` | `buyer_agent_name_prefix` | String |  | The prefix to the name (e.g., Dr., Mr., Ms.). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentNameSuffix` | `buyer_agent_name_suffix` | String |  | The suffix to the name (e.g., Esq., Jr., III). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentNationalAssociationId` | `buyer_agent_national_association_id` | String |  | The national association ID of the buyer's agent (e.g., the NRDS number in the U.S.). |  |
| `BuyerAgentOfficePhone` | `buyer_agent_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentOfficePhoneExt` | `buyer_agent_office_phone_ext` | String |  | The extension of the given phone number (if applicable). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentPager` | `buyer_agent_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentPreferredPhone` | `buyer_agent_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentPreferredPhoneExt` | `buyer_agent_preferred_phone_ext` | String |  | The extension of the given phone number (if applicable). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentStateLicense` | `buyer_agent_state_license` | String |  | The license of the buyer agent. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentTollFreePhone` | `buyer_agent_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentURL` | `buyer_agent_url` | String |  | The website Uniform Resource Identifier (URI) of the buyers agent. |  |
| `BuyerAgentVoiceMail` | `buyer_agent_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_agent_key]` |
| `BuyerAgentVoiceMailExt` | `buyer_agent_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of buyer_agent_key]` |
| `BuyerBrokerageCompensation` | `buyer_brokerage_compensation` | String |  | The total compensation to be paid to the buyer's brokerage for this sale, expressed as either a percentage or a constant currency amount. |  |
| `BuyerBrokerageCompensationType` | `buyer_brokerage_compensation_type` | enum | [`compensation_type`](../lookups.md#compensation_type) | A list of types to clarify the value entered in the BuyerBrokerageCompensation field. |  |
| `BuyerFinancing` | `buyer_financing` | varchar (multi) | [`buyer_financing`](../lookups.md#buyer_financing) | A list of options that describe the type of financing used. |  |
| `BuyerOffice` | `buyer_office` | Resource |  | The buyer agent's office. | `[Resource]` |
| `BuyerOfficeAOR` | `buyer_office_aor` | enum | [`aor`](../lookups.md#aor) | The buyer's office's board or association of REALTORS®. | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeEmail` | `buyer_office_email` | String |  | The email address of the buyer's office. | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeFax` | `buyer_office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeKey` | `buyer_office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `BuyerOfficeMlsId` | `buyer_office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeName` | `buyer_office_name` | String |  | The legal name of the brokerage representing the buyer. | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeNationalAssociationId` | `buyer_office_national_association_id` | String |  | The national association ID of the buyer's office (e.g., the NRDS number in the U.S.). |  |
| `BuyerOfficePhone` | `buyer_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficePhoneExt` | `buyer_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of buyer_office_key]` |
| `BuyerOfficeURL` | `buyer_office_url` | String |  | The website Uniform Resource Identifier (URI) for the buyers office. |  |
| `BuyerTeam` | `buyer_team` | Resource |  | Two or more agents working on the buyer agent's team. | `[Resource]` |
| `BuyerTeamKey` | `buyer_team_key` | String |  | A system unique identifier. | `-> teams.team_key` |
| `BuyerTeamName` | `buyer_team_name` | String |  | The name of the team representing the buyer. | `[REVIEW]` |
| `CableTvExpense` | `cable_tv_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `CancellationDate` | `cancellation_date` | Date |  | The date that the listing contract between the seller and listing agent was canceled. |  |
| `CapRate` | `cap_rate` | Number |  | The equivalent to the return on investment you would receive if you pay cash for a property. |  |
| `CarportSpaces` | `carport_spaces` | Number |  | The number of carport spaces included in the sale. |  |
| `CarportYN` | `carport_yn` | Boolean |  | A flag indicating that the listing has a carport. |  |
| `CarrierRoute` | `carrier_route` | String |  | The group of addresses to which the U.S. |  |
| `City` | `city` | enum | [`city`](../lookups.md#city) | The city in the listing address. |  |
| `CityRegion` | `city_region` | String |  | A subsection or area of a defined city (e.g., SOHO in New York, NY; Ironbound in Newark, NJ; Inside the Beltway). |  |
| `CloseDate` | `close_date` | Date |  | With for-sale listings, this is the date the purchase agreement was fulfilled. |  |
| `ClosePrice` | `close_price` | Number |  | The amount of money paid by the purchaser to the seller for the property under the agreement. |  |
| `CoBuyerAgent` | `co_buyer_agent` | Resource |  | The co-buyer's agent involved in the transaction. | `[Resource]` |
| `CoBuyerAgentAOR` | `co_buyer_agent_aor` | enum | [`aor`](../lookups.md#aor) | The co-buyer agent's board or association of REALTORS®. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentDesignation` | `co_buyer_agent_designation` | varchar (multi) | [`co_buyer_agent_designation`](../lookups.md#co_buyer_agent_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completion of required courses. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentDirectPhone` | `co_buyer_agent_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentEmail` | `co_buyer_agent_email` | String |  | The email address of the buyer's co-agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentFax` | `co_buyer_agent_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentFirstName` | `co_buyer_agent_first_name` | String |  | The first name of the buyer's co-agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentFullName` | `co_buyer_agent_full_name` | String |  | The first, middle and last name of the buyer's co-agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentHomePhone` | `co_buyer_agent_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentKey` | `co_buyer_agent_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `CoBuyerAgentLastName` | `co_buyer_agent_last_name` | String |  | The last name of the buyer's co-agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentMiddleName` | `co_buyer_agent_middle_name` | String |  | The middle name of the buyer's co-agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentMlsId` | `co_buyer_agent_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentMobilePhone` | `co_buyer_agent_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentNamePrefix` | `co_buyer_agent_name_prefix` | String |  | The prefix to the name (e.g., Dr., Mr., Ms.). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentNameSuffix` | `co_buyer_agent_name_suffix` | String |  | The suffix to the name (e.g., Esq., Jr., III). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentNationalAssociationId` | `co_buyer_agent_national_association_id` | String |  | The national association ID of the co-buyer's agent (e.g., the NRDS number in the U.S.). |  |
| `CoBuyerAgentOfficePhone` | `co_buyer_agent_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentOfficePhoneExt` | `co_buyer_agent_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentPager` | `co_buyer_agent_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentPreferredPhone` | `co_buyer_agent_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentPreferredPhoneExt` | `co_buyer_agent_preferred_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentStateLicense` | `co_buyer_agent_state_license` | String |  | The license of the co-buyers' agent. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentTollFreePhone` | `co_buyer_agent_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentURL` | `co_buyer_agent_url` | String |  | The website Uniform Resource Identifier (URI) of the co-buyers agent. |  |
| `CoBuyerAgentVoiceMail` | `co_buyer_agent_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerAgentVoiceMailExt` | `co_buyer_agent_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_buyer_agent_key]` |
| `CoBuyerOffice` | `co_buyer_office` | Resource |  | The co-buyer agent's office. | `[Resource]` |
| `CoBuyerOfficeAOR` | `co_buyer_office_aor` | enum | [`aor`](../lookups.md#aor) | The co-buyer's office's board or association of REALTORS®. | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeEmail` | `co_buyer_office_email` | String |  | The email address of the buyer's co-office. | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeFax` | `co_buyer_office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeKey` | `co_buyer_office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `CoBuyerOfficeMlsId` | `co_buyer_office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeName` | `co_buyer_office_name` | String |  | The legal name of the brokerage co-representing the buyer. | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeNationalAssociationId` | `co_buyer_office_national_association_id` | String |  | The national association ID of the co-buyer's office (e.g., the NRDS number in the U.S.). |  |
| `CoBuyerOfficePhone` | `co_buyer_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficePhoneExt` | `co_buyer_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_buyer_office_key]` |
| `CoBuyerOfficeURL` | `co_buyer_office_url` | String |  | The website Uniform Resource Identifier (URI) for the co-buyer's office. |  |
| `CoListAgent` | `co_list_agent` | Resource |  | The co-listing agent involved in the transaction. | `[Resource]` |
| `CoListAgentAOR` | `co_list_agent_aor` | enum | [`aor`](../lookups.md#aor) | The Co-listing Agent's board or association of REALTORS®. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentDesignation` | `co_list_agent_designation` | varchar (multi) | [`co_list_agent_designation`](../lookups.md#co_list_agent_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® and each affiliated group upon completion of required courses. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentDirectPhone` | `co_list_agent_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentEmail` | `co_list_agent_email` | String |  | The email address of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentFax` | `co_list_agent_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentFirstName` | `co_list_agent_first_name` | String |  | The first name of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentFullName` | `co_list_agent_full_name` | String |  | The first, middle and last name of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentHomePhone` | `co_list_agent_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentKey` | `co_list_agent_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `CoListAgentLastName` | `co_list_agent_last_name` | String |  | The last name of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentMiddleName` | `co_list_agent_middle_name` | String |  | The middle name of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentMlsId` | `co_list_agent_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentMobilePhone` | `co_list_agent_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentNamePrefix` | `co_list_agent_name_prefix` | String |  | The prefix to the name (e.g., Dr., Mr., Ms.). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentNameSuffix` | `co_list_agent_name_suffix` | String |  | The suffix to the name (e.g., Esq., Jr., III). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentNationalAssociationId` | `co_list_agent_national_association_id` | String |  | The national association ID of the co-listing agent (e.g., the NRDS number in the U.S.). |  |
| `CoListAgentOfficePhone` | `co_list_agent_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentOfficePhoneExt` | `co_list_agent_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentPager` | `co_list_agent_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentPreferredPhone` | `co_list_agent_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentPreferredPhoneExt` | `co_list_agent_preferred_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentStateLicense` | `co_list_agent_state_license` | String |  | The license of the co-listing agent. | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentTollFreePhone` | `co_list_agent_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentURL` | `co_list_agent_url` | String |  | The website Uniform Resource Identifier (URI) of the co-listing agent. |  |
| `CoListAgentVoiceMail` | `co_list_agent_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_agent_key]` |
| `CoListAgentVoiceMailExt` | `co_list_agent_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_list_agent_key]` |
| `CoListOffice` | `co_list_office` | Resource |  | The co-listing agent's office. | `[Resource]` |
| `CoListOfficeAOR` | `co_list_office_aor` | enum | [`aor`](../lookups.md#aor) | The co-listing office's board or association of REALTORS®. | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeEmail` | `co_list_office_email` | String |  | The email address of the co-listing office. | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeFax` | `co_list_office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeKey` | `co_list_office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `CoListOfficeMlsId` | `co_list_office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeName` | `co_list_office_name` | String |  | The legal name of the brokerage co-representing the seller. | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeNationalAssociationId` | `co_list_office_national_association_id` | String |  | The national association ID of the co-listing office (e.g., the NRDS number in the U.S.). |  |
| `CoListOfficePhone` | `co_list_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficePhoneExt` | `co_list_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of co_list_office_key]` |
| `CoListOfficeURL` | `co_list_office_url` | String |  | The website Uniform Resource Identifier (URI) for the co-listing office. |  |
| `CommonInterest` | `common_interest` | enum | [`common_interest`](../lookups.md#common_interest) | A type of ownership in a property that is composed of an individual lot or unit and a share of the ownership or use of common areas. |  |
| `CommonWalls` | `common_walls` | varchar (multi) | [`common_walls`](../lookups.md#common_walls) | A multi-select list with options like 1 Common Wall, 2 Common Walls, No Common Walls, No One Above, No One Below. |  |
| `CommunityFeatures` | `community_features` | varchar (multi) | [`community_features`](../lookups.md#community_features) | A list of features related to or available within the community. |  |
| `CompSaleYN` | `comp_sale_yn` | Boolean |  | Indicates whether or not this sale was entered for comparative purposes. |  |
| `CompensationComments` | `compensation_comments` | String |  | A textual description of the compensation involved in the transaction. |  |
| `Concessions` | `concessions` | enum | [`concessions`](../lookups.md#concessions) | Indicates whether or not there are concessions included in the sales agreement (i.e., Yes, No or Call Listing Agent). |  |
| `ConcessionsAmount` | `concessions_amount` | Number |  | The dollar amount of the concessions. |  |
| `ConcessionsComments` | `concessions_comments` | String |  | The comments describing the concessions made by the buyer or the seller. |  |
| `ConstructionMaterials` | `construction_materials` | varchar (multi) | [`construction_materials`](../lookups.md#construction_materials) | A list of the materials that were used in the construction of the property. |  |
| `ContinentRegion` | `continent_region` | String |  | A subsection or area of a continent (e.g., Southern Europe, Scandinavia). |  |
| `Contingency` | `contingency` | String |  | A list of contingencies that must be satisfied in order to complete the transaction. |  |
| `ContingentDate` | `contingent_date` | Date |  | The date an offer was made with a contingency. |  |
| `ContractStatusChangeDate` | `contract_status_change_date` | Date |  | The date of the listing's contractual status change. |  |
| `Cooling` | `cooling` | varchar (multi) | [`cooling`](../lookups.md#cooling) | A list describing the cooling or air conditioning features of the property. |  |
| `CoolingYN` | `cooling_yn` | Boolean |  | Indicates whether or not the property has some form of cooling or air conditioning. |  |
| `CopyrightNotice` | `copyright_notice` | String |  | A notice of the legal rights of the owner of the information or data. |  |
| `Country` | `country` | enum | [`country`](../lookups.md#country) | The country abbreviation in a postal address. |  |
| `CountryRegion` | `country_region` | String |  | A subsection or area of a defined country (e.g., Napa Valley in the U.S., the Amalfi Coast in Italy). |  |
| `CountyOrParish` | `county_or_parish` | enum | [`county_or_parish`](../lookups.md#county_or_parish) | The county, parish or other regional authority. |  |
| `CoveredSpaces` | `covered_spaces` | Number |  | The total number of garage and carport spaces. |  |
| `CropsIncludedYN` | `crops_included_yn` | Boolean |  | Indicates whether or not crops are included in the sale of the property. |  |
| `CrossStreet` | `cross_street` | String |  | The nearest cross streets to the property. |  |
| `CultivatedArea` | `cultivated_area` | Number |  | The measurement or percentage of the property that has been cultivated. |  |
| `CumulativeDaysOnMarket` | `cumulative_days_on_market` | Number |  | The cumulative number of days the property is on market, as defined by the MLS business rules. |  |
| `CurrentFinancing` | `current_financing` | varchar (multi) | [`current_financing`](../lookups.md#current_financing) | A list of options that describe the type of financing that the seller currently has in place for the property being sold (i.e., Cash, FHA Loan, etc.). |  |
| `CurrentUse` | `current_use` | varchar (multi) | [`current_or_possible_use`](../lookups.md#current_or_possible_use) | A list of the type(s) of current use of the property. |  |
| `DOH1` | `doh1` | String |  | The Department of Housing decal number for the mobile or manufactured home. |  |
| `DOH2` | `doh2` | String |  | The Department of Housing decal number for the mobile or manufactured home. |  |
| `DOH3` | `doh3` | String |  | The Department of Housing decal number for the mobile or manufactured home. |  |
| `DaysInMls` | `days_in_mls` | Number |  | The number of days the listing was on market within the MLS system. |  |
| `DaysOnMarket` | `days_on_market` | Number |  | The number of days the listing is on market, as defined by the MLS business rules. |  |
| `DaysOnSite` | `days_on_site` | Number |  | The number of days the listing appeared on the given site, typically a public portal. |  |
| `DevelopmentStatus` | `development_status` | varchar (multi) | [`development_status`](../lookups.md#development_status) | A list of the development status of the property, which is an important factor in selling, purchasing and developing land properties. |  |
| `DirectionFaces` | `direction_faces` | enum | [`direction_faces`](../lookups.md#direction_faces) | The compass direction that the main entrance to the building faces (e.g., North, South, East, West, Northeast, Southwest). |  |
| `Directions` | `directions` | String |  | Driving directions to the property. |  |
| `Disclaimer` | `disclaimer` | String |  | Text that serves as the negation or limitation of the rights under a warranty given by a seller to a buyer. |  |
| `Disclosures` | `disclosures` | varchar (multi) | [`disclosures`](../lookups.md#disclosures) | Legal or pertinent information that should be disclosed to potential buyer's agents. |  |
| `DistanceToBusComments` | `distance_to_bus_comments` | String |  | A textual description of the distance to local bus stops. |  |
| `DistanceToBusNumeric` | `distance_to_bus_numeric` | Number |  | The numeric distance from the property to the nearest bus stop. |  |
| `DistanceToBusUnits` | `distance_to_bus_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToElectricComments` | `distance_to_electric_comments` | String |  | Provides details about the property's access to serviceable electrical utility and the distance to it. |  |
| `DistanceToElectricNumeric` | `distance_to_electric_numeric` | Number |  | The numeric distance from the property to the electrical utility. |  |
| `DistanceToElectricUnits` | `distance_to_electric_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToFreewayComments` | `distance_to_freeway_comments` | String |  | A textual description of the distance to freeways. |  |
| `DistanceToFreewayNumeric` | `distance_to_freeway_numeric` | Number |  | The numeric distance from the property to the nearest freeway. |  |
| `DistanceToFreewayUnits` | `distance_to_freeway_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToGasComments` | `distance_to_gas_comments` | String |  | Provides details about the property's access to serviceable natural gas utility and the distance to it. |  |
| `DistanceToGasNumeric` | `distance_to_gas_numeric` | Number |  | The numeric distance from the property to the gas utility. |  |
| `DistanceToGasUnits` | `distance_to_gas_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToPhoneServiceComments` | `distance_to_phone_service_comments` | String |  | Provides details about the property's access to phone service and the distance to it. |  |
| `DistanceToPhoneServiceNumeric` | `distance_to_phone_service_numeric` | Number |  | The numeric distance from the property to the phone utility. |  |
| `DistanceToPhoneServiceUnits` | `distance_to_phone_service_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToPlaceofWorshipComments` | `distance_to_placeof_worship_comments` | String |  | A textual description of the distance to local places of worship. |  |
| `DistanceToPlaceofWorshipNumeric` | `distance_to_placeof_worship_numeric` | Number |  | The numeric distance from the property to the nearest place of worship. |  |
| `DistanceToPlaceofWorshipUnits` | `distance_to_placeof_worship_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToSchoolBusComments` | `distance_to_school_bus_comments` | String |  | Distance from the property to the nearest school bus pickup point. |  |
| `DistanceToSchoolBusNumeric` | `distance_to_school_bus_numeric` | Number |  | The numeric distance from the property to the nearest school bus pickup point. |  |
| `DistanceToSchoolBusUnits` | `distance_to_school_bus_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToSchoolsComments` | `distance_to_schools_comments` | String |  | A textual description of the distance to local schools. |  |
| `DistanceToSchoolsNumeric` | `distance_to_schools_numeric` | Number |  | The numeric distance from the property to the nearest school. |  |
| `DistanceToSchoolsUnits` | `distance_to_schools_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToSewerComments` | `distance_to_sewer_comments` | String |  | Provides details about the property's access to sewer or septic service and the distance to it. |  |
| `DistanceToSewerNumeric` | `distance_to_sewer_numeric` | Number |  | The numeric distance from the property to the sewer utility. |  |
| `DistanceToSewerUnits` | `distance_to_sewer_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToShoppingComments` | `distance_to_shopping_comments` | String |  | A description of the distance to primary shopping sources, such as groceries, gasoline, clothing or department stores. |  |
| `DistanceToShoppingNumeric` | `distance_to_shopping_numeric` | Number |  | The numeric distance from the property to the nearest shopping. |  |
| `DistanceToShoppingUnits` | `distance_to_shopping_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToStreetComments` | `distance_to_street_comments` | String |  | Provides details about the property's access to a maintained road or street adjacent to the lot, conditions of access and distance to a maintained road. |  |
| `DistanceToStreetNumeric` | `distance_to_street_numeric` | Number |  | The numeric distance from the property to the street. |  |
| `DistanceToStreetUnits` | `distance_to_street_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DistanceToWaterComments` | `distance_to_water_comments` | String |  | Provides details about the property's access to serviceable water utility and the distance to it. |  |
| `DistanceToWaterNumeric` | `distance_to_water_numeric` | Number |  | The numeric distance from the property to the water utility. |  |
| `DistanceToWaterUnits` | `distance_to_water_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit linear measurement (i.e., Feet, Meters, Yards, Kilometers, Miles, etc.). |  |
| `DocumentStatus` | `document_status` | enum | [`document_status`](../lookups.md#document_status) | The statuses a document could be in during a transaction. |  |
| `DocumentsAvailable` | `documents_available` | varchar (multi) | [`documents_available`](../lookups.md#documents_available) | A list of the documents available for the property. |  |
| `DocumentsChangeTimestamp` | `documents_change_timestamp` | Timestamp |  | The system-generated timestamp of when the last update or change to the documents for this listing was made. |  |
| `DocumentsCount` | `documents_count` | Number |  | The total number of documents or supplements included with the listing. |  |
| `DoorFeatures` | `door_features` | varchar (multi) | [`door_features`](../lookups.md#door_features) | A list of features or description of the doors included in the sale/lease. |  |
| `DualOrVariableRateCommissionYN` | `dual_or_variable_rate_commission_yn` | Boolean |  | A commission arrangement in which the seller agrees to pay a specified commission to the listing broker if the property is sold through the efforts of a cooperating broker. |  |
| `Electric` | `electric` | varchar (multi) | [`electric`](../lookups.md#electric) | A list of electric-service related features of the property (e.g., 110 Volt, 3 Phase, 220 Volt, RV Hookup). |  |
| `ElectricExpense` | `electric_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `ElectricOnPropertyYN` | `electric_on_property_yn` | Boolean |  | Indicates whether or not the property currently has electrical utility available on the property. |  |
| `ElementarySchool` | `elementary_school` | enum | [`elementary_school`](../lookups.md#elementary_school) | The name of the primary school having a catchment area that includes the associated property. |  |
| `ElementarySchoolDistrict` | `elementary_school_district` | enum | [`elementary_school_district`](../lookups.md#elementary_school_district) | The name of the elementary school district having a catchment area that includes the associated property. |  |
| `Elevation` | `elevation` | Number |  | The elevation of the property in relation to sea level. |  |
| `ElevationUnits` | `elevation_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit of measurement used in the Elevation field (i.e., Feet, Meters). |  |
| `EntryLevel` | `entry_level` | Number |  | A numeric field that describes the level within the structure, single-family residence (SFR) or a unit in a building, where the main entry to the dwelling is located. |  |
| `EntryLocation` | `entry_location` | String |  | A description of the main entryway to the property (e.g., elevator, ground level w/ steps, ground level w/o steps, top level). |  |
| `Exclusions` | `exclusions` | String |  | Elements of the property that will not be included in the sale (e.g., chandeliers removed prior to close). |  |
| `ExistingLeaseType` | `existing_lease_type` | varchar (multi) | [`existing_lease_type`](../lookups.md#existing_lease_type) | Information about the status of the existing lease on the property (i.e., Net, NNN, NN, Gross, Absolute Net, Escalation Clause, Ground Lease). |  |
| `ExpirationDate` | `expiration_date` | Date |  | The date when the listing agreement will expire. |  |
| `ExteriorFeatures` | `exterior_features` | varchar (multi) | [`exterior_features`](../lookups.md#exterior_features) | A list of features or a description of the exterior of the property included in the sale/lease. |  |
| `FarmCreditServiceInclYN` | `farm_credit_service_incl_yn` | Boolean |  | Indicates whether or not Farm Credit Service shares are included in the price of the property. |  |
| `FarmLandAreaSource` | `farm_land_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements. |  |
| `FarmLandAreaUnits` | `farm_land_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (i.e., Square Feet, Square Meters, Acres, etc.). |  |
| `Fencing` | `fencing` | varchar (multi) | [`fencing`](../lookups.md#fencing) | A list of types of fencing found at the property being sold. |  |
| `FhaEligibility` | `fha_eligibility` | enum | [`fha_eligibility`](../lookups.md#fha_eligibility) | The status of the property's FHA eligibility. |  |
| `FinancialDataSource` | `financial_data_source` | varchar (multi) | [`financial_data_source`](../lookups.md#financial_data_source) | The source of the rental information (e.g., Accountant, Owner). |  |
| `FireplaceFeatures` | `fireplace_features` | varchar (multi) | [`fireplace_features`](../lookups.md#fireplace_features) | A list of features or a description of the fireplace(s) included in the sale/lease. |  |
| `FireplaceYN` | `fireplace_yn` | Boolean |  | Does the property include a fireplace. |  |
| `FireplacesTotal` | `fireplaces_total` | Number |  | Indicates whether or not the property includes a fireplace. |  |
| `Flooring` | `flooring` | varchar (multi) | [`flooring`](../lookups.md#flooring) | A list of the type(s) of flooring found within the property. |  |
| `FoundationArea` | `foundation_area` | Number |  | The area or dimensions of the footprint of the structure on the lot. |  |
| `FoundationDetails` | `foundation_details` | varchar (multi) | [`foundation_details`](../lookups.md#foundation_details) | A list of the type(s) of foundation on which the property sits. |  |
| `FrontageLength` | `frontage_length` | String |  | A textual description of the length of the frontages selected in the Frontage Type field. |  |
| `FrontageType` | `frontage_type` | varchar (multi) | [`frontage_type`](../lookups.md#frontage_type) | A pick list of types of frontage (i.e., Oceanfront, Lakefront, Golf Course, etc.). |  |
| `FuelExpense` | `fuel_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `Furnished` | `furnished` | enum | [`furnished`](../lookups.md#furnished) | The property being leased is furnished, unfurnished or partially furnished. |  |
| `FurnitureReplacementExpense` | `furniture_replacement_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `GarageSpaces` | `garage_spaces` | Number |  | The number of spaces in the garage(s). |  |
| `GarageYN` | `garage_yn` | Boolean |  | A flag that indicates whether or not the listing has a garage. |  |
| `GardenerExpense` | `gardener_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `GrazingPermitsBlmYN` | `grazing_permits_blm_yn` | Boolean |  | Indicates whether or not the property owner has grazing permits from the Bureau of Land Management. |  |
| `GrazingPermitsForestServiceYN` | `grazing_permits_forest_service_yn` | Boolean |  | Indicates whether or not the property owner has grazing permits from the Forestry Service. |  |
| `GrazingPermitsPrivateYN` | `grazing_permits_private_yn` | Boolean |  | Indicates whether or not the property owner has private grazing permits. |  |
| `GreenBuildingVerification` | `green_building_verification` | Collection |  | A collection of verifications or certifications awarded to a new or pre-existing residential or commercial structure (e.g., LEED, Energy Star, ICC-700). | `[Collection]` |
| `GreenBuildingVerificationType` | `green_building_verification_type` | varchar (multi) | [`green_building_verification_type`](../lookups.md#green_building_verification_type) | A list of available verifications and certifications awarded to a new or pre-existing residential or commercial structures (e.g., LEED, ENERGY STAR, ICC-700). |  |
| `GreenEnergyEfficient` | `green_energy_efficient` | varchar (multi) | [`green_energy_efficient`](../lookups.md#green_energy_efficient) | A pick list of general green attributes such as energy efficient doors or appliances without naming specific elements with ratings that may wane over time. |  |
| `GreenEnergyGeneration` | `green_energy_generation` | varchar (multi) | [`green_energy_generation`](../lookups.md#green_energy_generation) | The methods of generating power that are included in the sale or lease. |  |
| `GreenIndoorAirQuality` | `green_indoor_air_quality` | varchar (multi) | [`green_indoor_air_quality`](../lookups.md#green_indoor_air_quality) | A pick list of indoor air quality measures without naming specific elements with ratings that may wane over time. |  |
| `GreenLocation` | `green_location` | varchar (multi) | [`green_location`](../lookups.md#green_location) | A pick list describing efficiencies involved with the property's location such as walkability or transportation proximity without naming specific elements with ratings that may wane over time. |  |
| `GreenSustainability` | `green_sustainability` | varchar (multi) | [`green_sustainability`](../lookups.md#green_sustainability) | A pick list of sustainable elements used in the construction of the structure without naming specific elements with ratings that may wane over time. |  |
| `GreenVerificationYN` | `green_verification_yn` | Boolean |  | A flag indicating that the listing has a Green Verification. |  |
| `GreenWaterConservation` | `green_water_conservation` | varchar (multi) | [`green_water_conservation`](../lookups.md#green_water_conservation) | A pick list of general water conserving attributes of the property such as landscaping or reclamation without naming specific elements with ratings that may wane over time. |  |
| `GrossIncome` | `gross_income` | Number |  | The actual current income from rent and all other revenue-generating sources. |  |
| `GrossLivingAreaAnsi` | `gross_living_area_ansi` | Number |  | The total livable area with the structure as measured using American National Standards Institute (ANSI) measurement guidelines. |  |
| `GrossScheduledIncome` | `gross_scheduled_income` | Number |  | The maximum amount of annual rent collected if the property were 100% occupied all year and all tenants paid their rent. |  |
| `HabitableResidenceYN` | `habitable_residence_yn` | Boolean |  | Indicates whether or not the property includes a structure that can be lived in. |  |
| `Heating` | `heating` | varchar (multi) | [`heating`](../lookups.md#heating) | A list describing the heating features of the property. |  |
| `HeatingYN` | `heating_yn` | Boolean |  | Indicates whether or not the property has heating. |  |
| `HighSchool` | `high_school` | enum | [`high_school`](../lookups.md#high_school) | The name of the high school having a catchment area that includes the associated property. |  |
| `HighSchoolDistrict` | `high_school_district` | enum | [`high_school_district`](../lookups.md#high_school_district) | The name of the high school district having a catchment area that includes the associated property. |  |
| `HistoryTransactional` | `history_transactional` | Collection |  | A collection of historical items related to the property record. | `[Collection]` |
| `HomeWarrantyYN` | `home_warranty_yn` | Boolean |  | Indicates whether or not a home warranty is included in the sale of the property. |  |
| `HorseAmenities` | `horse_amenities` | varchar (multi) | [`horse_amenities`](../lookups.md#horse_amenities) | A list of horse amenities on the lot or in the community. |  |
| `HorseYN` | `horse_yn` | Boolean |  | Indicates whether or not the property allows for the raising of horses. |  |
| `HoursDaysOfOperation` | `hours_days_of_operation` | varchar (multi) | [`hours_days_of_operation`](../lookups.md#hours_days_of_operation) | A simplified enumerated list of the days and hours of operation of the business being sold (e.g., Open 24 Hours, Open Seven Days). |  |
| `HoursDaysOfOperationDescription` | `hours_days_of_operation_description` | String |  | A detailed description of the hours and days the business being sold is open for business. |  |
| `Inclusions` | `inclusions` | String |  | Portable elements of the property that will be included in the sale. |  |
| `IncomeIncludes` | `income_includes` | varchar (multi) | [`income_includes`](../lookups.md#income_includes) | A list of income sources included in the GrossScheduledIncome and GrossIncome (e.g., Laundry, Parking, Recreation, Storage). |  |
| `InsuranceExpense` | `insurance_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `InteriorFeatures` | `interior_features` | varchar (multi) | [`interior_or_room_features`](../lookups.md#interior_or_room_features) | A list of features or a description of the interior of the property included in the sale/lease. |  |
| `InternetAddressDisplayYN` | `internet_address_display_yn` | Boolean |  | Indicates whether or not the seller has allowed the listing address to be displayed on Internet sites. |  |
| `InternetAutomatedValuationDisplayYN` | `internet_automated_valuation_display_yn` | Boolean |  | Indicates whether or not the seller allows the listing to be displayed with an automated valuation model (AVM) on Internet sites. |  |
| `InternetConsumerCommentYN` | `internet_consumer_comment_yn` | Boolean |  | Indicates whether or not the seller allows a comment or blog system to be attached to the listing on Internet sites. |  |
| `InternetEntireListingDisplayYN` | `internet_entire_listing_display_yn` | Boolean |  | Indicates whether or not the seller has allowed the listing to be displayed on Internet sites. |  |
| `IrrigationSource` | `irrigation_source` | varchar (multi) | [`irrigation_source`](../lookups.md#irrigation_source) | The source which the property receives its water for irrigation. |  |
| `IrrigationWaterRightsAcres` | `irrigation_water_rights_acres` | Number |  | The number of acres allowed under the property's water rights. |  |
| `IrrigationWaterRightsYN` | `irrigation_water_rights_yn` | Boolean |  | Indicates whether or not the property includes water rights for irrigation. |  |
| `LaborInformation` | `labor_information` | varchar (multi) | [`labor_information`](../lookups.md#labor_information) | Information about labor laws that are applicable to the business being sold (i.e., Union, Non-Union, Employee License Required). |  |
| `LandLeaseAmount` | `land_lease_amount` | Number |  | When the land is not included in the sale, but is leased, the amount of the lease. |  |
| `LandLeaseAmountFrequency` | `land_lease_amount_frequency` | enum | [`fee_frequency`](../lookups.md#fee_frequency) | The frequency in which the land lease fee is paid when the land is not included in the sale but is leased. |  |
| `LandLeaseExpirationDate` | `land_lease_expiration_date` | Date |  | The expiration date of the land lease when the land is not included in the sale but is leased. |  |
| `LandLeaseYN` | `land_lease_yn` | Boolean |  | The land is not included in the sale and a lease exists. |  |
| `Latitude` | `latitude` | Number |  | The geographic latitude of some reference point on the property, specified in degrees and decimal parts. |  |
| `LaundryFeatures` | `laundry_features` | varchar (multi) | [`laundry_features`](../lookups.md#laundry_features) | Add this pick list of features and locations where the laundry is located in the property being sold (i.e., Gas Dryer Hookup, In Kitchen, In Garage, etc.). |  |
| `LeasableArea` | `leasable_area` | Number |  | The area that may be leased within the commercial property. |  |
| `LeasableAreaUnits` | `leasable_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). |  |
| `LeaseAmount` | `lease_amount` | Number |  | The amount of any lease the business pays for its current location. |  |
| `LeaseAmountFrequency` | `lease_amount_frequency` | enum | [`fee_frequency`](../lookups.md#fee_frequency) | The frequency the LeaseAmount is paid (e.g., monthly, weekly, annual). |  |
| `LeaseAssignableYN` | `lease_assignable_yn` | Boolean |  | Indicates whether or not the lease at the current location of the business can be assigned to another party. |  |
| `LeaseConsideredYN` | `lease_considered_yn` | Boolean |  | Indicates whether or not the seller will consider leasing the property instead of selling. |  |
| `LeaseExpiration` | `lease_expiration` | Date |  | The expiration date of the lease for the current location of the business. |  |
| `LeaseRenewalCompensation` | `lease_renewal_compensation` | varchar (multi) | [`lease_renewal_compensation`](../lookups.md#lease_renewal_compensation) | A list of compensations other than the original selling office compensation (i.e., Paid on Renewal, Paid on Tenant Purchase, No Renewal Commission, Call Listing Office, etc.). |  |
| `LeaseRenewalOptionYN` | `lease_renewal_option_yn` | Boolean |  | Indicates whether or not there is an option to renew the lease at the current location of the business. |  |
| `LeaseTerm` | `lease_term` | enum | [`lease_term`](../lookups.md#lease_term) | A pick list of lengths that represent the length of the lease (e.g., Weekly, Month to Month, 6-Month Lease, 12-Month Lease, 2-Year Lease). |  |
| `Levels` | `levels` | varchar (multi) | [`levels`](../lookups.md#levels) | The number of levels in the property being sold (e.g., One, Two, Three or More, Multi/Split). |  |
| `License1` | `license1` | String |  | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. |  |
| `License2` | `license2` | String |  | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. |  |
| `License3` | `license3` | String |  | The license number of the mobile or manufactured home, also known as the Department of Housing label/insignia number. |  |
| `LicensesExpense` | `licenses_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `ListAOR` | `list_aor` | enum | [`aor`](../lookups.md#aor) | The responsible board or association of REALTORS® for this listing. |  |
| `ListAgent` | `list_agent` | Resource |  | The listing agent involved in the transaction. | `[Resource]` |
| `ListAgentAOR` | `list_agent_aor` | enum | [`aor`](../lookups.md#aor) | The listing agent's board or association of REALTORS®. | `[dropped: satellite of list_agent_key]` |
| `ListAgentDesignation` | `list_agent_designation` | varchar (multi) | [`list_agent_designation`](../lookups.md#list_agent_designation) | Designations and certifications acknowledging experience and expertise in various real estate sectors are awarded by the National Association of REALTORS® (NAR) and each affiliated group upon completion of required courses. | `[dropped: satellite of list_agent_key]` |
| `ListAgentDirectPhone` | `list_agent_direct_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentEmail` | `list_agent_email` | String |  | The email address of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentFax` | `list_agent_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentFirstName` | `list_agent_first_name` | String |  | The first name of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentFullName` | `list_agent_full_name` | String |  | The first, middle and last name of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentHomePhone` | `list_agent_home_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentKey` | `list_agent_key` | String |  | A system unique identifier. | `-> member.member_key` |
| `ListAgentLastName` | `list_agent_last_name` | String |  | The last name of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentMiddleName` | `list_agent_middle_name` | String |  | The middle name of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentMlsId` | `list_agent_mls_id` | String |  | The local, well-known identifier for the member. | `[dropped: satellite of list_agent_key]` |
| `ListAgentMobilePhone` | `list_agent_mobile_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentNamePrefix` | `list_agent_name_prefix` | String |  | The prefix to the name (e.g., Dr., Mr., Ms.). | `[dropped: satellite of list_agent_key]` |
| `ListAgentNameSuffix` | `list_agent_name_suffix` | String |  | The suffix to the name (e.g., Esq., Jr., III). | `[dropped: satellite of list_agent_key]` |
| `ListAgentNationalAssociationId` | `list_agent_national_association_id` | String |  | The national association ID of the listing agent (e.g., the NRDS number in the U.S.). |  |
| `ListAgentOfficePhone` | `list_agent_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentOfficePhoneExt` | `list_agent_office_phone_ext` | String |  | The extension of the given phone number (if applicable). | `[dropped: satellite of list_agent_key]` |
| `ListAgentPager` | `list_agent_pager` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentPreferredPhone` | `list_agent_preferred_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentPreferredPhoneExt` | `list_agent_preferred_phone_ext` | String |  | The extension of the given phone number (if applicable). | `[dropped: satellite of list_agent_key]` |
| `ListAgentStateLicense` | `list_agent_state_license` | String |  | The license of the listing agent. | `[dropped: satellite of list_agent_key]` |
| `ListAgentTollFreePhone` | `list_agent_toll_free_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentURL` | `list_agent_url` | String |  | The website Uniform Resource Identifier (URI) of the listing agent. |  |
| `ListAgentVoiceMail` | `list_agent_voice_mail` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_agent_key]` |
| `ListAgentVoiceMailExt` | `list_agent_voice_mail_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of list_agent_key]` |
| `ListOffice` | `list_office` | Resource |  | The listing agent's office. | `[Resource]` |
| `ListOfficeAOR` | `list_office_aor` | enum | [`aor`](../lookups.md#aor) | The listing office's board or association of REALTORS®. | `[dropped: satellite of list_office_key]` |
| `ListOfficeEmail` | `list_office_email` | String |  | The email address of the listing office. | `[dropped: satellite of list_office_key]` |
| `ListOfficeFax` | `list_office_fax` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_office_key]` |
| `ListOfficeKey` | `list_office_key` | String |  | A system unique identifier. | `-> office.office_key` |
| `ListOfficeMlsId` | `list_office_mls_id` | String |  | The local, well-known identifier. | `[dropped: satellite of list_office_key]` |
| `ListOfficeName` | `list_office_name` | String |  | The legal name of the brokerage representing the seller. | `[dropped: satellite of list_office_key]` |
| `ListOfficeNationalAssociationId` | `list_office_national_association_id` | String |  | The national association ID of the listing office (e.g., the NRDS number in the U.S.). |  |
| `ListOfficePhone` | `list_office_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). | `[dropped: satellite of list_office_key]` |
| `ListOfficePhoneExt` | `list_office_phone_ext` | String |  | The extension of the given phone number, if applicable. | `[dropped: satellite of list_office_key]` |
| `ListOfficeURL` | `list_office_url` | String |  | The website Uniform Resource Identifier (URI) for the listing office. |  |
| `ListPrice` | `list_price` | Number |  | The current price of the property as determined by the seller and the seller's broker. |  |
| `ListPriceLow` | `list_price_low` | Number |  | The lower price used for Value Range Pricing. |  |
| `ListTeam` | `list_team` | Resource |  | Two or more agents working on the listing agent's team. | `[Resource]` |
| `ListTeamKey` | `list_team_key` | String |  | A system unique identifier. | `-> teams.team_key` |
| `ListTeamName` | `list_team_name` | String |  | The name of the team representing the seller. | `[REVIEW]` |
| `ListingAgreement` | `listing_agreement` | enum | [`listing_agreement`](../lookups.md#listing_agreement) | The nature of the agreement between the seller and the listing agent (e.g., Exclusive Agency, Open Listing). |  |
| `ListingContractDate` | `listing_contract_date` | Date |  | The effective date of the agreement between the seller and the seller's broker. |  |
| `ListingId` | `listing_id` | String |  | The well-known identifier for the listing. |  |
| `ListingKey` | `listing_key` | String |  | A unique identifier for this record from the immediate source. | `pk` |
| `ListingService` | `listing_service` | enum | [`listing_service`](../lookups.md#listing_service) | The type or level of service the listing member will be providing to the selling homeowner (e.g., Full Service, Limited Service, Entry Only). |  |
| `ListingTerms` | `listing_terms` | varchar (multi) | [`listing_terms`](../lookups.md#listing_terms) | Terms of the listing such as Lien Release, Subject to Court Approval or Owner Will Carry. |  |
| `ListingURL` | `listing_url` | String |  | Provides a link to the specific listing on a brokerage website, agent website or other public-facing source. |  |
| `ListingURLDescription` | `listing_url_description` | enum | [`listing_url_description`](../lookups.md#listing_url_description) | A pick list of options showing where the listing URL resides (i.e., Brokerage Website, Agent Website, etc.). |  |
| `LivingArea` | `living_area` | Number |  | The total livable area within the structure. |  |
| `LivingAreaSource` | `living_area_source` | enum | [`area_source`](../lookups.md#area_source) | The source of the measurements. |  |
| `LivingAreaUnits` | `living_area_units` | enum | [`area_units`](../lookups.md#area_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters). |  |
| `LockBoxLocation` | `lock_box_location` | String |  | A field describing the location of the lockbox. |  |
| `LockBoxSerialNumber` | `lock_box_serial_number` | String |  | The serial number of the lockbox placed on the property. |  |
| `LockBoxType` | `lock_box_type` | varchar (multi) | [`lock_box_type`](../lookups.md#lock_box_type) | A field describing the type of lockbox. |  |
| `Longitude` | `longitude` | Number |  | The geographic longitude of some reference point on the property, specified in degrees and decimal parts. |  |
| `LotDimensionsSource` | `lot_dimensions_source` | enum | [`lot_dimensions_source`](../lookups.md#lot_dimensions_source) | The source of the measurements. |  |
| `LotFeatures` | `lot_features` | varchar (multi) | [`lot_features`](../lookups.md#lot_features) | A list of features or a description of the lot included in the sale/lease. |  |
| `LotSizeAcres` | `lot_size_acres` | Number |  | The total acres of the lot. |  |
| `LotSizeArea` | `lot_size_area` | Number |  | The total area of the lot. |  |
| `LotSizeDimensions` | `lot_size_dimensions` | String |  | The dimensions of the lot minimally represented as length and width (i.e. |  |
| `LotSizeSource` | `lot_size_source` | enum | [`lot_size_source`](../lookups.md#lot_size_source) | The source of the measurements. |  |
| `LotSizeSquareFeet` | `lot_size_square_feet` | Number |  | The total square footage of the lot. |  |
| `LotSizeUnits` | `lot_size_units` | enum | [`lot_size_units`](../lookups.md#lot_size_units) | A pick list of the unit of measurement for the area (e.g., Square Feet, Square Meters, Acres). |  |
| `MLSAreaMajor` | `mls_area_major` | enum | [`mls_area_major`](../lookups.md#mls_area_major) | The major marketing area name, as defined by the MLS or other nongovernmental organization. |  |
| `MLSAreaMinor` | `mls_area_minor` | enum | [`mls_area_minor`](../lookups.md#mls_area_minor) | The minor/submarketing area name, as defined by the MLS or other nongovernmental organization. |  |
| `MainLevelBathrooms` | `main_level_bathrooms` | Number |  | The number of bathrooms located on the main or entry level of the property. |  |
| `MainLevelBedrooms` | `main_level_bedrooms` | Number |  | The number of bedrooms located on the main or entry level of the property. |  |
| `MaintenanceExpense` | `maintenance_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `MajorChangeTimestamp` | `major_change_timestamp` | Timestamp |  | The timestamp of the last major change on the listing (see also MajorChangeType). |  |
| `MajorChangeType` | `major_change_type` | enum | [`change_type`](../lookups.md#change_type) | A description of the last major change on the listing (i.e., Price Reduction, Back on Market). |  |
| `Make` | `make` | String |  | The make of the mobile or manufactured home. |  |
| `ManagerExpense` | `manager_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `MapCoordinate` | `map_coordinate` | String |  | A map coordinate for the property, as determined by local custom. |  |
| `MapCoordinateSource` | `map_coordinate_source` | String |  | The name of the map or map book publisher. |  |
| `MapURL` | `map_url` | String |  | A Uniform Resource Identifier (URI) to a map of the property. |  |
| `Media` | `media` | Collection |  | A collection of media items related to the Property record. | `[Collection]` |
| `MiddleOrJuniorSchool` | `middle_or_junior_school` | enum | [`middle_or_junior_school`](../lookups.md#middle_or_junior_school) | The name of the junior or middle school having a catchment area that includes the associated property. |  |
| `MiddleOrJuniorSchoolDistrict` | `middle_or_junior_school_district` | enum | [`middle_or_junior_school_district`](../lookups.md#middle_or_junior_school_district) | The name of the junior or middle school district having a catchment area that includes the associated property. |  |
| `MlsStatus` | `mls_status` | enum | [`mls_status`](../lookups.md#mls_status) | A local or regional status that is well known by business users. |  |
| `MobileDimUnits` | `mobile_dim_units` | enum | [`linear_units`](../lookups.md#linear_units) | A pick list of the unit of linear measurement (e.g., Feet, Meters, Yards, Kilometers, Miles). |  |
| `MobileHomeRemainsYN` | `mobile_home_remains_yn` | Boolean |  | Indicates whether or not the mobile home is to remain and be included in the sale of the property. |  |
| `MobileLength` | `mobile_length` | Number |  | The length of the mobile/manufactured home. |  |
| `MobileWidth` | `mobile_width` | Number |  | The width of the mobile/manufactured home. |  |
| `Model` | `model` | String |  | The model of the mobile or manufactured home. |  |
| `ModificationTimestamp` | `modification_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing was last modified. |  |
| `NetOperatingIncome` | `net_operating_income` | Number |  | The net operating income is the revenue from a property after operating expenses have been deducted but before deducting income taxes and financing expenses (interest and principal payments). |  |
| `NewConstructionYN` | `new_construction_yn` | Boolean |  | Indicates whether or not the property is newly constructed and has not been previously occupied. |  |
| `NewTaxesExpense` | `new_taxes_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `NumberOfBuildings` | `number_of_buildings` | Number |  | The total number of separate buildings included in the income property. |  |
| `NumberOfFullTimeEmployees` | `number_of_full_time_employees` | Number |  | The current number of individuals employed by the business on a full-time basis. |  |
| `NumberOfLots` | `number_of_lots` | Number |  | The total number of lots on the property or included in the sale. |  |
| `NumberOfPads` | `number_of_pads` | Number |  | The number of pads or spaces in the mobile home park. |  |
| `NumberOfPartTimeEmployees` | `number_of_part_time_employees` | Number |  | The current number of individuals employed by the business on a part-time basis. |  |
| `NumberOfSeparateElectricMeters` | `number_of_separate_electric_meters` | Number |  | The total number of separate electric meters on the property. |  |
| `NumberOfSeparateGasMeters` | `number_of_separate_gas_meters` | Number |  | The total number of separate gas meters on the property. |  |
| `NumberOfSeparateWaterMeters` | `number_of_separate_water_meters` | Number |  | The total number of separate water meters on the property. |  |
| `NumberOfUnitsInCommunity` | `number_of_units_in_community` | Number |  | The total number of units in the building, complex or community. |  |
| `NumberOfUnitsLeased` | `number_of_units_leased` | Number |  | The total number of units currently under a lease agreement. |  |
| `NumberOfUnitsMoMo` | `number_of_units_mo_mo` | Number |  | The total number of units leasable month to month. |  |
| `NumberOfUnitsTotal` | `number_of_units_total` | Number |  | Total number of units included in the income property, occupied or unoccupied. |  |
| `NumberOfUnitsVacant` | `number_of_units_vacant` | Number |  | The number of units currently vacant. |  |
| `OccupantName` | `occupant_name` | String |  | The name of the current occupant, if any, of the property being sold. |  |
| `OccupantPhone` | `occupant_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `OccupantType` | `occupant_type` | enum | [`occupant_type`](../lookups.md#occupant_type) | A field that describes the type of occupant (i.e., Owner, Tenant, Vacant). |  |
| `OffMarketDate` | `off_market_date` | Date |  | The date the listing was taken off market. |  |
| `OffMarketTimestamp` | `off_market_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to an off-market status... |  |
| `OnMarketDate` | `on_market_date` | Date |  | The date the listing was placed on market. |  |
| `OnMarketTimestamp` | `on_market_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to Active or Backup. |  |
| `OpenHouse` | `open_house` | Collection |  | A collection of open house items related to the Property record. | `[Collection]` |
| `OpenHouseModificationTimestamp` | `open_house_modification_timestamp` | Timestamp |  | A system-generated timestamp of when the last update or change to the open house information for this listing was made. |  |
| `OpenParkingSpaces` | `open_parking_spaces` | Number |  | The number of open or uncovered parking spaces included in the sale. |  |
| `OpenParkingYN` | `open_parking_yn` | Boolean |  | A flag indicating that any parking spaces associated with the property are not covered by a roof. |  |
| `OperatingExpense` | `operating_expense` | Number |  | The costs associated with the operation and maintenance of an income-producing property. |  |
| `OperatingExpenseIncludes` | `operating_expense_includes` | varchar (multi) | [`operating_expense_includes`](../lookups.md#operating_expense_includes) | When individual expense fields are not used and only a total is entered, this lists the expenses that are included in the OperatingExpense field. |  |
| `OriginalEntryTimestamp` | `original_entry_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing was entered and made visible to members of the MLS. |  |
| `OriginalListPrice` | `original_list_price` | Number |  | The original price of the property on the initial agreement between the seller and the seller's broker. |  |
| `OriginatingSystem` | `originating_system` | Resource |  | The originating system of the Property record. | `[Resource]` |
| `OriginatingSystemID` | `originating_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the originating record provider. | `-> ouid.organization_unique_id_key` |
| `OriginatingSystemKey` | `originating_system_key` | String |  | The system key, a unique record identifier, from the originating system. |  |
| `OriginatingSystemName` | `originating_system_name` | String |  | The name of the originating record provider, most commonly the name of the MLS. |  |
| `OtherEquipment` | `other_equipment` | varchar (multi) | [`other_equipment`](../lookups.md#other_equipment) | A list of other equipment that will be included in the sale of the property. |  |
| `OtherExpense` | `other_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `OtherParking` | `other_parking` | String |  | Other types of parking available to, or part of, the property. |  |
| `OtherStructures` | `other_structures` | varchar (multi) | [`other_structures`](../lookups.md#other_structures) | A list of structures other than the main dwelling (e.g., Guest House, Barn, Shed). |  |
| `OwnerName` | `owner_name` | String |  | The name of the owner of the property being sold. |  |
| `OwnerPays` | `owner_pays` | varchar (multi) | [`owner_pays`](../lookups.md#owner_pays) | A list of expenses for the property paid for by the owner as opposed to the tenant (e.g., Water, Trash, Electric). |  |
| `OwnerPhone` | `owner_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `Ownership` | `ownership` | String |  | A text description of the manner in which title to a property is held (e.g., Trust, Corporation, Joint Tenant, Individual). |  |
| `OwnershipType` | `ownership_type` | enum | [`ownership_type`](../lookups.md#ownership_type) | The current type of ownership of the business being sold (e.g., Corporation, LLC, Sole Proprietor, Partnership). |  |
| `ParcelNumber` | `parcel_number` | String |  | A number used to uniquely identify a parcel or lot. |  |
| `ParkManagerName` | `park_manager_name` | String |  | The name of the manager of the mobile home park. |  |
| `ParkManagerPhone` | `park_manager_phone` | String |  | North American 10-digit phone numbers should be in the format of ###-###-#### (separated by hyphens). |  |
| `ParkName` | `park_name` | String |  | The name of the mobile home park or corporate/commercial park. |  |
| `ParkingFeatures` | `parking_features` | varchar (multi) | [`parking_features`](../lookups.md#parking_features) | A list of features about or a description of the parking included in the sale/lease. |  |
| `ParkingTotal` | `parking_total` | Number |  | The total number of parking spaces included in the sale. |  |
| `PastureArea` | `pasture_area` | Number |  | A measurement or percentage of the property that has been allocated as pasture or grazing area. |  |
| `PatioAndPorchFeatures` | `patio_and_porch_features` | varchar (multi) | [`patio_and_porch_features`](../lookups.md#patio_and_porch_features) | A list of features about or a description of the patio or porch included in the sale/lease. |  |
| `PendingTimestamp` | `pending_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the most recent date/time the listing's status was set to Pending. |  |
| `PestControlExpense` | `pest_control_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `PetsAllowed` | `pets_allowed` | varchar (multi) | [`pets_allowed`](../lookups.md#pets_allowed) | Indicates whether or not pets are allowed at the property being leased, usually as a list of yes, no and more detailed restrictions/allowances. |  |
| `PhotosChangeTimestamp` | `photos_change_timestamp` | Timestamp |  | A system-generated timestamp of when the last update or change to the photos for this listing was made. |  |
| `PhotosCount` | `photos_count` | Number |  | The total number of pictures or photos included with the listing. |  |
| `PoolExpense` | `pool_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `PoolFeatures` | `pool_features` | varchar (multi) | [`pool_features`](../lookups.md#pool_features) | A list of features about or a description of a pool included in the sale/lease. |  |
| `PoolPrivateYN` | `pool_private_yn` | Boolean |  | The property has a privately owned pool that is included in the sale/lease. |  |
| `Possession` | `possession` | varchar (multi) | [`possession`](../lookups.md#possession) | A list defining when possession will occur (i.e., COE, COE+1, etc.). |  |
| `PossibleUse` | `possible_use` | varchar (multi) | [`current_or_possible_use`](../lookups.md#current_or_possible_use) | A list of the type(s) of possible or best uses of the property. |  |
| `PostalCity` | `postal_city` | enum | [`postal_city`](../lookups.md#postal_city) | The official city per the U.S. |  |
| `PostalCode` | `postal_code` | String |  | The postal code portion of a street or mailing address. |  |
| `PostalCodePlus4` | `postal_code_plus4` | String |  | The last four digits of a nine-digit U.S. |  |
| `PowerProduction` | `power_production` | Collection |  | A collection of the types of power production system(s) available on the property. | `[Collection]` |
| `PowerProductionType` | `power_production_type` | varchar (multi) | [`power_production_type`](../lookups.md#power_production_type) | A list of the types of power production systems available on the property. |  |
| `PowerProductionYN` | `power_production_yn` | Boolean |  | A flag indicating that the listing has a Power Production system. |  |
| `PreviousListPrice` | `previous_list_price` | Number |  | The most recent previous list price of the listing. |  |
| `PriceChangeTimestamp` | `price_change_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing's price was last changed. |  |
| `PrivateOfficeRemarks` | `private_office_remarks` | String |  | A Remarks field that is only visible to members of the same offices as the listing agent. |  |
| `PrivateRemarks` | `private_remarks` | String |  | Remarks that may contain security or proprietary information and should be restricted from public view. |  |
| `ProfessionalManagementExpense` | `professional_management_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `PropertyAttachedYN` | `property_attached_yn` | Boolean |  | Indicates whether or not the primary structure is attached to another structure that is not included in the sale (i.e., one unit of a duplex). |  |
| `PropertyCondition` | `property_condition` | varchar (multi) | [`property_condition`](../lookups.md#property_condition) | A list describing the condition of the property and any structures included in the sale. |  |
| `PropertySubType` | `property_sub_type` | enum | [`property_sub_type`](../lookups.md#property_sub_type) | A list of types of residential and residential lease properties (e.g., Single-Family Residence, Condominium, Townhouse) or a list of subtypes for mobile (e.g., Manufactured Home, Manufactured On Land). |  |
| `PropertyTimeZoneName` | `property_time_zone_name` | enum | [`iana_time_zone_values`](../lookups.md#iana_time_zone_values) | The standard name of the property time zone, as provided by the IANA tz database. |  |
| `PropertyTimeZoneObservesDstYN` | `property_time_zone_observes_dst_yn` | Boolean |  | Indicates whether the property is in a time zone that observes Daylight Savings Time (DST). |  |
| `PropertyTimeZoneStandardOffset` | `property_time_zone_standard_offset` | Number |  | The time zone offset is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. |  |
| `PropertyType` | `property_type` | enum | [`property_type`](../lookups.md#property_type) | A list of types of properties (e.g., Residential, Lease, Income, Land, Mobile, Commercial Sale). |  |
| `PublicRemarks` | `public_remarks` | String |  | Text remarks that may be displayed to the public. |  |
| `PublicSurveyRange` | `public_survey_range` | String |  | The range identified by the Public Land Survey System (PLSS). |  |
| `PublicSurveySection` | `public_survey_section` | String |  | The section identified by the Public Land Survey System (PLSS). |  |
| `PublicSurveyTownship` | `public_survey_township` | String |  | The township identified by the Public Land Survey System (PLSS). |  |
| `PurchaseContractDate` | `purchase_contract_date` | Date |  | With for-sale listings, this represents the date an offer was accepted and the listing was no longer on market. |  |
| `RVParkingDimensions` | `rv_parking_dimensions` | String |  | The dimensions of the RV parking area minimally represented as length and width (i.e., 25' x 18') or a measurement of all sides of the polygon representing the usable RV parking space (i.e., 33' x 15' x 12' x 60'). |  |
| `RangeArea` | `range_area` | Number |  | The measurement or percentage of the property that has been allocated as range. |  |
| `RentControlYN` | `rent_control_yn` | Boolean |  | Indicates whether or not the property is in a rent-control area. |  |
| `RentIncludes` | `rent_includes` | varchar (multi) | [`rent_includes`](../lookups.md#rent_includes) | A list of services or items that the tenant is not responsible to pay. |  |
| `RoadFrontageType` | `road_frontage_type` | varchar (multi) | [`road_frontage_type`](../lookups.md#road_frontage_type) | A pick list of types of road frontage (i.e., County, Freeway, Interstate, None). |  |
| `RoadResponsibility` | `road_responsibility` | varchar (multi) | [`road_responsibility`](../lookups.md#road_responsibility) | The person or entity responsible for road maintenance (e.g., City, County, Private). |  |
| `RoadSurfaceType` | `road_surface_type` | varchar (multi) | [`road_surface_type`](../lookups.md#road_surface_type) | A pick list of types of road surfaces in use to access the property. |  |
| `Roof` | `roof` | varchar (multi) | [`roof`](../lookups.md#roof) | A list describing the roof style type (e.g., Spanish Tile, Composite, Shake). |  |
| `RoomType` | `room_type` | varchar (multi) | [`room_type`](../lookups.md#room_type) | A list of identifiers for specific interior spaces within a structure (e.g., Bedroom, Bathroom, Kitchen, Living Room). |  |
| `Rooms` | `rooms` | Collection |  | A collection of types of rooms and details/features about the given room. | `[Collection]` |
| `RoomsTotal` | `rooms_total` | Number |  | The number of rooms in a dwelling. |  |
| `SeatingCapacity` | `seating_capacity` | Number |  | The seating capacity of the business being sold. |  |
| `SecurityFeatures` | `security_features` | varchar (multi) | [`security_features`](../lookups.md#security_features) | A list describing the security features included in the sale/lease. |  |
| `SeniorCommunityYN` | `senior_community_yn` | Boolean |  | Indicates whether or not a community is a senior community. |  |
| `SerialU` | `serial_u` | String |  | The serial number of the mobile or manufactured home. |  |
| `SerialX` | `serial_x` | String |  | The serial number of the mobile or manufactured home. |  |
| `SerialXX` | `serial_xx` | String |  | The serial number of the mobile or manufactured home. |  |
| `Sewer` | `sewer` | varchar (multi) | [`sewer`](../lookups.md#sewer) | A list describing the sewer or septic features of a property. |  |
| `ShowingAdvanceNotice` | `showing_advance_notice` | Number |  | The hours of advance notice required to schedule a showing. |  |
| `ShowingAttendedYN` | `showing_attended_yn` | Boolean |  | Indicates whether or not this home requires an attended showing (i.e., Yes = licensed agent representing the seller must be present during showing). |  |
| `ShowingConsiderations` | `showing_considerations` | varchar (multi) | [`showing_considerations`](../lookups.md#showing_considerations) | A pick list of conditions that may require caution or further consideration, such as bringing someone with you, when showing the property (i.e., Electricity Not On, Inconsistent Cell Service, No Exterior Lighting). |  |
| `ShowingContactName` | `showing_contact_name` | String |  | The name of the contact for the showing of the listed property. |  |
| `ShowingContactPhone` | `showing_contact_phone` | String |  | A telephone number that should be called to arrange showing the property. |  |
| `ShowingContactPhoneExt` | `showing_contact_phone_ext` | String |  | The extension of the given phone number, if applicable. |  |
| `ShowingContactType` | `showing_contact_type` | varchar (multi) | [`showing_contact_type`](../lookups.md#showing_contact_type) | The type of contact for the showing (i.e., Agent, Broker, Seller). |  |
| `ShowingDays` | `showing_days` | varchar (multi) | [`showing_days`](../lookups.md#showing_days) | The days of the week that the property is available for showing (i.e., Sundays, Mondays, Tuesdays, Wednesdays, Thursdays, Fridays, Saturdays). |  |
| `ShowingEndTime` | `showing_end_time` | Timestamp |  | From the days selected in the ShowingDays field, the end time that the property is available for showing. |  |
| `ShowingInstructions` | `showing_instructions` | String |  | Remarks that detail the seller's instructions for showing the subject property. |  |
| `ShowingRequirements` | `showing_requirements` | varchar (multi) | [`showing_requirements`](../lookups.md#showing_requirements) | A pick list of types of notice required to see the home (i.e., Appointment Required, Courtesy Call Only, Go Direct, etc.). |  |
| `ShowingServiceName` | `showing_service_name` | enum | [`showing_service_name`](../lookups.md#showing_service_name) | The name of the showing service used to request showings on the listing. |  |
| `ShowingStartTime` | `showing_start_time` | Timestamp |  | From the days selected in the ShowingDays field, the start time that the property is available for showing. |  |
| `SignOnPropertyYN` | `sign_on_property_yn` | Boolean |  | Indicates whether or not there a sign on the property. |  |
| `SimpleDaysOnMarket` | `simple_days_on_market` | Number |  | A simplified version of days on market (DOM) where the calculation is a simple start and end, such as the difference between the listing input or contract date and the date of sale. |  |
| `Skirt` | `skirt` | varchar (multi) | [`skirt`](../lookups.md#skirt) | A list of types of mobile home skirting. |  |
| `SocialMedia` | `social_media` | Collection |  | A collection of social media items related to the Property record. | `[Collection]` |
| `SourceSystem` | `source_system` | Resource |  | The source system of the Property record. | `[Resource]` |
| `SourceSystemID` | `source_system_id` | String |  | The OUID Resource's OrganizationUniqueId of the source record provider. | `-> ouid.organization_unique_id_key` |
| `SourceSystemKey` | `source_system_key` | String |  | The system key, a unique record identifier, from the source system. |  |
| `SourceSystemName` | `source_system_name` | String |  | The name of the immediate record provider. |  |
| `SpaFeatures` | `spa_features` | varchar (multi) | [`spa_features`](../lookups.md#spa_features) | A list of features or a description of the spa included in the sale/lease. |  |
| `SpaYN` | `spa_yn` | Boolean |  | Indicates whether or not the property has a spa. |  |
| `SpecialLicenses` | `special_licenses` | varchar (multi) | [`special_licenses`](../lookups.md#special_licenses) | Special licenses required/used by the business being sold (e.g., Beer/Wine, Class H, Professional, Gambling, None). |  |
| `SpecialListingConditions` | `special_listing_conditions` | varchar (multi) | [`special_listing_conditions`](../lookups.md#special_listing_conditions) | A list of options that describe the type of sale (e.g., Standard, REO, Short Sale, Probate, Auction, NOD) at the time of listing. |  |
| `StandardStatus` | `standard_status` | enum | [`standard_status`](../lookups.md#standard_status) | The status of the listing as it reflects the state of the contract between the listing agent and seller, or an agreement with a buyer (e.g., Active, Active Under Contract, Canceled, Closed, Expired, Pending, Withdrawn). |  |
| `StartShowingDate` | `start_showing_date` | Date |  | The date the listing agent/broker expects to start showing the property. |  |
| `StateOrProvince` | `state_or_province` | enum | [`state_or_province`](../lookups.md#state_or_province) | Text field containing the accepted postal abbreviation for the state or province. |  |
| `StateRegion` | `state_region` | String |  | A subsection or area of a defined state or province (e.g., Florida Keys, Hudson Valley in New York, Silicon Valley in California). |  |
| `StatusChangeTimestamp` | `status_change_timestamp` | Timestamp |  | The transactional timestamp automatically recorded by the MLS system representing the date/time the listing's status was last changed. |  |
| `Stories` | `stories` | Number |  | The number of floors in the property being sold. |  |
| `StoriesTotal` | `stories_total` | Number |  | The total number of floors in the building. |  |
| `StreetAdditionalInfo` | `street_additional_info` | String |  | Information other than a prefix or suffix for the street portion of a postal address. |  |
| `StreetDirPrefix` | `street_dir_prefix` | enum | [`street_direction`](../lookups.md#street_direction) | The direction indicator that precedes the listed property's street name. |  |
| `StreetDirSuffix` | `street_dir_suffix` | enum | [`street_direction`](../lookups.md#street_direction) | The direction indicator that follows a listed property's street address. |  |
| `StreetName` | `street_name` | String |  | The street name portion of a listed property's street address. |  |
| `StreetNumber` | `street_number` | String |  | The street number portion of a listed property's street address. |  |
| `StreetNumberNumeric` | `street_number_numeric` | Number |  | The integer portion of the street number. |  |
| `StreetSuffix` | `street_suffix` | enum | [`street_suffix`](../lookups.md#street_suffix) | The suffix portion of a listed property's street address. |  |
| `StreetSuffixModifier` | `street_suffix_modifier` | String |  | Allows for the entry of a unique street suffix that was not found in the Street Suffix pick list or to extend or prefix the suffix. |  |
| `StructureType` | `structure_type` | varchar (multi) | [`structure_type`](../lookups.md#structure_type) | The type of structure that the property completely or partially encompasses. |  |
| `SubAgencyCompensation` | `sub_agency_compensation` | String |  | The total commission to be paid to the subagency, expressed as either a percentage or a constant currency amount. |  |
| `SubAgencyCompensationType` | `sub_agency_compensation_type` | enum | [`compensation_type`](../lookups.md#compensation_type) | A list of types to clarify the value entered in the SubAgencyCompensation field. |  |
| `SubdivisionName` | `subdivision_name` | String |  | A neighborhood, community, complex or builder tract. |  |
| `SuppliesExpense` | `supplies_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `SyndicateTo` | `syndicate_to` | varchar (multi) | [`syndicate_to`](../lookups.md#syndicate_to) | When permitted by the broker, the options made by the agent on behalf of the seller, where they would like their listings syndicated (e.g., Zillow, Trulia, Realtor.com, Homes.com). |  |
| `SyndicationRemarks` | `syndication_remarks` | String |  | For MLSs that host a separate "Public Remarks" for syndication purposes, this field should be defaulted to contain public remarks. |  |
| `TaxAnnualAmount` | `tax_annual_amount` | Number |  | The annual property tax amount as of the last assessment made by the taxing authority. |  |
| `TaxAnnualAmountPerLivingAreaUnit` | `tax_annual_amount_per_living_area_unit` | Number |  | The annual property tax amount as of the last assessment made by the taxing authority divided by the property's living area. |  |
| `TaxAnnualAmountPerSquareFoot` | `tax_annual_amount_per_square_foot` | Number |  | The annual property tax amount as of the last assessment made by the taxing authority divided by the property's living area square footage. |  |
| `TaxAssessedValue` | `tax_assessed_value` | Number |  | The property value as of the last assessment made by the taxing authority. |  |
| `TaxBlock` | `tax_block` | String |  | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. |  |
| `TaxBookNumber` | `tax_book_number` | String |  | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. |  |
| `TaxLegalDescription` | `tax_legal_description` | String |  | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. |  |
| `TaxLot` | `tax_lot` | String |  | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. |  |
| `TaxMapNumber` | `tax_map_number` | String |  | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. |  |
| `TaxOtherAnnualAssessmentAmount` | `tax_other_annual_assessment_amount` | Number |  | Any other annual taxes, not including the tax reported in the TaxAmount field, as of the last assessment made by the taxing authority. |  |
| `TaxParcelLetter` | `tax_parcel_letter` | String |  | Some systems of parcel identification incorporate a method that utilizes a county identifier, a tax book number, a tax map number and a parcel identification number. |  |
| `TaxStatusCurrent` | `tax_status_current` | varchar (multi) | [`tax_status_current`](../lookups.md#tax_status_current) | The current tax status of the mobile home in cases where the land or space is included in the sale. |  |
| `TaxTract` | `tax_tract` | String |  | A type of legal description for land in developed areas where streets or other rights-of-ways delineate large parcels of land referred to as divided into lots on which homes or other types of developments are built. |  |
| `TaxYear` | `tax_year` | Number |  | The year in which the last assessment of the property value/tax was made. |  |
| `TenantPays` | `tenant_pays` | varchar (multi) | [`tenant_pays`](../lookups.md#tenant_pays) | A list of services or items that the tenant is responsible to pay. |  |
| `Topography` | `topography` | String |  | The state of the surface of the land included with the property (i.e., flat, rolling, etc.). |  |
| `TotalActualRent` | `total_actual_rent` | Number |  | Total actual rent currently being collected from tenants of the income property. |  |
| `Township` | `township` | String |  | A subdivision of the county. |  |
| `TransactionBrokerCompensation` | `transaction_broker_compensation` | String |  | The total commission to be paid to the transaction facilitator, expressed as either a percentage or a constant currency amount. |  |
| `TransactionBrokerCompensationType` | `transaction_broker_compensation_type` | enum | [`compensation_type`](../lookups.md#compensation_type) | A list of types to clarify the value entered in the TransactionBrokerCompensation field. |  |
| `TrashExpense` | `trash_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `UnitNumber` | `unit_number` | String |  | A text field containing the unit number or portion of a larger building or complex that should appear following the street suffix or, if it exists, the street suffix direction in the street address (e.g., Apt G, #55). |  |
| `UnitTypeType` | `unit_type_type` | varchar (multi) | [`unit_type_type`](../lookups.md#unit_type_type) | A list of floor plans or configurations of an individual unit (e.g., 1 Bedroom, Studio, Loft) in a multi-family or multi-unit development. |  |
| `UnitTypes` | `unit_types` | Collection |  | A collection of types of units included in the income (multifamily) property. | `[Collection]` |
| `UnitsFurnished` | `units_furnished` | enum | [`units_furnished`](../lookups.md#units_furnished) | States whether or not the units are furnished (i.e., All Units, Varies By Unit, None). |  |
| `UniversalPropertyId` | `universal_property_id` | String |  | The RESO Universal Property Identifier (UPI) is a unique identifier for all real property in the U.S. |  |
| `UniversalPropertySubId` | `universal_property_sub_id` | String |  | A unique identifier for all subsets or shares of real property in the U.S. |  |
| `UnparsedAddress` | `unparsed_address` | String |  | A text representation of the address with the full civic location as a single entity. |  |
| `Utilities` | `utilities` | varchar (multi) | [`utilities`](../lookups.md#utilities) | A list of the utilities for the property being sold/leased. |  |
| `VacancyAllowance` | `vacancy_allowance` | Number |  | An estimate of the amount of rent that may be foregone because of unoccupied units. |  |
| `VacancyAllowanceRate` | `vacancy_allowance_rate` | Number |  | An estimate of the percent of rent that may be foregone because of unoccupied units. |  |
| `Vegetation` | `vegetation` | varchar (multi) | [`vegetation`](../lookups.md#vegetation) | A list of the type(s) of residential vegetation on the property (not farm crops). |  |
| `VideosChangeTimestamp` | `videos_change_timestamp` | Timestamp |  | A system-generated timestamp of when the last update or change to the videos for this listing was made. |  |
| `VideosCount` | `videos_count` | Number |  | The total number of videos or virtual tours included with the listing. |  |
| `View` | `view` | varchar (multi) | [`view`](../lookups.md#view) | A view as seen from the listed property. |  |
| `ViewYN` | `view_yn` | Boolean |  | The property has a view. |  |
| `VirtualTourURLBranded` | `virtual_tour_url_branded` | String |  | A text field that holds the Uniform Resource Locator (URL) for a branded virtual tour of the property. |  |
| `VirtualTourURLUnbranded` | `virtual_tour_url_unbranded` | String |  | A text field that holds the Uniform Resource Locator (URL) for an unbranded virtual tour of the property. |  |
| `WalkScore` | `walk_score` | Number |  | A walkability index based on the time to walk from a property to nearby essentials such as grocery stores, schools, churches, etc. |  |
| `WaterBodyName` | `water_body_name` | String |  | The name, if known, of the body of water on which the property is located (e.g., lake name, river name, ocean name, sea name, canal name). |  |
| `WaterSewerExpense` | `water_sewer_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `WaterSource` | `water_source` | varchar (multi) | [`water_source`](../lookups.md#water_source) | A list of the source(s) of water for the property. |  |
| `WaterfrontFeatures` | `waterfront_features` | varchar (multi) | [`waterfront_features`](../lookups.md#waterfront_features) | The features of the waterfront on which the property is located. |  |
| `WaterfrontYN` | `waterfront_yn` | Boolean |  | The property is on a waterfront. |  |
| `WindowFeatures` | `window_features` | varchar (multi) | [`window_features`](../lookups.md#window_features) | A list of features or a description of the windows included in the sale/lease. |  |
| `WithdrawnDate` | `withdrawn_date` | Date |  | The date that the listing was withdrawn from the market. |  |
| `WoodedArea` | `wooded_area` | Number |  | A measurement or percentage of the property that is wooded or forest. |  |
| `WorkmansCompensationExpense` | `workmans_compensation_expense` | Number |  | The annual expense that is not paid directly by the tenant and is included in the Operating Expense calculations. |  |
| `YearBuilt` | `year_built` | Number |  | The year that an occupancy permit is first granted for the house or other local measure of initial habitability of the build. |  |
| `YearBuiltDetails` | `year_built_details` | String |  | A description of the details behind the year the structure was built. |  |
| `YearBuiltEffective` | `year_built_effective` | Number |  | The year a major rebuild/renovated of the structure occurred. |  |
| `YearBuiltSource` | `year_built_source` | enum | [`year_built_source`](../lookups.md#year_built_source) | A list of sources of the year built (e.g., Appraiser, Assessor, Builder, Estimated). |  |
| `YearEstablished` | `year_established` | Number |  | The year the business being sold was established. |  |
| `YearsCurrentOwner` | `years_current_owner` | Number |  | The number of years the current owner has had possession of the business. |  |
| `Zoning` | `zoning` | String |  | A division of the city or county into areas of different permissible land uses. |  |
| `ZoningDescription` | `zoning_description` | String |  | A list of descriptions of the zoning of the property. |  |

## Foreign keys OUT (this resource references)

- `property.buyer_agent_key` -> `member.member_key` (medium)
- `property.buyer_office_key` -> `office.office_key` (high)
- `property.buyer_team_key` -> `teams.team_key` (medium)
- `property.co_buyer_agent_key` -> `member.member_key` (medium)
- `property.co_buyer_office_key` -> `office.office_key` (high)
- `property.co_list_agent_key` -> `member.member_key` (medium)
- `property.co_list_office_key` -> `office.office_key` (high)
- `property.list_agent_key` -> `member.member_key` (medium)
- `property.list_office_key` -> `office.office_key` (high)
- `property.list_team_key` -> `teams.team_key` (medium)
- `property.originating_system_id` -> `ouid.organization_unique_id_key` (medium)
- `property.source_system_id` -> `ouid.organization_unique_id_key` (medium)

## Foreign keys IN (other resources reference this)

- `contact_listing_notes.listing_key` -> `property.listing_key` (medium)
- `contact_listings.listing_key` -> `property.listing_key` (medium)
- `property_green_verification.listing_id` -> `property.listing_key` (medium)
- `property_green_verification.listing_key` -> `property.listing_key` (medium)
- `property_power_production.listing_id` -> `property.listing_key` (medium)
- `property_power_production.listing_key` -> `property.listing_key` (medium)
- `property_rooms.listing_id` -> `property.listing_key` (medium)
- `property_rooms.listing_key` -> `property.listing_key` (medium)
- `property_unit_types.listing_id` -> `property.listing_key` (medium)
- `property_unit_types.listing_key` -> `property.listing_key` (medium)

## Inverse 1:N (collection-typed companions)

- `green_building_verification` -> `property_green_verification` (many `property_green_verification` per `property`)
- `history_transactional` -> `history_transactional` (many `history_transactional` per `property`)
- `media` -> `media` (many `media` per `property`)
- `open_house` -> `open_house` (many `open_house` per `property`)
- `power_production` -> `property_power_production` (many `property_power_production` per `property`)
- `rooms` -> `property_rooms` (many `property_rooms` per `property`)
- `social_media` -> `social_media` (many `social_media` per `property`)
- `unit_types` -> `property_unit_types` (many `property_unit_types` per `property`)

## Phase 2.5 satellite audit

Recommendations from `raw/satellites.csv`. `drop_from_host` rows are not present in the canonical DBML; `review` rows are kept but flagged; `keep_both` rows are silently kept.

| Column | FK | Recommendation | Notes |
|---|---|---|---|
| `buyer_agent_aor` | `buyer_agent_key` -> `member.member_aor` | `drop_from_host` |  |
| `buyer_agent_designation` | `buyer_agent_key` -> `member.member_designation` | `drop_from_host` |  |
| `buyer_agent_direct_phone` | `buyer_agent_key` -> `member.member_direct_phone` | `drop_from_host` |  |
| `buyer_agent_email` | `buyer_agent_key` -> `member.member_email` | `drop_from_host` |  |
| `buyer_agent_fax` | `buyer_agent_key` -> `member.member_fax` | `drop_from_host` |  |
| `buyer_agent_first_name` | `buyer_agent_key` -> `member.member_first_name` | `drop_from_host` |  |
| `buyer_agent_full_name` | `buyer_agent_key` -> `member.member_full_name` | `drop_from_host` |  |
| `buyer_agent_home_phone` | `buyer_agent_key` -> `member.member_home_phone` | `drop_from_host` |  |
| `buyer_agent_last_name` | `buyer_agent_key` -> `member.member_last_name` | `drop_from_host` |  |
| `buyer_agent_middle_name` | `buyer_agent_key` -> `member.member_middle_name` | `drop_from_host` |  |
| `buyer_agent_mls_id` | `buyer_agent_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `buyer_agent_mobile_phone` | `buyer_agent_key` -> `member.member_mobile_phone` | `drop_from_host` |  |
| `buyer_agent_name_prefix` | `buyer_agent_key` -> `member.member_name_prefix` | `drop_from_host` |  |
| `buyer_agent_name_suffix` | `buyer_agent_key` -> `member.member_name_suffix` | `drop_from_host` |  |
| `buyer_agent_office_phone` | `buyer_agent_key` -> `member.member_office_phone` | `drop_from_host` |  |
| `buyer_agent_office_phone_ext` | `buyer_agent_key` -> `member.member_office_phone_ext` | `drop_from_host` |  |
| `buyer_agent_pager` | `buyer_agent_key` -> `member.member_pager` | `drop_from_host` |  |
| `buyer_agent_preferred_phone` | `buyer_agent_key` -> `member.member_preferred_phone` | `drop_from_host` |  |
| `buyer_agent_preferred_phone_ext` | `buyer_agent_key` -> `member.member_preferred_phone_ext` | `drop_from_host` |  |
| `buyer_agent_state_license` | `buyer_agent_key` -> `member.member_state_license` | `drop_from_host` |  |
| `buyer_agent_toll_free_phone` | `buyer_agent_key` -> `member.member_toll_free_phone` | `drop_from_host` |  |
| `buyer_agent_url` | `buyer_agent_key` -> `member.?` | `keep_both` | no_child_match |
| `buyer_agent_voice_mail` | `buyer_agent_key` -> `member.member_voice_mail` | `drop_from_host` |  |
| `buyer_agent_voice_mail_ext` | `buyer_agent_key` -> `member.member_voice_mail_ext` | `drop_from_host` |  |
| `buyer_office_aor` | `buyer_office_key` -> `office.office_aor` | `drop_from_host` |  |
| `buyer_office_email` | `buyer_office_key` -> `office.office_email` | `drop_from_host` |  |
| `buyer_office_fax` | `buyer_office_key` -> `office.office_fax` | `drop_from_host` |  |
| `buyer_office_mls_id` | `buyer_office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `buyer_office_name` | `buyer_office_key` -> `office.office_name` | `drop_from_host` |  |
| `buyer_office_phone` | `buyer_office_key` -> `office.office_phone` | `drop_from_host` |  |
| `buyer_office_phone_ext` | `buyer_office_key` -> `office.office_phone_ext` | `drop_from_host` |  |
| `buyer_office_url` | `buyer_office_key` -> `office.?` | `keep_both` | no_child_match |
| `buyer_team_name` | `buyer_team_key` -> `teams.team_name` | `review` | name_type_match_but_definitions_differ |
| `co_buyer_agent_aor` | `co_buyer_agent_key` -> `member.member_aor` | `drop_from_host` |  |
| `co_buyer_agent_designation` | `co_buyer_agent_key` -> `member.member_designation` | `drop_from_host` |  |
| `co_buyer_agent_direct_phone` | `co_buyer_agent_key` -> `member.member_direct_phone` | `drop_from_host` |  |
| `co_buyer_agent_email` | `co_buyer_agent_key` -> `member.member_email` | `drop_from_host` |  |
| `co_buyer_agent_fax` | `co_buyer_agent_key` -> `member.member_fax` | `drop_from_host` |  |
| `co_buyer_agent_first_name` | `co_buyer_agent_key` -> `member.member_first_name` | `drop_from_host` |  |
| `co_buyer_agent_full_name` | `co_buyer_agent_key` -> `member.member_full_name` | `drop_from_host` |  |
| `co_buyer_agent_home_phone` | `co_buyer_agent_key` -> `member.member_home_phone` | `drop_from_host` |  |
| `co_buyer_agent_last_name` | `co_buyer_agent_key` -> `member.member_last_name` | `drop_from_host` |  |
| `co_buyer_agent_middle_name` | `co_buyer_agent_key` -> `member.member_middle_name` | `drop_from_host` |  |
| `co_buyer_agent_mls_id` | `co_buyer_agent_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `co_buyer_agent_mobile_phone` | `co_buyer_agent_key` -> `member.member_mobile_phone` | `drop_from_host` |  |
| `co_buyer_agent_name_prefix` | `co_buyer_agent_key` -> `member.member_name_prefix` | `drop_from_host` |  |
| `co_buyer_agent_name_suffix` | `co_buyer_agent_key` -> `member.member_name_suffix` | `drop_from_host` |  |
| `co_buyer_agent_office_phone` | `co_buyer_agent_key` -> `member.member_office_phone` | `drop_from_host` |  |
| `co_buyer_agent_office_phone_ext` | `co_buyer_agent_key` -> `member.member_office_phone_ext` | `drop_from_host` |  |
| `co_buyer_agent_pager` | `co_buyer_agent_key` -> `member.member_pager` | `drop_from_host` |  |
| `co_buyer_agent_preferred_phone` | `co_buyer_agent_key` -> `member.member_preferred_phone` | `drop_from_host` |  |
| `co_buyer_agent_preferred_phone_ext` | `co_buyer_agent_key` -> `member.member_preferred_phone_ext` | `drop_from_host` |  |
| `co_buyer_agent_state_license` | `co_buyer_agent_key` -> `member.member_state_license` | `drop_from_host` |  |
| `co_buyer_agent_toll_free_phone` | `co_buyer_agent_key` -> `member.member_toll_free_phone` | `drop_from_host` |  |
| `co_buyer_agent_url` | `co_buyer_agent_key` -> `member.?` | `keep_both` | no_child_match |
| `co_buyer_agent_voice_mail` | `co_buyer_agent_key` -> `member.member_voice_mail` | `drop_from_host` |  |
| `co_buyer_agent_voice_mail_ext` | `co_buyer_agent_key` -> `member.member_voice_mail_ext` | `drop_from_host` |  |
| `co_buyer_office_aor` | `co_buyer_office_key` -> `office.office_aor` | `drop_from_host` |  |
| `co_buyer_office_email` | `co_buyer_office_key` -> `office.office_email` | `drop_from_host` |  |
| `co_buyer_office_fax` | `co_buyer_office_key` -> `office.office_fax` | `drop_from_host` |  |
| `co_buyer_office_mls_id` | `co_buyer_office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `co_buyer_office_name` | `co_buyer_office_key` -> `office.office_name` | `drop_from_host` |  |
| `co_buyer_office_phone` | `co_buyer_office_key` -> `office.office_phone` | `drop_from_host` |  |
| `co_buyer_office_phone_ext` | `co_buyer_office_key` -> `office.office_phone_ext` | `drop_from_host` |  |
| `co_buyer_office_url` | `co_buyer_office_key` -> `office.?` | `keep_both` | no_child_match |
| `co_list_agent_aor` | `co_list_agent_key` -> `member.member_aor` | `drop_from_host` |  |
| `co_list_agent_designation` | `co_list_agent_key` -> `member.member_designation` | `drop_from_host` |  |
| `co_list_agent_direct_phone` | `co_list_agent_key` -> `member.member_direct_phone` | `drop_from_host` |  |
| `co_list_agent_email` | `co_list_agent_key` -> `member.member_email` | `drop_from_host` |  |
| `co_list_agent_fax` | `co_list_agent_key` -> `member.member_fax` | `drop_from_host` |  |
| `co_list_agent_first_name` | `co_list_agent_key` -> `member.member_first_name` | `drop_from_host` |  |
| `co_list_agent_full_name` | `co_list_agent_key` -> `member.member_full_name` | `drop_from_host` |  |
| `co_list_agent_home_phone` | `co_list_agent_key` -> `member.member_home_phone` | `drop_from_host` |  |
| `co_list_agent_last_name` | `co_list_agent_key` -> `member.member_last_name` | `drop_from_host` |  |
| `co_list_agent_middle_name` | `co_list_agent_key` -> `member.member_middle_name` | `drop_from_host` |  |
| `co_list_agent_mls_id` | `co_list_agent_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `co_list_agent_mobile_phone` | `co_list_agent_key` -> `member.member_mobile_phone` | `drop_from_host` |  |
| `co_list_agent_name_prefix` | `co_list_agent_key` -> `member.member_name_prefix` | `drop_from_host` |  |
| `co_list_agent_name_suffix` | `co_list_agent_key` -> `member.member_name_suffix` | `drop_from_host` |  |
| `co_list_agent_office_phone` | `co_list_agent_key` -> `member.member_office_phone` | `drop_from_host` |  |
| `co_list_agent_office_phone_ext` | `co_list_agent_key` -> `member.member_office_phone_ext` | `drop_from_host` |  |
| `co_list_agent_pager` | `co_list_agent_key` -> `member.member_pager` | `drop_from_host` |  |
| `co_list_agent_preferred_phone` | `co_list_agent_key` -> `member.member_preferred_phone` | `drop_from_host` |  |
| `co_list_agent_preferred_phone_ext` | `co_list_agent_key` -> `member.member_preferred_phone_ext` | `drop_from_host` |  |
| `co_list_agent_state_license` | `co_list_agent_key` -> `member.member_state_license` | `drop_from_host` |  |
| `co_list_agent_toll_free_phone` | `co_list_agent_key` -> `member.member_toll_free_phone` | `drop_from_host` |  |
| `co_list_agent_url` | `co_list_agent_key` -> `member.?` | `keep_both` | no_child_match |
| `co_list_agent_voice_mail` | `co_list_agent_key` -> `member.member_voice_mail` | `drop_from_host` |  |
| `co_list_agent_voice_mail_ext` | `co_list_agent_key` -> `member.member_voice_mail_ext` | `drop_from_host` |  |
| `co_list_office_aor` | `co_list_office_key` -> `office.office_aor` | `drop_from_host` |  |
| `co_list_office_email` | `co_list_office_key` -> `office.office_email` | `drop_from_host` |  |
| `co_list_office_fax` | `co_list_office_key` -> `office.office_fax` | `drop_from_host` |  |
| `co_list_office_mls_id` | `co_list_office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `co_list_office_name` | `co_list_office_key` -> `office.office_name` | `drop_from_host` |  |
| `co_list_office_phone` | `co_list_office_key` -> `office.office_phone` | `drop_from_host` |  |
| `co_list_office_phone_ext` | `co_list_office_key` -> `office.office_phone_ext` | `drop_from_host` |  |
| `co_list_office_url` | `co_list_office_key` -> `office.?` | `keep_both` | no_child_match |
| `list_agent_aor` | `list_agent_key` -> `member.member_aor` | `drop_from_host` |  |
| `list_agent_designation` | `list_agent_key` -> `member.member_designation` | `drop_from_host` |  |
| `list_agent_direct_phone` | `list_agent_key` -> `member.member_direct_phone` | `drop_from_host` |  |
| `list_agent_email` | `list_agent_key` -> `member.member_email` | `drop_from_host` |  |
| `list_agent_fax` | `list_agent_key` -> `member.member_fax` | `drop_from_host` |  |
| `list_agent_first_name` | `list_agent_key` -> `member.member_first_name` | `drop_from_host` |  |
| `list_agent_full_name` | `list_agent_key` -> `member.member_full_name` | `drop_from_host` |  |
| `list_agent_home_phone` | `list_agent_key` -> `member.member_home_phone` | `drop_from_host` |  |
| `list_agent_last_name` | `list_agent_key` -> `member.member_last_name` | `drop_from_host` |  |
| `list_agent_middle_name` | `list_agent_key` -> `member.member_middle_name` | `drop_from_host` |  |
| `list_agent_mls_id` | `list_agent_key` -> `member.member_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `list_agent_mobile_phone` | `list_agent_key` -> `member.member_mobile_phone` | `drop_from_host` |  |
| `list_agent_name_prefix` | `list_agent_key` -> `member.member_name_prefix` | `drop_from_host` |  |
| `list_agent_name_suffix` | `list_agent_key` -> `member.member_name_suffix` | `drop_from_host` |  |
| `list_agent_office_phone` | `list_agent_key` -> `member.member_office_phone` | `drop_from_host` |  |
| `list_agent_office_phone_ext` | `list_agent_key` -> `member.member_office_phone_ext` | `drop_from_host` |  |
| `list_agent_pager` | `list_agent_key` -> `member.member_pager` | `drop_from_host` |  |
| `list_agent_preferred_phone` | `list_agent_key` -> `member.member_preferred_phone` | `drop_from_host` |  |
| `list_agent_preferred_phone_ext` | `list_agent_key` -> `member.member_preferred_phone_ext` | `drop_from_host` |  |
| `list_agent_state_license` | `list_agent_key` -> `member.member_state_license` | `drop_from_host` |  |
| `list_agent_toll_free_phone` | `list_agent_key` -> `member.member_toll_free_phone` | `drop_from_host` |  |
| `list_agent_url` | `list_agent_key` -> `member.?` | `keep_both` | no_child_match |
| `list_agent_voice_mail` | `list_agent_key` -> `member.member_voice_mail` | `drop_from_host` |  |
| `list_agent_voice_mail_ext` | `list_agent_key` -> `member.member_voice_mail_ext` | `drop_from_host` |  |
| `list_office_aor` | `list_office_key` -> `office.office_aor` | `drop_from_host` |  |
| `list_office_email` | `list_office_key` -> `office.office_email` | `drop_from_host` |  |
| `list_office_fax` | `list_office_key` -> `office.office_fax` | `drop_from_host` |  |
| `list_office_mls_id` | `list_office_key` -> `office.office_mls_id` | `drop_from_host` | id_suffix_threshold_0.7 |
| `list_office_name` | `list_office_key` -> `office.office_name` | `drop_from_host` |  |
| `list_office_phone` | `list_office_key` -> `office.office_phone` | `drop_from_host` |  |
| `list_office_phone_ext` | `list_office_key` -> `office.office_phone_ext` | `drop_from_host` |  |
| `list_office_url` | `list_office_key` -> `office.?` | `keep_both` | no_child_match |
| `list_team_name` | `list_team_key` -> `teams.team_name` | `review` | name_type_match_but_definitions_differ |
| `originating_system_key` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `originating_system_name` | `originating_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_key` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |
| `source_system_name` | `source_system_id` -> `ouid.?` | `keep_both` | no_child_match |

