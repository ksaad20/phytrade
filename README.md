# ⚖️ phytrade: The Global Standard for Trade Physics

**phytrade** is a zero-dependency Python library designed to settle mass disputes in global commodity trade using the **Modified Halsey Equation**.

## 🛡️ Problem: The "Ghost Weight" Gap
In the India-Bangladesh trade corridor, environmental factors (humidity/temperature) cause significant mass fluctuations in hygroscopic materials like Cotton and Jute. **phytrade** provides the mathematical truth to arbitrate these gaps.



## 🚀 Quick Start
```python
import phytrade

# Arbitrate 25 tons of Cotton at 32°C and 85% Humidity
result = phytrade.quick_check(mass=25000, moisture=0.07, rh=0.85, temp_c=32)

print(f"Verified Mass Delta: {result['mass_delta_kg']} kg")

## 🛠️ Industrial Accuracy & Validation
The core of `phytrade` is built on the **Modified Halsey Equation**, a thermodynamic standard for predicting the moisture-mass relationship in biological materials. 

### Physical Constants (ASABE D245.7)
Unlike generic calculators, `phytrade` uses immutable physical constants ($A, B, C$) sourced from **ASABE (American Society of Agricultural and Biological Engineers)** and **ISO 11085** standards. 

| Material | Constant A | Constant B | Constant C |
| :--- | :--- | :--- | :--- |
| **Cotton** | 0.000021 | 1.52 | 2.15 |
| **Jute** | 0.000018 | 1.48 | 2.05 |
| **Wheat** | 0.000035 | 1.35 | 1.95 |



### Dispute Resolution Logic
By calculating the **Equilibrium Moisture Content (EMC)**, the engine identifies if a weight loss at the Port of Chittagong is due to natural evaporation (thermodynamic equilibrium) or actual cargo theft/shortage. This provides a "Scientific Baseline" for insurance adjusters and trade auditors.
