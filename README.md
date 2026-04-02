# phytrade (v1.1.9)

**Institutional Physics Library for Global Commodity Arbitration**

`phytrade` is a high-precision computational physics framework designed to resolve mass, quality, and environmental disputes in international trade. By implementing industry-standard thermodynamics, fluid dynamics, and mechanical stress models, it provides an objective "Arbitrator" for maritime and land-based commerce.

---

## 🏛️ Project Architecture: The 50-Problem Roadmap

Version 1.1.9 introduces a **Modular Domain Expansion**. The library is structured into five distinct categories to cover the entire lifecycle of global trade physics.



| Category | Domain | Status | Scope |
| :--- | :--- | :--- | :--- |
| **I** | **Thermodynamics** | ✅ **Active** | Problems 1-10 (Moisture, Heat, PCM) |
| **II** | **Fluid Dynamics** | 🏗️ *Planned* | Problems 11-20 (Viscosity, Flow, Cargo) |
| **III** | **Mechanical** | 🏗️ *Planned* | Problems 21-30 (Stress, Strain, Loading) |
| **IV** | **Logistics** | 🏗️ *Planned* | Problems 31-40 (Optimization, Routing) |
| **V** | **Strategic** | 🏗️ *Planned* | Problems 41-50 (Risk, Game Theory) |

---

## 🚀 Key Features (Category I: Thermodynamics)

The current release fully populates the `thermo` engine with 10 specialized solvers:

* **Mass Deconvolution:** Implementation of **ASABE D245.7** and **ASTM D2495** for moisture-adjusted mass arbitration.
* **Container Rain Prediction:** Dew point analysis to prevent cargo sweat and moisture damage.
* **Thermal Management:** PCM (Phase Change Material) requirement solvers and Vacuum Insulated Panel (VIP) status monitoring.
* **Biological Activity:** Respiration heat and ethylene diffusion models for perishable cargo.

---

## 📦 Installation 

```bash
pip install phytrade

---

## 🛠️ Usage

To integrate the arbitration engine into your workflow, use the domain-specific import:

```python
from phytrade.thermo import ThermoArbitrator

# 1. Initialize the Category I engine
arbitrator = ThermoArbitrator()

# 2. Solve a "Ghost Weight" (Moisture Arbitration) dispute
# Example: 25,000kg Cotton at 12% moisture in 65% RH / 30°C
result = arbitrator.solve_ghost_weight(
    mass=25000, 
    moisture=0.12, 
    rh=65, 
    temp_c=30, 
    material="Cotton"
)

print(f"Arbitrated Mass: {result['predicted_mass_kg']} kg")
print(f"Variance: {result['variance_kg']} kg")

📝 Standards Compliance
phytrade adheres to international scientific and engineering standards, including:

ASABE D245.7: Moisture relationships for agricultural products.

ASTM D2495: Standard test method for moisture in cotton.

ISO 19011: Guidelines for auditing management systems.

📄 License & Citation
License: Proprietary. All rights reserved.

If you use this library in commercial arbitration or academic research, please cite it using the included CITATION.cff file:

Plaintext
Asif, K. S. (2026). phytrade: Institutional Physics Library for Global Commodity Arbitration (v1.1.9).
Author: Kazi Saad Asif

Contact: kazisaadasif29@gmail.com

GitHub: ksaad20/phytrade
