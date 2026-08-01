import numpy as np


class BackgroundIntegrator:
    """
    Numerical integrator for the SUDAT cosmological background.

    This class evolves

        phi(z)
        phidot(z)

    on a fixed redshift grid.
    """

    def __init__(self, acceleration_function):

        self.acceleration = acceleration_function

    def evolve(self,
               z_grid,
               phi0,
               phidot0,
               step_factor=0.02):

        phi = np.zeros_like(z_grid)

        phidot = np.zeros_like(z_grid)

        phi[0] = phi0
        phidot[0] = phidot0

        for i in range(len(z_grid)-1):

            dz = abs(z_grid[i+1]-z_grid[i])

            phi_ddot = self.acceleration(
                phi[i],
                phidot[i],
                z_grid[i]
            )

            phidot[i+1] = (
                phidot[i]
                + phi_ddot*dz*step_factor
            )

            phi[i+1] = (
                phi[i]
                + phidot[i+1]*dz*step_factor
            )

        return phi, phidot