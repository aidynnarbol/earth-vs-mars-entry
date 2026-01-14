import matplotlib.pyplot as plt


def plot_comparison(earth, mars):
    plt.figure()
    plt.plot(earth["h"]/1000, earth["v"], label="Earth")
    plt.plot(mars["h"]/1000, mars["v"], label="Mars")
    plt.xlabel("Altitude (km)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Atmospheric Entry: Earth vs Mars")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_deceleration(earth, mars):
    plt.figure()
    plt.plot(earth["t"], earth["a"]/9.81, label="Earth")
    plt.plot(mars["t"], mars["a"]/9.81, label="Mars")
    plt.xlabel("Time (s)")
    plt.ylabel("Deceleration (g)")
    plt.title("Deceleration Profile Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()
