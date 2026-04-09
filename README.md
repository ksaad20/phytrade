# phytrade (v1.3.0)

**Institutional Physics Library and Protocol for Global Commodity Arbitration**

`phytrade` is a high-precision computational physics framework designed to resolve mass, quality, and environmental disputes in international trade. By implementing industry-standard thermodynamics, fluid dynamics, and mechanical stress models, it provides an objective "Arbitrator" for maritime and land-based commerce.

---

## 🏛️ Project Architecture: The 50-Problem Roadmap

Version **1.3.0** marks the transition from a specialized thermal tool to a comprehensive physics engine. All five core domains are now **Active**, populating the library with the first 50 essential problem-solvers for global trade.

| Category | Domain | Status | Scope |
| :--- | :--- | :--- | :--- |
| **I** | **Thermodynamics** | ✅ **Active** | Problems 1-10 (Moisture, Heat, PCM) |
| **II** | **Fluid Dynamics** | ✅ **Active** | Problems 11-20 (Drag, Cavitation, Siltation) |
| **III** | **Mechanical** | ✅ **Active** | Problems 21-30 (Stress, Torque, Wind Tech) |
| **IV** | **Logistics** | ✅ **Active** | Problems 31-40 (Platooning, Docking, Routing) |
| **V** | **Strategic** | ✅ **Active** | Problems 41-50 (ROI, Risk, Game Theory) |

---

## 🚀 Key Features (v1.3.0 Expansion)

The library now supports multi-domain arbitration across the following engines:

* **Thermo (Category I):** Mass Deconvolution (ASABE D245.7), Container Rain Prediction, and Perishable Respiration models.
* **Fluids (Category II):** **Hull Skin Friction** analysis for bio-fouling, **Propeller Cavitation** erosion risk, and **Port Siltation** depth impact on cargo capacity.
* **Mechanical (Category III):** **Wind-Assisted Propulsion** (Sails/Rotors) force calculation, **Shaft Torque** monitoring, and **Hull Stress** analysis.
* **Logistics (Category IV):** **Aerodynamic Drafting** (Truck/Ship Platooning) fuel savings and optimized **Dry-Docking** scheduling.
* **Strategic (Category V):** **Economical Speed** optimization, **Strategic Reserve** utilization, and **Market Volatility** hedging.

---

##🛠 Usage: The "Any Port" Arbitrator
To bypass localized data naming conventions, use the v1.3.0 mapping bridge:

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


FluidsArbitrator Technical Documentation

Overview

The FluidsArbitrator class is a high-fidelity simulation engine designed for maritime logistics and naval architecture. It calculates complex fluid interactions, including hull resistance, stability effects, and environmental depth monitoring.1. Core Environmental ConstantsThe class initializes with standard physical constants for maritime environments:Seawater Density ($\rho_{sw}$): $1025.0$ $kg/m^3$Gravity ($g$): $9.81$ $m/s^2$2. Methodology & Implementation

FluidsArbitrator: Complete Technical Reference
1. estimate_hull_skin_friction
Estimates the drag increase caused by bio-fouling (marine growth) on the hull.

Order: (velocity, wetted_area, bio_fouling_index)

Example: arbitrator.estimate_hull_skin_friction(10.5, 2500.0, 0.15)

2. model_free_surface_effect
Calculates the virtual rise in the center of gravity caused by liquid moving in partially filled tanks.

Order: (tank_width, tank_length, fluid_density)

Example: arbitrator.model_free_surface_effect(12.0, 30.0, 850.0)

3. predict_propeller_cavitation
Predicts if bubbles will form and collapse on propeller blades (threshold < 0.3).

Order: (p_static, p_vapor, tip_speed)

Example: arbitrator.predict_propeller_cavitation(101325.0, 2338.0, 40.0)

4. optimize_trim_draft
Calculates the most fuel-efficient longitudinal angle (trim) for the hull.

Order: (displacement, lcb_position, vcg)

Example: arbitrator.optimize_trim_draft(65000.0, 135.0, 14.5)

5. calculate_ballast_displacement
Determines the mass of water needed to reach a specific target draft.

Order: (target_draft, current_displacement)

Example: arbitrator.calculate_ballast_displacement(9.5, 58000.0)

6. simulate_wave_resistance
Uses the Froude Number to simulate energy lost to wave creation at specific speeds.

Order: (velocity, hull_length)

Example: arbitrator.simulate_wave_resistance(14.0, 220.0)

7. model_air_lubrication
Calculates friction reduction from a layer of micro-bubbles under the hull.

Order: (air_flow_rate, hull_surface)

