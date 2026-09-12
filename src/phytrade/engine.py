from typing import Any


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
        local_mapper = self.mapper if self.mapper else Mapper({})

        validated, message = local_schema.validate_telemetry(
            mass=float(raw_data.get("mass", 0)),
            velocity=float(raw_data.get("velocity", 0)),
            humidity=(
                float(raw_data["humidity"])
                if raw_data.get("humidity") is not None
                else None
            ),
        )

        if validated:
            return {
                "status": "valid",
                "message": message,
                "data": raw_data,
            }

        return {
            "status": "invalid",
            "message": message,
        }
