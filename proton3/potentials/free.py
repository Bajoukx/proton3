"""The potential for free particles."""

import numpy as np


def free_particle_1d(particle):
    """The potential for free particles."""
    return np.zeros_like(particle.x)
