import numpy as np
import matplotlib.pyplot as plt

from cosmology.integrator import BackgroundIntegrator
from cosmology.equations import (
    phi_acceleration,
    kinetic,
    potential
)

print()
print("===================================")
print("FIELD DYNAMICS REPORT")
print("===================================")
print()

# --------------------------------------------------

z = np.linspace(8.0, 0.0, 4000)

solver = BackgroundIntegrator(phi_acceleration)

phi, phidot = solver.evolve(
    z,
    phi0=1.0,
    phidot0=0.0
)

# --------------------------------------------------

K = np.zeros_like(z)
V = np.zeros_like(z)
ratio = np.zeros_like(z)

for i in range(len(z)):

    K[i] = kinetic(phidot[i])

    V[i] = potential(
        phi[i],
        z[i]
    )

    ratio[i] = K[i] / (V[i] + 1e-12)

# --------------------------------------------------

print("TODAY")
print("----------------------------")

print("Kinetic =", K[-1])
print("Potential =", V[-1])
print("K/V =", ratio[-1])

print()

print("HIGH REDSHIFT")
print("----------------------------")

print("Kinetic =", K[0])
print("Potential =", V[0])
print("K/V =", ratio[0])

print()

print("Maximum K/V =", ratio.max())

# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z, K, label="Kinetic")

plt.plot(z, V, label="Potential")

plt.grid()

plt.legend()

plt.xlabel("Redshift")

plt.ylabel("Energy")

plt.title("Kinetic vs Potential")

plt.tight_layout()

plt.savefig("kinetic_vs_potential.png")

plt.close()

# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z, ratio)

plt.grid()

plt.xlabel("Redshift")

plt.ylabel("K/V")

plt.title("Kinetic-to-Potential Ratio")

plt.tight_layout()

plt.savefig("kinetic_potential_ratio.png")

plt.close()

print()
print("Saved:")
print("kinetic_vs_potential.png")
print("kinetic_potential_ratio.png")