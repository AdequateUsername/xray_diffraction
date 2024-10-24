import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("sample_data/Cu.csv", delimiter=',', skiprows=2, usecols=(1, 2, 3))
events = data[::, 0]
channels = data[::, 1]
energy = data[::, 2]

plot_gaussian = True


def gaussian_func(x, x0, sigma, A):
    return A * (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


if plot_gaussian:
    initial_guess = [8.1, 0.5, 1.1]
    x_fit = np.linspace(7, 9, 10000)
    gaussian_fit = curve_fit(gaussian_func, energy, events, p0=initial_guess)
    gaussian_y_fit = gaussian_func(x_fit, *gaussian_fit[0])

plt.grid()
plt.plot(energy, events)
if plot_gaussian:
    plt.plot(x_fit, gaussian_y_fit)
plt.title("Copper Energy Spectrum")
plt.xlabel("Energy (keV)")
plt.ylabel("Frequency")
plt.xlim(2.5, 15)

print("mean")
print(gaussian_fit[0][0])
print("sigma")
print(gaussian_fit[0][1])

energy = gaussian_fit[0][0]
energy_unc = gaussian_fit[0][1] + 0.4
R = 13.6e-3     # keV
screen_coeff = 2.82598
screen_coeff_unc = 0.122
z = np.sqrt(energy / R) + screen_coeff
z_unc = np.sqrt((0.5 * (energy_unc / energy) * (np.sqrt(energy / R)))**2 + screen_coeff_unc**2)
print(z)
print(z_unc)

plt.legend(["Raw Data", f"Fitted Gaussian \n Mean energy: {energy:.1f} ± {energy_unc:.1f} keV \n Atomic number: {z:.1f} ± {z_unc:.1f}"])
plt.savefig("processed/Cu_energy_Gaussian", dpi=400)
plt.show()
