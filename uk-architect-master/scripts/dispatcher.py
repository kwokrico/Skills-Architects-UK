import os
import json

try:
    from scripts.calculators import run_calculation
except ImportError:
    try:
        from calculators import run_calculation
    except ImportError:
        run_calculation = None

SKILL_CHECKLISTS = {
    "uk-building-codes": ["bsa-gateway-checklist.md"],
    "uk-fire-life-safety": ["regulation-38-checklist.md"],
    "uk-spatial-planning": ["planning-submission-checklist.md"],
    "uk-building-sustainability": ["part-l-o-pathway.md"],
    "uk-heritage-conservation": ["hia-starter-checklist.md"],
    "uk-architect-calculator": ["calculator-io.md"],
    "uk-plan-of-work": [],
    "uk-construction-health-safety": ["cdm-preconstruction-checklist.md"],
    "uk-site-establishment": [],
    "uk-op-submission-strategy": ["bsa-gateway-checklist.md", "regulation-38-checklist.md"],
    "uk-fsd-licensing-compliance": ["regulation-38-checklist.md"],
}


def _load_skill_registry(base_path):
    """Load skill IDs from skills.json; fall back to subskills directory scan."""
    registry_path = os.path.join(base_path, "skills.json")
    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [entry["id"] for entry in data.get("skills", [])]

    subskills_base = os.path.join(base_path, "subskills")
    if not os.path.isdir(subskills_base):
        return []
    return sorted(
        name
        for name in os.listdir(subskills_base)
        if os.path.isdir(os.path.join(subskills_base, name))
    )


class UKArchitectDispatcher:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.subskills_base = os.path.join(self.base_path, "subskills")
        self.checklists_base = os.path.join(self.base_path, "references", "checklists")
        self.valid_skills = _load_skill_registry(self.base_path)

    def _resolve_skill_path(self, skill_id):
        primary = os.path.join(self.subskills_base, skill_id, f"{skill_id}.md")
        if os.path.exists(primary):
            return primary
        return None

    def _available_checklists(self, skill_id):
        names = SKILL_CHECKLISTS.get(skill_id, [])
        available = []
        for name in names:
            if os.path.isfile(os.path.join(self.checklists_base, name)):
                available.append(name)
        return available

    def load_sub_skill(self, skill_id):
        """Navigates to subskills/{id}/{id}.md and returns content."""
        if skill_id not in self.valid_skills:
            return {"error": f"Skill ID '{skill_id}' not recognized."}

        file_path = self._resolve_skill_path(skill_id)
        if not file_path:
            return {
                "error": f"Expected file at subskills/{skill_id}/{skill_id}.md not found."
            }

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            return {
                "status": "success",
                "skill_id": skill_id,
                "instructions": content,
                "references_available": self._available_checklists(skill_id),
            }
        except Exception as e:
            return {"error": str(e)}

    def run_uk_calculator(self, calc_type, data=None):
        """Run UK-oriented advisory calculations for early design checks."""
        if not run_calculation:
            return {"error": "Calculation module not found in scripts/."}

        if data is None:
            data = {}

        result = run_calculation(calc_type, data)
        if isinstance(result, dict) and result.get("error"):
            return result
        return {"status": "success", "result": result}
