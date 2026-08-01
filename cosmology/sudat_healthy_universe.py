import numpy as np
import matplotlib.pyplot as plt

print()
print("===================================")
print("HEALTHY UNIVERSE COMPARISON")
print("===================================")
print()

# ----------------------------------
# Fixed parameters
# ----------------------------------

Omega_m0 = 0.3

m = 1.0
lam = 1.0
beta = 1.0

# ----------------------------------
# Test healthy models
# ----------------------------------

V0_models = [225, 500, 1500]

# ----------------------------------
# Redshift grid
# ----------------------------------

z = np.linspace(8.0, 0.0, 3000)

def rho_m(z):
    return Omega_m0 * (1.0 + z)**3

# ----------------------------------
# Storage
# ----------------------------------

all_H = []
all_w = []
all_rho = []

# ==================================
# Loop over healthy universes
# ==================================

for V0 in V0_models:

    phi = np.zeros_like(z)
    phidot = np.zeros_like(z)

    phi[0] = 1.0

    rho_phi = np.zeros_like(z)
    w = np.zeros_like(z)
    H = np.zeros_like(z)

    def V(phi, rb):

        return (
            V0
            + 0.5*(m*m - 2.0*lam*rb)*phi**2
            + 0.25*beta*phi**4
        )

    def dV(phi, rb):

        return (
            (m*m - 2.0*lam*rb)*phi
            + beta*phi**3
        )

    # ------------------------------
    # Evolution
    # ------------------------------

    for i in range(len(z)-1):

        rb = rho_m(z[i])

        kinetic = 0.5 * phidot[i]**2
        potential = V(phi[i], rb)

        rho = kinetic + potential

        H_i = np.sqrt(rho + rb)

        phi_ddot = (
            -3.0*H_i*phidot[i]
            - dV(phi[i], rb)
        )

        dz = abs(z[i+1] - z[i])

        phidot[i+1] = (
            phidot[i]
            + phi_ddot*dz*0.02
        )

        phi[i+1] = (
            phi[i]
            + phidot[i+1]*dz*0.02
        )

    # ------------------------------
    # Diagnostics
    # ------------------------------

    for i in range(len(z)):

        rb = rho_m(z[i])

        kinetic = 0.5*phidot[i]**2

        potential = V(phi[i], rb)

        rho_phi[i] = kinetic + potential

        pressure = kinetic - potential

        w[i] = pressure/(rho_phi[i] + 1e-12)

        H[i] = np.sqrt(rho_phi[i] + rb)

    print("V0 =", V0)
    print("  w(today) =", w[-1])
    print("  rho(today) =", rho_phi[-1])
    print("  H(today) =", H[-1])
    print()

    all_H.append((V0, H))
    all_w.append((V0, w))
    all_rho.append((V0, rho_phi))

# ==================================
# Figure 1
# ==================================

plt.figure(figsize=(8,5))

for V0, H in all_H:
    plt.plot(z, H, label=f"V0={V0}")

plt.xlabel("z")
plt.ylabel("H")
plt.title("Healthy Expansion Histories")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("healthy_H.png")
plt.close()

# ==================================
# Figure 2
# ==================================

plt.figure(figsize=(8,5))

for V0, w in all_w:
    plt.plot(z, w, label=f"V0={V0}")

plt.xlabel("z")
plt.ylabel("w")
plt.title("Healthy Equation of State")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("healthy_w.png")
plt.close()

# ==================================
# Figure 3
# ==================================

plt.figure(figsize=(8,5))

for V0, rho in all_rho:
    plt.plot(z, rho, label=f"V0={V0}")

plt.xlabel("z")
plt.ylabel("rho_phi")
plt.title("Healthy Scalar Densities")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("healthy_rho.png")
plt.close()

print("Saved:")
print("healthy_H.png")
print("healthy_w.png")
print("healthy_rho.png")