---
name: uk-deliverables-workstages
description: >
  Issue packs, transmittals, deliverables registers, RACI matrices, ISO 19650 status codes, and stage freeze discipline
  for UK architectural projects. Use when coordinating consultant outputs by workstage.
disable-model-invocation: true
user-invocable: true
---

# UK Deliverables and Workstages

For RIBA stage definitions and gates, use `uk-plan-of-work`. For technical drawing content, use `uk-construction-documentation`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Issue pack structure and transmittals | `uk-deliverables-workstages` | — |
| Deliverables register by stage | `uk-deliverables-workstages` | `uk-plan-of-work` for stage gates |
| Consultant RACI and coordination | `uk-deliverables-workstages` | `uk-project-management` for delivery plan |
| ISO 19650 status codes (S0–AFC) | `uk-deliverables-workstages` | — |
| Stage freeze and change control | `uk-deliverables-workstages` | `uk-plan-of-work` |
| Drawing technical content | `uk-deliverables-workstages` | `uk-construction-documentation` |

## Issue-pack ready rule

An issue pack is ready only when:

1. Cover sheet and transmittal (`TX-[project]-[recipient]-[YYYYMMDD]`) are complete.
2. Deliverables register lists every document with revision, status, and author.
3. All cross-referenced documents are included or explicitly excluded with reason.
4. Recipient action (review / approve / comment / record) is stated.
5. Lead consultant has confirmed coordination sign-off.

## Execution protocol

1. Confirm RIBA stage, recipient group (client, LPA, BC, contractor, consultant), and BIM level if applicable.
2. Define deliverables register from [`../../references/templates/deliverables.md`](../../references/templates/deliverables.md) §1 stage map.
3. Assign RACI per discipline; identify lead consultant duties (meetings, progress reports, freeze logs).
4. Apply ISO 19650 status codes where BIM is used: WIP → S0 → S1 → S2 → A → B → C → CR → ACO → AB → AF → AU → AFC.
5. Issue transmittal with clear purpose (information / review / approval / construction).
6. Log stage freeze decisions in [`../../references/templates/stage-decision-log.md`](../../references/templates/stage-decision-log.md).

## Inputs required

- Project information standard (ISO 19650 level, naming convention)
- Consultant appointment scopes and RACI
- Current deliverables register and outstanding items
- Recipient requirements (client, LPA, BC, contractor)

## Outputs

- Issue pack cover and transmittal
- Deliverables register with status and revision
- RACI matrix for current stage
- Stage freeze log and change-control record

## Halt rules

- Halt authority submissions marked as approved without registered professional sign-off scope confirmed.
- Do not issue for construction (AFC) without lead consultant coordination sign-off.

## Secondary cross-links

- `uk-plan-of-work` — stage gates and task lists
- `uk-project-management` — delivery plan and client reporting
- `uk-construction-documentation` — technical package content
- `uk-procurement-strategy` — tender issue packs at Stage 4

## References

* [deliverables.md](../../references/templates/deliverables.md) — template index and stage map
* [stage-decision-log.md](../../references/templates/stage-decision-log.md) — freeze and gate records
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
