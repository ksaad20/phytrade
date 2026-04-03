import math

class MechanicalArbitrator:
    """
    Manages propulsion hardware, structural stress, and auxiliary wind tech.
    """
    def __init__(self):
        self.air_density = 1.225 # kg/m^3

    def calculate_wind_propulsion(self, wind_speed, sail_area, angle):
        """[19] Wind-Assisted Propulsion: Net force from sails/rotors."""
        force_total = 0.5 * self.air_density * (wind_speed**2) * sail_area * 1.5
        return force_total * math.cos(math.radians(angle))

    def evaluate_propeller_erosion(self, cav_hours, intensity):
        """[14 Mechanical] Predicts material loss due to bubble collapse."""
        return cav_hours * (intensity ** 2) * 0.001

    def monitor_shaft_torque(self, power_kw, rpm):
        """Calculates rotational force on the primary drive shaft."""
        if rpm == 0: return 0
        return (power_kw * 9550) / rpm

    def check_structural_integrity(self, trim_angle, load_stress):
        """Ensures hull stress is within safety limits during optimization."""
        effective_stress = load_stress / math.cos(trim_angle)
        return effective_stress < 250.0 # MPa limit example

    def auxiliary_power_demand(self, air_systems_active, ballast_pumps):
        """Calculates total load for non-propulsion systems."""
        return (air_systems_active * 50) + (ballast_pumps * 120)

    def calculate_gearbox_efficiency(self, heat_loss, input_power):
        """Monitors friction-related power loss in mechanical transmission."""
        return (input_power - heat_loss) / input_power

    def simulate_rudder_torque(self, water_velocity, rudder_angle):
        """Mechanical load on steering gear during maneuvers."""
        return 0.5 * 1025 * (water_velocity**2) * math.sin(math.radians(rudder_angle))

    def actuator_response_time(self, pressure, load):
        """Predicts mechanical latency in trim/ballast adjustment."""
        return load / (pressure * 0.8)

    def material_fatigue_index(self, cycles, stress_range):
        """Long-term wear tracking for hull and propeller components."""
        return cycles * (stress_range ** 3)

    def calibrate_sensor_offset(self, raw_val, environmental_temp):
        """Adjusts mechanical readings for thermal expansion."""
        return raw_val * (1 + (environmental_temp * 0.000012))
