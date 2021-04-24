import matplotlib.pyplot as plt
import numpy as np


def fY(y, n):
    one_plus_y = 1 + y / np.sqrt(n)

    return n ** (n - .5) / (np.math.factorial(n - 1)) * one_plus_y ** (n - 1) * np.exp(-n * one_plus_y)


if __name__ == '__main__':
    for n in [1, 2, 10]:
        y = np.linspace(-np.sqrt(n), 4, 100)

        result = fY(y, n)

        plt.plot(y, result)
        plt.ylabel("fYn(y)")
        plt.xlabel("y")
        plt.title(f"Distribution of fYn(y) when n = {n}")
        plt.savefig(f'{n}.png')
        plt.show()
