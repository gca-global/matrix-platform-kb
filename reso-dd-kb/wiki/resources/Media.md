# Media

The Media resource describes images, videos, virtual tours, documents, and other media items associated with a Property. Each media item carries a MediaURL, MediaCategory, and ordering information so consumers can render galleries in the intended sequence.

**Adoption** — weighted Org%: **23%** across 33 measured fields (median 23%, avg 23%).

## Groups

- **Listing** — 7 fields
- **Other** — 34 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `ChangedByMember` | Resource |  |  |  |  | The member who changed the Media record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116417) |
| `ChangedByMemberID` | String |  |  | 1% | 1% | The ID of the user, agent, member, etc., that uploaded the media this record refers to. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116422) |
| `ChangedByMemberKey` | String |  |  | 10% | 1% | The primary key of the member who uploaded the media this record refers to. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116428) |
| `ClassName` | String List, Single |  | [ClassName](#classname) | 30% | 5% | The class or table of the listing or other record of the media (e.g., Residential, Lease, Agent, Office, Contact). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116434) |
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135112) |
| `ImageHeight` | Number |  |  | 35% | 4% | The height of the image expressed in pixels. | [link](https://ddwiki.reso.org/display/DDW20/ImageHeight+Field) |
| `ImageOf` | String List, Single |  | [ImageOf](#imageof) |  | 13% | When the media is an image, a list of possible matches such as kitchen, bathroom, front of structure, etc. | [link](https://ddwiki.reso.org/display/DDW20/ImageOf+Field) |
| `ImageSizeDescription` | String List, Single |  | ImageSizeDescription | 25% | 2% | A text description of the size of the image (i.e., Small, Thumbnail, Medium, Large, X-Large). | [link](https://ddwiki.reso.org/display/DDW20/ImageSizeDescription+Field) |
| `ImageWidth` | Number |  |  |  | 14% | The width of the image expressed in pixels. | [link](https://ddwiki.reso.org/display/DDW20/ImageWidth+Field) |
| `LongDescription` | String |  |  | 55% | 21% | The full robust description of the object. | [link](https://ddwiki.reso.org/display/DDW20/LongDescription+Field) |
| `MediaAlteration` | String List, Multi | Listing | [MediaAlteration](#mediaalteration) |  | 1% | Photos may be enhanced, altered or even created by manual or computer drafting. | [link](https://ddwiki.reso.org/display/DDW20/MediaAlteration+Field) |
| `MediaCategory` | String List, Single |  | [MediaCategory](#mediacategory) | 55% | 9% | The category of the media object. | [link](https://ddwiki.reso.org/display/DDW20/MediaCategory+Field) |
| `MediaHTML` | String |  |  | 1% | 1% | The JavaScript or other method to embed a video, image, virtual tour or other media. | [link](https://ddwiki.reso.org/display/DDW20/MediaHTML+Field) |
| `MediaKey` | String |  |  |  | 48% | A system-unique identifier for the media object. | [link](https://ddwiki.reso.org/display/DDW20/MediaKey+Field) |
| `MediaModificationTimestamp` | Timestamp |  |  | 35% | 18% | A timestamp that is updated when a change to the object has been made, which may differ from a change to the Media Resource. | [link](https://ddwiki.reso.org/display/DDW20/MediaModificationTimestamp+Field) |
| `MediaObjectID` | String |  |  | 25% | 13% | The ID of the image, supplement or other object specified by the given media record. | [link](https://ddwiki.reso.org/display/DDW20/MediaObjectID+Field) |
| `MediaStatus` | String List, Single |  | MediaStatus | 25% | 4% | The status of the media item referenced by this record (i.e., updated, deleted, etc.). | [link](https://ddwiki.reso.org/display/DDW20/MediaStatus+Field) |
| `MediaType` | String List, Single |  | [MediaType](#mediatype) | 55% | 19% | Media types as defined by the Internet Assigned Numbers Authority (IANA), http://www.iana.org/assignments/media-types/index.html. | [link](https://ddwiki.reso.org/display/DDW20/MediaType+Field) |
| `MediaURL` | String |  |  |  | 51% | A URL pointing to the actual media object (image, video, document, virtual tour, etc.). | [link](https://ddwiki.reso.org/display/DDW20/MediaURL+Field) |
| `ModificationTimestamp` | Timestamp |  |  | 60% | 23% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135193) |
| `Order` | Number |  |  | 60% | 23% | The display order of the media object relative to other media objects of the same resource record. | [link](https://ddwiki.reso.org/display/DDW20/Order+Field) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the Media record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135205) |
| `OriginatingSystemID` | String |  |  | 30% | 3% | The RESO Unique Organization Identifier's OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135210) |
| `OriginatingSystemMediaKey` | String |  |  | 55% | 15% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemMediaKey+Field) |
| `OriginatingSystemName` | String |  |  | 50% | 19% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135222) |
| `OriginatingSystemResourceRecordId` | String | Listing |  |  | 1% | The originating system's well-known identifier of the related record from the source resource. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemResourceRecordID+Field) |
| `OriginatingSystemResourceRecordKey` | String | Listing |  |  | 23% | The originating system's primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemResourceRecordKey+Field) |
| `OriginatingSystemResourceRecordSystemId` | String | Listing |  |  |  | The system ID of the resource record from the originating system is used when the resource record is originated from a different system than the media. | [link](https://ddwiki.reso.org/display/DDW20/OriginatingSystemResourceRecordSystemID+Field) |
| `Permission` | String List, Multi |  | [Permission](#permission) | 25% | 11% | The permission-level of the media (i.e., Public, Private, IDX, VOW, Office Only, Firm Only, Agent Only). | [link](https://ddwiki.reso.org/display/DDW20/Permission+Field) |
| `PreferredPhotoYN` | Boolean |  |  | 25% | 2% | A flag indicating whether or not the media record in question is the preferred photo. | [link](https://ddwiki.reso.org/display/DDW20/PreferredPhotoYN+Field) |
| `ResourceName` | String List, Single |  | [ResourceName](#resourcename) |  | 26% | The name of the RESO resource the change record is for (Property, Member, Office, etc.). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116572) |
| `ResourceRecordID` | String |  |  |  | 43% | The well-known identifier of the related record from the source resource. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116577) |
| `ResourceRecordKey` | String |  |  | 55% | 23% | The primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=2116583) |
| `ShortDescription` | String |  |  | 50% | 15% | A short caption / description of the media object, typically displayed below the image in galleries. | [link](https://ddwiki.reso.org/display/DDW20/ShortDescription+Field) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the Media record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135266) |
| `SourceSystemID` | String |  |  | 10% | 15% | The OUID Resource's OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135271) |
| `SourceSystemMediaKey` | String |  |  | 15% | 1% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemMediaKey+Field) |
| `SourceSystemName` | String |  |  | 10% | 1% | The name of the immediate record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135283) |
| `SourceSystemResourceRecordId` | String | Listing |  |  |  | The source system's well-known identifier of the related record from the source resource. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemResourceRecordID+Field) |
| `SourceSystemResourceRecordKey` | String | Listing |  |  |  | The source system's primary key of the related record from the source resource (e.g., ListingKey, AgentKey, OfficeKey, TeamKey). | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemResourceRecordKey+Field) |
| `SourceSystemResourceRecordSystemId` | String | Listing |  |  |  | The system ID of the resource record from the source system is used when the resource record is sourced from a different system than the media. | [link](https://ddwiki.reso.org/display/DDW20/SourceSystemResourceRecordSystemID+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>ChangedByMember</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ChangedByMemberID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Cambiado por ID de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ChangedByMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Cambiado por Clave de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017

</details>

<details><summary><code>ClassName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Clase
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 12 2015

</details>

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>ImageHeight</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Altura de Imagen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>ImageSizeDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción de Tamaño de Imagen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>LongDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción Larga
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>MediaAlteration</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 21 2021
  - **Revision Date:** APR 21 2021
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>MediaCategory</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Categoría de Medio
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>MediaHTML</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** HTML de Medio
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 15 2013

</details>

<details><summary><code>MediaModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Modificación de Medio
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>MediaObjectID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Objeto de Medio
  - **Status Change Date:** JUL 03 2014
  - **Revision Date:** AUG 15 2013

</details>

<details><summary><code>MediaStatus</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Estado de Medio
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>MediaType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Medio
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** AUG 27 2015

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>Order</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Orden
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemMediaKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Medio de Sistema de Origen
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016

</details>

<details><summary><code>OriginatingSystemResourceRecordId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 17 2020
  - **Revision Date:** DEC 17 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>OriginatingSystemResourceRecordKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 17 2020
  - **Revision Date:** DEC 17 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>Permission</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Permiso
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JUN 02 2018

</details>

<details><summary><code>PreferredPhotoYN</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Fotografía Preferida SN
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** MAR 24 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>ResourceRecordKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Registro de Recurso
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>ShortDescription</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Descripción Corta
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** APR 04 2023
  - **Revision Date:** APR 04 2023
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemMediaKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Medios Sistema Fuente
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** DEC 05 2018
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemResourceRecordId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 17 2020
  - **Revision Date:** DEC 17 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemResourceRecordKey</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 17 2020
  - **Revision Date:** DEC 17 2020
  - **Added in Version:** 2.0.0

</details>

<details><summary><code>SourceSystemResourceRecordSystemId</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** DEC 17 2020
  - **Revision Date:** DEC 17 2020
  - **Added in Version:** 2.0.0

</details>

## Lookups

### ClassName

| Value | Definition |
|---|---|
| `Business Opportunity` | The class, sometimes known as property type, is a business for sale. |
| `Commercial Lease` | The class, sometimes known as property type, is a commercial property for lease. |
| `Commercial Sale` | The class, sometimes known as property type, is a commercial property for sale. |
| `Contacts` | The class is the collection of the member's contacts/clients. |
| `Cross Property` | The class, sometimes known as property type, is a collection of all listing property types. |
| `Farm` | The class, sometimes known as property type, is a farm. |
| `History Transactional` | The class is the transactional history of another class. |
| `Land` | The class, sometimes known as property type, is land for sale or lease. |
| `Manufactured In Park` | The class, sometimes known as property type, is a manufactured or mobile home in a mobile park. |
| `Media` | The class is one that contains records referencing media files. |
| `Member` | The class containing member records. |
| `Office` | The class containing office records. |
| `Open House` | The class containing open house records. |
| `Residential` | The class, sometimes known as property type, is residential property for sale. |
| `Residential Income` | The class, sometimes known as property type, is income or multifamily property for sale. |
| `Residential Lease` | The class, sometimes known as property type, is residential property for lease. |
| `Saved Search` | The class containing saved search data. |

### ImageOf

| Value | Definition |
|---|---|
| `Aerial View` | The image/photo is an aerial view of a structure or property. |
| `Atrium` | The image/photo is of an atrium. |
| `Attic` | The image/photo is of an attic. |
| `Back of Structure` | The image/photo is of the back of a structure. |
| `Balcony` | The image/photo is of a balcony. |
| `Bar` | The image/photo is of a bar. |
| `Barn` | The image/photo is of a barn. |
| `Basement` | The image/photo is of a basement. |
| `Basketball Court` | The image/photo is of a basketball court. |
| `Bathroom` | The image/photo is of a bathroom. |
| `Bedroom` | The image/photo is of a bedroom. |
| `Bonus Room` | The image/photo is of a bonus room. |
| `Breakfast Area` | The image/photo is of a breakfast area. |
| `Closet` | The image/photo is of a closet. |
| `Community` | The image/photo is of the surrounding community. |
| `Courtyard` | The image/photo is of a courtyard. |
| `Deck` | The image/photo is of a deck. |
| `Den` | The image/photo is of a den. |
| `Dining Area` | The image/photo is of a dining area. |
| `Dining Room` | The image/photo is of a dining room. |
| `Dock` | The image/photo is of a dock. |
| `Entrance Foyer` | The image/photo is of an entrance foyer. |
| `Entry` | The image/photo is of an entry. |
| `Exercise Room` | The image/photo is of an exercise room. |
| `Family Room` | The image/photo is of a family room. |
| `Fence` | The image/photo is of a fence. |
| `Fireplace` | The image/photo is of a fireplace. |
| `Floor Plan` | The image/photo is of a floor plan. |
| `Front of Structure` | The image/photo is of the front of a structure. |
| `Game Room` | The image/photo is of a game room. |
| `Garage` | The image/photo is of a garage. |
| `Garden` | The image/photo is of a garden. |
| `Golf Course` | The image/photo is of a golf course. |
| `Great Room` | The image/photo is of a great room. |
| `Guest Quarters` | The image/photo is of guest quarters. |
| `Gym` | The image/photo is of a gym. |
| `Hallway` | The image/photo is of a hallway. |
| `Hobby Room` | The image/photo is of a hobby room. |
| `Inlaw` | The image/photo is of an in-law or mother-in-law room or quarters. |
| `Kitchen` | The image/photo is of a kitchen. |
| `Lake` | The image/photo is of a lake. |
| `Laundry` | The image/photo is of a laundry room. |
| `Library` | The image/photo is of a library. |
| `Living Room` | The image/photo is of a living room. |
| `Loading Dock` | The image/photo is of a loading dock. |
| `Lobby` | The image/photo is of a lobby. |
| `Loft` | The image/photo is of a loft. |
| `Lot` | The image/photo is of a lot. |
| `Map` | The image/photo is of a map. |
| `Master Bathroom` | The image/photo is of a primary bathroom. |
| `Master Bedroom` | The image/photo is of a primary bedroom. |
| `Media Room` | The image/photo is of a media room. |
| `Mud Room` | The image/photo is of a mud room. |
| `Nursery` | The image/photo is of a nursery. |
| `Office` | The image/photo is of an office. |
| `Other` | The image/photo is of a room or aspect of the property other than those listed in the ImageOf enumerations. |
| `Out Buildings` | The image/photo is of an out building. |
| `Pantry` | The image/photo is of a pantry. |
| `Parking` | The image/photo is of a parking area. |
| `Patio` | The image/photo is of a patio. |
| `Pier` | The image/photo is of a pier. |
| `Plat Map` | The image/photo is of a plat map. |
| `Playground` | The image/photo is of a playground. |
| `Pond` | The image/photo is of a pond. |
| `Pool` | The image/photo is of a pool. |
| `Reception` | The image/photo is of a reception area. |
| `Recreation Room` | The image/photo is of a recreation room. |
| `Sauna` | The image/photo is of a sauna. |
| `Showroom` | The image/photo is of a showroom. |
| `Side of Structure` | The image/photo is of the side of a structure. |
| `Sitting Room` | The image/photo is of a sitting room. |
| `Spa` | The image/photo is of a spa. |
| `Stable` | The image/photo is of a stable. |
| `Stairs` | The image/photo is of stairs. |
| `Storage` | The image/photo is of a storage area. |
| `Studio` | The image/photo is of a studio. |
| `Study` | The image/photo is of a study. |
| `Sun Room` | The image/photo is of a sunroom. |
| `Tennis Court` | The image/photo is of a tennis court or tennis courts. |
| `Utility Room` | The image/photo is of a utility room. |
| `View` | The image/photo is of a view. |
| `Walk-In Closet(s)` | The image/photo is of a walk-in closet or walk-in closets. |
| `Waterfront` | The image/photo is of a waterfront. |
| `Wine Cellar` | The image/photo is of a wine cellar. |
| `Workshop` | The image/photo is of a workshop. |
| `Yard` | The image/photo is of a yard. |

### MediaAlteration

| Value | Definition |
|---|---|
| `Decluttered - Item Removed` | Removal of items that may be deceitful or depict a listing inaccuracy in some way, including the removal of items beyond the homeowner's control, such as power lines, poor views or unsightly property … |
| `Model Home` | A representative home, apartment or office space used as part of a sales campaign to demonstrate the design, structure and appearance of the dwelling. |
| `None` | There has been no alteration or fabrication of the image. |
| `Other Media Modification` | The image has been altered in some other way than is noted in this list of lookup values. |
| `Twilight Conversion` | If the sun is placed in the wrong location, a viewer may believe that certain rooms or amenities (e.g., pool, sunroom) will receive a misrepresented amount of sunlight or particular view at a time of day. |
| `Virtual Enhancements` | Visual enhancements may include changing the sky color or greening the grass, but these enhancements should be disclosed if they are deceptive (e.g., adding green grass where healthy grass cannot grow… |
| `Virtual Renovation` | Undisclosed, this can mislead a buyer into thinking the property has already been renovated and that there are no more expenses necessary to reach that state. |
| `Virtual Representation - To Be Built` | Undisclosed, a buyer may not realize that this is an artist rendering and not an actual build. |
| `Virtual Representation - Under Construction` | Undisclosed, a buyer may not realize that this is an artist rendering and not an actual build in progress. |
| `Virtual Staging - Item Addition` | Addition of virtual items or depictions that may misrepresent what is part of the property, the condition of the property or proportions/sizes of rooms or amenities. |

### MediaCategory

| Value | Definition |
|---|---|
| `Agent Photo` | The media is an agent photo. |
| `Branded Virtual Tour` | The media is a branded virtual tour. |
| `Document` | The media is a document. |
| `Floor Plan` | The media is a floor plan. |
| `Office Logo` | The media is an office logo. |
| `Office Photo` | The media is an office photo. |
| `Photo` | The media is a photo. |
| `Unbranded Virtual Tour` | The media is an unbranded virtual tour. |
| `Video` | The media is a video. |

### MediaType

| Value | Definition |
|---|---|
| `doc` | The media is a Microsoft Word .doc file type. |
| `docx` | The media is a Microsoft Word docx file type. |
| `gif` | The media is a .gif file type. |
| `jpeg` | The media is a jpeg (or jpg) file type. |
| `mov` | The media is a .mov file type. |
| `mp4` | The media is an .mp4 file type. |
| `mpeg` | The media is an .mpeg (or .mpg) file type. |
| `pdf` | The media is a .pdf file type. |
| `png` | The media is a .png file type. |
| `quicktime` | The media is a QuickTime file type. |
| `rtf` | The media is an .rtf file type. |
| `tiff` | The media is a .tiff (or .tif) file type. |
| `txt` | The media is a .txt file type. |
| `wmv` | The media is a .wmv file type. |
| `xls` | The media is a Microsoft Excel .xls file type. |
| `xlsx` | The media is a Microsoft Excel .xlsx file type. |

### Permission

| Value | Definition |
|---|---|
| `Agent Only` | The image or document is for agent use only. |
| `Firm Only` | The image or document is for firm use only. |
| `IDX` | The image or document is acceptable for IDX use. |
| `Office Only` | The image or document is for office use only. |
| `Private` | The image or document is private and should have limited distribution. |
| `Public` | The image or document may be viewed by the public. |
| `VOW` | The image or document is okay for VOW use. |

### ResourceName

| Value | Definition |
|---|---|
| `Association` | This record is related to another record in the Association Resource. |
| `Contacts` | This record is related to another record in the Contacts Resource. |
| `Member` | This record is related to another record in the Member Resource. |
| `Office` | This record is related to another record in the Office Resource. |
| `Property` | This record is related to another record in the Property Resource. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
