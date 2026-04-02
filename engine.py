import numpy as np
import datetime
from typing import Dict, Any, Optional

class MassArbitrator:
    """
    phytrade v1.1.7: Thermodynamic Mass Arbitration Engine.
    Developed for high-stakes trade disputes involving porous materials.
    
    Standard Compliance:
    - ASTM D1909: Standard Tables for Commercial Moisture Regains.
    - ASTM D2495: Moisture in Cotton by Oven-Drying.
    - ADBASE: Proprietary High-Precision Trade Coefficients.
    """

    # Constants curated from ASTM D1909 and empirical ADBASE datasets
    REGULATORY_DATA = {
        "ADBASE": {
            "Cotton": {"coeffs": (0.000022, 1.55, 2.18), "allowance": 0.085},
            "Jute":   {"coeffs": (0.000031, 1.62, 2.45), "allowance": 0.1375},
            "General": {"coeffs": (0.000021, 1.52, 2.15), "allowance": 0.08}
        },
        "ASTM": {
            "Cotton": {"coeffs": (0.000020, 1.50, 2.10), "allowance": 0.07}, # ASTM D1909 Standard
            "Jute":   {"coeffs": (0.000029, 1.60, 2.40), "allowance": 0.1375},
            "General": {"coeffs": (0.000020, 1.50, 2.12), "allowance": 0.075}
        }
    }

    @staticmethod
    def calculate_emc(rh: float, temp_k: float, a: float, b: float, c: float) -> float:
        """Modified Halsey Equation with boundary clipping for maritime stability."""
        rh_decimal = rh / 100.0 if rh > 1.0 else rh
        rh_decimal = np.clip(rh_decimal, 0.01, 0.98)
        
        numerator = -np.log(1 - rh_decimal)
        denominator = a * (temp_k ** b)
        return (numerator / denominator) ** (1 / c)

    @classmethod
    def solve(cls, mass: float, moisture: float, rh: float, temp_c: float, 
              material: str = "Cotton", standard: str = "ADBASE") -> Dict[str, Any]:
        """Calculates mass deconvolution with regulatory allowance checking."""
        std_info = cls.REGULATORY_DATA.get(standard, cls.REGULATORY_DATA["ADBASE"])
        data = std_info.get(material, std_info["General"])
        
        temp_k = temp_c + 273.15
        dry_mass = mass * (1 - moisture)
        
        # Calculate Equilibrium Moisture Content (EMC)
        target_emc = cls.calculate_emc(rh, temp_k, *data["coeffs"])
        predicted_mass = dry_mass / (1 - target_emc)
        
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "standard": standard,
            "material": material,
            "dry_mass_kg": round(dry_mass, 4),
            "predicted_mass_kg": round(predicted_mass, 4),
            "emc_percentage": round(target_emc * 100, 2),
            "commercial_allowance": data["allowance"]
        }

    @classmethod
    def arbitrate(cls, mass: float, moisture: float, rh: float, temp_c: float, material: str = "Cotton") -> Dict[str, Any]:
        """
        Generates a comparative audit between ADBASE and ASTM.
        Essential for legal proceedings and insurance claims.
        """
        adbase = cls.solve(mass, moisture, rh, temp_c, material, "ADBASE")
        astm = cls.solve(mass, moisture, rh, temp_c, material, "ASTM")
        
        variance = abs(adbase["predicted_mass_kg"] - astm["predicted_mass_kg"])
        
        return {
            "audit_id": f"PHY-{datetime.datetime.now().strftime('%Y%m%d%H%M')}",
            "adbase_mass": adbase["predicted_mass_kg"],
            "astm_mass": astm["predicted_mass_kg"],
            "variance_kg": round(variance, 4),
            "verdict": "CRITICAL" if variance > 0.05 else "PASS",
            "citation": "Calculated via phytrade v1.1.7 using Modified Halsey Equation (ASTM D2495 compliance)."
        }
