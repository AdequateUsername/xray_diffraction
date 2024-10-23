"""Calculate Rydberg constant using Moseley's law"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

z = [40, 42, 47, 49]
theta = [6.8, 6.0, 4.7, 4.3]
theta_unc = [0.2, 0.2, 0.2, 0.2]
a0 = 564.02 * 10 ** (-12)
wl_inverse_root = []
wl_inverse_root_unc = []
wl_inverse_root_unc_invert = []
for i, angle in enumerate(theta):
    angle = angle / 180 * np.pi
    wl_inverse_root.append(1 / np.sqrt(a0 * np.sin(angle)))
    unc = (1 / np.sqrt(a0 * np.sin(angle - theta_unc[i] * np.pi / 180)) - 1 / np.sqrt(
        a0 * np.sin(angle + theta_unc[i] * np.pi / 180))) / 2
    wl_inverse_root_unc.append(unc)
    wl_inverse_root_unc_invert.append(1/unc)



def straight_line(x, m, c):
    return m * x + c

def straight_line_fixed_m(x, c):
    return np.sqrt(10973731) * x + c


"""Case: gradient can vary"""
x_fit = np.linspace(35, 50, 1000)
single_guess = [np.sqrt(10971000), -0.2]
single_fit = curve_fit(straight_line, z, wl_inverse_root, p0=single_guess, sigma=wl_inverse_root_unc)
single_y_fit = straight_line(x_fit, *single_fit[0])
plt.grid()
plt.title("Determination of Rydberg Constant and Screening Coefficient")
plt.xlabel("Atomic Number")
plt.ylabel("Inverse Square Root of Wavelength (m^-0.5)")
plt.errorbar(z, wl_inverse_root, yerr=wl_inverse_root_unc, fmt='x')
plt.plot(x_fit, single_y_fit)
plt.tight_layout()
plt.savefig("rydberg_constant_screening_coefficient", dpi=400)
plt.show()

print("Case: determining Rydberg constant")
rydberg = (single_fit[0][0]) ** 2
rydberg_unc = (2 * np.sqrt(single_fit[1][0][0]) / single_fit[0][0]) * (single_fit[0][0])**2
screen_coef = single_fit[0][1] / single_fit[0][0]
screen_coef_unc = np.sqrt(
    (np.sqrt(single_fit[1][1][1]) / single_fit[0][1]) ** 2 + (np.sqrt(single_fit[1][0][0]) / single_fit[0][0]) ** 2)
print("Rydberg constant is:")
print(str(rydberg) + " ± " + str(rydberg_unc))
print()
print("Screening coefficient is:")
print(str(screen_coef) + " ± " + str(screen_coef_unc))

"""Case: gradient cannot vary; use actual Rydberg constant"""
single_guess = [-0.2]
single_fit = curve_fit(straight_line_fixed_m, z, wl_inverse_root, p0=single_guess, sigma=wl_inverse_root_unc)
single_y_fit = straight_line_fixed_m(x_fit, *single_fit[0])
plt.grid()
plt.title("Determination of Screening Coefficient\nwith Known Rydberg Constant")
plt.xlabel("Atomic Number")
plt.ylabel("Inverse Square Root of Wavelength (m^-0.5)")
plt.errorbar(z, wl_inverse_root, yerr=wl_inverse_root_unc, fmt='x')
plt.plot(x_fit, single_y_fit)
plt.tight_layout()
plt.savefig("screening_coefficient_fixed_R", dpi=400)
plt.show()

print("Case: actual Rydberg constant")
rydberg = 10973731
rydberg_unc = 0
screen_coef = single_fit[0][0] / np.sqrt(10973731)
screen_coef_unc = np.sqrt(single_fit[1][0][0]) / np.sqrt(10973731)
print("Rydberg constant is:")
print(str(rydberg) + " ± " + str(rydberg_unc))
print()
print("Screening coefficient is:")
print(str(screen_coef) + " ± " + str(screen_coef_unc))
