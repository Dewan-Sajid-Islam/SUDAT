import numpy as np
import matplotlib.pyplot as plt

from cosmology.equations import (
    rho_b,
    rho_phi,
    equation_of_state,
    Hubble,
    phi_acceleration
)

from cosmology.integrator import BackgroundIntegrator

from cosmology.observables import (
    Omega_m,
    Omega_phi,
    w_effective
)

print()
print("===================================")
print("SUDAT BACKGROUND REPORT")
print("===================================")
print()

# ----------------------------------------------------
# Background solution
# ----------------------------------------------------

z = np.linspace(8.0, 0.0, 4000)

solver = BackgroundIntegrator(phi_acceleration)

phi, phidot = solver.evolve(
    z,
    phi0=1.0,
    phidot0=0.0
)

rho = np.zeros_like(z)
H = np.zeros_like(z)
w = np.zeros_like(z)

OmegaM = np.zeros_like(z)
OmegaPhi = np.zeros_like(z)
weff = np.zeros_like(z)

for i in range(len(z)):

    rho[i] = rho_phi(phi[i], phidot[i], z[i])

    H[i] = Hubble(phi[i], phidot[i], z[i])

    w[i] = equation_of_state(
        phi[i],
        phidot[i],
        z[i]
    )

    OmegaM[i] = Omega_m(
        phi[i],
        phidot[i],
        z[i]
    )

    OmegaPhi[i] = Omega_phi(
        phi[i],
        phidot[i],
        z[i]
    )

    weff[i] = w_effective(
        phi[i],
        phidot[i],
        z[i]
    )

print("Today's Universe")
print("----------------")
print(f"phi       = {phi[-1]}")
print(f"H         = {H[-1]}")
print(f"rho_phi   = {rho[-1]}")
print(f"w         = {w[-1]}")
print(f"Omega_m   = {OmegaM[-1]}")
print(f"Omega_phi = {OmegaPhi[-1]}")
print(f"w_eff     = {weff[-1]}")

print()

print("Early Universe")
print("----------------")
print(f"Omega_m   = {OmegaM[0]}")
print(f"Omega_phi = {OmegaPhi[0]}")
print(f"w         = {w[0]}")

# ----------------------------------------------------
# Figure 1
# ----------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z, OmegaM, label="Omega_m")
plt.plot(z, OmegaPhi, label="Omega_phi")

plt.legend()
plt.grid()

plt.xlabel("Redshift")

plt.ylabel("Density Fraction")

plt.title("Energy Budget")

plt.tight_layout()

plt.savefig("energy_budget.png")

plt.close()

# ----------------------------------------------------
# Figure 2
# ----------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(z, weff)

plt.grid()

plt.xlabel("Redshift")

plt.ylabel("w_eff")

plt.title("Effective Equation of State")

plt.tight_layout()

plt.savefig("effective_w.png")

plt.close()

print()
print("Saved:")
print("energy_budget.png")
print("effective_w.png")