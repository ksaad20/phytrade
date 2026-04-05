import pandas as pd
from .schema import PhysicalConstraints  # Added the dot (.) for package relative import

class Mapper:  # Renamed from AgnosticMapper to match our __init__.py 'Engine' style
    """
    Commercial Bridge: Maps any external port data (CSV/JSON)
    to the PhyTrade Physical Schema.
    """
    def __init__(self, column_mapping: dict):
        # Example: {"Ship_WT": "mass", "SOG": "velocity", "Time_Delta": "delta_t"}
        self.mapping = column_mapping

    def map_and_validate(self, raw_data_path: str):
        # 1. Load raw port data
        df = pd.read_csv(raw_data_path)
        
        # 2. Translate local port terms to Physics terms
        mapped_df = df.rename(columns=self.mapping)
        
        results = []
        for index, row in mapped_df.iterrows():
            # 3. Validate against the Physics Constraints (Institutional Grade)
            is_valid, msg = PhysicalConstraints.validate_telemetry(
                mass=row.get('mass', 0),
                velocity=row.get('velocity', 0),
                humidity=row.get('humidity', None)
            )
            results.append({"row": index, "valid": is_valid, "status": msg})
            
        return mapped_df, results
