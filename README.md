# UK Architect Skills

### A Tier 2 professional skill suite for UK architectural practice

`Skills-Architect-UK` is a Tier 2 professional skill suite built around one master router (`uk-architect-master`) and 35 specialist sub-skills. It supports England/Wales/Scotland/NI workflows: Building Regulations and Approved Documents, Building Safety Act 2022, planning, fire and life safety, sustainability (Part L/O), procurement (JCT 2024 / NEC4), and practical completion.

---

## Contents

- [Quick Start](#quick-start)
- [What You Get](#what-you-get)
- [How It Works](#how-it-works)
- [Folder Structure](#folder-structure)
- [Calculators](#calculators)
- [Verification](#verification)
- [Standards and Frameworks](#standards-and-frameworks)

---

## Quick Start

### Claude Desktop

1. Copy or clone this repository; use the `uk-architect-master/` package as the skill root.
2. Keep the package structure unchanged (see [Folder Structure](#folder-structure)).
3. Load the skill from the `uk-architect-master` directory.
4. Ask a UK architecture question (examples below).

### Plugin directory launch

```bash
claude --plugin-dir "/path/to/Skills-Architect-UK/uk-architect-master"
```

### Cursor (optional)

See [AGENTS.md](AGENTS.md) for activation in Cursor workspaces.

---

## What You Get

- **1 master router:** `uk-architect-master` in `uk-architect-master/SKILL.md`
- **35 sub-skills** across compliance, design, engineering, commercial, and handover
- **Compliance layer:** `references/config.json`, `references/compliance.md`, `references/operational.md`, `references/domain_terms.json`
- **Registry:** `skills.json` (single source of truth for dispatcher IDs)
- **Templates:** stage decision log, compliance memo, snagging schedule under `references/templates/`
- **Calculators:** Part L/O screens, IPMS conversion, egress advisory (`scripts/calculators.py`)

---

## How It Works

1. **Quick answer first** — Master quick reference (HRB, gateways, RIBA, planning vs BR).
2. **Route to a specialist** — `load_sub_skill` with an ID from `skills.json` / Section 5 of `SKILL.md`.
3. **Run calculators** — `run_uk_calculator` with payloads documented in `references/checklists/calculator-io.md`.

Legacy alias `run_hk_calculator` remains for backward compatibility; prefer `run_uk_calculator`.

---

## Folder Structure

```text
uk-architect-master/
├── SKILL.md                 # Master router: uk-architect-master
├── skills.json              # Sub-skill registry and load_when hints
├── main.py                  # Plugin entry: load_sub_skill + calculator dispatch
├── subskills/
│   └── <module-id>/
│       └── <module-id>.md
├── references/
│   ├── compliance.md
│   ├── operational.md
│   ├── domain_terms.json
│   ├── config.json
│   ├── templates/
│   └── checklists/
├── scripts/
│   ├── dispatcher.py
│   ├── calculators.py
│   └── update_subskills.py
└── evals/
    ├── evals.json
    └── files/

uk-architect-master-workspace/   # Sibling eval outputs (not inside skill folder)
└── iteration-1/
```

---

## Calculators

| `calc_type` | Purpose |
|-------------|---------|
| `part_l_screen` | Early fabric U-value and optional TER check |
| `part_o_screen` | Overheating risk band (advisory) |
| `ipms_converter` | GIA/NIA ↔ IPMS indicative conversion |
| `egress_screen` | Diagonal travel distance advisory screen |

All outputs are **advisory only**; full compliance requires SAP/SBEM, dynamic thermal modelling, and fire strategy sign-off.

---

## Verification

Run the golden questions in [uk-architect-master/VERIFICATION.md](uk-architect-master/VERIFICATION.md) after install or major edits.

---

## Example Prompts

- "Is this residential tower likely HRB and what BSA gateways apply?"
- "Map Approved Document routes for Part L and Part O at RIBA Stage 3."
- "What should our Regulation 38 pack contain before practical completion?"
- "Compare JCT 2024 variation routes for this employer change."
- "Screen Part O risk for a south-facing 40% glazing ratio without purge ventilation."
- "Draft a stage decision log for planning submission readiness."

---

## Standards and Frameworks

- RIBA Plan of Work 2020
- Building Safety Act 2022 and HRB gateways
- Building Regulations and Approved Documents
- CDM 2015
- Fire Safety (England) Regulations 2022
- JCT 2024 / NEC4 (contract administration guidance only)
- ISO 19650 (information management)

Always confirm jurisdiction and project-specific consultant sign-off.

---

## Authoring

Structure follows [FUNC_Skills_Guideline/GUIDELINE.md](FUNC_Skills_Guideline/GUIDELINE.md) (Tier 2 professional role skill). Deep authoring reference: [Blueprint & Toolkit — Creating High-Performance Claude Professional Skills](Blueprint%20&%20Toolkit-%20Creating%20High-Performance%20Claude%20Professional%20Skills.md).
