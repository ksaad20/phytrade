import sys
import os

# 1. Force Python to look in 'src' first
sys.path.insert(0, os.path.abspath("src"))

# 2. Import the classes directly from their specific files
# This is the "Maximum Certainty" way to avoid the ImportError
from phytrade.engine import Engine
from phytrade.schema import Schema
from phytrade.mapper import Mapper

def main():
    print("-" * 30)
    print("PHYTRADE ENTERPRISE ARBITRATOR")
    print("-" * 30)

    # 3. Initialize with custom mapping (The 'Any Port' Logic)
    singapore_mapping = {
        "vessel_displacement": "mass",
        "current_sog": "velocity",
        "arrival_delay": "delta_t",
        "cargo_value_usd": "contract_value"
    }
    
    # Passing Schema directly to the Engine is the Pro-tier way 
    # to handle validation without circular imports.
    engine = Engine(baseline_entropy=1.5)
    
    # 4. Run the data
    raw_telemetry = {
        "mass": 180000, 
        "velocity": 24.5, 
        "delta_t": 72, 
        "contract_value": 15000000
    }
    
    result = engine.calculate_dispute_value(
        raw_telemetry['mass'], 
        raw_telemetry['velocity'], 
        raw_telemetry['delta_t'], 
        raw_telemetry['contract_value']
    )
    
    print(f"STATUS: {result['status']}")
    print(f"SETTLEMENT: ${result['recommended_settlement_usd']:,.2f}")

if __name__ == "__main__":
    main()
