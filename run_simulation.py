import sys
import os
import json

# 1. Path Management: Tell Python to look inside the 'src' directory
# This allows us to use 'from phytrade.engine' instead of relative imports
sys.path.insert(0, os.path.abspath("src"))

# 2. Decoupled Imports: Import specifically from the modules
# Since __init__.py is empty, we don't import 'phytrade' top-level
from phytrade.engine import Engine
from phytrade.mapper import Mapper
from phytrade.schema import Schema

def main():
    print("-" * 45)
    # Using a fallback version if __init__ is empty
    print("INITIALIZING PHYTRADE ARBITRATOR v1.2.7")
    print("-" * 45 + "\n")

    # 1. Initialize the Engine (Baseline Entropy for the Port)
    # Higher entropy = more disorder/delay sensitivity
    engine = Engine(baseline_entropy=1.5)

    # 2. Port-Specific Data Mapping
    # This maps 'Port Jargon' (CSV headers) to 'Physics Constants'
    singapore_mapping = {
        "vessel_displacement": "mass",
        "current_sog": "velocity",
        "arrival_delay": "delta_t",
        "cargo_value_usd": "contract_value"
    }
    
    # Initialize Mapper with specific port logic
    mapper = Mapper(column_mapping=singapore_mapping)

    # 3. Simulate Raw Incoming Telemetry from a Port
    raw_telemetry = {
        "mass": 180000,        # Metric Tons
        "velocity": 24.5,      # Knots
        "delta_t": 72,         # Hours of Delay
        "contract_value": 15000000  # 15M USD Trade
    }

    print("[*] Analyzing Physics-Based Dispute...")
    print(f" - Mass: {raw_telemetry['mass']} MT")
    print(f" - Velocity: {raw_telemetry['velocity']} knots")
    print(f" - Delay: {raw_telemetry['delta_t']} hrs\n")

    # 4. Execute the Settlement Logic
    # The Engine handles the kinetic energy and entropy calculations
    settlement = engine.calculate_dispute_value(
        mass=raw_telemetry['mass'],
        velocity=raw_telemetry['velocity'],
        delta_t=raw_telemetry['delta_t'],
        contract_value=raw_telemetry['contract_value']
    )

    # 5. Output the Institutional Result
    print("-" * 15 + " SETTLEMENT VERDICT " + "-" * 15)
    print(f"STATUS:       {settlement['status']}")
    print(f"IMPACT (KE):  {settlement['kinetic_energy_joules']:.2f} Joules")
    print(f"ENTROPY Δ:    {settlement['system_entropy']:.4f}")
    print("-" * 20)
    print(f"RECOMMENDED SETTLEMENT: ${settlement['recommended_settlement_usd']:,.2f}")
    print("-" * 45)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[!] Unexpected Error: {e}")
        print("Tip: Check that 'src/phytrade/__init__.py' is empty and 'schema.py' has MIN_MASS_KG defined.")
