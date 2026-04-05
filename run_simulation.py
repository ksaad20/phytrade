"""
PhyTrade v1.2.7: Commercial Port Simulation
Simulating an Institutional Physics-Based Settlement
"""

import sys
import os

# ADD THESE TWO LINES HERE
# This tells Python that your code lives in the 'src' folder
sys.path.insert(0, os.path.abspath("src"))

import phytrade
import json

def main():
    print(f"{'='*45}")
    print(f" INITIALIZING PHYTRADE ARBITRATOR v{phytrade.__version__} ")
    print(f"{'='*45}\n")

    # 1. Initialize the Engine (Baseline Entropy for the Port)
    # Higher entropy = more disorder/delay sensitivity
    engine = phytrade.Engine(baseline_entropy=1.5)

    # 2. Port-Specific Data Mapping
    # This maps 'Port Jargon' (CSV headers) to 'Physics Constants'
    singapore_mapping = {
        "Vessel_Displacement": "mass", 
        "Current_SOG": "velocity", 
        "Arrival_Delay": "delta_t",
        "Cargo_Value_USD": "contract_value"
    }
    mapper = phytrade.Mapper(column_mapping=singapore_mapping)

    # 3. Simulate Raw Incoming Telemetry from a Port
    # In a real scenario, this would come from mapper.map_and_validate('port_logs.csv')
    raw_telemetry = {
        "mass": 180000,          # Metric Tons
        "velocity": 24.5,        # Knots
        "delta_t": 72,           # Hours of Delay
        "contract_value": 15000000 # 15M USD Trade
    }

    print(f"[*] Analyzing Physics-Based Dispute...")
    print(f"    - Mass: {raw_telemetry['mass']} MT")
    print(f"    - Velocity: {raw_telemetry['velocity']} knots")
    print(f"    - Delay: {raw_telemetry['delta_t']} hrs\n")

    # 4. Execute the Settlement Logic
    # Using the Engine we refined in the previous step
    settlement = engine.calculate_dispute_value(
        mass=raw_telemetry['mass'],
        velocity=raw_telemetry['velocity'],
        delta_t=raw_telemetry['delta_t'],
        contract_value=raw_telemetry['contract_value']
    )

    # 5. Output the Institutional Result
    print(f"--- SETTLEMENT VERDICT ---")
    print(f"STATUS:      {settlement['status']}")
    print(f"IMPACT (KE): {settlement['kinetic_energy_joules']:,.2f} Joules")
    print(f"ENTROPY Δ:   {settlement['system_entropy']:.4f}")
    print(f"{'-'*26}")
    print(f"RECOMMENDED SETTLEMENT: ${settlement['recommended_settlement_usd']:,.2f}")
    print(f"{'='*45}")

if __name__ == "__main__":
    try:
        main()
    except AttributeError as e:
        print(f"\n[!] Error: Your __init__.py is missing a component.")
        print(f"    Check that 'Engine' and 'Mapper' are exported in src/phytrade/__init__.py")
    except Exception as e:
        print(f"\n[!] Unexpected Error: {e}")
  
