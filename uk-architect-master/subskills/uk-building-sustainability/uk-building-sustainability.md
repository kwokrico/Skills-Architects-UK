---
name: uk-building-sustainability
description: >
  Guides Part L, Part O, embodied carbon, and rating tools (BREEAM, WELL, LEED) for UK projects. Use for sustainability
  strategy, overheating risk, and energy compliance pathways — not final SAP/SBEM certification.
disable-model-invocation: true
user-invocable: true
---

# UK Building Sustainability

For statutory Building Regulations routing, use `uk-building-codes`. For calculator screens, use `uk-architect-calculator`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Part L strategy, TER/DER, carbon | `uk-building-sustainability` | `uk-architect-calculator` for screens |
| Part O overheating | `uk-building-sustainability` | `uk-architect-calculator` (`part_o_screen`) |
| BREEAM / WELL / LEED targets | `uk-building-sustainability` | — |
| Facade U-values and thermal bridges | `uk-building-sustainability` | `uk-building-envelope` |
| Building Regulations gateways only | `uk-building-sustainability` | `uk-building-codes` |

## Execution protocol

1. Confirm dwelling vs non-domestic route (SAP vs SBEM) and notional building baseline.
2. Run early screens via `run_uk_calculator` where data exists; treat as advisory only.
3. Integrate facade, services, and renewables assumptions into a single narrative.
4. Map rating tool credits only when target and assessor are confirmed.
5. Document embodied carbon scope (RICS/ICE methodology) when requested.
6. Escalate if Part O risk is High — require dynamic analysis or approved simplified method.

## Inputs required

- Energy modelling outputs (if any), target U-values, glazing ratios
- Orientation, shading, ventilation strategy for Part O
- Rating tool version and target score

## Outputs

- Sustainability strategy summary by RIBA stage
- Part L / Part O compliance pathway (high level)
- Consultant coordination list (energy, MEP, facade)
- Risk register for rating tool shortfalls

## Halt rules

- Halt on claimed Part L sign-off without issued SAP/SBEM and BR PD coordination.
- Halt if Part O High risk is ignored in design recommendations.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [part-l-o-pathway.md](../../references/checklists/part-l-o-pathway.md) — module checklist
