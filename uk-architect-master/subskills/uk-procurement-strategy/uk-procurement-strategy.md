---
name: uk-procurement-strategy
description: >
  Procurement route selection for UK projects: traditional, design and build, management contracting, and NEC4 ECC.
  Use for risk allocation, contract form mapping, and weather/delay treatment by route — not tender execution.
disable-model-invocation: true
user-invocable: true
---

# UK Procurement Strategy

For tender documentation, variations, and contract administration, use `uk-tender-contract-administration`. For cost plans and BoQ, use `uk-cost-consultancy`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Procurement route selection | `uk-procurement-strategy` | — |
| Traditional vs D&B vs management vs NEC4 | `uk-procurement-strategy` | — |
| Risk allocation by route | `uk-procurement-strategy` | — |
| Weather / exceptionally adverse delay by contract | `uk-procurement-strategy` | `uk-tender-contract-administration` for EOT claims |
| Tender issue and CA duties | `uk-procurement-strategy` | `uk-tender-contract-administration` |
| Cost plan and BoQ | `uk-procurement-strategy` | `uk-cost-consultancy` |

## Route comparison (summary)

| Route | Typical contract | Design risk | Programme risk | Best when |
|-------|------------------|-------------|----------------|-----------|
| Traditional | JCT Standard / Intermediate | Architect/employer to tender | Contractor | Design quality priority; employer retains design control |
| Design & Build | JCT D&B 2024 | Contractor (except employer requirements) | Contractor | Single point; employer accepts design transfer |
| Management | JCT MC / CM | Employer via trade packages | Manager + trades | Fast start; complex interfaces |
| NEC4 ECC | Option A–F | Per option (e.g. C target cost) | Shared via compensation events | Collaborative; public sector common |

## Execution protocol

1. Confirm client objectives, risk appetite, programme, and budget certainty.
2. Assess design completeness at intended tender point and employer's appetite for design transfer.
3. Apply route decision guide in [`../../references/uk-procurement-routes-comparison.md`](../../references/uk-procurement-routes-comparison.md).
4. Map selected route to contract form and key risk allocation (design, ground, programme, weather).
5. Reference weather/EOT treatment in [`../../references/uk-weather-eot-by-procurement.md`](../../references/uk-weather-eot-by-procurement.md).
6. Produce route recommendation memo using [`../../references/templates/tender-route-recommendation.md`](../../references/templates/tender-route-recommendation.md).

## Inputs required

- Client brief, budget, programme, and risk appetite
- Design stage at intended tender point
- Public vs private sector (affects NEC4 / OJEU legacy considerations)
- HRB status (may constrain procurement and competency requirements)

## Outputs

- Route recommendation memo with risk allocation table
- Contract form selection note
- Stage-gate outputs for procurement (pre-tender, tender, award)
- Weather/delay clause pointer by selected route

## Halt rules

- Halt route recommendation if client objectives and risk appetite are unknown.
- Do not recommend a contract form without confirming public/private sector constraints.

## Secondary cross-links

- `uk-tender-contract-administration` — tender execution and CA duties
- `uk-cost-consultancy` — cost plans and tender pricing
- `uk-project-management` — delivery plan alignment
- `uk-plan-of-work` — Stage 0–1 procurement decisions

## References

* [uk-procurement-routes-comparison.md](../../references/uk-procurement-routes-comparison.md) — route matrix
* [uk-weather-eot-by-procurement.md](../../references/uk-weather-eot-by-procurement.md) — delay treatment
* [tender-route-recommendation.md](../../references/templates/tender-route-recommendation.md) — output template
* [compliance.md](../../references/compliance.md) — halt rules
