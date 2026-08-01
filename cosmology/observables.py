import numpy as np

from .equations import (
    rho_b,
    rho_phi,
    equation_of_state,
    Hubble
)

# =====================================================
# BASIC OBSERVABLES
# =====================================================

def H_of_z(phi, phidot, z):
    """
    Dimensionless Hubble parameter.
    """
    return Hubble(phi, phidot, z)


def rho_m_of_z(z):
    """
    Matter density.
    """
    return rho_b(z)


def rho_phi_of_z(phi, phidot, z):
    """
    Scalar-field density.
    """
    return rho_phi(phi, phidot, z)


def w_of_z(phi, phidot, z):
    """
    Scalar-field equation of state.
    """
    return equation_of_state(phi, phidot, z)


# =====================================================
# DENSITY FRACTIONS
# =====================================================

def Omega_m(phi, phidot, z):

    rb = rho_b(z)
    rp = rho_phi(phi, phidot, z)

    return rb / (rb + rp)


def Omega_phi(phi, phidot, z):

    rb = rho_b(z)
    rp = rho_phi(phi, phidot, z)

    return rp / (rb + rp)


# =====================================================
# EFFECTIVE EQUATION OF STATE
# =====================================================

def w_effective(phi, phidot, z):

    om = Omega_m(phi, phidot, z)
    op = Omega_phi(phi, phidot, z)

    return om * 0.0 + op * w_of_z(phi, phidot, z)


# =====================================================
# COMOVING DISTANCE
# =====================================================

def comoving_distance(z_array,
                       phi_array,
                       phidot_array):

    dc = np.zeros_like(z_array)

    for i in range(1, len(z_array)):

        dz = abs(z_array[i] - z_array[i-1])

        H = Hubble(
            phi_array[i],
            phidot_array[i],
            z_array[i]
        )

        dc[i] = dc[i-1] + dz / H

    return dc


# =====================================================
# LUMINOSITY DISTANCE
# =====================================================

def luminosity_distance(z_array,
                        phi_array,
                        phidot_array):

    dc = comoving_distance(
        z_array,
        phi_array,
        phidot_array
    )

    return (1.0 + z_array) * dc


# =====================================================
# ANGULAR DIAMETER DISTANCE
# =====================================================

def angular_diameter_distance(z_array,
                              phi_array,
                              phidot_array):

    dc = comoving_distance(
        z_array,
        phi_array,
        phidot_array
    )

    return dc / (1.0 + z_array)