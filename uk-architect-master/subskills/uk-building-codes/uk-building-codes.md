---
name: uk-building-codes
description: >
  Routes UK Building Regulations compliance, Approved Documents, BSA 2022 gateways, HRB dutyholders, and golden-thread
  record-keeping. Use for technical compliance roadmaps, gateway readiness, or Building Control strategy.
disable-model-invocation: true
user-invocable: true
---

# UK Building Codes

For planning policy and LPA submissions, use `uk-spatial-planning` instead. For fire strategy detail, use `uk-fire-life-safety`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Approved Documents, Schedule 1 functional reqs | `uk-building-codes` | — |
| BSA gateways, HRB classification, dutyholders | `uk-building-codes` | `uk-fire-life-safety` for AD B strategy |
| Building Control route and submission packs | `uk-building-codes` | `uk-construction-documentation` for issue packages |
| Planning permission / conditions | `uk-building-codes` | `uk-spatial-planning` |
| Part L/O numeric screens | `uk-building-codes` | `uk-architect-calculator` then `uk-building-sustainability` |

## Execution protocol

1. Confirm jurisdiction and whether the project is HRB (halt if unknown and scope is HRB-sensitive — see `../../references/compliance.md`).
2. Map scope to relevant Parts (A–R) and identify applicable Approved Documents (including national variants).
3. Separate **planning** consent from **Building Regulations** compliance tracks in the response.
4. For HRBs: state gateway stage, dutyholder register, and golden-thread information requirements.
5. Define evidence needed for Building Control (drawings, specs, calculations, third-party certs).
6. Log assumptions; escalate unresolved conflicts to project board with options.

## Inputs required

- Brief, classification (HRB/non-HRB), RIBA stage, and procurement route
- Survey, context, and existing building data for refurbishments
- Consultant strategies (fire, structure, services) where issued
- Building Control body and submission history

## Outputs

- Compliance roadmap by stage with owner and due dates
- Gateway readiness checklist (HRB)
- Issue-ready coordination note for Building Control / BSR interfaces
- Decision log entry per `../../references/templates/stage-decision-log.md`

## Halt rules

- Do not confirm gateway sign-off without named accountable dutyholders.
- Do not assert AD compliance without citing the relevant AD and project-specific analysis status.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [bsa-gateway-checklist.md](../../references/checklists/bsa-gateway-checklist.md) — module checklist
