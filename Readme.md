# README FILE

## Particle in a box simulator:
This project simulates the quantum mechanical model known as the particle in a box, a fundamental concept in quantum mechanics. It visualizes wavefunctions and corresponding energy levels for a particle confined in a one-dimensional infinite potential well.

## Overview:
The simulation computes and plots:
* Wavefunctions (Wf(n,a))
* Energy levels (Energy(n))
for different quantum numbers (n).
This model is a classic example of quantization in the particle in a box system.

## Features:
1. Computes normalized wavefunctions
2. Calculates discrete energy levels
3. Plots multiple quantum states (n = 1 to 5)
4. Displays energy values directly in the legend

## Formulas Used:

## Wavefunction –
Wf n(a) = ((2/L)**(1/2))sin(n*pi*x/L)

## Energy level-
Energy(n)=((nh)*2)/(8*m*L*2)

Where:
* ( n ): Quantum number (1, 2, 3, ...)
* ( h ): Planck's constant
* ( m ): Mass of the particle (electron)
* ( L ): Length of the box

## Requirements:
Install the required Python libraries:
pip install numpy matplotlib

## How to Run:
1. Clone or download this repository
2. Run the Python script:
   python particle_in_box.py
3. A plot will be displayed showing wavefunctions for different energy states.

## The graph shows:
* Wavefunctions for ( n = 1 ) to ( n = 5 )
* Nodes increasing with quantum number
* Energy values in Joules displayed in the legend

## Key Insights:
* Energy is quantized and increases with ( n^2 )
* Higher ( n ) → more oscillations in the wavefunction
* The particle cannot exist outside the box
* Wavefunctions are zero at the boundaries

## References:
* Introductory Quantum Mechanics textbooks
* Standard solutions of the Schrödinger equation
