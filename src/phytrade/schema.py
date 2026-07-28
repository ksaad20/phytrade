class Schema:
    MIN_MASS_KG = 0
    MAX_VESSEL_VELOCITY_KNOTS = 40
    MAX_HUMIDITY_PERCENT = 100

    @staticmethod
    def validate_telemetry(mass: float, velocity: float, humidity: float | None = None):
    
    
        if mass < Schema.MIN_MASS_KG:
            return False, "Invalid Mass: Below physical trade limit."

        if velocity > Schema.MAX_VESSEL_VELOCITY_KNOTS:
            return False, "Invalid Velocity: Exceeds physical hull limits."

        if humidity is not None and (
            humidity < 0
            or humidity > Schema.MAX_HUMIDITY_PERCENT
        ):
            return False, "Invalid Environment: Humidity out of bounds."

        return True, "Data Physically Validated"
