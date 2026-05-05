# Lookups (RESO DD 2.0)

222 lookups extracted from `raw/lookups.csv` and `raw/lookup_values.csv`. Use the table of contents to jump; each anchor is the snake-cased lookup name.

Kinds:

- **closed-SV** - a `String List, Single` column with a closed value list. Emitted as a DBML `Enum` in `wiki/dbml/lookups.dbml`.
- **closed-MV** - a `String List, Multi` column with a closed value list. Stored as `varchar` in DBML; column note carries `multi: <name>`.
- **open** - jurisdiction-defined or no closed value list (e.g. `AOR`, `City`). Stored as `varchar`.

## Index

| Lookup | Kind | Values | Used by |
|---|---|---:|---|
| [`accessibility_features`](#accessibility_features) | closed-MV | 35 | `property.accessibility_features` |
| [`actor_type`](#actor_type) | closed-SV | 5 | `internet_tracking.actor_type` |
| [`aor`](#aor) | open | 0 | 13 columns |
| [`appliances`](#appliances) | closed-MV | 75 | `property.appliances` |
| [`architectural_style`](#architectural_style) | closed-MV | 44 | `property.architectural_style` |
| [`area_source`](#area_source) | closed-SV | 9 | 8 columns |
| [`area_units`](#area_units) | closed-SV | 2 | 9 columns |
| [`association_amenities`](#association_amenities) | closed-MV | 76 | `property.association_amenities` |
| [`association_fee_includes`](#association_fee_includes) | closed-MV | 15 | `property.association_fee_includes` |
| [`association_status`](#association_status) | closed-SV | 2 | `association.association_status` |
| [`association_type`](#association_type) | closed-SV | 3 | `association.association_type` |
| [`attended`](#attended) | closed-SV | 3 | `open_house.open_house_attended_by` |
| [`basement`](#basement) | closed-MV | 24 | `property.basement` |
| [`billing_preference`](#billing_preference) | closed-SV | 3 | `member.member_billing_preference` |
| [`body_type`](#body_type) | closed-MV | 7 | `property.body_type` |
| [`building_features`](#building_features) | open | 0 | `property.building_features` |
| [`business_type`](#business_type) | closed-MV | 109 | `property.business_type` |
| [`buyer_agent_designation`](#buyer_agent_designation) | closed-MV | 27 | `property.buyer_agent_designation` |
| [`buyer_financing`](#buyer_financing) | closed-MV | 13 | `property.buyer_financing` |
| [`caravan_allowed_class_names`](#caravan_allowed_class_names) | closed-MV | 9 | `caravan.caravan_allowed_class_names` |
| [`caravan_allowed_statuses`](#caravan_allowed_statuses) | closed-MV | 3 | `caravan.caravan_allowed_statuses` |
| [`caravan_resource_name`](#caravan_resource_name) | closed-SV | 7 | `caravan.caravan_organizer_resource_name`, `caravan_stop.stop_resource_name` |
| [`caravan_status`](#caravan_status) | closed-SV | 3 | `caravan.caravan_status` |
| [`caravan_stop_attended`](#caravan_stop_attended) | closed-SV | 3 | `caravan_stop.stop_attended_by` |
| [`caravan_stop_class_name`](#caravan_stop_class_name) | closed-SV | 9 | `caravan_stop.stop_class_name` |
| [`caravan_type`](#caravan_type) | closed-SV | 3 | `caravan.caravan_type` |
| [`change_type`](#change_type) | closed-SV | 13 | `history_transactional.change_type`, `property.major_change_type` |
| [`city`](#city) | open | 0 | `property.city` |
| [`class_name`](#class_name) | closed-SV | 17 | 8 columns |
| [`closet_type`](#closet_type) | closed-SV | 3 | `property_rooms.bedroom_closet_type` |
| [`co_buyer_agent_designation`](#co_buyer_agent_designation) | closed-MV | 27 | `property.co_buyer_agent_designation` |
| [`co_list_agent_designation`](#co_list_agent_designation) | closed-MV | 27 | `property.co_list_agent_designation` |
| [`common_interest`](#common_interest) | closed-SV | 6 | `property.common_interest` |
| [`common_walls`](#common_walls) | closed-MV | 6 | `property.common_walls` |
| [`community_features`](#community_features) | closed-MV | 21 | `property.community_features` |
| [`compensation_type`](#compensation_type) | closed-SV | 4 | `property.buyer_brokerage_compensation_type`, `property.sub_agency_compensation_type`, `property.transaction_broker_compensation_type` |
| [`concessions`](#concessions) | closed-SV | 3 | `property.concessions` |
| [`construction_materials`](#construction_materials) | closed-MV | 54 | `property.construction_materials` |
| [`contact_listing_preference`](#contact_listing_preference) | closed-SV | 3 | `contact_listings.contact_listing_preference` |
| [`contact_status`](#contact_status) | closed-SV | 4 | `contacts.contact_status` |
| [`contact_type`](#contact_type) | closed-MV | 22 | `contacts.contact_type` |
| [`cooling`](#cooling) | closed-MV | 24 | `property.cooling` |
| [`country`](#country) | closed-SV | 246 | 12 columns |
| [`county_or_parish`](#county_or_parish) | open | 0 | 11 columns |
| [`current_financing`](#current_financing) | closed-MV | 15 | `property.current_financing` |
| [`current_or_possible_use`](#current_or_possible_use) | closed-MV | 43 | `property.current_use`, `property.possible_use` |
| [`daily_schedule`](#daily_schedule) | closed-MV | 15 | `prospecting.daily_schedule` |
| [`development_status`](#development_status) | closed-MV | 10 | `property.development_status` |
| [`device_type`](#device_type) | closed-SV | 5 | `internet_tracking.device_type` |
| [`direction_faces`](#direction_faces) | closed-SV | 8 | `property.direction_faces` |
| [`disclosures`](#disclosures) | open | 0 | `property.disclosures` |
| [`documents_available`](#documents_available) | open | 0 | `property.documents_available` |
| [`document_status`](#document_status) | closed-SV | 16 | `property.document_status` |
| [`door_features`](#door_features) | closed-MV | 5 | `property.door_features` |
| [`electric`](#electric) | closed-MV | 18 | `property.electric` |
| [`elementary_school`](#elementary_school) | open | 0 | `property.elementary_school` |
| [`elementary_school_district`](#elementary_school_district) | open | 0 | `property.elementary_school_district` |
| [`event_source`](#event_source) | closed-SV | 6 | `internet_tracking.event_source` |
| [`event_target`](#event_target) | closed-SV | 21 | `internet_tracking.event_target` |
| [`event_type`](#event_type) | closed-SV | 20 | `internet_tracking.event_type` |
| [`existing_lease_type`](#existing_lease_type) | closed-MV | 9 | `property.available_lease_type`, `property.existing_lease_type` |
| [`exterior_features`](#exterior_features) | closed-MV | 37 | `property.exterior_features` |
| [`fee_frequency`](#fee_frequency) | closed-SV | 11 | 4 columns |
| [`fencing`](#fencing) | closed-MV | 29 | `property.fencing` |
| [`fha_eligibility`](#fha_eligibility) | closed-SV | 5 | `property.fha_eligibility` |
| [`financial_data_source`](#financial_data_source) | closed-MV | 3 | `property.financial_data_source` |
| [`fireplace_features`](#fireplace_features) | closed-MV | 44 | `property.fireplace_features` |
| [`flooring`](#flooring) | closed-MV | 39 | `property.flooring` |
| [`foundation_details`](#foundation_details) | closed-MV | 12 | `property.foundation_details` |
| [`frontage_type`](#frontage_type) | closed-MV | 9 | `property.frontage_type` |
| [`furnished`](#furnished) | closed-SV | 4 | `property.furnished`, `property_unit_types.unit_type_furnished` |
| [`green_building_verification_type`](#green_building_verification_type) | closed-SV | 18 | `property.green_building_verification_type`, `property_green_verification.green_building_verification_type` |
| [`green_energy_efficient`](#green_energy_efficient) | closed-MV | 12 | `property.green_energy_efficient` |
| [`green_energy_generation`](#green_energy_generation) | closed-MV | 2 | `property.green_energy_generation` |
| [`green_indoor_air_quality`](#green_indoor_air_quality) | closed-MV | 4 | `property.green_indoor_air_quality` |
| [`green_location`](#green_location) | open | 0 | `property.green_location` |
| [`green_sustainability`](#green_sustainability) | closed-MV | 7 | `property.green_sustainability` |
| [`green_verification_source`](#green_verification_source) | closed-SV | 10 | `property_green_verification.green_verification_source` |
| [`green_verification_status`](#green_verification_status) | closed-SV | 2 | `property_green_verification.green_verification_status` |
| [`green_water_conservation`](#green_water_conservation) | closed-MV | 6 | `property.green_water_conservation` |
| [`heating`](#heating) | closed-MV | 42 | `property.heating` |
| [`high_school`](#high_school) | open | 0 | `property.high_school` |
| [`high_school_district`](#high_school_district) | open | 0 | `property.high_school_district` |
| [`horse_amenities`](#horse_amenities) | closed-MV | 18 | `property.horse_amenities` |
| [`hours_days_of_operation`](#hours_days_of_operation) | closed-MV | 9 | `property.hours_days_of_operation` |
| [`iana_time_zone_values`](#iana_time_zone_values) | closed-SV | 482 | `lock_or_box.listing_time_zone`, `property.property_time_zone_name`, `showing.showing_time_zone` |
| [`image_of`](#image_of) | closed-SV | 86 | `media.image_of` |
| [`image_size_description`](#image_size_description) | open | 0 | `media.image_size_description` |
| [`income_includes`](#income_includes) | closed-MV | 6 | `property.income_includes` |
| [`interior_or_room_features`](#interior_or_room_features) | closed-MV | 53 | `property.interior_features`, `property_rooms.room_features` |
| [`irrigation_source`](#irrigation_source) | open | 0 | `property.irrigation_source` |
| [`labor_information`](#labor_information) | closed-MV | 3 | `property.labor_information` |
| [`languages`](#languages) | closed-SV | 190 | `contacts.language`, `member.member_languages`, `prospecting.language` |
| [`laundry_features`](#laundry_features) | closed-MV | 24 | `property.laundry_features` |
| [`lease_renewal_compensation`](#lease_renewal_compensation) | closed-MV | 5 | `property.lease_renewal_compensation` |
| [`lease_term`](#lease_term) | closed-SV | 10 | `property.lease_term` |
| [`levels`](#levels) | closed-MV | 8 | `property.levels` |
| [`linear_units`](#linear_units) | closed-SV | 2 | 15 columns |
| [`list_agent_designation`](#list_agent_designation) | closed-MV | 27 | `property.list_agent_designation` |
| [`listing_agreement`](#listing_agreement) | closed-SV | 7 | `property.listing_agreement` |
| [`listing_service`](#listing_service) | closed-SV | 3 | `property.listing_service` |
| [`listing_terms`](#listing_terms) | closed-MV | 26 | `property.listing_terms` |
| [`listing_url_description`](#listing_url_description) | closed-SV | 7 | `property.listing_url_description` |
| [`lock_box_type`](#lock_box_type) | closed-MV | 8 | `property.lock_box_type` |
| [`lock_or_box_access_type`](#lock_or_box_access_type) | closed-MV | 3 | `lock_or_box.lock_or_box_access_type` |
| [`lot_dimensions_source`](#lot_dimensions_source) | closed-SV | 11 | `property.lot_dimensions_source` |
| [`lot_features`](#lot_features) | closed-MV | 56 | `property.lot_features` |
| [`lot_size_source`](#lot_size_source) | closed-SV | 9 | `property.lot_size_source` |
| [`lot_size_units`](#lot_size_units) | closed-SV | 3 | `property.lot_size_units` |
| [`media_alteration`](#media_alteration) | closed-MV | 10 | `media.media_alteration` |
| [`media_category`](#media_category) | closed-SV | 9 | `media.media_category` |
| [`media_status`](#media_status) | open | 0 | `media.media_status` |
| [`media_type`](#media_type) | closed-SV | 16 | `media.media_type` |
| [`member_association_bill_status`](#member_association_bill_status) | closed-SV | 3 | `member_association.member_association_bill_status` |
| [`member_designation`](#member_designation) | closed-MV | 27 | `member.member_designation` |
| [`member_mls_security_class`](#member_mls_security_class) | open | 0 | `member.member_mls_security_class` |
| [`member_other_phone_type`](#member_other_phone_type) | closed-SV | 14 | `member.member_other_phone_type` |
| [`member_state_license_type`](#member_state_license_type) | closed-SV | 3 | `member_state_license.member_state_license_type` |
| [`member_status`](#member_status) | closed-SV | 2 | `member.member_status`, `member_association.member_association_status` |
| [`member_type`](#member_type) | closed-SV | 19 | `member.member_type` |
| [`middle_or_junior_school`](#middle_or_junior_school) | open | 0 | `property.middle_or_junior_school` |
| [`middle_or_junior_school_district`](#middle_or_junior_school_district) | open | 0 | `property.middle_or_junior_school_district` |
| [`mls_area_major`](#mls_area_major) | open | 0 | `property.mls_area_major` |
| [`mls_area_minor`](#mls_area_minor) | open | 0 | `property.mls_area_minor` |
| [`mls_status`](#mls_status) | open | 0 | `property.mls_status` |
| [`noted_by`](#noted_by) | closed-SV | 2 | `contact_listing_notes.noted_by` |
| [`object_id_type`](#object_id_type) | closed-SV | 8 | `internet_tracking.object_id_type` |
| [`object_type`](#object_type) | closed-SV | 7 | `internet_tracking.object_type` |
| [`occupant_type`](#occupant_type) | closed-SV | 3 | `property.occupant_type` |
| [`office_association_primary_indicator`](#office_association_primary_indicator) | closed-SV | 4 | `office_association.office_association_primary_indicator` |
| [`office_branch_type`](#office_branch_type) | closed-SV | 3 | `office.office_branch_type` |
| [`office_corporate_license_type`](#office_corporate_license_type) | closed-SV | 2 | `office_corporate_license.office_corporate_license_type` |
| [`office_status`](#office_status) | closed-SV | 2 | `office.office_status`, `office_association.office_association_status` |
| [`office_type`](#office_type) | closed-SV | 11 | `office.office_type` |
| [`open_house_status`](#open_house_status) | closed-SV | 3 | `open_house.open_house_status` |
| [`open_house_type`](#open_house_type) | closed-SV | 5 | `open_house.open_house_type` |
| [`operating_expense_includes`](#operating_expense_includes) | closed-MV | 33 | `property.operating_expense_includes` |
| [`organization_type`](#organization_type) | open | 0 | `ouid.organization_type` |
| [`other_equipment`](#other_equipment) | closed-MV | 21 | `property.other_equipment` |
| [`other_phone_type`](#other_phone_type) | closed-SV | 14 | `contacts.other_phone_type`, `other_phone.other_phone_type` |
| [`other_structures`](#other_structures) | closed-MV | 33 | `property.other_structures` |
| [`owner_pays`](#owner_pays) | closed-MV | 29 | `property.owner_pays` |
| [`ownership_type`](#ownership_type) | closed-SV | 4 | `property.ownership_type` |
| [`parking_features`](#parking_features) | closed-MV | 72 | `property.parking_features` |
| [`patio_and_porch_features`](#patio_and_porch_features) | closed-MV | 16 | `property.patio_and_porch_features` |
| [`permission`](#permission) | closed-MV | 7 | `media.permission` |
| [`pets_allowed`](#pets_allowed) | closed-MV | 8 | `property.pets_allowed` |
| [`pool_features`](#pool_features) | closed-MV | 35 | `property.pool_features` |
| [`possession`](#possession) | closed-MV | 12 | `property.possession` |
| [`postal_city`](#postal_city) | open | 0 | `property.postal_city` |
| [`power_production_annual_status`](#power_production_annual_status) | closed-SV | 3 | `property_power_production.power_production_annual_status` |
| [`power_production_ownership`](#power_production_ownership) | closed-SV | 2 | `property_power_production.power_production_ownership` |
| [`power_production_type`](#power_production_type) | closed-SV | 2 | `property.power_production_type`, `property_power_production.power_production_type` |
| [`power_storage_type`](#power_storage_type) | closed-SV | 5 | `property_power_storage.power_storage_type` |
| [`preferred_address`](#preferred_address) | closed-SV | 3 | `contacts.preferred_address` |
| [`preferred_mail`](#preferred_mail) | closed-SV | 4 | `member.member_preferred_mail` |
| [`preferred_media`](#preferred_media) | closed-SV | 3 | `member.member_preferred_media`, `office.office_preferred_media` |
| [`preferred_phone`](#preferred_phone) | closed-SV | 7 | `contacts.preferred_phone` |
| [`preferred_publication`](#preferred_publication) | closed-SV | 5 | `member.member_preferred_publication` |
| [`property_condition`](#property_condition) | closed-MV | 5 | `property.property_condition` |
| [`property_sub_type`](#property_sub_type) | closed-SV | 31 | `property.property_sub_type` |
| [`property_type`](#property_type) | closed-SV | 9 | `property.property_type` |
| [`queue_transaction_type`](#queue_transaction_type) | closed-SV | 3 | `queue.queue_transaction_type` |
| [`reason_active_or_disabled`](#reason_active_or_disabled) | closed-SV | 16 | `prospecting.reason_active_or_disabled` |
| [`rent_includes`](#rent_includes) | closed-MV | 13 | `property.rent_includes` |
| [`resource_name`](#resource_name) | closed-SV | 5 | 7 columns |
| [`response_types`](#response_types) | closed-SV | 2 | `internet_tracking_summary.response_type` |
| [`road_frontage_type`](#road_frontage_type) | closed-MV | 13 | `property.road_frontage_type` |
| [`road_responsibility`](#road_responsibility) | closed-MV | 3 | `property.road_responsibility` |
| [`road_surface_type`](#road_surface_type) | closed-MV | 11 | `property.road_surface_type` |
| [`roof`](#roof) | closed-MV | 34 | `property.roof` |
| [`room_length_width_source`](#room_length_width_source) | closed-SV | 11 | `property_rooms.room_length_width_source` |
| [`room_level`](#room_level) | closed-SV | 7 | `property_rooms.room_level` |
| [`room_type`](#room_type) | closed-SV | 33 | `property.room_type`, `property_rooms.room_type` |
| [`rule_format`](#rule_format) | closed-SV | 4 | `rules.rule_format` |
| [`rule_type`](#rule_type) | open | 0 | `rules.rule_type` |
| [`saved_search_type`](#saved_search_type) | open | 0 | `saved_search.saved_search_type` |
| [`schedule_type`](#schedule_type) | closed-SV | 3 | `prospecting.schedule_type` |
| [`search_query_exceptions`](#search_query_exceptions) | open | 0 | `saved_search.search_query_exceptions` |
| [`search_query_type`](#search_query_type) | closed-SV | 2 | `saved_search.search_query_type` |
| [`security_features`](#security_features) | closed-MV | 28 | `property.security_features` |
| [`sewer`](#sewer) | closed-MV | 15 | `property.sewer` |
| [`showing_appointment_method`](#showing_appointment_method) | closed-MV | 3 | `showing_appointment.showing_appointment_method` |
| [`showing_appointment_status`](#showing_appointment_status) | closed-SV | 4 | `showing_appointment.showing_appointment_status` |
| [`showing_considerations`](#showing_considerations) | closed-MV | 14 | `property.showing_considerations` |
| [`showing_contact_type`](#showing_contact_type) | closed-MV | 4 | `property.showing_contact_type` |
| [`showing_days`](#showing_days) | open | 0 | `property.showing_days` |
| [`showing_method`](#showing_method) | closed-MV | 3 | `showing_availability.showing_method` |
| [`showing_method_request`](#showing_method_request) | closed-MV | 3 | `showing_request.showing_method_request` |
| [`showing_requestor`](#showing_requestor) | closed-MV | 11 | `showing_request.showing_requestor` |
| [`showing_request_type`](#showing_request_type) | closed-MV | 6 | `showing_request.showing_request_type` |
| [`showing_requirements`](#showing_requirements) | closed-MV | 18 | `property.showing_requirements` |
| [`showing_service_name`](#showing_service_name) | closed-SV | 10 | `property.showing_service_name` |
| [`showing_status`](#showing_status) | closed-SV | 4 | `showing.showing_status` |
| [`skirt`](#skirt) | closed-MV | 19 | `property.skirt` |
| [`social_media_type`](#social_media_type) | closed-SV | 17 | 7 columns |
| [`spa_features`](#spa_features) | closed-MV | 10 | `property.spa_features` |
| [`special_licenses`](#special_licenses) | closed-MV | 13 | `property.special_licenses` |
| [`special_listing_conditions`](#special_listing_conditions) | closed-MV | 12 | `property.special_listing_conditions` |
| [`standard_status`](#standard_status) | closed-SV | 11 | `property.standard_status` |
| [`state_or_province`](#state_or_province) | closed-SV | 65 | 19 columns |
| [`street_direction`](#street_direction) | closed-SV | 8 | `property.street_dir_prefix`, `property.street_dir_suffix` |
| [`street_suffix`](#street_suffix) | open | 0 | `property.street_suffix` |
| [`structure_type`](#structure_type) | closed-MV | 17 | `property.structure_type` |
| [`syndicate_agent_option`](#syndicate_agent_option) | open | 0 | `office.syndicate_agent_option` |
| [`syndicate_to`](#syndicate_to) | closed-MV | 4 | `member.syndicate_to`, `office.syndicate_to`, `property.syndicate_to` |
| [`tax_status_current`](#tax_status_current) | closed-MV | 3 | `property.tax_status_current` |
| [`team_impersonation_level`](#team_impersonation_level) | open | 0 | `team_members.team_impersonation_level` |
| [`team_member_type`](#team_member_type) | closed-SV | 10 | `team_members.team_member_type` |
| [`team_status`](#team_status) | closed-SV | 2 | `teams.team_status` |
| [`tenant_pays`](#tenant_pays) | closed-MV | 29 | `property.tenant_pays` |
| [`tracking_type`](#tracking_type) | closed-SV | 5 | `internet_tracking_summary.tracking_type` |
| [`transaction_type`](#transaction_type) | closed-SV | 5 | `transaction_management.transaction_type` |
| [`units_furnished`](#units_furnished) | closed-SV | 3 | `property.units_furnished` |
| [`unit_type_type`](#unit_type_type) | closed-SV | 10 | `property.unit_type_type`, `property_unit_types.unit_type_type` |
| [`utilities`](#utilities) | closed-MV | 23 | `property.utilities` |
| [`vegetation`](#vegetation) | closed-MV | 10 | `property.vegetation` |
| [`view`](#view) | closed-MV | 38 | `property.view` |
| [`waterfront_features`](#waterfront_features) | closed-MV | 20 | `property.waterfront_features` |
| [`water_source`](#water_source) | closed-MV | 9 | `property.water_source` |
| [`window_features`](#window_features) | closed-MV | 21 | `property.window_features` |
| [`year_built_source`](#year_built_source) | closed-SV | 8 | `property.year_built_source` |

---

## accessibility_features

- Source name: `AccessibilityFeatures`
- Kind: **closed-MV**
- Value count: 35
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AccessibilityFeatures/)
- Used by:
  - `property.accessibility_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accessible Approach with Ramp | AccessibleApproachWithRamp | A minimum of one entrance to the structure with a clear, evenly paved walkway from a parking or pedestrian arrival area. |
| Accessible Bedroom | AccessibleBedroom | Bedroom has adequate turnaround of 60" or other approved turnaround configuration. |
| Accessible Central Living Area | AccessibleCentralLivingArea | Hard surface flooring or low-pile carpet, securely attached along edges. |
| Accessible Closets | AccessibleClosets | Closet doors are 32” clearance throughout the central living area. |
| Accessible Common Area | AccessibleCommonArea | Common area, used for entertaining guests, level, with 36" passage through and around the space. |
| Accessible Doors | AccessibleDoors | Minimum 32" clear passage; levered handle; threshold, if present, maximum 1/2" but beveled on both sides when over 1/4". |
| Accessible Electrical and Environmental Controls | AccessibleElectricalAndEnvironmentalControls | Thermostats and security system controls located on floor with central living area. |
| Accessible Elevator Installed | AccessibleElevatorInstalled | Elevator with minimum 32" door and minimum 36" x 48" turning radius. |
| Accessible Entrance | AccessibleEntrance | Entrance door is a minimum of 32" wide; threshold, when present, maximum 1/2" but when over 1/4" is beveled on both sides. |
| Accessible Full Bath | AccessibleFullBath | Bathroom has adequate turnaround: 60" or other approved turnaround configuration. |
| Accessible Hallway(s) | AccessibleHallways | Hallway is a minimum of 36", preferred 42", wide (or adequate alternative based on individual configuration). |
| Accessible Kitchen | AccessibleKitchen | 40" clear turn-around, or 36" clear with clear under-counter space for T-turn space in kitchen, unimpeded by fixtures. |
| Accessible Kitchen Appliances | AccessibleKitchenAppliances | Stove controls in front or side, at countertop height; oven with side-access door at counter level; microwave is at counter level. |
| Accessible Stairway | AccessibleStairway | Handrails on both sides of stairs, extended when possible, with shear force of 250 pounds. |
| Accessible Washer/Dryer | AccessibleWasherDryer | Raised clothes washer and/or dryer, front controls, side opening, both open to center. |
| Accessible for Hearing-Impairment | AccessibleForHearingImpairment | Home is wired for flashing lights and/or vibrating smoke alarm, door bell or other alerting features. |
| Adaptable Bathroom Walls | AdaptableBathroomWalls | Reinforced main bathroom walls, including bath or shower, to permit installation of grab bars (with shear force of 250 pounds) and/or fixtures in the future. |
| Adaptable For Elevator | AdaptableForElevator | Stacked closets in a multistory house for possible future conversion to an elevator. |
| Ceiling Track | CeilingTrack | Track installed in ceiling for lift chair (Hoyer lift). |
| Central Living Area | CentralLivingArea | Includes common area; hallway(s); full or three-quarters bathroom; kitchen; at least one bedroom; access to environmental controls; and access to floors above main floor, if necessary. |
| Common Area | CommonArea | The portion of the home near accessible entrance, used for entertaining guests. |
| Customized Wheelchair Accessible | CustomizedWheelchairAccessible | Customized accessibility for specific size or style of wheelchair or scooter. |
| Electronic Environmental Controls | ElectronicEnvironmentalControls | Programmable electronic controls for thermostat, lights, security system and automatic doors. |
| Enhanced Accessible | EnhancedAccessible | The central living area is fully accessible for lifelong living by all residents, no matter their ability. |
| Exterior Wheelchair Lift | ExteriorWheelchairLift | A mechanical wheelchair lift is installed outside the home to facilitate barrier-free approach. |
| Grip-Accessible Features | GripAccessibleFeatures | All doors, faucets and other mechanisms throughout the central living area are lever, hands-free or another style that can be controlled with a closed hand, clenched fist or weak hands. |
| Reinforced Floors | ReinforcedFloors | Reinforced floors for bariatric needs, power wheelchairs, therapeutic tub or heavy medical equipment. |
| Safe Emergency Egress from Home | SafeEmergencyEgressFromHome | A minimum of two, no-step, accessible egresses from central living area. |
| Smart Technology | SmartTechnology | Smart Home (computer-controlled) and/or smart products (e.g., voice-activated controls, voice reminder, remote monitoring of individuals with dementia). |
| Stair Lift | StairLift | A professionally installed motorized rail to climb an interior or exterior stairway. |
| Standby Generator | StandbyGenerator | Backup generator for refrigeration of medications, life-sustaining medical equipment or essential room temperature control. |
| Therapeutic Whirlpool | TherapeuticWhirlpool | Therapeutic whirlpool, properly installed. |
| Visitable | Visitable | A person in a wheelchair can easily enter the home and access the main common area. |
| Visitor Bathroom | VisitorBathroom | The bathroom that is closest to the common area, minimum half bath. |
| Walker-Accessible Stairs | WalkerAccessibleStairs | Treads are minimum 25" deep, with maximum 4" rise and minimum 36" wide. |

## actor_type

- Source name: `ActorType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ActorType/)
- Used by:
  - `internet_tracking.actor_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The event was generated by what the source defines as a real estate professional. |
| Bot | Bot | The event was generated by a bot or some type of scripting tool |
| Client | Client | The event was generated by what the source defines as a registered client |
| Consumer | Consumer | The event was generated by what the source defines as a consumer |
| Unknown | Unknown | The generating Actor type could not be identified |

## aor

- Source name: `AOR`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AOR/)
- Used by:
  - `lock_or_box.showing_agent_aor` (type=`String List, Single`)
  - `member.member_aor` (type=`String List, Single`)
  - `ouid.organization_aor` (type=`String List, Single`)
  - `office.office_aor` (type=`String List, Single`)
  - `property.buyer_agent_aor` (type=`String List, Single`)
  - `property.buyer_office_aor` (type=`String List, Single`)
  - `property.co_buyer_agent_aor` (type=`String List, Single`)
  - `property.co_buyer_office_aor` (type=`String List, Single`)
  - `property.co_list_agent_aor` (type=`String List, Single`)
  - `property.co_list_office_aor` (type=`String List, Single`)
  - `property.list_aor` (type=`String List, Single`)
  - `property.list_agent_aor` (type=`String List, Single`)
  - `property.list_office_aor` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## appliances

- Source name: `Appliances`
- Kind: **closed-MV**
- Value count: 75
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Appliances/)
- Used by:
  - `property.appliances` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bar Fridge | BarFridge | A refrigerator that is sized and/or built to be part of a bar. |
| Built-In Electric Oven | BuiltInElectricOven | A built-in electric oven. |
| Built-In Electric Range | BuiltInElectricRange | A built-in electric range. |
| Built-In Freezer | BuiltInFreezer | A built-in freezer. |
| Built-In Gas Oven | BuiltInGasOven | A built-in gas oven |
| Built-In Gas Range | BuiltInGasRange | A built-in gas range. |
| Built-In Range | BuiltInRange | A built-in range where the fuel type is not specified. |
| Built-In Refrigerator | BuiltInRefrigerator | A built-in refrigerator |
| Convection Oven | ConvectionOven | An oven that has fans to circulate air around food. |
| Cooktop | Cooktop | A kitchen stove or cooker; a kitchen appliance designed for the purpose of cooking food. |
| Dishwasher | Dishwasher | A dishwasher is a mechanical device for cleaning dishware and cutlery. |
| Disposal | Disposal | A garbage disposal unit (also known as a garbage disposal, waste disposal unit, garbage disposer or garburator (in Canada)) is a device, usually electrically powered, installed under a kitchen sink between the sink's drain and the trap. |
| Double Oven | DoubleOven | A built-in oven fixture that has either two ovens, or one oven and one microwave oven. |
| Down Draft | DownDraft | A vent that is part of the surface of a cooktop that has a fan which sucks cooking fumes/smoke down. |
| Dryer | Dryer | A clothes dryer. |
| ENERGY STAR Qualified Appliances | EnergyStarQualifiedAppliances | The property includes qualified ENERGY STAR appliances. |
| ENERGY STAR Qualified Dishwasher | EnergyStarQualifiedDishwasher | The property includes a qualified ENERGY STAR dishwasher. |
| ENERGY STAR Qualified Dryer | EnergyStarQualifiedDryer | The property includes a qualified ENERGY STAR clothes dryer. |
| ENERGY STAR Qualified Freezer | EnergyStarQualifiedFreezer | The property includes a qualified ENERGY STAR freezer. |
| ENERGY STAR Qualified Refrigerator | EnergyStarQualifiedRefrigerator | The property includes a qualified ENERGY STAR refrigerator. |
| ENERGY STAR Qualified Washer | EnergyStarQualifiedWasher | The property includes a qualified ENERGY STAR clothes washer. |
| ENERGY STAR Qualified Water Heater | EnergyStarQualifiedWaterHeater | The property includes a qualified ENERGY STAR water heater. |
| Electric Cooktop | ElectricCooktop | A cooktop or stove that produces heat by way of electricity rather than gas. |
| Electric Oven | ElectricOven | An oven that is heated by electricity, typically by way of heating coils. |
| Electric Range | ElectricRange | An oven and cooktop that generates heat by way of electricity. |
| Electric Water Heater | ElectricWaterHeater | A water heater that heats the water by way of electricity. |
| Exhaust Fan | ExhaustFan | The cooktop has an exhaust fan. |
| Free-Standing Electric Oven | FreeStandingElectricOven | The oven is freestanding, not built-in, and uses electricity to produce heat. |
| Free-Standing Electric Range | FreeStandingElectricRange | The range is freestanding, not built-in, and uses electricity to produce heat for its oven and cooktop. |
| Free-Standing Freezer | FreeStandingFreezer | The freezer is freestanding and not built-in. |
| Free-Standing Gas Oven | FreeStandingGasOven | The oven is freestanding, not built-in, and uses gas to produce heat. |
| Free-Standing Gas Range | FreeStandingGasRange | The range is freestanding, not built-in, and uses gas to produce heat for its oven and cooktop. |
| Free-Standing Range | FreeStandingRange | The range is freestanding, not built-in. |
| Free-Standing Refrigerator | FreeStandingRefrigerator | The refrigerator is freestanding, not built-in. |
| Freezer | Freezer | The property includes a freezer. |
| Gas Cooktop | GasCooktop | A cooktop or stove that produces heat by way of gas rather than electricity. |
| Gas Oven | GasOven | An oven that is heated by gas. |
| Gas Range | GasRange | An oven and cooktop that generates heat by way of gas. |
| Gas Water Heater | GasWaterHeater | A water heater that heats the water with gas. |
| Heat Pump Water Heater | HeatPumpWaterHeater | A water heater that uses electricity to move heat from one place to another instead of generating heat directly. |
| Humidifier | Humidifier | The property includes a humidity-control device or system. |
| Ice Maker | IceMaker | The property includes an ice maker. |
| Indoor Grill | IndoorGrill | The property has an indoor grill. |
| Induction Cooktop | InductionCooktop | The electric cooktop is based on magnetic induction rather than heating coils. |
| Instant Hot Water | InstantHotWater | The property has a circulatory or instant hot water system. |
| Microwave | Microwave | The property includes a microwave. |
| None | None | The property includes no appliances. |
| Other | Other | The property includes appliances other than those available on this list. |
| Oven | Oven | The property includes an oven. |
| Plumbed For Ice Maker | PlumbedForIceMaker | The property has plumbing for an ice maker. |
| Portable Dishwasher | PortableDishwasher | The property includes a portable dishwasher. |
| Propane Cooktop | PropaneCooktop | The gas cooktop uses propane as its fuel and either has a local tank or runs on a housewide propane system. |
| Range | Range | The property includes a range, which is a single unit that has both an oven and a cooktop. |
| Range Hood | RangeHood | The range has a hooded exhaust. |
| Refrigerator | Refrigerator | The property includes a refrigerator. |
| Self Cleaning Oven | SelfCleaningOven | The oven included with the property has a self-cleaning feature. |
| Smart Appliance(s) | SmartAppliances | Appliances that have convenience and energy saving aspects. |
| Solar Hot Water | SolarHotWater | The hot water heater has either a passive or active solar component. |
| Stainless Steel Appliance(s) | StainlessSteelAppliances | Some or all of the appliances included in the property are stainless steel. |
| Tankless Water Heater | TanklessWaterHeater | A tankless water heater is included with the property. |
| Trash Compactor | TrashCompactor | The property has a trash compactor. |
| Vented Exhaust Fan | VentedExhaustFan | The cooktop has an exhaust fan that is vented. |
| Warming Drawer | WarmingDrawer | The property has a warming drawer. |
| Washer | Washer | The property includes a clothes washer. |
| Washer/Dryer | WasherDryer | The property includes a clothes washer and dryer. |
| Washer/Dryer Stacked | WasherDryerStacked | The property has a stacked clothes washer and dryer. |
| Water Heater | WaterHeater | The property has a water heater. |
| Water Purifier | WaterPurifier | The property has a water purifier. |
| Water Purifier Owned | WaterPurifierOwned | The property has a water purifier that is owned and not rented/leased. |
| Water Purifier Rented | WaterPurifierRented | The property has a water purifier that is on a rental or lease agreement. |
| Water Softener | WaterSoftener | The property has a water-softening system. |
| Water Softener Owned | WaterSoftenerOwned | The property has a water-softening system that is owned and not rented/leased. |
| Water Softener Rented | WaterSoftenerRented | The property has a water-softening system that is on a rental or lease agreement. |
| Wine Cooler | WineCooler | The property includes a wine cooler. |
| Wine Refrigerator | WineRefrigerator | The property includes a wine refrigerator. |

## architectural_style

- Source name: `ArchitecturalStyle`
- Kind: **closed-MV**
- Value count: 44
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ArchitecturalStyle/)
- Used by:
  - `property.architectural_style` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| A-Frame | AFrame | An architectural style that generally features four walls extending up from the foundation and a steeply pitched roof that reaches near the ground, creating an overall shape of the letter “A” or a triangle. |
| Art Deco | ArtDeco | An architectural style that generally includes decorative windows, spires or other tower-like structures and facades with vertical lines and other ornamental geometric patterns. |
| Barndominium | Barndominium | An architectural style that is typically a metal pole barn or other barn-like structure with a living area that encompasses a portion of or the entire building. |
| Berm | Berm | An architectural style built partially or entirely below grade, with earthen material (i.e., dirt, grass) covering at least one or more walls. |
| Bungalow | Bungalow | An architectural style (also known as cottage) that is generally small with a single story or partial second story that has an overhanging, sloped roof and covered porch. |
| Cabin | Cabin | An architectural style that is generally small in size with a simple floor plan and built with mostly natural materials. |
| Cape Cod | CapeCod | An architectural style that is generally framed rectangularly, includes one and a half or two stories of height, has a centered front door, and is built with a moderately steeply-pitched, gabled roof. |
| Colonial | Colonial | An architectural style that is generally framed rectangularly, includes two or three stories in height, and is built with a brick, stone or wood facade and steeply-pitched, gabled roof. |
| Contemporary | Contemporary | An architectural style that generally includes large windows, natural construction elements, geometric shapes and minimalistic elements. |
| Craftsman | Craftsman | An architectural style (also known as arts and crafts) that generally is one or one and a half stories in height, has wood siding or shaker shingles, includes covered porches with exposed beams or columns, and is built with low-pitched, gabled roofs. |
| Creole | Creole | A prominent architectural style in the Southern United States, particularly the state of Louisiana, that is generally one to one and a half stories in height and includes full front porches and high, gabled roofs with a ridge parallel to the road it fronts. |
| Dome | Dome | An architectural style (also known as geodesic) that generally takes the shape of a sphere or spherical ellipsoid and has a shell-type framework. |
| Dutch Colonial | DutchColonial | An architectural style that generally has steep, broken-pitched, gambrel roofs that contain at least one dormer window. |
| Farmhouse | Farmhouse | An architectural style that is generally one and a half or two stories in height, asymmetrical in design, and built with central chimneys and large porches that sometimes cover multiple sides of the home. |
| Federal | Federal | An architectural style that is generally square or rectangular, emphasizing balance and symmetry, and has a brick exterior, typically without a porch. |
| French Provincial | FrenchProvincial | An architectural style that is generally multi-story with a brick or stucco exterior, slate roof and tall, slender windows. |
| Georgian | Georgian | An architectural style that is generally symmetrical with two or three stories in height and a brick or stone exterior with regularly spaced windows. |
| Gothic Revival | GothicRevival | An architectural style that generally emphasizes decorative elements, arch designs in windows and doorways, and steeply pitched, pointed and gabled roofs. |
| Greek Revival | GreekRevival | An architectural style that generally includes a plaster or stucco exterior with tall columns and framed, dormer windows. |
| Italianate | Italianate | An architectural style that is generally two to four stories in height with gently sloping, hipped roofs and tall, narrow or arched windows. |
| Mediterranean | Mediterranean | An architectural style that generally features a blend of Spanish Revival and Italian Renaissance architecture with stucco exterior, red clay or tile roofs, decorative archways, wrought ironwork in balconies and window grilles, and an incorporation of outdoor living spaces. |
| Mid-Century Modern | MidCenturyModern | An architectural style that is generally asymmetrical and split-level or one story in height with large or floor-to-ceiling windows. |
| Modern | Modern | An architectural style similar to mid-century modern that emphasizes function over form, straight lines and geometric shapes while keeping purely decorative aspects to a minimum. |
| Monterey | Monterey | An architectural style that is generally two stories in height with large porches, full-length balconies, hipped roofs and tall, double-hung windows. |
| National | National | An architectural style that is generally utilitarian, rectangular in shape and built with gabled or pyramidal roofs. |
| Neoclassical | Neoclassical | An architectural style that generally emphasizes symmetry and often features large columns, decorative doorways and evenly spaced, divided pane windows. |
| Other | Other | The architectural style is something other than the options provided. |
| Prairie | Prairie | An architectural style that is generally asymmetrical and emphasizes horizontal lines, handmade woodwork, metalwork and art glass. |
| Pueblo | Pueblo | An architectural style (also known as Southwestern or adobe) that is generally constructed of adobe, which may be covered by stucco, with an emphasis on natural, earth-tone materials. |
| Queen Anne | QueenAnne | An architectural style that is generally asymmetrical with round or polygonal towers or turrets, large wrap-around porches, and steeply pitched, gabled, slate roofs. |
| Raised Ranch | RaisedRanch | An architectural style (also known as bi-level or split foyer) with designed living space below grade that generally have two full levels of living space with a short set of stairs leading up and down from inside the entrance to the home. |
| Ranch | Ranch | An architectural style that is generally one story in height, low to the ground and built with low-pitched roofs and attached, front-facing garages. |
| Regency | Regency | An architectural style similar to Georgian that is generally two or three stories in height and symmetrical with a painted stucco façade and built with large columns supporting a covered entryway. |
| Rustic | Rustic | An architectural style that is generally built mostly with wood, stone and other natural materials that create a naturally aged and rough look. |
| Saltbox | Saltbox | An architectural style originating in New England that is generally two stories in height in the front and one in the rear with a gable roof. |
| See Remarks | SeeRemarks | See remarks for information about the architectural style of the home. |
| Shingle | Shingle | An architectural style that is generally asymmetrical with shingle-covered exteriors, wide porches and steeply pitched roofs. |
| Shotgun | Shotgun | An architectural style that is generally one story in height, rectangular, long and narrow with gabled roofs. |
| Spanish | Spanish | An architectural style that is most common in the Southwestern United States and generally has a stucco exterior with liberal use of wood and tile. |
| Split Level | SplitLevel | An architectural style (also known as tri level or quad level) that is generally asymmetrical and has facades with minimal decorative elements. |
| Stick | Stick | An architectural style related to Victorian that is generally asymmetrical with two to three stories of height and a highly decorative shingle or clapboard exterior that may include towers and an emphasis on geometric patterns. |
| Traditional | Traditional | An architectural style that uses several different exterior materials, has simple triangular rooflines, includes regularly spaced and sized windows, and is complemented by large, covered porches. |
| Tudor | Tudor | An architectural style that is generally asymmetrical that has a brick or stone exterior with wood accents and is characterized by steeply pitched, gabled roofs, casement windows and arched doorways. |
| Victorian | Victorian | An architectural style that is generally two to three stories in height with asymmetrical or complex shapes and highly decorative ornamentation such as brackets, spindles and patterned shingles. |

## area_source

- Source name: `AreaSource`
- Kind: **closed-SV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AreaSource/)
- Used by:
  - `property.above_grade_finished_area_source` (type=`String List, Single`)
  - `property.above_grade_unfinished_area_source` (type=`String List, Single`)
  - `property.below_grade_finished_area_source` (type=`String List, Single`)
  - `property.below_grade_unfinished_area_source` (type=`String List, Single`)
  - `property.building_area_source` (type=`String List, Single`)
  - `property.farm_land_area_source` (type=`String List, Single`)
  - `property.living_area_source` (type=`String List, Single`)
  - `property_rooms.room_area_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | An appraiser provided the measurement of the area. |
| Assessor | Assessor | The assessor provided the measurement of the area. |
| Builder | Builder | The builder provided the measurement of the area. |
| Estimated | Estimated | The measurement of the area is an estimate. |
| Other | Other | The measurement of the area was provided by another party not listed. |
| Owner | Owner | The owner provided the measurement of the area. |
| Plans | Plans | The measurement of the area was taken from building plans. |
| Public Records | PublicRecords | The measurement of the area was received from public records. |
| See Remarks | SeeRemarks | See remarks for information about the source of the area measurement. |

## area_units

- Source name: `AreaUnits`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AreaUnits/)
- Used by:
  - `property.above_grade_finished_area_units` (type=`String List, Single`)
  - `property.above_grade_unfinished_area_units` (type=`String List, Single`)
  - `property.below_grade_finished_area_units` (type=`String List, Single`)
  - `property.below_grade_unfinished_area_units` (type=`String List, Single`)
  - `property.building_area_units` (type=`String List, Single`)
  - `property.farm_land_area_units` (type=`String List, Single`)
  - `property.leasable_area_units` (type=`String List, Single`)
  - `property.living_area_units` (type=`String List, Single`)
  - `property_rooms.room_area_units` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Square Feet | SquareFeet | The value reported in the related Area field is in square feet. |
| Square Meters | SquareMeters | The value reported in the related Area field is in square meters. |

## association_amenities

- Source name: `AssociationAmenities`
- Kind: **closed-MV**
- Value count: 76
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AssociationAmenities/)
- Used by:
  - `property.association_amenities` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Airport/Runway | AirportRunway | The homeowner association includes access or some service related to an airport or runway. |
| Barbecue | Barbecue | The homeowner association includes use of or access to a barbecue. |
| Basketball Court | BasketballCourt | The homeowner association includes use of or access to a basketball court. |
| Beach Access | BeachAccess | The homeowner association includes access to a beach. |
| Beach Rights | BeachRights | The homeowner association includes use of a beach that has beach rights restrictions. |
| Billiard Room | BilliardRoom | The homeowner association includes use of or access to a billiard room. |
| Boat Dock | BoatDock | The homeowner association includes use of or access to a boat dock. |
| Boat Slip | BoatSlip | The homeowner association includes use of or access to a boat slip. |
| Boating | Boating | The homeowner association includes use of or access to boating. |
| Cabana | Cabana | The homeowner association includes use of or access to a cabana. |
| Cable TV | CableTv | The homeowner association includes cable-based services. |
| Car Wash Area | CarWashArea | The homeowner association includes use of or access to an area to wash your car. |
| Clubhouse | Clubhouse | The homeowner association includes use of or access to a clubhouse. |
| Coin Laundry | CoinLaundry | The homeowner association includes use of or access to a coin laundry. |
| Concierge | Concierge | The homeowner association includes use of or access to a concierge service. |
| Day Care | DayCare | The homeowner association includes use of or access to a day care service. |
| Dog Park | DogPark | The homeowner association includes use of or access to a dog park. |
| Dry Dock | DryDock | The homeowner association includes use of or access to a dry dock. |
| Electricity | Electricity | The homeowner association includes electricity. |
| Elevator(s) | Elevators | The homeowner association includes use of or access to an elevator or elevators. |
| Exercise Course | ExerciseCourse | The homeowner association includes use of or access to an exercise course. |
| Fitness Center | FitnessCenter | The homeowner association includes use of or access to a fitness center. |
| Game Court Exterior | GameCourtExterior | The homeowner association includes use of or access to an outdoors game court. |
| Game Court Interior | GameCourtInterior | The homeowner association includes use of or access to an indoors game court. |
| Game Room | GameRoom | The homeowner association includes use of or access to a game room. |
| Gas | Gas | The homeowner association includes natural gas. |
| Gated | Gated | The homeowner association property/area is gated. |
| Golf Course | GolfCourse | The homeowner association includes use of or access to a golf course. |
| Hot Water | HotWater | The homeowner association includes hot water. |
| Indoor Pool | IndoorPool | The homeowner association includes use of or access to an indoor pool. |
| Insurance | Insurance | The homeowner association includes insurance. |
| Jogging Path | JoggingPath | The homeowner association includes use of or access to a jogging path. |
| Landscaping | Landscaping | The homeowner association includes landscaping. |
| Laundry | Laundry | The homeowner association includes laundry. |
| Maid service | MaidService | The homeowner association includes use of or access to a maid service. |
| Maintenance | Maintenance | The homeowner association includes maintenance. |
| Maintenance Grounds | MaintenanceGrounds | The homeowner association includes grounds maintenance. |
| Maintenance Structure | MaintenanceStructure | The homeowner association includes building maintenance. |
| Management | Management | The homeowner association includes management services. |
| Marina | Marina | The homeowner association includes use of or access to a marina. |
| Meeting Room | MeetingRoom | The homeowner association includes use of or access to a meeting room. |
| None | None | The homeowner association has no amenities. |
| Other | Other | The homeowner association includes amenities not included on this list. |
| Park | Park | The homeowner association includes use of or access to a park. |
| Parking | Parking | The homeowner association includes use of or access to parking. |
| Party Room | PartyRoom | The homeowner association includes use of or access to a party room. |
| Picnic Area | PicnicArea | The homeowner association includes use of or access to a picnic area. |
| Playground | Playground | The homeowner association includes use of or access to a playground. |
| Pond Seasonal | PondSeasonal | The homeowner association includes seasonal use of or access to a pond. |
| Pond Year Round | PondYearRound | The homeowner association includes use of or access to a pond all year long. |
| Pool | Pool | The homeowner association includes use of or access to a pool. |
| Powered Boats Allowed | PoweredBoatsAllowed | The homeowner association allows the use of powered boats. |
| RV Parking | RvParking | The homeowner association includes use of or access to recreational vehicle (RV) parking. |
| RV/Boat Storage | RvBoatStorage | The homeowner association includes use of or access to recreational vehicle (RV) and/or boat storage. |
| Racquetball | Racquetball | The homeowner association includes use of or access to a racquetball court or courts. |
| Recreation Facilities | RecreationFacilities | The homeowner association includes use of or access to recreation facilities. |
| Recreation Room | RecreationRoom | The homeowner association includes use of or access to a recreation room. |
| Roof Deck | RoofDeck | The homeowner association includes use of or access to a roof deck. |
| Sauna | Sauna | The homeowner association includes use of or access to a sauna. |
| Security | Security | The homeowner association includes security services. |
| Service Elevator(s) | ServiceElevators | The homeowner association includes use of or access to a service elevator or elevators. |
| Shuffleboard Court | ShuffleboardCourt | The homeowner association includes use of or access to a shuffleboard court. |
| Ski Accessible | SkiAccessible | The homeowner association includes access to skiing. |
| Snow Removal | SnowRemoval | The homeowner association includes snow removal. |
| Spa/Hot Tub | SpaHotTub | The homeowner association includes use of or access to a spa and/or hot tub. |
| Sport Court | SportCourt | The homeowner association includes use of or access to a sport court. |
| Stable(s) | Stables | The homeowner association includes use of or access to a horse stable. |
| Storage | Storage | The homeowner association includes storage space. |
| Stream Seasonal | StreamSeasonal | The homeowner association includes seasonal use of or access to a stream. |
| Stream Year Round | StreamYearRound | The homeowner association includes use of or access to a stream all year long. |
| Taxes | Taxes | The homeowner association includes taxes. |
| Tennis Court(s) | TennisCourts | The homeowner association includes use of or access to a tennis court. |
| Trail(s) | Trails | The homeowner association includes use of or access to a trail. |
| Trash | Trash | The homeowner association includes trash service. |
| Water | Water | The homeowner association includes water. |
| Workshop Area | WorkshopArea | The homeowner association includes use of or access to a workshop area. |

## association_fee_includes

- Source name: `AssociationFeeIncludes`
- Kind: **closed-MV**
- Value count: 15
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AssociationFeeIncludes/)
- Used by:
  - `property.association_fee_includes` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Cable TV | CableTv | Cable TV is included in the fee paid to the homeowner association. |
| Earthquake Insurance | EarthquakeInsurance | Earthquake insurance is included in the fee paid to the homeowner association. |
| Electricity | Electricity | Electricity is included in the fee paid to the homeowner association. |
| Gas | Gas | Gas is included in the fee paid to the homeowner association. |
| Insurance | Insurance | Insurance is included in the fee paid to the homeowner association. |
| Internet | Internet | Internet access is included with the homeowner association dues paid by the owner. |
| Maintenance Grounds | MaintenanceGrounds | Maintenance of the grounds includes lawns and common areas but not exterior structures. |
| Maintenance Structure | MaintenanceStructure | Maintenance of the exterior of the structure includes roofing, walls, exterior structures but does not include the grounds. |
| Pest Control | PestControl | Pest control is included in the fee paid to the association. |
| Security | Security | Security is included in the fee paid to the association. |
| Sewer | Sewer | Sewer is included in the fee paid to the association. |
| Snow Removal | SnowRemoval | Snow removal is included in the fee paid to the association. |
| Trash | Trash | Trash is included in the fee paid to the association. |
| Utilities | Utilities | Utilities are included in the fee paid to the association. |
| Water | Water | Water is included in the fee paid to the association. |

## association_status

- Source name: `AssociationStatus`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AssociationStatus/)
- Used by:
  - `association.association_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The association record is active. |
| Inactive | Inactive | The association record is inactive. |

## association_type

- Source name: `AssociationType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/AssociationType/)
- Used by:
  - `association.association_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Local | Local | The association is a local association of REALTORS®. |
| MLS | Mls | The association is also an MLS. |
| Not Applicable | NotApplicable | The type of association is not relative to the record. |

## attended

- Source name: `Attended`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Attended/)
- Used by:
  - `open_house.open_house_attended_by` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | A licensed real estate agent will be present at the open house event. |
| Seller | Seller | A licensed real estate agent will not be present and the property owner will be present at the open house event. |
| Unattended | Unattended | The open house event will not be attended. |

## basement

- Source name: `Basement`
- Kind: **closed-MV**
- Value count: 24
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Basement/)
- Used by:
  - `property.basement` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Apartment | Apartment | The basement is set up as an apartment living space. |
| Bath/Stubbed | BathStubbed | The basement is stubbed for a bathroom. |
| Block | Block | The basement has block construction. |
| Concrete | Concrete | The basement has a concrete floor and/or walls. |
| Crawl Space | CrawlSpace | The basement is/has a crawl space. |
| Daylight | Daylight | The basement has natural lighting. |
| Dirt Floor | DirtFloor | The basement has a dirt floor. |
| Exterior Entry | ExteriorEntry | The basement has an exterior entry. |
| Finished | Finished | The basement is finished to a given standard of completion (e.g., underlayment and flooring; walls framed, insulated, drywalled and painted). |
| French Drain | FrenchDrain | The basement has a French drain. |
| Full | Full | The basement fills the entire space under the house. |
| Full Exposure | FullExposure | The basement of the home has a full-wall, standard-sized windows and a door to the outside at or above ground level. |
| Interior Entry | InteriorEntry | The basement has an interior entry. |
| No Exposure | NoExposure | The basement of the home is below ground without full-sized windows or a door to the outside. |
| None | None | The property has no basement. |
| Other | Other | The basement has features or attributes other than those listed in this field. |
| Partial | Partial | The basement partially fills the space under the house. |
| Partial Exposure | PartialExposure | The basement of the home is roughly halfway below ground level and has at least one full-sized window but without a door to the outside. |
| Partially Finished | PartiallyFinished | The basement is partially finished. |
| Storage Space | StorageSpace | The basement has storage space. |
| Sump Pump | SumpPump | The basement has a sump pump. |
| Unfinished | Unfinished | The basement is unfinished. |
| Walk-Out Access | WalkOutAccess | A structure where the basement space is directly accessible from the outside with the entryway level with the ground. |
| Walk-Up Access | WalkUpAccess | A structure where the basement space is directly accessible from the outside with the entryway below ground and usually exterior stairs leading up to the ground level. |

## billing_preference

- Source name: `BillingPreference`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BillingPreference/)
- Used by:
  - `member.member_billing_preference` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Email | Email | Send billing to the member's email address. |
| Fax | Fax | Send billing to the member via fax. |
| Mail | Mail | Send billing to the member via postal mail. |

## body_type

- Source name: `BodyType`
- Kind: **closed-MV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BodyType/)
- Used by:
  - `property.body_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Double Wide | DoubleWide | The body/structure type of the mobile/manufactured home is a double-wide. |
| Expando | Expando | The body/structure type of the mobile/manufactured home is an expando. |
| Other | Other | A body type is not included on this list. |
| Quad Wide | QuadWide | The body/structure type of the mobile/manufactured home is a quad. |
| See Remarks | SeeRemarks | The body/structure type of the mobile/manufactured home is described by additional remarks. |
| Single Wide | SingleWide | The body/structure type of the mobile/manufactured home is a single-wide. |
| Triple Wide | TripleWide | The body/structure type of the mobile/manufactured home is a triple-wide. |

## building_features

- Source name: `BuildingFeatures`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BuildingFeatures/)
- Used by:
  - `property.building_features` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## business_type

- Source name: `BusinessType`
- Kind: **closed-MV**
- Value count: 109
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BusinessType/)
- Used by:
  - `property.business_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accounting | Accounting | The listing is for an accounting business. |
| Administrative and Support | AdministrativeAndSupport | The listing is for an administrative and support business. |
| Advertising | Advertising | The listing is for an advertising business. |
| Agriculture | Agriculture | The listing is for an agriculture business. |
| Animal Grooming | AnimalGrooming | The listing is for an animal grooming business. |
| Appliances | Appliances | The listing is for an appliances business. |
| Aquarium Supplies | AquariumSupplies | The listing is for an aquarium supplies business. |
| Arts and Entertainment | ArtsAndEntertainment | The listing is for an arts and entertainment business. |
| Athletic | Athletic | The listing is for an athletic business. |
| Auto Body | AutoBody | The listing is for an auto body business. |
| Auto Dealer | AutoDealer | The listing is for an auto dealer business. |
| Auto Glass | AutoGlass | The listing is for an auto glass business. |
| Auto Parts | AutoParts | The listing is for an auto parts business. |
| Auto Rent/Lease | AutoRentLease | The listing is for an auto rent/lease business. |
| Auto Repair-Specialty | AutoRepairSpecialty | The listing is for an auto repair specialty business. |
| Auto Service | AutoService | The listing is for an auto service business. |
| Auto Stereo/Alarm | AutoStereoAlarm | The listing is for an auto stereo/alarm business. |
| Auto Tires | AutoTires | The listing is for an auto tires business. |
| Auto Wrecking | AutoWrecking | The listing is for an auto wrecking business. |
| Bakery | Bakery | The listing is for a bakery business. |
| Bar/Tavern/Lounge | BarTavernLounge | The listing is for a bar/tavern/lounge business. |
| Barber/Beauty | BarberBeauty | The listing is for a barber/beauty business. |
| Bed & Breakfast | BedAndBreakfast | The listing is for a bed & breakfast business. |
| Books/Cards/Stationary | BooksCardsStationary | The listing is for a books/cards/stationery business. |
| Butcher | Butcher | The listing is for a butcher business. |
| Cabinets | Cabinets | The listing is for a cabinets business. |
| Candy/Cookie | CandyCookie | The listing is for a candy/cookie business. |
| Car Wash | CarWash | The listing is for a car wash business. |
| Carpet/Tile | CarpetTile | The listing is for a carpet/tile business. |
| Child Care | ChildCare | The listing is for a child care business. |
| Church | Church | The listing is for a church business. |
| Clothing | Clothing | The listing is for a clothing business. |
| Commercial | Commercial | The listing is for a commercial business. |
| Computer | Computer | The listing is for a computer business. |
| Construction/Contractor | ConstructionContractor | The listing is for a construction/contractor business. |
| Convalescent | Convalescent | The listing is for a convalescent business. |
| Convenience Store | ConvenienceStore | The listing is for a convenience store business. |
| Dance Studio | DanceStudio | The listing is for a dance studio business. |
| Decorator | Decorator | The listing is for a decorator business. |
| Deli/Catering | DeliCatering | The listing is for a deli/catering business. |
| Dental | Dental | The listing is for a dental business. |
| Distribution | Distribution | The listing is for a distribution business. |
| Doughnut | Doughnut | The listing is for a doughnut business. |
| Drugstore | Drugstore | The listing is for a drugstore business. |
| Dry Cleaner | DryCleaner | The listing is for a dry cleaner business. |
| Education/School | EducationSchool | The listing is for an education/school business. |
| Electronics | Electronics | The listing is for an electronics business. |
| Employment | Employment | The listing is for an employment business. |
| Farm | Farm | The listing is for a farm business. |
| Fast Food | FastFood | The listing is for a fast food business. |
| Financial | Financial | The listing is for a financial business. |
| Fitness | Fitness | The listing is for a fitness business. |
| Florist/Nursery | FloristNursery | The listing is for a florist/nursery business. |
| Food & Beverage | FoodAndBeverage | The listing is for a food & beverage business. |
| Forest Reserve | ForestReserve | The listing is for a forest reserve business. |
| Franchise | Franchise | The listing is for a franchise business. |
| Furniture | Furniture | The listing is for a furniture business. |
| Gas Station | GasStation | The listing is for a gas station business. |
| Gift Shop | GiftShop | The listing is for a gift shop business. |
| Grocery | Grocery | The listing is for a grocery business. |
| Hardware | Hardware | The listing is for a hardware business. |
| Health Food | HealthFood | The listing is for a health food business. |
| Health Services | HealthServices | The listing is for a health services business. |
| Hobby | Hobby | The listing is for a hobby business. |
| Home Cleaner | HomeCleaner | The listing is for a home cleaner business. |
| Hospitality | Hospitality | The listing is for a hospitality business. |
| Hotel/Motel | HotelMotel | The listing is for a hotel/motel business. |
| Ice Cream/Frozen Yogurt | IceCreamFrozenYogurt | The listing is for an ice cream/frozen yogurt business. |
| Industrial | Industrial | The listing is for an industrial business. |
| Jewelry | Jewelry | The listing is for a jewelry business. |
| Landscaping | Landscaping | The listing is for a landscaping business. |
| Laundromat | Laundromat | The listing is for a laundromat business. |
| Liquor Store | LiquorStore | The listing is for a liquor store business. |
| Locksmith | Locksmith | The listing is for a locksmith business. |
| Manufacturing | Manufacturing | The listing is for a manufacturing business. |
| Medical | Medical | The listing is for a medical business. |
| Mixed | Mixed | The listing is for a mixed business. |
| Mobile/Trailer Park | MobileTrailerPark | The listing is for a mobile/trailer park business. |
| Music | Music | The listing is for a music business. |
| Nursing Home | NursingHome | The listing is for a nursing home business. |
| Office Supply | OfficeSupply | The listing is for an office supply business. |
| Other | Other | The listing is for a business not readily categorized into another business type. |
| Paints | Paints | The listing is for a paint business. |
| Parking | Parking | The listing is for a parking business. |
| Pet Store | PetStore | The listing is for a pet store business. |
| Photographer | Photographer | The listing is for a photography business. |
| Pizza | Pizza | The listing is for a pizza business. |
| Printing | Printing | The listing is for a printing business. |
| Professional Service | ProfessionalService | The listing is for a professional service business. |
| Professional/Office | ProfessionalOffice | The listing is for a professional/office business. |
| Real Estate | RealEstate | The listing is for a real estate business. |
| Recreation | Recreation | The listing is for a recreation business. |
| Rental | Rental | The listing is for a rental business. |
| Residential | Residential | The listing is for a residential business. |
| Restaurant | Restaurant | The listing is for a restaurant business. |
| Retail | Retail | The listing is for a retail business. |
| Saddlery/Harness | SaddleryHarness | The listing is for a saddlery/harness business. |
| Sporting Goods | SportingGoods | The listing is for a sporting goods business. |
| Storage | Storage | The listing is for a storage business. |
| Toys | Toys | The listing is for a toy business. |
| Transportation | Transportation | The listing is for a transportation business. |
| Travel | Travel | The listing is for a travel business. |
| Upholstery | Upholstery | The listing is for an upholstery business. |
| Utility | Utility | The listing is for a utility business. |
| Variety | Variety | The listing is for a variety business. |
| Video | Video | The listing is for a video business. |
| Wallpaper | Wallpaper | The listing is for a wallpaper business. |
| Warehouse | Warehouse | The listing is for a warehouse business. |
| Wholesale | Wholesale | The listing is for a wholesale business. |

## buyer_agent_designation

- Source name: `BuyerAgentDesignation`
- Kind: **closed-MV**
- Value count: 27
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BuyerAgentDesignation/)
- Used by:
  - `property.buyer_agent_designation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accredited Buyer's Representative / ABR | AccreditedBuyersRepresentative | The Accredited Buyer's Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| Accredited Land Consultant / ALC | AccreditedLandConsultant | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| At Home With Diversity / AHWD | AtHomeWithDiversity | Learn to work effectively with and within today's diverse real estate market. |
| Certified Commercial Investment Member / CCIM | CertifiedCommercialInvestmentMember | The Certified Commercial Investment Member (CCIM) designation is commercial real estate's global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| Certified Distressed Property Expert / CDPE | CertifiedDistressedPropertyExpert | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today's turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| Certified International Property Specialist / CIPS | CertifiedInternationalPropertySpecialist | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| Certified Property Manager / CPM | CertifiedPropertyManager | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| Certified Real Estate Brokerage Manager / CRB | CertifiedRealEstateBrokerageManager | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| Certified Real Estate Team Specialist / C-RETS | CertifiedRealEstateTeamSpecialist | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| Certified Residential Specialist / CRS | CertifiedResidentialSpecialist | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| Counselor of Real Estate / CRE | CounselorOfRealEstate | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| General Accredited Appraiser / GAA | GeneralAccreditedAppraiser | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Graduate, REALTOR Institute / GRI | GraduateRealtorInstitute | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| Military Relocation Professional / MRP | MilitaryRelocationProfessional | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| NAR's Green Designation / GREEN | NARsGreenDesignation | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| Performance Management Network / PMN | PerformanceManagementNetwork | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| Pricing Strategy Advisor / PSA | PricingStrategyAdvisor | Enhance your skills in pricing properties, creating CMAs (comparative market analysis), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| REALTOR Association Certified Executive / RCE | RealtorAssociationCertifiedExecutive | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| Real Estate Negotiation Expert / RENE | RealEstateNegotiationExpert | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| Residential Accredited Appraiser / RAA | ResidentialAccreditedAppraiser | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Resort & Second-Home Property Specialist / RSPS | ResortAndSecondHomePropertySpecialist | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| Seller Representative Specialist / SRS | SellerRepresentativeSpecialist | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| Seniors Real Estate Specialist / SRES | SeniorsRealEstateSpecialist | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| Short Sales & Foreclosure Resource / SFR | ShortSalesAndForeclosureResource | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| Society of Industrial and Office REALTORS / SIOR | SocietyOfIndustrialAndOfficeRealtors | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| Transnational Referral Certification / TRC | TransnationalReferralCertification | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |
| e-PRO | ePRO | NAR's e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |

## buyer_financing

- Source name: `BuyerFinancing`
- Kind: **closed-MV**
- Value count: 13
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/BuyerFinancing/)
- Used by:
  - `property.buyer_financing` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Assumed | Assumed | The buyer assumed a current form of financing. |
| Cash | Cash | The buyer paid cash for the property. |
| Contract | Contract | The purchase of a property involves an agreement to perform services, provide product, share income or some other determined method of payment for the property. |
| Conventional | Conventional | The buyer is using conventional financing to purchase the home. |
| FHA | Fha | A loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| FHA 203(b) | Fha203b | The basic home mortgage loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| FHA 203(k) | Fha203k | A loan for the rehabilitation and repair of a single-family residence from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| Other | Other | The buyer is using another form of financing that is not included among the options provided on this list. |
| Private | Private | Financing is provided by a private party. |
| Seller Financing | SellerFinancing | The seller is providing financing to the buyer. |
| Trust Deed | TrustDeed | Financing where title of the property is placed with a trustee who secures payment of the loan for a beneficiary. |
| USDA | Usda | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| VA | Va | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

## caravan_allowed_class_names

- Source name: `CaravanAllowedClassNames`
- Kind: **closed-MV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanAllowedClassNames/)
- Used by:
  - `caravan.caravan_allowed_class_names` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Business Opportunity | BusinessOpportunity | The class, sometimes known as property type, is a business for sale. |
| Commercial Lease | CommercialLease | The class, sometimes known as property type, is a commercial property for lease. |
| Commercial Sale | CommercialSale | The class, sometimes known as property type, is a commercial property for sale. |
| Farm | Farm | The class, sometimes known as property type, is a farm. |
| Land | Land | The class, sometimes known as property type, is land for sale or lease. |
| Manufactured In Park | ManufacturedInPark | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| Residential | Residential | The class, sometimes known as property type, is residential property for sale. |
| Residential Income | ResidentialIncome | The class, sometimes known as property type, is income or multifamily property for sale. |
| Residential Lease | ResidentialLease | The class, sometimes known as property type, is residential property for lease. |

## caravan_allowed_statuses

- Source name: `CaravanAllowedStatuses`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanAllowedStatuses/)
- Used by:
  - `caravan.caravan_allowed_statuses` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The listing is on market, and an offer has not been accepted. |
| Active Under Contract | ActiveUnderContract | An offer has been accepted, but the listing is still on market. |
| Pending | Pending | An offer has been accepted, and the listing is no longer on market. |

## caravan_resource_name

- Source name: `CaravanResourceName`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanResourceName/)
- Used by:
  - `caravan.caravan_organizer_resource_name` (type=`String List, Single`)
  - `caravan_stop.stop_resource_name` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Association | Association | This record is related to another record in the Association resource. |
| Caravan | Caravan | This record is related to another record in the Caravan resource. |
| Contacts | Contacts | This record is related to another record in the Contacts resource. |
| Member | Member | This record is related to another record in the Member resource. |
| Office | Office | This record is related to another record in the Office resource. |
| OpenHouse | OpenHouse | This record is related to another record in the OpenHouse resource. |
| Property | Property | This record is related to another record in the Property resource. |

## caravan_status

- Source name: `CaravanStatus`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanStatus/)
- Used by:
  - `caravan.caravan_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The organized tour is upcoming or in progress and has not been canceled. |
| Canceled | Canceled | The organized tour has been canceled. |
| Ended | Ended | The organized tour has occurred and has ended. |

## caravan_stop_attended

- Source name: `CaravanStopAttended`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanStopAttended/)
- Used by:
  - `caravan_stop.stop_attended_by` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The caravan stop will be attended by a licensed agent. |
| Seller | Seller | The caravan stop will be attended by the seller. |
| Unattended | Unattended | The caravan stop will not be attended. |

## caravan_stop_class_name

- Source name: `CaravanStopClassName`
- Kind: **closed-SV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanStopClassName/)
- Used by:
  - `caravan_stop.stop_class_name` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Business Opportunity | BusinessOpportunity | The class, sometimes known as property type, is a business for sale. |
| Commercial Lease | CommercialLease | The class, sometimes known as property type, is a commercial property for lease. |
| Commercial Sale | CommercialSale | The class, sometimes known as property type, is a commercial property for sale. |
| Farm | Farm | The class, sometimes known as property type, is a farm. |
| Land | Land | The class, sometimes known as property type, is land for sale or lease. |
| Manufactured In Park | ManufacturedInPark | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| Residential | Residential | The class, sometimes known as property type, is residential property for sale. |
| Residential Income | ResidentialIncome | The class, sometimes known as property type, is income or multifamily property for sale. |
| Residential Lease | ResidentialLease | The class, sometimes known as property type, is residential property for lease. |

## caravan_type

- Source name: `CaravanType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CaravanType/)
- Used by:
  - `caravan.caravan_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Association | Association | The tour is being organized by an association or board of REALTORS®. |
| Broker | Broker | The tour is being organized by a brokerage. |
| Other | Other | The tour is being organized by an entity other than an association or brokerage. |

## change_type

- Source name: `ChangeType`
- Kind: **closed-SV**
- Value count: 13
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ChangeType/)
- Used by:
  - `history_transactional.change_type` (type=`String List, Single`)
  - `property.major_change_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The change to the listing was a change of status to Active. |
| Active Under Contract | ActiveUnderContract | The change to the listing was a change of status to Active Under Contract. |
| Back On Market | BackOnMarket | The change to the listing was a change of status to Back On Market. |
| Canceled | Canceled | The change to the listing was a change of status to Canceled. |
| Closed | Closed | The change to the listing was a change of status to Closed. |
| Coming Soon | ComingSoon | The change to the listing was a change of status to Coming Soon. |
| Deleted | Deleted | The change to the listing was a change of status to Deleted. |
| Expired | Expired | The change to the listing was a change of status to Expired. |
| Hold | Hold | The change to the listing was a change of status to Hold. |
| New Listing | NewListing | The listing is new and hasn't had any status or price changes since its original input. |
| Pending | Pending | The change to the listing was a change of status to Pending. |
| Price Change | PriceChange | The change to the listing was a change to the ListPrice. |
| Withdrawn | Withdrawn | The change to the listing was a change of status to Withdrawn. |

## city

- Source name: `City`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/City/)
- Used by:
  - `property.city` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## class_name

- Source name: `ClassName`
- Kind: **closed-SV**
- Value count: 17
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ClassName/)
- Used by:
  - `contact_listings.class_name` (type=`String List, Single`)
  - `history_transactional.class_name` (type=`String`)
  - `media.class_name` (type=`String List, Single`)
  - `other_phone.class_name` (type=`String List, Single`)
  - `queue.class_name` (type=`String List, Single`)
  - `rules.class_name` (type=`String List, Single`)
  - `saved_search.class_name` (type=`String List, Single`)
  - `social_media.class_name` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Business Opportunity | BusinessOpportunity | The class, sometimes known as property type, is a business for sale. |
| Commercial Lease | CommercialLease | The class, sometimes known as property type, is a commercial property for lease. |
| Commercial Sale | CommercialSale | The class, sometimes known as property type, is a commercial property for sale. |
| Contacts | Contacts | The class is the collection of the member's contacts/clients. |
| Cross Property | CrossProperty | The class, sometimes known as property type, is a collection of all listing property types. |
| Farm | Farm | The class, sometimes known as property type, is a farm. |
| History Transactional | HistoryTransactional | The class is the transactional history of another class. |
| Land | Land | The class, sometimes known as property type, is land for sale or lease. |
| Manufactured In Park | ManufacturedInPark | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| Media | Media | The class is one that contains records referencing media files. |
| Member | Member | The class containing member records. |
| Office | Office | The class containing office records. |
| Open House | OpenHouse | The class containing open house records. |
| Residential | Residential | The class, sometimes known as property type, is residential property for sale. |
| Residential Income | ResidentialIncome | The class, sometimes known as property type, is income or multifamily property for sale. |
| Residential Lease | ResidentialLease | The class, sometimes known as property type, is residential property for lease. |
| Saved Search | SavedSearch | The class containing saved search data. |

## closet_type

- Source name: `ClosetType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ClosetType/)
- Used by:
  - `property_rooms.bedroom_closet_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Built-in Closet | BuiltInCloset | The bedroom has a built-in closet. |
| None | None | The room does not have a closet. |
| Walk-in Closet | WalkInCloset | The bedroom has a walk-in closet. |

## co_buyer_agent_designation

- Source name: `CoBuyerAgentDesignation`
- Kind: **closed-MV**
- Value count: 27
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CoBuyerAgentDesignation/)
- Used by:
  - `property.co_buyer_agent_designation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accredited Buyer's Representative / ABR | AccreditedBuyersRepresentative | The Accredited Buyer's Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| Accredited Land Consultant / ALC | AccreditedLandConsultant | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| At Home With Diversity / AHWD | AtHomeWithDiversity | Learn to work effectively with and within today's diverse real estate market. |
| Certified Commercial Investment Member / CCIM | CertifiedCommercialInvestmentMember | The Certified Commercial Investment Member (CCIM) designation is commercial real estate's global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| Certified Distressed Property Expert / CDPE | CertifiedDistressedPropertyExpert | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today's turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| Certified International Property Specialist / CIPS | CertifiedInternationalPropertySpecialist | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| Certified Property Manager / CPM | CertifiedPropertyManager | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| Certified Real Estate Brokerage Manager / CRB | CertifiedRealEstateBrokerageManager | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| Certified Real Estate Team Specialist / C-RETS | CertifiedRealEstateTeamSpecialist | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| Certified Residential Specialist / CRS | CertifiedResidentialSpecialist | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| Counselor of Real Estate / CRE | CounselorOfRealEstate | The Counselors of Real Estate® is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| General Accredited Appraiser / GAA | GeneralAccreditedAppraiser | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Graduate, REALTOR Institute / GRI | GraduateRealtorInstitute | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| Military Relocation Professional / MRP | MilitaryRelocationProfessional | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| NAR's Green Designation / GREEN | NARsGreenDesignation | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| Performance Management Network / PMN | PerformanceManagementNetwork | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| Pricing Strategy Advisor / PSA | PricingStrategyAdvisor | Enhance your skills in pricing properties, creating CMAs (comparative market analysis), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| REALTOR Association Certified Executive / RCE | RealtorAssociationCertifiedExecutive | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| Real Estate Negotiation Expert / RENE | RealEstateNegotiationExpert | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| Residential Accredited Appraiser / RAA | ResidentialAccreditedAppraiser | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Resort & Second-Home Property Specialist / RSPS | ResortAndSecondHomePropertySpecialist | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| Seller Representative Specialist / SRS | SellerRepresentativeSpecialist | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| Seniors Real Estate Specialist / SRES | SeniorsRealEstateSpecialist | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| Short Sales & Foreclosure Resource / SFR | ShortSalesAndForeclosureResource | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| Society of Industrial and Office REALTORS / SIOR | SocietyOfIndustrialAndOfficeRealtors | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| Transnational Referral Certification / TRC | TransnationalReferralCertification | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |
| e-PRO | ePRO | NAR's e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |

## co_list_agent_designation

- Source name: `CoListAgentDesignation`
- Kind: **closed-MV**
- Value count: 27
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CoListAgentDesignation/)
- Used by:
  - `property.co_list_agent_designation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accredited Buyer's Representative / ABR | AccreditedBuyersRepresentative | The Accredited Buyer's Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| Accredited Land Consultant / ALC | AccreditedLandConsultant | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| At Home With Diversity / AHWD | AtHomeWithDiversity | Learn to work effectively with and within today's diverse real estate market. |
| Certified Commercial Investment Member / CCIM | CertifiedCommercialInvestmentMember | The Certified Commercial Investment Member (CCIM) designation is commercial real estate's global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| Certified Distressed Property Expert / CDPE | CertifiedDistressedPropertyExpert | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today's turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| Certified International Property Specialist / CIPS | CertifiedInternationalPropertySpecialist | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| Certified Property Manager / CPM | CertifiedPropertyManager | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| Certified Real Estate Brokerage Manager / CRB | CertifiedRealEstateBrokerageManager | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| Certified Real Estate Team Specialist / C-RETS | CertifiedRealEstateTeamSpecialist | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| Certified Residential Specialist / CRS | CertifiedResidentialSpecialist | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| Counselor of Real Estate / CRE | CounselorOfRealEstate | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| General Accredited Appraiser / GAA | GeneralAccreditedAppraiser | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Graduate, REALTOR Institute / GRI | GraduateRealtorInstitute | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| Military Relocation Professional / MRP | MilitaryRelocationProfessional | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| NAR's Green Designation / GREEN | NARsGreenDesignation | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| Performance Management Network / PMN | PerformanceManagementNetwork | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| Pricing Strategy Advisor / PSA | PricingStrategyAdvisor | Enhance your skills in pricing properties, creating CMAs (comparative market analysis), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| REALTOR Association Certified Executive / RCE | RealtorAssociationCertifiedExecutive | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| Real Estate Negotiation Expert / RENE | RealEstateNegotiationExpert | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| Residential Accredited Appraiser / RAA | ResidentialAccreditedAppraiser | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Resort & Second-Home Property Specialist / RSPS | ResortAndSecondHomePropertySpecialist | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| Seller Representative Specialist / SRS | SellerRepresentativeSpecialist | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| Seniors Real Estate Specialist / SRES | SeniorsRealEstateSpecialist | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| Short Sales & Foreclosure Resource / SFR | ShortSalesAndForeclosureResource | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| Society of Industrial and Office REALTORS / SIOR | SocietyOfIndustrialAndOfficeRealtors | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| Transnational Referral Certification / TRC | TransnationalReferralCertification | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |
| e-PRO | ePRO | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |

## common_interest

- Source name: `CommonInterest`
- Kind: **closed-SV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CommonInterest/)
- Used by:
  - `property.common_interest` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Community Apartment | CommunityApartment | Ownership interest where purchaser receives a partial/fractional interest in the land coupled with the right of exclusive occupancy of an apartment located thereon. |
| Condominium | Condominium | Ownership of an individual unit where each homeowner only owns their individual unit space and an undivided share in the ownership of common areas or in a common homeowner association (HOA). |
| None | None | Ownership of an entire parcel or lot that is not in a common-interest development (CID) or not held subject to any other common interest rights. |
| Planned Development | PlannedDevelopment | Ownership consisting of an individual lot or parcel, generally including the ownership of the land and any structures on the individual lot or parcel. |
| Stock Cooperative | StockCooperative | Ownership of an interest in a corporation which is formed primarily for the purpose of holding title to improved real property, either in fee simple or for a term of years. |
| Timeshare | Timeshare | Ownership in a time period or a point system granting possession rights to a unit or occupancy rights at a property. |

## common_walls

- Source name: `CommonWalls`
- Kind: **closed-MV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CommonWalls/)
- Used by:
  - `property.common_walls` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 1 Common Wall | OneCommonWall | The dwelling being sold has one common wall with another property that is not part of the sale. |
| 2+ Common Walls | TwoOrMoreCommonWalls | The dwelling being sold has two or more common walls with another property that is not part of the sale. |
| End Unit | EndUnit | The dwelling being sold has one or more common walls with another property that is not part of the sale and is at the end of a row of units. |
| No Common Walls | NoCommonWalls | The dwelling being sold has no attached structures that are not part of the sale. |
| No One Above | NoOneAbove | The property is attached to another dwelling that is not part of the sale, but there is no unit above the one being sold. |
| No One Below | NoOneBelow | The property is attached to another dwelling that is not part of the sale, but there is no unit below the one being sold. |

## community_features

- Source name: `CommunityFeatures`
- Kind: **closed-MV**
- Value count: 21
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CommunityFeatures/)
- Used by:
  - `property.community_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Airport/Runway | AirportRunway | The community has an airport or runway. |
| Clubhouse | Clubhouse | The community has a clubhouse. |
| Curbs | Curbs | The community streets have curbs. |
| Fishing | Fishing | The community has places to go fishing. |
| Fitness Center | FitnessCenter | The community has a fitness center. |
| Gated | Gated | The community is gated. |
| Golf | Golf | The community has golfing. |
| Lake | Lake | The community has a lake. |
| None | None | The community includes no additional features. |
| Other | Other | The community has features beyond those listed in this field. |
| Park | Park | The community has a park. |
| Pickleball | Pickleball | The community has a pickleball court. |
| Playground | Playground | The community has a playground. |
| Pool | Pool | The community has a pool. |
| Racquetball | Racquetball | The community has racquetball facilities. |
| Restaurant | Restaurant | The community has a restaurant. |
| Sidewalks | Sidewalks | The community streets have sidewalks. |
| Stable(s) | Stables | The community has one or more horse stables. |
| Street Lights | StreetLights | The community streets have lighting. |
| Suburban | Suburban | The community is a suburban setting. |
| Tennis Court(s) | TennisCourts | The community has one or more tennis courts. |

## compensation_type

- Source name: `CompensationType`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CompensationType/)
- Used by:
  - `property.buyer_brokerage_compensation_type` (type=`String List, Single`)
  - `property.sub_agency_compensation_type` (type=`String List, Single`)
  - `property.transaction_broker_compensation_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| $ | Dollars | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) as a dollar amount of the gross compensation. |
| % | Percent | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) as a percentage of the gross compensation. |
| Other | Other | A compensation type not included on this list. |
| See Remarks | SeeRemarks | The value entered in any of the compensation fields (BuyerBrokerageCompensation, SubAgencyCompensation, TransactionBrokerCompensation) is something other than % or $ or is a special combination of $, % and other compensation types. |

## concessions

- Source name: `Concessions`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Concessions/)
- Used by:
  - `property.concessions` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Call Listing Agent | CallListingAgent | Call the listing agent for information about concessions made/offered by the seller. |
| No | No | There are no concessions included with this listing. |
| Yes | Yes | There are concessions that are part of the listing/sale. |

## construction_materials

- Source name: `ConstructionMaterials`
- Kind: **closed-MV**
- Value count: 54
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ConstructionMaterials/)
- Used by:
  - `property.construction_materials` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Adobe | Adobe | The structure was made wholly or partly with adobe. |
| Aluminum Siding | AluminumSiding | The structure was made wholly or partly with aluminum siding. |
| Asbestos | Asbestos | The structure includes asbestos as a construction material. |
| Asphalt | Asphalt | The structure was made wholly or partly with asphalt. |
| Attic/Crawl Hatchway(s) Insulated | AtticCrawlHatchwaysInsulated | When not insulated, a home's attic hatch or crawlspace hatch creates one of the biggest gaps in the building envelope, increasing heat loss in winter and heat gain in summer, while making indoor living areas uncomfortable. |
| Batts Insulation | BattsInsulation | Rolls and batts, or blankets, are flexible products made from mineral fibers such as fiberglass, rock wool, cotton or wool. |
| Block | Block | The structure was made wholly or partly with block. |
| Blown-In Insulation | BlownInInsulation | Blown-in or loose-fill insulation is usually made of fiberglass, rock wool or cellulose in the form of loose fibers or fiber pellets installed using special pneumatic equipment. |
| Board & Batten Siding | BoardAndBattenSiding | The structure was made wholly or partly with board & batten siding. |
| Brick | Brick | The structure was made wholly or partly with brick. |
| Brick Veneer | BrickVeneer | The structure was made wholly or partly with brick veneer. |
| Cedar | Cedar | The structure was made wholly or partly with cedar. |
| Cement Siding | CementSiding | The structure was made wholly or partly with cement siding. |
| Clapboard | Clapboard | The structure was made wholly or partly with clapboard. |
| Concrete | Concrete | The structure was made wholly or partly with concrete. |
| Ducts Professionally Air-Sealed | DuctsProfessionallyAirSealed | The structure was made wholly or partly with ducts professionally air-sealed. |
| Exterior Duct-Work is Insulated | ExteriorDuctWorkIsInsulated | U.S. |
| Fiber Cement | FiberCement | The structure was made wholly or partly with fiber cement. |
| Fiberglass Siding | FiberglassSiding | The structure was made wholly or partly with fiberglass siding. |
| Foam Insulation | FoamInsulation | Spray foam or foam-in-place insulation can be sprayed into walls, on attic surfaces, or under floors to insulate and reduce air leakage. |
| Frame | Frame | The structure includes a frame. |
| Glass | Glass | The structure was made wholly or partly with glass. |
| HardiPlank Type | HardiplankType | The structure includes HardiPlank® siding as a construction material. |
| ICAT Recessed Lighting | IcatRecessedLighting | ICAT (Insulation Contact Air Tight) recessed light fixtures are rated both to safely come in contact with insulation and are better airsealed. |
| ICFs (Insulated Concrete Forms) | InsulatedConcreteForms | The structure was made wholly or partly with insulated concrete forms. |
| Lap Siding | LapSiding | The structure was made wholly or partly with lap siding. |
| Log | Log | The structure was made wholly or partly with log. |
| Log Siding | LogSiding | The structure was made wholly or partly with log siding. |
| Low VOC Insulation | LowVocInsulation | Volatile organic compounds (VOCs) are emitted as gases from certain solids or liquids. |
| Masonite | Masonite | The structure was made wholly or partly with Masonite. |
| Metal Siding | MetalSiding | The structure was made wholly or partly with metal siding. |
| Natural Building | NaturalBuilding | The structure was made wholly or partly with natural building. |
| Other | Other | The structure was made wholly or partly with other construction materials. |
| Plaster | Plaster | The structure was made wholly or partly with plaster. |
| Radiant Barrier | RadiantBarrier | The structure was made wholly or partly with radiant barrier. |
| Rammed Earth | RammedEarth | The structure was made wholly or partly with rammed earth. |
| Recycled/Bio-Based Insulation | RecycledBioBasedInsulation | Insulation can be made from natural or recycled materials ranging from paper to soy to denim, using sustainable materials to improve energy efficiency. |
| Redwood Siding | RedwoodSiding | The structure was made wholly or partly with redwood siding. |
| See Remarks | SeeRemarks | See remarks for more information about what the structure was wholly or partly made of. |
| Shake Siding | ShakeSiding | The structure was made wholly or partly with shake siding. |
| Shingle Siding | ShingleSiding | The structure was made wholly or partly with shingle siding. |
| Slump Block | SlumpBlock | The structure was made wholly or partly with slump block. |
| Spray Foam Insulation | SprayFoamInsulation | The structure was made wholly or partly with spray foam insulation. |
| Steel Frame | SteelFrame | The framing of the structure is made of cold-formed steel (CFS). |
| Steel Siding | SteelSiding | The structure was made wholly or partly with steel siding. |
| Stone | Stone | The structure was made wholly or partly with stone. |
| Stone Veneer | StoneVeneer | The structure was made wholly or partly with stone veneer. |
| Straw | Straw | The structure was made wholly or partly with straw. |
| Stucco | Stucco | The structure was made wholly or partly with stucco. |
| Synthetic Stucco | SyntheticStucco | The structure was made wholly or partly with synthetic stucco. |
| Unknown | Unknown | It is unknown what the structure was wholly or partly made of. |
| Vertical Siding | VerticalSiding | The structure was made wholly or partly with vertical siding. |
| Vinyl Siding | VinylSiding | The structure was made wholly or partly with vinyl siding. |
| Wood Siding | WoodSiding | The structure was made wholly or partly with wood siding. |

## contact_listing_preference

- Source name: `ContactListingPreference`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ContactListingPreference/)
- Used by:
  - `contact_listings.contact_listing_preference` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Discard | Discard | The contact has flagged to discard the given listing. |
| Favorite | Favorite | The contact has flagged the given listing as a favorite. |
| Possibility | Possibility | The contact has flagged the given listing as a possibility. |

## contact_status

- Source name: `ContactStatus`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ContactStatus/)
- Used by:
  - `contacts.contact_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The contact is active. |
| Deleted | Deleted | The contact has been deleted. |
| Inactive | Inactive | The contact is no longer active. |
| On Vacation | OnVacation | The contact is on vacation. |

## contact_type

- Source name: `ContactType`
- Kind: **closed-MV**
- Value count: 22
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ContactType/)
- Used by:
  - `contacts.contact_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Business | Business | The contact is a business relation. |
| Buyer | Buyer | The contact is the owner or principal who is purchasing the property in the transaction. |
| Buyer Attorney | BuyerAttorney | The contact supports the buyer's legal obligations of the transaction |
| Family | Family | The contact is a family member. |
| Financial Planner | FinancialPlanner | The contact represents the client's financial interests |
| Friend | Friend | The contact is a personal friend. |
| Home Improvement Specialist | HomeImprovementSpecialist | The contact works on improvements and maintenance to the property in the transaction. |
| Home Inspector | HomeInspector | The contact supports the property inspection obligations of the transaction. |
| Home Security Provider | HomeSecurityProvider | The contact provides and manages home security services to the property in the transaction. |
| Home Warranty Representative | HomeWarrantyRepresentative | The contact provides home warranty services and products to the transaction. |
| Insurance Representative | InsuranceRepresentative | The contact supports the insurance obligations of the transaction. |
| Landlord | Landlord | The contact is the owner or principal who is renting or leasing out the property in the transaction. |
| Lead | Lead | The lead is a contact that may be a potential buyer or seller to the member. |
| Loan Officer | LoanOfficer | The lender or other role that supports the mortgage obligations of the transaction. |
| Moving/Storage | MovingStorage | Provides moving or storage services to the transaction. |
| Other | Other | Any different type of role than what is explicitly provided as an option. |
| Prospect | Prospect | The contact is a prospective client. |
| Ready to Buy | ReadyToBuy | The contact is a client who is ready to start a transaction. |
| Seller | Seller | The owner or principal who is selling the property in the transaction. |
| Seller Attorney | SellerAttorney | The contact is a lead that may be a potential buyer or seller to the member. |
| Tenant | Tenant | The contact is the prospective renter or lessor of the property in the transaction. |
| Title Representative | TitleRepresentative | The contact supports the title and escrow obligations of the transaction. |

## cooling

- Source name: `Cooling`
- Kind: **closed-MV**
- Value count: 24
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Cooling/)
- Used by:
  - `property.cooling` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Attic Fan | AtticFan | The property has an attic fan. |
| Ceiling Fan(s) | CeilingFans | The property has one or more ceiling fans. |
| Central Air | CentralAir | The property has central air conditioning. |
| Dual | Dual | The cooling system has two units. |
| Ductless | Ductless | The cooling system does not have ducted or a wall/window-type unit. |
| ENERGY STAR Qualified Equipment | EnergyStarQualifiedEquipment | The cooling system is qualified as ENERGY STAR. |
| Electric | Electric | The cooling system is powered by electricity. |
| Evaporative Cooling | EvaporativeCooling | The cooling system works by way of water evaporation rather than a compressor and coolant. |
| Exhaust Fan | ExhaustFan | The structure has an exhaust fan. |
| Gas | Gas | The cooling system is powered by gas. |
| Geothermal | Geothermal | The cooling system runs on a geothermal source. |
| Heat Pump | HeatPump | A system that exchanges heat between a warm and cool space. |
| Humidity Control | HumidityControl | The cooling system includes humidity control. |
| Multi Units | MultiUnits | The cooling system includes more than one unit. |
| None | None | The property includes no cooling system. |
| Other | Other | The cooling system is different or has features that are not included on this list. |
| Roof Turbine(s) | RoofTurbines | The cooling system utilizes a roof turbine. |
| Separate Meters | SeparateMeters | The cooling system has separate meters for its multiple units/zones. |
| Varies by Unit | VariesByUnit | The cooling equipment varies by unit. |
| Wall Unit(s) | WallUnits | The cooling system is stand alone and mounted in an opening in an outer wall. |
| Wall/Window Unit(s) | WallWindowUnits | The cooling system is mounted in an opening in the wall or in a window. |
| Whole House Fan | WholeHouseFan | The property has a whole house fan. |
| Window Unit(s) | WindowUnits | The cooling system is window mounted. |
| Zoned | Zoned | The cooling system has more than one zone. |

## country

- Source name: `Country`
- Kind: **closed-SV**
- Value count: 246
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Country/)
- Used by:
  - `association.association_country` (type=`String List, Single`)
  - `association.association_mail_country` (type=`String List, Single`)
  - `contacts.home_country` (type=`String List, Single`)
  - `contacts.other_country` (type=`String List, Single`)
  - `contacts.work_country` (type=`String List, Single`)
  - `lock_or_box.listing_country` (type=`String List, Single`)
  - `member.member_country` (type=`String List, Single`)
  - `ouid.organization_country` (type=`String List, Single`)
  - `office.office_country` (type=`String List, Single`)
  - `office.office_mail_country` (type=`String List, Single`)
  - `property.country` (type=`String List, Single`)
  - `teams.team_country` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| AD | AD | Andorra is the country in which the individual, entity or property is located. |
| AE | AE | United Arab Emirates is the country in which the individual, entity or property is located. |
| AF | AF | Afghanistan is the country in which the individual, entity or property is located. |
| AG | AG | Antigua Barbuda is the country in which the individual, entity or property is located. |
| AI | AI | Anguilla is the country in which the individual, entity or property is located. |
| AL | AL | Albania is the country in which the individual, entity or property is located. |
| AM | AM | Armenia is the country in which the individual, entity or property is located. |
| AN | AN | Netherlands Antilles is the country in which the individual, entity or property is located. |
| AO | AO | Angola is the country in which the individual, entity or property is located. |
| AQ | AQ | Antarctica is the country in which the individual, entity or property is located. |
| AR | AR | Argentina is the country in which the individual, entity or property is located. |
| AS | AS | American Samoa is the country in which the individual, entity or property is located. |
| AT | AT | Austria is the country in which the individual, entity or property is located. |
| AU | AU | Australia is the country in which the individual, entity or property is located. |
| AW | AW | Aruba is the country in which the individual, entity or property is located. |
| AX | AX | Aland Islands is the country in which the individual, entity or property is located. |
| AZ | AZ | Azerbaijan is the country in which the individual, entity or property is located. |
| BA | BA | Bosnia Herzegovina is the country in which the individual, entity or property is located. |
| BB | BB | Barbados is the country in which the individual, entity or property is located. |
| BD | BD | Bangladesh is the country in which the individual, entity or property is located. |
| BE | BE | Belgium is the country in which the individual, entity or property is located. |
| BF | BF | Burkina Faso is the country in which the individual, entity or property is located. |
| BG | BG | Bulgaria is the country in which the individual, entity or property is located. |
| BH | BH | Bahrain is the country in which the individual, entity or property is located. |
| BI | BI | Burundi is the country in which the individual, entity or property is located. |
| BJ | BJ | Benin is the country in which the individual, entity or property is located. |
| BL | BL | Saint Barthelemy is the country in which the individual, entity or property is located. |
| BM | BM | Bermuda is the country in which the individual, entity or property is located. |
| BN | BN | Brunei Darussalam is the country in which the individual, entity or property is located. |
| BO | BO | Bolivia is the country in which the individual, entity or property is located. |
| BR | BR | Brazil is the country in which the individual, entity or property is located. |
| BS | BS | Bahamas is the country in which the individual, entity or property is located. |
| BT | BT | Bhutan is the country in which the individual, entity or property is located. |
| BV | BV | Bouvet Island is the country in which the individual, entity or property is located. |
| BW | BW | Botswana is the country in which the individual, entity or property is located. |
| BY | BY | Belarus is the country in which the individual, entity or property is located. |
| BZ | BZ | Belize is the country in which the individual, entity or property is located. |
| CA | CA | Canada is the country in which the individual, entity or property is located. |
| CC | CC | Cocos (Keeling) Islands is the country in which the individual, entity or property is located. |
| CD | CD | Congo Democratic Republic is the country in which the individual, entity or property is located. |
| CF | CF | Central African Republic is the country in which the individual, entity or property is located. |
| CG | CG | Congo is the country in which the individual, entity or property is located. |
| CH | CH | Switzerland is the country in which the individual, entity or property is located. |
| CI | CI | Cote d'Ivoire is the country in which the individual, entity or property is located. |
| CK | CK | Cook Islands is the country in which the individual, entity or property is located. |
| CL | CL | Chile is the country in which the individual, entity or property is located. |
| CM | CM | Cameroon is the country in which the individual, entity or property is located. |
| CN | CN | China is the country in which the individual, entity or property is located. |
| CO | CO | Colombia is the country in which the individual, entity or property is located. |
| CR | CR | Costa Rica is the country in which the individual, entity or property is located. |
| CU | CU | Cuba is the country in which the individual, entity or property is located. |
| CV | CV | Cabo Verde is the country in which the individual, entity or property is located. |
| CX | CX | Christmas Island is the country in which the individual, entity or property is located. |
| CY | CY | Cyprus is the country in which the individual, entity or property is located. |
| CZ | CZ | Czechia is the country in which the individual, entity or property is located. |
| DE | DE | Germany is the country in which the individual, entity or property is located. |
| DJ | DJ | Djibouti is the country in which the individual, entity or property is located. |
| DK | DK | Denmark is the country in which the individual, entity or property is located. |
| DM | DM | Dominica is the country in which the individual, entity or property is located. |
| DO | DO | Dominican Republic is the country in which the individual, entity or property is located. |
| DZ | DZ | Algeria is the country in which the individual, entity or property is located. |
| EC | EC | Ecuador is the country in which the individual, entity or property is located. |
| EE | EE | Estonia is the country in which the individual, entity or property is located. |
| EG | EG | Egypt is the country in which the individual, entity or property is located. |
| EH | EH | Western Sahara is the country in which the individual, entity or property is located. |
| ER | ER | Eritrea is the country in which the individual, entity or property is located. |
| ES | ES | Spain is the country in which the individual, entity or property is located. |
| ET | ET | Ethiopia is the country in which the individual, entity or property is located. |
| FI | FI | Finland is the country in which the individual, entity or property is located. |
| FJ | FJ | Fiji is the country in which the individual, entity or property is located. |
| FK | FK | Falkland Islands is the country in which the individual, entity or property is located. |
| FM | FM | Micronesia is the country in which the individual, entity or property is located. |
| FO | FO | Faroe Islands is the country in which the individual, entity or property is located. |
| FR | FR | France is the country in which the individual, entity or property is located. |
| GA | GA | Gabon is the country in which the individual, entity or property is located. |
| GB | GB | United Kingdom is the country in which the individual, entity or property is located. |
| GD | GD | Grenada is the country in which the individual, entity or property is located. |
| GE | GE | Georgia is the country in which the individual, entity or property is located. |
| GF | GF | French Guiana is the country in which the individual, entity or property is located. |
| GG | GG | Guernsey is the country in which the individual, entity or property is located. |
| GH | GH | Ghana is the country in which the individual, entity or property is located. |
| GI | GI | Gibraltar is the country in which the individual, entity or property is located. |
| GL | GL | Greenland is the country in which the individual, entity or property is located. |
| GM | GM | Gambia is the country in which the individual, entity or property is located. |
| GN | GN | Guinea is the country in which the individual, entity or property is located. |
| GP | GP | Guadeloupe is the country in which the individual, entity or property is located. |
| GQ | GQ | Equatorial Guinea is the country in which the individual, entity or property is located. |
| GR | GR | Greece is the country in which the individual, entity or property is located. |
| GS | GS | South Georgia is the country in which the individual, entity or property is located. |
| GT | GT | Guatemala is the country in which the individual, entity or property is located. |
| GU | GU | Guam is the country in which the individual, entity or property is located. |
| GW | GW | Guinea-Bissau is the country in which the individual, entity or property is located. |
| GY | GY | Guyana is the country in which the individual, entity or property is located. |
| HK | HK | Hong Kong is the country in which the individual, entity or property is located. |
| HM | HM | Heard And McDonald Islands is the country in which the individual, entity or property is located. |
| HN | HN | Honduras is the country in which the individual, entity or property is located. |
| HR | HR | Croatia is the country in which the individual, entity or property is located. |
| HT | HT | Haiti is the country in which the individual, entity or property is located. |
| HU | HU | Hungary is the country in which the individual, entity or property is located. |
| ID | ID | Indonesia is the country in which the individual, entity or property is located. |
| IE | IE | Ireland is the country in which the individual, entity or property is located. |
| IL | IL | Israel is the country in which the individual, entity or property is located. |
| IM | IM | Isle Of Man is the country in which the individual, entity or property is located. |
| IN | IN | India is the country in which the individual, entity or property is located. |
| IO | IO | British Indian Ocean Territory is the country in which the individual, entity or property is located. |
| IQ | IQ | Iraq is the country in which the individual, entity or property is located. |
| IR | IR | Iran is the country in which the individual, entity or property is located. |
| IS | IS | Iceland is the country in which the individual, entity or property is located. |
| IT | IT | Italy is the country in which the individual, entity or property is located. |
| JE | JE | Jersey is the country in which the individual, entity or property is located. |
| JM | JM | Jamaica is the country in which the individual, entity or property is located. |
| JO | JO | Jordan is the country in which the individual, entity or property is located. |
| JP | JP | Japan is the country in which the individual, entity or property is located. |
| KE | KE | Kenya is the country in which the individual, entity or property is located. |
| KG | KG | Kyrgyzstan is the country in which the individual, entity or property is located. |
| KH | KH | Cambodia is the country in which the individual, entity or property is located. |
| KI | KI | Kiribati is the country in which the individual, entity or property is located. |
| KM | KM | Comoros is the country in which the individual, entity or property is located. |
| KN | KN | Saint Kitts And Nevis is the country in which the individual, entity or property is located. |
| KP | KP | North Korea, officially named the Democratic People's Republic of Korea, is the country in which the individual, entity or property is located. |
| KR | KR | South Korea, officially named the Republic of Korea, is the country in which the individual, entity or property is located. |
| KW | KW | Kuwait is the country in which the individual, entity or property is located. |
| KY | KY | Cayman Islands is the country in which the individual, entity or property is located. |
| KZ | KZ | Kazakhstan is the country in which the individual, entity or property is located. |
| LA | LA | Lao is the country in which the individual, entity or property is located. |
| LB | LB | Lebanon is the country in which the individual, entity or property is located. |
| LC | LC | Saint Lucia is the country in which the individual, entity or property is located. |
| LI | LI | Liechtenstein is the country in which the individual, entity or property is located. |
| LK | LK | Sri Lanka is the country in which the individual, entity or property is located. |
| LR | LR | Liberia is the country in which the individual, entity or property is located. |
| LS | LS | Lesotho is the country in which the individual, entity or property is located. |
| LT | LT | Lithuania is the country in which the individual, entity or property is located. |
| LU | LU | Luxembourg is the country in which the individual, entity or property is located. |
| LV | LV | Latvia is the country in which the individual, entity or property is located. |
| LY | LY | Libyan Arab Jamahiriya is the country in which the individual, entity or property is located. |
| MA | MA | Morocco is the country in which the individual, entity or property is located. |
| MC | MC | Monaco is the country in which the individual, entity or property is located. |
| MD | MD | Moldova is the country in which the individual, entity or property is located. |
| ME | ME | Montenegro is the country in which the individual, entity or property is located. |
| MF | MF | Saint Martin is the country in which the individual, entity or property is located. |
| MG | MG | Madagascar is the country in which the individual, entity or property is located. |
| MH | MH | Marshall Islands is the country in which the individual, entity or property is located. |
| MK | MK | Macedonia is the country in which the individual, entity or property is located. |
| ML | ML | Mali is the country in which the individual, entity or property is located. |
| MM | MM | Myanmar is the country in which the individual, entity or property is located. |
| MN | MN | Mongolia is the country in which the individual, entity or property is located. |
| MO | MO | Macao is the country in which the individual, entity or property is located. |
| MP | MP | Northern Mariana Islands is the country in which the individual, entity or property is located. |
| MQ | MQ | Martinique is the country in which the individual, entity or property is located. |
| MR | MR | Mauritania is the country in which the individual, entity or property is located. |
| MS | MS | Montserrat is the country in which the individual, entity or property is located. |
| MT | MT | Malta is the country in which the individual, entity or property is located. |
| MU | MU | Mauritius is the country in which the individual, entity or property is located. |
| MV | MV | Maldives is the country in which the individual, entity or property is located. |
| MW | MW | Malawi is the country in which the individual, entity or property is located. |
| MX | MX | Mexico is the country in which the individual, entity or property is located. |
| MY | MY | Malaysia is the country in which the individual, entity or property is located. |
| MZ | MZ | Mozambique is the country in which the individual, entity or property is located. |
| NA | NA | Namibia is the country in which the individual, entity or property is located. |
| NC | NC | New Caledonia is the country in which the individual, entity or property is located. |
| NE | NE | Niger is the country in which the individual, entity or property is located. |
| NF | NF | Norfolk Island is the country in which the individual, entity or property is located. |
| NG | NG | Nigeria is the country in which the individual, entity or property is located. |
| NI | NI | Nicaragua is the country in which the individual, entity or property is located. |
| NL | NL | Netherlands is the country in which the individual, entity or property is located. |
| NP | NP | Nepal is the country in which the individual, entity or property is located. |
| NR | NR | Nauru is the country in which the individual, entity or property is located. |
| NU | NU | Niue is the country in which the individual, entity or property is located. |
| NZ | NZ | New Zealand is the country in which the individual, entity or property is located. |
| OM | OM | Oman is the country in which the individual, entity or property is located. |
| OT | OT | The country in which the individual, entity or property is located is something other than what is covered by ISO standard 3166 |
| PA | PA | Panama is the country in which the individual, entity or property is located. |
| PE | PE | Peru is the country in which the individual, entity or property is located. |
| PF | PF | French Polynesia is the country in which the individual, entity or property is located. |
| PG | PG | Papua New Guinea is the country in which the individual, entity or property is located. |
| PH | PH | Philippines is the country in which the individual, entity or property is located. |
| PK | PK | Pakistan is the country in which the individual, entity or property is located. |
| PL | PL | Poland is the country in which the individual, entity or property is located. |
| PM | PM | Saint Pierre And Miquelon is the country in which the individual, entity or property is located. |
| PN | PN | Pitcairn is the country in which the individual, entity or property is located. |
| PR | PR | Puerto Rico is the country in which the individual, entity or property is located. |
| PS | PS | Palestinian Territory is the country in which the individual, entity or property is located. |
| PT | PT | Portugal is the country in which the individual, entity or property is located. |
| PW | PW | Palau is the country in which the individual, entity or property is located. |
| PY | PY | Paraguay is the country in which the individual, entity or property is located. |
| QA | QA | Qatar is the country in which the individual, entity or property is located. |
| RE | RE | Reunion is the country in which the individual, entity or property is located. |
| RO | RO | Romania is the country in which the individual, entity or property is located. |
| RS | RS | Serbia is the country in which the individual, entity or property is located. |
| RU | RU | Russian Federation is the country in which the individual, entity or property is located. |
| RW | RW | Rwanda is the country in which the individual, entity or property is located. |
| SA | SA | Saudi Arabia is the country in which the individual, entity or property is located. |
| SB | SB | Solomon Islands is the country in which the individual, entity or property is located. |
| SC | SC | Seychelles is the country in which the individual, entity or property is located. |
| SD | SD | Sudan is the country in which the individual, entity or property is located. |
| SE | SE | Sweden is the country in which the individual, entity or property is located. |
| SG | SG | Singapore is the country in which the individual, entity or property is located. |
| SH | SH | Saint Helena is the country in which the individual, entity or property is located. |
| SI | SI | Slovenia is the country in which the individual, entity or property is located. |
| SJ | SJ | Svalbard - Jan Mayen is the country in which the individual, entity or property is located. |
| SK | SK | Slovakia is the country in which the individual, entity or property is located. |
| SL | SL | Sierra Leone is the country in which the individual, entity or property is located. |
| SM | SM | San Marino is the country in which the individual, entity or property is located. |
| SN | SN | Senegal is the country in which the individual, entity or property is located. |
| SO | SO | Somalia is the country in which the individual, entity or property is located. |
| SR | SR | Suriname is the country in which the individual, entity or property is located. |
| ST | ST | Sao Tome And Principe is the country in which the individual, entity or property is located. |
| SV | SV | El Salvador is the country in which the individual, entity or property is located. |
| SY | SY | Syrian Arab Republic is the country in which the individual, entity or property is located. |
| SZ | SZ | Swaziland is the country in which the individual, entity or property is located. |
| TC | TC | Turks - Caicos Islands is the country in which the individual, entity or property is located. |
| TD | TD | Chad is the country in which the individual, entity or property is located. |
| TF | TF | French Southern Territories is the country in which the individual, entity or property is located. |
| TG | TG | Togo is the country in which the individual, entity or property is located. |
| TH | TH | Thailand is the country in which the individual, entity or property is located. |
| TJ | TJ | Tajikistan is the country in which the individual, entity or property is located. |
| TK | TK | Tokelau is the country in which the individual, entity or property is located. |
| TL | TL | Timor-Leste is the country in which the individual, entity or property is located. |
| TM | TM | Turkmenistan is the country in which the individual, entity or property is located. |
| TN | TN | Tunisia is the country in which the individual, entity or property is located. |
| TO | TO | Tonga is the country in which the individual, entity or property is located. |
| TR | TR | Türkiye is the country in which the individual, entity or property is located. |
| TT | TT | Trinidad - Tobago is the country in which the individual, entity or property is located. |
| TV | TV | Tuvalu is the country in which the individual, entity or property is located. |
| TW | TW | Taiwan is the country in which the individual, entity or property is located. |
| TZ | TZ | Tanzania is the country in which the individual, entity or property is located. |
| UA | UA | Ukraine is the country in which the individual, entity or property is located. |
| UG | UG | Uganda is the country in which the individual, entity or property is located. |
| UM | UM | United States Minor Islands is the country in which the individual, entity or property is located. |
| US | US | United States is the country in which the individual, entity or property is located. |
| UY | UY | Uruguay is the country in which the individual, entity or property is located. |
| UZ | UZ | Uzbekistan is the country in which the individual, entity or property is located. |
| VA | VA | Holy See (Vatican City) is the country in which the individual, entity or property is located. |
| VC | VC | Saint Vincent - Grenadines is the country in which the individual, entity or property is located. |
| VE | VE | Venezuela is the country in which the individual, entity or property is located. |
| VG | VG | Virgin Islands British is the country in which the individual, entity or property is located. |
| VI | VI | Virgin Islands U.S. |
| VN | VN | Viet Nam is the country in which the individual, entity or property is located. |
| VU | VU | Vanuatu is the country in which the individual, entity or property is located. |
| WF | WF | Wallis And Futuna is the country in which the individual, entity or property is located. |
| WS | WS | Samoa is the country in which the individual, entity or property is located. |
| YE | YE | Yemen is the country in which the individual, entity or property is located. |
| YT | YT | Mayotte is the country in which the individual, entity or property is located. |
| ZA | ZA | South Africa is the country in which the individual, entity or property is located. |
| ZM | ZM | Zambia is the country in which the individual, entity or property is located. |
| ZW | ZW | Zimbabwe is the country in which the individual, entity or property is located. |

## county_or_parish

- Source name: `CountyOrParish`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CountyOrParish/)
- Used by:
  - `association.association_county_or_parish` (type=`String List, Single`)
  - `association.association_mail_county_or_parish` (type=`String List, Single`)
  - `contacts.home_county_or_parish` (type=`String List, Single`)
  - `contacts.other_county_or_parish` (type=`String List, Single`)
  - `contacts.work_county_or_parish` (type=`String List, Single`)
  - `member.member_county_or_parish` (type=`String List, Single`)
  - `ouid.organization_county_or_parish` (type=`String List, Single`)
  - `office.office_county_or_parish` (type=`String List, Single`)
  - `office.office_mail_county_or_parish` (type=`String List, Single`)
  - `property.county_or_parish` (type=`String List, Single`)
  - `teams.team_county_or_parish` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## current_financing

- Source name: `CurrentFinancing`
- Kind: **closed-MV**
- Value count: 15
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CurrentFinancing/)
- Used by:
  - `property.current_financing` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Assumable | Assumable | The financing currently in place may be assumed. |
| Contract | Contract | The purchase of a property involves an agreement to perform services, provide product, share income or some other determined method of payment for the property. |
| Conventional | Conventional | The buyer is using conventional financing to purchase the home. |
| FHA | Fha | A loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| FHA 203(b) | Fha203b | The basic home mortgage loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| FHA 203(k) | Fha203k | A loan for the rehabilitation and repair of a single-family residence from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| Leased Renewables | LeasedRenewables | A renewable system (i.e., solar or wind) belonging to a third party is installed on a customer's property at little or no cost to the property owner. |
| None | None | There is no current financing on the property. |
| Other | Other | The current owner is using another form of financing that is not included in the options provided on this list. |
| Power Purchase Agreement | PowerPurchaseAgreement | A renewable system belonging to a third-party is installed on a customer's property at little or no up-front cost to the property owner. |
| Private | Private | Financing is provided by a private party. |
| Property-Assessed Clean Energy | PropertyAssessedCleanEnergy | Property-assessed clean energy (PACE) is a financing tool for property owners to fund energy or water efficiency or renewable energy installations. |
| Trust Deed | TrustDeed | Financing where property title is placed with a trustee who secures payment of the loan for a beneficiary. |
| USDA | Usda | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| VA | Va | A loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

## current_or_possible_use

- Source name: `CurrentOrPossibleUse`
- Kind: **closed-MV**
- Value count: 43
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/CurrentOrPossibleUse/)
- Used by:
  - `property.current_use` (type=`String List, Multi`)
  - `property.possible_use` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agricultural | Agricultural | The land is currently used for or could be used for agriculture. |
| Automotive | Automotive | This land is currently used for or could be used for automotive maintenance or repair. |
| Cattle | Cattle | This land is currently used for or could be used for cattle. |
| Commercial | Commercial | This land is currently used for or could be used for commercial purposes. |
| Dairy | Dairy | This land is currently used as or could be used as a dairy farm. |
| Development | Development | This land is currently used for or could be used for a new development. |
| Farm | Farm | This land is currently used as or could be used as a farm. |
| Fishery | Fishery | This land is currently used as or could be used as a fishery. |
| Grazing | Grazing | This land is currently used for or could be used for livestock grazing. |
| Highway/Tourist Service | HighwayTouristService | This land is currently used for or could be used for highway/tourist service. |
| Horses | Horses | This land is currently used for or could be used for horses. |
| Hunting | Hunting | This land is currently used for or could be used for hunting. |
| Industrial | Industrial | This land is currently used for or could be used for industrial purposes. |
| Investment | Investment | This land is currently used as or could be used as an investment. |
| Livestock | Livestock | This land is currently used for or could be used for livestock. |
| Manufactured Home | ManufacturedHome | This land is currently used for or could be used for a manufactured home or homes. |
| Medical/Dental | MedicalDental | This land is currently used for or could be used for a medical/dental business. |
| Mini Storage | MiniStorage | This land is currently used for or could be used for a mini storage business. |
| Mixed Use | MixedUse | This land is currently used for or could be used for mixed uses. |
| Multi-Family | MultiFamily | The land is currently used for or could be used for a multifamily dwelling or dwellings. |
| Nursery | Nursery | The land is currently used as or could be used as a nursery. |
| Office | Office | This land is currently used as or could be used as office space. |
| Orchard | Orchard | This land is currently used as or could be used as an orchard. |
| Other | Other | The land is currently used for or could be used for some use other than those on this list. |
| Pasture | Pasture | This land is currently used as or could be used as a pasture. |
| Place of Worship | PlaceOfWorship | This land is currently used as or could be used as a place of worship. |
| Plantable | Plantable | This land is currently used as or could be used as a plantable field. |
| Poultry | Poultry | This land is currently used as or could be used as a poultry farm. |
| Ranch | Ranch | This land is currently used as or could be used as a ranch. |
| Recreational | Recreational | This land is currently used for or could be used for recreational purposes. |
| Residential | Residential | This land is currently used for or could be used for residential purposes. |
| Retail | Retail | This land is currently used for or could be used for retail purposes. |
| Row Crops | RowCrops | This land is currently used for or could be used for row crops. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the current or possible use. |
| Single Family | SingleFamily | The land is currently used for single-family residence. |
| Subdevelopment | Subdevelopment | This land is currently used for or could be used for a subdevelopment or subdevelopments. |
| Subdivision | Subdivision | This land is currently used for or could be used for property subdivisions. |
| Timber | Timber | This land is currently used for or could be used for timber. |
| Tree Farm | TreeFarm | This land is currently used as or could be used as a tree farm. |
| Unimproved | Unimproved | The land is currently unimproved. |
| Vacant | Vacant | The land is currently vacant. |
| Vineyard | Vineyard | This land is currently used as or could be used as a vineyard. |
| Warehouse | Warehouse | This land is currently used for or could be used for warehousing. |

## daily_schedule

- Source name: `DailySchedule`
- Kind: **closed-MV**
- Value count: 15
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DailySchedule/)
- Used by:
  - `prospecting.daily_schedule` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Friday AM | FridayAm | The prospect automated email will be sent every Friday morning. |
| Friday PM | FridayPm | The prospect automated email will be sent every Friday evening. |
| Monday AM | MondayAm | The prospect automated email will be sent every Monday morning. |
| Monday PM | MondayPm | The prospect automated email will be sent every Monday evening. |
| None | None | The prospect automated email has not been setup for any daily schedule. |
| Saturday AM | SaturdayAm | The prospect automated email will be sent every Saturday morning. |
| Saturday PM | SaturdayPm | The prospect automated email will be sent every Saturday evening. |
| Sunday AM | SundayAm | The prospect automated email will be sent every Sunday morning. |
| Sunday PM | SundayPm | The prospect automated email will be sent every Sunday evening. |
| Thursday AM | ThursdayAm | The prospect automated email will be sent every Thursday morning. |
| Thursday PM | ThursdayPm | The prospect automated email will be sent every Thursday evening. |
| Tuesday AM | TuesdayAm | The prospect automated email will be sent every Tuesday morning. |
| Tuesday PM | TuesdayPm | The prospect automated email will be sent every Tuesday evening. |
| Wednesday AM | WednesdayAm | The prospect automated email will be sent every Wednesday morning. |
| Wednesday PM | WednesdayPm | The prospect automated email will be sent every Wednesday evening. |

## development_status

- Source name: `DevelopmentStatus`
- Kind: **closed-MV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DevelopmentStatus/)
- Used by:
  - `property.development_status` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Completed | Completed | The development of the land is complete. |
| Finished Lot(s) | FinishedLots | The development of the land is finished. |
| Other | Other | The development status of the land is something other than those options on this list. |
| Proposed | Proposed | The development of the land is in the proposal phase. |
| Raw Land | RawLand | The land is raw and undeveloped. |
| Rough Grade | RoughGrade | The development of the last is in the rough grade phase. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the development status of the land. |
| Site Plan Approved | SitePlanApproved | The site plan has been approved for the development. |
| Site Plan Filed | SitePlanFiled | The site plan has been filed for the development. |
| Under Construction | UnderConstruction | There is construction in progress at the development. |

## device_type

- Source name: `DeviceType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DeviceType/)
- Used by:
  - `internet_tracking.device_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Desktop | Desktop | The actor's device has been identified as a desktop device by the source. |
| Mobile | Mobile | The actor's device has been identified as a mobile device by the source. |
| Tablet | Tablet | The actor's device has been identified as a tablet device by the source. |
| Unknown | Unknown | The actor's device could not be identified by the source. |
| Wearable | Wearable | The actor's device has been identified as a wearable device by the source. |

## direction_faces

- Source name: `DirectionFaces`
- Kind: **closed-SV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DirectionFaces/)
- Used by:
  - `property.direction_faces` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| East | East | The front of the structure faces east. |
| North | North | The front of the structure faces north. |
| Northeast | Northeast | The front of the structure faces northeast. |
| Northwest | Northwest | The front of the structure faces northwest. |
| South | South | The front of the structure faces south. |
| Southeast | Southeast | The front of the structure faces southeast. |
| Southwest | Southwest | The front of the structure faces southwest. |
| West | West | The front of the structure faces west. |

## disclosures

- Source name: `Disclosures`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Disclosures/)
- Used by:
  - `property.disclosures` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## documents_available

- Source name: `DocumentsAvailable`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DocumentsAvailable/)
- Used by:
  - `property.documents_available` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## document_status

- Source name: `DocumentStatus`
- Kind: **closed-SV**
- Value count: 16
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DocumentStatus/)
- Used by:
  - `property.document_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accepted | Accepted | Document has been accepted by a party in the transaction. |
| Archived | Archived | Document has been archived by a party in the transaction. |
| Changed | Changed | Document has been changed by a party in the transaction. |
| Countered | Countered | Document has been countered by either (any) party. |
| Deleted | Deleted | Document has been deleted by a party in the transaction. |
| Delivered | Delivered | Document has been delivered by a party in the transaction. |
| Finalized | Finalized | Document has been finalized by all clients in the transaction. |
| In Escrow | InEscrow | Document indicating escrow for the transaction. |
| Missing | Missing | A placeholder for where a contract requires certain items before execution. |
| Optional | Optional | Document is optional for the transaction. |
| Published | Published | Document has been published by a party in the transaction. |
| Received | Received | Document has been received by a party in the transaction. |
| Rejected | Rejected | Document has been rejected by a party in the transaction. |
| Required | Required | Document is required for the transaction. |
| Signed | Signed | Document has been signed by a party in the transaction. |
| Submitted | Submitted | Document has been submitted to cooperating party or parties. |

## door_features

- Source name: `DoorFeatures`
- Kind: **closed-MV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/DoorFeatures/)
- Used by:
  - `property.door_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| ENERGY STAR Qualified Doors | EnergyStarQualifiedDoors | The property has a qualified ENERGY STAR door or multiple qualified doors. |
| French Doors | FrenchDoors | The property has doors with glass panes throughout the length of the door. |
| Mirrored Closet Door(s) | MirroredClosetDoors | The property has one or more closet doors that have a mirrored surface. |
| Sliding Doors | SlidingDoors | The property has sliding doors. |
| Storm Door(s) | StormDoors | The property has one or more storm doors. |

## electric

- Source name: `Electric`
- Kind: **closed-MV**
- Value count: 18
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Electric/)
- Used by:
  - `property.electric` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 100 Amp Service | Amps100 | The electrical features of the property include 100 amp service. |
| 150 Amp Service | Amps150 | The electrical features of the property include 150 amp service. |
| 200+ Amp Service | Amps200OrMore | The electrical features of the property include 200+ amp service. |
| 220 Volts | Volts220 | The electrical features of the property include 220 volts. |
| 220 Volts For Spa | Volts220ForSpa | The electrical features of the property include 220 volts for spa. |
| 220 Volts in Garage | Volts220InGarage | The electrical features of the property include 220 volts in garage. |
| 220 Volts in Kitchen | Volts220InKitchen | The electrical features of the property include 220 volts in kitchen. |
| 220 Volts in Laundry | Volts220InLaundry | The electrical features of the property include 220 volts in laundry. |
| 220 Volts in Workshop | Volts220InWorkshop | The electrical features of the property include 220 volts in workshop. |
| 440 Volts | Volts440 | The electrical features of the property include 440 volts. |
| Circuit Breakers | CircuitBreakers | The electrical features of the property include circuit breakers. |
| Energy Storage Device | EnergyStorageDevice | A device that captures energy at one time to be used at a later time. |
| Fuses | Fuses | The electrical features of the property include fuses. |
| Generator | Generator | The electrical features of the property include a generator. |
| Net Meter | NetMeter | Net metering is an electric service that allows electricity generated on a consumer's site ("on-site") to offset that consumer's use. |
| Pre-Wired for Renewables | PreWiredForRenewables | Indicates the electric infrastructure on the property has been extended to more easily incorporate an on-site electric generation facility in the future. |
| Ready for Renewables | ReadyForRenewables | Indicates a comprehensive infrastructure is in place on the property to more easily incorporate an on-site electric generation facility in the future. |
| Underground | Underground | The electrical features of the property include components that are underground. |

## elementary_school

- Source name: `ElementarySchool`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ElementarySchool/)
- Used by:
  - `property.elementary_school` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## elementary_school_district

- Source name: `ElementarySchoolDistrict`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ElementarySchoolDistrict/)
- Used by:
  - `property.elementary_school_district` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## event_source

- Source name: `EventSource`
- Kind: **closed-SV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/EventSource/)
- Used by:
  - `internet_tracking.event_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| AI | AI | The source of the object is the result of what the client systems deem as Artificial Intelligence (AI). |
| GPS | Gps | The source of the object is the result of Global Positioning System (GPS) activity. |
| List | List | The source of the object being viewed pertaining to application structure (e.g., the listing impression was displayed in a scrollable list/table with others). |
| Map | Map | The source of the object being viewed pertaining to application structure (e.g., the listing impression was displayed on a map). |
| Search Engine | SearchEngine | The source of the object is the result of a search engine assistant (e.g., Google, Bing, Safari). |
| Voice Assistant | VoiceAssistant | The source of the object being viewed pertaining to application structure (e.g., the listing impression was conveyed via a voice assistant like Amazon Echo). |

## event_target

- Source name: `EventTarget`
- Kind: **closed-SV**
- Value count: 21
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/EventTarget/)
- Used by:
  - `internet_tracking.event_target` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The EventType used a destination pertaining to the listing agent (e.g., the actor's Submission of Lead Form went to the listing agent's contact information). |
| Broker | Broker | The EventType used a destination pertaining to the listing broker (e.g., the Clicked on Phone Number EventType uses the broker's contact information). |
| Digg | Digg | The object was shared on Digg. |
| Email | Email | The object was sent in an email. |
| Facebook | Facebook | The object was shared on Facebook. |
| Facebook Messenger | FacebookMessenger | The object was shared via Facebook Messenger. |
| Instagram | Instagram | The object was shared on Instagram. |
| LinkedIn | Linkedin | The object was shared on LinkedIn. |
| Microsoft Teams | MicrosoftTeams | The object was shared via the Teams application/service. |
| Pinterest | Pinterest | The object was pinned on Pinterest. |
| Reddit | Reddit | The object was shared on Reddit. |
| SMS | Sms | The object was sent in an SMS message. |
| Slack | Slack | The object was shared via Slack. |
| Snapchat | Snapchat | The object was shared on Snapchat. |
| StumbleUpon | Stumbleupon | The object was shared on StumbleUpon. |
| TikTok | TikTok | The object was shared on TikTok. |
| Tumblr | Tumblr | The object was shared on Tumblr. |
| Twitter | Twitter | The object was posted on X (formerly Twitter). |
| WhatsApp | WhatsApp | The object was shared via the WhatsApp application. |
| YouTube | Youtube | The object was shared on YouTube. |
| iMessage | Imessage | The object was shared via iMessage. |

## event_type

- Source name: `EventType`
- Kind: **closed-SV**
- Value count: 20
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/EventType/)
- Used by:
  - `internet_tracking.event_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Click to Primary Hosted Site | ClickToPrimaryHostedSite | The actor was referred to the object's primary hosted website. |
| Clicked on Email Address | ClickedOnEmailAddress | The actor engaged in the act of emailing to the object's email address (note: does not indicate an email was sent). |
| Clicked on Phone Number | ClickedOnPhoneNumber | The actor clicked on a phone number link associated with the object. |
| Comments | Comments | Comments were made on the object. |
| Detailed View | DetailedView | The object was the main focal point in the actor's view. |
| Discard | Discard | The actor has reacted "negatively" to the object. |
| Driving Directions | DrivingDirections | The actor engaged in driving directions with the object |
| Exit Detailed View | ExitDetailedView | The actor left the detailed view. |
| Favorited | Favorited | The actor has reacted "positively" to the object. |
| Impression | Impression | The object appeared as a form of impression. |
| Maybe | Maybe | The actor has reacted "possibly positive" to the object. |
| Object Modified | ObjectModified | The tracking object was modified in some way. |
| Photo Gallery | PhotoGallery | The actor participated in a photo gallery display. |
| Printed | Printed | The actor printed the object. |
| Property Videos | PropertyVideos | The actor has interacted with a property video with the object. |
| Scrolled Depth | ScrolledDepth | The user has scrolled on the pageview. |
| Search | Search | The tracking object data is part of a search and will contain more than one result. |
| Share | Share | The sharing of a listing to another media or entity, including social media, IM (instant message), email and SMS (Short Message Service) messages. |
| Submission of Lead Form | SubmissionOfLeadForm | The actor has submitted a lead form. |
| Virtual Tour | VirtualTour | The actor viewed the object's virtual tour. |

## existing_lease_type

- Source name: `ExistingLeaseType`
- Kind: **closed-MV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ExistingLeaseType/)
- Used by:
  - `property.available_lease_type` (type=`String List, Multi`)
  - `property.existing_lease_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Absolute Net | AbsoluteNet | Also known as a bondable lease, the tenant carries every risk in addition to the costs of an NNN lease. |
| CPI Adjustment | CpiAdjustment | An escalation clause/provision in a lease to adjust the amount paid by the tenant (lessee) where the adjustment will follow the Consumer Price Index (CPI). |
| Escalation Clause | EscalationClause | A clause or provision in a lease document that set a formula for how rent will increase over time. |
| Gross | Gross | A lease agreement where the owner (lessor) pays all property changes normal to ownership. |
| Ground Lease | GroundLease | Typically a long-term lease of land where the tenant (lessee) has the right to develop or make improvements. |
| NN | Nn | A lease agreement where the tenant pays real estate taxes and building insurance. |
| NNN | Nnn | A lease agreement where the tenant pays real estate taxes, building insurance and maintenance. |
| Net | Net | A lease agreement where the tenant pays the real estate taxes. |
| Oral | Oral | The terms of the lease are agreed upon orally (not in writing) between the lessee and lessor. |

## exterior_features

- Source name: `ExteriorFeatures`
- Kind: **closed-MV**
- Value count: 37
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ExteriorFeatures/)
- Used by:
  - `property.exterior_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Awning(s) | Awnings | The property has one or more awnings on its exterior. |
| Balcony | Balcony | The property has an exterior balcony. |
| Barbecue | Barbecue | The property has an outdoor barbeque. |
| Basketball Court | BasketballCourt | The property has a basketball court. |
| Boat Slip | BoatSlip | The property includes a boat slip. |
| Built-in Barbecue | BuiltInBarbecue | The property has a built-in outdoor barbeque. |
| Courtyard | Courtyard | The property has a courtyard. |
| Covered Courtyard | CoveredCourtyard | The property has a covered courtyard. |
| Dock | Dock | The property includes a dock. |
| Dog Run | DogRun | The property has a dog run. |
| Electric Grill | ElectricGrill | The property has an outdoor electric grill. |
| Fire Pit | FirePit | The property has an outdoor fire pit. |
| Garden | Garden | The property has a garden. |
| Gas Grill | GasGrill | The property has an outdoor gas grill. |
| Gray Water System | GrayWaterSystem | The property has a gray water (aka greywater or grey water) system. |
| Kennel | Kennel | The property has a kennel. |
| Lighting | Lighting | The property has exterior lighting. |
| Misting System | MistingSystem | The property has a misting system. |
| None | None | The property has no exterior features. |
| Other | Other | The property has exterior features other than those on this list. |
| Outdoor Grill | OutdoorGrill | The property has an outdoor grill. |
| Outdoor Kitchen | OutdoorKitchen | The property has an outdoor kitchen. |
| Outdoor Shower | OutdoorShower | The property has an outdoor shower. |
| Permeable Paving | PermeablePaving | The property has preamble paving that allows fluids to run through the paving to the below ground or channeling. |
| Playground | Playground | The property has a playground. |
| Private Entrance | PrivateEntrance | The property has a private entrance. |
| Private Yard | PrivateYard | The property has a private yard. |
| RV Hookup | RvHookup | The property has hookups for recreational vehicles. |
| Rain Barrel/Cistern(s) | RainBarrelCisterns | The property has a cistern for water collection. |
| Rain Gutters | RainGutters | The structure has rain gutters. |
| Smart Camera(s)/Recording | SmartCamerasRecording | A camera or recording control unit that has convenience and energy-saving aspects. |
| Smart Irrigation | SmartIrrigation | An irrigation system that has convenience and energy-saving aspects. |
| Smart Light(s) | SmartLights | A lighting control unit that has convenience and energy-saving aspects. |
| Smart Lock(s) | SmartLocks | A locking system that has convenience and safety aspects. |
| Storage | Storage | The property has external storage. |
| Tennis Court(s) | TennisCourts | The property has one or more tennis courts. |
| Uncovered Courtyard | UncoveredCourtyard | The property has an uncovered courtyard. |

## fee_frequency

- Source name: `FeeFrequency`
- Kind: **closed-SV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FeeFrequency/)
- Used by:
  - `property.association_fee2_frequency` (type=`String List, Single`)
  - `property.association_fee_frequency` (type=`String List, Single`)
  - `property.land_lease_amount_frequency` (type=`String List, Single`)
  - `property.lease_amount_frequency` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Annually | Annually | A fee is paid or received once a year. |
| Bi-Monthly | BiMonthly | A fee is paid or received every other month. |
| Bi-Weekly | BiWeekly | A fee is paid or received every other week. |
| Daily | Daily | A fee is paid or received daily. |
| Monthly | Monthly | A fee is paid or received once a month. |
| One Time | OneTime | A fee is paid or received once and is not recurring. |
| Quarterly | Quarterly | A fee is paid or received every three months. |
| Seasonal | Seasonal | A fee is paid or received seasonally. |
| Semi-Annually | SemiAnnually | A fee is paid or received twice a year. |
| Semi-Monthly | SemiMonthly | A fee is paid or received twice a month, generally on the 1st and 15th, but that may vary. |
| Weekly | Weekly | A fee is paid or received weekly. |

## fencing

- Source name: `Fencing`
- Kind: **closed-MV**
- Value count: 29
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Fencing/)
- Used by:
  - `property.fencing` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Back Yard | BackYard | The backyard is fenced. |
| Barbed Wire | BarbedWire | The fencing has barbed wire. |
| Block | Block | The property has one or more block walls. |
| Brick | Brick | The property has one or more brick walls. |
| Chain Link | ChainLink | The property has chain-link fencing. |
| Cross Fenced | CrossFenced | The property is cross fenced. |
| Electric | Electric | The property has electric fencing. |
| Fenced | Fenced | The property is fenced. |
| Front Yard | FrontYard | The front yard is fenced. |
| Full | Full | The full property is fenced. |
| Gate | Gate | The fencing has one or more gates. |
| Invisible | Invisible | The property has invisible fencing. |
| Masonry | Masonry | The property has one or more masonry walls. |
| None | None | The property has no fencing. |
| Other | Other | The property has a type of fencing that is not included on this list. |
| Partial | Partial | The property is partially fenced. |
| Partial Cross | PartialCross | The property has partial cross fencing. |
| Perimeter | Perimeter | The property has a perimeter fence. |
| Pipe | Pipe | The property has pipe fencing. |
| Privacy | Privacy | The property has privacy fencing. |
| Security | Security | The property has security fencing. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the fencing. |
| Slump Stone | SlumpStone | The property has one or more slump stone walls. |
| Split Rail | SplitRail | The property has split rail fencing. |
| Stone | Stone | The property has one or more stone walls. |
| Vinyl | Vinyl | The property has vinyl fencing. |
| Wire | Wire | The property has wire fencing. |
| Wood | Wood | The property has wooden fencing. |
| Wrought Iron | WroughtIron | The property has wrought iron fencing. |

## fha_eligibility

- Source name: `FhaEligibility`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FhaEligibility/)
- Used by:
  - `property.fha_eligibility` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Approved | Approved | This listing is eligible for an FHA loan. |
| Conditionally Approved | ConditionallyApproved | This listing is eligible for a Federal Housing Administration (FHA) loan as long as some conditions are met. |
| Rejected | Rejected | This listing is not eligible for a Federal Housing Administration (FHA) loan. |
| Unknown | Unknown | Unknown is selected when Federal Housing Administration (FHA) eligibility is not known. |
| Withdrawn | Withdrawn | Federal Housing Administration (FHA) eligibility has been withdrawn and is no longer applicable. |

## financial_data_source

- Source name: `FinancialDataSource`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FinancialDataSource/)
- Used by:
  - `property.financial_data_source` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accountant | Accountant | The financial data in the listing was provided by an accountant. |
| Owner | Owner | the financial data in the listing was provided by the owner. |
| Property Manager | PropertyManager | the financial data in the listing was provided by the property manager. |

## fireplace_features

- Source name: `FireplaceFeatures`
- Kind: **closed-MV**
- Value count: 44
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FireplaceFeatures/)
- Used by:
  - `property.fireplace_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Basement | Basement | There is a fireplace in the basement. |
| Bath | Bath | The property includes a bathroom fireplace. |
| Bedroom | Bedroom | The property has a bedroom fireplace. |
| Blower Fan | BlowerFan | The fireplace has a blower fan. |
| Circulating | Circulating | The fireplace has a circulation system. |
| Decorative | Decorative | The property has a decorative fireplace. |
| Den | Den | The property has a fireplace in the den. |
| Dining Room | DiningRoom | The property has a fireplace in the dining room. |
| Double Sided | DoubleSided | The property has a double-sided fireplace. |
| EPA Certified Wood Stove | EpaCertifiedWoodStove | The property has a wood stove certified by the Environmental Protection Agency (EPA). |
| EPA Qualified Fireplace | EpaQualifiedFireplace | The property has a fireplace certified by the Environmental Protection Agency (EPA). |
| Electric | Electric | The fireplace is electric. |
| Factory Built | FactoryBuilt | The fireplace is factory built and later installed into the property. |
| Family Room | FamilyRoom | There is a fireplace in the family room. |
| Fire Pit | FirePit | The property has a fire pit. |
| Free Standing | FreeStanding | The fireplace is free standing, rather than built-in. |
| Gas | Gas | The fireplace burns gas. |
| Gas Log | GasLog | The gas fireplace has a gas log. |
| Gas Starter | GasStarter | The fireplace has a gas starter but also burns wood or other fuels. |
| Glass Doors | GlassDoors | The fireplace has glass doors. |
| Great Room | GreatRoom | There is a fireplace in the great room. |
| Heatilator | Heatilator | The fireplace has a built-in ventilation system used to circulate heat. |
| Insert | Insert | A fireplace insert is a device inserted into an existing masonry or prefabricated fireplace. |
| Kitchen | Kitchen | The property has a fireplace in the kitchen. |
| Library | Library | The property has a fireplace in the library. |
| Living Room | LivingRoom | The property has a fireplace in the living room. |
| Masonry | Masonry | The fireplace is made of masonry. |
| Master Bedroom | MasterBedroom | The property has a fireplace in the primary bedroom. |
| Metal | Metal | The fireplace is made of metal. |
| None | None | The property has no fireplace. |
| Other | Other | The fireplace has features that are not included on this list. |
| Outside | Outside | The property has an outdoor fireplace. |
| Pellet Stove | PelletStove | The property has a stove that burns compressed wood or biomass pellets to generate heat. |
| Propane | Propane | The fireplace burns propane. |
| Raised Hearth | RaisedHearth | The fireplace has a raised hearth. |
| Recreation Room | RecreationRoom | The property has a fireplace in a recreation room. |
| Sealed Combustion | SealedCombustion | The fireplace has a sealed combustion chamber. |
| See Remarks | SeeRemarks | See the remarks fields for additional information about any fireplace features. |
| See Through | SeeThrough | The property has a see-through fireplace, usually positioned between two rooms. |
| Stone | Stone | The property has a fireplace made with stone. |
| Ventless | Ventless | The property has a ventless fireplace. |
| Wood Burning | WoodBurning | The fireplace is wood burning. |
| Wood Burning Stove | WoodBurningStove | The property includes a wood-burning stove. |
| Zero Clearance | ZeroClearance | The property has a zero-clearance fireplace. |

## flooring

- Source name: `Flooring`
- Kind: **closed-MV**
- Value count: 39
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Flooring/)
- Used by:
  - `property.flooring` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Adobe | Adobe | The property includes adobe flooring. |
| Bamboo | Bamboo | The property includes bamboo flooring. |
| Brick | Brick | The property includes brick flooring. |
| CRI Green Label Plus Certified Carpet | CriGreenLabelPlusCertifiedCarpet | The property includes certified CRI Green Label Plus carpet flooring. |
| Carpet | Carpet | The property includes carpet flooring. |
| Ceramic Tile | CeramicTile | The property includes ceramic tile flooring. |
| Clay | Clay | The property includes clay flooring. |
| Combination | Combination | The property includes combination flooring. |
| Concrete | Concrete | The property includes concrete flooring. |
| Cork | Cork | The property includes cork flooring. |
| Dirt | Dirt | The property has dirt flooring. |
| Engineered Hardwood | EngineeredHardwood | The property includes engineered hardwood flooring, a type of flooring made up of derivative wood products that are manufactured by binding or fixing the strands, particles, fibers, veneers or boards of wood together with adhesives or other methods of fixation to form composite material. |
| FSC or SFI Certified Source Hardwood | FscOrSfiCertifiedSourceHardwood | The property includes certified FSC or SFI source hardwood flooring. |
| FloorScore(r) Certified Flooring | FloorScoreCertifiedFlooring | The property includes FloorScore® certified flooring . |
| Granite | Granite | The property includes granite flooring. |
| Hardwood | Hardwood | The property includes hardwood flooring. |
| Laminate | Laminate | The property includes laminate flooring. |
| Linoleum | Linoleum | The property includes linoleum flooring. |
| Luxury Vinyl | LuxuryVinyl | The property includes luxury vinyl flooring, which is a waterproof and durable flooring that mimics the look of hardwood or stone. |
| Marble | Marble | The property includes marble flooring. |
| None | None | The property has no flooring. |
| Other | Other | The property includes flooring that is not included on this list. |
| Painted/Stained | PaintedStained | The property includes painted or stained flooring. |
| Parquet | Parquet | The property includes parquet flooring. |
| Pavers | Pavers | The property includes flooring pavers. |
| Plank | Plank | The property includes plank flooring, which comes in multi-ply, long, narrow strips and is thicker than typical sheet vinyl. |
| Reclaimed Wood | ReclaimedWood | The property includes reclaimed wood flooring. |
| See Remarks | SeeRemarks | See the remarks field for additional information about the flooring included with the property. |
| Simulated Wood | SimulatedWood | The property includes simulated wood flooring. |
| Slate | Slate | The property includes slate flooring. |
| Softwood | Softwood | The property includes softwood flooring. |
| Stamped | Stamped | The property includes stamped flooring. |
| Stone | Stone | The property includes stone flooring. |
| Sustainable | Sustainable | The property includes sustainable flooring. |
| Terrazzo | Terrazzo | The property includes terrazzo flooring. |
| Tile | Tile | The property includes tile flooring. |
| Varies | Varies | The property flooring type varies. |
| Vinyl | Vinyl | The property includes vinyl flooring. |
| Wood | Wood | The property includes wood flooring. |

## foundation_details

- Source name: `FoundationDetails`
- Kind: **closed-MV**
- Value count: 12
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FoundationDetails/)
- Used by:
  - `property.foundation_details` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Block | Block | The foundation of the property is made wholly or partially of block. |
| Brick/Mortar | BrickMortar | The foundation of the property is made wholly or partially of brick/mortar. |
| Combination | Combination | The foundation of the property is made of a combination of materials. |
| Concrete Perimeter | ConcretePerimeter | The foundation of the property has a concrete perimeter. |
| None | None | There are no details about the foundation of the property. |
| Other | Other | A foundation type not included on this list. |
| Permanent | Permanent | The foundation is permanent and not temporary or movable. |
| Pillar/Post/Pier | PillarPostPier | The foundation of the property is made wholly or partially of pillar/post/pier. |
| Raised | Raised | The foundation of the property is raised. |
| See Remarks | SeeRemarks | See the listing's remarks for details about the foundation. |
| Slab | Slab | The foundation of the property is made wholly or partially of a concrete slab. |
| Stone | Stone | The foundation of the property is made wholly or partially of stone. |

## frontage_type

- Source name: `FrontageType`
- Kind: **closed-MV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/FrontageType/)
- Used by:
  - `property.frontage_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bay/Harbor | BayHarbor | The property fronts to a bay or harbor. |
| Golf Course | GolfCourse | The property fronts to a golf course. |
| Lagoon/Estuary | LagoonEstuary | The property fronts to a lagoon or estuary. |
| Lakefront | Lakefront | The property is on a lakefront. |
| Oceanfront | Oceanfront | The property is on an oceanfront. |
| Other | Other | The frontage of the property is something other than the options on this list. |
| River | River | The property is on a riverfront. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the frontage of the property. |
| Waterfront | Waterfront | The property is on a waterfront. |

## furnished

- Source name: `Furnished`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Furnished/)
- Used by:
  - `property.furnished` (type=`String List, Single`)
  - `property_unit_types.unit_type_furnished` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Furnished | Furnished | The dwelling being leased is furnished. |
| Negotiable | Negotiable | The property may be furnished or left unfurnished at the lessor's request. |
| Partially | Partially | The dwelling being leased is partially furnished. |
| Unfurnished | Unfurnished | The dwelling being leased is not furnished. |

## green_building_verification_type

- Source name: `GreenBuildingVerificationType`
- Kind: **closed-SV**
- Value count: 18
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenBuildingVerificationType/)
- Used by:
  - `property.green_building_verification_type` (type=`String List, Multi`)
  - `property_green_verification.green_building_verification_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Certified Passive House | CertifiedPassiveHouse | Super-insulated new homes that have been built to meet certification requirements demonstrating minimal or no heating and cooling system. |
| ENERGY STAR Certified Homes | EnergyStarCertifiedHomes | EPA ENERGY STAR Certified Homes is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to upgrade a new home's energy efficiency beyond minimum code requirements. |
| EnerPHit | Enerphit | Super-insulated existing homes that have been remodeled to meet certification requirements demonstrating minimal or no heating and cooling system. |
| HERS Index Score | HersIndexScore | The HERS Index is a nationally recognized scoring system for measuring a home's energy performance in the U.S. |
| Home Energy Score | HomeEnergyScore | The Home Energy Score, managed by the U.S. |
| Home Energy Upgrade Certificate of Energy Efficiency Improvements | HomeEnergyUpgradeCertificateOfEnergyEfficiencyImprovements | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU). |
| Home Energy Upgrade Certificate of Energy Efficiency Performance | HomeEnergyUpgradeCertificateOfEnergyEfficiencyPerformance | Buildings Performance Institute BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades specifies a standard way of describing the improvements made to an existing home through a home energy upgrade (HEU) and provides one or more measures of a home's performance. |
| Home Performance with ENERGY STAR | HomePerformanceWithEnergyStar | Home Performance with ENERGY STAR (HPwES) offers whole-house solutions to high energy bills and homes with comfort problems. |
| Indoor airPLUS | IndoorAirplus | Indoor airPLUS from the U.S. |
| LEED For Homes | LeedForHomes | The U.S. |
| Living Building Challenge | LivingBuildingChallenge | The International Living Future Institute third-party certification that proves that a home produces as much or more energy than is used. |
| NGBS New Construction | NgbsNewConstruction | Home Innovation Research Labs certifies homes to the ICC-700 National Green Building Standard (NGBS), which has undergone the full consensus process and received approval from the American National Standards Institute (ANSI). |
| NGBS Small Projects Remodel | NgbsSmallProjectsRemodel | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| NGBS Whole-Home Remodel | NgbsWholeHomeRemodel | Home Innovation Research Labs provides project certification to the National Green Building Standard (NGBS). |
| PHIUS+ | PhiusPlus | Super-insulated homes that have met certification requirements demonstrating minimal or no heating and cooling system. |
| Pearl Certification | PearlCertification | Pearl is a national firm that provides third-party certification of high-performing homes (residential, 1-4 units) at various levels. |
| WaterSense | Watersense | EPA WaterSense is a set of optional construction practices and technologies (above minimum code requirements) that builders can follow to ensure a home uses less water while still providing the same level of comfort and convenience. |
| Zero Energy Ready Home | ZeroEnergyReadyHome | DOE Zero Energy Ready Home is a set of optional construction practices and technologies (above minimum code and ENERGY STAR Certified Home requirements) that builders can follow to ensure high-performance homes that are so energy efficient that all or most annual energy consumption can be offset with renewable energy. |

## green_energy_efficient

- Source name: `GreenEnergyEfficient`
- Kind: **closed-MV**
- Value count: 12
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenEnergyEfficient/)
- Used by:
  - `property.green_energy_efficient` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appliances | Appliances | For purposes of marketing, the property has appliances that have some green/efficient rating or quality. |
| Construction | Construction | For purposes of marketing, the property has construction that has some green/efficient rating or quality. |
| Doors | Doors | For purposes of marketing, the property has doors that have some green/efficient rating or quality. |
| Exposure/Shade | ExposureShade | For purposes of marketing, the property has exposure/shade that has some green/efficient rating or quality. |
| HVAC | Hvac | For purposes of marketing, the property has a heating, ventilation and air conditioning system that has some green/efficient rating or quality. |
| Incentives | Incentives | For purposes of marketing, the property has incentives that have some green/efficiency focus. |
| Insulation | Insulation | For purposes of marketing, the property has insulation that has some green/efficient rating or quality. |
| Lighting | Lighting | For purposes of marketing, the property has lighting that has some green/efficient rating or quality. |
| Roof | Roof | For purposes of marketing, the property has a roof that has some green/efficient rating or quality. |
| Thermostat | Thermostat | For purposes of marketing, the property has a thermostat or thermostats that have some green/efficient rating or quality. |
| Water Heater | WaterHeater | For purposes of marketing, the property has a water heater that has some green/efficient rating or quality. |
| Windows | Windows | For purposes of marketing, the property has windows that have some green/efficient rating or quality. |

## green_energy_generation

- Source name: `GreenEnergyGeneration`
- Kind: **closed-MV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenEnergyGeneration/)
- Used by:
  - `property.green_energy_generation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Solar | Solar | A renewable form of onsite power generation. |
| Wind | Wind | A renewable form of onsite power generation. |

## green_indoor_air_quality

- Source name: `GreenIndoorAirQuality`
- Kind: **closed-MV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenIndoorAirQuality/)
- Used by:
  - `property.green_indoor_air_quality` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Contaminant Control | ContaminantControl | The property has been carefully designed to prevent, monitor and suppress pollution issues. |
| Integrated Pest Management | IntegratedPestManagement | The property is designed for systematic management of pests that uses prevention, exclusion, monitoring and suppression. |
| Moisture Control | MoistureControl | Every foundation, roof, roofing component, exterior wall, door, skylight and window is designed and maintained to be watertight and free of persistent dampness or moisture. |
| Ventilation | Ventilation | Furnaces, water heaters, woodstoves and other devices that employ combustion-burning fuel are vented to the outside in a manner that meets manufacturer specifications to prevent back drafting. |

## green_location

- Source name: `GreenLocation`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenLocation/)
- Used by:
  - `property.green_location` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## green_sustainability

- Source name: `GreenSustainability`
- Kind: **closed-MV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenSustainability/)
- Used by:
  - `property.green_sustainability` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Conserving Methods | ConservingMethods | Construction is planned to require fewer materials while maintaining structural integrity and may include advanced wall framing as documented in several major green building programs. |
| Onsite Recycling Center | OnsiteRecyclingCenter | Property includes sufficient built-in storage space and/or containers for temporary storage of recyclable materials and/or compost collection. |
| Recyclable Materials | RecyclableMaterials | The structure includes multiple products that have a significant amount of postconsumer recycled content. |
| Recycled Materials | RecycledMaterials | The structure includes multiple products that have a significant amount of postconsumer recycled content. |
| Regionally-Sourced Materials | RegionallySourcedMaterials | Refers to building materials that were manufactured, extracted, harvested or recovered within 500 miles of the building. |
| Renewable Materials | RenewableMaterials | The structure includes materials that are naturally occurring, abundant and/or fast growing. |
| Salvaged Materials | SalvagedMaterials | The structure incorporates materials that were diverted from a landfill and/or sourced to give an otherwise unused item fresh use as an attached fixture. |

## green_verification_source

- Source name: `GreenVerificationSource`
- Kind: **closed-SV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenVerificationSource/)
- Used by:
  - `property_green_verification.green_verification_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Administrator | Administrator | An administrator such as a utility, governmental entity, etc. |
| Assessor | Assessor | The assessor provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Builder | Builder | The builder provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Contractor or Installer | ContractorOrInstaller | The contractor or installer provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Other | Other | Data such as photovoltaic characteristics, or a verified score, certification, label, etc. |
| Owner | Owner | The owner provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Program Sponsor | ProgramSponsor | The program sponsor provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Program Verifier | ProgramVerifier | The program verifier hired as a third-party provided data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| Public Records | PublicRecords | Data such as photovoltaic characteristics or a verified score, certification, label, etc. |
| See Remarks | SeeRemarks | See remarks for information about the source of data, such as photovoltaic characteristics or a verified score, certification, label, etc. |

## green_verification_status

- Source name: `GreenVerificationStatus`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenVerificationStatus/)
- Used by:
  - `property_green_verification.green_verification_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Complete | Complete | Indicates that the verification process is complete. |
| In Process | InProcess | Indicates that the verification process is underway but not complete. |

## green_water_conservation

- Source name: `GreenWaterConservation`
- Kind: **closed-MV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/GreenWaterConservation/)
- Used by:
  - `property.green_water_conservation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Efficient Hot Water Distribution | EfficientHotWaterDistribution | Efficient hot water distribution systems are designed to generate hot water using fewer fuel resources and to get hot water to low-flow faucets and fixtures more quickly. |
| Gray Water System | GrayWaterSystem | The property includes a gray water system. |
| Green Infrastructure | GreenInfrastructure | A set of strategies and specifically designed systems to manage stormwater runoff through a variety of small, cost-effective landscape features located on a property. |
| Low-Flow Fixtures | LowFlowFixtures | Toilets, bathroom faucets, showerheads, irrigation controllers and other products can be manufactured to use less water than minimum standards. |
| Water Recycling | WaterRecycling | The property includes a system to reuse stormwater via rain barrels or cisterns for landscaping or to treat and reuse water from bathroom sinks, showers and clothes washing drains for landscape irrigation and/or toilet flushing. |
| Water-Smart Landscaping | WaterSmartLandscaping | Water-smart landscapes are designed to require less water and fertilizer treatments. |

## heating

- Source name: `Heating`
- Kind: **closed-MV**
- Value count: 42
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Heating/)
- Used by:
  - `property.heating` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active Solar | ActiveSolar | Active solar heating systems use solar energy to heat a fluid - either liquid or air - and then transfer the solar heat directly to the interior space or to a storage system for later use. |
| Baseboard | Baseboard | Baseboard heating utilizes convection; as cold air drops from the window, it enters the baseboard heating unit where the air is warmed by heating elements, typically fins. |
| Ceiling | Ceiling | A heating unit that is installed into or upon the surface of the ceiling. |
| Central | Central | A system where heat is generated in one or more locations in the structure and distributed throughout the structure. |
| Coal | Coal | The heating system uses coal as its fuel to generate heat. |
| Coal Stove | CoalStove | A coal-burning stove that is used for heat. |
| Ductless | Ductless | The heating system does not have ducting like that found in forced-air systems. |
| ENERGY STAR Qualified Equipment | EnergyStarQualifiedEquipment | The heating system is ENERGY STAR qualified. |
| ENERGY STAR/ACCA RSI Qualified Installation | EnergyStarAccaRsiQualifiedInstallation | The heating system installation was done by a qualified ENERGY STAR or ACCA RSI contractor. |
| Electric | Electric | The heating system utilizes electricity and heating elements such as coils or fins to generate heat. |
| Exhaust Fan | ExhaustFan | The property has an exhaust fan. |
| Fireplace Insert | FireplaceInsert | The property has a fireplace insert for generating heat. |
| Fireplace(s) | Fireplaces | The property has one or more fireplaces used to generate heat. |
| Floor Furnace | FloorFurnace | The property has a radiant heating system that is mounted into the floor and distributes heat via convection. |
| Forced Air | ForcedAir | The property has a forced air system, typically via ducting throughout the structure. |
| Geothermal | Geothermal | A geothermal heating system, also known as a ground source heat pump, transfers heat from below ground into the structure. |
| Gravity | Gravity | A gravity heating system, also known as an octopus furnace, is typically a ducted system that doesn't use a fan but rather is designed to allow the heat to rise naturally through the ducts to different areas of the structure. |
| Heat Pump | HeatPump | A system that exchanges heat between a warm and cool space. |
| Hot Water | HotWater | The heating system uses a boiler and pipes to deliver hot water to radiators throughout the dwelling. |
| Humidity Control | HumidityControl | The heating system has humidity control. |
| Kerosene | Kerosene | The heating system uses kerosene as its fuel to generate heat. |
| Natural Gas | NaturalGas | The heating system uses natural gas as its fuel to generate heat. |
| None | None | The property does not have a heating system. |
| Oil | Oil | The heating system uses oil as its fuel to generate heat. |
| Other | Other | The property has a heating system or features that are not included on this list. |
| Passive Solar | PassiveSolar | Passive solar is a building design where the walls, windows, floors, etc., are made to collect heat and warm the dwelling. |
| Pellet Stove | PelletStove | The property has a stove that burns compressed wood or biomass pellets to generate heat. |
| Propane | Propane | The heating system uses propane as its fuel to generate heat. |
| Propane Stove | PropaneStove | The property has a stove that burns propane to generate heat. |
| Radiant | Radiant | The heating system uses radiators to release heat within the dwelling. |
| Radiant Ceiling | RadiantCeiling | The radiant heating element(s) are located in the ceiling. |
| Radiant Floor | RadiantFloor | The radiant heating element(s) are located in the floor. |
| See Remarks | SeeRemarks | See the remarks fields for additional information about the heating system included with the property. |
| Separate Meters | SeparateMeters | The heating system has multiple units and/or is zoned with separate meters for each zone/unit. |
| Solar | Solar | The property has a heating system or method that uses an unspecified type of solar heating. |
| Space Heater | SpaceHeater | The property comes with a stand-alone space heater. |
| Steam | Steam | The heating system uses a boiler and pipes to deliver hot water to radiators throughout the dwelling. |
| Varies by Unit | VariesByUnit | The type of heating or heating features vary from unit to unit. |
| Wall Furnace | WallFurnace | Typically a ductless system that is built into a wall to deliver to the room in which it's installed. |
| Wood | Wood | The heating system uses wood as its fuel to generate heat. |
| Wood Stove | WoodStove | The property has a stove that burns wood to generate heat. |
| Zoned | Zoned | The heating system is zoned, allowing for independent control of two or more parts of the structure. |

## high_school

- Source name: `HighSchool`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/HighSchool/)
- Used by:
  - `property.high_school` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## high_school_district

- Source name: `HighSchoolDistrict`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/HighSchoolDistrict/)
- Used by:
  - `property.high_school_district` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## horse_amenities

- Source name: `HorseAmenities`
- Kind: **closed-MV**
- Value count: 18
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/HorseAmenities/)
- Used by:
  - `property.horse_amenities` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Arena | Arena | The property allows for horses and has an arena. |
| Barn | Barn | The property allows horses and has a barn. |
| Boarding Facilities | BoardingFacilities | The property has boarding facilities for horses. |
| Corral(s) | Corrals | The property allows horses and has one or more corrals. |
| Hay Storage | HayStorage | The property allows horses and has hay storage. |
| None | None | The property either does not allow horses or has no amenities for horses. |
| Other | Other | The property has horse amenities other than those on this list. |
| Paddocks | Paddocks | The property allows horses and has an enclosed living are for them. |
| Palpation Chute | PalpationChute | A portion of the livestock chute where the animal is held for examination or other purposes. |
| Pasture | Pasture | The property includes or has access to a pasture for horses. |
| Riding Trail | RidingTrail | The property includes or has access to a riding trail or riding trails. |
| Round Pen | RoundPen | The property includes or has access to a round enclosure used for horse training. |
| See Remarks | SeeRemarks | See the remarks fields for additional information about horse amenities. |
| Shaving Bin | ShavingBin | The property includes or has access to a storage container for wood shavings that are used as ground cover for horses. |
| Stable(s) | Stables | The property includes or has access to a horse stable or stables. |
| Tack Room | TackRoom | The property includes or has access to a room to store equipment such as saddles, stirrups, bridles, halters, reins, bits, harnesses, martingales, breastplates, etc. |
| Trailer Storage | TrailerStorage | The property includes or has access to a place to store a horse trailer. |
| Wash Rack | WashRack | The property includes or has access to a rack used to confine/restrain a horse for purposes of washing the horse. |

## hours_days_of_operation

- Source name: `HoursDaysOfOperation`
- Kind: **closed-MV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/HoursDaysOfOperation/)
- Used by:
  - `property.hours_days_of_operation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Evenings Only | EveningsOnly | The business being sold is open in the evenings only. |
| Open -8 Hours/Day | OpenLessThan8HoursDay | The business being sold is open less than 8 hours per day. |
| Open 24 Hours | Open24Hours | The business being sold is open 24 hours per day. |
| Open 7 Days | Open7Days | The business being sold is open 7 days per week. |
| Open 8 Hours/Day | Open8HoursDay | The business being sold is open 8 hours per day. |
| Open 8+ Hours/Day | OpenOver8HoursDay | The business being sold is open more than 8 hours per day. |
| Open Monday-Friday | OpenMondayFriday | The business being sold is open Monday through Friday. |
| Open Saturday | OpenSaturday | The business being sold is open on Saturdays. |
| Open Sunday | OpenSunday | The business being sold is open on Sundays. |

## iana_time_zone_values

- Source name: `IanaTimeZoneValues`
- Kind: **closed-SV**
- Value count: 482
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/IanaTimeZoneValues/)
- Used by:
  - `lock_or_box.listing_time_zone` (type=`String List, Single`)
  - `property.property_time_zone_name` (type=`String List, Single`)
  - `showing.showing_time_zone` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Africa/Abidjan | AfricaAbidjan | The time zone is Africa/Abidjan in the IANA tz database. |
| Africa/Accra | AfricaAccra | The time zone formerly known as Africa/Accra is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Addis_Ababa | AfricaAddisAbaba | The time zone formerly known as Africa/Addis_Ababa is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Algiers | AfricaAlgiers | The time zone is Africa/Algiers in the IANA tz database. |
| Africa/Asmara | AfricaAsmara | The time zone formerly known as Africa/Asmara is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Asmera | AfricaAsmera | The time zone formerly known as Africa/Asmera is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Bamako | AfricaBamako | The time zone formerly known as Africa/Bamako is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Bangui | AfricaBangui | The time zone formerly known as Africa/Bangui is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Banjul | AfricaBanjul | The time zone formerly known as Africa/Banjul is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Bissau | AfricaBissau | The time zone is Africa/Bissau in the IANA tz database. |
| Africa/Blantyre | AfricaBlantyre | The time zone formerly known as Africa/Blantyre is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Brazzaville | AfricaBrazzaville | The time zone formerly known as Africa/Brazzaville is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Bujumbura | AfricaBujumbura | The time zone formerly known as Africa/Bujumbura is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Cairo | AfricaCairo | The time zone is Africa/Cairo in the IANA tz database. |
| Africa/Casablanca | AfricaCasablanca | The time zone is Africa/Casablanca in the IANA tz database. |
| Africa/Ceuta | AfricaCeuta | The time zone is Africa/Ceuta in the IANA tz database. |
| Africa/Conakry | AfricaConakry | The time zone formerly known as Africa/Conakry is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Dakar | AfricaDakar | The time zone formerly known as Africa/Dakar is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Dar_es_Salaam | AfricaDarEsSalaam | The time zone formerly known as Africa/Dar_es_Salaam is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Djibouti | AfricaDjibouti | The time zone formerly known as Africa/Djibouti is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Douala | AfricaDouala | The time zone formerly known as Africa/Douala is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/El_Aaiun | AfricaElAaiun | The time zone is Africa/El_Aaiun in the IANA tz database. |
| Africa/Freetown | AfricaFreetown | The time zone formerly known as Africa/Freetown is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Gaborone | AfricaGaborone | The time zone formerly known as Africa/Gaborone is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Harare | AfricaHarare | The time zone formerly known as Africa/Harare is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Johannesburg | AfricaJohannesburg | The time zone is Africa/Johannesburg in the IANA tz database. |
| Africa/Juba | AfricaJuba | The time zone is Africa/Juba in the IANA tz database. |
| Africa/Kampala | AfricaKampala | The time zone formerly known as Africa/Kampala is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Khartoum | AfricaKhartoum | The time zone is Africa/Khartoum in the IANA tz database. |
| Africa/Kigali | AfricaKigali | The time zone formerly known as Africa/Kigali is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Kinshasa | AfricaKinshasa | The time zone formerly known as Africa/Kinshasa is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Lagos | AfricaLagos | The time zone is Africa/Lagos in the IANA tz database. |
| Africa/Libreville | AfricaLibreville | The time zone formerly known as Africa/Libreville is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Lome | AfricaLome | The time zone formerly known as Africa/Lome is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Luanda | AfricaLuanda | The time zone formerly known as Africa/Luanda is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Lubumbashi | AfricaLubumbashi | The time zone formerly known as Africa/Lubumbashi is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Lusaka | AfricaLusaka | The time zone formerly known as Africa/Lusaka is now represented as Africa/Maputo in the IANA tz database for backwards compatibility. |
| Africa/Malabo | AfricaMalabo | The time zone formerly known as Africa/Malabo is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Maputo | AfricaMaputo | The time zone is Africa/Maputo in the IANA tz database. |
| Africa/Maseru | AfricaMaseru | The time zone formerly known as Africa/Maseru is now represented as Africa/Johannesburg in the IANA tz database for backwards compatibility. |
| Africa/Mbabane | AfricaMbabane | The time zone formerly known as Africa/Mbabane is now represented as Africa/Johannesburg in the IANA tz database for backwards compatibility. |
| Africa/Mogadishu | AfricaMogadishu | The time zone formerly known as Africa/Mogadishu is now represented as Africa/Nairobi in the IANA tz database for backwards compatibility. |
| Africa/Monrovia | AfricaMonrovia | The time zone is Africa/Monrovia in the IANA tz database. |
| Africa/Nairobi | AfricaNairobi | The time zone is Africa/Nairobi in the IANA tz database. |
| Africa/Ndjamena | AfricaNdjamena | The time zone is Africa/Ndjamena in the IANA tz database. |
| Africa/Niamey | AfricaNiamey | The time zone formerly known as Africa/Niamey is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Nouakchott | AfricaNouakchott | The time zone formerly known as Africa/Nouakchott is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Ouagadougou | AfricaOuagadougou | The time zone formerly known as Africa/Ouagadougou is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Porto-Novo | AfricaPortoNovo | The time zone formerly known as Africa/Porto-Novo is now represented as Africa/Lagos in the IANA tz database for backwards compatibility. |
| Africa/Sao_Tome | AfricaSaoTome | The time zone is Africa/Sao_Tome in the IANA tz database. |
| Africa/Timbuktu | AfricaTimbuktu | The time zone formerly known as Africa/Timbuktu is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Africa/Tripoli | AfricaTripoli | The time zone is Africa/Tripoli in the IANA tz database. |
| Africa/Tunis | AfricaTunis | The time zone is Africa/Tunis in the IANA tz database. |
| Africa/Windhoek | AfricaWindhoek | The time zone is Africa/Windhoek in the IANA tz database. |
| America/Adak | AmericaAdak | The time zone is America/Adak in the IANA tz database. |
| America/Anchorage | AmericaAnchorage | The time zone is America/Anchorage in the IANA tz database. |
| America/Anguilla | AmericaAnguilla | The time zone formerly known as America/Anguilla is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Antigua | AmericaAntigua | The time zone formerly known as America/Antigua is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Araguaina | AmericaAraguaina | The time zone is America/Araguaina in the IANA tz database. |
| America/Argentina/Buenos_Aires | AmericaArgentinaBuenosAires | The time zone is America/Argentina/Buenos_Aires in the IANA tz database. |
| America/Argentina/Catamarca | AmericaArgentinaCatamarca | The time zone is America/Argentina/Catamarca in the IANA tz database. |
| America/Argentina/ComodRivadavia | AmericaArgentinaComodRivadavia | The time zone formerly known as America/Argentina/ComodRivadavia is now represented as America/Argentina/Catamarca in the IANA tz database for backwards compatibility. |
| America/Argentina/Cordoba | AmericaArgentinaCordoba | The time zone is America/Argentina/Cordoba in the IANA tz database. |
| America/Argentina/Jujuy | AmericaArgentinaJujuy | The time zone is America/Argentina/Jujuy in the IANA tz database. |
| America/Argentina/La_Rioja | AmericaArgentinaLaRioja | The time zone is America/Argentina/La_Rioja in the IANA tz database. |
| America/Argentina/Mendoza | AmericaArgentinaMendoza | The time zone is America/Argentina/Mendoza in the IANA tz database. |
| America/Argentina/Rio_Gallegos | AmericaArgentinaRioGallegos | The time zone is America/Argentina/Rio_Gallegos in the IANA tz database. |
| America/Argentina/Salta | AmericaArgentinaSalta | The time zone is America/Argentina/Salta in the IANA tz database. |
| America/Argentina/San_Juan | AmericaArgentinaSanJuan | The time zone is America/Argentina/San_Juan in the IANA tz database. |
| America/Argentina/San_Luis | AmericaArgentinaSanLuis | The time zone is America/Argentina/San_Luis in the IANA tz database. |
| America/Argentina/Tucuman | AmericaArgentinaTucuman | The time zone is America/Argentina/Tucuman in the IANA tz database. |
| America/Argentina/Ushuaia | AmericaArgentinaUshuaia | The time zone is America/Argentina/Ushuaia in the IANA tz database. |
| America/Aruba | AmericaAruba | The time zone formerly known as America/Aruba is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Asuncion | AmericaAsuncion | The time zone is America/Asuncion in the IANA tz database. |
| America/Atikokan | AmericaAtikokan | The time zone formerly known as America/Atikokan is now represented as America/Panama in the IANA tz database for backwards compatibility. |
| America/Atka | AmericaAtka | The time zone formerly known as America/Atka is now represented as America/Adak in the IANA tz database for backwards compatibility. |
| America/Bahia | AmericaBahia | The time zone is America/Bahia in the IANA tz database. |
| America/Bahia_Banderas | AmericaBahiaBanderas | The time zone is America/Bahia_Banderas in the IANA tz database. |
| America/Barbados | AmericaBarbados | The time zone is America/Barbados in the IANA tz database. |
| America/Belem | AmericaBelem | The time zone is America/Belem in the IANA tz database. |
| America/Belize | AmericaBelize | The time zone is America/Belize in the IANA tz database. |
| America/Blanc-Sablon | AmericaBlancSablon | The time zone formerly known as America/Blanc-Sablon is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Boa_Vista | AmericaBoaVista | The time zone is America/Boa_Vista in the IANA tz database. |
| America/Bogota | AmericaBogota | The time zone is America/Bogota in the IANA tz database. |
| America/Boise | AmericaBoise | The time zone is America/Boise in the IANA tz database. |
| America/Buenos_Aires | AmericaBuenosAires | The time zone formerly known as America/Buenos_Aires is now represented as America/Argentina/Buenos_Aires in the IANA tz database for backwards compatibility. |
| America/Cambridge_Bay | AmericaCambridgeBay | The time zone is America/Cambridge_Bay in the IANA tz database. |
| America/Campo_Grande | AmericaCampoGrande | The time zone is America/Campo_Grande in the IANA tz database. |
| America/Cancun | AmericaCancun | The time zone is America/Cancun in the IANA tz database. |
| America/Caracas | AmericaCaracas | The time zone is America/Caracas in the IANA tz database. |
| America/Catamarca | AmericaCatamarca | The time zone formerly known as America/Catamarca is now represented as America/Argentina/Catamarca in the IANA tz database for backwards compatibility. |
| America/Cayenne | AmericaCayenne | The time zone is America/Cayenne in the IANA tz database. |
| America/Cayman | AmericaCayman | The time zone formerly known as America/Cayman is now represented as America/Panama in the IANA tz database for backwards compatibility. |
| America/Chicago | AmericaChicago | The time zone is America/Chicago in the IANA tz database. |
| America/Chihuahua | AmericaChihuahua | The time zone is America/Chihuahua in the IANA tz database. |
| America/Ciudad_Juarez | AmericaCiudadJuarez | The time zone is America/Ciudad_Juarez in the IANA tz database. |
| America/Coral_Harbour | AmericaCoralHarbour | The time zone formerly known as America/Coral_Harbour is now represented as America/Panama in the IANA tz database for backwards compatibility. |
| America/Cordoba | AmericaCordoba | The time zone formerly known as America/Cordoba is now represented as America/Argentina/Cordoba in the IANA tz database for backwards compatibility. |
| America/Costa_Rica | AmericaCostaRica | The time zone is America/Costa_Rica in the IANA tz database. |
| America/Coyhaique | AmericaCoyhaique | The time zone is America/Coyhaique in the IANA tz database. |
| America/Creston | AmericaCreston | The time zone formerly known as America/Creston is now represented as America/Phoenix in the IANA tz database for backwards compatibility. |
| America/Cuiaba | AmericaCuiaba | The time zone is America/Cuiaba in the IANA tz database. |
| America/Curacao | AmericaCuracao | The time zone formerly known as America/Curacao is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Danmarkshavn | AmericaDanmarkshavn | The time zone is America/Danmarkshavn in the IANA tz database. |
| America/Dawson | AmericaDawson | The time zone is America/Dawson in the IANA tz database. |
| America/Dawson_Creek | AmericaDawsonCreek | The time zone is America/Dawson_Creek in the IANA tz database. |
| America/Denver | AmericaDenver | The time zone is America/Denver in the IANA tz database. |
| America/Detroit | AmericaDetroit | The time zone is America/Detroit in the IANA tz database. |
| America/Dominica | AmericaDominica | The time zone formerly known as America/Dominica is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Edmonton | AmericaEdmonton | The time zone is America/Edmonton in the IANA tz database. |
| America/Eirunepe | AmericaEirunepe | The time zone is America/Eirunepe in the IANA tz database. |
| America/El_Salvador | AmericaElSalvador | The time zone is America/El_Salvador in the IANA tz database. |
| America/Ensenada | AmericaEnsenada | The time zone formerly known as America/Ensenada is now represented as America/Tijuana in the IANA tz database for backwards compatibility. |
| America/Fort_Nelson | AmericaFortNelson | The time zone is America/Fort_Nelson in the IANA tz database. |
| America/Fort_Wayne | AmericaFortWayne | The time zone formerly known as America/Fort_Wayne is now represented as America/Indiana/Indianapolis in the IANA tz database for backwards compatibility. |
| America/Fortaleza | AmericaFortaleza | The time zone is America/Fortaleza in the IANA tz database. |
| America/Glace_Bay | AmericaGlaceBay | The time zone is America/Glace_Bay in the IANA tz database. |
| America/Godthab | AmericaGodthab | The time zone formerly known as America/Godthab is now represented as America/Nuuk in the IANA tz database for backwards compatibility. |
| America/Goose_Bay | AmericaGooseBay | The time zone is America/Goose_Bay in the IANA tz database. |
| America/Grand_Turk | AmericaGrandTurk | The time zone is America/Grand_Turk in the IANA tz database. |
| America/Grenada | AmericaGrenada | The time zone formerly known as America/Grenada is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Guadeloupe | AmericaGuadeloupe | The time zone formerly known as America/Guadeloupe is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Guatemala | AmericaGuatemala | The time zone is America/Guatemala in the IANA tz database. |
| America/Guayaquil | AmericaGuayaquil | The time zone is America/Guayaquil in the IANA tz database. |
| America/Guyana | AmericaGuyana | The time zone is America/Guyana in the IANA tz database. |
| America/Halifax | AmericaHalifax | The time zone is America/Halifax in the IANA tz database. |
| America/Havana | AmericaHavana | The time zone is America/Havana in the IANA tz database. |
| America/Hermosillo | AmericaHermosillo | The time zone is America/Hermosillo in the IANA tz database. |
| America/Indiana/Indianapolis | AmericaIndianaIndianapolis | The time zone is America/Indiana/Indianapolis in the IANA tz database. |
| America/Indiana/Knox | AmericaIndianaKnox | The time zone is America/Indiana/Knox in the IANA tz database. |
| America/Indiana/Marengo | AmericaIndianaMarengo | The time zone is America/Indiana/Marengo in the IANA tz database. |
| America/Indiana/Petersburg | AmericaIndianaPetersburg | The time zone is America/Indiana/Petersburg in the IANA tz database. |
| America/Indiana/Tell_City | AmericaIndianaTellCity | The time zone is America/Indiana/Tell_City in the IANA tz database. |
| America/Indiana/Vevay | AmericaIndianaVevay | The time zone is America/Indiana/Vevay in the IANA tz database. |
| America/Indiana/Vincennes | AmericaIndianaVincennes | The time zone is America/Indiana/Vincennes in the IANA tz database. |
| America/Indiana/Winamac | AmericaIndianaWinamac | The time zone is America/Indiana/Winamac in the IANA tz database. |
| America/Indianapolis | AmericaIndianapolis | The time zone formerly known as America/Indianapolis is now represented as America/Indiana/Indianapolis in the IANA tz database for backwards compatibility. |
| America/Inuvik | AmericaInuvik | The time zone is America/Inuvik in the IANA tz database. |
| America/Iqaluit | AmericaIqaluit | The time zone is America/Iqaluit in the IANA tz database. |
| America/Jamaica | AmericaJamaica | The time zone is America/Jamaica in the IANA tz database. |
| America/Jujuy | AmericaJujuy | The time zone formerly known as America/Jujuy is now represented as America/Argentina/Jujuy in the IANA tz database for backwards compatibility. |
| America/Juneau | AmericaJuneau | The time zone is America/Juneau in the IANA tz database. |
| America/Kentucky/Louisville | AmericaKentuckyLouisville | The time zone is America/Kentucky/Louisville in the IANA tz database. |
| America/Kentucky/Monticello | AmericaKentuckyMonticello | The time zone is America/Kentucky/Monticello in the IANA tz database. |
| America/Knox_IN | AmericaKnoxIN | The time zone formerly known as America/Knox_IN is now represented as America/Indiana/Knox in the IANA tz database for backwards compatibility. |
| America/Kralendijk | AmericaKralendijk | The time zone formerly known as America/Kralendijk is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/La_Paz | AmericaLaPaz | The time zone is America/La_Paz in the IANA tz database. |
| America/Lima | AmericaLima | The time zone is America/Lima in the IANA tz database. |
| America/Los_Angeles | AmericaLosAngeles | The time zone is America/Los_Angeles in the IANA tz database. |
| America/Louisville | AmericaLouisville | The time zone formerly known as America/Louisville is now represented as America/Kentucky/Louisville in the IANA tz database for backwards compatibility. |
| America/Lower_Princes | AmericaLowerPrinces | The time zone formerly known as America/Lower_Princes is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Maceio | AmericaMaceio | The time zone is America/Maceio in the IANA tz database. |
| America/Managua | AmericaManagua | The time zone is America/Managua in the IANA tz database. |
| America/Manaus | AmericaManaus | The time zone is America/Manaus in the IANA tz database. |
| America/Marigot | AmericaMarigot | The time zone formerly known as America/Marigot is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Martinique | AmericaMartinique | The time zone is America/Martinique in the IANA tz database. |
| America/Matamoros | AmericaMatamoros | The time zone is America/Matamoros in the IANA tz database. |
| America/Mazatlan | AmericaMazatlan | The time zone is America/Mazatlan in the IANA tz database. |
| America/Mendoza | AmericaMendoza | The time zone formerly known as America/Mendoza is now represented as America/Argentina/Mendoza in the IANA tz database for backwards compatibility. |
| America/Menominee | AmericaMenominee | The time zone is America/Menominee in the IANA tz database. |
| America/Merida | AmericaMerida | The time zone is America/Merida in the IANA tz database. |
| America/Metlakatla | AmericaMetlakatla | The time zone is America/Metlakatla in the IANA tz database. |
| America/Mexico_City | AmericaMexicoCity | The time zone is America/Mexico_City in the IANA tz database. |
| America/Miquelon | AmericaMiquelon | The time zone is America/Miquelon in the IANA tz database. |
| America/Moncton | AmericaMoncton | The time zone is America/Moncton in the IANA tz database. |
| America/Monterrey | AmericaMonterrey | The time zone is America/Monterrey in the IANA tz database. |
| America/Montevideo | AmericaMontevideo | The time zone is America/Montevideo in the IANA tz database. |
| America/Montreal | AmericaMontreal | The time zone formerly known as America/Montreal is now represented as America/Toronto in the IANA tz database for backwards compatibility. |
| America/Montserrat | AmericaMontserrat | The time zone formerly known as America/Montserrat is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Nassau | AmericaNassau | The time zone formerly known as America/Nassau is now represented as America/Toronto in the IANA tz database for backwards compatibility. |
| America/New_York | AmericaNewYork | The time zone is America/New_York in the IANA tz database. |
| America/Nipigon | AmericaNipigon | The time zone formerly known as America/Nipigon is now represented as America/Toronto in the IANA tz database for backwards compatibility. |
| America/Nome | AmericaNome | The time zone is America/Nome in the IANA tz database. |
| America/Noronha | AmericaNoronha | The time zone is America/Noronha in the IANA tz database. |
| America/North_Dakota/Beulah | AmericaNorthDakotaBeulah | The time zone is America/North_Dakota/Beulah in the IANA tz database. |
| America/North_Dakota/Center | AmericaNorthDakotaCenter | The time zone is America/North_Dakota/Center in the IANA tz database. |
| America/North_Dakota/New_Salem | AmericaNorthDakotaNewSalem | The time zone is America/North_Dakota/New_Salem in the IANA tz database. |
| America/Nuuk | AmericaNuuk | The time zone is America/Nuuk in the IANA tz database. |
| America/Ojinaga | AmericaOjinaga | The time zone is America/Ojinaga in the IANA tz database. |
| America/Panama | AmericaPanama | The time zone is America/Panama in the IANA tz database. |
| America/Pangnirtung | AmericaPangnirtung | The time zone formerly known as America/Pangnirtung is now represented as America/Iqaluit in the IANA tz database for backwards compatibility. |
| America/Paramaribo | AmericaParamaribo | The time zone is America/Paramaribo in the IANA tz database. |
| America/Phoenix | AmericaPhoenix | The time zone is America/Phoenix in the IANA tz database. |
| America/Port-au-Prince | AmericaPortAuPrince | The time zone is America/Port-au-Prince in the IANA tz database. |
| America/Port_of_Spain | AmericaPortOfSpain | The time zone formerly known as America/Port_of_Spain is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Porto_Acre | AmericaPortoAcre | The time zone formerly known as America/Porto_Acre is now represented as America/Rio_Branco in the IANA tz database for backwards compatibility. |
| America/Porto_Velho | AmericaPortoVelho | The time zone is America/Porto_Velho in the IANA tz database. |
| America/Puerto_Rico | AmericaPuertoRico | The time zone is America/Puerto_Rico in the IANA tz database. |
| America/Punta_Arenas | AmericaPuntaArenas | The time zone is America/Punta_Arenas in the IANA tz database. |
| America/Rainy_River | AmericaRainyRiver | The time zone formerly known as America/Rainy_River is now represented as America/Winnipeg in the IANA tz database for backwards compatibility. |
| America/Rankin_Inlet | AmericaRankinInlet | The time zone is America/Rankin_Inlet in the IANA tz database. |
| America/Recife | AmericaRecife | The time zone is America/Recife in the IANA tz database. |
| America/Regina | AmericaRegina | The time zone is America/Regina in the IANA tz database. |
| America/Resolute | AmericaResolute | The time zone is America/Resolute in the IANA tz database. |
| America/Rio_Branco | AmericaRioBranco | The time zone is America/Rio_Branco in the IANA tz database. |
| America/Rosario | AmericaRosario | The time zone formerly known as America/Rosario is now represented as America/Argentina/Cordoba in the IANA tz database for backwards compatibility. |
| America/Santa_Isabel | AmericaSantaIsabel | The time zone formerly known as America/Santa_Isabel is now represented as America/Tijuana in the IANA tz database for backwards compatibility. |
| America/Santarem | AmericaSantarem | The time zone is America/Santarem in the IANA tz database. |
| America/Santiago | AmericaSantiago | The time zone is America/Santiago in the IANA tz database. |
| America/Santo_Domingo | AmericaSantoDomingo | The time zone is America/Santo_Domingo in the IANA tz database. |
| America/Sao_Paulo | AmericaSaoPaulo | The time zone is America/Sao_Paulo in the IANA tz database. |
| America/Scoresbysund | AmericaScoresbysund | The time zone is America/Scoresbysund in the IANA tz database. |
| America/Shiprock | AmericaShiprock | The time zone formerly known as America/Shiprock is now represented as America/Denver in the IANA tz database for backwards compatibility. |
| America/Sitka | AmericaSitka | The time zone is America/Sitka in the IANA tz database. |
| America/St_Barthelemy | AmericaStBarthelemy | The time zone formerly known as America/St_Barthelemy is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/St_Johns | AmericaStJohns | The time zone is America/St_Johns in the IANA tz database. |
| America/St_Kitts | AmericaStKitts | The time zone formerly known as America/St_Kitts is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/St_Lucia | AmericaStLucia | The time zone formerly known as America/St_Lucia is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/St_Thomas | AmericaStThomas | The time zone formerly known as America/St_Thomas is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/St_Vincent | AmericaStVincent | The time zone formerly known as America/St_Vincent is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Swift_Current | AmericaSwiftCurrent | The time zone is America/Swift_Current in the IANA tz database. |
| America/Tegucigalpa | AmericaTegucigalpa | The time zone is America/Tegucigalpa in the IANA tz database. |
| America/Thule | AmericaThule | The time zone is America/Thule in the IANA tz database. |
| America/Thunder_Bay | AmericaThunderBay | The time zone formerly known as America/Thunder_Bay is now represented as America/Toronto in the IANA tz database for backwards compatibility. |
| America/Tijuana | AmericaTijuana | The time zone is America/Tijuana in the IANA tz database. |
| America/Toronto | AmericaToronto | The time zone is America/Toronto in the IANA tz database. |
| America/Tortola | AmericaTortola | The time zone formerly known as America/Tortola is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Vancouver | AmericaVancouver | The time zone is America/Vancouver in the IANA tz database. |
| America/Virgin | AmericaVirgin | The time zone formerly known as America/Virgin is now represented as America/Puerto_Rico in the IANA tz database for backwards compatibility. |
| America/Whitehorse | AmericaWhitehorse | The time zone is America/Whitehorse in the IANA tz database. |
| America/Winnipeg | AmericaWinnipeg | The time zone is America/Winnipeg in the IANA tz database. |
| America/Yakutat | AmericaYakutat | The time zone is America/Yakutat in the IANA tz database. |
| America/Yellowknife | AmericaYellowknife | The time zone formerly known as America/Yellowknife is now represented as America/Edmonton in the IANA tz database for backwards compatibility. |
| Antarctica/Casey | AntarcticaCasey | The time zone is Antarctica/Casey in the IANA tz database. |
| Antarctica/Davis | AntarcticaDavis | The time zone is Antarctica/Davis in the IANA tz database. |
| Antarctica/DumontDUrville | AntarcticaDumontDUrville | The time zone formerly known as Antarctica/DumontDUrville is now represented as Pacific/Port_Moresby in the IANA tz database for backwards compatibility. |
| Antarctica/Macquarie | AntarcticaMacquarie | The time zone is Antarctica/Macquarie in the IANA tz database. |
| Antarctica/Mawson | AntarcticaMawson | The time zone is Antarctica/Mawson in the IANA tz database. |
| Antarctica/McMurdo | AntarcticaMcMurdo | The time zone formerly known as Antarctica/McMurdo is now represented as Pacific/Auckland in the IANA tz database for backwards compatibility. |
| Antarctica/Palmer | AntarcticaPalmer | The time zone is Antarctica/Palmer in the IANA tz database. |
| Antarctica/Rothera | AntarcticaRothera | The time zone is Antarctica/Rothera in the IANA tz database. |
| Antarctica/South_Pole | AntarcticaSouthPole | The time zone formerly known as Antarctica/South_Pole is now represented as Pacific/Auckland in the IANA tz database for backwards compatibility. |
| Antarctica/Syowa | AntarcticaSyowa | The time zone formerly known as Antarctica/Syowa is now represented as Asia/Riyadh in the IANA tz database for backwards compatibility. |
| Antarctica/Troll | AntarcticaTroll | The time zone is Antarctica/Troll in the IANA tz database. |
| Antarctica/Vostok | AntarcticaVostok | The time zone is Antarctica/Vostok in the IANA tz database. |
| Arctic/Longyearbyen | ArcticLongyearbyen | The time zone formerly known as Arctic/Longyearbyen is now represented as Europe/Berlin in the IANA tz database for backwards compatibility. |
| Asia/Aden | AsiaAden | The time zone formerly known as Asia/Aden is now represented as Asia/Riyadh in the IANA tz database for backwards compatibility. |
| Asia/Almaty | AsiaAlmaty | The time zone is Asia/Almaty in the IANA tz database. |
| Asia/Amman | AsiaAmman | The time zone is Asia/Amman in the IANA tz database. |
| Asia/Anadyr | AsiaAnadyr | The time zone is Asia/Anadyr in the IANA tz database. |
| Asia/Aqtau | AsiaAqtau | The time zone is Asia/Aqtau in the IANA tz database. |
| Asia/Aqtobe | AsiaAqtobe | The time zone is Asia/Aqtobe in the IANA tz database. |
| Asia/Ashgabat | AsiaAshgabat | The time zone is Asia/Ashgabat in the IANA tz database. |
| Asia/Ashkhabad | AsiaAshkhabad | The time zone formerly known as Asia/Ashkhabad is now represented as Asia/Ashgabat in the IANA tz database for backwards compatibility. |
| Asia/Atyrau | AsiaAtyrau | The time zone is Asia/Atyrau in the IANA tz database. |
| Asia/Baghdad | AsiaBaghdad | The time zone is Asia/Baghdad in the IANA tz database. |
| Asia/Bahrain | AsiaBahrain | The time zone formerly known as Asia/Bahrain is now represented as Asia/Qatar in the IANA tz database for backwards compatibility. |
| Asia/Baku | AsiaBaku | The time zone is Asia/Baku in the IANA tz database. |
| Asia/Bangkok | AsiaBangkok | The time zone is Asia/Bangkok in the IANA tz database. |
| Asia/Barnaul | AsiaBarnaul | The time zone is Asia/Barnaul in the IANA tz database. |
| Asia/Beirut | AsiaBeirut | The time zone is Asia/Beirut in the IANA tz database. |
| Asia/Bishkek | AsiaBishkek | The time zone is Asia/Bishkek in the IANA tz database. |
| Asia/Brunei | AsiaBrunei | The time zone formerly known as Asia/Brunei is now represented as Asia/Kuching in the IANA tz database for backwards compatibility. |
| Asia/Calcutta | AsiaCalcutta | The time zone formerly known as Asia/Calcutta is now represented as Asia/Kolkata in the IANA tz database for backwards compatibility. |
| Asia/Chita | AsiaChita | The time zone is Asia/Chita in the IANA tz database. |
| Asia/Choibalsan | AsiaChoibalsan | The time zone formerly known as Asia/Choibalsan is now represented as Asia/Ulaanbaatar in the IANA tz database for backwards compatibility. |
| Asia/Chongqing | AsiaChongqing | The time zone formerly known as Asia/Chongqing is now represented as Asia/Shanghai in the IANA tz database for backwards compatibility. |
| Asia/Chungking | AsiaChungking | The time zone formerly known as Asia/Chungking is now represented as Asia/Shanghai in the IANA tz database for backwards compatibility. |
| Asia/Colombo | AsiaColombo | The time zone is Asia/Colombo in the IANA tz database. |
| Asia/Dacca | AsiaDacca | The time zone formerly known as Asia/Dacca is now represented as Asia/Dhaka in the IANA tz database for backwards compatibility. |
| Asia/Damascus | AsiaDamascus | The time zone is Asia/Damascus in the IANA tz database. |
| Asia/Dhaka | AsiaDhaka | The time zone is Asia/Dhaka in the IANA tz database. |
| Asia/Dili | AsiaDili | The time zone is Asia/Dili in the IANA tz database. |
| Asia/Dubai | AsiaDubai | The time zone is Asia/Dubai in the IANA tz database. |
| Asia/Dushanbe | AsiaDushanbe | The time zone is Asia/Dushanbe in the IANA tz database. |
| Asia/Famagusta | AsiaFamagusta | The time zone is Asia/Famagusta in the IANA tz database. |
| Asia/Gaza | AsiaGaza | The time zone is Asia/Gaza in the IANA tz database. |
| Asia/Harbin | AsiaHarbin | The time zone formerly known as Asia/Harbin is now represented as Asia/Shanghai in the IANA tz database for backwards compatibility. |
| Asia/Hebron | AsiaHebron | The time zone is Asia/Hebron in the IANA tz database. |
| Asia/Ho_Chi_Minh | AsiaHoChiMinh | The time zone is Asia/Ho_Chi_Minh in the IANA tz database. |
| Asia/Hong_Kong | AsiaHongKong | The time zone is Asia/Hong_Kong in the IANA tz database. |
| Asia/Hovd | AsiaHovd | The time zone is Asia/Hovd in the IANA tz database. |
| Asia/Irkutsk | AsiaIrkutsk | The time zone is Asia/Irkutsk in the IANA tz database. |
| Asia/Istanbul | AsiaIstanbul | The time zone formerly known as Asia/Istanbul is now represented as Europe/Istanbul in the IANA tz database for backwards compatibility. |
| Asia/Jakarta | AsiaJakarta | The time zone is Asia/Jakarta in the IANA tz database. |
| Asia/Jayapura | AsiaJayapura | The time zone is Asia/Jayapura in the IANA tz database. |
| Asia/Jerusalem | AsiaJerusalem | The time zone is Asia/Jerusalem in the IANA tz database. |
| Asia/Kabul | AsiaKabul | The time zone is Asia/Kabul in the IANA tz database. |
| Asia/Kamchatka | AsiaKamchatka | The time zone is Asia/Kamchatka in the IANA tz database. |
| Asia/Karachi | AsiaKarachi | The time zone is Asia/Karachi in the IANA tz database. |
| Asia/Kashgar | AsiaKashgar | The time zone formerly known as Asia/Kashgar is now represented as Asia/Urumqi in the IANA tz database for backwards compatibility. |
| Asia/Kathmandu | AsiaKathmandu | The time zone is Asia/Kathmandu in the IANA tz database. |
| Asia/Katmandu | AsiaKatmandu | The time zone formerly known as Asia/Katmandu is now represented as Asia/Kathmandu in the IANA tz database for backwards compatibility. |
| Asia/Khandyga | AsiaKhandyga | The time zone is Asia/Khandyga in the IANA tz database. |
| Asia/Kolkata | AsiaKolkata | The time zone is Asia/Kolkata in the IANA tz database. |
| Asia/Krasnoyarsk | AsiaKrasnoyarsk | The time zone is Asia/Krasnoyarsk in the IANA tz database. |
| Asia/Kuala_Lumpur | AsiaKualaLumpur | The time zone formerly known as Asia/Kuala_Lumpur is now represented as Asia/Singapore in the IANA tz database for backwards compatibility. |
| Asia/Kuching | AsiaKuching | The time zone is Asia/Kuching in the IANA tz database. |
| Asia/Kuwait | AsiaKuwait | The time zone formerly known as Asia/Kuwait is now represented as Asia/Riyadh in the IANA tz database for backwards compatibility. |
| Asia/Macao | AsiaMacao | The time zone formerly known as Asia/Macao is now represented as Asia/Macau in the IANA tz database for backwards compatibility. |
| Asia/Macau | AsiaMacau | The time zone is Asia/Macau in the IANA tz database. |
| Asia/Magadan | AsiaMagadan | The time zone is Asia/Magadan in the IANA tz database. |
| Asia/Makassar | AsiaMakassar | The time zone is Asia/Makassar in the IANA tz database. |
| Asia/Manila | AsiaManila | The time zone is Asia/Manila in the IANA tz database. |
| Asia/Muscat | AsiaMuscat | The time zone formerly known as Asia/Muscat is now represented as Asia/Dubai in the IANA tz database for backwards compatibility. |
| Asia/Nicosia | AsiaNicosia | The time zone is Asia/Nicosia in the IANA tz database. |
| Asia/Novokuznetsk | AsiaNovokuznetsk | The time zone is Asia/Novokuznetsk in the IANA tz database. |
| Asia/Novosibirsk | AsiaNovosibirsk | The time zone is Asia/Novosibirsk in the IANA tz database. |
| Asia/Omsk | AsiaOmsk | The time zone is Asia/Omsk in the IANA tz database. |
| Asia/Oral | AsiaOral | The time zone is Asia/Oral in the IANA tz database. |
| Asia/Phnom_Penh | AsiaPhnomPenh | The time zone formerly known as Asia/Phnom_Penh is now represented as Asia/Bangkok in the IANA tz database for backwards compatibility. |
| Asia/Pontianak | AsiaPontianak | The time zone is Asia/Pontianak in the IANA tz database. |
| Asia/Pyongyang | AsiaPyongyang | The time zone is Asia/Pyongyang in the IANA tz database. |
| Asia/Qatar | AsiaQatar | The time zone is Asia/Qatar in the IANA tz database. |
| Asia/Qostanay | AsiaQostanay | The time zone is Asia/Qostanay in the IANA tz database. |
| Asia/Qyzylorda | AsiaQyzylorda | The time zone is Asia/Qyzylorda in the IANA tz database. |
| Asia/Rangoon | AsiaRangoon | The time zone formerly known as Asia/Rangoon is now represented as Asia/Yangon in the IANA tz database for backwards compatibility. |
| Asia/Riyadh | AsiaRiyadh | The time zone is Asia/Riyadh in the IANA tz database. |
| Asia/Saigon | AsiaSaigon | The time zone formerly known as Asia/Saigon is now represented as Asia/Ho_Chi_Minh in the IANA tz database for backwards compatibility. |
| Asia/Sakhalin | AsiaSakhalin | The time zone is Asia/Sakhalin in the IANA tz database. |
| Asia/Samarkand | AsiaSamarkand | The time zone is Asia/Samarkand in the IANA tz database. |
| Asia/Seoul | AsiaSeoul | The time zone is Asia/Seoul in the IANA tz database. |
| Asia/Shanghai | AsiaShanghai | The time zone is Asia/Shanghai in the IANA tz database. |
| Asia/Singapore | AsiaSingapore | The time zone is Asia/Singapore in the IANA tz database. |
| Asia/Srednekolymsk | AsiaSrednekolymsk | The time zone is Asia/Srednekolymsk in the IANA tz database. |
| Asia/Taipei | AsiaTaipei | The time zone is Asia/Taipei in the IANA tz database. |
| Asia/Tashkent | AsiaTashkent | The time zone is Asia/Tashkent in the IANA tz database. |
| Asia/Tbilisi | AsiaTbilisi | The time zone is Asia/Tbilisi in the IANA tz database. |
| Asia/Tehran | AsiaTehran | The time zone is Asia/Tehran in the IANA tz database. |
| Asia/Tel_Aviv | AsiaTelAviv | The time zone formerly known as Asia/Tel_Aviv is now represented as Asia/Jerusalem in the IANA tz database for backwards compatibility. |
| Asia/Thimbu | AsiaThimbu | The time zone formerly known as Asia/Thimbu is now represented as Asia/Thimphu in the IANA tz database for backwards compatibility. |
| Asia/Thimphu | AsiaThimphu | The time zone is Asia/Thimphu in the IANA tz database. |
| Asia/Tokyo | AsiaTokyo | The time zone is Asia/Tokyo in the IANA tz database. |
| Asia/Tomsk | AsiaTomsk | The time zone is Asia/Tomsk in the IANA tz database. |
| Asia/Ujung_Pandang | AsiaUjungPandang | The time zone formerly known as Asia/Ujung_Pandang is now represented as Asia/Makassar in the IANA tz database for backwards compatibility. |
| Asia/Ulaanbaatar | AsiaUlaanbaatar | The time zone is Asia/Ulaanbaatar in the IANA tz database. |
| Asia/Ulan_Bator | AsiaUlanBator | The time zone formerly known as Asia/Ulan_Bator is now represented as Asia/Ulaanbaatar in the IANA tz database for backwards compatibility. |
| Asia/Urumqi | AsiaUrumqi | The time zone is Asia/Urumqi in the IANA tz database. |
| Asia/Ust-Nera | AsiaUstNera | The time zone is Asia/Ust-Nera in the IANA tz database. |
| Asia/Vientiane | AsiaVientiane | The time zone formerly known as Asia/Vientiane is now represented as Asia/Bangkok in the IANA tz database for backwards compatibility. |
| Asia/Vladivostok | AsiaVladivostok | The time zone is Asia/Vladivostok in the IANA tz database. |
| Asia/Yakutsk | AsiaYakutsk | The time zone is Asia/Yakutsk in the IANA tz database. |
| Asia/Yangon | AsiaYangon | The time zone is Asia/Yangon in the IANA tz database. |
| Asia/Yekaterinburg | AsiaYekaterinburg | The time zone is Asia/Yekaterinburg in the IANA tz database. |
| Asia/Yerevan | AsiaYerevan | The time zone is Asia/Yerevan in the IANA tz database. |
| Atlantic/Azores | AtlanticAzores | The time zone is Atlantic/Azores in the IANA tz database. |
| Atlantic/Bermuda | AtlanticBermuda | The time zone is Atlantic/Bermuda in the IANA tz database. |
| Atlantic/Canary | AtlanticCanary | The time zone is Atlantic/Canary in the IANA tz database. |
| Atlantic/Cape_Verde | AtlanticCapeVerde | The time zone is Atlantic/Cape_Verde in the IANA tz database. |
| Atlantic/Faeroe | AtlanticFaeroe | The time zone formerly known as Atlantic/Faeroe is now represented as Atlantic/Faroe in the IANA tz database for backwards compatibility. |
| Atlantic/Faroe | AtlanticFaroe | The time zone is Atlantic/Faroe in the IANA tz database. |
| Atlantic/Jan_Mayen | AtlanticJanMayen | The time zone formerly known as Atlantic/Jan_Mayen is now represented as Europe/Berlin in the IANA tz database for backwards compatibility. |
| Atlantic/Madeira | AtlanticMadeira | The time zone is Atlantic/Madeira in the IANA tz database. |
| Atlantic/Reykjavik | AtlanticReykjavik | The time zone formerly known as Atlantic/Reykjavik is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Atlantic/South_Georgia | AtlanticSouthGeorgia | The time zone is Atlantic/South_Georgia in the IANA tz database. |
| Atlantic/St_Helena | AtlanticStHelena | The time zone formerly known as Atlantic/St_Helena is now represented as Africa/Abidjan in the IANA tz database for backwards compatibility. |
| Atlantic/Stanley | AtlanticStanley | The time zone is Atlantic/Stanley in the IANA tz database. |
| Australia/ACT | AustraliaACT | The time zone formerly known as Australia/ACT is now represented as Australia/Sydney in the IANA tz database for backwards compatibility. |
| Australia/Adelaide | AustraliaAdelaide | The time zone is Australia/Adelaide in the IANA tz database. |
| Australia/Brisbane | AustraliaBrisbane | The time zone is Australia/Brisbane in the IANA tz database. |
| Australia/Broken_Hill | AustraliaBrokenHill | The time zone is Australia/Broken_Hill in the IANA tz database. |
| Australia/Canberra | AustraliaCanberra | The time zone formerly known as Australia/Canberra is now represented as Australia/Sydney in the IANA tz database for backwards compatibility. |
| Australia/Currie | AustraliaCurrie | The time zone formerly known as Australia/Currie is now represented as Australia/Hobart in the IANA tz database for backwards compatibility. |
| Australia/Darwin | AustraliaDarwin | The time zone is Australia/Darwin in the IANA tz database. |
| Australia/Eucla | AustraliaEucla | The time zone is Australia/Eucla in the IANA tz database. |
| Australia/Hobart | AustraliaHobart | The time zone is Australia/Hobart in the IANA tz database. |
| Australia/LHI | AustraliaLhi | The time zone formerly known as Australia/LHI is now represented as Australia/Lord_Howe in the IANA tz database for backwards compatibility. |
| Australia/Lindeman | AustraliaLindeman | The time zone is Australia/Lindeman in the IANA tz database. |
| Australia/Lord_Howe | AustraliaLordHowe | The time zone is Australia/Lord_Howe in the IANA tz database. |
| Australia/Melbourne | AustraliaMelbourne | The time zone is Australia/Melbourne in the IANA tz database. |
| Australia/NSW | AustraliaNsw | The time zone formerly known as Australia/NSW is now represented as Australia/Sydney in the IANA tz database for backwards compatibility. |
| Australia/North | AustraliaNorth | The time zone formerly known as Australia/North is now represented as Australia/Darwin in the IANA tz database for backwards compatibility. |
| Australia/Perth | AustraliaPerth | The time zone is Australia/Perth in the IANA tz database. |
| Australia/Queensland | AustraliaQueensland | The time zone formerly known as Australia/Queensland is now represented as Australia/Brisbane in the IANA tz database for backwards compatibility. |
| Australia/South | AustraliaSouth | The time zone formerly known as Australia/South is now represented as Australia/Adelaide in the IANA tz database for backwards compatibility. |
| Australia/Sydney | AustraliaSydney | The time zone is Australia/Sydney in the IANA tz database. |
| Australia/Tasmania | AustraliaTasmania | The time zone formerly known as Australia/Tasmania is now represented as Australia/Hobart in the IANA tz database for backwards compatibility. |
| Australia/Victoria | AustraliaVictoria | The time zone formerly known as Australia/Victoria is now represented as Australia/Melbourne in the IANA tz database for backwards compatibility. |
| Australia/West | AustraliaWest | The time zone formerly known as Australia/West is now represented as Australia/Perth in the IANA tz database for backwards compatibility. |
| Australia/Yancowinna | AustraliaYancowinna | The time zone formerly known as Australia/Yancowinna is now represented as Australia/Broken_Hill in the IANA tz database for backwards compatibility. |
| Brazil/Acre | BrazilAcre | The time zone formerly known as Brazil/Acre is now represented as America/Rio_Branco in the IANA tz database for backwards compatibility. |
| Brazil/DeNoronha | BrazilDeNoronha | The time zone formerly known as Brazil/DeNoronha is now represented as America/Noronha in the IANA tz database for backwards compatibility. |
| Brazil/East | BrazilEast | The time zone formerly known as Brazil/East is now represented as America/Sao_Paulo in the IANA tz database for backwards compatibility. |
| Brazil/West | BrazilWest | The time zone formerly known as Brazil/West is now represented as America/Manaus in the IANA tz database for backwards compatibility. |
| Canada/Atlantic | CanadaAtlantic | The time zone formerly known as Canada/Atlantic is now represented as America/Halifax in the IANA tz database for backwards compatibility. |
| Canada/Central | CanadaCentral | The time zone formerly known as Canada/Central is now represented as America/Winnipeg in the IANA tz database for backwards compatibility. |
| Canada/Eastern | CanadaEastern | The time zone formerly known as Canada/Eastern is now represented as America/Toronto in the IANA tz database for backwards compatibility. |
| Canada/Mountain | CanadaMountain | The time zone formerly known as Canada/Mountain is now represented as America/Edmonton in the IANA tz database for backwards compatibility. |
| Canada/Newfoundland | CanadaNewfoundland | The time zone formerly known as Canada/Newfoundland is now represented as America/St_Johns in the IANA tz database for backwards compatibility. |
| Canada/Pacific | CanadaPacific | The time zone formerly known as Canada/Pacific is now represented as America/Vancouver in the IANA tz database for backwards compatibility. |
| Canada/Saskatchewan | CanadaSaskatchewan | The time zone formerly known as Canada/Saskatchewan is now represented as America/Regina in the IANA tz database for backwards compatibility. |
| Canada/Yukon | CanadaYukon | The time zone formerly known as Canada/Yukon is now represented as America/Whitehorse in the IANA tz database for backwards compatibility. |
| ETC/UTC | EtcUtc | The time zone is ETC/UTC in the IANA tz database. |
| Etc/GMT | EtcGmt | The time zone is Etc/GMT in the IANA tz database. |
| Etc/GMT+1 | EtcGmtPlus1 | The time zone is Etc/GMT+1 in the IANA tz database. |
| Etc/GMT+10 | EtcGmtPlus10 | The time zone is Etc/GMT+10 in the IANA tz database. |
| Etc/GMT+11 | EtcGmtPlus11 | The time zone is Etc/GMT+11 in the IANA tz database. |
| Etc/GMT+12 | EtcGmtPlus12 | The time zone is Etc/GMT+12 in the IANA tz database. |
| Etc/GMT+2 | EtcGmtPlus2 | The time zone is Etc/GMT+2 in the IANA tz database. |
| Etc/GMT+3 | EtcGmtPlus3 | The time zone is Etc/GMT+3 in the IANA tz database. |
| Etc/GMT+4 | EtcGmtPlus4 | The time zone is Etc/GMT+4 in the IANA tz database. |
| Etc/GMT+5 | EtcGmtPlus5 | The time zone is Etc/GMT+5 in the IANA tz database. |
| Etc/GMT+6 | EtcGmtPlus6 | The time zone is Etc/GMT+6 in the IANA tz database. |
| Etc/GMT+7 | EtcGmtPlus7 | The time zone is Etc/GMT+7 in the IANA tz database. |
| Etc/GMT+8 | EtcGmtPlus8 | The time zone is Etc/GMT+8 in the IANA tz database. |
| Etc/GMT+9 | EtcGmtPlus9 | The time zone is Etc/GMT+9 in the IANA tz database. |
| Etc/GMT-1 | EtcGmtMinus1 | The time zone is Etc/GMT-1 in the IANA tz database. |
| Etc/GMT-10 | EtcGmtMinus10 | The time zone is Etc/GMT-10 in the IANA tz database. |
| Etc/GMT-11 | EtcGmtMinus11 | The time zone is Etc/GMT-11 in the IANA tz database. |
| Etc/GMT-12 | EtcGmtMinus12 | The time zone is Etc/GMT-12 in the IANA tz database. |
| Etc/GMT-13 | EtcGmtMinus13 | The time zone is Etc/GMT-13 in the IANA tz database. |
| Etc/GMT-14 | EtcGmtMinus14 | The time zone is Etc/GMT-14 in the IANA tz database. |
| Etc/GMT-2 | EtcGmtMinus2 | The time zone is Etc/GMT-2 in the IANA tz database. |
| Etc/GMT-3 | EtcGmtMinus3 | The time zone is Etc/GMT-3 in the IANA tz database. |
| Etc/GMT-4 | EtcGmtMinus4 | The time zone is Etc/GMT-4 in the IANA tz database. |
| Etc/GMT-5 | EtcGmtMinus5 | The time zone is Etc/GMT-5 in the IANA tz database. |
| Etc/GMT-6 | EtcGmtMinus6 | The time zone is Etc/GMT-6 in the IANA tz database. |
| Etc/GMT-7 | EtcGmtMinus7 | The time zone is Etc/GMT-7 in the IANA tz database. |
| Etc/GMT-8 | EtcGmtMinus8 | The time zone is Etc/GMT-8 in the IANA tz database. |
| Etc/GMT-9 | EtcGmtMinus9 | The time zone is Etc/GMT-9 in the IANA tz database. |
| Europe/Andorra | EuropeAndorra | The time zone is Europe/Andorra in the IANA tz database. |
| Europe/Astrakhan | EuropeAstrakhan | The time zone is Europe/Astrakhan in the IANA tz database. |
| Europe/Athens | EuropeAthens | The time zone is Europe/Athens in the IANA tz database. |
| Europe/Belgrade | EuropeBelgrade | The time zone is Europe/Belgrade in the IANA tz database. |
| Europe/Berlin | EuropeBerlin | The time zone is Europe/Berlin in the IANA tz database. |
| Europe/Brussels | EuropeBrussels | The time zone is Europe/Brussels in the IANA tz database. |
| Europe/Bucharest | EuropeBucharest | The time zone is Europe/Bucharest in the IANA tz database. |
| Europe/Budapest | EuropeBudapest | The time zone is Europe/Budapest in the IANA tz database. |
| Europe/Chisinau | EuropeChisinau | The time zone is Europe/Chisinau in the IANA tz database. |
| Europe/Dublin | EuropeDublin | The time zone is Europe/Dublin in the IANA tz database. |
| Europe/Gibraltar | EuropeGibraltar | The time zone is Europe/Gibraltar in the IANA tz database. |
| Europe/Helsinki | EuropeHelsinki | The time zone is Europe/Helsinki in the IANA tz database. |
| Europe/Istanbul | EuropeIstanbul | The time zone is Europe/Istanbul in the IANA tz database. |
| Europe/Kaliningrad | EuropeKaliningrad | The time zone is Europe/Kaliningrad in the IANA tz database. |
| Europe/Kirov | EuropeKirov | The time zone is Europe/Kirov in the IANA tz database. |
| Europe/Kyiv | EuropeKyiv | The time zone is Europe/Kyiv in the IANA tz database. |
| Europe/Lisbon | EuropeLisbon | The time zone is Europe/Lisbon in the IANA tz database. |
| Europe/London | EuropeLondon | The time zone is Europe/London in the IANA tz database. |
| Europe/Madrid | EuropeMadrid | The time zone is Europe/Madrid in the IANA tz database. |
| Europe/Malta | EuropeMalta | The time zone is Europe/Malta in the IANA tz database. |
| Europe/Minsk | EuropeMinsk | The time zone is Europe/Minsk in the IANA tz database. |
| Europe/Moscow | EuropeMoscow | The time zone is Europe/Moscow in the IANA tz database. |
| Europe/Paris | EuropeParis | The time zone is Europe/Paris in the IANA tz database. |
| Europe/Prague | EuropePrague | The time zone is Europe/Prague in the IANA tz database. |
| Europe/Riga | EuropeRiga | The time zone is Europe/Riga in the IANA tz database. |
| Europe/Rome | EuropeRome | The time zone is Europe/Rome in the IANA tz database. |
| Europe/Samara | EuropeSamara | The time zone is Europe/Samara in the IANA tz database. |
| Europe/Saratov | EuropeSaratov | The time zone is Europe/Saratov in the IANA tz database. |
| Europe/Simferopol | EuropeSimferopol | The time zone is Europe/Simferopol in the IANA tz database. |
| Europe/Sofia | EuropeSofia | The time zone is Europe/Sofia in the IANA tz database. |
| Europe/Tallinn | EuropeTallinn | The time zone is Europe/Tallinn in the IANA tz database. |
| Europe/Tirane | EuropeTirane | The time zone is Europe/Tirane in the IANA tz database. |
| Europe/Ulyanovsk | EuropeUlyanovsk | The time zone is Europe/Ulyanovsk in the IANA tz database. |
| Europe/Vienna | EuropeVienna | The time zone is Europe/Vienna in the IANA tz database. |
| Europe/Vilnius | EuropeVilnius | The time zone is Europe/Vilnius in the IANA tz database. |
| Europe/Volgograd | EuropeVolgograd | The time zone is Europe/Volgograd in the IANA tz database. |
| Europe/Warsaw | EuropeWarsaw | The time zone is Europe/Warsaw in the IANA tz database. |
| Europe/Zurich | EuropeZurich | The time zone is Europe/Zurich in the IANA tz database. |
| Factory | Factory | The time zone is Factory in the IANA tz database. |
| Indian/Chagos | IndianChagos | The time zone is Indian/Chagos in the IANA tz database. |
| Indian/Maldives | IndianMaldives | The time zone is Indian/Maldives in the IANA tz database. |
| Indian/Mauritius | IndianMauritius | The time zone is Indian/Mauritius in the IANA tz database. |
| Pacific/Apia | PacificApia | The time zone is Pacific/Apia in the IANA tz database. |
| Pacific/Auckland | PacificAuckland | The time zone is Pacific/Auckland in the IANA tz database. |
| Pacific/Bougainville | PacificBougainville | The time zone is Pacific/Bougainville in the IANA tz database. |
| Pacific/Chatham | PacificChatham | The time zone is Pacific/Chatham in the IANA tz database. |
| Pacific/Easter | PacificEaster | The time zone is Pacific/Easter in the IANA tz database. |
| Pacific/Efate | PacificEfate | The time zone is Pacific/Efate in the IANA tz database. |
| Pacific/Fakaofo | PacificFakaofo | The time zone is Pacific/Fakaofo in the IANA tz database. |
| Pacific/Fiji | PacificFiji | The time zone is Pacific/Fiji in the IANA tz database. |
| Pacific/Galapagos | PacificGalapagos | The time zone is Pacific/Galapagos in the IANA tz database. |
| Pacific/Gambier | PacificGambier | The time zone is Pacific/Gambier in the IANA tz database. |
| Pacific/Guadalcanal | PacificGuadalcanal | The time zone is Pacific/Guadalcanal in the IANA tz database. |
| Pacific/Guam | PacificGuam | The time zone is Pacific/Guam in the IANA tz database. |
| Pacific/Honolulu | PacificHonolulu | The time zone is Pacific/Honolulu in the IANA tz database. |
| Pacific/Kanton | PacificKanton | The time zone is Pacific/Kanton in the IANA tz database. |
| Pacific/Kiritimati | PacificKiritimati | The time zone is Pacific/Kiritimati in the IANA tz database. |
| Pacific/Kosrae | PacificKosrae | The time zone is Pacific/Kosrae in the IANA tz database. |
| Pacific/Kwajalein | PacificKwajalein | The time zone is Pacific/Kwajalein in the IANA tz database. |
| Pacific/Marquesas | PacificMarquesas | The time zone is Pacific/Marquesas in the IANA tz database. |
| Pacific/Nauru | PacificNauru | The time zone is Pacific/Nauru in the IANA tz database. |
| Pacific/Niue | PacificNiue | The time zone is Pacific/Niue in the IANA tz database. |
| Pacific/Norfolk | PacificNorfolk | The time zone is Pacific/Norfolk in the IANA tz database. |
| Pacific/Noumea | PacificNoumea | The time zone is Pacific/Noumea in the IANA tz database. |
| Pacific/Pago_Pago | PacificPagoPago | The time zone is Pacific/Pago_Pago in the IANA tz database. |
| Pacific/Palau | PacificPalau | The time zone is Pacific/Palau in the IANA tz database. |
| Pacific/Pitcairn | PacificPitcairn | The time zone is Pacific/Pitcairn in the IANA tz database. |
| Pacific/Port_Moresby | PacificPortMoresby | The time zone is Pacific/Port_Moresby in the IANA tz database. |
| Pacific/Rarotonga | PacificRarotonga | The time zone is Pacific/Rarotonga in the IANA tz database. |
| Pacific/Tahiti | PacificTahiti | The time zone is Pacific/Tahiti in the IANA tz database. |
| Pacific/Tarawa | PacificTarawa | The time zone is Pacific/Tarawa in the IANA tz database. |
| Pacific/Tongatapu | PacificTongatapu | The time zone is Pacific/Tongatapu in the IANA tz database. |

## image_of

- Source name: `ImageOf`
- Kind: **closed-SV**
- Value count: 86
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ImageOf/)
- Used by:
  - `media.image_of` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aerial View | AerialView | The image/photo is an aerial view of a structure or property. |
| Atrium | Atrium | The image/photo is of an atrium. |
| Attic | Attic | The image/photo is of an attic. |
| Back of Structure | BackOfStructure | The image/photo is of the back of a structure. |
| Balcony | Balcony | The image/photo is of a balcony. |
| Bar | Bar | The image/photo is of a bar. |
| Barn | Barn | The image/photo is of a barn. |
| Basement | Basement | The image/photo is of a basement. |
| Basketball Court | BasketballCourt | The image/photo is of a basketball court. |
| Bathroom | Bathroom | The image/photo is of a bathroom. |
| Bedroom | Bedroom | The image/photo is of a bedroom. |
| Bonus Room | BonusRoom | The image/photo is of a bonus room. |
| Breakfast Area | BreakfastArea | The image/photo is of a breakfast area. |
| Closet | Closet | The image/photo is of a closet. |
| Community | Community | The image/photo is of the surrounding community. |
| Courtyard | Courtyard | The image/photo is of a courtyard. |
| Deck | Deck | The image/photo is of a deck. |
| Den | Den | The image/photo is of a den. |
| Dining Area | DiningArea | The image/photo is of a dining area. |
| Dining Room | DiningRoom | The image/photo is of a dining room. |
| Dock | Dock | The image/photo is of a dock. |
| Entrance Foyer | EntranceFoyer | The image/photo is of an entrance foyer. |
| Entry | Entry | The image/photo is of an entry. |
| Exercise Room | ExerciseRoom | The image/photo is of an exercise room. |
| Family Room | FamilyRoom | The image/photo is of a family room. |
| Fence | Fence | The image/photo is of a fence. |
| Fireplace | Fireplace | The image/photo is of a fireplace. |
| Floor Plan | FloorPlan | The image/photo is of a floor plan. |
| Front of Structure | FrontOfStructure | The image/photo is of the front of a structure. |
| Game Room | GameRoom | The image/photo is of a game room. |
| Garage | Garage | The image/photo is of a garage. |
| Garden | Garden | The image/photo is of a garden. |
| Golf Course | GolfCourse | The image/photo is of a golf course. |
| Great Room | GreatRoom | The image/photo is of a great room. |
| Guest Quarters | GuestQuarters | The image/photo is of guest quarters. |
| Gym | Gym | The image/photo is of a gym. |
| Hallway | Hallway | The image/photo is of a hallway. |
| Hobby Room | HobbyRoom | The image/photo is of a hobby room. |
| Inlaw | Inlaw | The image/photo is of an in-law or mother-in-law room or quarters. |
| Kitchen | Kitchen | The image/photo is of a kitchen. |
| Lake | Lake | The image/photo is of a lake. |
| Laundry | Laundry | The image/photo is of a laundry room. |
| Library | Library | The image/photo is of a library. |
| Living Room | LivingRoom | The image/photo is of a living room. |
| Loading Dock | LoadingDock | The image/photo is of a loading dock. |
| Lobby | Lobby | The image/photo is of a lobby. |
| Loft | Loft | The image/photo is of a loft. |
| Lot | Lot | The image/photo is of a lot. |
| Map | Map | The image/photo is of a map. |
| Master Bathroom | MasterBathroom | The image/photo is of a primary bathroom. |
| Master Bedroom | MasterBedroom | The image/photo is of a primary bedroom. |
| Media Room | MediaRoom | The image/photo is of a media room. |
| Mud Room | MudRoom | The image/photo is of a mud room. |
| Nursery | Nursery | The image/photo is of a nursery. |
| Office | Office | The image/photo is of an office. |
| Other | Other | The image/photo is of a room or aspect of the property other than those listed in the ImageOf enumerations. |
| Out Buildings | OutBuildings | The image/photo is of an out building. |
| Pantry | Pantry | The image/photo is of a pantry. |
| Parking | Parking | The image/photo is of a parking area. |
| Patio | Patio | The image/photo is of a patio. |
| Pier | Pier | The image/photo is of a pier. |
| Plat Map | PlatMap | The image/photo is of a plat map. |
| Playground | Playground | The image/photo is of a playground. |
| Pond | Pond | The image/photo is of a pond. |
| Pool | Pool | The image/photo is of a pool. |
| Reception | Reception | The image/photo is of a reception area. |
| Recreation Room | RecreationRoom | The image/photo is of a recreation room. |
| Sauna | Sauna | The image/photo is of a sauna. |
| Showroom | Showroom | The image/photo is of a showroom. |
| Side of Structure | SideOfStructure | The image/photo is of the side of a structure. |
| Sitting Room | SittingRoom | The image/photo is of a sitting room. |
| Spa | Spa | The image/photo is of a spa. |
| Stable | Stable | The image/photo is of a stable. |
| Stairs | Stairs | The image/photo is of stairs. |
| Storage | Storage | The image/photo is of a storage area. |
| Studio | Studio | The image/photo is of a studio. |
| Study | Study | The image/photo is of a study. |
| Sun Room | SunRoom | The image/photo is of a sunroom. |
| Tennis Court | TennisCourt | The image/photo is of a tennis court or tennis courts. |
| Utility Room | UtilityRoom | The image/photo is of a utility room. |
| View | View | The image/photo is of a view. |
| Walk-In Closet(s) | WalkInClosets | The image/photo is of a walk-in closet or walk-in closets. |
| Waterfront | Waterfront | The image/photo is of a waterfront. |
| Wine Cellar | WineCellar | The image/photo is of a wine cellar. |
| Workshop | Workshop | The image/photo is of a workshop. |
| Yard | Yard | The image/photo is of a yard. |

## image_size_description

- Source name: `ImageSizeDescription`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ImageSizeDescription/)
- Used by:
  - `media.image_size_description` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## income_includes

- Source name: `IncomeIncludes`
- Kind: **closed-MV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/IncomeIncludes/)
- Used by:
  - `property.income_includes` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Laundry | Laundry | The income amount includes income from laundry facilities. |
| Parking | Parking | The income amount includes income from parking. |
| RV Storage | RvStorage | The income amount includes income from charging for RV storage. |
| Recreation | Recreation | The income amount includes income from charging for recreation facilities. |
| Rent Only | RentOnly | The income amount includes income from only the rent charged to the tenants. |
| Storage | Storage | The income amount includes income from charging for general storage. |

## interior_or_room_features

- Source name: `InteriorOrRoomFeatures`
- Kind: **closed-MV**
- Value count: 53
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/InteriorOrRoomFeatures/)
- Used by:
  - `property.interior_features` (type=`String List, Multi`)
  - `property_rooms.room_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bar | Bar | A built-in or movable fixture for the storage, preparation, serving and/or consumption of drinks. |
| Beamed Ceilings | BeamedCeilings | A property that has exposed beams across the ceiling of a room or rooms. |
| Bidet | Bidet | A type of sink designed to wash the undercarriage of the human body. |
| Bookcases | Bookcases | Shelves for books or other objects that may or may not be built into the property. |
| Breakfast Bar | BreakfastBar | A surface designed for eating, which is typically smaller than a dining table and attached to another kitchen surface. |
| Built-in Features | BuiltInFeatures | Some features are physically attached to the structure. |
| Cathedral Ceiling(s) | CathedralCeilings | A type of vaulted ceiling that is typically higher than normal ceilings and has a slant or curve to reach its uppermost point, which tends to be equal distance from the two shorter walls in the room. |
| Cedar Closet(s) | CedarClosets | A closet that is partially or fully lined with cedarwood. |
| Ceiling Fan(s) | CeilingFans | A fan is mounted from the ceiling in a room or multiple rooms. |
| Central Vacuum | CentralVacuum | A built-in vacuum that typically consists of a power/collection unit that is typically installed in a garage or closet, tubing from the power unit to rooms throughout the house and including wall-mounted receptacles for the connection of a movable vacuum hose. |
| Chandelier | Chandelier | A decorative lighting fixture that typically branches out with several lights (or candles) with other decorative components such as glass, crystal or other reflective or light-enhancing materials. |
| Coffered Ceiling(s) | CofferedCeilings | A ceiling with multiple decorative indentations, trays or sunken panels. |
| Crown Molding | CrownMolding | A decorative trim covering the seam between the ceiling and walls. |
| Double Vanity | DoubleVanity | Bathroom cabinetry with two built-in sinks. |
| Dry Bar | DryBar | A built-in or movable fixture for the storage, preparation, serving and consumption of drinks that does not have a water supply or sink. |
| Dumbwaiter | Dumbwaiter | A small elevator, typically for carrying food between floors in a structure. |
| Eat-in Kitchen | EatInKitchen | A kitchen that has been designed to accommodate dining. |
| Elevator | Elevator | A platform or compartment housed within a shaft for raising or lowering people or objects. |
| Entrance Foyer | EntranceFoyer | A room or hall at the entrance leading to other parts of the structure. |
| Granite Counters | GraniteCounters | The counters are made of a type of granite stone. |
| High Ceilings | HighCeilings | The ceiling height is greater than what might be considered a normal ceiling height. |
| High Speed Internet | HighSpeedInternet | The property has access to high-speed internet service but may or may not be wired and/or connected to that service. |
| His and Hers Closets | HisAndHersClosets | The room or rooms have two separate closets. |
| In-Law Floorplan | InLawFloorplan | The structure has an area within that has the characteristics of an independent apartment, typically with a living area, kitchen, bedroom and bathroom. |
| Kitchen Island | KitchenIsland | A separate counter surface in a kitchen that is not attached to other surfaces or to a wall. |
| Laminate Counters | LaminateCounters | The counters are covered with a laminate. |
| Low Flow Plumbing Fixtures | LowFlowPlumbingFixtures | Some or all of the fixtures are designed to save water. |
| Master Downstairs | MasterDownstairs | There is a primary bedroom on the main level of the structure. |
| Natural Woodwork | NaturalWoodwork | The property or room has features made from real wood. |
| Open Floorplan | OpenFloorplan | A generic design term for a floor plan that makes use of large open spaces and avoids the use of small enclosed spaces. |
| Other | Other | The room or interior has features other than those included on this list. |
| Pantry | Pantry | A small room or closet where food, dishes and utensils are stored. |
| Recessed Lighting | RecessedLighting | A light fixture installed into a hollow opening in the ceiling. |
| Sauna | Sauna | A small room or separate structure designed to produce heat to induce perspiration with wet steam (often poured over hot stones) or with dry heat. |
| See Remarks | SeeRemarks | See the remarks fields for additional information about the room or interior. |
| Smart Camera(s)/Recording | SmartCamerasRecording | A camera or recording control unit that has convenience and energy-saving aspects. |
| Smart Home | SmartHome | A generic term for electronic automation of features such as lighting, heating/cooling, security and other amenities. |
| Smart Light(s) | SmartLights | A lighting control unit that has convenience and energy-saving aspects. |
| Smart Thermostat | SmartThermostat | A heating/cooling control unit that has convenience and energy-saving aspects. |
| Soaking Tub | SoakingTub | A bathtub that is typically deeper and may be shorter than traditional tubs. |
| Solar Tube(s) | SolarTubes | A reflective tube that extends from a light-gathering surface on the roof of the structure down into a room where the outside light is distributed. |
| Sound System | SoundSystem | The property includes a sound system that typically includes in-wall wiring and recessed/built-in speakers and a built-in location for the amplifier and other audio equipment. |
| Stone Counters | StoneCounters | The property or room has counters that are made of some type of stone. |
| Storage | Storage | The property or room has storage space. |
| Tile Counters | TileCounters | The property or room has counters that are made of some type of tile. |
| Track Lighting | TrackLighting | A type of lighting where the light fixtures are mounted on a track allowing for adjustment of the position of the lights. |
| Tray Ceiling(s) | TrayCeilings | A ceiling with an inverted tray or recessed area, often rectangular, that adds depth and interest. |
| Vaulted Ceiling(s) | VaultedCeilings | Derived from the Italian word "volta," is this is typically a high ceiling with no attic between the ceiling and the roof. |
| Walk-In Closet(s) | WalkInClosets | A closet that is a small room with an entryway. |
| WaterSense Fixture(s) | WaterSenseFixtures | Water fixtures that are backed by independent, third-party certification and meet Environmental Protection Agency (EPA) specifications for water efficiency and performance. |
| Wet Bar | WetBar | Commonly a built-in fixture for the storage, preparation, serving and/or consumption of drinks that has a faucet and sink. |
| Wired for Data | WiredForData | The property has been wired for data, typically Category 5 or 6 wiring for the support of Ethernet data communications. |
| Wired for Sound | WiredForSound | The property has been wired for a built-in sound system. |

## irrigation_source

- Source name: `IrrigationSource`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/IrrigationSource/)
- Used by:
  - `property.irrigation_source` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## labor_information

- Source name: `LaborInformation`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LaborInformation/)
- Used by:
  - `property.labor_information` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Employee License Required | EmployeeLicenseRequired | Special licensing is required for employees. |
| Non-Union | NonUnion | A labor union is not currently established with the given business. |
| Union | Union | A labor union is established with the given business. |

## languages

- Source name: `Languages`
- Kind: **closed-SV**
- Value count: 190
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Languages/)
- Used by:
  - `contacts.language` (type=`String List, Multi`)
  - `member.member_languages` (type=`String List, Multi`)
  - `prospecting.language` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Abkhazian | Abkhazian | The language spoken by the member/individual is Abkhazian. |
| Afar | Afar | The language spoken by the member/individual is Afar. |
| Afrikaans | Afrikaans | The language spoken by the member/individual is Afrikaans. |
| Albanian | Albanian | The language spoken by the member/individual is Albanian. |
| American Sign Language | AmericanSignLanguage | The language spoken by the member/individual is American Sign Language. |
| Amharic | Amharic | The language spoken by the member/individual is Amharic. |
| Arabic | Arabic | The language spoken by the member/individual is Arabic. |
| Aramaic | Aramaic | The language spoken by the member/individual is Aramaic. |
| Armenian | Armenian | The language spoken by the member/individual is Armenian. |
| Assamese | Assamese | The language spoken by the member/individual is Assamese. |
| Assyrian Neo-Aramaic | AssyrianNeoAramaic | The language spoken by the member/individual is Assyrian Neo-Aramaic. |
| Avestan | Avestan | The language spoken by the member/individual is Avestan. |
| Aymara | Aymara | The language spoken by the member/individual is Aymara. |
| Azerbaijani | Azerbaijani | The language spoken by the member/individual is Azerbaijani. |
| Bambara | Bambara | The language spoken by the member/individual is Bambara. |
| Bashkir | Bashkir | The language spoken by the member/individual is Bashkir. |
| Basque | Basque | The language spoken by the member/individual is Basque. |
| Bengali | Bengali | The language spoken by the member/individual is Bengali. |
| Bihari | Bihari | The language spoken by the member/individual is Bihari. |
| Bikol | Bikol | The language spoken by the member/individual is Bikol. |
| Bislama | Bislama | The language spoken by the member/individual is Bislama. |
| Bosnian | Bosnian | The language spoken by the member/individual is Bosnian. |
| Brazilian Portuguese | BrazilianPortuguese | The language spoken by the member/individual is Brazilian Portuguese. |
| Bulgarian | Bulgarian | The language spoken by the member/individual is Bulgarian. |
| Burmese | Burmese | The language spoken by the member/individual is Burmese. |
| Byelorussian | Byelorussian | The language spoken by the member/individual is Byelorussian. |
| Cambodian | Cambodian | The language spoken by the member/individual is Cambodian. |
| Cantonese | Cantonese | The language spoken by the member/individual is Cantonese. |
| Cape Verdean Creole | CapeVerdeanCreole | The language spoken by the member/individual is Cape Verdean Creole. |
| Catalan | Catalan | The language spoken by the member/individual is Catalan. |
| Cebuano | Cebuano | The language spoken by the member/individual is Cebuano. |
| Chamorro | Chamorro | The language spoken by the member/individual is Chamorro. |
| Chechen | Chechen | The language spoken by the member/individual is Chechen. |
| Chinese | Chinese | The language spoken by the member/individual is Chinese. |
| Chuukese | Chuukese | The language spoken by the member/individual is Chuukese. |
| Chuvash | Chuvash | The language spoken by the member/individual is Chuvash. |
| Cornish | Cornish | The language spoken by the member/individual is Cornish. |
| Corsican | Corsican | The language spoken by the member/individual is Corsican. |
| Croatian | Croatian | The language spoken by the member/individual is Croatian. |
| Czech | Czech | The language spoken by the member/individual is Czech. |
| Danish | Danish | The language spoken by the member/individual is Danish. |
| Dari (Afghan Persian) | Dari | The language spoken by the member/individual is Dari (Afghan Persian). |
| Dioula | Dioula | The language spoken by the member/individual is Dioula. |
| Dutch | Dutch | The language spoken by the member/individual is Dutch. |
| Dzongkha | Dzongkha | The language spoken by the member/individual is Dzongkha. |
| English | English | The language spoken by the member/individual is English. |
| Esperanto | Esperanto | The language spoken by the member/individual is Esperanto. |
| Estonian | Estonian | The language spoken by the member/individual is Estonian. |
| Faroese | Faroese | The language spoken by the member/individual is Faroese. |
| Farsi | Farsi | The language spoken by the member/individual is Farsi. |
| Fiji | Fiji | The language spoken by the member/individual is Fiji. |
| Finnish | Finnish | The language spoken by the member/individual is Finnish. |
| Flemish | Flemish | The language spoken by the member/individual is Flemish. |
| French | French | The language spoken by the member/individual is French. |
| Frisian | Frisian | The language spoken by the member/individual is Frisian. |
| Galician | Galician | The language spoken by the member/individual is Galician. |
| Georgian | Georgian | The language spoken by the member/individual is Georgian. |
| German | German | The language spoken by the member/individual is German. |
| Greek | Greek | The language spoken by the member/individual is Greek. |
| Greenlandic | Greenlandic | The language spoken by the member/individual is Greenlandic. |
| Guarani | Guarani | The language spoken by the member/individual is Guarani. |
| Gujarati | Gujarati | The language spoken by the member/individual is Gujarati. |
| Haitian Creole | HaitianCreole | The language spoken by the member/individual is Haitian Creole. |
| Hausa | Hausa | The language spoken by the member/individual is Hausa. |
| Hebrew | Hebrew | The language spoken by the member/individual is Hebrew. |
| Herero | Herero | The language spoken by the member/individual is Herero. |
| Hiligaynon | Hiligaynon | The language spoken by the member/individual is Hiligaynon. |
| Hindi | Hindi | The language spoken by the member/individual is Hindi. |
| Hiri Motu | HiriMotu | The language spoken by the member/individual is Hiri Motu. |
| Hmong | Hmong | The language spoken by the member/individual is Hmong. |
| Hungarian | Hungarian | The language spoken by the member/individual is Hungarian. |
| Iban | Iban | The language spoken by the member/individual is Iban. |
| Icelandic | Icelandic | The language spoken by the member/individual is Icelandic. |
| Igbo | Igbo | The language spoken by the member/individual is Igbo. |
| Ilocano | Ilocano | The language spoken by the member/individual is Ilocano. |
| Indonesian | Indonesian | The language spoken by the member/individual is Indonesian. |
| Interlingua | Interlingua | The language spoken by the member/individual is Interlingua. |
| Inuktitut | Inuktitut | The language spoken by the member/individual is Inuktitut. |
| Inupiak | Inupiak | The language spoken by the member/individual is Inupiak. |
| Irish (Gaelic) | Irish | The language spoken by the member/individual is Irish (Gaelic). |
| Italian | Italian | The language spoken by the member/individual is Italian. |
| Japanese | Japanese | The language spoken by the member/individual is Japanese. |
| Javanese | Javanese | The language spoken by the member/individual is Javanese. |
| K'iche' | KIche | The language spoken by the member/individual is K'iche'. |
| Kannada | Kannada | The language spoken by the member/individual is Kannada. |
| Kashmiri | Kashmiri | The language spoken by the member/individual is Kashmiri. |
| Kazakh | Kazakh | The language spoken by the member/individual is Kazakh. |
| Kichwa | Kichwa | The language spoken by the member/individual is Kichwa. |
| Kikuyu | Kikuyu | The language spoken by the member/individual is Kikuyu. |
| Kinyarwanda | Kinyarwanda | The language spoken by the member/individual is Kinyarwanda. |
| Kirghiz | Kirghiz | The language spoken by the member/individual is Kirghiz. |
| Kirundi | Kirundi | The language spoken by the member/individual is Kirundi. |
| Komi | Komi | The language spoken by the member/individual is Komi. |
| Korean | Korean | The language spoken by the member/individual is Korean. |
| Kpelle | Kpelle | The language spoken by the member/individual is Kpelle. |
| Kru | Kru | The language spoken by the member/individual is Kru. |
| Kurdish | Kurdish | The language spoken by the member/individual is Kurdish. |
| Lao | Lao | The language spoken by the member/individual is Lao. |
| Latin | Latin | The language spoken by the member/individual is Latin. |
| Latvian | Latvian | The language spoken by the member/individual is Latvian. |
| Lingala | Lingala | The language spoken by the member/individual is Lingala. |
| Lithuanian | Lithuanian | The language spoken by the member/individual is Lithuanian. |
| Luxemburgish | Luxemburgish | The language spoken by the member/individual is Luxemburgish. |
| Macedonian | Macedonian | The language spoken by the member/individual is Macedonian. |
| Malagasy | Malagasy | The language spoken by the member/individual is Malagasy. |
| Malay | Malay | The language spoken by the member/individual is Malay. |
| Malayalam | Malayalam | The language spoken by the member/individual is Malayalam. |
| Maltese | Maltese | The language spoken by the member/individual is Maltese. |
| Mandarin | Mandarin | The language spoken by the member/individual is Mandarin. |
| Maninka | Maninka | The language spoken by the member/individual is Maninka. |
| Manx Gaelic | ManxGaelic | The language spoken by the member/individual is Manx Gaelic. |
| Maori | Maori | The language spoken by the member/individual is Maori. |
| Marathi | Marathi | The language spoken by the member/individual is Marathi. |
| Marshallese | Marshallese | The language spoken by the member/individual is Marshallese. |
| Moldovan | Moldovan | The language spoken by the member/individual is Moldovan. |
| Mongolian | Mongolian | The language spoken by the member/individual is Mongolian. |
| Nauru | Nauru | The language spoken by the member/individual is Nauru. |
| Navajo | Navajo | The language spoken by the member/individual is Navajo. |
| Ndebele | Ndebele | The language spoken by the member/individual is Ndebele. |
| Ndonga | Ndonga | The language spoken by the member/individual is Ndonga. |
| Nepali | Nepali | The language spoken by the member/individual is Nepali. |
| Norwegian | Norwegian | The language spoken by the member/individual is Norwegian. |
| Norwegian (Nynorsk) | NorwegianNynorsk | The language spoken by the member/individual is Norwegian (Nynorsk). |
| Nyanja | Nyanja | The language spoken by the member/individual is Nyanja. |
| Occitan | Occitan | The language spoken by the member/individual is Occitan. |
| Oriya | Oriya | The language spoken by the member/individual is Oriya. |
| Oromo | Oromo | The language spoken by the member/individual is Oromo. |
| Ossetian | Ossetian | The language spoken by the member/individual is Ossetian. |
| Pali | Pali | The language spoken by the member/individual is Pali. |
| Pangasinan | Pangasinan | The language spoken by the member/individual is Pangasinan. |
| Papiamento | Papiamento | The language spoken by the member/individual is Papiamento. |
| Pashto | Pashto | The language spoken by the member/individual is Pashto. |
| Polish | Polish | The language spoken by the member/individual is Polish. |
| Portuguese | Portuguese | The language spoken by the member/individual is Portuguese. |
| Punjabi | Punjabi | The language spoken by the member/individual is Punjabi. |
| Quechua | Quechua | The language spoken by the member/individual is Quechua. |
| Romanian | Romanian | The language spoken by the member/individual is Romanian. |
| Romany | Romany | The language spoken by the member/individual is Romany. |
| Russian | Russian | The language spoken by the member/individual is Russian. |
| Sami | Sami | The language spoken by the member/individual is Sami. |
| Samoan | Samoan | The language spoken by the member/individual is Samoan. |
| Sangho | Sangho | The language spoken by the member/individual is Sangho. |
| Sanskrit | Sanskrit | The language spoken by the member/individual is Sanskrit. |
| Sardinian | Sardinian | The language spoken by the member/individual is Sardinian. |
| Scots Gaelic | ScotsGaelic | The language spoken by the member/individual is Scots Gaelic. |
| Serbian | Serbian | The language spoken by the member/individual is Serbian. |
| Serbo-Croatian | SerboCroatian | The language spoken by the member/individual is Serbo-Croatian. |
| Sesotho | Sesotho | The language spoken by the member/individual is Sesotho. |
| Setswana | Setswana | The language spoken by the member/individual is Setswana. |
| Shan | Shan | The language spoken by the member/individual is Shan. |
| Shona | Shona | The language spoken by the member/individual is Shona. |
| Sindhi | Sindhi | The language spoken by the member/individual is Sindhi. |
| Sinhalese | Sinhalese | The language spoken by the member/individual is Sinhalese. |
| Siswati | Siswati | The language spoken by the member/individual is Siswati. |
| Slovak | Slovak | The language spoken by the member/individual is Slovak. |
| Slovenian | Slovenian | The language spoken by the member/individual is Slovenian. |
| Somali | Somali | The language spoken by the member/individual is Somali. |
| Southern Ndebele | SouthernNdebele | The language spoken by the member/individual is Southern Ndebele. |
| Spanish | Spanish | The language spoken by the member/individual is Spanish. |
| Sundanese | Sundanese | The language spoken by the member/individual is Sundanese. |
| Swahili | Swahili | The language spoken by the member/individual is Swahili. |
| Swedish | Swedish | The language spoken by the member/individual is Swedish. |
| Syriac | Syriac | The language spoken by the member/individual is Syriac. |
| Tagalog | Tagalog | The language spoken by the member/individual is Tagalog. |
| Tahitian | Tahitian | The language spoken by the member/individual is Tahitian. |
| Tajik | Tajik | The language spoken by the member/individual is Tajik. |
| Tamil | Tamil | The language spoken by the member/individual is Tamil. |
| Tatar | Tatar | The language spoken by the member/individual is Tatar. |
| Telugu | Telugu | The language spoken by the member/individual is Telugu. |
| Thai | Thai | The language spoken by the member/individual is Thai. |
| Tibetan | Tibetan | The language spoken by the member/individual is Tibetan. |
| Tigrinya | Tigrinya | The language spoken by the member/individual is Tigrinya. |
| Tongan | Tongan | The language spoken by the member/individual is Tongan. |
| Tsonga | Tsonga | The language spoken by the member/individual is Tsonga. |
| Turkish | Turkish | The language spoken by the member/individual is Turkish. |
| Turkmen | Turkmen | The language spoken by the member/individual is Turkmen. |
| Twi | Twi | The language spoken by the member/individual is Twi. |
| Uigur | Uigur | The language spoken by the member/individual is Uigur. |
| Ukrainian | Ukrainian | The language spoken by the member/individual is Ukrainian. |
| Urdu | Urdu | The language spoken by the member/individual is Urdu. |
| Uzbek | Uzbek | The language spoken by the member/individual is Uzbek. |
| Vietnamese | Vietnamese | The language spoken by the member/individual is Vietnamese. |
| Volapuk | Volapuk | The language spoken by the member/individual is Volapuk. |
| Welsh | Welsh | The language spoken by the member/individual is Welsh. |
| Wolof | Wolof | The language spoken by the member/individual is Wolof. |
| Xhosa | Xhosa | The language spoken by the member/individual is Xhosa. |
| Yiddish | Yiddish | The language spoken by the member/individual is Yiddish. |
| Yoruba | Yoruba | The language spoken by the member/individual is Yoruba. |
| Zhuang | Zhuang | The language spoken by the member/individual is Zhuang. |
| Zulu | Zulu | The language spoken by the member/individual is Zulu. |

## laundry_features

- Source name: `LaundryFeatures`
- Kind: **closed-MV**
- Value count: 24
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LaundryFeatures/)
- Used by:
  - `property.laundry_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Common Area | CommonArea | Laundry features are in a common area. |
| Electric Dryer Hookup | ElectricDryerHookup | The property has electric clothes dryer connections. |
| Gas Dryer Hookup | GasDryerHookup | The property has gas clothes dryer connections. |
| In Basement | InBasement | Laundry features are located in a basement. |
| In Bathroom | InBathroom | Laundry features are located in a bathroom. |
| In Carport | InCarport | Laundry features are located in a carport. |
| In Garage | InGarage | Laundry features are located in a garage. |
| In Hall | InHall | Laundry features are located in a hall. |
| In Kitchen | InKitchen | Laundry features are located in a kitchen. |
| In Unit | InUnit | Laundry features are located in a unit. |
| Inside | Inside | Laundry features are located indoors. |
| Laundry Chute | LaundryChute | The property has a laundry chute. |
| Laundry Closet | LaundryCloset | The property has a laundry closet. |
| Laundry Room | LaundryRoom | The property has a laundry room. |
| Lower Level | LowerLevel | Laundry features are located on a lower level. |
| Main Level | MainLevel | Laundry features are located on the main level. |
| Multiple Locations | MultipleLocations | Laundry features are located in multiple locations. |
| None | None | There are no laundry features. |
| Other | Other | There are laundry features other than those on this list. |
| Outside | Outside | Laundry features are located outside. |
| See Remarks | SeeRemarks | See remarks for additional information about laundry features. |
| Sink | Sink | The laundry area has a sink. |
| Upper Level | UpperLevel | Laundry features are located on an upper level. |
| Washer Hookup | WasherHookup | The property has a hookups for a clothes washer. |

## lease_renewal_compensation

- Source name: `LeaseRenewalCompensation`
- Kind: **closed-MV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LeaseRenewalCompensation/)
- Used by:
  - `property.lease_renewal_compensation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Call Listing Agent | CallListingAgent | For details about additional selling office compensation for lease renewals, contact the listing agent. |
| Call Listing Office | CallListingOffice | For details about additional selling office compensation for lease renewals, contact the listing office. |
| Commission Paid On Tenant Purchase | CommissionPaidOnTenantPurchase | Additional commission is paid in the event the tenant purchases the property. |
| No Renewal Commission | NoRenewalCommission | There is no additional commission if the tenant renews or extends the lease. |
| Renewal Commission Paid | RenewalCommissionPaid | There is additional commission paid if the tenant renews the lease. |

## lease_term

- Source name: `LeaseTerm`
- Kind: **closed-SV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LeaseTerm/)
- Used by:
  - `property.lease_term` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 12 Months | TwelveMonths | The length of the lease is 12 months. |
| 24 Months | TwentyFourMonths | The length of the lease is 24 months. |
| 6 Months | SixMonths | The length of the lease is 6 months. |
| Month To Month | MonthToMonth | The length of the lease is month to month. |
| Negotiable | Negotiable | The length of the lease is negotiable. |
| None | None | There is no stated term to the lease. |
| Other | Other | The term of the lease is something other than is available on this list. |
| Renewal Option | RenewalOption | The lease has a renewal option. |
| Short Term Lease | ShortTermLease | The lease is short term. |
| Weekly | Weekly | The length of the lease is weekly. |

## levels

- Source name: `Levels`
- Kind: **closed-MV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Levels/)
- Used by:
  - `property.levels` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bi-Level | BiLevel | A bi-level home has two staggered levels. |
| Multi/Split | MultiSplit | A split-level home (also called a tri-level home) is a style of house in which the floor levels are staggered so that the "main" level of the house (e.g., the level that usually contains the front entry) is partway between the upper and lower floors. |
| One | One | The property being sold has one level. |
| One and One Half | OneAndOneHalf | A 1.5-story house is where the height of any of the walls on the second floor are less than the height of the walls on the first floor. |
| Quad-Level | QuadLevel | A quad-level home has four staggered levels connected by two or more short sets of stairs. |
| Three Or More | ThreeOrMore | The property being sold has three or more levels. |
| Tri-Level | TriLevel | A tri-level home has three staggered levels connected by two or more short sets of stairs. |
| Two | Two | The property being sold has two levels. |

## linear_units

- Source name: `LinearUnits`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LinearUnits/)
- Used by:
  - `property.distance_to_bus_units` (type=`String List, Single`)
  - `property.distance_to_electric_units` (type=`String List, Single`)
  - `property.distance_to_freeway_units` (type=`String List, Single`)
  - `property.distance_to_gas_units` (type=`String List, Single`)
  - `property.distance_to_phone_service_units` (type=`String List, Single`)
  - `property.distance_to_placeof_worship_units` (type=`String List, Single`)
  - `property.distance_to_school_bus_units` (type=`String List, Single`)
  - `property.distance_to_schools_units` (type=`String List, Single`)
  - `property.distance_to_sewer_units` (type=`String List, Single`)
  - `property.distance_to_shopping_units` (type=`String List, Single`)
  - `property.distance_to_street_units` (type=`String List, Single`)
  - `property.distance_to_water_units` (type=`String List, Single`)
  - `property.elevation_units` (type=`String List, Single`)
  - `property.mobile_dim_units` (type=`String List, Single`)
  - `property_rooms.room_length_width_units` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Feet | Feet | The elevation of the property is measured in feet. |
| Meters | Meters | The elevation of the property is measured in meters. |

## list_agent_designation

- Source name: `ListAgentDesignation`
- Kind: **closed-MV**
- Value count: 27
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ListAgentDesignation/)
- Used by:
  - `property.list_agent_designation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accredited Buyer's Representative / ABR | AccreditedBuyersRepresentative | The Accredited Buyer's Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| Accredited Land Consultant / ALC | AccreditedLandConsultant | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| At Home With Diversity / AHWD | AtHomeWithDiversity | Learn to work effectively with and within today's diverse real estate market. |
| Certified Commercial Investment Member / CCIM | CertifiedCommercialInvestmentMember | The Certified Commercial Investment Member (CCIM) designation is commercial real estate's global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| Certified Distressed Property Expert / CDPE | CertifiedDistressedPropertyExpert | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today's turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| Certified International Property Specialist / CIPS | CertifiedInternationalPropertySpecialist | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| Certified Property Manager / CPM | CertifiedPropertyManager | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| Certified Real Estate Brokerage Manager / CRB | CertifiedRealEstateBrokerageManager | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| Certified Real Estate Team Specialist / C-RETS | CertifiedRealEstateTeamSpecialist | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| Certified Residential Specialist / CRS | CertifiedResidentialSpecialist | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| Counselor of Real Estate / CRE | CounselorOfRealEstate | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| General Accredited Appraiser / GAA | GeneralAccreditedAppraiser | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Graduate, REALTOR Institute / GRI | GraduateRealtorInstitute | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| Military Relocation Professional / MRP | MilitaryRelocationProfessional | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| NAR's Green Designation / GREEN | NARsGreenDesignation | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| Performance Management Network / PMN | PerformanceManagementNetwork | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| Pricing Strategy Advisor / PSA | PricingStrategyAdvisor | Enhance your skills in pricing properties, creating CMAs (comparative market analysis), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| REALTOR Association Certified Executive / RCE | RealtorAssociationCertifiedExecutive | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| Real Estate Negotiation Expert / RENE | RealEstateNegotiationExpert | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| Residential Accredited Appraiser / RAA | ResidentialAccreditedAppraiser | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Resort & Second-Home Property Specialist / RSPS | ResortAndSecondHomePropertySpecialist | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| Seller Representative Specialist / SRS | SellerRepresentativeSpecialist | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| Seniors Real Estate Specialist / SRES | SeniorsRealEstateSpecialist | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| Short Sales & Foreclosure Resource / SFR | ShortSalesAndForeclosureResource | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| Society of Industrial and Office REALTORS / SIOR | SocietyOfIndustrialAndOfficeRealtors | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| Transnational Referral Certification / TRC | TransnationalReferralCertification | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |
| e-PRO | ePRO | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |

## listing_agreement

- Source name: `ListingAgreement`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ListingAgreement/)
- Used by:
  - `property.listing_agreement` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Exclusive Agency | ExclusiveAgency | A contract giving one brokerage firm, for a specified time, the right to sell/lease the property and also allowing the owner, acting alone, to sell/lease the property without paying commission. |
| Exclusive Right To Lease | ExclusiveRightToLease | A contract giving the broker the right to collect commission if the property is leased by anyone, including the owner, during the term of the agreement. |
| Exclusive Right To Sell | ExclusiveRightToSell | A contract giving the broker the right to collect commission if the property is sold by anyone, including the owner, during the term of the agreement. |
| Exclusive Right With Exception | ExclusiveRightWithException | A contract giving the broker the right to collect commission if the property is sold by anyone, including the owner, during the term of the agreement unless some specified exceptions to the agreement occur. |
| Net | Net | A listing in which the broker's commission is the excess of the sale price over an agreed-upon (net) price to the seller; illegal in some states because it can create a conflict of interest for the broker. |
| Open | Open | Often used for commercial property, a listing given to any number of brokers without liability to compensate any except the one who first secures a buyer who is ready, willing and able to meet the terms of the listing and secures the seller's acceptance. |
| Probate | Probate | An Exclusive Right To Sell listing agreement that also resides under authority of the local probate code. |

## listing_service

- Source name: `ListingService`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ListingService/)
- Used by:
  - `property.listing_service` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Entry Only | EntryOnly | The only service provided by the brokerage is the input of the listing into the MLS system. |
| Full Service | FullService | A full set of services offered by a brokerage. |
| Limited Service | LimitedService | A limited set of services offered by a brokerage |

## listing_terms

- Source name: `ListingTerms`
- Kind: **closed-MV**
- Value count: 26
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ListingTerms/)
- Used by:
  - `property.listing_terms` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 1031 Exchange | Exchange1031 | The seller may be interested in a 1031 exchange as part of the sale. |
| All Inclusive Trust Deed | AllInclusiveTrustDeed | The property is under an all-inclusive trust deed. |
| Assumable | Assumable | The seller is interested in assumable financing. |
| Cash | Cash | The seller would like a cash sale. |
| Contract | Contract | The seller may be interested in an agreement to perform services, provide product, share income or some other agreement as the method of payment for the property. |
| Conventional | Conventional | The seller may accept a buyer using conventional financing to purchase the home. |
| Existing Bonds | ExistingBonds | The property for sale has existing bonds. |
| FHA | FHA | The seller may accept a buyer with a loan from an approved provider that follows the guidelines of, and is insured by, the Federal Housing Administration (FHA). |
| Land Use Fee | LandUseFee | The listed property has a land use fee. |
| Lease Back | LeaseBack | The seller may be interested in the simultaneous sale of a property with a lease back to the seller who then becomes the tenant. |
| Lease Option | LeaseOption | The seller may be interested in selling as a lease option to the buyer. |
| Lease Purchase | LeasePurchase | The seller may be interested in selling as a lease purchase. |
| Lien Release | LienRelease | The property for sale may require a lien release. |
| Owner May Carry | OwnerMayCarry | The seller may be interested in carrying the mortgage note. |
| Owner Pay Points | OwnerPayPoints | The seller may carry points. |
| Owner Will Carry | OwnerWillCarry | The seller will carry the mortgage note. |
| Private Financing Available | PrivateFinancingAvailable | Financing is provided by a private party. |
| Relocation Property | RelocationProperty | The property for sale is a relocation property. |
| Seller Equity Share | SellerEquityShare | The seller may be interested in investing in an equity share. |
| Special Funding | SpecialFunding | The seller may be interested in a special funding arrangement. |
| Submit | Submit | Contact the listing agent for the listing terms. |
| Trade | Trade | The seller may be interested in a trade arrangement. |
| Trust Conveyance | TrustConveyance | A trust conveyance (to another trustee) may be involved in the sale of the property. |
| Trust Deed | TrustDeed | The seller may accept financing where title of the property is placed with a trustee who secures payment of the loan for a beneficiary. |
| USDA Loan | UsdaLoan | The seller may accept a loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |
| VA Loan | VaLoan | The seller may accept a loan from an approved provider that follows the guidelines of, and is insured by, the U.S. |

## listing_url_description

- Source name: `ListingURLDescription`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ListingURLDescription/)
- Used by:
  - `property.listing_url_description` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent Website | AgentWebsite | A link that directs to the listing on an agent website. |
| Broker Website | BrokerWebsite | A link that directs to the listing on a broker website. |
| Brokerage Website | BrokerageWebsite | A link that directs to the listing on a brokerage website. |
| Franchisor Website | FranchisorWebsite | A link that directs to the listing on a franchisor website. |
| MLS Website | MlsWebsite | A link that directs to the listing on an MLS website. |
| Other Website | OtherWebsite | A link that directs to the listing on a general website. |
| Syndication Website | SyndicationWebsite | A link that directs to the listing on a syndication website. |

## lock_box_type

- Source name: `LockBoxType`
- Kind: **closed-MV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LockBoxType/)
- Used by:
  - `property.lock_box_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Call Listing Office | CallListingOffice | Call the listing office for information about accessing the property. |
| Call Seller Direct | CallSellerDirect | Call the seller directly to arrange for access to the property. |
| Combo | Combo | The lockbox on the property is opened via combination. |
| None | None | There is no lockbox on the property. |
| Other | Other | A lockbox type is not included on this list. |
| See Remarks | SeeRemarks | See remarks for details about the lockbox and accessing the property. |
| SentriLock | Sentrilock | The lockbox is from SentriLock and requires a SentriLock key or access code. |
| Supra | Supra | The lockbox is from Supra and requires a Supra key. |

## lock_or_box_access_type

- Source name: `LockOrBoxAccessType`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LockOrBoxAccessType/)
- Used by:
  - `lock_or_box.lock_or_box_access_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| App | App | The lockbox/smart lock can be unlocked with a mobile application. |
| Card | Card | The lockbox/smart lock can be unlocked with an access card. |
| Code | Code | The lockbox/smart lock can be unlocked with an access code. |

## lot_dimensions_source

- Source name: `LotDimensionsSource`
- Kind: **closed-SV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LotDimensionsSource/)
- Used by:
  - `property.lot_dimensions_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | The lot dimensions were provided by an appraiser. |
| Assessor | Assessor | The lot dimensions were provided by an assessor. |
| Builder | Builder | The lot dimensions were provided by a builder. |
| Estimated | Estimated | The lot dimensions were estimated. |
| GIS Calculated | GisCalculated | The lot dimensions were calculated by a Geographic Information System (GIS). |
| Measured | Measured | The lot dimensions were measured. |
| Other | Other | The lot dimensions were provided by a source other than those on this list. |
| Owner | Owner | The lot dimensions were provided by the owner. |
| Public Records | PublicRecords | The lot dimensions were taken from public records. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the source of the lot dimensions. |
| Survey | Survey | The lot dimensions were provided by a land survey. |

## lot_features

- Source name: `LotFeatures`
- Kind: **closed-MV**
- Value count: 56
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LotFeatures/)
- Used by:
  - `property.lot_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agricultural | Agricultural | The lot has agricultural features. |
| Back Yard | BackYard | The lot has a backyard. |
| Bluff | Bluff | The lot is on or near a bluff. |
| City Lot | CityLot | The lot is in a city/urban setting. |
| Cleared | Cleared | The lot has been cleared. |
| Close to Clubhouse | CloseToClubhouse | The lot is located close to a community clubhouse. |
| Corner Lot | CornerLot | The lot is located on the corner of an intersection. |
| Corners Marked | CornersMarked | The corners of the lot have been marked. |
| Cul-De-Sac | CulDeSac | The lot is located on a street that is closed on one end in a circular shape. |
| Desert Back | DesertBack | The back of the lot faces a desert area. |
| Desert Front | DesertFront | The front of the lot faces a desert area. |
| Farm | Farm | The lot is or has characteristics of a farm. |
| Few Trees | FewTrees | The lot has a few trees. |
| Flag Lot | FlagLot | Named for the shape, a flag lot has a long driveway leading to the property that, together, may have the appearance of a pole and flag. |
| Front Yard | FrontYard | The lot has a front yard. |
| Garden | Garden | The lot has a garden. |
| Gentle Sloping | GentleSloping | The lot's slope is gentle. |
| Greenbelt | Greenbelt | the lot is adjacent to a greenbelt. |
| Interior Lot | InteriorLot | Also referred to as an inside lot, an interior lot faces a street on only one side. |
| Irregular Lot | IrregularLot | The lot is not a rectangle. |
| Lake on Lot | LakeOnLot | The lot is not waterfront but the lake water feature is part of the lot. |
| Landscaped | Landscaped | The lot has been fully or partially landscaped. |
| Level | Level | The lot is level/flat. |
| Many Trees | ManyTrees | The lot has many trees. |
| Meadow | Meadow | The lot has a meadow. |
| Native Plants | NativePlants | The lot's landscaping includes native plants. |
| Near Golf Course | NearGolfCourse | The lot is near a golf course. |
| Near Public Transit | NearPublicTransit | The lot is near public transportation. |
| On Golf Course | OnGolfCourse | The lot is directly adjacent to a golf course. |
| Open Lot | OpenLot | The lot is open. |
| Orchard(s) | Orchards | The lot includes one or more orchards. |
| Other | Other | The lot has features other than those on this list. |
| Pasture | Pasture | The lot includes a pasture. |
| Paved | Paved | The lot is partially or fully paved. |
| Pie Shaped Lot | PieShapedLot | The lot is shaped like a pie or triangle and is typically narrow at the front and wide at the back. |
| Pond on Lot | PondOnLot | The lot is not waterfront but the pond water feature is part of the lot. |
| Private | Private | The lot is private or has features that provide privacy from adjacent areas such as neighbors or roads. |
| Rectangular Lot | RectangularLot | Also known as a regular-shaped lot, the lot has a rectangle or square shape. |
| Rock Outcropping | RockOutcropping | Rock features or barriers that transition a grading in the landscape. |
| Rolling Slope | RollingSlope | The slope of the property varies in a rolling or wavy fashion. |
| Secluded | Secluded | The lot is secluded. |
| See Remarks | SeeRemarks | See the remarks fields for additional information about the lot's features. |
| Sloped | Sloped | The lot is sloped. |
| Sloped Down | SlopedDown | The lot is sloped down, typically from the perspective of looking at the property from the street. |
| Sloped Up | SlopedUp | The lot is sloped up, typically from the perspective of looking at the property from the street. |
| Split Possible | SplitPossible | It may be possible that the lot could be split into two or more parcels. |
| Sprinklers In Front | SprinklersInFront | There are irrigation sprinklers on the front of the lot. |
| Sprinklers In Rear | SprinklersInRear | There are irrigation sprinklers to the rear of the lot. |
| Steep Slope | SteepSlope | The lot is sloped steeply. |
| Subdivided | Subdivided | The lot has been subdivided into two or more parcels. |
| Views | Views | There are views from the lot. |
| Waterfall | Waterfall | The lot has a waterfall. |
| Waterfront | Waterfront | The lot is located on a waterfront. |
| Wetlands | Wetlands | The lot is located near or within wetlands. |
| Wooded | Wooded | The lot is wooded. |
| Zero Lot Line | ZeroLotLine | The structure comes up to or very near the property line. |

## lot_size_source

- Source name: `LotSizeSource`
- Kind: **closed-SV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LotSizeSource/)
- Used by:
  - `property.lot_size_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | An appraiser provided the measurement of the lot size. |
| Assessor | Assessor | The assessor provided the measurement of the lot size. |
| Builder | Builder | The builder provided the measurement of the lot size. |
| Estimated | Estimated | The measurement of the lot size is an estimate. |
| Other | Other | The measurement of the lot size was provided by another party not listed. |
| Owner | Owner | The owner provided the measurement of the lot size. |
| Plans | Plans | The measurement of the lot size was taken from building plans. |
| Public Records | PublicRecords | The measurement of the lot size was received from public records. |
| See Remarks | SeeRemarks | See remarks for information about the source of the lot size measurement. |

## lot_size_units

- Source name: `LotSizeUnits`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/LotSizeUnits/)
- Used by:
  - `property.lot_size_units` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Acres | Acres | The value reported in the Lot Size Area field is in acres. |
| Square Feet | SquareFeet | The value reported in the Lot Size Area field is in square feet. |
| Square Meters | SquareMeters | The value reported in the Lot Size Area field is in square meters. |

## media_alteration

- Source name: `MediaAlteration`
- Kind: **closed-MV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MediaAlteration/)
- Used by:
  - `media.media_alteration` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Decluttered - Item Removed | DeclutteredItemRemoved | Removal of items that may be deceitful or depict a listing inaccuracy in some way, including the removal of items beyond the homeowner's control, such as power lines, poor views or unsightly property conditions. |
| Model Home | ModelHome | A representative home, apartment or office space used as part of a sales campaign to demonstrate the design, structure and appearance of the dwelling. |
| None | None | There has been no alteration or fabrication of the image. |
| Other Media Modification | OtherMediaModification | The image has been altered in some other way than is noted in this list of lookup values. |
| Twilight Conversion | TwilightConversion | If the sun is placed in the wrong location, a viewer may believe that certain rooms or amenities (e.g., pool, sunroom) will receive a misrepresented amount of sunlight or particular view at a time of day. |
| Virtual Enhancements | VirtualEnhancements | Visual enhancements may include changing the sky color or greening the grass, but these enhancements should be disclosed if they are deceptive (e.g., adding green grass where healthy grass cannot grow). |
| Virtual Renovation | VirtualRenovation | Undisclosed, this can mislead a buyer into thinking the property has already been renovated and that there are no more expenses necessary to reach that state. |
| Virtual Representation - To Be Built | VirtualRepresentationToBeBuilt | Undisclosed, a buyer may not realize that this is an artist rendering and not an actual build. |
| Virtual Representation - Under Construction | VirtualRepresentationUnderConstruction | Undisclosed, a buyer may not realize that this is an artist rendering and not an actual build in progress. |
| Virtual Staging - Item Addition | VirtualStagingItemAddition | Addition of virtual items or depictions that may misrepresent what is part of the property, the condition of the property or proportions/sizes of rooms or amenities. |

## media_category

- Source name: `MediaCategory`
- Kind: **closed-SV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MediaCategory/)
- Used by:
  - `media.media_category` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent Photo | AgentPhoto | The media is an agent photo. |
| Branded Virtual Tour | BrandedVirtualTour | The media is a branded virtual tour. |
| Document | Document | The media is a document. |
| Floor Plan | FloorPlan | The media is a floor plan. |
| Office Logo | OfficeLogo | The media is an office logo. |
| Office Photo | OfficePhoto | The media is an office photo. |
| Photo | Photo | The media is a photo. |
| Unbranded Virtual Tour | UnbrandedVirtualTour | The media is an unbranded virtual tour. |
| Video | Video | The media is a video. |

## media_status

- Source name: `MediaStatus`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MediaStatus/)
- Used by:
  - `media.media_status` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## media_type

- Source name: `MediaType`
- Kind: **closed-SV**
- Value count: 16
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MediaType/)
- Used by:
  - `media.media_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| doc | Doc | The media is a Microsoft Word .doc file type. |
| docx | Docx | The media is a Microsoft Word docx file type. |
| gif | Gif | The media is a .gif file type. |
| jpeg | Jpeg | The media is a jpeg (or jpg) file type. |
| mov | Mov | The media is a .mov file type. |
| mp4 | Mp4 | The media is an .mp4 file type. |
| mpeg | Mpeg | The media is an .mpeg (or .mpg) file type. |
| pdf | Pdf | The media is a .pdf file type. |
| png | Png | The media is a .png file type. |
| quicktime | Quicktime | The media is a QuickTime file type. |
| rtf | Rtf | The media is an .rtf file type. |
| tiff | Tiff | The media is a .tiff (or .tif) file type. |
| txt | Txt | The media is a .txt file type. |
| wmv | Wmv | The media is a .wmv file type. |
| xls | Xls | The media is a Microsoft Excel .xls file type. |
| xlsx | Xlsx | The media is a Microsoft Excel .xlsx file type. |

## member_association_bill_status

- Source name: `MemberAssociationBillStatus`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberAssociationBillStatus/)
- Used by:
  - `member_association.member_association_bill_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Billed | Billed | The member has been billed by an association of REALTORS®. |
| Not Billed | NotBilled | The member has not been billed by an association of REALTORS®. |
| Paid | Paid | The member has paid an association of REALTORS®. |

## member_designation

- Source name: `MemberDesignation`
- Kind: **closed-MV**
- Value count: 27
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberDesignation/)
- Used by:
  - `member.member_designation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accredited Buyer's Representative / ABR | AccreditedBuyersRepresentative | The Accredited Buyer's Representative (ABR®) designation is designed for real estate buyer agents who focus on working directly with buyer-clients. |
| Accredited Land Consultant / ALC | AccreditedLandConsultant | Accredited Land Consultants (ALCs) are the most trusted, knowledgeable, experienced and highest-producing experts in all segments of land. |
| At Home With Diversity / AHWD | AtHomeWithDiversity | Learn to work effectively with and within today's diverse real estate market. |
| Certified Commercial Investment Member / CCIM | CertifiedCommercialInvestmentMember | The Certified Commercial Investment Member (CCIM) designation is commercial real estate's global standard for professional achievement, earned through an extensive curriculum of 200 classroom hours and professional experiential requirements. |
| Certified Distressed Property Expert / CDPE | CertifiedDistressedPropertyExpert | A Certified Distressed Property Expert® (CDPE) has a thorough understanding of complex issues in today's turbulent real estate industry and knowledge of foreclosure avoidance options available to homeowners. |
| Certified International Property Specialist / CIPS | CertifiedInternationalPropertySpecialist | The CIPS designation is for REALTORS® from the United States and abroad, as well as association staff and volunteer leaders who wish to develop or grow their international real estate business. |
| Certified Property Manager / CPM | CertifiedPropertyManager | Certified Property Managers® (CPM®) are recognized as experts in real estate management, and they are at the top of the profession. |
| Certified Real Estate Brokerage Manager / CRB | CertifiedRealEstateBrokerageManager | The Certified Real Estate Brokerage Manager (CRB) Designation raises professional standards, strengthens individual and office performance, and indicates expertise in brokerage management. |
| Certified Real Estate Team Specialist / C-RETS | CertifiedRealEstateTeamSpecialist | The Certified Real Estate Team Specialist certification is designed to improve team development, individual leadership skills and financial performance. |
| Certified Residential Specialist / CRS | CertifiedResidentialSpecialist | Certified Residential Specialist (CRS) is the highest credential awarded to residential sales agents, managers and brokers. |
| Counselor of Real Estate / CRE | CounselorOfRealEstate | The Counselors of Real Estate® (CRE®) is an international group of recognized professionals who provide seasoned, expert, objective advice on real property and land-related matters. |
| General Accredited Appraiser / GAA | GeneralAccreditedAppraiser | For general appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Graduate, REALTOR Institute / GRI | GraduateRealtorInstitute | REALTORS® with the GRI designation have in-depth training in legal and regulatory issues, technology, professional standards, and the sales process. |
| Military Relocation Professional / MRP | MilitaryRelocationProfessional | The National Association of REALTORS® Military Relocation Professional certification focuses on educating real estate professionals about working with current and former military service members to find housing solutions that best suit their needs and take full advantage of military benefits and support. |
| NAR's Green Designation / GREEN | NARsGreenDesignation | Through the National Association of REALTORS® Green designation, the Green Resource Council provides ongoing education, resources and tools to help real estate practitioners find, understand and market properties with green features. |
| Performance Management Network / PMN | PerformanceManagementNetwork | This designation is unique to the REALTOR® family of designations, emphasizing that in order to enhance your business, you must enhance yourself. |
| Pricing Strategy Advisor / PSA | PricingStrategyAdvisor | Enhance your skills in pricing properties, creating CMAs (comparative market analysis), working with appraisers and guiding clients through the anxieties and misperceptions they often have about home values with the National Association of REALTORS® PSA (Pricing Strategy Advisor) certification. |
| REALTOR Association Certified Executive / RCE | RealtorAssociationCertifiedExecutive | The REALTOR® Association Certified Executive (RCE) is the only professional designation designed specifically for REALTOR® association executives. |
| Real Estate Negotiation Expert / RENE | RealEstateNegotiationExpert | This certification is for real estate professionals who want to sharpen their negotiation skills. |
| Residential Accredited Appraiser / RAA | ResidentialAccreditedAppraiser | For residential appraisers, this designation is awarded to those whose education and experience exceed state appraisal certification requirements and is supported by the National Association of REALTORS®. |
| Resort & Second-Home Property Specialist / RSPS | ResortAndSecondHomePropertySpecialist | This certification is designed for REALTORS® who facilitate the buying, selling or management of properties for investment, development, retirement or second homes in a resort, recreational and/or vacation destination. |
| Seller Representative Specialist / SRS | SellerRepresentativeSpecialist | The Seller Representative Specialist (SRS) designation is the premier credential in seller representation. |
| Seniors Real Estate Specialist / SRES | SeniorsRealEstateSpecialist | The Seniors Real Estate Specialist (SRES®) designation program educates REALTORS® on how to profitably and ethically serve the real estate needs of the fastest-growing market in real estate, clients age 50+. |
| Short Sales & Foreclosure Resource / SFR | ShortSalesAndForeclosureResource | The Short Sales & Foreclosure Resource (SFR®) certification teaches real estate professionals to work with distressed sellers and the finance, tax and legal professionals who can help them. |
| Society of Industrial and Office REALTORS / SIOR | SocietyOfIndustrialAndOfficeRealtors | The Society of Industrial and Office REALTORS® (SIOR) designation is held by only the most knowledgeable, experienced and successful commercial real estate brokerage specialists. |
| Transnational Referral Certification / TRC | TransnationalReferralCertification | Real estate professionals who have taken the Transnational Referral Certified (TRC) training, have completed special training on making and receiving client referrals from professionals in other countries. |
| e-PRO | ePRO | The National Association of REALTORS® e-PRO® certification teaches you to use cutting-edge technologies and digital initiatives to link up with today's savvy real estate consumer. |

## member_mls_security_class

- Source name: `MemberMlsSecurityClass`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberMlsSecurityClass/)
- Used by:
  - `member.member_mls_security_class` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## member_other_phone_type

- Source name: `MemberOtherPhoneType`
- Kind: **closed-SV**
- Value count: 14
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberOtherPhoneType/)
- Used by:
  - `member.member_other_phone_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Direct | Direct | This direct number of the member. |
| Fax | Fax | The fax number of the member. |
| First | First | The preferred phone number of the member. |
| Home | Home | The home phone number of the member. |
| Mobile | Mobile | The mobile phone number of the member. |
| Modem | Modem | The modem of the member. |
| Office | Office | The office phone number of the member. |
| Pager | Pager | The pager number of the member. |
| Preferred | Preferred | The preferred phone number of the member. |
| SMS | Sms | The Short Message Service (SMS)/text number of the member. |
| Second | Second | The second preferred phone number of the member. |
| Third | Third | The third preferred phone number of the member. |
| Toll Free | TollFree | The toll-free phone number of the member. |
| Voicemail | Voicemail | The voicemail of the member. |

## member_state_license_type

- Source name: `MemberStateLicenseType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberStateLicenseType/)
- Used by:
  - `member_state_license.member_state_license_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | The member state license type is appraiser. |
| Broker | Broker | The member state license type is broker. |
| Salesperson | Salesperson | The member state license type is salesperson. |

## member_status

- Source name: `MemberStatus`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberStatus/)
- Used by:
  - `member.member_status` (type=`String List, Single`)
  - `member_association.member_association_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The member's account is active. |
| Inactive | Inactive | the member's account is not active. |

## member_type

- Source name: `MemberType`
- Kind: **closed-SV**
- Value count: 19
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MemberType/)
- Used by:
  - `member.member_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Affiliate | Affiliate | The member is affiliated with the real estate industry in some manner (e.g., home inspector, photographer, mortgage consultant) but is not necessarily a REALTOR®. |
| Assistant | Assistant | The member is an assistant. |
| Association Staff | AssociationStaff | The member is a member of an association's staff. |
| Designated REALTOR Appraiser | DesignatedRealtorAppraiser | The member is a designated appraiser and a member of the National Association of REALTORS® (NAR). |
| Designated REALTOR Participant | DesignatedRealtorParticipant | The member is a designated broker and a member of the National Association of REALTORS® (NAR). |
| Leasing Agent | LeasingAgent | The member holds a leasing license. |
| Licensed Assistant | LicensedAssistant | The member is a licensed assistant. |
| MLS Only Appraiser | MlsOnlyAppraiser | The member is an appraiser and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| MLS Only Broker | MlsOnlyBroker | The member is a broker and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| MLS Only Broker Associate | MlsOnlyBrokerAssociate | The member is a broker and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| MLS Only Salesperson | MlsOnlySalesperson | The member is a salesperson and not a member of the National Association of REALTORS® (NAR), receiving MLS services only. |
| MLS Staff | MlsStaff | The individual is a member of MLS staff. |
| Non Member/Vendor | NonMemberVendor | The individual is not a member or is a vendor. |
| Office Manager | OfficeManager | The member is a licensed office manager. |
| Photographer | Photographer | The member is a photographer. |
| REALTOR Appraiser | RealtorAppraiser | The member is an appraiser and a member of the National Association of REALTORS® (NAR). |
| REALTOR Broker Associate | RealtorBrokerAssociate | The member has a broker's license but is working under a broker and is a member of the National Association of REALTORS® (NAR). |
| REALTOR Salesperson | RealtorSalesperson | The member is a sales person and a member of the National Association of REALTORS® (NAR). |
| Unlicensed Assistant | UnlicensedAssistant | The member is an unlicensed assistant. |

## middle_or_junior_school

- Source name: `MiddleOrJuniorSchool`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MiddleOrJuniorSchool/)
- Used by:
  - `property.middle_or_junior_school` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## middle_or_junior_school_district

- Source name: `MiddleOrJuniorSchoolDistrict`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MiddleOrJuniorSchoolDistrict/)
- Used by:
  - `property.middle_or_junior_school_district` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## mls_area_major

- Source name: `MLSAreaMajor`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MLSAreaMajor/)
- Used by:
  - `property.mls_area_major` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## mls_area_minor

- Source name: `MLSAreaMinor`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MLSAreaMinor/)
- Used by:
  - `property.mls_area_minor` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## mls_status

- Source name: `MlsStatus`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/MlsStatus/)
- Used by:
  - `property.mls_status` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## noted_by

- Source name: `NotedBy`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/NotedBy/)
- Used by:
  - `contact_listing_notes.noted_by` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The agent has written the given note about the given listing. |
| Contact | Contact | The contact has written the given note about the given listing. |

## object_id_type

- Source name: `ObjectIdType`
- Kind: **closed-SV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ObjectIdType/)
- Used by:
  - `internet_tracking.object_id_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| ListingId | ListingId | The ObjectID is the MLS listing number. |
| ListingKey | ListingKey | The object is a key field from an MLS system. |
| OpenHouseId | OpenHouseId | The ObjectID is an open house ID. |
| OpenHouseKey | OpenHouseKey | The ObjectID is the key of an open house record. |
| ParcelNumber | ParcelNumber | When no listing exists or the tracking is property-centric, the ObjectIdType of the property's parcel number is used. |
| SavedSearchKey | SavedSearchKey | When the event is the execution of a saved search, the ObjectID will be the SavedSearchKey from the system that executed the search. |
| UPI | Upi | When no listing exists and the tracking is property-centric, the RESO Universal Property Identifier (UPI) is used. |
| Unique | Unique | The ObjectID is a unique ID supplied by the source and is not one of the other types. |

## object_type

- Source name: `ObjectType`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ObjectType/)
- Used by:
  - `internet_tracking.object_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Document | Document | The object of the tracking event is a document. |
| Listing | Listing | The object of the tracking event is a real estate listing. |
| Open House | OpenHouse | The object of the tracking event is an open house event. |
| Photo | Photo | The object of the tracking event is a photo. |
| Property | Property | When no listing exists or the tracking is property-centric, the ObjectType of Property is used. |
| Saved Search | SavedSearch | When the event is the execution of a saved search, the ObjectType will be a Saved Search from the system that executed the search. |
| Virtual Tour | VirtualTour | The object of the tracking event is considered a virtual tour. |

## occupant_type

- Source name: `OccupantType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OccupantType/)
- Used by:
  - `property.occupant_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Owner | Owner | The occupant is the owner. |
| Tenant | Tenant | The occupant is a tenant. |
| Vacant | Vacant | The property is vacant. |

## office_association_primary_indicator

- Source name: `OfficeAssociationPrimaryIndicator`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OfficeAssociationPrimaryIndicator/)
- Used by:
  - `office_association.office_association_primary_indicator` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Not Applicable | NotApplicable | The office status as primary, secondary, etc., is not applicable. |
| Primary | Primary | The office is primary with the related association. |
| Secondary | Secondary | The office is secondary with the related association. |
| Tertiary | Tertiary | The office is tertiary with the related association. |

## office_branch_type

- Source name: `OfficeBranchType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OfficeBranchType/)
- Used by:
  - `office.office_branch_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Branch | Branch | This office is a branch office. |
| Main | Main | This office is the broker's main office. |
| Stand Alone | StandAlone | This office is a stand-alone or single-office brokerage. |

## office_corporate_license_type

- Source name: `OfficeCorporateLicenseType`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OfficeCorporateLicenseType/)
- Used by:
  - `office_corporate_license.office_corporate_license_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | The office corporate license type is appraiser. |
| Broker | Broker | The office corporate license type is broker. |

## office_status

- Source name: `OfficeStatus`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OfficeStatus/)
- Used by:
  - `office.office_status` (type=`String List, Single`)
  - `office_association.office_association_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The member office's account is active. |
| Inactive | Inactive | The member office's account is not active. |

## office_type

- Source name: `OfficeType`
- Kind: **closed-SV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OfficeType/)
- Used by:
  - `office.office_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Affiliate | Affiliate | The record in the office roster is an affiliate office. |
| Appraiser | Appraiser | The record in the office roster is an appraiser office. |
| Association | Association | The record in the office roster is an association office. |
| MLS | Mls | The record in the office roster is an MLS office. |
| MLS Only Branch | MlsOnlyBranch | The record in the office roster is a broker branch office who receives only MLS service. |
| MLS Only Firm | MlsOnlyFirm | The record in the office roster is a broker firm office that receives only MLS service. |
| MLS Only Office | MlsOnlyOffice | The record in the office roster is a broker office that receives only MLS service. |
| Non Member/Vendor | NonMemberVendor | The record in the office roster is a nonmember/vendor office. |
| Realtor Branch Office | RealtorBranchOffice | The record in the office roster is a REALTOR® branch office. |
| Realtor Firm | RealtorFirm | The record in the office roster is a REALTOR® firm office. |
| Realtor Office | RealtorOffice | The record in the office roster is a REALTOR® office. |

## open_house_status

- Source name: `OpenHouseStatus`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OpenHouseStatus/)
- Used by:
  - `open_house.open_house_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The open house is active and continuing as scheduled. |
| Canceled | Canceled | The open house has been canceled. |
| Ended | Ended | The open house has ended and is past the scheduled open house date and time. |

## open_house_type

- Source name: `OpenHouseType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OpenHouseType/)
- Used by:
  - `open_house.open_house_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Broker | Broker | The open house is only open to brokers and, at times, agents. |
| Livestream Broker | LivestreamBroker | The open house is livestreamed and only open to brokers and, at times, agents. |
| Livestream Public | LivestreamPublic | The open house is livestreamed and open to the general public. |
| Office | Office | The open house is only open to the members of a particular office or offices. |
| Public | Public | The open house is open to the general public. |

## operating_expense_includes

- Source name: `OperatingExpenseIncludes`
- Kind: **closed-MV**
- Value count: 33
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OperatingExpenseIncludes/)
- Used by:
  - `property.operating_expense_includes` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accounting | Accounting | The operating expense amount includes accounting costs. |
| Advertising | Advertising | The operating expense amount includes advertising costs. |
| Association | Association | The operating expense amount includes association costs. |
| Cable TV | CableTv | The operating expense amount includes cable TV costs. |
| Capital Improvements | CapitalImprovements | The operating expense amount includes capital improvements costs. |
| Depreciation | Depreciation | The operating expense amount includes depreciation costs. |
| Equipment Rental | EquipmentRental | The operating expense amount includes equipment rental costs. |
| Fuel | Fuel | The operating expense amount includes fuel costs. |
| Furniture Replacement | FurnitureReplacement | The operating expense amount includes furniture replacement costs. |
| Gardener | Gardener | The operating expense amount includes gardener costs. |
| Insurance | Insurance | The operating expense amount includes insurance costs. |
| Legal | Legal | The operating expense amount includes legal costs. |
| Licenses | Licenses | The operating expense amount includes license costs. |
| Maintenance | Maintenance | The operating expense amount includes maintenance costs. |
| Maintenance Grounds | MaintenanceGrounds | The operating expense amount includes maintenance grounds costs. |
| Maintenance Structure | MaintenanceStructure | The operating expense amount includes maintenance structure costs. |
| Manager | Manager | The operating expense amount includes manager costs. |
| Mortgage/Loans | MortgageLoans | The operating expense amount includes mortgage/loan costs. |
| New Tax | NewTax | The operating expense amount includes new tax costs. |
| Other | Other | The operating expense amount includes other costs. |
| Parking | Parking | The operating expense amount includes parking costs. |
| Pest Control | PestControl | The operating expense amount includes pest control costs. |
| Pool/Spa | PoolSpa | The operating expense amount includes pool/spa costs. |
| Professional Management | ProfessionalManagement | The operating expense amount includes professional management costs. |
| Security | Security | The operating expense amount includes security costs. |
| Snow Removal | SnowRemoval | The operating expense amount includes snow removal costs. |
| Staff | Staff | The operating expense amount includes staff costs. |
| Supplies | Supplies | The operating expense amount includes supplies costs. |
| Trash | Trash | The operating expense amount includes trash costs. |
| Utilities | Utilities | The operating expense amount includes utility costs. |
| Vacancy Allowance | VacancyAllowance | The operating expense amount includes vacancy allowance costs. |
| Water/Sewer | WaterSewer | The operating expense amount includes water/sewer costs. |
| Workmans Compensation | WorkmansCompensation | The operating expense amount includes workman's compensation costs. |

## organization_type

- Source name: `OrganizationType`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OrganizationType/)
- Used by:
  - `ouid.organization_type` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## other_equipment

- Source name: `OtherEquipment`
- Kind: **closed-MV**
- Value count: 21
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OtherEquipment/)
- Used by:
  - `property.other_equipment` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Air Purifier | AirPurifier | The property includes an air purifier. |
| Call Listing Agent | CallListingAgent | Call the listing agent for more information about other equipment included with the property. |
| Compressor | Compressor | The property includes a compressor. |
| DC Well Pump | DcWellPump | The property includes a DC well pump. |
| Dehumidifier | Dehumidifier | The property includes a dehumidifier. |
| Farm Equipment | FarmEquipment | The property includes farm equipment. |
| Fuel Tank(s) | FuelTanks | The property includes a fuel tank or fuel tanks. |
| Generator | Generator | The property includes a generator. |
| Home Theater | HomeTheater | The property includes a home theater. |
| Intercom | Intercom | The property includes an intercom. |
| Irrigation Equipment | IrrigationEquipment | The property includes irrigation equipment. |
| List Available | ListAvailable | A list of other equipment included with the property is available upon request. |
| Livestock Equipment | LivestockEquipment | The property includes livestock equipment. |
| Negotiable | Negotiable | The other equipment included with the property is negotiable. |
| None | None | There is no other equipment included with the property. |
| Orchard Equipment | OrchardEquipment | The property includes orchard equipment. |
| Other | Other | The property includes equipment other than what's included on this list. |
| Rotary Antenna | RotaryAntenna | The property includes a rotary antenna. |
| Satellite Dish | SatelliteDish | The property includes a satellite dish. |
| TV Antenna | TvAntenna | The property includes a TV antenna. |
| Varies by Unit | VariesByUnit | The equipment included with the property varies from unit to unit. |

## other_phone_type

- Source name: `OtherPhoneType`
- Kind: **closed-SV**
- Value count: 14
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OtherPhoneType/)
- Used by:
  - `contacts.other_phone_type` (type=`String List, Single`)
  - `other_phone.other_phone_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Direct | Direct | This is the contact's direct number. |
| Fax | Fax | This is the contact's fax. |
| First | First | This is the contact's first preferred phone. |
| Home | Home | This is the contact's home phone. |
| Mobile | Mobile | This is the contact's mobile phone. |
| Modem | Modem | This is the contact's modem. |
| Office | Office | This is the contact's office phone. |
| Pager | Pager | This is the contact's pager. |
| Preferred | Preferred | This is the contact's preferred phone. |
| SMS | Sms | This is the contact's SMS/text number. |
| Second | Second | This is the contact's second preferred phone. |
| Third | Third | This is the contact's third preferred phone. |
| Toll Free | TollFree | This is the contact's toll-free number. |
| Voicemail | Voicemail | This is the contact's voicemail. |

## other_structures

- Source name: `OtherStructures`
- Kind: **closed-MV**
- Value count: 33
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OtherStructures/)
- Used by:
  - `property.other_structures` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Airplane Hangar | AirplaneHangar | The property includes an airplane hangar. |
| Arena | Arena | The property includes an arena. |
| Barn(s) | Barns | The property includes a barn or barns. |
| Boat House | BoatHouse | The property includes a boat house. |
| Cabana | Cabana | The property includes a cabana. |
| Cave(s) | Caves | The property includes a cave or caves. |
| Corral(s) | Corrals | The property includes a corral or corrals. |
| Covered Arena | CoveredArena | The property includes a covered arena. |
| Garage(s) | Garages | The property includes a garage or garages. |
| Gazebo | Gazebo | The property includes a gazebo. |
| Grain Storage | GrainStorage | The property includes grain storage. |
| Greenhouse | Greenhouse | The property includes a greenhouse. |
| Guest House | GuestHouse | The property includes a guest house. |
| Kennel/Dog Run | KennelDogRun | The property includes a kennel or dog run. |
| Mobile Home | MobileHome | The property includes a mobile home. |
| None | None | The property has no other structures. |
| Other | Other | The property includes a structure other than those included on this list. |
| Outbuilding | Outbuilding | The property includes an outbuilding. |
| Outdoor Kitchen | OutdoorKitchen | The property includes an outdoor kitchen. |
| Packing Shed | PackingShed | The property includes a packing shed. |
| Pergola | Pergola | The property includes a pergola. |
| Pool House | PoolHouse | The property includes a pool house. |
| Poultry Coop | PoultryCoop | The property includes a poultry coop. |
| RV/Boat Storage | RvBoatStorage | The property includes RV or boat storage. |
| Residence | Residence | The property includes a residence structure. |
| Second Garage | SecondGarage | The property includes a second garage. |
| Second Residence | SecondResidence | The property includes a second residence. |
| See Remarks | SeeRemarks | See the public or private remarks for information about other structures on the property. |
| Shed(s) | Sheds | The property includes a shed or sheds. |
| Stable(s) | Stables | The property includes a stable or stables. |
| Storage | Storage | The property includes storage. |
| Tennis Court(s) | TennisCourts | The property includes a tennis court or tennis courts. |
| Workshop | Workshop | The property includes a workshop. |

## owner_pays

- Source name: `OwnerPays`
- Kind: **closed-MV**
- Value count: 29
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OwnerPays/)
- Used by:
  - `property.owner_pays` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| All Utilities | AllUtilities | The owner/lessor pays for all utilities. |
| Association Fees | AssociationFees | The owner/lessor pays for association fees. |
| Cable TV | CableTv | The owner/lessor pays for cable television. |
| Common Area Maintenance | CommonAreaMaintenance | The owner/lessor pays for common area maintenance. |
| Electricity | Electricity | The owner/lessor pays for electricity. |
| Exterior Maintenance | ExteriorMaintenance | The owner/lessor pays for exterior maintenance. |
| Gas | Gas | The owner/lessor pays for gas. |
| Grounds Care | GroundsCare | The owner/lessor pays for grounds care. |
| HVAC Maintenance | HvacMaintenance | The owner/lessor pays for HVAC maintenance. |
| Hot Water | HotWater | The owner/lessor pays for hot water. |
| Insurance | Insurance | The owner/lessor pays for insurance. |
| Janitorial Service | JanitorialService | The owner/lessor pays for janitorial service. |
| Management | Management | The owner/lessor pays for management. |
| None | None | The owner/lessor pays for no utilities, services, etc. |
| Other | Other | The owner/lessor pays for items that are not included on this list. |
| Other Tax | OtherTax | The owner/lessor pays for other taxes. |
| Parking Fee | ParkingFee | The owner/lessor pays for parking fees. |
| Pest Control | PestControl | The owner/lessor pays for pest control. |
| Pool Maintenance | PoolMaintenance | The owner/lessor pays for pool maintenance. |
| Repairs | Repairs | The owner/lessor pays for repairs. |
| Roof Maintenance | RoofMaintenance | The owner/lessor pays for roof maintenance. |
| Security | Security | The owner/lessor pays for security. |
| See Remarks | SeeRemarks | See the listing's remarks for details on what the owner/lessor pays for. |
| Sewer | Sewer | The owner/lessor pays for sewer. |
| Snow Removal | SnowRemoval | The owner/lessor pays for snow removal. |
| Taxes | Taxes | The owner/lessor pays for taxes. |
| Telephone | Telephone | The owner/lessor pays for telephone. |
| Trash Collection | TrashCollection | The owner/lessor pays for trash collection. |
| Water | Water | The owner/lessor pays for water. |

## ownership_type

- Source name: `OwnershipType`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/OwnershipType/)
- Used by:
  - `property.ownership_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Corporation | Corporation | The ownership type of the business being sold is a corporation. |
| LLC | Llc | The ownership type of the business being sold is a limited liability corporation. |
| Partnership | Partnership | The ownership type of the business being sold is a partnership. |
| Sole Proprietor | SoleProprietor | The ownership type of the business being sold is a sole proprietor. |

## parking_features

- Source name: `ParkingFeatures`
- Kind: **closed-MV**
- Value count: 72
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ParkingFeatures/)
- Used by:
  - `property.parking_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Additional Parking | AdditionalParking | The property has additional parking. |
| Aggregate | Aggregate | While aggregate is a type of concrete, it is different in application, maintenance and durability. |
| Alley Access | AlleyAccess | The property has alley access. |
| Asphalt | Asphalt | The property has asphalt parking. |
| Assigned | Assigned | The property has assigned parking spaces. |
| Attached | Attached | The property has attached parking. |
| Attached Carport | AttachedCarport | The property has an attached carport. |
| Basement | Basement | A basement garage is partially or mostly below grade, with its entrance level with the basement floor. |
| Boat | Boat | The property has a space to park/store a boat. |
| Carport | Carport | The property has a carport. |
| Circular Driveway | CircularDriveway | The property has a circular driveway. |
| Common | Common | The property has common/shared parking. |
| Community Structure | CommunityStructure | The property has a community parking structure. |
| Concrete | Concrete | The property has concrete paved parking. |
| Converted Garage | ConvertedGarage | The property has a converted garage. |
| Covered | Covered | The property has covered parking. |
| Deck | Deck | The property has a deck for parking. |
| Deeded | Deeded | The property has deeded parking. |
| Detached | Detached | The property has detached parking. |
| Detached Carport | DetachedCarport | The property has a detached carport. |
| Direct Access | DirectAccess | The parking has direct access to the property or structure. |
| Drive Through | DriveThrough | The property has drive-through parking. |
| Driveway | Driveway | The property has a driveway. |
| Electric Gate | ElectricGate | The property has an electric gate. |
| Electric Vehicle Charging Station(s) | ElectricVehicleChargingStations | The property has one or more electric vehicle charging station. |
| Enclosed | Enclosed | The property has enclosed parking. |
| Garage | Garage | The property has a garage. |
| Garage Door Opener | GarageDoorOpener | The garage has an automatic garage door opener. |
| Garage Faces Front | GarageFacesFront | The property has a garage that faces the front of the property. |
| Garage Faces Rear | GarageFacesRear | The property has a garage that faces the rear of the property. |
| Garage Faces Side | GarageFacesSide | The property has a garage that faces the side of the property. |
| Gated | Gated | The property has gated parking. |
| Golf Cart Garage | GolfCartGarage | The property has a golf cart garage. |
| Gravel | Gravel | The property has parking on gravel. |
| Guest | Guest | The property has guest parking. |
| Heated Garage | HeatedGarage | The property has a heated garage. |
| Inside Entrance | InsideEntrance | The property has parking with an inside entrance. |
| Kitchen Level | KitchenLevel | The property has parking at the kitchen level. |
| Leased | Leased | The property has leased parking. |
| Lighted | Lighted | The property has lighted parking. |
| No Garage | NoGarage | The property has no garage. |
| None | None | The property does not include parking or no parking is available. |
| Off Site | OffSite | The property has off-site parking. |
| Off Street | OffStreet | The property has off-street parking. |
| On Site | OnSite | The property has on-site parking. |
| On Street | OnStreet | The property has on-street parking only. |
| Open | Open | The property has open or unassigned parking. |
| Other | Other | The property has parking features other than those included on this list. |
| Outside | Outside | The property has outside parking that is not enclosed. |
| Oversized | Oversized | The property has parking for oversized vehicles. |
| Parking Lot | ParkingLot | The property has access to a parking lot. |
| Parking Pad | ParkingPad | The property has a parking pad. |
| Paved | Paved | The property has paved parking. |
| Paver Block | PaverBlock | The property has parking on paver blocks. |
| Permit Required | PermitRequired | Parking at the property or on the street requires a permit. |
| Private | Private | The property has private parking. |
| RV Access/Parking | RvAccessParking | The property has access/parking for recreational vehicles. |
| RV Carport | RvCarport | The property has a carport for recreational vehicles. |
| RV Garage | RvGarage | The property has a garage for recreational vehicles. |
| RV Gated | RvGated | The property has gated parking for recreational vehicles. |
| Secured | Secured | The property has secure parking. |
| See Remarks | SeeRemarks | See remarks for additional information about parking. |
| Shared Driveway | SharedDriveway | The property has a shared driveway. |
| Side By Side | SideBySide | The property has side-by-side parking spaces. |
| Storage | Storage | The property has storage in the parking area. |
| Tandem | Tandem | The property has tandem parking. |
| Unassigned | Unassigned | The property has unassigned or open parking. |
| Underground | Underground | The property has underground parking. |
| Unpaved | Unpaved | The property has parking on an unpaved surface. |
| Valet | Valet | The property has valet parking available. |
| Varies by Unit | VariesByUnit | The parking varies from unit to unit. |
| Workshop in Garage | WorkshopInGarage | The property has a workshop in the garage. |

## patio_and_porch_features

- Source name: `PatioAndPorchFeatures`
- Kind: **closed-MV**
- Value count: 16
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PatioAndPorchFeatures/)
- Used by:
  - `property.patio_and_porch_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Awning(s) | Awnings | The property has one or more awnings. |
| Covered | Covered | The property has a covered patio or porch. |
| Deck | Deck | The property has a deck. |
| Enclosed | Enclosed | The property has an enclosed patio or porch. |
| Front Porch | FrontPorch | The property has a front porch. |
| Glass Enclosed | GlassEnclosed | The property has a glass-enclosed patio or porch. |
| None | None | The property has no patio or porch. |
| Other | Other | The property has a patio or porch feature other than what's included on this list. |
| Patio | Patio | The property has a patio. |
| Porch | Porch | The property has a porch. |
| Rear Porch | RearPorch | The property has a rear porch. |
| Screened | Screened | The property has a screened patio or porch. |
| See Remarks | SeeRemarks | See the remarks fields for more information on the patio or porch features of the property. |
| Side Porch | SidePorch | The property has a side porch. |
| Terrace | Terrace | The property has a terrace. |
| Wrap Around | WrapAround | The property has wraparound patio or porch. |

## permission

- Source name: `Permission`
- Kind: **closed-MV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Permission/)
- Used by:
  - `media.permission` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent Only | AgentOnly | The image or document is for agent use only. |
| Firm Only | FirmOnly | The image or document is for firm use only. |
| IDX | Idx | The image or document is acceptable for IDX use. |
| Office Only | OfficeOnly | The image or document is for office use only. |
| Private | Private | The image or document is private and should have limited distribution. |
| Public | Public | The image or document may be viewed by the public. |
| VOW | Vow | The image or document is okay for VOW use. |

## pets_allowed

- Source name: `PetsAllowed`
- Kind: **closed-MV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PetsAllowed/)
- Used by:
  - `property.pets_allowed` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Breed Restrictions | BreedRestrictions | There are breed restrictions on allowed pets. |
| Call | Call | Call to inquire about pet restrictions. |
| Cats OK | CatsOk | Cats are allowed. |
| Dogs OK | DogsOk | Dogs are allowed. |
| No | No | No pets are allowed. |
| Number Limit | NumberLimit | There is a limit on the number of pets allowed. |
| Size Limit | SizeLimit | There are size restrictions on allowed pets. |
| Yes | Yes | All pets are allowed. |

## pool_features

- Source name: `PoolFeatures`
- Kind: **closed-MV**
- Value count: 35
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PoolFeatures/)
- Used by:
  - `property.pool_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Above Ground | AboveGround | The pool is above ground. |
| Association | Association | The pool is an association pool. |
| Black Bottom | BlackBottom | The pool has a black bottom. |
| Cabana | Cabana | The pool has a cabana. |
| Community | Community | The pool is a community/shared pool. |
| Diving Board | DivingBoard | The pool has a diving board. |
| ENERGY STAR Qualified pool pump | EnergyStarQualifiedPoolPump | The pool has a qualified ENERGY STAR pool pump. |
| Electric Heat | ElectricHeat | The pool is heated by electricity. |
| Fenced | Fenced | The pool is fenced. |
| Fiberglass | Fiberglass | The pool is made of or lined with fiberglass. |
| Filtered | Filtered | The pool has a filtration system. |
| Gas Heat | GasHeat | The pool is heated by gas. |
| Gunite | Gunite | The pool has a gunite surface. |
| Heated | Heated | The pool is heated. |
| In Ground | InGround | The pool is built into the ground. |
| Indoor | Indoor | The pool is indoors or within a structure. |
| Infinity | Infinity | Also named a negative edge, zero edge or infinity edge, an infinity pool has one or more edges where water flows over the edge, creating a visual effect of water with no boundary. |
| Lap | Lap | The pool is specifically designed for swimming laps. |
| Liner | Liner | The pool has a liner. |
| None | None | There is no pool included with the property. |
| Other | Other | There are pool features other than those included on this list. |
| Outdoor Pool | OutdoorPool | The pool is outdoors. |
| Pool Cover | PoolCover | The pool has a cover. |
| Pool Sweep | PoolSweep | The pool has an automatic sweep or cleaner. |
| Pool/Spa Combo | PoolSpaCombo | The pool includes a spa. |
| Private | Private | The pool is privately owned and/or secluded. |
| Salt Water | SaltWater | The pool has a saltwater system. |
| Screen Enclosure | ScreenEnclosure | The pool has a screened enclosure. |
| See Remarks | SeeRemarks | See the remarks fields for more information about the pool. |
| Solar Cover | SolarCover | The pool has a solar cover. |
| Solar Heat | SolarHeat | The pool has some form of solar heating. |
| Sport | Sport | The pool has two shallow ends on opposite sides of the pool with a deeper center. |
| Tile | Tile | The pool is tiled. |
| Vinyl | Vinyl | The pool has a vinyl surface. |
| Waterfall | Waterfall | The pool has a waterfall. |

## possession

- Source name: `Possession`
- Kind: **closed-MV**
- Value count: 12
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Possession/)
- Used by:
  - `property.possession` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Close Of Escrow | CloseOfEscrow | Possession is passed to the buyer at the close of escrow. |
| Close Plus 1 Day | ClosePlus1Day | Possession is passed to the buyer one day after the close of escrow. |
| Close Plus 2 Days | ClosePlus2Days | Possession is passed to the buyer two days after the close of escrow. |
| Close Plus 3 Days | ClosePlus3Days | Possession is passed to the buyer three days after the close of escrow. |
| Close Plus 3 to 5 Days | ClosePlus3To5Days | Possession is passed to the buyer three to five days after the close of escrow. |
| Close Plus 30 Days | ClosePlus30Days | Possession is passed to the buyer 30 days after the close of escrow. |
| Negotiable | Negotiable | Timing of the passing of possession to the buyer is negotiable. |
| Other | Other | A type of possession not included on this list. |
| Rental Agreement | RentalAgreement | Possession is stipulated in the rental agreement. |
| See Remarks | SeeRemarks | See the listing/agent remarks for more information on possession. |
| Seller Rent Back | SellerRentBack | Possession is determined by the details of the seller rent-back agreement. |
| Subject To Tenant Rights | SubjectToTenantRights | The terms of the transfer of possession are subject to the rights of the current tenant. |

## postal_city

- Source name: `PostalCity`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PostalCity/)
- Used by:
  - `property.postal_city` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## power_production_annual_status

- Source name: `PowerProductionAnnualStatus`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PowerProductionAnnualStatus/)
- Used by:
  - `property_power_production.power_production_annual_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Actual | Actual | Annual production derived from 12 or more months of actual data. |
| Estimated | Estimated | Annual production as estimated at the time or before the system began operation. |
| Partially Estimated | PartiallyEstimated | Annual production derived from less than 12 months of actual data, and therefore extrapolated to estimate annual production. |

## power_production_ownership

- Source name: `PowerProductionOwnership`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PowerProductionOwnership/)
- Used by:
  - `property_power_production.power_production_ownership` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Seller Owned | SellerOwned | The selected power production system is owned by the seller of the property. |
| Third-Party Owned | ThirdPartyOwned | The selected power production system is owned by a third party (e.g., Leased, Power Purchase Agreement). |

## power_production_type

- Source name: `PowerProductionType`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PowerProductionType/)
- Used by:
  - `property.power_production_type` (type=`String List, Multi`)
  - `property_power_production.power_production_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Photovoltaics | Photovoltaics | Solar photovoltaic (PV) devices which generate electricity directly from sunlight via an electronic process that occurs naturally in certain types of material, called semiconductors. |
| Wind | Wind | Renewable form of onsite power generation. |

## power_storage_type

- Source name: `PowerStorageType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PowerStorageType/)
- Used by:
  - `property_power_storage.power_storage_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Lead Acid Battery | LeadAcidBattery | The power storage type is lead acid battery. |
| Lithium Ion Battery | LithiumIonBattery | The power storage type is lithium ion battery. |
| Lithium Iron Phosphate | LithiumIronPhosphate | The power storage type is lithium iron phosphate. |
| Other | Other | The power storage type is other. |
| Unknown | Unknown | The power storage type is something other than the given options |

## preferred_address

- Source name: `PreferredAddress`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PreferredAddress/)
- Used by:
  - `contacts.preferred_address` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Home | Home | The contact prefers the use of their home address. |
| Other | Other | The contact prefers the use of their other address. |
| Work | Work | The contact prefers the use of their work address. |

## preferred_mail

- Source name: `PreferredMail`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PreferredMail/)
- Used by:
  - `member.member_preferred_mail` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Home Address | HomeAddress | Send mail to the home address. |
| Mailing Address | MailingAddress | Send mail to the designated mailing address. |
| Office Mailing Address | OfficeMailingAddress | Send mail to the office's designated mailing address. |
| Office Street Address | OfficeStreetAddress | Send mail to office's street address. |

## preferred_media

- Source name: `PreferredMedia`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PreferredMedia/)
- Used by:
  - `member.member_preferred_media` (type=`String List, Single`)
  - `office.office_preferred_media` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Email | Email | Send media via email. |
| Fax | Fax | Send media via fax. |
| Mail | Mail | Send media via postal mail. |

## preferred_phone

- Source name: `PreferredPhone`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PreferredPhone/)
- Used by:
  - `contacts.preferred_phone` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Direct | Direct | The contact prefers the use of their direct phone. |
| Home | Home | The contact prefers the use of their home phone. |
| Mobile | Mobile | The contact prefers the use of their mobile phone. |
| Office | Office | The contact prefers the use of their office phone. |
| Other | Other | The contact prefers the use of their other phone. |
| Toll Free | TollFree | The contact prefers the use of their toll-free phone. |
| Voicemail | Voicemail | The contact prefers the use of their voicemail phone. |

## preferred_publication

- Source name: `PreferredPublication`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PreferredPublication/)
- Used by:
  - `member.member_preferred_publication` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Fax | Fax | Send publications via fax. |
| Home Address | HomeAddress | Send publications to the home address. |
| Mailing Address | MailingAddress | Send publications to the designated mailing address. |
| Office Mailing Address | OfficeMailingAddress | Send publications to the office mailing address. |
| Office Street Address | OfficeStreetAddress | Send publications to the office street address. |

## property_condition

- Source name: `PropertyCondition`
- Kind: **closed-MV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PropertyCondition/)
- Used by:
  - `property.property_condition` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Fixer | Fixer | The property is in need of moderate or extensive repair. |
| New Construction | NewConstruction | The property is newly built. |
| To Be Built | ToBeBuilt | The property has yet to be built. |
| Under Construction | UnderConstruction | The property is still under construction; building has not been completed. |
| Updated/Remodeled | UpdatedRemodeled | The property has been remodeled or updated is some fashion. |

## property_sub_type

- Source name: `PropertySubType`
- Kind: **closed-SV**
- Value count: 31
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PropertySubType/)
- Used by:
  - `property.property_sub_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agriculture | Agriculture | The property is for farming and agricultural activities. |
| Apartment | Apartment | A unit within a wholly owned structure of five or more units. |
| Boat Slip | BoatSlip | A place where you can tie up a boat or houseboat. |
| Business | Business | The property is designed for any type of business. |
| Cabin | Cabin | A single-family residence that may have limited utilities. |
| Co-Ownership | CoOwnership | Co-ownership indicates that the property is owned by two or more parties in which each party has an equal ownership interest and obtains ownership at the same time. |
| Condominium | Condominium | A unit within a structure where ownership is on a unit-by-unit basis. |
| Deeded Parking | DeededParking | A parking space (or spaces) that are owned and separate from a residence. |
| Duplex | Duplex | A multifamily structure that has two independent units with a shared wall or ceiling/floor. |
| Farm | Farm | A place where agricultural and similar activities take place, especially the growing of crops. |
| Hotel/Motel | HotelMotel | The property is designed for hotel or motel use. |
| Industrial | Industrial | The property is designed for industrial use. |
| Manufactured Home | ManufacturedHome | A factory-built house that is transported to the lot. |
| Manufactured On Land | ManufacturedOnLand | A factory-built house that is transported to the lot and sold with the land. |
| Mixed Use | MixedUse | The property is designed to be used in more than one way (i.e., office and retail). |
| Mobile Home | MobileHome | A factory-built house that is transported to the lot, retains axles and was built prior to June 15, 1976. |
| Mobile Home Park | MobileHomePark | A permanent area for a group of mobile homes, usually with fixed utilities. |
| Multi Family | MultiFamily | A structure or complex with five or more units that are individual dwellings. |
| Office | Office | The property is designed to be used as office space. |
| Own Your Own | OwnYourOwn | A unit within a structure where ownership is based on a partial deed and rights to occupy a unit. |
| Quadruplex | Quadruplex | A multifamily structure with four independent units with shared walls or ceilings/floors. |
| Ranch | Ranch | A place where agricultural and similar activities take place, especially the raising of livestock. |
| Retail | Retail | The property designed to be used as retail space. |
| Single Family Residence | SingleFamilyResidence | A single family residence on real property. |
| Stock Cooperative | StockCooperative | A unit within a structure where ownership is based on a share of stock and rights to occupy a unit. |
| Tenancy in Common | TenancyInCommon | Tenancy in Common (TIC) indicates that the property is owned by two or more parties in which each party has an ownership interest, which may or may not be equal, and may obtain ownership at different times. |
| Timeshare | Timeshare | A form of property ownership where a property is held by a number of people, each with the right of possession for a specified time interval. |
| Townhouse | Townhouse | A dwelling unit generally having two or more floors and attached to other similar units via party walls. |
| Triplex | Triplex | A multifamily structure with three independent units with shared walls or ceilings/floors. |
| Unimproved Land | UnimprovedLand | Commercial land that has not been built upon or improved. |
| Warehouse | Warehouse | The property is designed to be used for warehousing. |

## property_type

- Source name: `PropertyType`
- Kind: **closed-SV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/PropertyType/)
- Used by:
  - `property.property_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Business Opportunity | BusinessOpportunity | The property type of the listing is Business Opportunity. |
| Commercial Lease | CommercialLease | The property type of the listing is Commercial Lease. |
| Commercial Sale | CommercialSale | The property type of the listing is Commercial Sale. |
| Farm | Farm | The property type of the listing is Farm. |
| Land | Land | The property type of the listing is Land. |
| Manufactured In Park | ManufacturedInPark | The property type of the listing is Manufactured in Park. |
| Residential | Residential | The property type of the listing is Residential. |
| Residential Income | ResidentialIncome | The property type of the listing is Residential Income. |
| Residential Lease | ResidentialLease | The property type of the listing is Residential Lease. |

## queue_transaction_type

- Source name: `QueueTransactionType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/QueueTransactionType/)
- Used by:
  - `queue.queue_transaction_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Add | Add | The resource record being referenced by the queue does not yet exist in the target and is an addition. |
| Change | Change | The resource record being referenced by the queue exists in the target and is being modified. |
| Delete | Delete | The resource record being referenced by the queue exists in the target and is to be removed. |

## reason_active_or_disabled

- Source name: `ReasonActiveOrDisabled`
- Kind: **closed-SV**
- Value count: 16
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ReasonActiveOrDisabled/)
- Used by:
  - `prospecting.reason_active_or_disabled` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent Disabled | AgentDisabled | The agent has disabled this auto email. |
| Client Disabled | ClientDisabled | The auto email has been disabled by the client/recipient. |
| Concierge Notification | ConciergeNotification | The automated email is on hold pending concierge approval by the member and is temporarily disabled. |
| Final Ignored Warning | FinalIgnoredWarning | The final warning that the automated email has not been viewed by the client/recipient and may be inactivated due to being ignored but is still active. |
| Ignored | Ignored | The automated email was not viewed by the client/recipient in the time frame designated by the host system and has been disabled. |
| Initial Ignored Warning | InitialIgnoredWarning | The first warning that the auto email has not been viewed by the client/recipient. |
| Invalid | Invalid | The automated email is no longer valid per some conditions set by the host system and has been disabled. |
| No Listings Found | NoListingsFound | The automated email has not found any listings matching the criteria and has been disabled per the host system rules. |
| No Listings Found Warning | NoListingsFoundWarning | The automated email has not found any listings matching the criteria and may be disabled but is still active. |
| No One To Send To | NoOneToSendTo | There is no valid email address and the auto email has been inactivated. |
| Over Limit | OverLimit | The automated email has reached the limit of listing results as set by the host system and has been disabled. |
| Re-Activated | ReActivated | The automated email was previously disabled and has been set back to active. |
| Revised | Revised | The automated email has been revised and is active. |
| Search Failing | SearchFailing | The automated email's search criteria is failing, should be reviewed by the host system and has been disabled. |
| Welcome Email Ignored | WelcomeEmailIgnored | The initial automated email has not been viewed by the client/recipient and has been deactivated. |
| Welcome Email Ignored Warning | WelcomeEmailIgnoredWarning | The initial automated email has not been viewed by the client/recipient but is still active. |

## rent_includes

- Source name: `RentIncludes`
- Kind: **closed-MV**
- Value count: 13
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RentIncludes/)
- Used by:
  - `property.rent_includes` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| All Utilities | AllUtilities | Rent for the dwelling includes all utilities. |
| Cable TV | CableTv | Rent for the dwelling includes cable TV. |
| Electricity | Electricity | Rent for the dwelling includes electricity. |
| Gardener | Gardener | Rent for the dwelling includes gardening services. |
| Gas | Gas | Rent for the dwelling includes gas. |
| Internet | Internet | Rent for the dwelling includes Internet service. |
| Management | Management | Rent for the dwelling includes management. |
| None | None | Rent for the dwelling does not include other potential costs such as utilities, management, services, etc. |
| Other | Other | An item of what rent includes that is not on this list. |
| See Remarks | SeeRemarks | See the listing's remarks for details about things included in the rent. |
| Sewer | Sewer | Rent for the dwelling includes sewer. |
| Trash Collection | TrashCollection | Rent for the dwelling includes trash collection. |
| Water | Water | Rent for the dwelling includes water. |

## resource_name

- Source name: `ResourceName`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ResourceName/)
- Used by:
  - `contact_listings.resource_name` (type=`String List, Single`)
  - `media.resource_name` (type=`String List, Single`)
  - `other_phone.resource_name` (type=`String List, Single`)
  - `queue.resource_name` (type=`String List, Single`)
  - `rules.resource_name` (type=`String List, Single`)
  - `saved_search.resource_name` (type=`String List, Single`)
  - `social_media.resource_name` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Association | Association | This record is related to another record in the Association Resource. |
| Contacts | Contacts | This record is related to another record in the Contacts Resource. |
| Member | Member | This record is related to another record in the Member Resource. |
| Office | Office | This record is related to another record in the Office Resource. |
| Property | Property | This record is related to another record in the Property Resource. |

## response_types

- Source name: `ResponseTypes`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ResponseTypes/)
- Used by:
  - `internet_tracking_summary.response_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Events | Events | The client/server data exchange is working with event-level InternetTracking data. |
| Summary | Summary | The client/server are working with summary-level InternetTracking data. |

## road_frontage_type

- Source name: `RoadFrontageType`
- Kind: **closed-MV**
- Value count: 13
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoadFrontageType/)
- Used by:
  - `property.road_frontage_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Alley | Alley | The property fronts to an alley. |
| City Street | CityStreet | The property fronts to a city street. |
| County Road | CountyRoad | The property fronts to a county road. |
| Easement | Easement | The property fronts to an easement. |
| Freeway | Freeway | The property fronts to a freeway. |
| Highway | Highway | The property fronts to a highway. |
| Interstate | Interstate | The property fronts to an interstate. |
| None | None | The property does not have any road frontage. |
| Other | Other | The property fronts to a road other than those on this list. |
| Private Road | PrivateRoad | The property fronts to a private road. |
| See Remarks | SeeRemarks | See public or private remarks for details on the road frontage. |
| State Road | StateRoad | The property fronts to a state road. |
| Unimproved | Unimproved | The property's road frontage is unimproved. |

## road_responsibility

- Source name: `RoadResponsibility`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoadResponsibility/)
- Used by:
  - `property.road_responsibility` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Private Maintained Road | PrivateMaintainedRoad | The property's road is privately maintained. |
| Public Maintained Road | PublicMaintainedRoad | The property's road is publicly maintained. |
| Road Maintenance Agreement | RoadMaintenanceAgreement | The property has a road maintenance agreement. |

## road_surface_type

- Source name: `RoadSurfaceType`
- Kind: **closed-MV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoadSurfaceType/)
- Used by:
  - `property.road_surface_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Alley Paved | AlleyPaved | The property's road is a paved alley. |
| Asphalt | Asphalt | The property's road is asphalt. |
| Chip And Seal | ChipAndSeal | The property's road is chip and seal. |
| Concrete | Concrete | The property's road is concrete. |
| Dirt | Dirt | The property's road is dirt. |
| Gravel | Gravel | The property's road is gravel. |
| None | None | The property has no road. |
| Other | Other | The surface type of the property's road is something other than those on this list. |
| Paved | Paved | The property's road is paved. |
| See Remarks | SeeRemarks | See the public or private remarks for details on the road surface type. |
| Unimproved | Unimproved | The property's road is unimproved. |

## roof

- Source name: `Roof`
- Kind: **closed-MV**
- Value count: 34
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Roof/)
- Used by:
  - `property.roof` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aluminum | Aluminum | The roof is made wholly or partially of aluminum. |
| Asbestos Shingle | AsbestosShingle | The roof is made wholly or partially of asbestos shingles. |
| Asphalt | Asphalt | The roof is made wholly or partially of asphalt. |
| Bahama | Bahama | The roof is a Bahama roof. |
| Barrel | Barrel | The roof is a barrel roof. |
| Bituthene | Bituthene | The roof is made wholly or partially of Bituthene. |
| Built-Up | BuiltUp | The roof is wholly or partially a built-up roof system. |
| Composition | Composition | The roof is made wholly or partially of composition. |
| Concrete | Concrete | The roof is made wholly or partially of concrete. |
| Copper | Copper | The roof is made wholly or partially of copper. |
| Elastomeric | Elastomeric | The roof is made wholly or partially of elastomeric. |
| Fiberglass | Fiberglass | The roof is made wholly or partially of fiberglass. |
| Flat | Flat | The roof is wholly or partially flat. |
| Flat Tile | FlatTile | The roof is made wholly or partially of flat tile. |
| Foam | Foam | The roof is made wholly or partially of foam. |
| Green Roof | GreenRoof | The roof is wholly or partially a green roof. |
| Mansard | Mansard | The roof is made wholly or partially of mansard. |
| Membrane | Membrane | The roof is made wholly or partially of membrane. |
| Metal | Metal | The roof is made wholly or partially of metal. |
| Mixed | Mixed | The roof is made wholly or partially of mixed materials. |
| None | None | The roof materials are unstated, unknown or there are none. |
| Other | Other | The roof is made wholly or partially of materials other than those on this list. |
| Rolled/Hot Mop | RolledHotMop | The roof is made wholly or partially of rolled/hot mop. |
| Rubber | Rubber | The roof is made wholly or partially of rubber. |
| See Remarks | SeeRemarks | See the listing's remarks for details on the roof. |
| Shake | Shake | The roof is made wholly or partially of shake. |
| Shingle | Shingle | The roof is made wholly or partially of shingle. |
| Slate | Slate | The roof is made wholly or partially of slate. |
| Spanish Tile | SpanishTile | The roof is made wholly or partially of Spanish tile. |
| Stone | Stone | The roof is made wholly or partially of stone. |
| Synthetic | Synthetic | The roof is made wholly or partially of synthetic materials. |
| Tar/Gravel | TarGravel | The roof is made wholly or partially of tar/gravel. |
| Tile | Tile | The roof is made wholly or partially of tile. |
| Wood | Wood | The roof is made wholly or partially of wood. |

## room_length_width_source

- Source name: `RoomLengthWidthSource`
- Kind: **closed-SV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoomLengthWidthSource/)
- Used by:
  - `property_rooms.room_length_width_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | The length and width of the room were provided by an appraiser. |
| Assessor | Assessor | The length and width of the room were provided by the assessor. |
| Builder | Builder | The length and width of the room were provided by the builder. |
| Estimated | Estimated | The length and width of the room were estimated. |
| GIS Calculated | GisCalculated | The length and width of the room were calculated by a Geographic Information System (GIS). |
| Measured | Measured | The length and width of the room were measured. |
| Other | Other | The length and width of the room were provided by an other means than those included in this list. |
| Owner | Owner | The length and width of the room were provided by the owner. |
| Public Records | PublicRecords | The length and width of the room were taken from public records. |
| See Remarks | SeeRemarks | See the Public or Private Remarks for details on the source of the room's length and width measurements. |
| Survey | Survey | The length and width of the room were provided by survey. |

## room_level

- Source name: `RoomLevel`
- Kind: **closed-SV**
- Value count: 7
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoomLevel/)
- Used by:
  - `property_rooms.room_level` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Basement | Basement | The given room is located on the basement level. |
| First | First | The given room is located on the first level. |
| Lower | Lower | The given room is located on a lower level. |
| Main | Main | The given room is located on the main level. |
| Second | Second | The given room is located on the second level. |
| Third | Third | The given room is located on the third level. |
| Upper | Upper | The given room is located on an upper level. |

## room_type

- Source name: `RoomType`
- Kind: **closed-SV**
- Value count: 33
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RoomType/)
- Used by:
  - `property.room_type` (type=`String List, Multi`)
  - `property_rooms.room_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Basement | Basement | A floor of a building below ground level. |
| Bathroom | Bathroom | The first bathroom, when a primary bathroom is not designated. |
| Bathroom 1 | Bathroom1 | The first bathroom, when a primary bathroom is not designated. |
| Bathroom 2 | Bathroom2 | The second bathroom. |
| Bathroom 3 | Bathroom3 | The third bathroom. |
| Bathroom 4 | Bathroom4 | The fourth bathroom. |
| Bathroom 5 | Bathroom5 | The fifth bathroom. |
| Bedroom | Bedroom | The type of room is a bedroom. |
| Bedroom 1 | Bedroom1 | The first bedroom, when a primary bedroom is not designated. |
| Bedroom 2 | Bedroom2 | The second bedroom. |
| Bedroom 3 | Bedroom3 | The third bedroom. |
| Bedroom 4 | Bedroom4 | The fourth bedroom. |
| Bedroom 5 | Bedroom5 | The fifth bedroom. |
| Bonus Room | BonusRoom | A room that can be used for multiple purposes. |
| Den | Den | Typically a secluded comfortable room used as a study or entertainment room. |
| Dining Room | DiningRoom | A room in a home where meals are eaten. |
| Exercise Room | ExerciseRoom | A room that is specifically geared to contain exercise equipment. |
| Family Room | FamilyRoom | A comfortable room in a dwelling frequently used for leisure use. |
| Game Room | GameRoom | Typically a bonus room that is specifically equipped for game play. |
| Great Room | GreatRoom | Denotes a room space within an abode which combines the specific functions of several of the more traditional room spaces (e.g., family room, living room, study, etc.) into a singular unified space. |
| Gym | Gym | A room that, in addition to exercise equipment, has other characteristics of a gymnasium. |
| Kitchen | Kitchen | The room used for the preparation and storage of food; cookery. |
| Laundry | Laundry | A utility room specifically used for laundry equipment (washer and dryer). |
| Library | Library | A room that is specifically geared to house books and other media typically found in a library. |
| Living Room | LivingRoom | A room in a private house used for general social and leisure activities. |
| Loft | Loft | A loft can be an upper story or attic in a building, directly under the roof. |
| Master Bathroom | MasterBathroom | Typically the largest of the bathrooms and attached to the primary bedroom. |
| Master Bedroom | MasterBedroom | Typically the largest of the bedrooms with an attached bathroom. |
| Media Room | MediaRoom | A room that is specifically geared for the watching of movies, TV or other forms of multimedia. |
| Office | Office | A room used for business. |
| Sauna | Sauna | A small room or house designed as a place to experience dry or wet heat sessions, or an establishment with one or more of these and auxiliary facilities. |
| Utility Room | UtilityRoom | A room that usually contains laundry, HVAC (heating, ventilation and air conditioning), water heating or some other utilitarian equipment. |
| Workshop | Workshop | A room containing tools or equipment used for the manufacturing or repair of goods. |

## rule_format

- Source name: `RuleFormat`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RuleFormat/)
- Used by:
  - `rules.rule_format` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| $filter | OdataFilter | Business rules expressed utilizing the OData $filter syntax. |
| JavaScript | Javascript | Business rules expressed utilizing the JavaScript language. |
| REBR | Rebr | Real Estate Business Rule (REBR) notation, based on RuleSpeak-structured notation, uses a predictable syntax to allow humans to clearly and unambiguously specify real estate business rules. |
| RetsValidation | RetsValidation | Business rules expressed using the well defined RETS 1.9 Validation Expressions. |

## rule_type

- Source name: `RuleType`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/RuleType/)
- Used by:
  - `rules.rule_type` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## saved_search_type

- Source name: `SavedSearchType`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SavedSearchType/)
- Used by:
  - `saved_search.saved_search_type` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## schedule_type

- Source name: `ScheduleType`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ScheduleType/)
- Used by:
  - `prospecting.schedule_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| ASAP | Asap | The prospect will be sent automated emails as soon as possible through each day. |
| Daily | Daily | The prospect will be sent automated emails daily. |
| Monthly | Monthly | The prospect will be sent automated emails once per month. |

## search_query_exceptions

- Source name: `SearchQueryExceptions`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SearchQueryExceptions/)
- Used by:
  - `saved_search.search_query_exceptions` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## search_query_type

- Source name: `SearchQueryType`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SearchQueryType/)
- Used by:
  - `saved_search.search_query_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| $filter | OdataFilter | The query is in the form of Odata's $filter. |
| DMQL2 | Dmql2 | The query is in the form of DMQL2. |

## security_features

- Source name: `SecurityFeatures`
- Kind: **closed-MV**
- Value count: 28
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SecurityFeatures/)
- Used by:
  - `property.security_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 24 Hour Security | TwentyFourHourSecurity | The property has 24-hour security. |
| Building Security | BuildingSecurity | The property has building security. |
| Carbon Monoxide Detector(s) | CarbonMonoxideDetectors | The property has a carbon monoxide detector or detectors. |
| Closed Circuit Camera(s) | ClosedCircuitCameras | The property has a closed-circuit camera or cameras. |
| Fire Alarm | FireAlarm | The property has a fire alarm or fire alarms. |
| Fire Escape | FireEscape | The property has a fire escape. |
| Fire Sprinkler System | FireSprinklerSystem | The property has a fire sprinkler system. |
| Firewall(s) | Firewalls | The property has a firewall or firewalls. |
| Gated Community | GatedCommunity | The property is in a gated community. |
| Gated with Guard | GatedWithGuard | The property is in a gated community/area with guard service. |
| Key Card Entry | KeyCardEntry | The property or community has key card entry. |
| Other | Other | The property has security features other than those on this list. |
| Panic Alarm | PanicAlarm | The property has a panic alarm. |
| Prewired | Prewired | The property is prewired for a security system. |
| Secured Garage/Parking | SecuredGarageParking | The property has a secured garage or parking area. |
| Security Fence | SecurityFence | The property has a security fence. |
| Security Gate | SecurityGate | The property has a security gate. |
| Security Guard | SecurityGuard | The property or community has a security guard. |
| Security Lights | SecurityLights | The property has security lights. |
| Security Service | SecurityService | The property has a security service. |
| Security System | SecuritySystem | The property has a security system. |
| Security System Leased | SecuritySystemLeased | The property has a leased security system. |
| Security System Owned | SecuritySystemOwned | The property has an owned security system. |
| See Remarks | SeeRemarks | See the remarks fields for more information about the security features of the property. |
| Smoke Detector(s) | SmokeDetectors | The property has a smoke detector or smoke detectors. |
| Varies By Unit | VariesByUnit | The security features vary from unit to unit. |
| Window Bars | WindowBars | The property has window bars. |
| Window Bars with Quick Release | WindowBarsWithQuickRelease | The property has window bars with a quick-release mechanism. |

## sewer

- Source name: `Sewer`
- Kind: **closed-MV**
- Value count: 15
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Sewer/)
- Used by:
  - `property.sewer` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aerobic Septic | AerobicSeptic | The property has an aerobic septic. |
| Cesspool | Cesspool | The property has a cesspool. |
| Engineered Septic | EngineeredSeptic | The property has an engineered septic. |
| Holding Tank | HoldingTank | The property has a holding tank. |
| Mound Septic | MoundSeptic | The property has a mound septic. |
| None | None | The property has no sewer, septic or cesspool. |
| Other | Other | The property has a system other than sewer, septic or cesspool on this list. |
| Perc Test On File | PercTestOnFile | The property has a perc test on file. |
| Perc Test Required | PercTestRequired | The property requires a perc test. |
| Private Sewer | PrivateSewer | The property has a private sewer. |
| Public Sewer | PublicSewer | The property has a public sewer. |
| Septic Needed | SepticNeeded | The property needs a septic system. |
| Septic Tank | SepticTank | The property has a septic tank. |
| Shared Septic | SharedSeptic | The property has a shared septic. |
| Unknown | Unknown | The property's sewer/septic is unknown. |

## showing_appointment_method

- Source name: `ShowingAppointmentMethod`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingAppointmentMethod/)
- Used by:
  - `showing_appointment.showing_appointment_method` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| In-Person | InPerson | An in-person showing appointment is confirmed for this property. |
| Other | Other | A showing appointment type other than those available on this list is confirmed for this property. |
| Virtual | Virtual | A virtual showing appointment is confirmed for this property. |

## showing_appointment_status

- Source name: `ShowingAppointmentStatus`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingAppointmentStatus/)
- Used by:
  - `showing_appointment.showing_appointment_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Cancelled | Cancelled | The status of this appointment request is canceled. |
| Confirmed | Confirmed | The status of this appointment request is confirmed. |
| Denied | Denied | The status of this appointment request is denied. |
| Pending | Pending | The status of this appointment request is pending. |

## showing_considerations

- Source name: `ShowingConsiderations`
- Kind: **closed-MV**
- Value count: 14
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingConsiderations/)
- Used by:
  - `property.showing_considerations` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Day Sleeper | DaySleeper | The property has a tenant/occupant who sleeps during the day. |
| Electricity Not On | ElectricityNotOn | The property does not have electricity or the electricity is not turned on. |
| Inconsistent Cell Service | InconsistentCellService | There is inconsistent cellular service at the location of the property. |
| Limited Visibility From Road | LimitedVisibilityFromRoad | The property has limited visibility from the road. |
| Minimal Exterior Lighting | MinimalExteriorLighting | The property has minimal exterior lighting. |
| Minimal Interior Lighting | MinimalInteriorLighting | The property has minimal interior lighting. |
| No Exterior Lighting | NoExteriorLighting | The property has no exterior lighting. |
| No Heat | NoHeat | The property does not have an heating system or the heating system is turned off. |
| No Interior Lighting | NoInteriorLighting | The property has no interior lighting. |
| Occupied | Occupied | The property is currently occupied. |
| Pet(s) on Premises | PetsOnPremises | There are currently pets at the property. |
| Remote Location | RemoteLocation | The property is in a remote location. |
| Security System | SecuritySystem | The property has a security system that is a consideration when showing. |
| See Remarks | SeeRemarks | See remarks for more information about showing considerations for the property. |

## showing_contact_type

- Source name: `ShowingContactType`
- Kind: **closed-MV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingContactType/)
- Used by:
  - `property.showing_contact_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The showing contact is a licensed agent. |
| Occupant | Occupant | The showing contact is the occupant. |
| Owner | Owner | The showing contact is the owner. |
| Property Manager | PropertyManager | The showing contact is the property manager. |

## showing_days

- Source name: `ShowingDays`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingDays/)
- Used by:
  - `property.showing_days` (type=`String List, Multi`)

*No closed value list - jurisdiction-defined.*

## showing_method

- Source name: `ShowingMethod`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingMethod/)
- Used by:
  - `showing_availability.showing_method` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| In-Person | InPerson | In-person showings are allowed for this property. |
| Other | Other | Other types of showings are allowed for this property. |
| Virtual | Virtual | Virtual showings are allowed for this property. |

## showing_method_request

- Source name: `ShowingMethodRequest`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingMethodRequest/)
- Used by:
  - `showing_request.showing_method_request` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| In-Person | InPerson | An in-person showing has been requested for this property. |
| Other | Other | A showing type other than those available on this list has been requested for this property. |
| Virtual | Virtual | A virtual showing has been requested for this property. |

## showing_requestor

- Source name: `ShowingRequestor`
- Kind: **closed-MV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingRequestor/)
- Used by:
  - `showing_request.showing_requestor` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Agent | Agent | The role of the person making the request is an agent. |
| Consumer | Consumer | The role of the person making the request is a consumer. |
| Home Improvement Specialist | HomeImprovementSpecialist | The role of the person making the request is a home improvement specialist. |
| Home Inspector | HomeInspector | The role of the person making the request is a home inspector. |
| Home Security Provider | HomeSecurityProvider | The role of the person making the request is a home security provider. |
| Member Type | MemberType | The type of member (i.e., agent, broker, office manager, appraiser, REALTOR®, photographer, etc.) |
| Moving Storage | MovingStorage | The role of the person making the request works at a moving/storage company. |
| Occupant | Occupant | The role of the person making the request is an occupant. |
| Owner | Owner | The role of the person making the request is an owner. |
| Property Manager | PropertyManager | The role of the person making the request is a property manager. |
| Sales Office | SalesOffice | The role of the person making the request is a member of a sales office. |

## showing_request_type

- Source name: `ShowingRequestType`
- Kind: **closed-MV**
- Value count: 6
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingRequestType/)
- Used by:
  - `showing_request.showing_request_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Broker Preview | BrokerPreview | A broker preview showing request made on a property. |
| Broker Price Opinion | BrokerPriceOpinion | A broker price opinion showing request made on a property. |
| First | First | The first showing request being made on a property. |
| Inspection | Inspection | An inspection showing request made on a property. |
| Second | Second | The second showing request made on a property. |
| Walk-through | WalkThrough | A walk-through showing request made on the property. |

## showing_requirements

- Source name: `ShowingRequirements`
- Kind: **closed-MV**
- Value count: 18
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingRequirements/)
- Used by:
  - `property.showing_requirements` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 24 Hour Notice | TwentyFourHourNotice | A 24-hour notice is required to show the property. |
| Appointment Only | AppointmentOnly | Showing of the property is by appointment only. |
| Call Listing Agent | CallListingAgent | Call the listing agent to arrange a showing of the property. |
| Call Listing Office | CallListingOffice | Call the listing office to arrange a showing of the property. |
| Call Manager | CallManager | Call the property manager to arrange a showing of the property. |
| Call Owner | CallOwner | Call the property owner to arrange a showing of the property. |
| Call Tenant | CallTenant | Call the tenant/occupant directly to arrange a showing of the property. |
| Combination Lock Box | CombinationLockBox | The property has a combination lockbox for showing access. |
| Do Not Show | DoNotShow | Do not show this property. |
| Email Listing Agent | EmailListingAgent | Email the listing agent for more information about showing the property. |
| Key In Office | KeyInOffice | The key to access the property for showing must be retrieved from the listing or manager's office. |
| Lockbox | Lockbox | The property has an electronic lockbox for showing access. |
| No Lockbox | NoLockbox | There is no lockbox on the property. |
| No Sign | NoSign | The property has no "for sale" sign. |
| Restricted Hours | RestrictedHours | The times when the property may be shown are restricted. |
| See Remarks | SeeRemarks | See the remarks fields for more information about showing the property. |
| Showing Service | ShowingService | A service used by a listing broker to provide showing services of listed properties. |
| Text Listing Agent | TextListingAgent | Text message the listing agent to arrange a showing of the property. |

## showing_service_name

- Source name: `ShowingServiceName`
- Kind: **closed-SV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingServiceName/)
- Used by:
  - `property.showing_service_name` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aligned Showings | AlignedShowings | Showings for the listing are scheduled through Aligned Showings. |
| BrokerBay | BrokerBay | Showings for the listing are scheduled through BrokerBay. |
| Homesnap | HomeSnap | Showings for the listing are scheduled through HomeSnap. |
| Instashowing | InstaShowing | Showings for the listing are scheduled through Instashowing. |
| LocalShowing | LocalShowing | Showings for the listing are scheduled through Local Showing. |
| None | None | No showing service is used for the listing. |
| Other | Other | Showings for the listing are scheduled through a showing service other than those available on this list. |
| SentriKey Showing | SentrikeyShowing | Showings for the listing are scheduled through SentriKey Showing. |
| ShowingTime | ShowingTime | Showings for the listing are scheduled through ShowingTime. |
| Showingly | Showingly | Showings for the listing are scheduled through Showingly. |

## showing_status

- Source name: `ShowingStatus`
- Kind: **closed-SV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/ShowingStatus/)
- Used by:
  - `showing.showing_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Accepting Requests | AcceptingRequests | Showing requests are accepted. |
| No Showings | NoShowings | No showing requests are accepted. |
| On Hold | OnHold | Showing requests are temporarily not accepted. |
| Restricted Showings | RestrictedShowings | Showings are accepted with restrictions. |

## skirt

- Source name: `Skirt`
- Kind: **closed-MV**
- Value count: 19
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Skirt/)
- Used by:
  - `property.skirt` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aluminum | Aluminum | The mobile/manufactured home has a skirt made of aluminum. |
| Block | Block | The mobile/manufactured home has a skirt made of block. |
| Brick | Brick | The mobile/manufactured home has a skirt made of brick. |
| Combination | Combination | The mobile/manufactured home has a skirt made of a combination of materials. |
| Concrete | Concrete | The mobile/manufactured home has a skirt made of concrete. |
| Fiberglass | Fiberglass | The mobile/manufactured home has a skirt made of fiberglass. |
| Frame | Frame | The mobile/manufactured home has a skirt that is framed. |
| Glass | Glass | The mobile/manufactured home has a skirt made of glass. |
| Masonite | Masonite | The mobile/manufactured home has a skirt made of Masonite. |
| Metal | Metal | The mobile/manufactured home has a skirt made of metal. |
| None | None | The mobile/manufactured home does not have a skirt. |
| Other | Other | The mobile/manufactured home has a skirt made of materials other than those on this list. |
| Steel | Steel | The mobile/manufactured home has a skirt made of steel. |
| Stone | Stone | The mobile/manufactured home has a skirt made of stone. |
| Stucco | Stucco | The mobile/manufactured home has a skirt made of stucco. |
| Synthetic | Synthetic | The mobile/manufactured home has a skirt made of synthetic materials. |
| Unknown | Unknown | The mobile/manufactured home has a skirt made of unknown materials. |
| Vinyl | Vinyl | The mobile/manufactured home has a skirt made of vinyl. |
| Wood | Wood | The mobile/manufactured home has a skirt made of wood. |

## social_media_type

- Source name: `SocialMediaType`
- Kind: **closed-SV**
- Value count: 17
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SocialMediaType/)
- Used by:
  - `association.social_media_type` (type=`String List, Single`)
  - `contacts.social_media_type` (type=`String List, Single`)
  - `member.social_media_type` (type=`String List, Single`)
  - `ouid.organization_social_media_type` (type=`String List, Single`)
  - `office.social_media_type` (type=`String List, Single`)
  - `social_media.social_media_type` (type=`String List, Single`)
  - `teams.social_media_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Blog | Blog | Information pertaining to the blog of the member/office/contact. |
| Digg | Digg | Information pertaining to the Digg account of the member/office/contact. |
| Facebook | Facebook | Information pertaining to the Facebook account of the member/office/contact. |
| Facebook Messenger | FacebookMessenger | Information pertaining to the Facebook Messenger contact information of the member/office/contact. |
| GooglePlus | Googleplus | Information pertaining to the GooglePlus account of the member/office/contact. |
| Instagram | Instagram | Information pertaining to the Instagram account of the member/office/contact. |
| LinkedIn | Linkedin | Information pertaining to the LinkedIn account of the member/office/contact. |
| Pinterest | Pinterest | Information pertaining to the Pinterest account of the member/office/contact. |
| Reddit | Reddit | Information pertaining to the Reddit account of the member/office/contact. |
| Slack | Slack | Information pertaining to the Slack account of the member/office/contact. |
| Snapchat | Snapchat | Information pertaining to the Snapchat account of the member/office/contact. |
| StumbleUpon | Stumbleupon | Information pertaining to the StumbleUpon account of the member/office/contact. |
| Tumblr | Tumblr | Information pertaining to the Tumblr account of the member/office/contact. |
| Twitter | Twitter | Information pertaining to the X (formerly Twitter) account of the member/office/contact. |
| Website | Website | Information pertaining to the website of the member/office/contact. |
| YouTube | Youtube | Information pertaining to the YouTube account of the member/office/contact. |
| iMessage | iMessage | Information pertaining to the iMessage contact information of the member/office/contact. |

## spa_features

- Source name: `SpaFeatures`
- Kind: **closed-MV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SpaFeatures/)
- Used by:
  - `property.spa_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Above Ground | AboveGround | The spa is not built into the ground. |
| Bath | Bath | The bath has a built-in spa or jets. |
| Community | Community | The property has access to a community spa. |
| Fiberglass | Fiberglass | The spa is lined or made of fiberglass. |
| Gunite | Gunite | The spa is lined with gunite. |
| Heated | Heated | The spa is heated. |
| In Ground | InGround | The spa is built into the ground. |
| None | None | The property has no spa. |
| Private | Private | The spa is privately owned or is secluded. |
| See Remarks | SeeRemarks | See the remarks fields for more information about the spa. |

## special_licenses

- Source name: `SpecialLicenses`
- Kind: **closed-MV**
- Value count: 13
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SpecialLicenses/)
- Used by:
  - `property.special_licenses` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Beer/Wine | BeerWine | The business being sold uses/requires a beer/wine license. |
| Class H | ClassH | The business being sold uses/requires a Class H license. |
| Entertainment | Entertainment | The business being sold uses/requires an entertainment license. |
| Franchise | Franchise | The business being sold uses/requires a franchise license. |
| Gambling | Gambling | The business being sold uses/requires a gambling license. |
| Liquor | Liquor | The business being sold uses/requires a liquor license. |
| Liquor 5 Years Or Less | Liquor5YearsOrLess | The business being sold uses/requires a liquor license, five years or less. |
| Liquor 5 Years Or More | Liquor5YearsOrMore | The business being sold uses/requires a liquor license, five years or more. |
| Liquor-Off Sale | LiquorOffSale | The business being sold uses/requires a liquor off-sale license. |
| Liquor-On Sale | LiquorOnSale | The business being sold uses/requires a liquor on-sale license. |
| None | None | The business being sold uses/requires/has no license. |
| Other | Other | The business being sold uses/requires some other license. |
| Professional | Professional | The business being sold uses/requires a professional license. |

## special_listing_conditions

- Source name: `SpecialListingConditions`
- Kind: **closed-MV**
- Value count: 12
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SpecialListingConditions/)
- Used by:
  - `property.special_listing_conditions` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Auction | Auction | The listing is an auction. |
| Bankruptcy Property | BankruptcyProperty | The listed property is currently involved in a bankruptcy. |
| Conservatorship | Conservatorship | Conservatorship is a legal concept in the United States. |
| HUD Owned | HudOwned | The listed property is owned and being sold by the U.S. |
| In Foreclosure | InForeclosure | The listed property is currently in the process of foreclosure. |
| Notice Of Default | NoticeOfDefault | There is a notice of default on the listed property. |
| Probate Listing | ProbateListing | The listed property is a probate sale. |
| Real Estate Owned | RealEstateOwned | The listed property is currently owned by a bank/lender. |
| Short Sale | ShortSale | The listing is a short sale (short pay) and may require bank approval. |
| Standard | Standard | The listing has none of the other conditions in the Special Listing Conditions field. |
| Third Party Approval | ThirdPartyApproval | A court or other third-party approval is required for the sale to finalize. |
| Trust | Trust | A three-party fiduciary relationship in which the first party, the trustor or settlor, transfers a property upon the second party for the benefit of the third party, the beneficiary. |

## standard_status

- Source name: `StandardStatus`
- Kind: **closed-SV**
- Value count: 11
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/StandardStatus/)
- Used by:
  - `property.standard_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The listing is on market and an offer has not been accepted. |
| Active Under Contract | ActiveUnderContract | An offer has been accepted but the listing is still on market. |
| Canceled | Canceled | The listing contract has been terminated. |
| Closed | Closed | The purchase agreement has been fulfilled or the lease agreement has been executed. |
| Coming Soon | ComingSoon | This is a listing that has not yet been on market but will be on market soon. |
| Delete | Delete | The listing contract was never valid or there is another reason for the contract to be nullified. |
| Expired | Expired | The listing contract has expired. |
| Hold | Hold | A contract exists between the seller and the listing member. |
| Incomplete | Incomplete | The listing has not yet been completely entered and is not yet published in the MLS. |
| Pending | Pending | An offer has been accepted and the listing is no longer on market. |
| Withdrawn | Withdrawn | The listing has been withdrawn from the market, but a contract still exists between the seller and the listing member. |

## state_or_province

- Source name: `StateOrProvince`
- Kind: **closed-SV**
- Value count: 65
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/StateOrProvince/)
- Used by:
  - `association.association_mail_state_of_province` (type=`String List, Single`)
  - `association.association_state_or_province` (type=`String List, Single`)
  - `contacts.home_state_or_province` (type=`String List, Single`)
  - `contacts.other_state_or_province` (type=`String List, Single`)
  - `contacts.work_state_or_province` (type=`String List, Single`)
  - `internet_tracking.actor_state_or_province` (type=`String List, Single`)
  - `lock_or_box.listing_state_or_province` (type=`String List, Single`)
  - `member.member_state_license_state` (type=`String List, Single`)
  - `member.member_state_or_province` (type=`String List, Single`)
  - `member_state_license.member_state_license_state` (type=`String List, Single`)
  - `ouid.organization_state_license_state` (type=`String List, Single`)
  - `ouid.organization_state_or_province` (type=`String List, Single`)
  - `office.office_mail_state_or_province` (type=`String List, Single`)
  - `office.office_primary_state_or_province` (type=`String List, Single`)
  - `office.office_state_or_province` (type=`String List, Single`)
  - `office_corporate_license.office_corporate_license_state` (type=`String List, Single`)
  - `property.state_or_province` (type=`String List, Single`)
  - `teams.team_lead_state_license_state` (type=`String List, Single`)
  - `teams.team_state_or_province` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| AB | AB | The Canadian province in which the listing is located is Alberta. |
| AK | AK | The U.S. |
| AL | AL | The U.S. |
| AR | AR | The U.S. |
| AZ | AZ | The U.S. |
| BC | BC | The Canadian province in which the listing is located is British Columbia. |
| CA | CA | The U.S. |
| CO | CO | The U.S. |
| CT | CT | The U.S. |
| DC | DC | The U.S. |
| DE | DE | The U.S. |
| FL | FL | The U.S. |
| GA | GA | The U.S. |
| HI | HI | The U.S. |
| IA | IA | The U.S. |
| ID | ID | The U.S. |
| IL | IL | The U.S. |
| IN | IN | The U.S. |
| KS | KS | The U.S. |
| KY | KY | The U.S. |
| LA | LA | The U.S. |
| MA | MA | The U.S. |
| MB | MB | The Canadian province in which the listing is located is Manitoba. |
| MD | MD | The U.S. |
| ME | ME | The U.S. |
| MI | MI | The U.S. |
| MN | MN | The U.S. |
| MO | MO | The U.S. |
| MS | MS | The U.S. |
| MT | MT | The U.S. |
| NB | NB | The Canadian province in which the listing is located is New Brunswick. |
| NC | NC | The U.S. |
| ND | ND | The U.S. |
| NE | NE | The U.S. |
| NF | NF | The Canadian province in which the listing is located is Newfoundland and Labrador. |
| NH | NH | The U.S. |
| NJ | NJ | The U.S. |
| NM | NM | The U.S. |
| NS | NS | The Canadian province in which the listing is located is Nova Scotia. |
| NT | NT | The Canadian territory in which the listing is located is Northwest Territories. |
| NU | NU | The Canadian territory in which the listing is located is Nunavut. |
| NV | NV | The U.S. |
| NY | NY | The U.S. |
| OH | OH | The U.S. |
| OK | OK | The U.S. |
| ON | ON | The Canadian province in which the listing is located is Ontario. |
| OR | OR | The U.S. |
| PA | PA | The U.S. |
| PE | PE | The Canadian province in which the listing is located is Prince Edward Island. |
| QC | QC | The Canadian province in which the listing is located is Quebec. |
| RI | RI | The U.S. |
| SC | SC | The U.S. |
| SD | SD | The U.S. |
| SK | SK | The Canadian province in which the listing is located is Saskatchewan. |
| TN | TN | The U.S. |
| TX | TX | The U.S. |
| UT | UT | The U.S. |
| VA | VA | The U.S. |
| VI | VI | The U.S. |
| VT | VT | The U.S. |
| WA | WA | The U.S. |
| WI | WI | The U.S. |
| WV | WV | The U.S. |
| WY | WY | The U.S. |
| YT | YT | The Canadian territory in which the listing is located is Yukon. |

## street_direction

- Source name: `StreetDirection`
- Kind: **closed-SV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/StreetDirection/)
- Used by:
  - `property.street_dir_prefix` (type=`String List, Single`)
  - `property.street_dir_suffix` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| E | E | The street suffix or prefix direction is east. |
| N | N | The street suffix or prefix direction is north. |
| NE | NE | The street suffix or prefix direction is northeast. |
| NW | NW | The street suffix or prefix direction is northwest. |
| S | S | The street suffix or prefix direction is south. |
| SE | SE | The street suffix or prefix direction is southeast. |
| SW | SW | The street suffix or prefix direction is southwest. |
| W | W | The street suffix or prefix direction is west. |

## street_suffix

- Source name: `StreetSuffix`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/StreetSuffix/)
- Used by:
  - `property.street_suffix` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## structure_type

- Source name: `StructureType`
- Kind: **closed-MV**
- Value count: 17
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/StructureType/)
- Used by:
  - `property.structure_type` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Cabin | Cabin | A single-family residence that may have limited utilities and rooms. |
| Dock | Dock | A floating or pillar-supported structure over water used to park watercraft. |
| Duplex | Duplex | A multifamily structure with two independent units sharing a common roof. |
| Flex | Flex | A commercial property that is designed to be used in different ways (e.g., Office, Retail, Warehouse). |
| Hotel/Motel | HotelMotel | A commercial structure designed to be a hotel or motel. |
| House | House | A single-family residence on real property either attached or detached from another structure. |
| Industrial | Industrial | A commercial structure designed for industrial use. |
| Manufactured House | ManufacturedHouse | A factory-built house that is transported to a lot. |
| Mixed Use | MixedUse | The property is designed to be used in more than one way. |
| Multi Family | MultiFamily | A structure or complex with five or more units that are individual dwellings. |
| None | None | The property has no structure. |
| Office | Office | A commercial structure designed to be used as office space. |
| Quadruplex | Quadruplex | A multifamily structure with four independent units sharing a common roof. |
| Retail | Retail | A commercial structure designed to be used for retail space. |
| Townhouse | Townhouse | A dwelling unit, generally having two or more floors and attached to other similar units via party walls. |
| Triplex | Triplex | A multifamily structure with three independent units sharing a common roof. |
| Warehouse | Warehouse | A commercial structure designed for warehousing. |

## syndicate_agent_option

- Source name: `SyndicateAgentOption`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SyndicateAgentOption/)
- Used by:
  - `office.syndicate_agent_option` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## syndicate_to

- Source name: `SyndicateTo`
- Kind: **closed-MV**
- Value count: 4
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/SyndicateTo/)
- Used by:
  - `member.syndicate_to` (type=`String List, Multi`)
  - `office.syndicate_to` (type=`String List, Multi`)
  - `property.syndicate_to` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Homes.com | HomesDotCom | The broker, or member if permitted by the broker, is allowing their listings to be sent to Homes.com. |
| ListHub | Listhub | The broker, or member if permitted by the broker, is allowing their listings to be sent to ListHub.com. |
| Realtor.com | RealtorDotCom | The broker, or member if permitted by the broker, is allowing their listings to be sent to Realtor.com. |
| Zillow/Trulia | ZillowTrulia | The broker, or member if permitted by the broker, is allowing their listings to be sent to Zillow and Trulia. |

## tax_status_current

- Source name: `TaxStatusCurrent`
- Kind: **closed-MV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TaxStatusCurrent/)
- Used by:
  - `property.tax_status_current` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Personal | Personal | The tax is based on personal property. |
| Personal And Real | PersonalAndReal | The tax is based on both personal and real property. |
| Real | Real | The tax is based on real property. |

## team_impersonation_level

- Source name: `TeamImpersonationLevel`
- Kind: **open**
- Value count: 0
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TeamImpersonationLevel/)
- Used by:
  - `team_members.team_impersonation_level` (type=`String List, Single`)

*No closed value list - jurisdiction-defined.*

## team_member_type

- Source name: `TeamMemberType`
- Kind: **closed-SV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TeamMemberType/)
- Used by:
  - `team_members.team_member_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Administration Assistant | AdministrationAssistant | The member of a team who assists with administrative tasks. |
| Buyer Agent | BuyerAgent | A member of the real estate team. |
| Lead Manager | LeadManager | The member of the team who is the lead manager. |
| Listing Agent | ListingAgent | The member of a team who is the lead manager. |
| Marketing Assistant | MarketingAssistant | The member of a team who assists with marketing. |
| Operations Manager | OperationsManager | The member of the team who manages operations. |
| Showing Agent | ShowingAgent | The member of a team who manages operations. |
| Team Lead | TeamLead | The leading member of a team. |
| Team Member | TeamMember | A member of a real estate team. |
| Transaction Coordinator | TransactionCoordinator | The member of a team who handles transaction details. |

## team_status

- Source name: `TeamStatus`
- Kind: **closed-SV**
- Value count: 2
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TeamStatus/)
- Used by:
  - `teams.team_status` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Active | Active | The team is active. |
| Inactive | Inactive | The team is not active. |

## tenant_pays

- Source name: `TenantPays`
- Kind: **closed-MV**
- Value count: 29
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TenantPays/)
- Used by:
  - `property.tenant_pays` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| All Utilities | AllUtilities | The tenant pays for all utilities. |
| Association Fees | AssociationFees | The tenant pays for association fees. |
| Cable TV | CableTv | The tenant pays for cable TV. |
| Common Area Maintenance | CommonAreaMaintenance | The tenant pays for common area maintenance. |
| Electricity | Electricity | The tenant pays for electricity. |
| Exterior Maintenance | ExteriorMaintenance | The tenant pays for exterior maintenance. |
| Gas | Gas | The tenant pays for gas. |
| Grounds Care | GroundsCare | The tenant pays for grounds care. |
| HVAC Maintenance | HvacMaintenance | The tenant pays for HVAC maintenance. |
| Hot Water | HotWater | The tenant pays for hot water. |
| Insurance | Insurance | The tenant pays for insurance. |
| Janitorial Service | JanitorialService | The tenant pays for janitorial service. |
| Management | Management | The tenant pays for management. |
| None | None | The tenant pays for no other utilities, services, etc. |
| Other | Other | The tenant pays for items other than those on this list. |
| Other Tax | OtherTax | The tenant pays for other taxes. |
| Parking Fee | ParkingFee | The tenant pays for parking fees. |
| Pest Control | PestControl | The tenant pays for pest control. |
| Pool Maintenance | PoolMaintenance | The tenant pays for pool maintenance. |
| Repairs | Repairs | The tenant pays for repairs. |
| Roof | Roof | The tenant pays for roof maintenance. |
| Security | Security | The tenant pays for security. |
| See Remarks | SeeRemarks | See listing remarks for details on what the tenant pays for. |
| Sewer | Sewer | The tenant pays for sewer. |
| Snow Removal | SnowRemoval | The tenant pays for snow removal. |
| Taxes | Taxes | The tenant pays for taxes. |
| Telephone | Telephone | The tenant pays for telephone. |
| Trash Collection | TrashCollection | The tenant pays for trash collection. |
| Water | Water | The tenant pays for water. |

## tracking_type

- Source name: `TrackingType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TrackingType/)
- Used by:
  - `internet_tracking_summary.tracking_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| ListAgentMlsId | ListAgentMlsId | Indicates that the ListAgentMlsId is the focus of the tracking search. |
| ListOfficeMlsId | ListOfficeMlsId | Indicates that the ListOfficeMlsId is the focus of the tracking search. |
| ListingId | ListingId | Indicates that the ListingId is the focus of the tracking search. |
| MainOfficeMlsId | MainOfficeMlsId | Indicates that the MainOfficeMLSId is the focus of the tracking search. |
| OUID | Ouid | Indicates that the RESO Unique Organization Identifier (UOI) is the focus of the tracking search. |

## transaction_type

- Source name: `TransactionType`
- Kind: **closed-SV**
- Value count: 5
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/TransactionType/)
- Used by:
  - `transaction_management.transaction_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Lease Offer | LeaseOffer | The transaction type is for the rental of a listing. |
| Listing for Lease | ListingForLease | The transaction type is for the lease of a listing. |
| Listing for Sale | ListingForSale | The transaction type is for the sale of a listing. |
| Other | Other | This transaction type may or may not relate to real estate. |
| Purchase Offer | PurchaseOffer | The transaction type is for the purchase of a listing. |

## units_furnished

- Source name: `UnitsFurnished`
- Kind: **closed-SV**
- Value count: 3
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/UnitsFurnished/)
- Used by:
  - `property.units_furnished` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| All Units | AllUnits | All of the units in the listed income property are furnished. |
| None | None | None of the units in the listed income property are furnished. |
| Varies By Unit | VariesByUnit | Some of the units in the listing income property are furnished. |

## unit_type_type

- Source name: `UnitTypeType`
- Kind: **closed-SV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/UnitTypeType/)
- Used by:
  - `property.unit_type_type` (type=`String List, Multi`)
  - `property_unit_types.unit_type_type` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| 1 Bedroom | OneBedroom | The type of unit has one bedroom. |
| 2 Bedroom | TwoBedroom | The type of unit has two bedrooms. |
| 3 Bedroom | ThreeBedroom | The type of unit has three bedrooms. |
| 4 Bedroom Or More | FourBedroomOrMore | The type of unit has four or more bedrooms. |
| Apartments | Apartments | The type of unit is apartments. |
| Efficiency | Efficiency | The type of unit is an efficiency. |
| Loft | Loft | The type of unit is a loft. |
| Manager's Unit | ManagersUnit | The type of unit is a manager's unit. |
| Penthouse | Penthouse | The type of unit is a penthouse. |
| Studio | Studio | The type of unit is a studio. |

## utilities

- Source name: `Utilities`
- Kind: **closed-MV**
- Value count: 23
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Utilities/)
- Used by:
  - `property.utilities` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Cable Available | CableAvailable | The property has cable available but is not connected. |
| Cable Connected | CableConnected | Cable service is physically connected but not necessarily paid. |
| Cable Not Available | CableNotAvailable | Cable is not available in the area of the property. |
| Electricity Available | ElectricityAvailable | Electricity is available from the public utility but not connected. |
| Electricity Connected | ElectricityConnected | Electricity from the public utility is available and connected but not necessarily paid. |
| Electricity Not Available | ElectricityNotAvailable | Electricity from the public utility is not available. |
| Natural Gas Available | NaturalGasAvailable | Natural gas is available from the public utility but not connected. |
| Natural Gas Connected | NaturalGasConnected | Natural gas from the public utility is available and connected but not necessarily paid. |
| Natural Gas Not Available | NaturalGasNotAvailable | Natural gas from the public utility is not available. |
| None | None | There are no public utilities currently available or connected. |
| Other | Other | There are utilities other than those listed. |
| Phone Available | PhoneAvailable | The property has telephone service available but is not connected. |
| Phone Connected | PhoneConnected | Telephone service is physically connected but not necessarily paid. |
| Phone Not Available | PhoneNotAvailable | Telephone service is not available in the area of the property. |
| Propane | Propane | The property has a propane system. |
| See Remarks | SeeRemarks | See remarks for details about the public or other utilities available/installed at the property. |
| Sewer Available | SewerAvailable | Sewer service is available from the public utility but not connected. |
| Sewer Connected | SewerConnected | Sewer service from the public utility is available and connected but not necessarily paid. |
| Sewer Not Available | SewerNotAvailable | Sewer service from the public utility is not available. |
| Underground Utilities | UndergroundUtilities | All or some of the utilities are run underground. |
| Water Available | WaterAvailable | Water service is available from the public utility but not connected. |
| Water Connected | WaterConnected | Water service from the public utility is available and connected but not necessarily paid. |
| Water Not Available | WaterNotAvailable | Water service from the public utility is not available. |

## vegetation

- Source name: `Vegetation`
- Kind: **closed-MV**
- Value count: 10
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/Vegetation/)
- Used by:
  - `property.vegetation` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Brush | Brush | The lot has brush. |
| Cleared | Cleared | The lot has been cleared. |
| Crop(s) | Crops | There are crops on the lot. |
| Grassed | Grassed | The lot is grassed. |
| Heavily Wooded | HeavilyWooded | The lot is heavily wooded. |
| Natural State | NaturalState | The lot is in its natural state. |
| Other | Other | There are other types of vegetation on the lot than those on this list. |
| Partially Wooded | PartiallyWooded | The lot is partially wooded. |
| See Remarks | SeeRemarks | See the public or private remarks for details about the vegetation found on the lot. |
| Wooded | Wooded | The lot is wooded. |

## view

- Source name: `View`
- Kind: **closed-MV**
- Value count: 38
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/View/)
- Used by:
  - `property.view` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bay | Bay | The property has a bay view. |
| Beach | Beach | The property has a beach view. |
| Bridge(s) | Bridges | The property has a view of a bridge or bridges. |
| Canal | Canal | The property has a canal view. |
| Canyon | Canyon | The property has a canyon view. |
| City | City | The property has a city view. |
| City Lights | CityLights | The property has a view of city lights. |
| Creek/Stream | CreekStream | The property has a creek/stream view. |
| Desert | Desert | The property has a desert view. |
| Downtown | Downtown | The property has a downtown view. |
| Forest | Forest | The property has a forest view. |
| Garden | Garden | The property has a garden view. |
| Golf Course | GolfCourse | The property has a view of a golf course. |
| Hills | Hills | The property has a view of hills. |
| Lake | Lake | The property has a lake view. |
| Marina | Marina | The property has a marina view. |
| Meadow | Meadow | The property has a view of a meadow. |
| Mountain(s) | Mountains | The property has a mountain view. |
| Neighborhood | Neighborhood | The property has a view of the surrounding neighborhood. |
| None | None | The property has no view. |
| Ocean | Ocean | The property has an ocean view. |
| Orchard | Orchard | The property has a view of the orchard(s). |
| Other | Other | The property has a view other than those listed. |
| Panoramic | Panoramic | The property has a panoramic view. |
| Park/Greenbelt | ParkGreenbelt | The property has a park/greenbelt view. |
| Pasture | Pasture | The property has a view of a pasture. |
| Pond | Pond | The property has a view of a pond. |
| Pool | Pool | The property has a view of a pool. |
| Ridge | Ridge | The property has a view of a ridge. |
| River | River | The property has a river view. |
| Rural | Rural | The property has a rural view. |
| See Remarks | SeeRemarks | See the remarks fields for more information about the view from the property. |
| Skyline | Skyline | The property has a skyline view. |
| Territorial | Territorial | The property has a view of the surrounding area. |
| Trees/Woods | TreesWoods | The property has a view of trees or woods. |
| Valley | Valley | The property has a view of a valley. |
| Vineyard | Vineyard | The property has a view of a vineyard. |
| Water | Water | The property has a water view. |

## waterfront_features

- Source name: `WaterfrontFeatures`
- Kind: **closed-MV**
- Value count: 20
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/WaterfrontFeatures/)
- Used by:
  - `property.waterfront_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Bay Access | BayAccess | The property has access to a bay. |
| Bayfront | Bayfront | The property is on a bayfront. |
| Beach Access | BeachAccess | The property has access to a beach. |
| Beach Front | BeachFront | The property is on a beachfront. |
| Canal Access | CanalAccess | The property has access to a canal. |
| Canal Front | CanalFront | The property is located on a canal. |
| Creek | Creek | The property is either on or near a creek. |
| Lagoon | Lagoon | The property is either on or near a lagoon. |
| Lake Front | LakeFront | The property is on a lakefront. |
| Lake Privileges | LakePrivileges | The property includes rights to access a lake. |
| Marina in Community | MarinaInCommunity | This property has a marina in the community. |
| Navigable Water | NavigableWater | The water can be navigated by water vessels. |
| Ocean Access | OceanAccess | The property has access to an ocean. |
| Ocean Front | OceanFront | The property is on an oceanfront. |
| Pond | Pond | The property is on or near a pond. |
| River Access | RiverAccess | The property has access to a river. |
| River Front | RiverFront | The property is located on a riverfront. |
| Seawall | Seawall | The property is protected by a seawall or barrier. |
| Stream | Stream | The property is on or near a stream. |
| Waterfront | Waterfront | The property is located on a waterfront. |

## water_source

- Source name: `WaterSource`
- Kind: **closed-MV**
- Value count: 9
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/WaterSource/)
- Used by:
  - `property.water_source` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Cistern | Cistern | The property's source of water has/includes a cistern. |
| None | None | The property has no current source of water. |
| Other | Other | The property has a source of water other than those listed. |
| Private | Private | The property's source of water is private. |
| Public | Public | The property's source of water is public. |
| See Remarks | SeeRemarks | See the listing's remarks for details on the property's water source. |
| Shared Well | SharedWell | The property's source of water has/includes a shared well. |
| Spring | Spring | The property's source of water has/includes a spring. |
| Well | Well | The property's source of water has/includes a well. |

## window_features

- Source name: `WindowFeatures`
- Kind: **closed-MV**
- Value count: 21
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/WindowFeatures/)
- Used by:
  - `property.window_features` (type=`String List, Multi`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Aluminum Frames | AluminumFrames | The windows have aluminum frames. |
| Bay Window(s) | BayWindows | The property has one or more bay windows. |
| Blinds | Blinds | The property has window blinds. |
| Display Window(s) | DisplayWindows | The property has one or more windows that would normally be used to display goods or products. |
| Double Pane Windows | DoublePaneWindows | The property has windows with two panes of glass. |
| Drapes | Drapes | The property has drapes. |
| ENERGY STAR Qualified Windows | EnergyStarQualifiedWindows | The property has qualified ENERGY STAR windows. |
| Garden Window(s) | GardenWindows | The property has one or more garden windows. |
| Insulated Windows | InsulatedWindows | The property has insulated windows. |
| Low-Emissivity Windows | LowEmissivityWindows | The property has low-emissivity windows. |
| Plantation Shutters | PlantationShutters | The property has plantation shutters. |
| Screens | Screens | The property has screens. |
| Shutters | Shutters | The property has shutters. |
| Skylight(s) | Skylights | The property has skylights. |
| Solar Screens | SolarScreens | The property has solar screens. |
| Storm Window(s) | StormWindows | The property has storm windows. |
| Tinted Windows | TintedWindows | The property has tinted windows. |
| Triple Pane Windows | TriplePaneWindows | The property has triple-pane windows. |
| Window Coverings | WindowCoverings | The property has window coverings. |
| Window Treatments | WindowTreatments | The property has window treatments. |
| Wood Frames | WoodFrames | The property has wood-framed windows. |

## year_built_source

- Source name: `YearBuiltSource`
- Kind: **closed-SV**
- Value count: 8
- [dd.reso.org page](https://dd.reso.org/DD2.0/lookups/YearBuiltSource/)
- Used by:
  - `property.year_built_source` (type=`String List, Single`)

| StandardValue | LegacyODataValue | Definition |
|---|---|---|
| Appraiser | Appraiser | An appraiser provided the year built. |
| Assessor | Assessor | The assessor provided the year built. |
| Builder | Builder | The builder provided the year built. |
| Estimated | Estimated | The year built is an estimate. |
| Other | Other | The year built was provided by another party not listed. |
| Owner | Owner | The owner provided the year built. |
| Public Records | PublicRecords | The year built was received from public records. |
| See Remarks | SeeRemarks | See remarks for information about the source of the lot size measurement. |

