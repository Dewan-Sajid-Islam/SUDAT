import numpy as np

# =====================================================
# SUDAT MODEL PARAMETERS
# =====================================================

Omega_m0 = 0.30

m = 1.0
lam = 1.0
beta = 1.0

V0 = 225.0

# =====================================================
# BACKGROUND MATTER DENSITY
# =====================================================

def rho_b(z):
    """
    Background matter density.
    """
    return Omega_m0 * (1.0 + z)**3


# =====================================================
# SUDAT POTENTIAL
# =====================================================

def potential(phi, z):
    """
    Scalar-field potential.
    """

    rb = rho_b(z)

    return (
        V0
        + 0.5 * (m*m - 2.0*lam*rb) * phi**2
        + 0.25 * beta * phi**4
    )


# =====================================================
# POTENTIAL DERIVATIVE
# =====================================================

def dV_dphi(phi, z):
    """
    dV/dphi
    """

    rb = rho_b(z)

    return (
        (m*m - 2.0*lam*rb) * phi
        + beta * phi**3
    )


# =====================================================
# KINETIC ENERGY
# =====================================================

def kinetic(phidot):

    return 0.5 * phidot**2


# =====================================================
# SCALAR ENERGY DENSITY
# =====================================================

def rho_phi(phi, phidot, z):

    return (
        kinetic(phidot)
        + potential(phi, z)
    )


# =====================================================
# SCALAR PRESSURE
# =====================================================

def pressure(phi, phidot, z):

    return (
        kinetic(phidot)
        - potential(phi, z)
    )


# =====================================================
# EQUATION OF STATE
# =====================================================

def equation_of_state(phi, phidot, z):

    rho = rho_phi(phi, phidot, z)

    p = pressure(phi, phidot, z)

    return p / (rho + 1e-12)


# =====================================================
# FRIEDMANN EQUATION
# =====================================================

def Hubble(phi, phidot, z):
    """
    Dimensionless Hubble parameter.
    """

    return np.sqrt(
        rho_b(z)
        + rho_phi(phi, phidot, z)
    )


# =====================================================
# KLEIN-GORDON EQUATION
# =====================================================

def phi_acceleration(phi, phidot, z):
    """
    Scalar-field acceleration.
    """

    H = Hubble(phi, phidot, z)

    return (
        -3.0 * H * phidot
        - dV_dphi(phi, z)
    )