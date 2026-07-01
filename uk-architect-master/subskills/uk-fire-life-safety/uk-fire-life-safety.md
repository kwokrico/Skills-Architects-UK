---
name: uk-fire-life-safety
description: >
  Supports UK fire strategy development, Approved Document B alignment, compartmentation, evacuation design, and
  Regulation 38 handover planning. Use for fire engineering coordination and life-safety design decisions.
disable-model-invocation: true
user-invocable: true
---

# UK Fire and Life Safety

For general Building Regulations routing, use `uk-building-codes`. For planning fire statements, use `uk-spatial-planning`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Fire strategy, AD B, means of escape | `uk-fire-life-safety` | — |
| Regulation 38 handover content | `uk-fire-life-safety` | `uk-practical-completion-snagging` for PC process |
| BSA gateway dutyholders only | `uk-fire-life-safety` | `uk-building-codes` |
| Early egress distance screen | `uk-fire-life-safety` | `uk-architect-calculator` (`egress_screen`) |
| FSD licensing / specialist sign-off | `uk-fire-life-safety` | `uk-fsd-licensing-compliance` |

## Execution protocol

1. Confirm building use, height, and HRB status; identify if a qualified fire engineer is appointed.
2. Establish design approach: code-compliant AD B route vs fire-engineered solution (document which).
3. Review means of escape, travel distances, compartmentation, firefighting access, and suppression assumptions.
4. Coordinate structural fire protection and services penetrations with envelope and MEP sub-skills.
5. Define Regulation 38 information set and issue responsibility before PC.
6. Halt if user requests final fire certification without engineer input.

## Inputs required

- Use classification, storeys, occupancy, and evacuation profiles
- Existing fire strategy reports and consultant correspondence
- Approved inspector / LABC comments on fire matters
- Sprinkler and suppression assumptions

## Outputs

- Fire strategy coordination summary (not a substitute for signed fire strategy)
- AD B / BS 9999 / engineered approach decision record
- Regulation 38 handover checklist
- Interface actions for structure, services, and facade

## Halt rules

- Halt on contradictory fire engineer vs Building Control positions — do not merge silently.
- Halt if means-of-escape dimensions are requested without a agreed strategy basis.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [regulation-38-checklist.md](../../references/checklists/regulation-38-checklist.md) — module checklist
