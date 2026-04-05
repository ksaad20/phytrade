"""
SPTS: Standardized Physics-Trade Schema
"""

class Schema:
    # Constants
    MAX_VESSEL_VELOCITY_KNOTS = 40.0
    MIN_MASS_KG = 1.0
    MAX_HUMIDITY_PERCENT = 100.0
    MAX_ENTROPY_DELTA = 5.0

    @staticmethod
    def validate_telemetry(mass: float, velocity: float, humidity: float = None):
        if mass < Schema.MIN_MASS_KG:
            return False, "Invalid Mass: Below physical trade limit."
        if velocity > Schema.MAX_VESSEL_VELOCITY_KNOTS:
            return False, "Invalid Velocity: Exceeds physical hull limits."
        if humidity is not None:
            if humidity < 0 or humidity > Schema.MAX_HUMIDITY_PERCENT:
                return False, "Invalid Environment: Humidity out of bounds."
        return True, "Data Physically Validated"

# Add this line to fix the AgnosticMapper error
PhysicalConstraints = Schema
