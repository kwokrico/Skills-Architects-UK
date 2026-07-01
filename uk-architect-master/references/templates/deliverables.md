# UK architect deliverables — template index

Use this file when the user needs a **formal record**, stage gate pack, or contract-facing artifact. Match structure to the template below; issue standalone files from [`compliance-memo.md`](compliance-memo.md), [`stage-decision-log.md`](stage-decision-log.md), and [`snagging-schedule.md`](snagging-schedule.md) where noted.

**Conventions** (see [`operational.md`](../operational.md)):

| Artifact | ID pattern |
|----------|------------|
| Stage decision log | `SDL-[project]-[stage]-[YYYYMMDD]` |
| Compliance memo | `CM-[project]-[topic]-[rev]` |
| Snagging list | `SN-[project]-[zone]-[rev]` |
| Transmittal | `TX-[project]-[recipient]-[YYYYMMDD]` |
| Site inspection | `SI-[project]-[visit]-[YYYYMMDD]` |
| Fee proposal | `FP-[project]-[rev]` |

**Jurisdiction:** England default unless stated. Confirm Wales, Scotland, or Northern Ireland when statutory references differ.

**Disclaimer:** Templates support professional practice workflow only — not statutory sign-off, legal advice, or structural/fire certification.

---

## 0. Universal response skeleton

Apply to any substantive technical or commercial answer (master §3.1). Start with the deliverable; no filler preamble.

```markdown
## Summary
[Position in one paragraph — what we know, what we recommend]

## Contractual / regulatory position
- Planning: [status]
- Building Control / BSR: [status; Gateway if HRB]
- Appointment: [scope and limits]
- Contract: [form, relevant clause or notice type]

## Analysis
[Objective assessment; cite Approved Documents, contract, or policy — do not invent citations]

## Options and recommendation
| Option | Pros | Cons | Programme |
|--------|------|------|-----------|
| A | | | |
| B | | | |

**Recommendation:** [Clear preferred route and conditions]

## Risks, next steps, and programme impact
- [Risk] — [Mitigation] — [Owner] — [Due]

## Clarifications required
- [ ] [Missing intake item from operational checklist]
```

---

## 1. RIBA stage map — typical architect outputs

| Stage | Name | Primary deliverables (architect-led or coordinated) |
|-------|------|-----------------------------------------------------|
| 0 | Strategic definition | Strategic brief, feasibility options, order-of-cost study, project risks register |
| 1 | Preparation and briefing | Project brief, stakeholder map, spatial requirements, gateway / HRB classification memo |
| 2 | Concept design | Concept drawings, planning strategy, D&A Statement draft, fire strategy concept, sustainability targets |
| 3 | Spatial coordination | Coordinated Stage 3 package, planning submission (if applicable), BR pre-application advice record |
| 4 | Technical design | Technical design drawings, specifications (NBS/Uniclass), BR full plans submission, tender documents |
| 5 | Manufacturing and construction | IFC/issue-for-construction, site inspections, RFIs, variations, H&S file inputs, gateway evidence (HRB) |
| 6 | Handover | PC checklist, snagging, Regulation 38 pack, O&M coordination, defects lists, final account support |
| 7 | In use | PoE brief, lessons learned, golden-thread updates (HRB), asset information updates |

---

## 2. Standalone template files

| Template | Use when |
|----------|----------|
| [`stage-decision-log.md`](stage-decision-log.md) | Stage gate, design freeze, procurement route, or significant project decision |
| [`compliance-memo.md`](compliance-memo.md) | Statutory conflict, halt condition, or formal compliance position |
| [`snagging-schedule.md`](snagging-schedule.md) | Pre-PC / PC / defects-period defect tracking |

---

## 3. Appointment and commercial

### 3.1 Fee proposal and scope of services

**Ref:** `FP-[project]-[rev]`  
**Stage:** 0–1 (issue); revise on scope change

