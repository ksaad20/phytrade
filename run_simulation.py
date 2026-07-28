import os
import sys

# 1. Force the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from phytrade.engine import Engine


def main():
    engine = Engine()

    result = engine.calculate_dispute_value(
        mass=10000,
        velocity=12,
        delta_t=3600,
        contract_value=500000,
    )

    print(result)


if __name__ == "__main__":
    main()
