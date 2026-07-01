---
name: uk-plan-of-work
description: >
  RIBA Plan of Work 2020 stages 0–7, stage gates, BSA gateway mapping, and per-stage task checklists for UK projects.
  Use when the user asks about workstage progression, stage deliverables, or gateway alignment.
disable-model-invocation: true
user-invocable: true
---

# UK Plan of Work

For issue-pack structure and transmittals, use `uk-deliverables-workstages`. For detailed compliance roadmaps, use `uk-building-codes`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| RIBA stage 0–7 tasks and gates | `uk-plan-of-work` | — |
| BSA gateway mapping per stage | `uk-plan-of-work` | `uk-building-codes` for HRB dutyholder detail |
| Stage gate checklist / freeze | `uk-plan-of-work` | `uk-deliverables-workstages` for issue-pack rules |
| Issue pack contents | `uk-plan-of-work` | `uk-deliverables-workstages` |
| Contract variations / EOT | `uk-plan-of-work` | `uk-tender-contract-administration` |

## Stage mapping

| RIBA stage | Name | Planning | Building Control | Contract / commercial |
|------------|------|----------|------------------|----------------------|
| 0 | Strategic definition | Feasibility, policy review | HRB classification memo | Business case, procurement strategy outline |
| 1 | Preparation and briefing | Project brief, stakeholder map | Pre-application advice | Appointments, fee basis |
| 2 | Concept design | Planning strategy, D&A Statement | Fire strategy concept | Cost plan 1, programme outline |
| 3 | Spatial coordination | Planning submission | BR pre-application | Coordinated Stage 3 package |
| 4 | Technical design | Discharge conditions | Full Plans / HRB Gateway 2 | Tender documents, cost plan 3 |
| 5 | Manufacturing and construction | Condition compliance | Site inspections, Gateway 2 hold | Variations, valuations |
| 6 | Handover | — | Completion certificate, Gateway 3 | PC, Regulation 38, snagging |
| 7 | In use | — | Golden thread updates (HRB) | Defects period, PoE |

## Execution protocol

1. Confirm current RIBA stage, HRB status, and jurisdiction (England default).
2. Identify the next stage gate and required inputs per [`../../references/uk-pow-stages-0-7.md`](../../references/uk-pow-stages-0-7.md).
3. Map statutory milestones (planning, BC, BSA gateways) to the stage — keep planning and BR tracks separate.
4. List deliverables with owner, due date, and approval authority.
5. Flag stage-freeze criteria and change-control route if gate is imminent.
6. Cross-reference [`../../references/templates/stage-gate-checklist.md`](../../references/templates/stage-gate-checklist.md) for formal records.

## Inputs required

- Project brief, classification (HRB/non-HRB), and appointment scope
- Current stage deliverables status and outstanding consultant inputs
- Planning and Building Control submission history
- Contract form and procurement route

## Outputs

- Stage gate checklist with pass/fail criteria
- Per-stage task tracker with owners and due dates
- BSA gateway alignment memo (HRB projects)
- Stage decision log per [`../../references/templates/stage-decision-log.md`](../../references/templates/stage-decision-log.md)

## Halt rules

- Halt stage progression advice if HRB status is unknown on a regulatory-sensitive question.
- Do not assume UK Building Regulations apply to devolved nations without confirmation.

## Secondary cross-links

- `uk-deliverables-workstages` — issue packs and RACI
- `uk-project-management` — delivery plan and client reporting
- `uk-building-codes` — gateway readiness and compliance roadmaps
- `uk-procurement-strategy` — route selection at Stage 0–1

## References

* [uk-pow-stages-0-7.md](../../references/uk-pow-stages-0-7.md) — full per-stage checklists
* [stage-gate-checklist.md](../../references/templates/stage-gate-checklist.md) — gate record template
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