```markdown
# Fee proposal — [Client] — [Project]

**Ref:** FP-[project]-[rev]  
**Date:** [YYYY-MM-DD]  
**Valid until:** [date]  
**Prepared by:** [Practice name / ARB registered architect]

## Executive summary
[One paragraph: project, our understanding, recommended appointment structure, total fee range or fixed sum]

## Project understanding
- **Site:** [address, constraints]
- **Proposed use:** [use class / brief]
- **Procurement route (assumed):** [traditional / D&B / management / etc.]
- **Target programme:** [key dates]
- **HRB / BSA:** [Yes/No/Unknown — if Yes, note gateway and golden-thread implications]

## Scope of services
Services are offered under [RIBA Professional Services Contract 2020 / bespoke terms — state which].

| RIBA stage | Included services | Excluded / by others |
|------------|-------------------|----------------------|
| 0–1 | [e.g. brief development, feasibility layouts] | [e.g. topographical survey by client] |
| 2–3 | [e.g. concept and spatial design, planning coordination] | |
| 4 | [e.g. technical design, BR submission coordination] | |
| 5–6 | [e.g. contract admin, site visits — state frequency] | |
| 7 | [e.g. PoE — if included] | |

### Assumed visit regime (Stage 5–6)
- **Contract administration:** [Yes/No]
- **Site inspections:** [e.g. fortnightly during main works] — additional visits at [hourly rate / day rate]
- **Meeting attendance:** [design team, client, contractor]

## Fee basis
| Element | Basis | Amount (ex VAT) |
|---------|-------|-----------------|
| Stages 0–3 | [lump sum / % of construction cost / hourly cap] | £ |
| Stage 4 | | £ |
| Stage 5–6 CA | [ % of contract sum / monthly retainer ] | £ |
| Expenses | [mileage, printing, planning fees at net + X%] | As incurred |
| **Total (ex VAT)** | | **£** |

## Payment terms
- [e.g. monthly invoices, stage payments tied to deliverables]
- **Suspension:** per contract if fees overdue
- **VAT:** charged at prevailing rate

## Programme and dependencies
- Client decisions within [X] working days
- Consultant information per agreed programme
- Planning / BR timelines not guaranteed

## Professional standards and insurance
- Services by ARB-registered architects
- PI cover: £[limit] aggregate
- Limitation of liability: [per appointment terms]

## Exclusions and special assumptions
- [Structural, MEP, fire engineering by separate appointments]
- [Party wall, ecology, transport, etc.]
- [Listed building / conservation specialist if needed]

## Terms and acceptance
- Subject to signed appointment and agreed programme
- [Conflict check / money laundering / CDM competence declarations if required]

**Accepted by client:** _________________________ **Date:** ___________
```

### 3.2 Consultant appointment instruction

**Ref:** `CI-[project]-[discipline]-[rev]`

```markdown
# Consultant instruction — [Discipline] — [Project]

**From:** [Lead architect / CA]  
**To:** [Consultant firm]  
**Ref:** CI-[project]-[discipline]-[rev]  
**Date:** [YYYY-MM-DD]

## Instruction
[Clear description of work required — drawings, calculations, report, workshop attendance]

## Scope boundary
- **In scope:** [ ]
- **Out of scope:** [ ]
- **Interface with:** [other consultants / contractor]

## Programme
| Milestone | Date |
|-----------|------|
| Information required for coordination | |
| Issue for review | |
| Final issue | |

## Standards and deliverables
- [British Standards, Approved Documents, employer requirements]
- **Format:** [PDF / native model / IFC] per [BEP / EIR]
- **Classification:** [Uniclass / NBS clauses]

## Fees
[Fixed fee / variation to existing appointment / day rate cap]

**Authorised by:** [Name, role]
```

---

## 4. Planning and consent

### 4.1 Planning coordination report

**Stage:** 2–3 | **Ref:** `PCR-[project]-[rev]`

