import numpy as np


# Интенсивность отказов датчика
lambda_sensor = 0.0005
# Интенсивность отказов вычислителя
lambda_computer = 1 / 3000
# Интенсивность отказов исполнительного механизма
lambda_actuator = 1 / 1500

# Количество испытаний
N = 100000

# Продолжительность эксперимента
t = 5

success_count = 0
failure_count = 0

# Проведение испытаний
for i in range(N):

# Генерация времени отказа первого датчика
    failure_time_1 = np.random.exponential(
        scale=1 / lambda_sensor
    )

    # Генерация времени отказа второго датчика
    failure_time_2 = np.random.exponential(
        scale=1 / lambda_sensor
    )

    if failure_time_1 > t or failure_time_2 > t:
        success_count += 1
    else:
        failure_count += 1

print("Результаты моделирования датчиков:")
print(f"Исправных датчиков: {success_count}")
print(f"Отказавших датчиков: {failure_count}")

# Оценка надёжности методом Монте-Карло
reliability_estimate = success_count / N

print(f"Оценка надёжности: {reliability_estimate:.6f}")


# Эксперимент с резервированными вычислителями

success_computer = 0
failure_computer = 0

for i in range(N):

    # Время до отказа первого вычислителя
    failure_time_1 = np.random.exponential(
        scale=1 / lambda_computer
    )

    # Время до отказа второго вычислителя
    failure_time_2 = np.random.exponential(
        scale=1 / lambda_computer
    )

    # Проверка работоспособности пары
    if failure_time_1 > t or failure_time_2 > t:
        success_computer += 1
    else:
        failure_computer += 1

# Расчёт надёжности пары вычислителей
reliability_computer = success_computer / N

print("\nРезультаты моделирования вычислителей:")
print(f"Исправных подсистем: {success_computer}")
print(f"Отказавших подсистем: {failure_computer}")
print(f"Оценка надёжности: {reliability_computer:.6f}")


# Моделирование всей системы

success_system = 0
failure_system = 0

for i in range(N):

    # Время до отказа двух датчиков
    sensor_1 = np.random.exponential(
        scale=1 / lambda_sensor
    )

    sensor_2 = np.random.exponential(
        scale=1 / lambda_sensor
    )

    # Время до отказа двух вычислителей
    computer_1 = np.random.exponential(
        scale=1 / lambda_computer
    )

    computer_2 = np.random.exponential(
        scale=1 / lambda_computer
    )

    # Время до отказа исполнительного механизма
    actuator = np.random.exponential(
        scale=1 / lambda_actuator
    )

    # Проверка работоспособности всей системы
    if (sensor_1 > t or sensor_2 > t) and \
       (computer_1 > t or computer_2 > t) and \
       actuator > t:

        success_system += 1

    else:
        failure_system += 1


# Расчёт надёжности всей системы
reliability_system = success_system / N

print("\nРезультаты моделирования всей системы:")
print(f"Работоспособных систем: {success_system}")
print(f"Отказавших систем: {failure_system}")
print(f"Оценка надёжности: {reliability_system:.6f}")
