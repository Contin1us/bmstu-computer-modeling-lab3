
import math

from src.visualization import plot_convergence, plot_reliability
from src.monte_carlo import (
    simulate_system,
    lambda_sensor,
    lambda_computer,
    lambda_actuator
)

# Продолжительность моделирования
t = 5

# Количество испытаний для каждого эксперимента
N_values = [100, 1000, 10000, 100000, 1000000]


# Аналитический расчёт надёжности

# Надёжность пары резервированных датчиков
R_sensor = 1 - (1 - math.exp(-lambda_sensor * t)) ** 2

# Надёжность пары резервированных вычислителей
R_computer = 1 - (1 - math.exp(-lambda_computer * t)) ** 2

# Надёжность исполнительного механизма
R_actuator = math.exp(-lambda_actuator * t)

# Общая надёжность системы
R_analytical = R_sensor * R_computer * R_actuator


print("Аналитическая надёжность системы:")
print(f"{R_analytical:.8f}")

print("\nРезультаты эксперимента со сходимостью:")
print("-" * 75)
print(f"{'N':<12}{'Оценка надёжности':<22}{'Абсолютная ошибка':<22}{'Отказы':<12}")
print("-" * 75)

errors = []
reliability_values = []
# Проведение экспериментов
for N in N_values:
    reliability, success, failure = simulate_system(N, t)
    reliability_values.append(reliability)
    error = abs(reliability - R_analytical)
    errors.append(error)

    print(
        f"{N:<12}"
        f"{reliability:<22.8f}"
        f"{error:<22.8f}"
        f"{failure:<12}"
    )


# Построение графиков
plot_convergence(N_values, errors)

plot_reliability(
    N_values,
    reliability_values,
    R_analytical
)