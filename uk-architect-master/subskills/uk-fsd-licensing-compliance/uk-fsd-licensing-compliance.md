---
name: uk-fsd-licensing-compliance
description: >
  FSO compliance evidence, fire commissioning, responsible person handover, and fire alarm/sprinkler testing chain
  for UK building completion. Use for fire services completion — not fire strategy design.
disable-model-invocation: true
user-invocable: true
---

# UK Fire Completion and Commissioning

For fire strategy design and AD B compliance, use `uk-fire-life-safety`. For BC completion sequencing, use `uk-op-submission-strategy`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| FSO compliance evidence at completion | `uk-fsd-licensing-compliance` | — |
| Fire alarm / sprinkler commissioning and testing | `uk-fsd-licensing-compliance` | — |
| Responsible person handover | `uk-fsd-licensing-compliance` | — |
| Regulation 38 fire safety information | `uk-fsd-licensing-compliance` | `uk-fire-life-safety` |
| Fire strategy design / AD B | `uk-fsd-licensing-compliance` | `uk-fire-life-safety` |
| Building Control completion certificate | `uk-fsd-licensing-compliance` | `uk-op-submission-strategy` |

## Handover sequence

1. **Design basis** — fire strategy, specification, and cause-and-effect diagrams as-built.
2. **Installation** — fire alarm, sprinklers, smoke control, emergency lighting per specification.
3. **Commissioning** — third-party testing per BS 5839, BS EN 12845, etc.; certificates issued.
4. **Inspection** — building control / fire engineer witness where required.
5. **Handover** — Regulation 38 pack to responsible person; FSO compliance evidence assembled.
6. **Ongoing** — responsible person duties under Fire Safety (England) Regulations 2022.

## Execution protocol

1. Confirm building use class, responsible person appointed, and fire strategy status.
2. List required commissioning tests by system (alarm, sprinkler, AOV, emergency lighting, dry/wet riser).
3. Define inspection readiness checklist with pass/fail criteria.
4. Coordinate hydrant, hose reel, and flow test requirements with fire engineer.
5. Assemble deliverable set for responsible person and BC completion pack.
6. Document escalation model for test failures (remedial scope, re-test, programme impact).

## Inputs required

- Fire strategy and cause-and-effect diagrams (as-built)
- Commissioning certificates and test records
- Responsible person appointment
- Regulation 38 pack draft status

## Outputs

- Fire commissioning checklist with test status
- Test certificates index
- Escalation stage plan for failures
- Responsible person handover pack outline

## Halt rules

- Cannot confirm FSO compliance without commissioning test passes and certificates.
- Novel fire engineering interpretation — escalate to fire engineer and building control.

## Secondary cross-links

- `uk-fire-life-safety` — fire strategy design
- `uk-op-submission-strategy` — BC completion sequencing
- `uk-building-services` — MEP fire services coordination
- `uk-practical-completion-snagging` — defects during commissioning

## References

* [regulation-38-checklist.md](../../references/checklists/regulation-38-checklist.md) — handover pack
* [bc-completion-readiness-matrix.md](../../references/templates/bc-completion-readiness-matrix.md) — completion tracker
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — FSO vocabulary
