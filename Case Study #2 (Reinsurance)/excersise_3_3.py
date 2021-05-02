import numpy as np
import pandas as pd


def estimator_1(x, R):
    diff = (x - R)
    diff[diff < 0] = 0

    return np.sum(diff) / x.shape[0]


if __name__ == '__main__':
    Rs = [3000000, 3500000, 4000000, 5000000, 7500000]

    data = pd.read_csv('IE300_CASE2_DATA.txt', sep=r'\s+', engine='python', names=('Year', 'Price'))
    data["Price"] = data['Price'].apply(lambda x: x.replace(",", ''))
    data["Price"] = pd.to_numeric(data['Price'])

    x = data['Price'].values

    for R in Rs:
        print(R, estimator_1(x, R))
