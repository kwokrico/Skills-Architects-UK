---
name: uk-architect-calculator
description: >
  Documents advisory UK design calculators (Part L fabric, Part O overheating screen, IPMS conversion, egress distance).
  Use when calling run_uk_calculator or validating calc_type JSON payloads.
disable-model-invocation: true
user-invocable: true
---

# UK Architect Calculator

For sustainability strategy narrative, use `uk-building-sustainability`. For fire strategy sign-off, use `uk-fire-life-safety`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| run_uk_calculator / calc_type payloads | `uk-architect-calculator` | — |
| Part L / Part O compliance sign-off | `uk-architect-calculator` | `uk-building-sustainability` |
| Full means of escape design | `uk-architect-calculator` | `uk-fire-life-safety` |

## Execution protocol

1. Select `calc_type` and build `data` JSON per reference below.
2. Call `run_uk_calculator` (or legacy `run_hk_calculator` alias).
3. Present results with calculator disclaimer verbatim.
4. Map `Review` or `High` outcomes to escalation in `../../references/compliance.md`.

## Calculator payloads

See `../../references/checklists/calculator-io.md` for required fields.

## Halt rules

- Do not present calculator output as statutory compliance confirmation.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [calculator-io.md](../../references/checklists/calculator-io.md) — module checklist
