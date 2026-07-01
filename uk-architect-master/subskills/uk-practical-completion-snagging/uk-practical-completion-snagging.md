---
name: uk-practical-completion-snagging
description: >
  Supports practical completion, snagging, handover, defects period management, and Regulation 38 coordination at closeout.
  Use when the user asks about PC certificates, retention, or end-of-construction governance.
disable-model-invocation: true
user-invocable: true
---

# UK Practical Completion and Snagging

For contract certification mechanics, use `uk-tender-contract-administration`. For fire information content, use `uk-fire-life-safety`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Practical completion, snagging lists | `uk-practical-completion-snagging` | — |
| Regulation 38 at handover | `uk-practical-completion-snagging` | `uk-fire-life-safety` |
| Certificate of making good defects | `uk-practical-completion-snagging` | `uk-tender-contract-administration` |
| Building Control completion | `uk-practical-completion-snagging` | `uk-building-codes` |
| OP / asset handover packs | `uk-practical-completion-snagging` | `uk-op-submission-strategy` |

## Execution protocol

1. Confirm contract definition of practical completion and list outstanding works.
2. Run snagging survey with location references and priority (safety, function, cosmetic).
3. Verify statutory completions (Building Control, fire, commissioning) parallel to contractual PC.
4. Align Regulation 38 issue with responsible person identification.
5. Plan defects period monitoring and retention release triggers.
6. Document PC date implications for LDs, insurance, and occupation.

## Inputs required

- Contract PC clauses and snagging protocol
- Inspection records, NCRs, and outstanding RFIs
- Fire and commissioning certificates status

## Outputs

- Snagging schedule ([`../../references/templates/snagging-schedule.md`](../../references/templates/snagging-schedule.md))
- PC readiness summary with blockers
- Handover information register
- Aftercare / defects period action plan

## Halt rules

- Halt PC recommendation if life-safety commissioning or Regulation 38 gaps remain unresolved.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [snagging-schedule.md](../../references/templates/snagging-schedule.md) — snagging output structure
* [regulation-38-checklist.md](../../references/checklists/regulation-38-checklist.md) — fire handover prompts
