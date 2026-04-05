import numpy as np

class Engine:
    def __init__(self, baseline_entropy=1.0):
        """
        Initializes the Physics-Trade Engine.
        Imports are handled locally to prevent circular dependency deadlocks.
        """
        # Local imports break the circular loop with __init__.py and schema.py
        from .schema import Schema
        from .mapper import Mapper
        
        # We point to the Class itself, not Schema(), because it is a static utility
        self.schema = Schema
        self.baseline_entropy = baseline_entropy
        self.mapper = Mapper()

    def calculate_dispute_value(self, mass, velocity, delta_t, contract_value):
        """Calculates 'Financial Friction' based on Kinetic Energy and Time Disorder."""
        
        # 1. Kinetic Energy (Potential for damage/impact)
        # Formula: ke = 0.5 * m * v^2
        ke = 0.5 * mass * (velocity**2)

        # 2. Entropy Delta (Disorder caused by time delay)
        # Using np.log1p (log of 1+x) is safer for very small or zero delta_t
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy

        # 3. Financial Friction Coefficient
        friction_factor = ke * entropy_delta

        # 4. Final Settlement (Normalized via sigmoid-style scaling)
        # This prevents the friction from exceeding the total trade value
        settlement = (friction_factor / (1 + friction_factor)) * contract_value

        return {
            "kinetic_energy_joules": ke,
            "system_entropy": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data):
        """The 'Any Port' logic: Maps raw input to validated physics parameters."""
        # Pass the Schema class to the mapper for validation logic
        mapped = self.mapper.apply(raw_data, self.schema)
        
        return self.calculate_dispute_value(
            mass=mapped['mass'],
            velocity=mapped['velocity'],
            delta_t=mapped['time_delay'],
            contract_value=mapped['value']
        )
