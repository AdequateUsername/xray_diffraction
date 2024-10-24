import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("sample_data/Ag.csv", delimiter=',', skiprows=2, usecols=(1, 2, 3))
events = data[::, 0]
channels = data[::, 1]
energy = data[::, 2]

plot_gaussian = False
def gaussian_func(x, x0, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

if plot_gaussian:
    initial_guess = [365, 2]
    x_fit = np.linspace(250, 500, 10000)
    gaussian_fit = curve_fit(gaussian_func, channels[350:370], events[350:370], p0=initial_guess)
    gaussian_y_fit = gaussian_func(x_fit, *gaussian_fit[0]) * 2000

plt.grid()
plt.plot(energy, events)
if plot_gaussian:
    plt.plot(x_fit, gaussian_y_fit)
plt.title("Molybdenum Straight-through Spectrum (channels)")
plt.xlabel("Energy (channels)")
plt.ylabel("Frequency")
plt.savefig("processed/Ag", dpi=400)
plt.show()