Example: arbitrator.model_air_lubrication(4.5, 1800.0)

8. monitor_port_siltation
Predicts safe depth remaining after sediment buildup over time.

Order: (baseline_depth, silt_rate_daily, days)

Example: arbitrator.monitor_port_siltation(16.0, 0.02, 60)

9. resolve_bernoulli_pressure
Resolves fluid pressure between two points based on velocity and elevation changes.

Order: (p1, v1, h1, v2, h2)

Example: arbitrator.resolve_bernoulli_pressure(120000.0, 1.5, 5.0, 3.0, 2.0)

10. calculate_reynolds_number
Determines if the water flow around the hull is laminar or turbulent.

Order: (velocity, length, kinematic_viscosity)

Example: arbitrator.calculate_reynolds_number(12.0, 200.0, 0.00000105)



Category,Functions
Resistance,"estimate_hull_skin_friction, simulate_wave_resistance, model_air_lubrication"
Stability,"model_free_surface_effect, optimize_trim_draft, calculate_ballast_displacement"
Physics/Flow,"predict_propeller_cavitation, resolve_bernoulli_pressure, calculate_reynolds_number"
Environment,monitor_port_siltation

This documentation covers the ThermoArbitrator class, which handles thermodynamics, heat transfer, and cargo preservation calculations.

ThermoArbitrator Technical Documentation
1. predict_container_rain
Calculates the dew point within a shipping container and determines if "container rain" (condensation) will occur based on the surface temperature.

Parameters:

temp_air (float): Ambient air temperature in degrees Celsius ( 
∘
 C).

rh (float): Relative humidity as a percentage (0−100%).

temp_surface (float): The temperature of the container's inner ceiling/walls ( 
∘
 C).

Example Call:

Python
# Air: 30°C, Humidity: 80%, Surface: 22°C

result = ThermoArbitrator.predict_container_rain(30.0, 80.0, 22.0)

2. solve_ghost_weight
Calculates the dry mass of a cargo load (Mass Deconvolution) by determining the Equilibrium Moisture Content (EMC).Parameters:mass (float): Current total mass of the cargo in kilograms ($kg$).moisture (float): Current moisture content (decimal, e.g., $0.15$ for $15\%$).rh (float): Ambient relative humidity ($0-100\%$).temp_c (float): Ambient temperature ($^\circ C$).material (str): Type of cargo (e.g., "Cotton", "Timber").std (str): Standards set to use (e.g., "ASABE", "ASTM").Example Call:Pythonarbitrator = ThermoArbitrator()
result = arbitrator.solve_ghost_weight(5000.0, 0.12, 65.0, 25.0, "Cotton", "ASABE")

3. respiration_heatEstimates the heat energy generated by living produce during transit.Parameters:mass_kg (float): Total mass of the product ($kg$).product (str): Product name (e.g., "Apple", "Banana", "Strawberry").Example Call:Pythonheat_watts = ThermoArbitrator.respiration_heat(2000.0, "Banana")

4. pcm_requirement

Calculates the amount of Phase Change Material (PCM) needed to maintain temperature over a duration.Parameters:hours (float): Required duration of temperature maintenance ($h$).leak_watts (float): Calculated heat leakage rate of the container ($W$).Example Call:


# Maintain for 48 hours with 50W leakage
kg_needed = ThermoArbitrator.pcm_requirement(48.0, 50.0)

5. insulation_decay

Predicts the degradation of insulation R-value over time due to environmental factors.Parameters:r_init (float): Initial R-value of the insulation.weeks (float): Time elapsed since installation ($weeks$).Example Call:

current_r = ThermoArbitrator.insulation_decay(5.0, 52.0)

6. ethylene_diffusionCalculates the rate of ethylene gas spread, critical for preventing over-ripening of produce.Parameters:gradient (float): The concentration gradient of the gas.area (float): Surface area through which diffusion occurs ($m^2$).Example Call:

diff_rate = ThermoArbitrator.ethylene_diffusion(0.05, 2.5)

7. sublimation_loss

Calculates mass lost to sublimation, typically used for dry ice cooling systems.Parameters:area (float): Exposed surface area of the solid ($m^2$).vp_diff (float): Vapor pressure difference.hours (float): Duration of exposure ($h$).Example Call:

kg_lost = ThermoArbitrator.sublimation_loss(0.5, 12.0, 24.0)

8. thermal_bridgeCalculates the heat flow through structural "leaks" or bridges in the container.Parameters:temp_delta (float): Temperature difference between inside and outside ($\Delta T$).area (float): Cross-sectional area of the bridge ($m^2$).Example Call:

