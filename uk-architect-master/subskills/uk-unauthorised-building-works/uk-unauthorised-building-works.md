---
name: uk-unauthorised-building-works
description: >
  Regularisation, enforcement, retrospective approval, or unlawful works remediation. Use when the user asks about topics in this module scope for UK architectural practice.
disable-model-invocation: true
user-invocable: true
---

# UK Unauthorised Building Works

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| PD eligibility | `uk-unauthorised-building-works` | `uk-minor-works` |
| Planning enforcement | `uk-unauthorised-building-works` | `uk-spatial-planning` |

## Execution protocol

1. Confirm project context per master intake checklist (`../../references/operational.md`).
2. Apply module scope: Regularisation, enforcement, retrospective approval, or unlawful works remediation
3. Cross-check golden-thread fields for regulatory answers (HRB, RIBA stage, dutyholders).
4. Document assumptions; escalate conflicts per `../../references/compliance.md`.
5. Produce outputs using `../../references/templates/stage-decision-log.md` where a formal record is needed.

## Inputs required

- Brief, site, stage, and appointment scope
- Relevant consultant inputs for this discipline
- Applicable statutory or contract documents referenced by the user

## Outputs

- Discipline-specific coordination note and action list
- Risks, programme impact, and next-step owners

## Halt rules

- Halt when jurisdiction, HRB status, or appointment scope is unknown and material to the answer.
- Do not provide formal legal, structural, or fire certification conclusions.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [stage-decision-log.md](../../references/templates/stage-decision-log.md) — output structure
