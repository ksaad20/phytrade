# phytrade (v1.2.8)

**Institutional Physics Library and Protocol for Global Commodity Arbitration**

`phytrade` is a high-precision computational physics framework designed to resolve mass, quality, and environmental disputes in international trade. By implementing industry-standard thermodynamics, fluid dynamics, and mechanical stress models, it provides an objective "Arbitrator" for maritime and land-based commerce.

---

## 🏛️ Project Architecture: The 50-Problem Roadmap

Version **1.2.8** marks the transition from a specialized thermal tool to a comprehensive physics engine. All five core domains are now **Active**, populating the library with the first 50 essential problem-solvers for global trade.

| Category | Domain | Status | Scope |
| :--- | :--- | :--- | :--- |
| **I** | **Thermodynamics** | ✅ **Active** | Problems 1-10 (Moisture, Heat, PCM) |
| **II** | **Fluid Dynamics** | ✅ **Active** | Problems 11-20 (Drag, Cavitation, Siltation) |
| **III** | **Mechanical** | ✅ **Active** | Problems 21-30 (Stress, Torque, Wind Tech) |
| **IV** | **Logistics** | ✅ **Active** | Problems 31-40 (Platooning, Docking, Routing) |
| **V** | **Strategic** | ✅ **Active** | Problems 41-50 (ROI, Risk, Game Theory) |

---

## 🚀 Key Features (v1.2.8 Expansion)

The library now supports multi-domain arbitration across the following engines:

* **Thermo (Category I):** Mass Deconvolution (ASABE D245.7), Container Rain Prediction, and Perishable Respiration models.
* **Fluids (Category II):** **Hull Skin Friction** analysis for bio-fouling, **Propeller Cavitation** erosion risk, and **Port Siltation** depth impact on cargo capacity.
* **Mechanical (Category III):** **Wind-Assisted Propulsion** (Sails/Rotors) force calculation, **Shaft Torque** monitoring, and **Hull Stress** analysis.
* **Logistics (Category IV):** **Aerodynamic Drafting** (Truck/Ship Platooning) fuel savings and optimized **Dry-Docking** scheduling.
* **Strategic (Category V):** **Economical Speed** optimization, **Strategic Reserve** utilization, and **Market Volatility** hedging.

---

##🛠 Usage: The "Any Port" Arbitrator
To bypass localized data naming conventions, use the v1.2.8 mapping bridge:

'''bash

from phytrade.engine import Engine
from phytrade.schema import Schema
from phytrade.mapper import Mapper

# 1. Initialize the Protocol
schema = Schema()
mapper = Mapper()
engine = Engine(baseline_entropy=1.5, schema=schema, mapper=mapper)

# 2. Define Local Port Jargon (e.g., Singapore, Rotterdam, or Chattogram)
local_mapping = {
    "vessel_displacement": "mass",
    "current_sog": "velocity",
    "arrival_delay": "delta_t",
    "cargo_value_usd": "contract_value"
}

# 3. Raw Telemetry Data
raw_data = {
    "vessel_displacement": 180000, 
    "current_sog": 24.5, 
    "arrival_delay": 72, 
    "cargo_value_usd": 15000000
}

# 4. Execute Objective Arbitration
# This bypasses human bias by using the laws of physics as the contract base.
mapped_data = {local_mapping[k]: v for k, v in raw_data.items()}
result = engine.calculate_dispute_value(**mapped_data)

print(f"Arbitration Status: {result['status']}")
print(f"Recommended Settlement: ${result['recommended_settlement_usd']:,.2f}")


## 📦 Installation 

```bash
pip install phytrade

🛠️ Usage  
To integrate the arbitration engine into your workflow, initialize the specific domain arbitrator:

from phytrade import ThermoArbitrator, FluidsArbitrator, MechanicalArbitrator

# 1. Initialize the Engines
thermo = ThermoArbitrator()
fluids = FluidsArbitrator()
mech = MechanicalArbitrator()

# 2. Solve a Hull Friction Dispute (Problem 11)
# Estimate drag increase from bio-fouling (15% fouling index) at 12 knots
drag_increase = fluids.estimate_hull_skin_friction(
    velocity=6.17,  # 12 knots in m/s
    wetted_area=3500, 
    bio_fouling_index=0.15
)

# 3. Calculate Wind Propulsion Offset (Problem 19)
wind_force = mech.calculate_wind_propulsion(
    wind_speed=15.0, 
    sail_area=200, 
    angle=45
)

print(f"Added Drag Force: {drag_increase} N")
print(f"Wind Assist Force: {wind_force} N")

📝 Standards Compliance
phytrade adheres to international scientific and engineering standards, including:

ASABE D245.7: Moisture relationships for agricultural products.

ASTM D2495: Standard test method for moisture in cotton.

ITTC Recommended Procedures: For Hull Resistance and Propeller Cavitation.

ISO 19011: Guidelines for auditing management systems.

IMO MARPOL Annex VI: For Carbon Intensity Indicator (CII) modeling.

📄 License & Citation
License:Proprietary. All rights reserved.

If you use this library in commercial arbitration or academic research, please cite it using the included CITATION.cff file:

Plaintext:

Asif, K. S. (2026). phytrade: Institutional Physics Library for Global Commodity Arbitration (v1.2.6).

Author: Kazi Saad Asif

Contact: kazisaadasif29@gmail.com

GitHub: ksaad20/phytrade
