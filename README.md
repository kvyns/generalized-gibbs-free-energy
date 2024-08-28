# Gibbs free energy vs Temperature plotter for different elements

This repository contains a Python-based calculator for determining the Gibbs free energy of phase transitions for various elements. The code is designed to be flexible and can accommodate different temperature ranges and equations for solid and liquid phases.

## Features

- Calculates the Gibbs free energy of phase transitions for various elements
- Accommodates different temperature ranges and equations for solid and liquid phases
- Plots the Gibbs free energy vs. temperature for both phases
- Finds and plots the melting point

## Prerequisites

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kvyns/generalized-gibbs-free-energy.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script python main.py
2. Modify the temperature ranges and equations for solid and liquid phases as needed

## Results
 Actual vs. Calculated Melting Points
 --------------------------------------
| Element |	Actual Melting Point (K) |	Calculated Melting Point (K) | Error (%) |
| ------- | ------------------------ | ---------------------------- | --------- |
| Aluminium |	933.47 |	932.12 |	0.15 |

<img src = "Calculated.png" height = 200px width="auto" align="center"/>
## History
This project was initially developed for Aluminium as a part of Materials Modelling and has since been generalized to accommodate other elements. The original Aluminium-specific code is available here.
