---
name: uk-op-submission-strategy
description: >
  Building Control completion certificate strategy, BSR Gateway 3 evidence, partial occupation rules, and record
  drawings for UK projects. Use when planning statutory completion — not contractual practical completion.
disable-model-invocation: true
user-invocable: true
---

# UK Building Control Completion Strategy

For contractual PC and snagging, use `uk-practical-completion-snagging`. For fire commissioning evidence, use `uk-fsd-licensing-compliance`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Building Control completion certificate | `uk-op-submission-strategy` | — |
| BSR Gateway 3 evidence and readiness | `uk-op-submission-strategy` | `uk-building-codes` for dutyholder detail |
| Partial occupation / sectional completion | `uk-op-submission-strategy` | `uk-tender-contract-administration` for contract PC |
| Record drawings and as-built submission | `uk-op-submission-strategy` | `uk-construction-documentation` |
| Contractual PC and snagging | `uk-op-submission-strategy` | `uk-practical-completion-snagging` |
| Fire commissioning / FSO evidence | `uk-op-submission-strategy` | `uk-fsd-licensing-compliance` |

## Completion authority sequence

| Step | Authority / party | Prerequisite | Owner |
|------|-------------------|--------------|-------|
| 1 | Building Control / BSR | All regulated works complete; final inspection passed | Principal Contractor + BC body |
| 2 | BSR Gateway 3 (HRB) | Golden thread, competency evidence, change control log | Accountable Person |
| 3 | Fire authority / FSO | Commissioning certificates, fire strategy as-built | Responsible Person + fire engineer |
| 4 | Regulation 38 | Fire safety information pack to responsible person | Principal Designer / architect |
| 5 | Contractual PC | Snagging complete per contract definition | Contract Administrator |

## Execution protocol

1. Confirm HRB status, BC body (LABC / approved inspector / BSR), and jurisdiction.
2. Assemble readiness matrix per [`../../references/templates/bc-completion-readiness-matrix.md`](../../references/templates/bc-completion-readiness-matrix.md).
3. Coordinate final inspection strategy: witness points, outstanding conditions, minor deviations.
4. For HRB: verify Gateway 3 evidence against BSA requirements — do not conflate with contractual PC.
5. Plan record drawing submission and as-built information for golden thread (HRB).
6. Screen for unauthorised works — cross-check `uk-unauthorised-building-works` if regularisation needed.

## Inputs required

- Approved drawings and specification vs as-built status
- BC inspection history and outstanding conditions
- Gateway 3 checklist (HRB)
- Commissioning certificates and test records
- Regulation 38 pack status

## Outputs

- BC completion readiness matrix with owner and status
- Authority coordination tracker
- Record drawing index
- 8-week readiness programme (inspections, tests, submissions)

## Halt rules

- Halt occupation/completion confirmation without inspection evidence.
- Do not guarantee completion outcome without site verification.
- Unauthorised works may block completion — cross-check `uk-unauthorised-building-works`.

## Secondary cross-links

- `uk-fsd-licensing-compliance` — fire commissioning chain
- `uk-practical-completion-snagging` — contractual PC
- `uk-certificate-of-compliance` — s106 and infrastructure handover
- `uk-site-supervision` — inspection witness records

## References

* [bc-completion-readiness-matrix.md](../../references/templates/bc-completion-readiness-matrix.md) — readiness tracker
* [bsa-gateway-checklist.md](../../references/checklists/bsa-gateway-checklist.md) — Gateway 3 (HRB)
* [regulation-38-checklist.md](../../references/checklists/regulation-38-checklist.md) — fire information handover
* [compliance.md](../../references/compliance.md) — halt rules