heat_loss = ThermoArbitrator.thermal_bridge(15.0, 0.02)

9. solar_gainEstimates the thermal energy absorbed by a container from direct sunlight.Parameters:irradiance (float): Solar radiation intensity ($W/m^2$).area (float): Exposed surface area (roof/sides) ($m^2$).Example Call:

watts_gained = ThermoArbitrator.solar_gain(800.0, 30.0)

10. vip_statusChecks the integrity of Vacuum Insulated Panels (VIP) based on internal pressure.Parameters:pressure (float): Internal panel pressure (typically in $mbar$ or $Pa$).Example Call:

# Status returns "INTACT" if pressure <= 0.5
status = ThermoArbitrator.vip_status(0.2)

Function,Unit of Input 1,Unit of Input 2,Result Unit
Respiration,kg,Product Name,W
PCM Req.,hours,W,kg
Solar Gain,W/m2,m2,W
Sublimation,m2,ΔP,kg
Diffusion,Gradient,m2,Flow Rate

MechanicalArbitrator Technical DocumentationThe MechanicalArbitrator class manages hardware-level simulations, structural safety checks, and auxiliary energy calculations.

1. calculate_wind_propulsionCalculates the net force generated by wind-assisted propulsion (sails or rotors) based on air density and relative wind angle.Parameters:wind_speed (float): Velocity of the wind ($m/s$).sail_area (float): Surface area of the sail/rotor ($m^2$).angle (float): Relative wind angle (degrees).Example Call:Python# Wind: 15.0 m/s, Sail: 50.0 m2, Angle: 30 degrees
force_n = mech.calculate_wind_propulsion(15.0, 50.0, 30.0)

2. evaluate_propeller_erosionPredicts material degradation on propeller blades caused by the collapse of cavitation bubbles.Parameters:cav_hours (float): Cumulative hours operating under cavitation.intensity (float): Cavitation intensity index.Example Call:Python# 120 hours of operation at intensity 5.5
loss_val = mech.evaluate_propeller_erosion(120.0, 5.5)

3. monitor_shaft_torqueCalculates the rotational moment (Torque) applied to the primary drive shaft.Parameters:power_kw (float): Power output in kilowatts ($kW$).rpm (float): Revolutions per minute ($RPM$).Example Call:Python# 5000 kW at 120 RPM
torque_nm = mech.monitor_shaft_torque(5000.0, 120.0)

4. check_structural_integrityA safety check ensuring that hull stress remains within the defined safety limit ($\leq 250.0$ $MPa$).Parameters:trim_angle (float): The current pitch angle of the ship.load_stress (float): The raw stress measured on the hull ($MPa$).Example Call:Python# Returns True if safe, False if stress exceeds 250.0 MPa
is_safe = mech.check_structural_integrity(5.0, 210.0)

5. auxiliary_power_demandAggregates the total electrical load required for active non-propulsion systems.Parameters:air_systems_active (int): Number of active air handling units ($50$ $kW$ each).ballast_pumps (int): Number of active ballast pumps ($120$ $kW$ each).Example Call:Python# 4 air units and 2 pumps active
total_kw = mech.auxiliary_power_demand(4, 2)

6. calculate_gearbox_efficiencyMonitors power transmission health by comparing heat loss to total input power.Parameters:heat_loss (float): Energy dissipated as heat ($kW$).input_power (float): Total power entering the gearbox ($kW$).Example Call:Python# 15 kW lost out of 1000 kW input
efficiency = mech.calculate_gearbox_efficiency(15.0, 1000.0)

7. simulate_rudder_torqueCalculates the mechanical torque required to adjust or hold the rudder during maneuvers.Parameters:water_velocity (float): Speed of water flow past the rudder ($m/s$).rudder_angle (float): Angle of the rudder (degrees).Example Call:Python# Water at 8.0 m/s with a 25 degree rudder angle
rudder_nm = mech.simulate_rudder_torque(8.0, 25.0)

8. actuator_response_timePredicts the mechanical latency in hydraulic or mechanical adjustment systems.Parameters:pressure (float): System hydraulic pressure ($bar$).load (float): The physical weight being moved ($kg$).Example Call:

Example Call:Python# 200 bar pressure moving a 1500 kg load
latency_sec = mech.actuator_response_time(200.0, 1500.0)

9. material_fatigue_indexCalculates a wear score for the hull or propeller based on stress cycles.Parameters:cycles (float): Number of loading cycles (in millions).stress_range (float): The range of stress applied ($MPa$).Example Call:Python# 1.2 million cycles at 85.0 MPa range
fatigue_score = mech.material_fatigue_index(1.2, 85.0)

