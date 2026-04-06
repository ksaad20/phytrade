import sys
import os

# 1. Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath("src"))

# 2. IMPORTANT: Import directly from the engine file, 
# NOT from the 'phytrade' package generally.
from phytrade.engine import Engine

def main():
    print("--- PHYTRADE v1.2.7 SIMULATION ---")
    
    # Initialize engine
    engine = Engine(baseline_entropy=1.5)
    
    # Run a direct calculation
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
