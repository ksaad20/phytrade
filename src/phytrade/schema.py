"""
SPTS: Standardized Physics-Trade Schema
Defines the physical boundaries for valid trade arbitration.
"""

class schema:
    # Constants for global maritime/commodity trade
    MAX_VESSEL_VELOCITY_KNOTS = 40.0  # Physical limit for cargo ships
    MIN_MASS_KG = 1.0                # Smallest tradeable unit
    MAX_HUMIDITY_PERCENT = 100.0     # Environmental limit for commodity storage
    MAX_ENTROPY_DELTA = 5.0          # Maximum allowable 'disorder' before system failure

    @staticmethod
    def validate_telemetry(mass, velocity, humidity=None):
        """
        Validates if the incoming trade data is physically possible.
        Returns (True, "Success") or (False, "Error Message").
        """
        if mass < PhysicalConstraints.MIN_MASS_KG:
            return False, "Invalid Mass: Below physical trade limit."
        
        if velocity > (PhysicalConstraints.MAX_VESSEL_VELOCITY_KNOTS * 0.51444): # Convert to m/s
            return False, "Invalid Velocity: Exceeds physical hull limits."
            
        if humidity and (humidity < 0 or humidity > PhysicalConstraints.MAX_HUMIDITY_PERCENT):
            return False, "Invalid Environment: Humidity out of bounds."
            
        return True, "Data Physically Validated"

# This will be used by the 'AgnosticMapper' in the next step.
