import numpy as np

print()
print("===================================")
print("REALISTIC REGION SCAN")
print("===================================")
print()

# ----------------------------------
# LCDM
# ----------------------------------

Omega_m0 = 0.3
Omega_L0 = 0.7

# ----------------------------------
# SUDAT parameters
# ----------------------------------

m = 1.0
lam = 1.0
beta = 1.0

# ----------------------------------
# Redshift grid
# ----------------------------------

z = np.linspace(0, 8, 1000)

def rho_m(z):
    return Omega_m0*(1+z)**3

H_LCDM = np.sqrt(
    Omega_m0*(1+z)**3
    + Omega_L0
)

H_LCDM /= H_LCDM[0]

# ----------------------------------
# Scan
# ----------------------------------

V0_values = np.arange(225, 1001, 25)

best_V0 = None
best_difference = 1e99

results = []

for V0 in V0_values:

    z_rev = z[::-1]

    phi = np.zeros_like(z_rev)
    phidot = np.zeros_like(z_rev)

    phi[0] = 1.0

    H_SUDAT = np.zeros_like(z_rev)

    stable = True

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

        rho_phi = kinetic + potential

        if rho_phi <= 0:

            stable = False
            break

        H = np.sqrt(rho_phi + rb)

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

        if abs(phi[i+1]) > 100:

            stable = False
            break

    if not stable:
        continue

    rb = rho_m(z_rev[-1])

    kinetic = 0.5*phidot[-1]**2

    potential = V(phi[-1], rb)

    rho_phi = kinetic + potential

    H_SUDAT[-1] = np.sqrt(rho_phi + rb)

    H_SUDAT = H_SUDAT[::-1]

    H_SUDAT /= H_SUDAT[0]

    difference = np.max(
        np.abs(
            (H_SUDAT - H_LCDM)/H_LCDM
        )*100
    )

    results.append((V0, difference))

    if difference < best_difference:

        best_difference = difference
        best_V0 = V0

# ----------------------------------
# Results
# ----------------------------------

print("Top candidates")
print()

results.sort(key=lambda x: x[1])

for V0, diff in results[:15]:

    print(
        f"V0={V0:4.0f}"
        f"   max diff={diff:.2f}%"
    )

print()
print("===================================")
print("BEST MODEL")
print("===================================")
print()

print("V0 =", best_V0)
print("Maximum deviation =", best_difference, "%")

print()
print("DONE")