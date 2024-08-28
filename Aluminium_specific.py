
import numpy as np
import matplotlib.pyplot as plt

# Temperature ranges for solid phase calculations
T1 = np.linspace(298.15, 700, 1000)
T2 = np.linspace(700, 933.47, 1000)
T3 = np.linspace(933.47, 1000, 1000)

# Gibbs free energy calculations for solid phase
G1 = -7976.15 + 137.093038 * T1 - 24.3671976 * T1 * np.log(T1) - 1.884662E-3 * T1 ** 2 - 0.8776648E-6 * T1 ** 3 + 74092 / T1
G2 = -11276.24 + 223.048446 * T2 - 38.5844296 * T2 * np.log(T2) + 18.531982E-3 * T2 ** 2 - 5.764227E-6 * T2 ** 3 + 74092 / T2
G3 = -11278.378 + 188.684153 * T3 - 31.748192 * T3 * np.log(T3) - 1.231E28 / T3 ** 9

# Combine dictionaries for solid phase Gibbs free energy
d_gs = {**dict(zip(T2, G2)), **dict(zip(T3, G3))}

# Gibbs free energy calculations for liquid phase
GL1 = 3028.879 + 125.251171 * T1 - 24.3671976 * T1 * np.log(T1) - 1.884662E-3 * T1 ** 2 - 0.877664E-6 * T1 ** 3 + 74092 / T1 + 7.934E-20 * T1 ** 7
GL2 = -271.21 + 211.206579 * T2 - 38.58442 * T2 * np.log(T2) + 18.531982E-3 * T2 ** 2 - 5.764227E-6 * T2 ** 3 + 74092 / T2 + 7.934E-20 * T2 ** 7
GL3 = -795.996 + 177.430178 * T3 - 31.748192 * T3 * np.log(T3)

# Combine dictionaries for liquid phase Gibbs free energy
d_gl = {**dict(zip(T2, GL2)), **dict(zip(T3, GL3))}

# Plot Gibbs free energy for solid and liquid phases
plt.plot(T1, G1, label='Solid Phase')
plt.plot(T2, G2)
plt.plot(T3, G3)
plt.plot(T1, GL1, label='Liquid Phase')
plt.plot(T2, GL2)
plt.plot(T3, GL3)

# Calculate melting point by finding temperature where Gibbs free energies are approximately equal
melting_point = None
for temp, energy in d_gs.items():
    if temp in d_gl and abs(energy - d_gl[temp]) < 0.01:
        melting_point = temp
        break

# Plot melting point if found
if melting_point:
    plt.scatter(melting_point, d_gs[melting_point], color='red', label=f'Melting Point: {melting_point} K')
    plt.axvline(melting_point, color='gray', linestyle='--')
    plt.axhline(d_gs[melting_point], color='gray', linestyle='--')
    plt.annotate(f'Melting Point: {melting_point} K', xy=(melting_point, d_gs[melting_point]), xytext=(melting_point + 50, d_gs[melting_point] + 200),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

# Label axes and plot
plt.xlabel('Temperature (K)')
plt.ylabel('Gibbs Free Energy (J/mol)')
plt.title('Gibbs Free Energy vs. Temperature')
plt.legend()
plt.grid(True)

# Display plot
plt.show()
