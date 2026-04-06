import sys
import os

# 1. Point directly to the source folder
sys.path.insert(0, os.path.abspath("src"))

# 2. Import the Engine class directly from the file
from phytrade.engine import Engine

def main():
    print("--- PHYTRADE v1.2.7 SIMULATION ---")
    
    # Simple Engine test (This bypasses Schema/Mapper entirely)
    engine = Engine(baseline_entropy=1.5)
    
    result = engine.calculate_dispute_value(
        mass=180000, 
        velocity=24.5, 
        delta_t=72, 
        contract_value=15000000
    )

    print(f"STATUS: {result['status']}")
    print(f"SETTLEMENT: ${result['recommended_settlement_usd']:,.2f}")

if __name__ == "__main__":
    main()
