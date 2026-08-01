import numpy as np

print()
print("===================================")
print("SUDAT MASS SCAN")
print("===================================")
print()

# ----------------------------------
# LCDM
# ----------------------------------

Omega_m0 = 0.3
Omega_L0 = 0.7

# ----------------------------------
# Fixed SUDAT parameters
# ----------------------------------

V0 = 225

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
# Mass scan
# ----------------------------------

m_values = [
    0.1,
    0.2,
    0.5,
    1.0,
    2.0,
    3.0,
    5.0,
    10.0
]

results = []

# ----------------------------------
# Main loop
# ----------------------------------

for m in m_values:

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
            - dV(phi[i], rb)
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

        print(f"m = {m:4.1f}   FAILED")
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

    results.append((m, difference))

    print(
        f"m = {m:4.1f}"
        f"   max diff = {difference:.2f}%"
    )

# ----------------------------------
# Summary
# ----------------------------------

print()
print("===================================")
print("BEST MASS")
print("===================================")
print()

if len(results) == 0:

    print("No stable models found.")

else:

    results.sort(
        key=lambda x: x[1]
    )

    best_m, best_diff = results[0]

    print("m =", best_m)
    print("Maximum deviation =", best_diff, "%")

print()
print("DONE")