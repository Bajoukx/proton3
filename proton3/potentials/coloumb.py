"""Coloumb potentials."""

import numpy as np

#from proton.constants import atomic_units 


def coloumb_potential_1d(particle):
    """Coloumb potential in one dimension."""
    k_c = 1.0

    r = np.sqrt((particle.x)**2)
    r = np.where(r < 0.000001, 0.000001, r)
    
    #external_electric_field = 1e3 * atomic_units.ELECTRONVOLT / m #shows Stark effect

    return - k_c / r + particle.x # * external_electric_field

