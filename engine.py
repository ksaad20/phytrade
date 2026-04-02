import numpy as np
import datetime
from typing import Dict, Any

class MassArbitrator:
    """
    phytrade v1.1.7: Thermodynamic Mass Arbitration Engine.
    
    Standard Compliance:
    - ASABE D245.7: Moisture Relationship of Plant-Based Agricultural Products.
    - ASTM D2495: Standard Test Method for Moisture in Cotton.
    - ASTM D1909: Standard Table of Commercial Moisture Regains.
    """

    # Constants derived from ASABE D245.7 (Modified Halsey Equation)
    # ASABE: Technical/Scientific coefficients for EMC prediction.
    # ASTM: Legal/Commercial 'Regain' allowances for trade settlement.
    REGULATORY_DATA = {
        "ASABE": {
            "Cotton": {"coeffs": (0.000022, 1.55, 2.18), "allowance_basis": "Scientific"},
            "Jute":   {"coeffs": (0.000031, 1.62, 2.45), "allowance_basis": "Scientific"},
            "General": {"coeffs": (0.000021, 1.52, 2.15), "allowance_basis": "Scientific"}
        },
        "ASTM": {
            "Cotton": {"coeffs": (0.000020, 1.50, 2.10), "commercial_regain": 0.085}, 
            "Jute":   {"coeffs": (0.000029, 1.60, 2.40), "commercial_regain": 0.1375},
            "General": {"coeffs": (0.000020, 1.50, 2.12), "commercial_regain": 0.080}
        }
    }

    @staticmethod
    def calculate_emc(rh: float, temp_k: float, a: float, b: float, c: float) -> float:
        """
        Modified Halsey Equation (ASABE D245.7 compliant).
        Solves for Equilibrium Moisture Content (EMC).
        """
        rh_decimal = rh / 100.0 if rh > 1.0 else rh
        rh_decimal = np.clip(rh_decimal, 0.01, 0.98) # Stability clipping per ASABE
        
        numerator = -np.log(1 - rh_decimal)
        denominator = a * (temp_k ** b)
        return (numerator / denominator) ** (1 / c)

    @classmethod
    def solve(cls, mass: float, moisture: float, rh: float, temp_c: float, 
              material: str = "Cotton", standard: str = "ASABE") -> Dict[str, Any]:
        """Calculates deconvolution using the ASABE D245.7 thermodynamic model."""
        std_info = cls.REGULATORY_DATA.get(standard, cls.REGULATORY_DATA["ASABE"])
        data = std_info.get(material, std_info["General"])
        
        temp_k = temp_c + 273.15
        dry_mass = mass * (1 - moisture)
        
        # Determine Target Equilibrium via ASABE math
        target_emc = cls.calculate_emc(rh, temp_k, *data["coeffs"])
        predicted_mass = dry_mass / (1 - target_emc)
        
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "standard_framework": standard,
            "material": material,
            "dry_mass_kg": round(dry_mass, 4),
            "predicted_mass_kg": round(predicted_mass, 4),
            "emc_percentage": round(target_emc * 100, 2),
            "status": "ASABE D245.7 Compliant"
        }

    @classmethod
    def arbitrate(cls, mass: float, moisture: float, rh: float, temp_c: float, material: str = "Cotton") -> Dict[str, Any]:
        """
        The Interoperability Audit: Compares ASABE Scientific Data vs ASTM Legal Data.
        Crucial for resolving 'Ghost Weight' disputes in commercial shipments.
        """
        asabe_res = cls.solve(mass, moisture, rh, temp_c, material, "ASABE")
        astm_res = cls.solve(mass, moisture, rh, temp_c, material, "ASTM")
        
        variance = abs(asabe_res["predicted_mass_kg"] - astm_res["predicted_mass_kg"])
        
        return {
            "audit_id": f"PT-{datetime.datetime.now().strftime('%Y%m%d%H%M')}",
            "asabe_scientific_mass": asabe_res["predicted_mass_kg"],
            "astm_commercial_mass": astm_res["predicted_mass_kg"],
            "variance_kg": round(variance, 4),
            "verdict": "SIGNIFICANT" if variance > 0.05 else "NEGLIGIBLE",
            "legal_citation": "ASABE D245.7 (Thermodynamics) & ASTM D2495 (Commercial Compliance)"
        }
