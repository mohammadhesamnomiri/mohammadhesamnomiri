def parse_measurement(raw: str, max_distance: float = 250.0):
    """Parse Arduino CSV output: angle,distance_cm."""
    if not raw or "," not in raw:
        return None
    try:
        angle, distance = map(float, raw.strip().split(",", 1))
    except ValueError:
        return None
    if not 0 <= angle <= 180 or not 0 <= distance <= max_distance:
        return None
    return angle, distance
