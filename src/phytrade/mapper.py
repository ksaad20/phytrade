import pandas as pd
from .schema import PhysicalConstraints

class AgnosticMapper:
    """
    Commercial Bridge: Maps any external trade data (CSV/JSON) 
    to the PhyTrade Physical Schema.
    """
    def __init__(self, column_mapping: dict):
        """
        :param column_mapping: Dictionary mapping User Columns to Physics Constants.
                               Example: {"Ship_WT": "mass", "SOG": "velocity"}
        """
        self.mapping = column_mapping

    def map_and_validate(self, raw_data_path: str):
        """
        1. Loads raw port data.
        2. Renames columns to internal physics constants.
        3. Runs the PhysicalConstraints check on every row.
        """
        df = pd.read_csv(raw_data_path)
        
        # Translate local terms to Physics terms
        mapped_df = df.rename(columns=self.mapping)
        
        results = []
        for index, row in mapped_df.iterrows():
            # Validate row against the PhysicalConstraints from Step #1
            is_valid, msg = PhysicalConstraints.validate_telemetry(
                mass=row.get('mass', 0),
                velocity=row.get('velocity', 0),
                humidity=row.get('humidity', None)
            )
            results.append({"row": index, "valid": is_valid, "status": msg})
            
        return mapped_df, results

# Commercial Use Example:
# mapper = AgnosticMapper({"Vessel_Displacement": "mass", "Current_Speed": "velocity"})
# clean_data, report = mapper.map_and_validate("matarbari_logs.csv")