```markdown
# Planning coordination report — [Project]

**Ref:** PCR-[project]-[rev]  
**Date:** [YYYY-MM-DD]  
**LPA:** [authority]  
**Application type:** [full / outline / reserved matters / LDC / prior approval]

## Summary
[Planning strategy, key risks, recommended submission route and programme]

## Site and policy context
- **Designations:** [conservation area, listed building, TPO, flood zone, HRB policy]
- **NPPF / local plan:** [relevant policies]
- **Use class:** [existing → proposed]
- **CIL / s106:** [liable / heads of terms / draft obligations]

## Proposal description
[GIA/NIA, units, height, access, parking, refuse, cycle storage]

## Consultation and engagement
| Stakeholder | Status | Issues |
|-------------|--------|--------|
| Pre-application | [date / ref] | |
| Highways | | |
| Environment / ecology | | |

## Submission package checklist
See `uk-spatial-planning/references/planning-submission-checklist.md`. Confirm LPA validation list before lodgement.

| Item | Status | Owner |
|------|--------|-------|
| Application form and fee | | |
| Plans and elevations | | |
| Design & Access Statement | | |
| Planning statement | | |
| Technical annexes | | |

## Conditions anticipation
| Likely condition | Design response |
|----------------|-----------------|
| Materials | | |
| Hours / construction management | | |

## Programme
- Target submission: [date]
- Estimated determination: [weeks] + [disposal of conditions]

## Recommendation
[Proceed / revise / alternative scheme]
```

### 4.2 Design and Access Statement — outline

**Stage:** 2–3 (planning submission)

```markdown
# Design and Access Statement — [Project] — OUTLINE

*Expand sections per LPA and project scale; required for major development and where policy demands.*

## 1. Introduction
- Project, site address, applicant, design team
- Planning history and context

## 2. Design principles
- Client brief and objectives
- Urban design / context response (scale, massing, materials)
- Sustainability and climate resilience (Part L, Part O, WLC targets)

## 3. Layout and access
- Movement hierarchy: pedestrian, cycle, vehicle, service
- Inclusive access (Part M): level access, lifts, sanitary provision, contrast, wayfinding
- Public realm and landscape interface

## 4. Built form
- Massing diagram and rationale
- Elevations and materials palette
- Daylight/sunlight (if relevant): [study reference]

## 5. Internal layout
- Uses and flexibility
- Residential / commercial mix if applicable
- Servicing and refuse strategy

## 6. Heritage (if applicable)
- Listed building / conservation area / HIA summary
- Harm and public benefit balance

## 7. Consultation
- Stakeholder engagement summary and design changes made

## 8. Conclusion
- How proposal meets local plan and NPPF tests
```

---

## 5. Building Regulations and building safety

### 5.1 Building Control submission transmittal

**Stage:** 4 | **Ref:** `TX-[project]-BCB-[YYYYMMDD]`

```markdown
# Transmittal — Building Regulations submission — [Project]

**To:** [LABC / Approved Inspector / RBAC]  
**From:** [Lead designer / agent]  
**Ref:** TX-[project]-BCB-[YYYYMMDD]

## Submission type
- [ ] Full plans | [ ] Building notice | [ ] Regularisation
- **HRB:** [Yes/No] — if Yes, Gateway 2 reference: [ ]

## Package contents
| Ref | Document | Rev | Date |
|-----|----------|-----|------|
| | General arrangement plans | | |
| | Specifications / schedule of works | | |
| | Structural design certificate / calcs | | |
| | Fire strategy / engineered solution | | |
| | Part L / SAP or SBEM summary | | |
| | Part O / TM59 summary (if applicable) | | |
| | Part M access strategy | | |
| | Drainage / S104 / S278 interfaces | | |

## Declarations
- Design prepared to meet functional requirements of Building Regulations
- **BR Principal Designer** (if appointed): [name]
- CDM Principal Designer (construction H&S): [name] — separate appointment

## Queries for Building Control
1. [ ]
```

### 5.2 HRB gateway / golden-thread record

**Stage:** 1–6 (HRB only) | **Ref:** `GT-[project]-G[n]-[rev]`

```markdown
# Gateway [1/2/3] compliance record — [Project]

**Ref:** GT-[project]-G[n]-[rev]  
**Date:** [YYYY-MM-DD]  
**Accountable person / client dutyholder:** [name]

## Building classification
- **HRB confirmation:** [criteria met — cite current regulations]
- **BSR engagement:** [reference numbers, dates]

## Gateway status
| Gateway | Requirement | Evidence held | Status |
|---------|-------------|---------------|--------|
| G1 Planning | BSR consultation | | |
| G2 Construction | Design meets functional reqs | | |
| G3 Completion | Golden thread complete | | |

## Golden-thread information themes
- [ ] Fire and structure strategy (issued for construction)
- [ ] Change control log (design changes post-G2)
- [ ] Inspection and test records
- [ ] Resident engagement strategy (where required)

## Halt / escalation
- [ ] Do not proceed to construction without G2 approval (HRB)
- [ ] Do not occupy without G3 / FSC as applicable

## Next actions
| Action | Owner | Due |
|--------|-------|-----|
| | | |
```

