from typing import Any

import numpy as np


class Engine:
    def __init__(self, mapper=None, schema=None):
        self.mapper = mapper
        self.schema = schema

    def calculate_dispute_value(
        self,
        mass: float,
        velocity: float,
        delta_t: float,
        contract_value: float,
    ) -> dict[str, Any]:
        """Pure Physics Layer - No Imports Allowed Here."""

        momentum = mass * velocity
        energy = 0.5 * mass * velocity**2
        displacement = velocity * delta_t

        return {
            "momentum": momentum,
            "energy": energy,
            "displacement": displacement,
            "contract_value": contract_value,
        }

    def process_port_data(
        self,
        raw_data: dict[str, Any],
    ) -> dict[str, Any]:
        from .mapper import Mapper
        from .schema import Schema

        local_schema = self.schema if self.schema else Schema()
        local_mapper = self.mapper if self.mapper else Mapper()

        validated = local_schema.validate(raw_data)

        if validated:
            return local_mapper.map(raw_data)

        return {"status": "invalid"}
