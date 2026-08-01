import numpy as np

# ==========================================
# SUDAT VIABILITY SCAN
# ==========================================

print()
print("===================================")
print("SUDAT VIABILITY SCAN")
print("===================================")
print()

# ------------------------------------------
# Fixed parameters
# ------------------------------------------

Omega_m0 = 0.3

# ------------------------------------------
# Redshift grid
# ------------------------------------------

z = np.linspace(8.0, 0.0, 1500)

# ------------------------------------------
# Matter density
# ------------------------------------------

def rho_m(z):
    return Omega_m0 * (1.0 + z)**3

# ------------------------------------------
# Scan ranges
# ------------------------------------------

V0_values = [0.5, 1.0, 2.0, 5.0, 10.0]

m_values = [0.25, 0.5, 1.0, 2.0]

lam_values = [0.25, 0.5, 1.0, 2.0]

beta_values = [0.25, 0.5, 1.0, 2.0]

# ------------------------------------------
# Storage
# ------------------------------------------

healthy_models = []

# ==========================================
# Scan
# ==========================================

for V0 in V0_values:

    for m in m_values:

        for lam in lam_values:

            for beta in beta_values:

                phi = np.zeros_like(z)
                phidot = np.zeros_like(z)

                phi[0] = 1.0
                phidot[0] = 0.0

                rho_phi_values = []

                healthy = True

                # --------------------------
                # Potential
                # --------------------------

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

                # --------------------------
                # Evolution
                # --------------------------

                for i in range(len(z)-1):

                    rb = rho_m(z[i])

                    kinetic = 0.5*phidot[i]**2

                    potential = V(phi[i], rb)

                    rho_phi = kinetic + potential

                    rho_phi_values.append(rho_phi)

                    # ----------------------
                    # Health checks
                    # ----------------------

                    if np.isnan(rho_phi):
                        healthy = False
                        break

                    if rho_phi <= 0:
                        healthy = False
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
                        healthy = False
                        break

                # --------------------------
                # Save healthy models
                # --------------------------

                if healthy:

                    healthy_models.append(
                        (
                            V0,
                            m,
                            lam,
                            beta,
                            min(rho_phi_values)
                        )
                    )

# ==========================================
# Results
# ==========================================

print("Healthy models found:")
print(len(healthy_models))
print()

if len(healthy_models) > 0:

    print("Top candidates:")
    print()

    healthy_models = sorted(
        healthy_models,
        key=lambda x: x[4],
        reverse=True
    )

    for model in healthy_models[:20]:

        print(
            "V0=",
            model[0],
            " m=",
            model[1],
            " lam=",
            model[2],
            " beta=",
            model[3],
            " min_rho=",
            round(model[4],6)
        )

else:

    print("No healthy models found.")

print()
print("DONE")