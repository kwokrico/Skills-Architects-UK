import math


class PartLScreenCalculator:
    """Early-stage Part L advisory checks (non-statutory)."""

    def calculate(self, data):
        proposed_u = data.get("proposed_u")
        target_u = data.get("target_u")
        dwelling_area = data.get("dwelling_area")
        notional_emission_rate = data.get("notional_emission_rate")
        design_emission_rate = data.get("design_emission_rate")

        if proposed_u is None or target_u is None:
            return {"error": "part_l_screen requires 'proposed_u' and 'target_u'."}

        fabric_pass = proposed_u <= target_u
        ter_check = None
        if design_emission_rate is not None and notional_emission_rate is not None:
            ter_check = {
                "design_emission_rate": round(float(design_emission_rate), 3),
                "target_emission_rate": round(float(notional_emission_rate), 3),
                "status": "Pass" if design_emission_rate <= notional_emission_rate else "Review",
            }

        return {
            "calculator": "part_l_screen",
            "fabric_status": "Pass" if fabric_pass else "Review",
            "proposed_u": float(proposed_u),
            "target_u": float(target_u),
            "dwelling_area": dwelling_area,
            "ter_check": ter_check,
            "disclaimer": "Advisory only. Final Part L compliance must be confirmed by full SAP/SBEM and regulatory review.",
        }


class PartOScreenCalculator:
    """Early-stage Part O overheating risk screen (non-statutory)."""

    def calculate(self, data):
        glazing_ratio = float(data.get("glazing_ratio", 0))
        orientation = str(data.get("orientation", "")).upper()
        purge_possible = bool(data.get("purge_ventilation_available", False))
        external_shading = bool(data.get("external_shading", False))
        urban_context = str(data.get("urban_context", "normal")).lower()

        risk_score = 0
        if glazing_ratio > 0.4:
            risk_score += 2
        elif glazing_ratio > 0.3:
            risk_score += 1
        if orientation in {"S", "SW", "W"}:
            risk_score += 1
        if not purge_possible:
            risk_score += 2
        if not external_shading:
            risk_score += 1
        if urban_context in {"dense", "urban_heat_island"}:
            risk_score += 1

        status = "Low"
        if risk_score >= 5:
            status = "High"
        elif risk_score >= 3:
            status = "Medium"
        return {
            "calculator": "part_o_screen",
            "risk_score": risk_score,
            "overheating_risk": status,
            "disclaimer": "Advisory screen only. Demonstrating Part O compliance requires full dynamic analysis or approved simplified methods.",
        }


class IPMSConverter:
    """Simple UK commercial area conversion helper."""

    def convert(self, data):
        value = data.get("value")
        from_type = str(data.get("from_type", "")).upper()
        to_type = str(data.get("to_type", "")).upper()
        if value is None:
            return {"error": "ipms_converter requires numeric 'value'."}

        # Advisory conversion factors for briefing comparisons only.
        factors = {
            ("GIA", "IPMS2"): 0.93,
            ("NIA", "IPMS3"): 0.98,
            ("IPMS2", "GIA"): 1.075,
            ("IPMS3", "NIA"): 1.02,
        }
        factor = factors.get((from_type, to_type))
        if factor is None:
            return {"error": f"No advisory factor defined for {from_type} -> {to_type}."}

        output = float(value) * factor
        return {
            "calculator": "ipms_converter",
            "from_type": from_type,
            "to_type": to_type,
            "input_value": float(value),
            "output_value": round(output, 3),
            "factor": factor,
            "disclaimer": "Indicative conversion only. Confirm measurement basis against project instruction and market standard.",
        }


class EgressScreenCalculator:
    """Very early egress check helper for briefing-stage use."""

    def calculate(self, data):
        length = float(data.get("length", 0))
        width = float(data.get("width", 0))
        sprinklered = bool(data.get("sprinklered", False))
        use_type = str(data.get("use_type", "residential")).lower()

        diagonal = math.sqrt(length ** 2 + width ** 2)
        if use_type == "residential":
            limit = 45 if sprinklered else 30
        else:
            limit = 45 if sprinklered else 30

        return {
            "calculator": "egress_screen",
            "diagonal_distance": round(diagonal, 2),
            "advisory_limit": limit,
            "status": "Pass" if diagonal <= limit else "Review",
            "disclaimer": "High-level advisory only. Final means-of-escape design must follow full Approved Document B and fire strategy assessment.",
        }


def run_calculation(calc_type, data):
    """Factory function for UK-oriented advisory calculators."""
    if calc_type == "part_l_screen":
        return PartLScreenCalculator().calculate(data)
    if calc_type == "part_o_screen":
        return PartOScreenCalculator().calculate(data)
    if calc_type == "ipms_converter":
        return IPMSConverter().convert(data)
    if calc_type == "egress_screen":
        return EgressScreenCalculator().calculate(data)
    return {"error": f"Calculator type {calc_type} not implemented."}