import math

from src.monte_carlo import (
    lambda_sensor,
    lambda_computer,
    lambda_actuator,
    simulate_system,
    simulate_system_without_reserve
)


def test_simulate_system():
    N = 100
    t = 5

    reliability, success, failure = simulate_system(N, t)

    assert success + failure == N
    assert reliability == success / N
    assert 0 <= reliability <= 1


def test_simulate_system_without_reserve():
    N = 100000
    t = 5

    reliability, success, failure = simulate_system_without_reserve(N, t)

    # Проверка количества испытаний
    assert success + failure == N

    # Проверка границ надёжности
    assert 0 <= reliability <= 1

    # Проверка соответствия оценки аналитическому значению
    analytical = math.exp(
        -(lambda_sensor + lambda_computer + lambda_actuator) * t
    )

    assert abs(reliability - analytical) < 0.001