10. calibrate_sensor_offsetAdjusts raw sensor readings to account for the thermal expansion of metal components.Parameters:raw_val (float): The uncorrected sensor reading.environmental_temp (float): Ambient temperature ($^\circ C$).Example Call:Python# Corrects a raw value of 102.4 at 35°C
calibrated_val = mech.calibrate_sensor_offset(102.4, 35.0)

Function Category,Function Name,Primary Unit,Return Type
Wind Propulsion,calculate_wind_propulsion,m/s,Force (N)
Shaft Dynamics,monitor_shaft_torque,RPM,Torque (Nm)
Structural Safety,check_structural_integrity,MPa,Boolean (Pass/Fail)
Efficiency,calculate_gearbox_efficiency,kW,Float (Ratio)
Maintenance,material_fatigue_index,Cycles (M),Index Score
Steering,simulate_rudder_torque,m/s,Torque (Nm)
Sensors,calibrate_sensor_offset,∘C,Adjusted Float

LogisticsArbitrator Technical DocumentationThe LogisticsArbitrator orchestrates convoy efficiency, scheduling, and drafting logistics.1. calculate_platoon_savingsCalculates aerodynamic/hydrodynamic fuel savings based on the distance between vehicles or vessels in a convoy.Parameters:gap_meters (float): Distance between units ($m$). Savings are $0$ if gap $> 20m$.vehicle_count (int): Total number of units in the platoon.Example Call:Python# 3 vessels with a 10m gap
pct_saved = arbitrator.calculate_platoon_savings(10.0, 3)

2. schedule_dry_dockDetermines docking priority based on efficiency loss from hull fouling.Parameters:efficiency_loss (float): Measured drop in performance.threshold (float): Limit at which maintenance is required.Example Call:Python# Returns True if 12% loss exceeds a 10% threshold
must_dock = arbitrator.schedule_dry_dock(0.12, 0.10)

3. optimize_convoy_configurationStrategic placement of vessels to maximize fleet-wide drafting efficiency based on fuel costs.Parameters:vessel_speeds (list): Max speeds of vessels.fuel_costs (list): Fuel burn costs per vessel.Example Call:Python# Returns indices of vessels sorted by cost
optimal_order = arbitrator.optimize_convoy_configuration([12, 15, 13], [300, 500, 350])

4. resolve_berth_priorityMatches vessel draft needs to real-time harbor depth/siltation.Parameters:draft_req (float): Required depth for the vessel ($m$).current_siltation (float): Actual harbor depth available ($m$).Example Call:Python# Check if 8.5m draft fits in 9.0m depth
is_safe = arbitrator.resolve_berth_priority(8.5, 9.0)

5. calculate_bunker_refuel_windowPredicts the fuel exhaustion point for refueling logistics.Parameters:consumption_rate (float): Units of fuel burned per hour.reserve (float): Total fuel currently on board.Example Call:

Python# 30 units left / 1.5 units per hour
hours_remaining = arbitrator.calculate_bunker_refuel_window(1.5, 30.0)

6. evaluate_route_riskBalances environmental force inputs (wave resistance vs. wind propulsion) for routing.Parameters:wave_resistance_data (float): Resistance data from sea state.wind_propulsion (float): Estimated force from wind assist.Example Call:Pythonrisk_score = arbitrator.evaluate_route_risk(0.8, 0.4)

7. manifest_weight_distributionStandardizes weight across sectors to ensure longitudinal trim safety.Parameters:total_cargo (float): Total mass ($kg$).sectors (int): Number of storage sections.Example Call:Pythonweight_per_bay = arbitrator.manifest_weight_distribution(50000.0, 5)

8. predict_delivery_latencyAdjusts ETA based on environmental and mechanical drag factors.Parameters:weather_factor (float): Environmental delay multiplier.speed_loss (float): Velocity reduction due to drag.Example Call:Pythonlatency_multiplier = arbitrator.predict_delivery_latency(1.2, 0.1)

9. cost_benefit_air_lubricationStrategic ROI analysis on micro-bubble system deployment.Parameters:installation_cost (float): CAPEX cost of the system.fuel_saved (float): Expected monetary savings in fuel.

10. optimize_dead_weightAggregates non-revenue mass to minimize total displacement.Parameters:ballast (float): Ballast water mass ($kg$).fuel (float): Remaining fuel mass ($kg$).cargo (float): Payload mass ($kg$).Example Call:Pythontotal_displacement = arbitrator.optimize_dead_weight(5000.0, 2000.0, 15000.0)


