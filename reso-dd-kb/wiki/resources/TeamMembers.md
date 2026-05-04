# TeamMembers

Fields tying Member records to related Teams records.

**RESO DD 2.0** — 21 fields · last revised 9/24/2015 · [dd.reso.org](https://dd.reso.org/DD2.0/TeamMembers/)

**Adoption** — weighted Org%: **0%** across 12 measured fields (median 0%, avg 0%).

## Groups

- **Other** — 21 fields

## Fields

| Field | Type | Group | Lookup | Org% | Description | Source |
|---|---|---|---|---|---|---|
| `HistoryTransactional` | Collection |  |  |  | The HistoryTransactional resource is the field-level audit log for changes made to other RESO resources. | [link](https://dd.reso.org/DD2.0/TeamMembers/HistoryTransactional/) |
| `Member` | Resource |  |  |  | The Member resource describes a person who is a member of the MLS — most commonly a real estate agent or broker. | [link](https://dd.reso.org/DD2.0/TeamMembers/Member/) |
| `MemberKey` | String |  |  | 0% | A system-unique identifier for the member. | [link](https://dd.reso.org/DD2.0/TeamMembers/MemberKey/) |
| `MemberLoginId` | String |  |  | 0% | The ID used to log on to the MLS system. | [link](https://dd.reso.org/DD2.0/TeamMembers/MemberLoginId/) |
| `MemberMlsId` | String |  |  | 0% | The local, well-known identifier for the member as assigned by the MLS. | [link](https://dd.reso.org/DD2.0/TeamMembers/MemberMlsId/) |
| `ModificationTimestamp` | Timestamp |  |  | 0% | The date and time the listing was last modified, formatted as ISO 8601. | [link](https://dd.reso.org/DD2.0/TeamMembers/ModificationTimestamp/) |
| `OriginalEntryTimestamp` | Timestamp |  |  | 0% | Date/time the roster (member or office) record was originally input into the source system. | [link](https://dd.reso.org/DD2.0/TeamMembers/OriginalEntryTimestamp/) |
| `OriginatingSystem` | Resource |  |  |  | The originating system of the TeamMembers record. | [link](https://dd.reso.org/DD2.0/TeamMembers/OriginatingSystem/) |
| `OriginatingSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the originating record provider. | [link](https://dd.reso.org/DD2.0/TeamMembers/OriginatingSystemID/) |
| `OriginatingSystemKey` | String |  |  | 0% | The system key, a unique record identifier, from the originating system. | [link](https://dd.reso.org/DD2.0/TeamMembers/OriginatingSystemKey/) |
| `OriginatingSystemName` | String |  |  |  | The name of the originating record provider, most commonly the name of the MLS. | [link](https://dd.reso.org/DD2.0/TeamMembers/OriginatingSystemName/) |
| `SourceSystem` | Resource |  |  |  | The source system of the TeamMembers record. | [link](https://dd.reso.org/DD2.0/TeamMembers/SourceSystem/) |
| `SourceSystemID` | String |  |  |  | The RESO Unique Organization Identifier (UOI) OrganizationUniqueId of the source record provider. | [link](https://dd.reso.org/DD2.0/TeamMembers/SourceSystemID/) |
| `SourceSystemKey` | String |  |  | 0% | The system key, a unique record identifier, from the source system. | [link](https://dd.reso.org/DD2.0/TeamMembers/SourceSystemKey/) |
| `SourceSystemName` | String |  |  | 0% | The name of the team member record provider. | [link](https://dd.reso.org/DD2.0/TeamMembers/SourceSystemName/) |
| `TeamImpersonationLevel` | String List, Single |  | TeamImpersonationLevel | 0% | The level of impersonation the member is allowed within the team (i.e., Impersonate (to work as the team), On Behalf (to show the team name but also show the member's info), None (don't allow this mem… | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamImpersonationLevel/) |
| `TeamKey` | String |  |  | 0% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamKey/) |
| `TeamMemberKey` | String |  |  | 0% | A system unique identifier. | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamMemberKey/) |
| `TeamMemberNationalAssociationId` | String |  |  |  | The national association ID of the member (e.g., in the U.S., this is an M1 or NRDS number). | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamMemberNationalAssociationId/) |
| `TeamMemberStateLicense` | String |  |  |  | The license of the member. | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamMemberStateLicense/) |
| `TeamMemberType` | String List, Single |  | [TeamMemberType](#teammembertype) | 0% | The role of the member within the team (e.g., Team Lead, Showing Agent, Buyer Agent). | [link](https://dd.reso.org/DD2.0/TeamMembers/TeamMemberType/) |

## Field details

Per-field structured metadata scraped from DDwiki (BEDES mapping, property-type applicability, Spanish / French-Canadian display names, change-history dates).

<details><summary><code>HistoryTransactional</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>Member</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>MemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>MemberLoginId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Inicio de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>MemberMlsId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de MLS de Miembro
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>ModificationTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo de Modificación
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 9/24/2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginalEntryTimestamp</code></summary>

  - **Status:** Active
  - **Spanish Name:** Marca de Tiempo Entrada Original
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 9/24/2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>OriginatingSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>OriginatingSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>OriginatingSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre de Sistema de Origen
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>SourceSystem</code></summary>

  - **Status:** Active
  - **Status Change Date:** 1/6/2022
  - **Revision Date:** 1/6/2022
  - **Added in Version:** 1.7.0

</details>

<details><summary><code>SourceSystemID</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>SourceSystemName</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nombre Sistema Fuente
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 2/18/2016
  - **Added in Version:** 1.5.0

</details>

<details><summary><code>TeamImpersonationLevel</code></summary>

  - **Status:** Active
  - **Spanish Name:** Nivel de Suplantación de Equipo
  - **Status Change Date:** 7/21/2015
  - **Revision Date:** 3/24/2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Equipo
  - **Status Change Date:** 6/21/2016
  - **Revision Date:** 3/18/2015
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberKey</code></summary>

  - **Status:** Active
  - **Spanish Name:** Clave de Miembro de Equipo
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberNationalAssociationId</code></summary>

  - **Status:** Active
  - **Spanish Name:** ID de Asociación Nacional de Miembro de Equipo
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberStateLicense</code></summary>

  - **Status:** Active
  - **Spanish Name:** Licencia Estatal de Miembro de Equipo
  - **Status Change Date:** 8/9/2017
  - **Revision Date:** 1/17/2017
  - **Added in Version:** 1.4.0

</details>

<details><summary><code>TeamMemberType</code></summary>

  - **Status:** Active
  - **Spanish Name:** Tipo de Miembro de Equipo
  - **Status Change Date:** 12/26/2018
  - **Revision Date:** 10/9/2018
  - **Added in Version:** 1.4.0

</details>

## Lookups

### TeamMemberType

10 values · used by 1 field(s) · [dd.reso.org](https://dd.reso.org/DD2.0/lookups/TeamMemberType/)

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
_Generated by `reso-dd-kb/scripts/refresh.py` on 2026-05-04 from `raw/*.csv`. Do not hand-edit; rerun the script after changing inputs._
