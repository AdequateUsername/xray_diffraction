import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("sample_data/unknowns/nr6.csv", delimiter=',', skiprows=2, usecols=(1, 2, 3))
events = data[::, 0]
channels = data[::, 1]
energy = data[::, 2]

plot_gaussian = False
plot_double_gaussian = False


def gaussian_func(x, x0, sigma, A):
    return A * (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

def double_gaussian_func(x, x01, sigma1, A1, x02, sigma2, A2):
    return A1 * (1 / (sigma1 * np.sqrt(2 * np.pi))) * np.exp(-(x - x01) ** 2 / (2 * sigma1 ** 2)) + A2 * (1 / (sigma2 * np.sqrt(2 * np.pi))) * np.exp(-(x - x02) ** 2 / (2 * sigma2 ** 2))


if plot_gaussian:
    initial_guess = [10.5, 0.5, 1.1]
    x_fit = np.linspace(9, 12, 10000)
    gaussian_fit = curve_fit(gaussian_func, energy, events, p0=initial_guess)
    gaussian_y_fit = gaussian_func(x_fit, *gaussian_fit[0])

elif plot_double_gaussian:
    initial_guess = [7.8, 0.5, 1.1, 8.5, 0.5, 0.9]
    x_fit = np.linspace(9, 10, 10000)
    gaussian_fit = curve_fit(double_gaussian_func, energy, events, p0=initial_guess)
    gaussian_y_fit = double_gaussian_func(x_fit, *gaussian_fit[0])

plt.grid()
plt.plot(energy, events)
if plot_gaussian or plot_double_gaussian:
    plt.plot(x_fit, gaussian_y_fit)
plt.title("Unknown Material Energy Spectrum")
plt.xlabel("Energy (keV)")
plt.ylabel("Frequency")
plt.xlim(11, 20)

if plot_gaussian:
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

elif plot_double_gaussian:
    print("mean1")
    print(gaussian_fit[0][0])
    print("sigma1")
    print(gaussian_fit[0][1])
    print("mean2")
    print(gaussian_fit[0][3])
    print("sigma2")
    print(gaussian_fit[0][4])

    energy1 = gaussian_fit[0][0]
    energy1_unc = gaussian_fit[0][1] + 0.4
    energy2 = gaussian_fit[0][3]
    energy2_unc = gaussian_fit[0][4] + 0.4
    R = 13.6e-3     # keV
    screen_coeff = 2.82598
    screen_coeff_unc = 0.122
    z1 = np.sqrt(energy1 / R) + screen_coeff
    z1_unc = np.sqrt((0.5 * (energy1_unc / energy1) * (np.sqrt(energy1 / R)))**2 + screen_coeff_unc**2)
    z2 = np.sqrt(energy2 / R) + screen_coeff
    z2_unc = np.sqrt((0.5 * (energy2_unc / energy2) * (np.sqrt(energy2 / R))) ** 2 + screen_coeff_unc ** 2)
    print(z1)
    print(z1_unc)
    print(z2)
    print(z2_unc)
    plt.legend(["Raw Data", f"Fitted Bimodal Gaussian \n Mean energy: {energy1:.1f} ± {energy1_unc:.1f} keV, {energy2:.1f} ± {energy2_unc:.1f} keV \n Atomic number: {z1:.1f} ± {z1_unc:.1f}, {z2:.1f} ± {z2_unc:.1f}"])

# plt.savefig("processed/unknowns/nr6", dpi=400)
plt.show()
