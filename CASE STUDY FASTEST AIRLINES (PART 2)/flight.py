import numpy as np
import pandas as pd


def probability(n_hat, n, m, p):
    return (n_hat + m * p) / (n + m)


def find_p_key_based(data, keys: dict, m=3, p=1 / 2):
    yes: pd.DataFrame = data[data['Delayed'] == 'Y']
    no = data[data['Delayed'] == 'N']

    total_yes = len(yes.index)
    total_no = len(no.index)

    total_size = len(data.index)

    p_y = total_yes / total_size
    p_n = total_no / total_size

    for (k, v) in keys.items():
        count_y = len(yes[yes[k] == v].index)
        count_n = len(no[no[k] == v].index)

        p_k_y = probability(count_y, total_yes, m, p)
        p_k_n = probability(count_n, total_no, m, p)

        p_y *= p_k_y
        p_n *= p_k_n

    return p_y, p_n


def arg_max(p):
    if p[0] > p[1]:
        return "Y"
    return "N"


def example_1():
    # Example 1
    data = pd.DataFrame({
        "Origin": ['DFW', "DFW", "DFW", "LAX", "LAX", "LAX", "LAX", "LAX", "DFW", "DFW"],
        "Destination": ['ORD', 'ORD', 'ORD', 'ORD', 'ORD', "LGA", "LGA", "LGA", "LGA", "ORD"],
        "Airline": ['Delta', 'Delta', 'Delta', 'Delta', "United", "United", "United", "Delta", "United", "United"],
        "Delayed": ['Y', "N", "Y", "N", "Y", "N", "Y", "N", "N", "Y"]
    })

    calculated_probability = find_p_key_based(data, {
        'Origin': "DFW",
        "Destination": "LGA",
        "Airline": "Delta"
    })
    print(data)
    print("P(Y) =", calculated_probability[0], "P(N) =", calculated_probability[1])
    print(arg_max(calculated_probability))


def exercise_1():
    # Exercise 1
    data = pd.DataFrame({
        "Origin": ['SEA', "SEA", "SEA", "SFO", "SFO", "SFO", "SFO", "SEA"],
        "Destination": ["ATL", "BOS", "ATL", "BOS", "ATL", "BOS", "BOS", "BOS"],
        "Airline": ["Southwest", "American", "United", "Southwest", "American", "United", "United", "Southwest"],
        "Weather": ["Poor", "Good", "Poor", "Poor", "Good", "Poor", "Good", "Poor"],
        "Delayed": ['N', "Y", "Y", "Y", "N", "Y", "N", "Y"]
    })

    print(data)

    calculated_probability = find_p_key_based(data, {
        'Origin': "SEA",
        "Destination": "ATL",
        "Airline": "Southwest",
        "Weather": "Good"
    })

    print("P(Y) =", calculated_probability[0], "P(N) =", calculated_probability[1])
    print(arg_max(calculated_probability))


def exercise_2():
    # Actual problem
    data = pd.read_csv("FlightDelay.csv")

    data['Total Delay'] = data["Departure Delay"] + data["Arrival Delay"]

    data['Delayed'] = np.where(data["Total Delay"] > 15, "Y", "N")

    return data


def exercise_3(data, output='out.csv'):
    data_points = [
        {
            'Origin': "JFK",
            "Destination": "LAS",
            "Carrier": "AA",
        },
        {
            'Origin': "JFK",
            "Destination": "LAS",
            "Carrier": "B6",
        },
        {
            'Origin': "SFO",
            "Destination": "ORD",
            "Carrier": "VX",
        },
        {
            'Origin': "SFO",
            "Destination": "ORD",
            "Carrier": "WN",
        }
    ]

    lines = []

    for data_point in data_points:
        p = find_p_key_based(data, data_point)
        classification = arg_max(p)

        lines.append(','.join(map(str, [*p, classification])) + '\n')

    with open(output, 'w') as output_file:
        output_file.writelines(lines)


if __name__ == '__main__':
    example_1()

    exercise_1()

    csv_data = exercise_2()

    exercise_3(csv_data)
