import numpy as np
import matplotlib.pyplot as plt

from .equations import (
    rho_phi,
    equation_of_state,
    Hubble,
    phi_acceleration
)

from .integrator import BackgroundIntegrator


# =====================================================
# BACKGROUND GRID
# =====================================================

z = np.linspace(8.0, 0.0, 4000)


# =====================================================
# INITIAL CONDITIONS
# =====================================================

phi0 = 1.0
phidot0 = 0.0


# =====================================================
# EVOLVE THE SCALAR FIELD
# =====================================================

solver = BackgroundIntegrator(phi_acceleration)

phi, phidot = solver.evolve(
    z,
    phi0,
    phidot0
)


# =====================================================
# COMPUTE COSMOLOGICAL QUANTITIES
# =====================================================

rho = np.zeros_like(z)
w = np.zeros_like(z)
H = np.zeros_like(z)

for i in range(len(z)):

    rho[i] = rho_phi(
        phi[i],
        phidot[i],
        z[i]
    )

    w[i] = equation_of_state(
        phi[i],
        phidot[i],
        z[i]
    )

    H[i] = Hubble(
        phi[i],
        phidot[i],
        z[i]
    )


# =====================================================
# OUTPUT
# =====================================================

print()
print("===================================")
print("SUDAT BACKGROUND V2")
print("===================================")
print()

print("phi(today) =", phi[-1])
print()

print("rho_phi(today) =", rho[-1])
print()

print("w(today) =", w[-1])
print()

print("H(today) =", H[-1])
print()


# =====================================================
# FIGURE 1
# =====================================================

plt.figure(figsize=(8,5))
plt.plot(z, phi)

plt.xlabel("Redshift z")
plt.ylabel("Field")

plt.title("Scalar Field Evolution")

plt.grid()

plt.tight_layout()

plt.savefig("background_v2_phi.png")

plt.close()


# =====================================================
# FIGURE 2
# =====================================================

plt.figure(figsize=(8,5))
plt.plot(z, rho)

plt.xlabel("Redshift z")
plt.ylabel("Density")

plt.title("Scalar Energy Density")

plt.grid()

plt.tight_layout()

plt.savefig("background_v2_rho.png")

plt.close()


# =====================================================
# FIGURE 3
# =====================================================

plt.figure(figsize=(8,5))
plt.plot(z, w)

plt.xlabel("Redshift z")
plt.ylabel("w")

plt.title("Equation of State")

plt.grid()

plt.tight_layout()

plt.savefig("background_v2_w.png")

plt.close()


# =====================================================
# FIGURE 4
# =====================================================

plt.figure(figsize=(8,5))
plt.plot(z, H)

plt.xlabel("Redshift z")
plt.ylabel("H")

plt.title("Expansion History")

plt.grid()

plt.tight_layout()

plt.savefig("background_v2_H.png")

plt.close()


print("Saved:")
print("background_v2_phi.png")
print("background_v2_rho.png")
print("background_v2_w.png")
print("background_v2_H.png")