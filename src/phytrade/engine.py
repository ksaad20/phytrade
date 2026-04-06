import numpy as np
from typing import TYPE_CHECKING, Dict, Any

# This prevents circular imports at runtime but allows IDE/Type checking
if TYPE_CHECKING:
    from phytrade.schema import Schema
    from phytrade.mapper import Mapper

class Engine:
    def __init__(self, baseline_entropy: float = 1.0, schema: 'Schema' = None, mapper: 'Mapper' = None):
        """
        Initializes the Physics-Trade Engine.
        Injecting schema and mapper as arguments makes the engine more 
        maneuverable and testable without global politics.
        """
        self.schema = schema
        self.baseline_entropy = baseline_entropy
        self.mapper = mapper

    def calculate_dispute_value(self, mass: float, velocity: float, delta_t: float, contract_value: float) -> Dict[str, Any]:
        """Core Physics: Kinetic Energy + Entropy Delta"""
        
        # Kinetic Energy: E = 0.5 * m * v^2
        ke = 0.5 * mass * (velocity**2)
        
        # Entropy Delta: log1p is more stable for small values
        entropy_delta = np.log1p(delta_t) / self.baseline_entropy
        
        friction_factor = ke + entropy_delta
        
        # Sigmoid scaling to ensure settlement doesn't exceed contract value
        # This keeps the business logic "objective"
        settlement = (friction_factor / (1 + friction_factor)) * contract_value
        
        return {
            "kinetic_energy_joules": ke,
            "system_entropy_delta": entropy_delta,
            "recommended_settlement_usd": round(settlement, 2),
            "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE"
        }

    def process_port_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maps inconsistent Port Jargon to validated physics parameters."""
        if not self.mapper or not self.schema:
            raise ImportError("Engine requires Mapper and Schema to process raw port data.")
            
        mapped = self.mapper.apply(raw_data, self.schema)
        
        return self.calculate_dispute_value(
            mass=mapped['mass'],
            velocity=mapped['velocity'],
            delta_t=mapped['time_delay'],
            contract_value=mapped['value']
        )
