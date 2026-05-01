# TeamMembers

_RESO Data Dictionary 2.0 resource — 21 fields. See [DDwiki](https://ddwiki.reso.org/display/DDW20/TeamMembers+Resource) for the canonical page._

**Adoption** — weighted Org%: **0%** across 12 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 21 fields

## Fields

| Field | Type | Group | Lookup | Sys% | Org% | Description | DDwiki |
|---|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135650) |
| `Member` | Resource |  |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135656) |
| `MemberKey` | String |  |  | 5% | 1% | A system-unique identifier for the member. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135661) |
| `MemberLoginId` | String |  |  | 5% | 1% | The ID used to log on to the MLS system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135667) |
| `MemberMlsId` | String |  |  | 5% | 1% | The local, well-known identifier for the member as assigned by the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135673) |
| `ModificationTimestamp` | Timestamp |  |  | 5% | 1% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135680) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 5% | 1% | Date/time the roster (member or office) record was originally input into the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135686) |
| `OriginatingSystem` | Resource |  |  |  |  | The originating system of the TeamMembers record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135692) |
| `OriginatingSystemID` | String |  |  | 1% | 1% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135702) |
| `OriginatingSystemKey` | String |  |  | 5% | 1% | The system key, a unique record identifier, from the originating system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135708) |
| `OriginatingSystemName` | String |  |  | 1% | 1% | The name of the originating record provider, most commonly the name of the MLS. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135714) |
| `SourceSystem` | Resource |  |  |  |  | The source system of the TeamMembers record. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135719) |
| `SourceSystemID` | String |  |  | 1% | 1% | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135727) |
| `SourceSystemKey` | String |  |  | 5% | 1% | The system key, a unique record identifier, from the source system. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135733) |
| `SourceSystemName` | String |  |  | 5% | 1% | The name of the team member record provider. | [link](https://ddwiki.reso.org/pages/viewpage.action?pageId=1135738) |
| `TeamImpersonationLevel` | String List, Single |  | TeamImpersonationLevel |  | 0% | The level of impersonation the member is allowed within the team (i.e., Impersonate (to work as the team), On Behalf (to show the team name but also show the member's info), None (don't allow this mem… | [link](https://ddwiki.reso.org/display/DDW20/TeamImpersonationLevel+Field) |
| `TeamKey` | String |  |  | 5% | 1% | A system-unique identifier for the team. | [link](https://ddwiki.reso.org/display/DDW20/TeamKey+Field) |
| `TeamMemberKey` | String |  |  | 5% | 1% | A system unique identifier. | [link](https://ddwiki.reso.org/display/DDW20/TeamMemberKey+Field) |
| `TeamMemberNationalAssociationId` | String |  |  | 1% | 1% | The national association ID of the member (e.g., in the U.S., this is an M1 or NRDS number). | [link](https://ddwiki.reso.org/display/DDW20/TeamMemberNationalAssociationId+Field) |
| `TeamMemberStateLicense` | String |  |  | 1% | 1% | The license of the member. | [link](https://ddwiki.reso.org/display/DDW20/TeamMemberStateLicense+Field) |
| `TeamMemberType` | String List, Single |  | [TeamMemberType](#teammembertype) | 5% | 1% | The role of the member within the team (e.g., Team Lead, Showing Agent, Buyer Agent). | [link](https://ddwiki.reso.org/display/DDW20/TeamMemberType+Field) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Member</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>MemberLoginId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Inicio de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de MLS de Miembro
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** SEP 24 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** ACTIVE
  - **Status Change Date:** JAN 06 2022
  - **Revision Date:** JAN 06 2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Nombre Sistema Fuente
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** FEB 18 2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>TeamKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Equipo
  - **Status Change Date:** JUN 21 2016
  - **Revision Date:** MAR 18 2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberKey</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Clave de Miembro de Equipo
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberNationalAssociationId</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** ID de Asociación Nacional de Miembro de Equipo
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberStateLicense</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Licencia Estatal de Miembro de Equipo
  - **Status Change Date:** AUG 09 2017
  - **Revision Date:** JAN 17 2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberType</code></summary>

  - **Status:** ACTIVE
  - **Spanish Name:** Tipo de Miembro de Equipo
  - **Status Change Date:** DEC 26 2018
  - **Revision Date:** OCT 09 2018
  - **Added in Version:** 1.4.0

</details>

## Lookups

### TeamMemberType

| Value | Definition |
|---|---|
| `Administration Assistant` | The member of a team who assists with administrative tasks. |
| `Buyer Agent` | A member of the real estate team. |
| `Lead Manager` | The member of the team who is the lead manager. |
| `Listing Agent` | The member of a team who is the lead manager. |
| `Marketing Assistant` | The member of a team who assists with marketing. |
| `Operations Manager` | The member of the team who manages operations. |
| `Showing Agent` | The member of a team who manages operations. |
| `Team Lead` | The leading member of a team. |
| `Team Member` | A member of a real estate team. |
| `Transaction Coordinator` | The member of a team who handles transaction details. |

---
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-01 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
