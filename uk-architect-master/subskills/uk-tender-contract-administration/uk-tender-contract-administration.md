---
name: uk-tender-contract-administration
description: >
  Advises on UK tender documentation and contract administration under JCT 2024, NEC4, and FIDIC.
  Use for variations, extensions of time, liquidated damages, claims, and contractor correspondence — not route selection or legal determination.
disable-model-invocation: true
user-invocable: true
---

# UK Tender and Contract Administration

For procurement route selection, use `uk-procurement-strategy`. For fee proposals, use `uk-fee-proposal-strategy`. For site quality and NCRs, use `uk-site-supervision`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| JCT / NEC4 / FIDIC administration | `uk-tender-contract-administration` | — |
| Variations, EOT, LDs, loss/expense | `uk-tender-contract-administration` | — |
| Tender documents, tender queries, assessment | `uk-tender-contract-administration` | — |
| Post-contract CA duties, certificates | `uk-tender-contract-administration` | — |
| Procurement route selection | `uk-tender-contract-administration` | `uk-procurement-strategy` |
| Cost plan, BoQ, valuations | `uk-tender-contract-administration` | `uk-cost-consultancy` |
| Architect fee and appointment | `uk-tender-contract-administration` | `uk-fee-proposal-strategy` |
| Snagging and PC certificates | `uk-tender-contract-administration` | `uk-practical-completion-snagging` |

## Execution protocol

1. Confirm procurement route and contract form are already selected — if not, route to `uk-procurement-strategy`.
2. Identify contract form, edition, and amendment schedule — halt if unknown for binding advice.
3. Map user question to contract mechanism (instruction, variation, compensation event, etc.).
4. Cite relevant clause **by name/number** only when contract is confirmed; otherwise describe generic JCT/NEC principles.
5. Separate architect certifier duties from employer agent duties per appointment.
6. Recommend record-keeping: notices, contemporary records, and without-prejudice boundaries.
7. Flag when quantity surveyor, lawyer, or adjudicator input is required.

## Inputs required

- Signed contract, amendments, and appointment documents
- Programme (contract and actual), notices, and correspondence
- Valuations, payment notices, and defect lists

## Outputs

- Contract position summary (advisory)
- Notice and evidence checklist
- Recommended next steps with programme/commercial impact
- Use `../../references/templates/compliance-memo.md` for formal issue records

## Halt rules

- Halt on formal legal dispute strategy — refer to legal counsel.
- Do not certify or determine extensions without stated contract grounds and evidence list.
- Halt route-selection questions — defer to `uk-procurement-strategy`.

## Secondary cross-links

- `uk-procurement-strategy` — route and contract form selection
- `uk-cost-consultancy` — BoQ, valuations, final account
- `uk-practical-completion-snagging` — PC and defects period
- `uk-weather-eot-by-procurement` — see `../../references/uk-weather-eot-by-procurement.md` for delay treatment by route

## References

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [compliance-memo.md](../../references/templates/compliance-memo.md) — formal issue records
* [uk-weather-eot-by-procurement.md](../../references/uk-weather-eot-by-procurement.md) — weather/delay by contract
