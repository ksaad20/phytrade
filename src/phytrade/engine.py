import numpy as np
from .schema import Schema
from .mapper import Mapper

class Engine:
    def __init__(self, baseline_entropy=1.0):
        self.baseline_entropy = baseline_entropy
        self.schema = Schema()
        self.mapper = Mapper()

    def calculate_dispute_value(self, mass, velocity, delta_t, contract_value):
        """Calculates 'Financial Friction' based on Kinetic Energy and Time Disorder."""
        
        # 1. Kinetic Energy (Potential for damage/impact)
        ke = 0.5 * mass * (velocity**2)
        
        # 2. Entropy Delta (Disorder caused by time delay)
        # log1p is safer for small delta_t values
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy
        
        # 3. Financial Friction Coefficient
        friction_factor = ke * entropy_delta
        
        # 4. Final Settlement (Normalized to prevent exceeding total trade value)
        # Using a sigmoid-style normalization: friction / (1 + friction)
        settlement = (friction_factor / (1 + friction_factor)) * contract_value
        
        return {
            "kinetic_energy_joules": ke,
            "system_entropy": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data):
        """The 'Any Port' logic: Maps raw input to physics parameters."""
        mapped = self.mapper.apply(raw_data, self.schema)
        return self.calculate_dispute_value(
            mass=mapped['mass'], 
            velocity=mapped['velocity'], 
            delta_t=mapped['time_delay'], 
            contract_value=mapped['value']
        )
