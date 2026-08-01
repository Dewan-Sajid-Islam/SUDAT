import numpy as np
import matplotlib.pyplot as plt

print()
print("===================================")
print("SUDAT vs LCDM")
print("===================================")
print()

# ===================================
# LCDM PARAMETERS
# ===================================

Omega_m0 = 0.3
Omega_L0 = 0.7

# ===================================
# SUDAT PARAMETERS
# ===================================

V0 = 225

m = 1.0
lam = 1.0
beta = 1.0

# ===================================
# REDSHIFT GRID
# ===================================

z = np.linspace(0, 8, 2000)

def rho_m(z):
    return Omega_m0*(1+z)**3

# ===================================
# LCDM
# ===================================

H_LCDM = np.sqrt(
    Omega_m0*(1+z)**3
    + Omega_L0
)

# ===================================
# SUDAT EVOLUTION
# ===================================

z_rev = z[::-1]

phi = np.zeros_like(z_rev)
phidot = np.zeros_like(z_rev)

phi[0] = 1.0

rho_phi = np.zeros_like(z_rev)
H_SUDAT = np.zeros_like(z_rev)

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

for i in range(len(z_rev)-1):

    rb = rho_m(z_rev[i])

    kinetic = 0.5*phidot[i]**2
    potential = V(phi[i], rb)

    rho_phi[i] = kinetic + potential

    H = np.sqrt(rho_phi[i] + rb)

    H_SUDAT[i] = H

    phi_ddot = (
        -3.0*H*phidot[i]
        -dV(phi[i], rb)
    )

    dz = abs(z_rev[i+1]-z_rev[i])

    phidot[i+1] = (
        phidot[i]
        + phi_ddot*dz*0.02
    )

    phi[i+1] = (
        phi[i]
        + phidot[i+1]*dz*0.02
    )

# final point

rb = rho_m(z_rev[-1])

kinetic = 0.5*phidot[-1]**2
potential = V(phi[-1], rb)

rho_phi[-1] = kinetic + potential

H_SUDAT[-1] = np.sqrt(
    rho_phi[-1] + rb
)

# reverse back

H_SUDAT = H_SUDAT[::-1]

# ===================================
# NORMALIZATION
# ===================================

H_LCDM /= H_LCDM[0]
H_SUDAT /= H_SUDAT[0]

# ===================================
# DIFFERENCE
# ===================================

difference = (
    (H_SUDAT - H_LCDM)
    / H_LCDM
)*100.0

# ===================================
# FIGURE 1
# ===================================

plt.figure(figsize=(8,5))

plt.plot(z, H_LCDM, label="LCDM")
plt.plot(z, H_SUDAT, label="SUDAT")

plt.xlabel("z")
plt.ylabel("Normalized H")
plt.title("Expansion History Comparison")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("Hz_comparison.png")
plt.close()

# ===================================
# FIGURE 2
# ===================================

plt.figure(figsize=(8,5))

plt.plot(z, difference)

plt.axhline(0,color='k',ls='--')

plt.xlabel("z")
plt.ylabel("% difference")

plt.title("Relative Difference")

plt.grid()

plt.tight_layout()
plt.savefig("Hz_difference.png")
plt.close()

# ===================================
# OUTPUT
# ===================================

print("Maximum difference (%)")
print(np.max(np.abs(difference)))

print()
print("Saved:")
print("Hz_comparison.png")
print("Hz_difference.png")