import numpy as np
from typing import Dict, Any

class Engine:
    def __init__(self, baseline_entropy: float = 1.0, schema=None, mapper=None):
        """
        Initializes the Physics-Trade Engine.
        We removed the type hints ': Schema' to stop the import crash.
        """
        self.schema = schema
        self.baseline_entropy = baseline_entropy
        self.mapper = mapper

    def calculate_dispute_value(self, mass: float, velocity: float, delta_t: float, contract_value: float) -> Dict[str, Any]:
        """Core Physics Logic - This is now 100% independent."""
        ke = 0.5 * mass * (velocity**2)
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy
        
        friction_factor = ke + entropy_delta
        settlement = (friction_factor / (1 + friction_factor)) * contract_value
        
        return {
            "kinetic_energy_joules": ke,
            "system_entropy_delta": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        # ONLY import these when the function is actually called
        from .schema import Schema
        from .mapper import Mapper
        
        local_schema = self.schema if self.schema else Schema()
        local_mapper = self.mapper if self.mapper else Mapper()
        
        mapped = local_mapper.apply(raw_data, local_schema)
        
        return self.calculate_dispute_value(
            mass=mapped['mass'],
            velocity=mapped['velocity'],
            delta_t=mapped['time_delay'],
            contract_value=mapped['value']
        )
