---
name: uk-certificate-of-compliance
description: >
  Statutory completion certificates (Building Control/BSR), s106 and community infrastructure obligations,
  and landlord compliance packs for UK developments. Use for multi-party completion sign-off evidence.
disable-model-invocation: true
user-invocable: true
---

# UK Certificate of Compliance

For Building Control completion strategy, use `uk-op-submission-strategy`. For contractual PC, use `uk-practical-completion-snagging`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| BC / BSR completion certificate evidence | `uk-certificate-of-compliance` | `uk-op-submission-strategy` for sequencing |
| s106 obligations and community infrastructure | `uk-certificate-of-compliance` | `uk-spatial-planning` for condition interpretation |
| Landlord compliance packs (commercial) | `uk-certificate-of-compliance` | `uk-lease-compliance` for lease terms |
| Infrastructure dedication / adoption | `uk-certificate-of-compliance` | — |
| Contractual PC certificate | `uk-certificate-of-compliance` | `uk-practical-completion-snagging` |

## What completion certificates mean (UK)

- **Building Control completion certificate** — confirms regulated works comply; enables lawful occupation (with FSO duties).
- **BSR Gateway 3 (HRB)** — separate from BC certificate; confirms golden thread and safety case.
- **s106 compliance** — planning obligations (affordable housing, highways, open space) may block practical completion of planning conditions.
- **Landlord packs** — tenant fit-out and asset handover evidence; contractual not statutory.

## Execution protocol

1. Map all completion certificates required (BC, BSR, s106, adoption agreements, landlord).
2. Do not conflate statutory BC completion with contractual PC or planning condition discharge.
3. Build readiness matrix: authority → prerequisite → owner → status.
4. For s106: track trigger points, bond releases, and adoption agreements.
5. For infrastructure handover: coordinate highways, drainage, and open space adoption.
6. Document risk hotspots (outstanding conditions, bond calls, adoption delays).

## Inputs required

- Planning permission and s106 agreement
- BC approval and inspection history
- Adoption agreements and bond status
- Lease/landlord requirements (commercial)

## Outputs

- Completion certificate readiness matrix
- s106 compliance tracker with trigger dates
- Infrastructure handover schedule
- Landlord compliance pack index (where applicable)

## Halt rules

- BC completion certificate is separate from contractual PC — do not conflate.
- s106 obligations may cap occupation — never assume planning alone governs if bonds outstanding.

## Secondary cross-links

- `uk-op-submission-strategy` — BC completion sequencing
- `uk-spatial-planning` — planning conditions and s106
- `uk-lease-compliance` — landlord/tenant obligations
- `uk-practical-completion-snagging` — contractual PC

## References

* [bc-completion-readiness-matrix.md](../../references/templates/bc-completion-readiness-matrix.md) — readiness tracker
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
