import math

# Интенсивности отказов компонентов
lambda_sensor = 0.0005
lambda_computer = 1 / 3000
lambda_actuator = 1 / 1500


# Надёжность системы без резервирования
def calculate_reliability_without_reserve(t):

    reliability = math.exp(
        -(lambda_sensor + lambda_computer + lambda_actuator) * t
    )

    return reliability


# Надёжность системы с резервированием
def calculate_reliability_with_reserve(t):

    reliability_sensor = 1 - (
        1 - math.exp(-lambda_sensor * t)
    ) ** 2

    reliability_computer = 1 - (
        1 - math.exp(-lambda_computer * t)
    ) ** 2

    reliability_actuator = math.exp(-lambda_actuator * t)

    reliability = (
        reliability_sensor
        * reliability_computer
        * reliability_actuator
    )

    return reliability