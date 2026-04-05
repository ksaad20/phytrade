"""
phytrade: Institutional Physics Library for Global Commodity Arbitration
Author: Kazi Saad Asif
"""

from importlib.metadata import version, PackageNotFoundError

# 1. Dynamic PyPI Versioning (Removes manual updates)
try:
    __version__ = version("phytrade")
except PackageNotFoundError:
    __version__ = "1.2.6"  # Fallback to your current version

__author__ = "Kazi Saad Asif"

# 2. Domain-Specific Arbitrators (Your existing imports)
from .thermo import ThermoArbitrator
from .fluids import FluidsArbitrator
from .mechanical import MechanicalArbitrator
from .logistics import LogisticsArbitrator
from .strategic import StrategicArbitrator

# 3. Core Commercial API (The "Any Port" logic)
from .engine import Engine
from .schema import Schema
from .mapper import Mapper

# 4. Public Exports
__all__ = [
    "__version__",
    "__author__",
    "ThermoArbitrator",
    "FluidsArbitrator",
    "MechanicalArbitrator",
    "LogisticsArbitrator",
    "StrategicArbitrator",
    "Engine",
    "Schema",
    "Mapper",
]
