
import math


from src.analytical import (
    calculate_reliability_without_reserve,
    calculate_reliability_with_reserve
)

from src.visualization import (
    plot_redundancy_comparison,
    plot_monte_carlo_comparison
)
from src.visualization import plot_convergence, plot_reliability
from src.monte_carlo import (
    simulate_system,
    simulate_system_without_reserve,
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

# Параметры сравнительного эксперимента

time_values = list(range(0, 1001, 10))

# Расчёт надёжности системы без резервирования

reliability_without = [
    calculate_reliability_without_reserve(t)
    for t in time_values
]


# Расчёт надёжности системы с резервированием

reliability_with = [
    calculate_reliability_with_reserve(t)
    for t in time_values
]

# Построение сравнительного графика

plot_redundancy_comparison(
    time_values,
    reliability_without,
    reliability_with
)


# Количество испытаний для сравнения
N_comparison = 100000

# Временные точки для эксперимента
comparison_times = [5, 100, 250, 500, 750, 1000]

print("\nСравнение систем методом Монте-Карло:")
print("-" * 85)

print(
    f"{'Время':<12}"
    f"{'Без резерва':<20}"
    f"{'С резервом':<20}"
    f"{'Аналитика без резерва':<22}"
    f"{'Аналитика с резервом':<22}"
)


reliability_without_mc_values = []
reliability_with_mc_values = []
reliability_without_analytical_values = []
reliability_with_analytical_values = []


for current_time in comparison_times:

    reliability_without_mc, success_1, failure_1 = (
        simulate_system_without_reserve(N_comparison, current_time)
    )

    reliability_with_mc, success_2, failure_2 = (
        simulate_system(N_comparison, current_time)
    )

    reliability_without_analytical = (
        calculate_reliability_without_reserve(current_time)
    )

    reliability_with_analytical = (
        calculate_reliability_with_reserve(current_time)
    )

    reliability_without_mc_values.append(reliability_without_mc)
    reliability_with_mc_values.append(reliability_with_mc)
    reliability_without_analytical_values.append(reliability_without_analytical)
    reliability_with_analytical_values.append(reliability_with_analytical)
    
    print(
        f"{current_time:<12}"
        f"{reliability_without_mc:<20.6f}"
        f"{reliability_with_mc:<20.6f}"
        f"{reliability_without_analytical:<22.6f}"
        f"{reliability_with_analytical:<22.6f}"
    )


# Построение итогового графика сравнения методов

plot_monte_carlo_comparison(
    comparison_times,
    reliability_without_mc_values,
    reliability_with_mc_values,
    reliability_without_analytical_values,
    reliability_with_analytical_values
)