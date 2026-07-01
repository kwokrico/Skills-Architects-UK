---
name: uk-site-establishment
description: >
  UK pre-construction mobilisation: Party Wall Act, Chapter 8 hoarding, utility diversions, TfL TMP, and
  telecom/utility protection (Openreach, DIAN). Use for site-start readiness before main works.
disable-model-invocation: true
user-invocable: true
---

# UK Site Establishment

For consent prerequisites and programming, use `uk-consent-scheduling`. For CDM H&S strategy, use `uk-construction-health-safety`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site mobilisation and readiness gate | `uk-site-establishment` | — |
| Party Wall Act notices and awards | `uk-site-establishment` | — |
| Hoarding and Chapter 8 (Safer Streets) | `uk-site-establishment` | — |
| Utility diversions and undertaker liaison | `uk-site-establishment` | — |
| Traffic management (TfL TMP, highways) | `uk-site-establishment` | — |
| Telecom protection (Openreach, DIAN) | `uk-site-establishment` | — |
| CDM H&S file / Principal Designer | `uk-site-establishment` | `uk-construction-health-safety` |
| Construction sequencing | `uk-site-establishment` | `uk-construction-programme` |

## Pre-construction readiness gate

Main works must not start until:

1. Building Control approval / commencement conditions met (`uk-consent-scheduling`).
2. Party Wall notices served and awards in place where applicable.
3. Hoarding permit and Chapter 8 traffic management approved.
4. Utility diversions and protection plans agreed with undertakers.
5. Site establishment checklist complete per [`../../references/uk-site-establishment-checklist.md`](../../references/uk-site-establishment-checklist.md).

## Traffic coordination (merged)

- **Planning TIA** vs **construction TMP** — do not conflate; planning studies inform design, TMP governs site works.
- TfL Street Works and highway authority approvals for London and trunk roads.
- Bus stop suspensions, lane closures, and pedestrian diversion routes.
- Coordinate hoarding design with traffic management drawings.

## Telecom and utility coordination (merged)

- Openreach and utility DIAN (Dial Before You Dig) before excavation.
- Licensed works require approved contractors — verify undertaker list.
- Fibre/cable protection during piling, excavation, and temporary works.
- Coordinate diversion sequencing with main utility connections.

## Execution protocol

1. Confirm consent status and BC commencement conditions.
2. Screen Party Wall Act applicability (adjacent owners, excavations within 3 m / 6 m).
3. Develop hoarding brief aligned to local authority and Chapter 8 requirements.
4. Liaise with utility undertakers; issue protection and diversion programmes.
5. Engage traffic consultant for TMP if highway interface or TfL red route.
6. Assemble pre-construction information (PCI) pack index for contractor handover.

## Inputs required

- Site boundaries, adjacent properties, and highway classification
- Approved hoarding and traffic drawings
- Utility records and undertaker correspondence
- Consent and BC commencement status

## Outputs

- Site establishment checklist with pass/fail status
- Hoarding design brief and permit tracker
- Utility diversion and protection programme
- TMP outline and highways submission tracker
- PCI pack assembly index

## Halt rules

- Cannot commence main works without valid Building Control approval / commencement conditions.
- Licensed telecom/utility works require approved contractors — verify before excavation.

## Secondary cross-links

- `uk-consent-scheduling` — consent prerequisites
- `uk-construction-health-safety` — CDM PCI and construction phase plan
- `uk-construction-programme` — mobilisation to main works sequence
- `uk-spatial-planning` — planning-condition traffic studies (TIA)

## References

* [uk-site-establishment-checklist.md](../../references/uk-site-establishment-checklist.md) — mobilisation gate
* [compliance.md](../../references/compliance.md) — halt rules
* [domain_terms.json](../../references/domain_terms.json) — Party Wall, TfL, utility vocabulary
