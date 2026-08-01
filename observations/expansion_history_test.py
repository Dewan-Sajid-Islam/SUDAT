import numpy as np
import matplotlib.pyplot as plt

from cosmology.integrator import BackgroundIntegrator
from cosmology.equations import (
    phi_acceleration
)
from cosmology.observables import (
    H_of_z
)

print()
print("===================================")
print("EXPANSION HISTORY VALIDATION")
print("===================================")
print()

# --------------------------------------------------

z = np.linspace(8.0,0.0,4000)

solver = BackgroundIntegrator(phi_acceleration)

phi,phidot = solver.evolve(
    z,
    phi0=1.0,
    phidot0=0.0
)

# --------------------------------------------------

H = np.zeros_like(z)

for i in range(len(z)):

    H[i] = H_of_z(
        phi[i],
        phidot[i],
        z[i]
    )

# --------------------------------------------------
# Normalize
# --------------------------------------------------

Hnorm = H/H[-1]

Omega_m = 0.3
Omega_L = 0.7

Hlcdm = np.sqrt(
    Omega_m*(1+z)**3
    +Omega_L
)

difference = 100*np.abs(Hnorm-Hlcdm)/Hlcdm

# --------------------------------------------------

print("Today's normalized H =",Hnorm[-1])

print()

print("Maximum deviation =",difference.max(),"%")

print()

print("Average deviation =",difference.mean(),"%")

# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z,Hlcdm,label="LCDM")

plt.plot(z,Hnorm,label="SUDAT")

plt.grid()

plt.legend()

plt.xlabel("Redshift")

plt.ylabel("Normalized H")

plt.title("Expansion History")

plt.tight_layout()

plt.savefig("expansion_validation.png")

plt.close()

# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z,difference)

plt.grid()

plt.xlabel("Redshift")

plt.ylabel("% Difference")

plt.title("Deviation from LCDM")

plt.tight_layout()

plt.savefig("expansion_difference.png")

plt.close()

print("Saved:")

print("expansion_validation.png")

print("expansion_difference.png")