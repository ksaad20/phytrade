import numpy as np

class MassArbitrator:
    """Proprietary engine for thermodynamic mass verification."""
    
    @staticmethod
    def calculate_emc(rh: float, temp_k: float, a: float, b: float, c: float) -> float:
        # Prevent math errors at extreme humidity (0% or 100%)
        rh = np.clip(rh, 0.01, 0.98)
        
        # Modified Halsey Equation
        numerator = -np.log(1 - rh)
        denominator = a * (temp_k ** b)
        
        return (numerator / denominator) ** (1 / c)

    @classmethod
    def solve(cls, mass, moisture, rh, temp_c, constants):
        """Standardized logic for resolving weight disputes."""
        temp_k = temp_c + 273.15
        dry_mass = mass * (1 - moisture)
        
        # Predict target Equilibrium Moisture Content (EMC)
        target_emc = cls.calculate_emc(rh, temp_k, *constants)
        
        # Predicted mass at the current atmospheric equilibrium
        predicted_mass = dry_mass / (1 - target_emc)
        
        return {
            "dry_mass_kg": round(dry_mass, 4),
            "predicted_mass_kg": round(predicted_mass, 4),
            "mass_delta_kg": round(predicted_mass - mass, 4),
            "emc_percentage": round(target_emc * 100, 2)
        }
