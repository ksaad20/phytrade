from pathlib import Path

import pandas as pd

from .schema import PhysicalConstraints


class Mapper:
    """
    Commercial Bridge: Maps external port data (CSV/JSON)
    to the PhyTrade Physical Schema.
    """

    def __init__(self, column_mapping: dict[str, str]):
        # Example:
        # {
        #     "Ship_WT": "mass",
        #     "SOG": "velocity",
        #     "Time_Delta": "delta_t",
        # }
        self.mapping = column_mapping

    def map_and_validate(
        self,
        raw_data_path: str | Path,
    ) -> tuple[pd.DataFrame, list[dict[str, object]]]:
        """
        Load external port data, map terminology into physics
        variables, and validate against physical constraints.
        """

        # 1. Load raw port data
        df = pd.read_csv(raw_data_path)

        # 2. Translate local port terms to physics terms
        mapped_df = df.rename(columns=self.mapping)

        results: list[dict[str, object]] = []

        for index, row in mapped_df.iterrows():
            # 3. Validate against Physics Constraints
            # (Institutional Grade)
            is_valid, message = (
                PhysicalConstraints.validate_telemetry(
                    mass=row.get("mass", 0),
                    velocity=row.get("velocity", 0),
                    humidity=row.get("humidity", None),
                )
            )

            results.append(
                {
                    "row": index,
                    "valid": is_valid,
                    "status": message,
                }
            )

        return mapped_df, results
