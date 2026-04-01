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
