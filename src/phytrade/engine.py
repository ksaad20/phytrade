import numpy as np

class Engine:
    def __init__(self, baseline_entropy=1.0):
        """
        Initializes the Physics-Trade Engine.
        Local imports prevent the 'cannot import name Schema' error.
        """
        from phytrade.schema import Schema
        from phytrade.mapper import Mapper
        
        self.schema = Schema
        self.baseline_entropy = baseline_entropy
        self.mapper = Mapper()

    def calculate_dispute_value(self, mass, velocity, delta_t, contract_value):
        """Core Physics: Kinetic Energy + Entropy Delta"""
        ke = 0.5 * mass * (velocity**2)
        # Using log1p for stability with zero-delay shipments
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy
        
        friction_factor = ke * entropy_delta
        # Sigmoid scaling prevents settlement from exceeding contract value
        settlement = (friction_factor / (1 + friction_factor)) * contract_value

        return {
            "kinetic_energy_joules": ke,
            "system_entropy": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data):
        """
        THE ENTERPRISE BRIDGE:
        Maps inconsistent 'Port Jargon' to validated physics parameters.
        """
        # The mapper uses the Schema to validate against physical constants
        mapped = self.mapper.apply(raw_data, self.schema)
        
        return self.calculate_dispute_value(
            mass=mapped['mass'],
            velocity=mapped['velocity'],
            delta_t=mapped['time_delay'],
            contract_value=mapped['value']
        )
