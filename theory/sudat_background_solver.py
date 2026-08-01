import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# SUDAT BACKGROUND SOLVER v1
# ==================================================

# ------------------------------
# PARAMETERS
# ------------------------------

V_lambda = 1500.0

m = 1.0
lam = 1.0
beta = 1.0

rho_b0 = 0.05

# ------------------------------
# REDSHIFT GRID
# ------------------------------

z = np.linspace(8.0, 0.0, 5000)

# ------------------------------
# BARYONS
# ------------------------------

def rho_b(z):
    return rho_b0 * (1.0 + z)**3

# ------------------------------
# POTENTIAL
# ------------------------------

def V(phi, rb):

    return (
        V_lambda
        + 0.5*(m*m - 2.0*lam*rb)*phi**2
        + 0.25*beta*phi**4
    )

# ------------------------------
# dV/dphi
# ------------------------------

def dV(phi, rb):

    return (
        (m*m - 2.0*lam*rb)*phi
        + beta*phi**3
    )

# ------------------------------
# ARRAYS
# ------------------------------

phi = np.zeros_like(z)
phidot = np.zeros_like(z)

rho_phi = np.zeros_like(z)
pressure_phi = np.zeros_like(z)

w = np.zeros_like(z)
H = np.zeros_like(z)

# ------------------------------
# INITIAL CONDITIONS
# ------------------------------

phi[0] = 1.0
phidot[0] = 0.0

# ------------------------------
# EVOLUTION
# ------------------------------

for i in range(len(z)-1):

    rb = rho_b(z[i])

    kinetic = 0.5 * phidot[i]**2

    potential = V(phi[i], rb)

    rho_phi[i] = kinetic + potential

    H[i] = np.sqrt(rb + rho_phi[i])

    phi_ddot = (
        -3.0 * H[i] * phidot[i]
        - dV(phi[i], rb)
    )

    dz = abs(z[i+1] - z[i])

    phidot[i+1] = (
        phidot[i]
        + phi_ddot * dz * 0.05
    )

    phi[i+1] = (
        phi[i]
        + phidot[i+1] * dz * 0.05
    )

# ------------------------------
# FINAL DIAGNOSTICS
# ------------------------------

for i in range(len(z)):

    rb = rho_b(z[i])

    kinetic = 0.5 * phidot[i]**2

    potential = V(phi[i], rb)

    rho_phi[i] = kinetic + potential

    pressure_phi[i] = kinetic - potential

    w[i] = (
        pressure_phi[i]
        /
        (rho_phi[i] + 1e-12)
    )

    H[i] = np.sqrt(
        rb + rho_phi[i]
    )

# ==================================================
# OUTPUT
# ==================================================

print()
print("====================================")
print("SUDAT BACKGROUND SOLVER")
print("====================================")
print()

print("w(today) =", w[-1])
print()

print("rho_phi(today) =", rho_phi[-1])
print()

print("phi(today) =", phi[-1])
print()

print("H(today) =", H[-1])
print()

# ==================================================
# PLOTS
# ==================================================

plt.figure(figsize=(8,5))
plt.plot(z, phi)
plt.xlabel("z")
plt.ylabel("phi")
plt.title("Scalar Field")
plt.grid()
plt.tight_layout()
plt.savefig("phi_of_z.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z, rho_phi)
plt.xlabel("z")
plt.ylabel("rho_phi")
plt.title("Scalar Energy Density")
plt.grid()
plt.tight_layout()
plt.savefig("rho_phi_of_z.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z, w)
plt.xlabel("z")
plt.ylabel("w")
plt.title("Equation of State")
plt.grid()
plt.tight_layout()
plt.savefig("w_of_z.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z, H)
plt.xlabel("z")
plt.ylabel("H")
plt.title("Expansion History")
plt.grid()
plt.tight_layout()
plt.savefig("H_of_z.png")
plt.close()

print("Saved:")
print("phi_of_z.png")
print("rho_phi_of_z.png")
print("w_of_z.png")
print("H_of_z.png")