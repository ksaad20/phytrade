# run_simulation.py
import sys
import os

# 1. Direct path injection
sys.path.insert(0, os.path.abspath("src"))

# 2. Direct imports to bypass __init__ deadlocks
from phytrade.engine import Engine

def main():
    print("-" * 30)
    print("PHYTRADE v1.2.7 SIMULATION")
    print("-" * 30)

    # Initialize with baseline entropy
    engine = Engine(baseline_entropy=1.5)

    # Simulation Data
    raw_telemetry = {
        "mass": 180000,
        "velocity": 24.5,
        "delta_t": 72,
        "contract_value": 15000000
    }

    # Run the math
    result = engine.calculate_dispute_value(
        mass=raw_telemetry["mass"],
        velocity=raw_telemetry["velocity"],
        delta_t=raw_telemetry["delta_t"],
        contract_value=raw_telemetry["contract_value"]
    )

    print(f"STATUS: {result['status']}")
    print(f"RECOMMENDED SETTLEMENT: ${result['recommended_settlement_usd']:,.2f}")

if __name__ == "__main__":
    main()
