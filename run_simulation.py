import sys
import os

# 1. Force the path
sys.path.insert(0, os.path.abspath("src"))

# 2. Direct Import from the file, bypassing __init__
from phytrade.engine import Engine

def main():
    print("--- PHYTRADE v1.2.7 START ---")
    engine = Engine(baseline_entropy=1.5)
    
    # Direct math test (Bypasses Schema/Mapper entirely)
    res = engine.calculate_dispute_value(180000, 24.5, 72, 15000000)
    
    print(f"STATUS: {res['status']}")
    print(f"SETTLEMENT: ${res['recommended_settlement_usd']:,.2f}")

if __name__ == "__main__":
    main()
