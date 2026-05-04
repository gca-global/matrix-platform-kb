# PropertyRooms

The PropertyRooms resource describes individual rooms within a Property: type (Bedroom/Bathroom/Kitchen/...), level (Basement/First/Second/...), dimensions, area, and room features. One Property has many PropertyRooms rows linked via ListingKey.

**Adoption** — weighted Org%: **19%** across 16 measured fields (median 24%, avg 19%).

## Groups

- **Other** — 19 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `BedroomClosetType` | String List, Single |  | [ClosetType](#closettype) |  |  | A list of possible closet types for a bedroom. | [link](https://ddwiki.reso.org/display/DDW20/BedroomClosetType+Field) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135786) |
| `Listing` | Resource |  |  |  |  | The listing associated with the PropertyRooms record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135792) |
| `ListingId` | String |  |  | 10% | 13% | The well-known identifier for the listing, also known as the MLS number. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135798) |
| `ListingKey` | String |  |  |  | 24% | A system-unique identifier for the listing. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135802) |
| `ModificationTimestamp` | Timestamp |  |  | 20% | 14% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135807) |
| `RoomArea` | Number |  |  |  | 8% | The numeric area of the room. | [link](https://ddwiki.reso.org/display/DDW20/RoomArea+Field) |
| `RoomAreaSource` | String List, Single |  | [AreaSource](#areasource) | 1% | 1% | The source of the measurement of the given room's area. | [link](https://ddwiki.reso.org/display/DDW20/RoomAreaSource+Field) |
| `RoomAreaUnits` | String List, Single |  | [AreaUnits](#areaunits) | 10% | 1% | The unit of measurement used for the value in the RoomArea field (e.g., Square Feet, Square Meters). | [link](https://ddwiki.reso.org/display/DDW20/RoomAreaUnits+Field) |
| `RoomDescription` | String |  |  | 15% | 7% | Free-text description of the room. | [link](https://ddwiki.reso.org/display/DDW20/RoomDescription+Field) |
| `RoomDimensions` | String |  |  | 15% | 10% | The room's dimensions as a free-text string (typically formatted '<length>x<width>'). | [link](https://ddwiki.reso.org/display/DDW20/RoomDimensions+Field) |
| `RoomFeatures` | String List, Multi |  | [InteriorOrRoomFeatures](#interiororroomfeatures) | 15% | 6% | A multi-value lookup of features present in the room: Ceiling Fan \| Walk-in Closet \| En-suite Bathroom \| Hardwood Floor \| Tile Floor \| Built-in Shelving \| ... | [link](https://ddwiki.reso.org/display/DDW20/RoomFeatures+Field) |
| `RoomKey` | String |  |  |  | 36% | The unique identifier for a room within the originating system. | [link](https://ddwiki.reso.org/display/DDW20/RoomKey+Field) |
| `RoomLength` | Number |  |  | 20% | 8% | The numeric length of the room. | [link](https://ddwiki.reso.org/display/DDW20/RoomLength+Field) |
| `RoomLengthWidthSource` | String List, Single |  | [RoomLengthWidthSource](#roomlengthwidthsource) | 1% | 1% | The source of the measurement of the given units length and width. | [link](https://ddwiki.reso.org/display/DDW20/RoomLengthWidthSource+Field) |
| `RoomLengthWidthUnits` | String List, Single |  | [LinearUnits](#linearunits) | 15% | 1% | The unit of measurement used for the value of RoomLength and RoomWidth fields (e.g., Feet, Meters). | [link](https://ddwiki.reso.org/display/DDW20/RoomLengthWidthUnits+Field) |
| `RoomLevel` | String List, Single |  | [RoomLevel](#roomlevel) | 15% | 12% | A single-value lookup describing which floor or level the room is on: Basement \| First \| Second \| Third \| Lower \| Upper \| Main \| Loft \| ... | [link](https://ddwiki.reso.org/display/DDW20/RoomLevel+Field) |
| `RoomType` | String List, Single |  | [RoomType](#roomtype) | 20% | 14% | A single-value lookup describing the type of room: Bedroom \| Bathroom \| Kitchen \| LivingRoom \| DiningRoom \| Office \| Laundry \| Bonus \| ... | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135880) |
| `RoomWidth` | Number |  |  |  | 26% | The numeric width of the room. | [link](https://ddwiki.reso.org/display/DDW20/RoomWidth+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>BedroomClosetType</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** AUG 17 2023
  - **Revision Date:** AUG 18 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Listing</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>ListingId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Listado
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomAreaSource</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Fuente de Área de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomAreaUnits</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Unidades de Área de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomDimensions</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Dimensiones de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomFeatures</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Características de Habitación
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** JUN 01 2018
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomLength</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Longitud de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomLengthWidthSource</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Fuente De Longitud Anchura De Habitación
  - **Status Change Date:** APR 08 2022
  - **Revision Date:** APR 08 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>RoomLengthWidthUnits</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Unidades de Longitud Anchura de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

<details><summary><code>RoomLevel</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nivel De Habitación
  - **Status Change Date:** APR 08 2022
  - **Revision Date:** APR 08 2022
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>RoomType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Habitación
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** MAY 24 2017
  - **Added in Version:** 1.6.0

</details>

## Lookups

### AreaSource

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

| Value | Definition |
|---|---|
| `Square Feet` | The value reported in the related Area field is in square feet. |
| `Square Meters` | The value reported in the related Area field is in square meters. |

### ClosetType

| Value | Definition |
|---|---|
| `Built-in Closet` | The bedroom has a built-in closet. |
| `None` | The room does not have a closet. |
| `Walk-in Closet` | The bedroom has a walk-in closet. |

### InteriorOrRoomFeatures

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

### LinearUnits

| Value | Definition |
|---|---|
| `Feet` | The elevation of the property is measured in feet. |
| `Meters` | The elevation of the property is measured in meters. |

### RoomLengthWidthSource

| Value | Definition |
|---|---|
| `Appraiser` | The length and width of the room were provided by an appraiser. |
| `Assessor` | The length and width of the room were provided by the assessor. |
| `Builder` | The length and width of the room were provided by the builder. |
| `Estimated` | The length and width of the room were estimated. |
| `GIS Calculated` | The length and width of the room were calculated by a Geographic Information System (GIS). |
| `Measured` | The length and width of the room were measured. |
| `Other` | The length and width of the room were provided by an other means than those included in this list. |
| `Owner` | The length and width of the room were provided by the owner. |
| `Public Records` | The length and width of the room were taken from public records. |
| `See Remarks` | See the Public or Private Remarks for details on the source of the room's length and width measurements. |
| `Survey` | The length and width of the room were provided by survey. |

### RoomLevel

| Value | Definition |
|---|---|
| `Basement` | The given room is located on the basement level. |
| `First` | The given room is located on the first level. |
| `Lower` | The given room is located on a lower level. |
| `Main` | The given room is located on the main level. |
| `Second` | The given room is located on the second level. |
| `Third` | The given room is located on the third level. |
| `Upper` | The given room is located on an upper level. |

### RoomType

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

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