### 5.3 Regulation 38 transmittal

**Stage:** 6 | Use with `uk-fire-life-safety/references/regulation-38-checklist.md`

```markdown
# Regulation 38 — fire safety information transmittal — [Project]

**Ref:** R38-[project]-[rev]  
**Date:** [YYYY-MM-DD]  
**From:** [Contract administrator / lead designer]  
**To:** [Responsible person — name and role]

## Purpose
Handover of fire safety information required under Regulation 38 at completion of building work.

## Recipient confirmation
- **Responsible person:** [name, organisation, contact]
- **Building address:** [ ]

## Enclosed information (checklist)
| Item | Ref | Rev | Included |
|------|-----|-----|----------|
| Fire strategy report | | | [ ] |
| Record drawings — compartmentation | | | [ ] |
| Fire door schedule and specifications | | | [ ] |
| Active fire measures — O&M and commissioning | | | [ ] |
| Maintenance and inspection regime | | | [ ] |

## Linked contract events
- Practical completion certificate: [date / pending]
- Building Control completion certificate: [ref]

**Received by responsible person:** _________________________ **Date:** ___________
```

---

## 6. Design development and coordination

### 6.1 Design review minutes

**Stage:** 2–4 | **Ref:** `DRM-[project]-[session]-[YYYYMMDD]`

```markdown
# Design review minutes — [Project] — Session [n]

**Date:** [YYYY-MM-DD]  
**Chair:** [ ]  
**Attendees:** [client, architect, consultants, contractor if applicable]  
**Status reviewed:** [e.g. Stage 3 spatial — Rev P03]

## Summary of review
[Overall status: proceed / proceed with actions / hold]

## Actions
| ID | Item | Owner | Due | Status |
|----|------|-------|-----|--------|
| 1 | | | | Open |

## Key decisions
| Topic | Decision | Rationale |
|-------|----------|-----------|
| | | |

## Risks and dependencies
- [Interface risk] — [mitigation]

## Next review
**Date:** [ ] **Scope:** [ ]
```

### 6.2 Coordination issue sheet (multi-discipline)

**Ref:** `CIS-[project]-[rev]`

```markdown
# Coordination issue sheet — [Project] — Rev [X]

| ID | Location | Issue | Disciplines | Severity | Target resolution | Status |
|----|----------|-------|-------------|----------|-------------------|--------|
| 001 | [grid/level] | [clash / clearance / spec conflict] | ARC / STR / MEP | H/M/L | | Open |

**Severity:** H = blocks issue for construction; M = design change required; L = comment
```

---

## 7. Procurement and contract administration

### 7.1 Tender analysis summary

**Stage:** 4–5 | **Ref:** `TAS-[project]-[rev]`

```markdown
# Tender analysis summary — [Project]

**Ref:** TAS-[project]-[rev]  
**Date:** [YYYY-MM-DD]  
**Contract form:** [e.g. JCT D&B 2024 / NEC4 ECC Option C]  
**CA:** [name]

## Summary recommendation
[Preferred tenderer and conditions for award — subject to client approval]

## Tenderers compared
| Criterion | Weight | Tenderer A | Tenderer B | Tenderer C |
|-----------|--------|------------|------------|------------|
| Price | | £ | £ | £ |
| Programme | | wks | wks | wks |
| Quality / method | | | | |
| Preliminaries / risk | | | | |
| **Weighted score** | | | | |

## Qualifications and exclusions
| Tenderer | Material qualifications | Risk to client |
|----------|-------------------------|----------------|
| | | |

## Equalisation / clarifications issued
- [RFQ / clarification log ref]

## Contract data amendments proposed
- [Retention, LDs, PI levels, design liability caps]

## Recommendation
[Award to X subject to: [client approvals, bond, collateral warranties, novation]]

**Client decision:** [ ] Approved [ ] Re-tender [ ] Negotiate
```

### 7.2 Request for information (RFI) — architect response

