import numpy as np

class Engine:
    def __init__(self, baseline_entropy=1.0):
        # We point self.schema to the Class itself, not an instance Schema()
        # This allows self.mapper.apply(raw_data, self.schema) to work correctly
        from .schema import Schema
        self.schema = Schema
        self.baseline_entropy = baseline_entropy
        
        from .mapper import Mapper
        self.mapper = Mapper()

    def calculate_dispute_value(self, mass, velocity, delta_t, contract_value):
        """
        Calculates 'Financial Friction' based on Kinetic Energy and Time Disorder.
        Note: Ensure velocity is converted to m/s if Joules are required.
        """
        # 1. Kinetic Energy (Potential for damage/impact)
        # ke = 0.5 * m * v^2
        ke = 0.5 * mass * (velocity**2)

        # 2. Entropy Delta (Disorder caused by time delay)
        # log1p is more stable for very small delta_t values
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy

        # 3. Financial Friction Coefficient
        friction_factor = ke * entropy_delta

        # 4. Final Settlement (Normalized via Sigmoid-style scaling)
        # Prevents the settlement from exceeding the total contract value
        settlement = (friction_factor / (1 + friction_factor)) * contract_value

        return {
            "kinetic_energy_joules": ke,
            "system_entropy": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data):
        """The 'Any Port' logic: Maps raw input to physics parameters."""
        # Passing self.schema (the class) to the mapper
        mapped = self.mapper.apply(raw_data, self.schema)
        
        return self.calculate_dispute_value(
            mass=mapped['mass'],
            velocity=mapped['velocity'],
            delta_t=mapped['time_delay'],
            contract_value=mapped['value']
        )
