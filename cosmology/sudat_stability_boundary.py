import numpy as np

print()
print("===================================")
print("SUDAT STABILITY BOUNDARY")
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
# Redshift grid
# ----------------------------------

z = np.linspace(8.0, 0.0, 2000)

def rho_m(z):
    return Omega_m0*(1.0+z)**3

# ----------------------------------
# Scan near the suspected boundary
# ----------------------------------

V0_values = np.arange(50, 601, 25)

healthy = []

# ----------------------------------
# Main scan
# ----------------------------------

for V0 in V0_values:

    phi = np.zeros_like(z)
    phidot = np.zeros_like(z)

    phi[0] = 1.0

    valid = True

    rho_min = 1e99

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

    for i in range(len(z)-1):

        rb = rho_m(z[i])

        kinetic = 0.5*phidot[i]**2

        potential = V(phi[i], rb)

        rho_phi = kinetic + potential

        rho_min = min(rho_min, rho_phi)

        if rho_phi <= 0:
            valid = False
            break

        H = np.sqrt(rho_phi + rb)

        phi_ddot = (
            -3.0*H*phidot[i]
            -dV(phi[i], rb)
        )

        dz = abs(z[i+1]-z[i])

        phidot[i+1] = (
            phidot[i]
            + phi_ddot*dz*0.02
        )

        phi[i+1] = (
            phi[i]
            + phidot[i+1]*dz*0.02
        )

        if abs(phi[i+1]) > 100:
            valid = False
            break

    status = "HEALTHY" if valid else "FAIL"

    print(
        f"V0 = {V0:4.0f}   "
        f"{status}"
    )

    if valid:
        healthy.append((V0, rho_min))

# ----------------------------------
# Summary
# ----------------------------------

print()
print("===================================")
print("SUMMARY")
print("===================================")
print()

if len(healthy) == 0:

    print("No stable region found.")

else:

    Vcrit = healthy[0][0]

    print("Approximate stability threshold:")
    print()

    print("V0_crit ≈", Vcrit)
    print()

    print("Healthy region:")
    print(f"V0 >= {Vcrit}")

print()
print("DONE")