**Stage:** 5–6 | **Ref:** `RFI-[project]-[number]-R[rev]`

```markdown
# RFI response — [Project]

**RFI no.:** [contractor ref]  
**Our ref:** RFI-[project]-[number]-R[rev]  
**Date received:** [ ]  
**Date response:** [YYYY-MM-DD]  
**Responded by:** [architect / CA]

## Question (summary)
[Contractor query in brief]

## Response
[Clear instruction or information — reference drawing/spec clause]

## Contractual status
- [ ] Confirmed variation required — VO to follow
- [ ] Clarification only — no change to contract sum/time
- [ ] Provisional — subject to [client / engineer confirmation]

## Attachments
| Drawing / document | Rev |
|--------------------|-----|
| | |

## Programme impact
[None / EOT notification may arise — refer to CA and contract]
```

### 7.3 Variation / change proposal

**Stage:** 5–6 | **Ref:** `VO-[project]-[number]` or `CE-[project]-[number]` (NEC)

```markdown
# Change proposal — [Project]

**Ref:** VO-[project]-[number]  
**Date:** [YYYY-MM-DD]  
**Initiated by:** [client / contractor / architect]  
**Contract:** [JCT / NEC clause reference]

## Description of change
[What is proposed — location, scope, reason]

## Reason
- [ ] Client instruction
- [ ] Design development / coordination
- [ ] Unforeseen condition
- [ ] Statutory / Building Control requirement

## Cost estimate
| Item | £ (ex VAT) |
|------|------------|
| Works | |
| Prelims / OH&P | |
| **Total** | |

## Time impact
- **Extension of time:** [days / none / TBC]
- **Critical path:** [comment]

## Design compliance
- Building Regulations: [no change / submission required]
- Planning: [permitted / condition discharge / new application required]
- Fire strategy: [review by fire engineer — Y/N]

## Recommendation
[Proceed / reject / defer pending client approval]

**Client approval:** _________________________ **Date:** ___________
```

---

## 8. Site and construction

### 8.1 Site inspection report

**Stage:** 5–6 | **Ref:** `SI-[project]-[visit]-[YYYYMMDD]`

```markdown
# Site inspection report — [Project]

**Ref:** SI-[project]-[visit]-[YYYYMMDD]  
**Date of visit:** [YYYY-MM-DD]  
**Weather:** [ ]  
**Attendees:** [architect, contractor, others]  
**Contract stage:** [substructure / superstructure / fit-out]

## Summary
[Overall progress, conformity with issued information, key concerns]

## Works observed
| Area | Observation | Conformance (Y/N/P) | Action |
|------|-------------|---------------------|--------|
| | | | |

## Health and safety (matters noted — not H&S audit)
- [Site induction, edge protection, housekeeping — refer hazards to principal contractor]

## Instructions issued on site
| Ref | Instruction | To |
|-----|-------------|-----|
| | | Site manager |

## Open RFIs / defects
- RFI [ ] — status
- Snagging ref SN-[project]-[zone]

## Photographs
- [File path / photo log numbers]

## Next visit
**Proposed:** [date] **Focus:** [ ]
```

### 8.2 Non-conformance report (architect-issued)

**Ref:** `NCR-[project]-[number]`

```markdown
# Non-conformance report — [Project]

**Ref:** NCR-[project]-[number]  
**Date:** [YYYY-MM-DD]  
**Raised by:** [architect / CA]  
**Location:** [ ]

## Non-conformance
[Description vs issued drawing/specification/regulation]

## Requirement
[Drawing ref / spec clause / regulation]

## Action required
[Remedy / investigate / propose alternative for approval]

## Target close-out:** [date]  
**Contractor response:** [ ] Accepted [ ] Proposed alternative — see [ref]

**Closed:** [date] **Verified by:** [ ]
```

---

## 9. Handover and close-out

### 9.1 Practical completion checklist

**Stage:** 6 | **Ref:** `PC-[project]-[rev]`

