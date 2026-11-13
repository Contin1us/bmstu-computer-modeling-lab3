import os
import matplotlib.pyplot as plt

def plot_convergence(N_values, errors):

    plt.figure(figsize=(10, 6))

    plt.plot(
        N_values,
        errors,
        marker="o",
        label="Абсолютная ошибка"
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Количество испытаний N")
    plt.ylabel("Абсолютная ошибка")

    plt.title("Сходимость метода Монте-Карло")

    plt.grid(True)
    plt.legend()

    os.makedirs("results", exist_ok=True)

    plt.savefig(
        "results/convergence.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


def plot_reliability(N_values, reliability_values, analytical_value):

    plt.figure(figsize=(10, 6))

    plt.plot(
        N_values,
        reliability_values,
        marker="o",
        label="Метод Монте-Карло"
    )

    plt.axhline(
        y=analytical_value,
        color="red",
        linestyle="--",
        label="Аналитическое значение"
    )

    plt.xscale("log")

    plt.xlabel("Количество испытаний N")
    plt.ylabel("Вероятность безотказной работы")

    plt.title("Зависимость оценки надёжности от числа испытаний")

    plt.grid(True)
    plt.legend()

    os.makedirs("results", exist_ok=True)

    plt.savefig(
        "results/reliability.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


def plot_redundancy_comparison(
    time_values,
    reliability_without,
    reliability_with
):

    plt.figure(figsize=(10, 6))

    plt.plot(
        time_values,
        reliability_without,
        label="Без резервирования"
    )

    plt.plot(
        time_values,
        reliability_with,
        label="С резервированием"
    )

    plt.xlabel("Время эксплуатации, ч")
    plt.ylabel("Вероятность безотказной работы")

    plt.title("Влияние резервирования на надёжность системы")

    plt.grid(True)
    plt.legend()

    os.makedirs("results", exist_ok=True)

    plt.savefig(
        "results/redundancy_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


def plot_monte_carlo_comparison(
    time_values,
    reliability_without_mc,
    reliability_with_mc,
    reliability_without_analytical,
    reliability_with_analytical
):

    plt.figure(figsize=(10, 6))

    # Аналитическая надёжность без резервирования
    plt.plot(
        time_values,
        reliability_without_analytical,
        label="Аналитика без резервирования"
    )

    # Результаты Монте-Карло без резервирования
    plt.scatter(
        time_values,
        reliability_without_mc,
        label="Монте-Карло без резервирования",
        marker="o"
    )

    # Аналитическая надёжность с резервированием
    plt.plot(
        time_values,
        reliability_with_analytical,
        label="Аналитика с резервированием"
    )

    # Результаты Монте-Карло с резервированием
    plt.scatter(
        time_values,
        reliability_with_mc,
        label="Монте-Карло с резервированием",
        marker="s"
    )

    plt.xlabel("Время эксплуатации, ч")
    plt.ylabel("Вероятность безотказной работы")

    plt.title("Сравнение аналитического расчёта и метода Монте-Карло")

    plt.grid(True)
    plt.legend()

    os.makedirs("results", exist_ok=True)

    plt.savefig(
        "results/monte_carlo_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()