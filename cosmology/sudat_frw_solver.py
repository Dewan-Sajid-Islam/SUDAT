import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# SUDAT FRW SOLVER v1
# ==========================================

# ------------------------------------------
# Parameters
# ------------------------------------------

V0 = 2.0

m = 1.0
lam = 1.0
beta = 1.0

Omega_m0 = 0.3

# ------------------------------------------
# Redshift grid
# ------------------------------------------

z = np.linspace(8.0, 0.0, 4000)

# ------------------------------------------
# Matter density
# ------------------------------------------

def rho_m(z):
    return Omega_m0 * (1 + z)**3

# ------------------------------------------
# Potential
# ------------------------------------------

def V(phi, rho_b):

    return (
        V0
        + 0.5*(m*m - 2*lam*rho_b)*phi**2
        + 0.25*beta*phi**4
    )

# ------------------------------------------
# Derivative
# ------------------------------------------

def dV(phi, rho_b):

    return (
        (m*m - 2*lam*rho_b)*phi
        + beta*phi**3
    )

# ------------------------------------------
# Arrays
# ------------------------------------------

phi = np.zeros_like(z)
phidot = np.zeros_like(z)

rho_phi = np.zeros_like(z)
w = np.zeros_like(z)
H = np.zeros_like(z)

# ------------------------------------------
# Initial conditions
# ------------------------------------------

phi[0] = 1.0
phidot[0] = 0.0

# ------------------------------------------
# Evolution
# ------------------------------------------

for i in range(len(z)-1):

    rm = rho_m(z[i])

    kinetic = 0.5*phidot[i]**2
    potential = V(phi[i], rm)

    rho_phi_i = kinetic + potential

    H_i = np.sqrt(abs(rm + rho_phi_i))

    phi_ddot = (
        -3.0*H_i*phidot[i]
        -dV(phi[i], rm)
    )

    dz = abs(z[i+1]-z[i])

    phidot[i+1] = phidot[i] + phi_ddot*dz*0.02

    phi[i+1] = phi[i] + phidot[i+1]*dz*0.02

# ------------------------------------------
# Diagnostics
# ------------------------------------------

for i in range(len(z)):

    rm = rho_m(z[i])

    kinetic = 0.5*phidot[i]**2
    potential = V(phi[i], rm)

    rho_phi[i] = kinetic + potential

    pressure = kinetic - potential

    w[i] = pressure/(rho_phi[i] + 1e-12)

    H[i] = np.sqrt(abs(rm + rho_phi[i]))

# ==========================================
# Output
# ==========================================

print()
print("===================================")
print("FRW BACKGROUND TEST")
print("===================================")
print()

print("w(high-z) =", w[0])
print("w(today)  =", w[-1])
print()

print("rho_phi(today) =", rho_phi[-1])
print()

print("H(today) =", H[-1])
print()

# ==========================================
# Figures
# ==========================================

plt.figure(figsize=(8,5))
plt.plot(z,H)
plt.xlabel("z")
plt.ylabel("H")
plt.title("FRW Expansion History")
plt.grid()
plt.tight_layout()
plt.savefig("frw_H.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z,w)
plt.xlabel("z")
plt.ylabel("w")
plt.title("Equation of State")
plt.grid()
plt.tight_layout()
plt.savefig("frw_w.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z,rho_phi)
plt.xlabel("z")
plt.ylabel("rho_phi")
plt.title("Scalar Density")
plt.grid()
plt.tight_layout()
plt.savefig("frw_rho_phi.png")
plt.close()

plt.figure(figsize=(8,5))
plt.plot(z,phi)
plt.xlabel("z")
plt.ylabel("phi")
plt.title("Field Evolution")
plt.grid()
plt.tight_layout()
plt.savefig("frw_phi.png")
plt.close()

print("Saved:")
print("frw_H.png")
print("frw_w.png")
print("frw_rho_phi.png")
print("frw_phi.png")