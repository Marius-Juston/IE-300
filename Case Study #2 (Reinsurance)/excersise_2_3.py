import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

if __name__ == '__main__':
    data = pd.read_csv('IE300_CASE2_DATA.txt', sep=r'\s+', engine='python', names=('Year', 'Price'))
    data["Price"] = data['Price'].apply(lambda x: x.replace(",", ''))
    data["Price"] = pd.to_numeric(data['Price'])

    print(data.head())

    sorted_data = data.sort_values(by='Price', ascending=False)

    print(sorted_data)

    cropped = sorted_data[:270]

    print(cropped)

    cropped['Price'] = cropped['Price'].apply(np.log)

    print(cropped)

    ax = plt.gca()

    x = cropped['Price'].values

    expo = stats.probplot(x, dist=stats.expon, plot=plt)
    plt.savefig("ExponentalQQ.png")
    plt.show()
    expo = stats.probplot(x, dist=stats.norm, plot=plt)
    plt.savefig("NormQQ.png")
    plt.show()
