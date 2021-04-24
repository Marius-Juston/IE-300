import matplotlib.pyplot as plt
import numpy as np


def create_p(n):
    values = np.arange(1, n + 1)

    return (values - 0.5) / n


if __name__ == '__main__':
    p = create_p(500)

    y = np.linspace(0, 1, 500)

    x = -np.log(1 - p)

    plt.scatter(x, y)
    plt.title("Uniform vs Exponential QQ plot")
    plt.xlabel("tj")
    plt.ylabel("Uniform (0, 1)")
    plt.savefig("QQ_U(0,1)_Exp.png")
    plt.show()

    n = 500

    p = 1
    plt.plot(np.linspace(0, 1), np.full(50, p))
    plt.title("Uniform Distribution")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.savefig("Unfirma_distrubtion.png")
    plt.show()

    x = np.linspace(0, 1)

    y = np.exp(-x)
    plt.plot(x, y)
    plt.title("Exponential Distribution")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.savefig("Exponential_distrubtion.png")
    plt.show()
