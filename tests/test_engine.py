from phytrade.engine import Engine


def test_calculate_dispute_value() -> None:
    engine = Engine()

    result = engine.calculate_dispute_value(
        mass=100.0,
        velocity=10.0,
        delta_t=5.0,
        contract_value=50_000.0,
    )

    assert result["momentum"] == 1_000.0
    assert result["energy"] == 5_000.0
    assert result["displacement"] == 50.0
    assert result["contract_value"] == 50_000.0
