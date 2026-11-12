import math

# Среднее время безотказной работы компонентов

mttf_sensor = 2000
mttf_computer = 3000
mttf_actuator = 1500
# Интенсивности отказов компонентов

lambda_sensor = 1 / mttf_sensor
lambda_computer = 1 / mttf_computer
lambda_actuator = 1 / mttf_actuator


print("Интенсивности отказов:")

print(f"Датчик: {lambda_sensor}")
print(f"Вычислитель: {lambda_computer}")
print(f"Исполнительный механизм: {lambda_actuator}")


t = 5


def calculate_reliability(lam, t):
    reliability = math.exp(-lam * t)
    return reliability


reliability_sensor = calculate_reliability(lambda_sensor, t)
reliability_computer = calculate_reliability(lambda_computer, t)
reliability_actuator = calculate_reliability(lambda_actuator, t)

print(f"Надёжность датчика за {t} часов: {reliability_sensor:.6f}")
print(f"Надёжность вычислителя за {t} часов: {reliability_computer:.6f}")
print(f"Надёжность исполнительного механизма за {t} часов: {reliability_actuator:.6f}")


# Надёжность резервированных подсистем


def calculate_redundant_reliability(reliability):
    result = 1 - (1 - reliability) ** 2
    return result

reliability_sensor_reserve = calculate_redundant_reliability(reliability_sensor)
reliability_computer_reserve = calculate_redundant_reliability(reliability_computer)


print(f"Надёжность пары датчиков: {reliability_sensor_reserve:.6f}")
print(f"Надёжность пары вычислителей: {reliability_computer_reserve:.6f}")


def calculate_system_reliability(sensor, computer, actuator):
    reliability = sensor * computer * actuator
    return reliability


reliability_system = calculate_system_reliability(
    reliability_sensor,
    reliability_computer,
    reliability_actuator
)


print(f"Надёжность системы без резервирования за {t} часов: {reliability_system:.6f}")
# Расчёт надёжности системы с резервированием

reliability_system_reserve = calculate_system_reliability(
    reliability_sensor_reserve,
    reliability_computer_reserve,
    reliability_actuator
)

print(f"Надёжность системы с резервированием: {reliability_system_reserve:.6f}")


difference = reliability_system_reserve - reliability_system
print(f"Увеличение надёжности: {difference:.6f}")