```markdown
# Practical completion checklist — [Project]

**Ref:** PC-[project]-[rev]  
**Contract:** [form]  
**Target PC date:** [YYYY-MM-DD]

## Contract administrator — readiness
| Item | Complete | Notes |
|------|----------|-------|
| Works substantially complete per contract definition | [ ] | |
| Snagging list issued (non-material items only) | [ ] | |
| Statutory completions (Building Control, FSC if HRB) | [ ] | |
| Testing and commissioning certificates | [ ] | |
| Regulation 38 pack ready / issued | [ ] | |
| O&M manuals and as-built information | [ ] | |
| H&S file (CDM) complete | [ ] | |
| Golden thread upload (HRB) | [ ] | |
| Collateral warranties / bonds | [ ] | |
| Final account preparation started | [ ] | |

## Outstanding items agreed for post-PC
| Item | Agreed completion | LDs / retention impact |
|------|-------------------|------------------------|
| | | |

## Certificates to issue
- [ ] Practical Completion Certificate — date: [ ]
- [ ] Making good defects period: [months] from PC

**CA signature:** _________________________ **Date:** ___________
```

### 9.2 Certificate of making good defects — architect record

**Stage:** 6 (end of DLP)

```markdown
# Making good defects — completion record — [Project]

**Defects period:** [start PC date] to [end date]  
**Contract:** [JCT clause reference]

## Defects notified during DLP
| Ref | Description | Notified | Closed |
|-----|-------------|----------|--------|
| | | | |

## Outstanding at DLP end
| Item | Agreed remedy | Date |
|------|---------------|------|
| None / [list] | | |

## Certificate
- [ ] Certificate of Making Good Defects to issue
- [ ] Retention release recommended — subject to contract and final account

**CA:** [name] **Date:** [YYYY-MM-DD]
```

---

## 10. Briefing and post-occupancy

### 10.1 Project brief (Stage 0–1)

```markdown
# Project brief — [Project] — Rev [X]

**Client:** [ ]  
**Date:** [YYYY-MM-DD]  
**Status:** Draft / Agreed

## Strategic objectives
[Business case, success criteria, budget ceiling, programme]

## Site
- Address, ownership, surveys available
- Constraints: [access, utilities, ecology, heritage, neighbours]

## Spatial requirements
| Space | Area (m²) | Adjacencies | Notes |
|-------|-----------|-------------|-------|
| | | | |

## Performance requirements
- **Accessibility:** [Part M target / inclusive design aspirations]
- **Energy / carbon:** [Part L, EPC, LETI, BREEAM]
- **Fire:** [residential/non-residential, HRB]
- **Acoustics / daylight:** [standards]

## Procurement and team
- Route: [ ]
- Consultants required: [ ]

## Approvals
**Client sign-off:** _________________________ **Date:** ___________
```

### 10.2 Post-occupancy evaluation — briefing note

**Stage:** 7

```markdown
# PoE briefing note — [Project]

**Occupation date:** [ ]  
**Evaluation window:** [e.g. 12 months post-occupation]

## Objectives
- Compare performance to design intent (energy, comfort, accessibility)
- Capture lessons for [practice / client portfolio]

## Metrics
| Metric | Design target | Measurement method |
|--------|---------------|-------------------|
| Energy use | [kWh/m²/yr] | [TM54 / smart meter] |
| Overheating | [Part O] | [Monitoring / survey] |
| User satisfaction | | [Survey] |

## Participants and programme
- [Workshops, surveys, site walkover dates]

## Outputs
- PoE report — ref: `POE-[project]-[rev]`
- Feedback to asset information / golden thread (HRB)
```

---

## 11. Template selection guide

| User intent | Start with |
|-------------|------------|
| Stage gate / design freeze | §2 `stage-decision-log.md` |
| Compliance conflict or halt | §2 `compliance-memo.md` |
| Defects at PC | §2 `snagging-schedule.md` + §9.1 |
| Win work / appoint practice | §3.1 |
| Planning submission | §4.1 + §4.2 |
| BR submission | §5.1 |
| HRB / BSR | §5.2 |
| Fire handover | §5.3 |
| Tender award | §7.1 |
| Site query | §7.2 or §8.1 |
| Client change | §7.3 |
| General technical answer | §0 |

---

*Align deliverables to current RIBA Plan of Work, contract terms, and project information standard (ISO 19650 where BIM is used). Update gateway and HRB criteria against the Building Safety Act and applicable regulations at the time of issue.*
