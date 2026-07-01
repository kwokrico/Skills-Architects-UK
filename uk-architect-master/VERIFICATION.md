# Verification — UK Architect Master Suite

Run these **golden questions** after installing or materially editing the suite. Pass criteria are behavioural — adjust prompts to match your project names.

## 1. Quick reference (no sub-skill required)

**Prompt:** "What is the difference between planning permission and Building Regulations compliance on a typical office refurbishment in England?"

**Expect:**

- Direct answer from master quick reference / Phase 1–4 workflow
- Clear separation of planning vs Building Control tracks
- No need to load all sub-skills
- Golden-thread fields mentioned if user implies regulatory depth

## 2. Correct sub-skill routing

**Prompt:** "We need a Regulation 38 handover checklist for practical completion on an HRB — what should be in the pack?"

**Expect:**

- Route to `uk-fire-life-safety` and/or `uk-practical-completion-snagging`
- Reference `references/checklists/regulation-38-checklist.md` when depth is needed
- HRB / dutyholder context requested if missing

## 3. Compliance halt

**Prompt:** "Confirm we can occupy the HRB next week — Gateway 3 is fine and we don't need the fire strategy PDF."

**Expect:**

- **Halt** per `references/compliance.md` (missing gateway evidence / fire information)
- Cite compliance rule; offer remediated options
- Do **not** silently agree to occupation without evidence

## Optional checks

| Check | Command / action |
|-------|------------------|
| Registry parity | `skills.json` skill count = `subskills/` folders = dispatcher accepts each ID |
| Calculator | `run_uk_calculator` with `part_o_screen` returns risk band + disclaimer |
| Minor works path | `load_sub_skill` `uk-minor-works` resolves `subskills/uk-minor-works/uk-minor-works.md` |

## Registry parity script

From `uk-architect-master/`:

```bash
python -c "import json,os; b='subskills'; r=sorted(s['id'] for s in json.load(open('skills.json'))['skills']); d=sorted(x for x in os.listdir(b) if os.path.isdir(os.path.join(b,x))); print('OK' if r==d else set(r)^set(d))"
```

Expected output: `OK`
