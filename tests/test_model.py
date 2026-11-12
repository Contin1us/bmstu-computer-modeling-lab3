import math

from src.model import calculate_reliability


def test_calculate_reliability():
    lam = 0.0005
    t = 5

    result = calculate_reliability(lam, t)

    expected = math.exp(-lam * t)

    assert result == expected