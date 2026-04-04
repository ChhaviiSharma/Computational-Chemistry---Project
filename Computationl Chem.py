# Particle in a box simulator 

import numpy as np
import matplotlib.pyplot as plt

# Pre-defined constants
h = 6.626e-34     # Planck constant
m = 9.109e-31     # electron mass
L = 1e-9          # box length (1 nm)

a = np.linspace(0,L,200)

# Function for WaveFunction
def Wf(n,a):
    return ((2/L)**(1/2))*np.sin(n*np.pi*a/L)

# Function for Energy
def Energy(n):
    return((n*2)(h*2))/(8*m(L**2))

# Ploting wavefunction
plt.figure(figsize=(9,4)) #Width=9,Length=4

for n in range(1,5):
    plt.plot(a, Wf(n,a), label=f"n={n}, E={Energy(n):.2e} J")

plt.title("Particle in a Box")
plt.xlabel("Distance")
plt.ylabel("Wavefunction")
plt.legend()

plt.grid()  # Background

plt.show()