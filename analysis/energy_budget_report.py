import numpy as np
import matplotlib.pyplot as plt

from cosmology.integrator import BackgroundIntegrator

from cosmology.equations import (
    rho_b,
    rho_phi,
    phi_acceleration,
    Hubble
)

print()
print("===================================")
print("SUDAT ENERGY BUDGET REPORT")
print("===================================")
print()

# --------------------------------------------------
# Solve background
# --------------------------------------------------

z = np.linspace(8.0, 0.0, 4000)

solver = BackgroundIntegrator(phi_acceleration)

phi, phidot = solver.evolve(
    z,
    phi0=1.0,
    phidot0=0.0
)

# --------------------------------------------------
# Allocate arrays
# --------------------------------------------------

rhoMatter = np.zeros_like(z)
rhoScalar = np.zeros_like(z)

fractionMatter = np.zeros_like(z)
fractionScalar = np.zeros_like(z)

H = np.zeros_like(z)

# --------------------------------------------------
# Compute energy budget
# --------------------------------------------------

for i in range(len(z)):

    rb = rho_b(z[i])

    rp = rho_phi(
        phi[i],
        phidot[i],
        z[i]
    )

    rhoMatter[i] = rb
    rhoScalar[i] = rp

    total = rb + rp

    fractionMatter[i] = rb / total
    fractionScalar[i] = rp / total

    H[i] = Hubble(
        phi[i],
        phidot[i],
        z[i]
    )

# --------------------------------------------------
# Console report
# --------------------------------------------------

print("TODAY")
print("----------------------------")

print("Matter density =", rhoMatter[-1])
print("Scalar density =", rhoScalar[-1])

print()

print("Matter fraction =", fractionMatter[-1])
print("Scalar fraction =", fractionScalar[-1])

print()

print("HIGH REDSHIFT")
print("----------------------------")

print("Matter density =", rhoMatter[0])
print("Scalar density =", rhoScalar[0])

print()

print("Matter fraction =", fractionMatter[0])
print("Scalar fraction =", fractionScalar[0])

print()

print("Maximum H =", H.max())
print("Minimum H =", H.min())

# --------------------------------------------------
# Figure 1
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    z,
    rhoMatter,
    label="Matter"
)

plt.plot(
    z,
    rhoScalar,
    label="Scalar"
)

plt.grid()

plt.legend()

plt.xlabel("Redshift")

plt.ylabel("Energy Density")

plt.title("Energy Budget")

plt.tight_layout()

plt.savefig("energy_budget_densities.png")

plt.close()

# --------------------------------------------------
# Figure 2
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    z,
    fractionMatter,
    label="Matter"
)

plt.plot(
    z,
    fractionScalar,
    label="Scalar"
)

plt.grid()

plt.legend()

plt.xlabel("Redshift")

plt.ylabel("Fraction")

plt.title("Fractional Contributions")

plt.tight_layout()

plt.savefig("energy_budget_fractions.png")

plt.close()

# --------------------------------------------------

print()
print("Saved:")
print("energy_budget_densities.png")
print("energy_budget_fractions.png")