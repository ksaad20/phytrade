import sys
import os

# 1. Force Python to look in 'src' first
sys.path.insert(0, os.path.abspath("src"))

# 2. Absolute imports to avoid the circular dependency issues
from phytrade.engine import Engine
from phytrade.schema import Schema
from phytrade.mapper import Mapper

def main():
    print("-" * 30)
    print("PHYTRADE ENTERPRISE ARBITRATOR")
    print("-" * 30)

    # 3. Initialize components
    schema = Schema()
    mapper = Mapper()
    # Passing schema and mapper to the Engine prevents the "Local Import" crash
    engine = Engine(baseline_entropy=1.5, schema=schema, mapper=mapper)

    # This is your "Any Port" Logic - mapping local jargon to physics keys
    singapore_mapping = {
        "vessel_displacement": "mass",
        "current_sog": "velocity",
        "arrival_delay": "delta_t",
        "cargo_value_usd": "contract_value"
    }

    # 4. Raw Telemetry Data (As it comes from the port)
    raw_telemetry = {
        "vessel_displacement": 180000, 
        "current_sog": 24.5, 
        "arrival_delay": 72, 
        "cargo_value_usd": 15000000
    }

    # 5. The Dispute Calculation Bridge
    # We use the mapping dictionary to tell the engine how to read the raw data
    # This is where you "Out-Rank" the bureaucracy: The math is automated.
    
    # Map the raw data to physics parameters
    mapped_data = {singapore_mapping[k]: v for k, v in raw_telemetry.items()}

    result = engine.calculate_dispute_value(
        mass=mapped_data['mass'],
        velocity=mapped_data['velocity'],
        delta_t=mapped_data['delta_t'],
        contract_value=mapped_data['contract_value']
    )

    # 6. Objective Output
    print(f"STATUS: {result['status']}")
    print(f"KINETIC ENERGY: {result['kinetic_energy_joules']:.2f} J")
    print(f"ENTROPY DELTA: {result['system_entropy_delta']:.4f}")
    print(f"SETTLEMENT: ${result['recommended_settlement_usd']:,.2f}")
    print("-" * 30)

if __name__ == "__main__":
    main()
