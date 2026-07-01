---
name: uk-construction-health-safety
description: >
  UK construction health and safety: CDM 2015 duties, HSE liaison, Principal Designer/Contractor roles, H&S file,
  risk assessments, and accident reporting. Use for site H&S — not building fire code strategy.
disable-model-invocation: true
user-invocable: true
---

# UK Construction Health and Safety

For fire strategy and AD B compliance, use `uk-fire-life-safety`. For site quality inspections, use `uk-site-supervision`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| CDM 2015 duties and appointments | `uk-construction-health-safety` | — |
| Principal Designer / Principal Contractor | `uk-construction-health-safety` | — |
| H&S file content and handover | `uk-construction-health-safety` | — |
| Construction phase plan, risk assessments | `uk-construction-health-safety` | — |
| HSE liaison, F10 notification, accident reporting | `uk-construction-health-safety` | — |
| Fire strategy / compartmentation | `uk-construction-health-safety` | `uk-fire-life-safety` |
| Building Regulations Principal Designer (BSA) | `uk-construction-health-safety` | `uk-building-codes` |

## Execution protocol

1. Confirm project notifiable status under CDM 2015 (halt if unknown for duty allocation).
2. Distinguish CDM Principal Designer from Building Regulations Principal Designer (BSA) — do not merge duties.
3. Apply pre-construction checklist in [`../../references/checklists/cdm-preconstruction-checklist.md`](../../references/checklists/cdm-preconstruction-checklist.md).
4. Coordinate design-stage hazard elimination and reduction; document residual risks for H&S file.
5. Define construction phase plan requirements and Principal Contractor interfaces.
6. Establish accident reporting route (RIDDOR) and site inspection cadence.

## Inputs required

- Project classification, notifiability, and dutyholder appointments
- Design information and residual risk register
- Construction phase plan (when on site)
- F10 notification status

## Outputs

- CDM dutyholder map with appointment status
- Pre-construction information pack outline
- H&S file content schedule
- Risk assessment summary and mitigation actions

## Halt rules

- Not building fire code — route fire strategy questions to `uk-fire-life-safety`.
- Halt if CDM notifiability is unknown when advising on Principal Designer/Contractor duties.

## Secondary cross-links

- `uk-site-establishment` — mobilisation H&S interfaces
- `uk-site-supervision` — site inspections and NCRs
- `uk-project-management` — CDM coordination in delivery plan
- `uk-building-codes` — BSA Principal Designer (separate from CDM PD)

## References

* [cdm-preconstruction-checklist.md](../../references/checklists/cdm-preconstruction-checklist.md) — CDM gateway
* [compliance.md](../../references/compliance.md) — halt rules and PD distinction
* [domain_terms.json](../../references/domain_terms.json) — CDM vocabulary
