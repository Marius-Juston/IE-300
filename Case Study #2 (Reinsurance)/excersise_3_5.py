import numpy as np
import pandas as pd


def hill_estimator(x, k, x_k_n):
    n = x.shape[0]

    return 1 / k * np.sum(np.log(x[n - k:]) - np.log(x_k_n))


def estimator_3(x, k, R):
    n = x.shape[0]
    x_k_n = x[n - k - 1]

    alpha = hill_estimator(x, k, x_k_n)

    return (R / ((1 / alpha) - 1)) * (k / n) * (R / x_k_n) ** (-1 / alpha)


if __name__ == '__main__':
    Rs = [3000000, 3500000, 4000000, 5000000, 7500000]

    data = pd.read_csv('IE300_CASE2_DATA.txt', sep=r'\s+', engine='python', names=('Year', 'Price'))
    data["Price"] = data['Price'].apply(lambda x: x.replace(",", ''))
    data["Price"] = pd.to_numeric(data['Price'])

    x = data['Price'].values
    x = np.sort(x)

    k = 95

    for R in Rs:
        print(R, estimator_3(x, k, R))
