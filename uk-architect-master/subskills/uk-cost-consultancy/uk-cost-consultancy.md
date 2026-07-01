---
name: uk-cost-consultancy
description: >
  UK quantity surveying scope: NRM cost plans, BoQ, tender pricing, interim valuations, variations, claims support,
  and final account. Use for commercial cost advice — not architect fee proposals.
disable-model-invocation: true
user-invocable: true
---

# UK Cost Consultancy

For architect fee proposals, use `uk-fee-proposal-strategy`. For contract certification and variations, use `uk-tender-contract-administration`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Feasibility budget and benchmarking | `uk-cost-consultancy` | — |
| Cost plans by RIBA stage (NRM1) | `uk-cost-consultancy` | — |
| BoQ and tender pricing (NRM2) | `uk-cost-consultancy` | — |
| Tender evaluation and comparison | `uk-cost-consultancy` | `uk-tender-contract-administration` for contract award |
| Interim valuations and variations | `uk-cost-consultancy` | `uk-tender-contract-administration` for certification |
| Claims support and final account | `uk-cost-consultancy` | — |
| Architect fee proposal | `uk-cost-consultancy` | `uk-fee-proposal-strategy` |
| Procurement route selection | `uk-cost-consultancy` | `uk-procurement-strategy` |

## Execution protocol

1. Confirm measurement basis (GIA, NIA, IPMS) and cost plan stage (0–4 per NRM1).
2. Establish elemental breakdown aligned to NRM1/NRM2 structure.
3. For design-stage control: compare cost plan to budget; identify variances and VM options.
4. For tender: coordinate BoQ with specification; support tender analysis and qualification review.
5. For post-contract: assess variation costs, support interim valuations, maintain cost report.
6. Cross-check certification interface with contract administrator — QS advises, CA certifies.

## Inputs required

- Project brief, area schedule, and specification level
- Cost plan stage and budget target
- Tender returns or valuation documents
- Contract form and pricing document (lump sum, remeasure, target cost)

## Outputs

- Cost plan by stage with elemental breakdown
- Tender comparison report with qualifications noted
- Variation cost estimate with supporting breakdown
- Cost report (forecast, committed, contingency, risk allowance)

## Halt rules

- Halt certification advice — cross-check with contract administrator appointment.
- Do not provide binding tender evaluation without complete returns and clarifications log.

## Secondary cross-links

- `uk-tender-contract-administration` — certification and contract mechanisms
- `uk-procurement-strategy` — route affects cost certainty and risk allowance
- `uk-deliverables-workstages` — cost report issue packs
- `uk-building-programming` — area schedules and benchmarks

## References

* [deliverables.md](../../references/templates/deliverables.md) — commercial templates
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — NRM and QS vocabulary
