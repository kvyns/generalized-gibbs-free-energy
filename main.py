import numpy as np
import matplotlib.pyplot as plt

class GibbsFreeEnergy:
    def __init__(self, name, temperature_ranges, equations):
        self.name = name
        self.temperature_ranges = temperature_ranges
        self.equations = equations

    def calculate_gibbs_free_energy(self):
        self.gibbs_free_energies = []
        for equation, temperature_range in zip(self.equations, self.temperature_ranges):
            gibbs_free_energy = equation(temperature_range)
            self.gibbs_free_energies.append(gibbs_free_energy)

    def plot_gibbs_free_energy(self):
        for temperature_range, gibbs_free_energy in zip(self.temperature_ranges, self.gibbs_free_energies):
            plt.plot(temperature_range, gibbs_free_energy, label=self.name)

    def combine_dictionaries(self):
        self.combined_dictionary = {}
        for temperature_range, gibbs_free_energy in zip(self.temperature_ranges, self.gibbs_free_energies):
            self.combined_dictionary.update(dict(zip(temperature_range, gibbs_free_energy)))

def find_melting_point(d_gs, d_gl):
    for temp, energy in d_gs.items():
        if temp in d_gl and abs(energy - d_gl[temp]) < 0.01:
            return temp
    return None

def plot_melting_point(melting_point, d_gs):
    if melting_point:
        plt.scatter(melting_point, d_gs[melting_point], color='red', label=f'Melting Point: {melting_point} K')
        plt.axvline(melting_point, color='gray', linestyle='--')
        plt.axhline(d_gs[melting_point], color='gray', linestyle='--')
        plt.annotate(f'Melting Point: {melting_point} K', xy=(melting_point, d_gs[melting_point]), xytext=(melting_point + 50, d_gs[melting_point] + 200),
                     arrowprops=dict(facecolor='black', arrowstyle='->'))

def plot_gibbs_free_energy(phases):
    for phase in phases:
        phase.calculate_gibbs_free_energy()
        phase.plot_gibbs_free_energy()
        phase.combine_dictionaries()

    plt.xlabel('Temperature (K)')
    plt.ylabel('Gibbs Free Energy (J/mol)')
    plt.title('Gibbs Free Energy vs. Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    #the below sections can be changed according to user requirements
    temperature_ranges = [np.linspace(298.15, 700, 1000), np.linspace(700, 933.47, 1000), np.linspace(933.47, 1000, 1000)]

    solid_phase_equations = [
        lambda T: -7976.15 + 137.093038 * T - 24.3671976 * T * np.log(T) - 1.884662E-3 * T ** 2 - 0.8776648E-6 * T ** 3 + 74092 / T,
        lambda T: -11276.24 + 223.048446 * T - 38.5844296 * T * np.log(T) + 18.531982E-3 * T ** 2 - 5.764227E-6 * T ** 3 + 74092 / T,
        lambda T: -11278.378 + 188.684153 * T - 31.748192 * T * np.log(T) - 1.231E28 / T ** 9
    ]

    liquid_phase_equations = [
        lambda T: 3028.879 + 125.251171 * T - 24.3671976 * T * np.log(T) - 1.884662E-3 * T ** 2 - 0.877664E-6 * T ** 3 + 74092 / T + 7.934E-20 * T ** 7,
        lambda T: -271.21 + 211.206579 * T - 38.58442 * T * np.log(T) + 18.531982E-3 * T ** 2 - 5.764227E-6 * T ** 3 + 74092 / T + 7.934E-20 * T ** 7,
        lambda T: -795.996 + 177.430178 * T - 31.748192 * T * np.log(T)
    ]

    solid_phase = GibbsFreeEnergy('Solid Phase', temperature_ranges, solid_phase_equations)
    liquid_phase = GibbsFreeEnergy('Liquid Phase', temperature_ranges, liquid_phase_equations)

    phases = [solid_phase, liquid_phase]

    plot_gibbs_free_energy(phases)

    d_gs = solid_phase.combined_dictionary
    d_gl = liquid_phase.combined_dictionary

    melting_point = find_melting_point(d_gs, d_gl)
    plot_melting_point(melting_point, d_gs)

if __name__ == "__main__":
    main()
