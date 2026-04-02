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

