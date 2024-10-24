import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("sample_data/Ag.csv", delimiter=',', skiprows=2, usecols=(1, 2, 3))
events = data[::, 0]
channels = data[::, 1]
energy = data[::, 2]

plot_gaussian = True


def gaussian_func(x, x0, sigma, A):
    return A * (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


if plot_gaussian:
    initial_guess = [23, 1, 40]
    x_fit = np.linspace(20, 25, 10000)
    gaussian_fit = curve_fit(gaussian_func, energy, events, p0=initial_guess)
    gaussian_y_fit = gaussian_func(x_fit, *gaussian_fit[0])

plt.grid()
plt.plot(energy, events)
if plot_gaussian:
    plt.plot(x_fit, gaussian_y_fit)
plt.title("Silver Energy Spectrum")
plt.xlabel("Energy (keV)")
plt.ylabel("Frequency")
plt.xlim(20, 30)
# plt.savefig("processed/Cu_energy", dpi=400)
plt.show()

print("mean")
print(gaussian_fit[0][0])
print("sigma")
print(gaussian_fit[0][1])
