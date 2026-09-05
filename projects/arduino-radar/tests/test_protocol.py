from radar_utils import parse_measurement


def test_valid_measurement():
    assert parse_measurement("90,42.5") == (90.0, 42.5)


def test_invalid_csv_is_rejected():
    assert parse_measurement("hello") is None
    assert parse_measurement("90") is None
    assert parse_measurement("x,42") is None


def test_out_of_range_measurement_is_rejected():
    assert parse_measurement("-1,20") is None
    assert parse_measurement("181,20") is None
    assert parse_measurement("90,251") is None
