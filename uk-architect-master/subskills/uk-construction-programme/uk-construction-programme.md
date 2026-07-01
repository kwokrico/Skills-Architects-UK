---
name: uk-construction-programme
description: >
  UK construction sequencing: swimlanes, fast-tracking, standard floor cycles, MMC interfaces, look-ahead programmes,
  and sectional completion. Use for site programme logic — illustrative durations only.
disable-model-invocation: true
user-invocable: true
---

# UK Construction Programme

For project delivery plan and client reporting, use `uk-project-management`. For site inspections and quality, use `uk-site-supervision`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Construction sequence and swimlanes | `uk-construction-programme` | — |
| Fast-tracking and trade stacking | `uk-construction-programme` | — |
| Standard floor cycle (RC frame, CLT, steel) | `uk-construction-programme` | — |
| 4-week look-ahead template | `uk-construction-programme` | — |
| MMC / modular delivery interfaces | `uk-construction-programme` | `uk-mic-dfma` |
| Sectional completion programme | `uk-construction-programme` | `uk-tender-contract-administration` for contractual PC |
| Site mobilisation / hoarding | `uk-construction-programme` | `uk-site-establishment` |

## Execution protocol

1. Confirm building typology, structural system, and procurement route.
2. Select archetype from [`../../references/uk-construction-sequence-swimlanes.md`](../../references/uk-construction-sequence-swimlanes.md).
3. Define hold points (e.g. frame completion, watertight, first fix, commissioning).
4. Identify architect/PM early-freeze packages that gate contractor sequence.
5. Produce narrative sequence with interface rules between trades.
6. Issue look-ahead using [`../../references/templates/construction-look-ahead.md`](../../references/templates/construction-look-ahead.md).

## Inputs required

- Structural system and facade type
- MMC/offsite scope if applicable
- Contract programme (baseline) and current progress
- Key interfaces (services, fire stopping, commissioning)

## Outputs

- Construction sequence narrative with swimlane diagram
- Hold-point register with approval requirements
- 4-week look-ahead programme
- Interface rules memo (architect freeze points)

## Halt rules

- Durations are illustrative only — project-specific programme required for binding commitments.
- Do not advise concealment of works ahead of inspection hold points.

## Secondary cross-links

- `uk-site-establishment` — mobilisation before main works
- `uk-site-supervision` — inspection witness at hold points
- `uk-mic-dfma` — modular delivery sequencing
- `uk-project-management` — master programme integration

## References

* [uk-construction-sequence-swimlanes.md](../../references/uk-construction-sequence-swimlanes.md) — archetype sequences
* [construction-look-ahead.md](../../references/templates/construction-look-ahead.md) — look-ahead template
* [compliance.md](../../references/compliance.md) — halt rules
