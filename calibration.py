import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("sample_data/calibration_straight_through.csv", delimiter=',', skiprows=2, usecols=(1, 2, 3))
events = data[::, 0]
channels = data[::, 1]
energy = data[::, 2]

plot_gaussian = True

def gaussian_func(x, x0, sigma, A, h):
    return A * (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + h

if plot_gaussian:
    initial_guess = [365, 15, 10000, 10000]
    x_fit = np.linspace(340, 390, 10000)
    gaussian_fit = curve_fit(gaussian_func, channels, events, p0=initial_guess)
    gaussian_y_fit = gaussian_func(x_fit, *gaussian_fit[0])

plt.grid()
plt.plot(channels, events)
if plot_gaussian:
    plt.plot(x_fit, gaussian_y_fit)
plt.title("Calibration of Straight Through Spectrum")
plt.xlabel("Channels")
plt.ylabel("Frequency")
plt.xlim(330, 400)
plt.savefig("processed/str8_through", dpi=400)
plt.show()

print("mean")
print(gaussian_fit[0][0])
print("sigma")
print(gaussian_fit[0][1])
print("amplitude")
print(gaussian_fit[0][2])
print("offset")
print(gaussian_fit[0][3])