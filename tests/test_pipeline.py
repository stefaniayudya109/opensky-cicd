import pytest
from src.transform import transform_states
from src.validate import validate_flight_data


def test_transform_and_validate_sample_payload():
    sample_payload = {
        "time": 1732417200,
        "states": [
            [
                "8a0123", "GIA402  ", "Indonesia", 1732417198, 1732417199,
                106.6559, -6.1256, 10058.4, False, 230.5, 95.0, 0.0,
                None, 10300.0, "1234", False, 0
            ]
        ]
    }
    df = transform_states(sample_payload)
    assert len(df) == 1
    assert df.loc[0, "callsign"] == "GIA402"
    assert validate_flight_data(df) is True


def test_validate_invalid_coordinates():
    bad_payload = {
        "time": 1732417200,
        "states": [
            [
                "8a0123", "GIA402", "Indonesia", 1732417198, 1732417199,
                250.0, -95.0, 10058.4, False, 230.5, 95.0, 0.0,
                None, 10300.0, "1234", False, 0
            ]
        ]
    }
    df = transform_states(bad_payload)
    with pytest.raises(ValueError):
        validate_flight_data(df)