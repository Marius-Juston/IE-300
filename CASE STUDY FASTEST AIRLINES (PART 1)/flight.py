import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    flight_file: pd.DataFrame = pd.read_csv("FlightTime.csv")

    flight_file = flight_file[flight_file['Flight Time'] > 230]

    d = 1741.16
    l_ori = -87.9
    l_des = -118.41

    target_flight_time = 0.117 * d + 0.517 * (l_ori - l_des) + 20
    print(target_flight_time)

    average_arr_delay, average_departure_delay = flight_file.mean()[['Arrival Delay', "Departure Delay"]]

    means: pd.DataFrame = flight_file.groupby("Carrier").mean()[["Flight Time"]]

    means["Typical Flight Time"] = target_flight_time + average_arr_delay + average_departure_delay

    means["Time Added"] = means["Flight Time"] - means["Typical Flight Time"]

    means = means.sort_values("Time Added")

    means.to_csv("Case_study_fastest_airlines_part_1.csv")

    ax = means.plot.bar(y="Time Added", title="Carrier vs Time Added", xlabel="Carrier",
                        ylabel="Time added (min)", rot=0, grid=True)

    for p in ax.patches:
        ax.annotate(str(round(p.get_height(), 3)), (p.get_x() * 1.005, max(p.get_height(), 0.1) * 1.005))
    plt.savefig("Case_study_fastest_airlines_part_1.png")