Function,Primary Input,Unit/Type,Logic Basis
Platoon Savings,gap_meters,m,Aerodynamic Drafting
Dry Dock,efficiency_loss,Float (%),Threshold Maintenance
Berth Priority,draft_req,m,Depth vs. Siltation
Bunker Window,reserve,Float,Consumption Prediction
Dead Weight,ballast/fuel/cargo,kg,Displacement Sum

Function,Decision Type,Key Metric,Result Type
Docking Strategy,Financial,Fuel vs. Cleaning,Boolean
Platoon Feasibility,Risk,Vessel Count / Safety,Boolean
Port Entry,Safety,Draft vs. Clearance,Boolean
Innovation Budget,R&D,ROI Comparison,String (Target)
Lifecycle Forecast,Asset Mgmt,Wear / Age,Float (Forecast)

StrategicArbitrator Technical Documentation
1. resolve_docking_strategy
Performs a financial trade-off analysis to determine if the cost of a dry-dock cleaning is offset by the fuel savings from reduced hull friction.

Order: (fuel_cost, cleaning_cost, drag_inc)

Example:

Python
# Fuel: $800/ton, Cleaning: $15,000, Drag Increase: 0.25 (25%)
should_dock = arbitrator.resolve_docking_strategy(800.0, 15000.0, 0.25)
2. evaluate_platoon_feasibility
Determines if a convoy should be formed based on fleet size and environmental safety thresholds.

Order: (vessel_count, route_safety)

Example:

Python
# 4 vessels available, Route safety index of 0.85
is_feasible = arbitrator.evaluate_platoon_feasibility(4, 0.85)
3. optimize_economical_speed
Calculates the most profitable speed by weighing freight revenue against exponential fuel consumption increases.

Order: (freight_rate, consumption_rate)

Example:

Python
# Rate: $50/unit, Base Consumption: 2.5 units/hour
eco_speed = arbitrator.optimize_economical_speed(50.0, 2.5)

4. port_entry_authorizationA safety gatekeeper that compares current vessel draft against harbor depth, including a $0.5m$ safety buffer.Order: (current_draft, siltation_clearance)Example:Python# Vessel Draft: 9.2m, Available Depth: 10.0m
can_enter = arbitrator.port_entry_authorization(9.2, 10.0)
5. allocate_innovation_budgetDirects capital expenditure (CAPEX) to the technology (Air Lubrication vs. Wind Propulsion) with the highest simulated ROI.Order: (air_lub_roi, wind_prop_roi)Example:Python# AirLub ROI: 18%, WindProp ROI: 14%
target_tech = arbitrator.allocate_innovation_budget(0.18, 0.14)
6. risk_assessment_cavitationCalculates a risk-to-reward ratio for operating propellers in cavitation-heavy regimes to gain speed.Order: (efficiency_gain, maintenance_cost)Example:Python# Gain: $5,000 in time saved, Repair cost: $2,000
risk_ratio = arbitrator.risk_assessment_cavitation(5000.0, 2000.0)

7. fleet_stability_index

Aggregates trim and ballast data into a single health metric for fleet-wide safety.Order: (avg_trim, ballast_utilization)Example:Python# Avg Trim: 2.5 degrees, Ballast used: 0.4 (40%)
fleet_health = arbitrator.fleet_stability_index(2.5, 0.4)

8. carbon_credit_valuationConverts fuel savings into monetary value based on a standard $50.0$ USD per ton carbon credit rate.Order: (fuel_saved_platooning, wind_offset)Example:Python# Saved 120 tons via platooning, 45 tons via wind
credit_value_usd = arbitrator.carbon_credit_valuation(120.0, 45.0)

9. infrastructure_lifecycle_forecastPredicts the remaining percentage of useful life for mechanical assets.Order: (wear_index, age)Example:Python# Wear Score: 35/100, Asset Age: 8 years
life_left_pct = arbitrator.infrastructure_lifecycle_forecast(35.0, 8.0)

10. global_priority_updateUpdates the internal priority matrix by summing live states across all fleet subsystems.Order: (system_states)Example:Python# Dictionary of binary system states (1 = Issue, 0 = OK)
current_states = {"mechanical": [1, 0, 0], "fluids": [0, 1], "logistics": [1]}
arbitrator.global_priority_update(current_states)

Function,Unit / Type 1,Unit / Type 2,Output
Docking,Price ($/ton),Cost ($),Boolean
Platoon,Count,Index (0-1),Boolean
Authorization,Draft (m),Depth (m),Boolean
Budget,ROI (%),ROI (%),"""AirLub"" / ""WindProp"""
Carbon,Tonnes,Tonnes,USD ($)

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
