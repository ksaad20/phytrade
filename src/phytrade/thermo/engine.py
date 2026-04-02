import numpy as np
from typing import Dict

class ThermoArbitrator:
    """Category I: Thermodynamics & Heat Transfer (Problems 1-10)"""

    def __init__(self):
        # Constants for Problem 2: Mass Deconvolution
        self.standards = {
            "ASABE": {"Cotton": (0.000022, 1.55, 2.18), "Timber": (0.000018, 1.45, 2.05), "General": (0.000021, 1.52, 2.15)},
            "ASTM": {"Cotton": (0.000020, 1.50, 2.10), "Timber": (0.000017, 1.40, 2.00), "General": (0.000020, 1.50, 2.12)}
        }

    @staticmethod
    def predict_container_rain(temp_air: float, rh: float, temp_surface: float) -> Dict:
        alpha = np.log(rh/100) + (17.625 * temp_air) / (243.04 + temp_air)
        dp = (243.04 * alpha) / (17.625 - alpha)
        return {"dew_point_c": round(dp, 2), "risk": "CRITICAL" if temp_surface <= dp else "SAFE"}

    def solve_ghost_weight(self, mass: float, moisture: float, rh: float, temp_c: float, material: str = "Cotton", std: str = "ASABE"):
        c = self.standards[std].get(material, self.standards[std]["General"])
        t_k, rh_d = temp_c + 273.15, np.clip(rh/100, 0.01, 0.98)
        emc = ((-np.log(1 - rh_d)) / (c[0] * (t_k ** c[1]))) ** (1 / c[2])
        predicted = (mass * (1 - moisture)) / (1 - emc)
        return {"predicted_mass_kg": round(predicted, 4), "emc_percent": round(emc*100, 2)}

    @staticmethod
    def respiration_heat(mass_kg: float, product: str = "Apple") -> float:
        return (mass_kg / 1000) * {"Apple": 15, "Banana": 40, "Strawberry": 60}.get(product, 20)

    @staticmethod
    def pcm_requirement(hours: float, leak_watts: float) -> float:
        return round((leak_watts * 3600 * hours) / (334 * 1000), 2)

    @staticmethod
    def insulation_decay(r_init: float, weeks: float) -> float:
        return round(r_init * np.exp(-0.02 * weeks), 3)

    @staticmethod
    def ethylene_diffusion(gradient: float, area: float) -> float:
        return 0.2 * area * gradient

    @staticmethod
    def sublimation_loss(area: float, vp_diff: float, hours: float) -> float:
        return round(0.00015 * area * vp_diff * hours, 4)

    @staticmethod
    def thermal_bridge(temp_delta: float, area: float) -> float:
        return 0.5 * area * temp_delta

    @staticmethod
    def solar_gain(irradiance: float, area: float) -> float:
        return irradiance * area * 0.7

    @staticmethod
    def vip_status(pressure: float) -> str:
        return "FAILING" if pressure > 0.5 else "INTACT"
