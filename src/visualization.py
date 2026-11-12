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