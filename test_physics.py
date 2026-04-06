import numpy as np

def calculate_dispute_value(mass, velocity, delta_t, contract_value, baseline_entropy=1.5):
    """The exact logic from your Engine.py but standalone."""
    ke = 0.5 * mass * (velocity**2)
    entropy_delta = np.log1p(delta_t) / baseline_entropy
    friction_factor = ke + entropy_delta
    settlement = (friction_factor / (1 + friction_factor)) * contract_value
    
    return {
        "status": "DISPUTE_VALIDATED" if entropy_delta > 1.2 else "STABLE_TRADE",
        "settlement": round(settlement, 2)
    }

if __name__ == "__main__":
    print("--- STANDALONE PROTOCOL TEST ---")
    res = calculate_dispute_value(180000, 24.5, 72, 15000000)
    print(f"STATUS: {res['status']}")
    print(f"SETTLEMENT: ${res['settlement']:,.2f}")
