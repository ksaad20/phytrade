
from .engine import MassArbitrator
from .registry import MATERIAL_REGISTRY

__version__ = "1.0.0"

def quick_check(mass, moisture, rh, temp_c, material="COTTON"):
    """Entry point for rapid trade mass verification."""
    constants = MATERIAL_REGISTRY.get(material.upper())
    if not constants:
        raise ValueError(f"Material {material} not found in physical registry.")
    return MassArbitrator.solve(mass, moisture, rh, temp_c, constants)
