# phytrade v1.1.8: The Global Standard for Trade Physics

**High-precision thermodynamic deconvolution and mass arbitration for international commerce.**

`phytrade` is a specialized Python engine designed to resolve mass discrepancies in porous materials (Cotton, Jute, etc.) by reconciling scientific equilibrium with commercial regulatory standards.

## 🚀 Key Features (v1.1.8)
* **ASABE D245.7 Compliance:** Implements the Modified Halsey Equation using certified agricultural engineering coefficients.
* **ASTM D2495 Interoperability:** Bridges the gap between scientific Equilibrium Moisture Content (EMC) and commercial weight allowances.
* **Mass Arbitration:** Identify "Ghost Weight" variances in maritime and land-based cargo.
* **Audit-Ready Reporting:** Generates timestamped reports with legal and scientific citations.

## 🛠 Installation
```bash
pip install phytrade

##Resolving a dispute 

from phytrade.engine import MassArbitrator

# Initialize the Arbitrator for a Cotton shipment
arb = MassArbitrator(material="Cotton")

# Run a side-by-side audit of ASABE vs ASTM standards
audit = arb.arbitrate(mass=25000, moisture=0.12, rh=75, temp_c=32)

print(f"ASABE Scientific Mass: {audit['asabe_scientific_mass']} kg")
print(f"ASTM Commercial Mass: {audit['astm_commercial_mass']} kg")
print(f"Variance: {audit['variance_kg']} kg")
print(f"Verdict: {audit['verdict']}")

