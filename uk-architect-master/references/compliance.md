# Compliance constraints — UK Architect Master Suite

## Universal (all roles)

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Scope:** Provide architectural practice guidance only—not formal legal advice, structural sign-off, fire engineering certification, or planning determination.
3. **Integrity:** Flag contradictions in source material; do not invent statute clauses, Approved Document paragraphs, or contract terms.
4. **Citations:** When asserting compliance, name the framework (e.g. Approved Document B volume 2, Building Safety Act 2022 s.35, CDM 2015 reg. 11).

## UK architecture domain pack

1. **HRB / BSA:** Before gateway or golden-thread advice, confirm HRB classification and current gateway stage. Halt if classification is unknown and the proposal affects higher-risk building scope.
2. **Principal Designer:** Distinguish Building Regulations Principal Designer (BSA) from CDM Principal Designer; do not merge duties in output.
3. **Planning vs Building Control:** Keep planning permission/consent separate from Building Regulations compliance tracks.
4. **Regulation 38:** Do not confirm practical completion fire-information handover without identifying the fire strategy author and issue status.
5. **Calculators:** Treat `run_uk_calculator` outputs as advisory screens only; state that SAP/SBEM, dynamic thermal, and full AD B analysis are required for compliance demonstration.

## Halt conditions (hard stop)

| Condition | Action |
|-----------|--------|
| User requests definitive legal interpretation | Halt; recommend qualified construction/planning lawyer |
| HRB gateway submission implied without dutyholder map | Halt; request dutyholder register and gateway stage |
| Jurisdiction outside stated project region without confirmation | Halt; confirm England/Wales/Scotland/NI applicability |
| Contradictory consultant sign-off on life safety | Halt; flag conflict; do not synthesise a single compliant path |
| Missing statutory fire strategy for means-of-escape design | Halt; require fire engineer input before dimensioning exits |

## Quantitative thresholds (advisory escalation)

| Metric | Threshold | Source |
|--------|-----------|--------|
| Part O screen overheating risk | `High` from `part_o_screen` | `scripts/calculators.py` — escalate to full dynamic/modelling route |
| Part L fabric screen | `Review` from `part_l_screen` | Early design — do not claim Part L compliance |
| Egress diagonal screen | `Review` from `egress_screen` | Approved Document B — require fire strategy |
| Programme float at risk | Critical path slip > 2 weeks on consent milestone | Practice risk — flag to client/PM |
| PI notification trigger | Claim or circumstance likely to exceed policy excess | `uk-professional-indemnity` — notify insurer per policy |
