import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP = {
    "uk-building-codes",
    "uk-fire-life-safety",
    "uk-spatial-planning",
    "uk-tender-contract-administration",
    "uk-practical-completion-snagging",
    "uk-building-sustainability",
    "uk-architect-calculator",
    "uk-architect-foundations",
    "uk-minor-works",
    "uk-plan-of-work",
    "uk-deliverables-workstages",
    "uk-procurement-strategy",
    "uk-project-management",
    "uk-cost-consultancy",
    "uk-construction-programme",
    "uk-construction-health-safety",
    "uk-site-establishment",
    "uk-op-submission-strategy",
    "uk-fsd-licensing-compliance",
    "uk-certificate-of-compliance",
}

USE_INSTEAD = {
    "uk-accessibility-design": [
        ("Building Regulations general routing", "uk-building-codes"),
        ("Planning merit only", "uk-spatial-planning"),
    ],
    "uk-acoustic-design": [
        ("Planning environmental noise", "uk-spatial-planning"),
        ("Building Control completion", "uk-building-codes"),
    ],
    "uk-alterations-additions": [
        ("PD small works", "uk-minor-works"),
        ("Unlawful works", "uk-unauthorised-building-works"),
    ],
    "uk-building-envelope": [
        ("Part L/O strategy", "uk-building-sustainability"),
        ("Fire facade strategy", "uk-fire-life-safety"),
    ],
    "uk-building-programming": [("Planning use class", "uk-spatial-planning")],
    "uk-building-services": [("Part L carbon strategy", "uk-building-sustainability")],
    "uk-building-typology": [("Concept options", "uk-concept-design")],
    "uk-cashflow-debt-recovery": [
        ("Fee proposal", "uk-fee-proposal-strategy"),
        ("Contract payment", "uk-tender-contract-administration"),
    ],
    "uk-concept-design": [("Technical packages", "uk-construction-documentation")],
    "uk-consent-scheduling": [("Planning policy", "uk-spatial-planning")],
    "uk-construction-documentation": [("Building Control strategy", "uk-building-codes")],
    "uk-daylighting-design": [("Planning sunlight/daylight", "uk-spatial-planning")],
    "uk-design-theory": [("Statutory compliance", "uk-building-codes")],
    "uk-fee-proposal-strategy": [("Contract admin", "uk-tender-contract-administration")],
    "uk-heritage-conservation": [
        ("Planning application", "uk-spatial-planning"),
        ("PD rights", "uk-minor-works"),
    ],
    "uk-lease-compliance": [("Contract law", "uk-tender-contract-administration")],
    "uk-material-selection": [("Envelope thermal", "uk-building-envelope")],
    "uk-mic-dfma": [("Site quality", "uk-site-supervision")],
    "uk-professional-indemnity": [("Contract liability", "uk-tender-contract-administration")],
    "uk-project-resource-levelling": [("Fee/cashflow", "uk-fee-proposal-strategy")],
    "uk-site-supervision": [("Contract variations", "uk-tender-contract-administration")],
    "uk-structural-systems": [("Building Regs coordination", "uk-building-codes")],
    "uk-unauthorised-building-works": [
        ("PD eligibility", "uk-minor-works"),
        ("Planning enforcement", "uk-spatial-planning"),
    ],
}


def main():
    with open(os.path.join(BASE, "skills.json"), encoding="utf-8") as f:
        skills = json.load(f)["skills"]

    sub_base = os.path.join(BASE, "subskills")
    for s in skills:
        sid = s["id"]
        if sid in SKIP:
            continue
        title = s["title"]
        load_when = s["load_when"]
        rows = USE_INSTEAD.get(sid, [("General regulations", "uk-building-codes")])
        table = "\n".join(f"| {q} | `{sid}` | `{alt}` |" for q, alt in rows[:4])
        body = f"""---
name: {sid}
description: >
  {load_when}. Use when the user asks about topics in this module scope for UK architectural practice.
disable-model-invocation: true
user-invocable: true
---

# {title}

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
{table}

## Execution protocol

1. Confirm project context per master intake checklist ([`../../references/operational.md`](../../references/operational.md)).
2. Apply module scope: {load_when}
3. Cross-check golden-thread fields for regulatory answers (HRB, RIBA stage, dutyholders).
4. Document assumptions; escalate conflicts per [`../../references/compliance.md`](../../references/compliance.md).
5. Produce outputs using [`../../references/templates/stage-decision-log.md`](../../references/templates/stage-decision-log.md) where a formal record is needed.

## Inputs required

- Brief, site, stage, and appointment scope
- Relevant consultant inputs for this discipline
- Applicable statutory or contract documents referenced by the user

## Outputs

- Discipline-specific coordination note and action list
- Risks, programme impact, and next-step owners

## Halt rules

- Halt when jurisdiction, HRB status, or appointment scope is unknown and material to the answer.
- Do not provide formal legal, structural, or fire certification conclusions.

## References

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [stage-decision-log.md](../../references/templates/stage-decision-log.md) — output structure
"""
        path = os.path.join(sub_base, sid, f"{sid}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        print("updated", sid)


if __name__ == "__main__":
    main()
