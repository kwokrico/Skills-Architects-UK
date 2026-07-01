---
name: uk-spatial-planning
description: >
  Guides UK planning policy, development management, applications, conditions, and s106 obligations. Use for LPA
  strategy, submission quality, and planning condition discharge — not Building Regulations compliance.
disable-model-invocation: true
user-invocable: true
---

# UK Spatial Planning

For Building Regulations and Approved Documents, use `uk-building-codes`. For listed buildings and conservation, add `uk-heritage-conservation`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Planning applications, policy tests, s106 | `uk-spatial-planning` | — |
| Permitted development / GPDO | `uk-spatial-planning` | `uk-minor-works` for small works focus |
| Listed building / conservation area | `uk-spatial-planning` | `uk-heritage-conservation` |
| Building Control / AD compliance | `uk-spatial-planning` | `uk-building-codes` |
| Consent programme sequencing | `uk-spatial-planning` | `uk-consent-scheduling` |

## Execution protocol

1. Confirm LPA, plan designation (e.g. allocation, constraints), and application type.
2. Separate **planning merit** from **technical building compliance** in the narrative.
3. Map policy tests (NPPF / local plan) and material considerations; list evidence gaps.
4. Review draft drawings/statements for consistency with fire, heritage, and transport consultee risks.
5. Track conditions and s106 triggers with discharge owners and dates.
6. Halt if user seeks a binding planning decision — only LPA can determine applications.

## Inputs required

- Site location, red line boundary, and proposal description
- Pre-app or officer feedback, consultee responses
- Design & Access Statement / planning statement status
- Community and stakeholder consultation outcomes where relevant

## Outputs

- Planning strategy memo with risks and programme
- Submission readiness checklist
- Condition discharge tracker (initial)
- Consultee coordination actions

## Halt rules

- Halt if heritage designation is unconfirmed and works affect historic fabric — route via `uk-heritage-conservation`.
- Do not state planning permission is guaranteed.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [planning-submission-checklist.md](../../references/checklists/planning-submission-checklist.md) — module checklist
