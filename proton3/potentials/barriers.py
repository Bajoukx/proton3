"""Quantum barrier potentials for the Schrödinger equation."""

import numpy as np


def quantum_barrier_1d(particle, barrier_start, barrier_end, barrier_height):
    """Quantum barrier function in one dimension."""
    barrier = np.piecewise(
        particle.x, [particle.x < barrier_start, particle.x >= barrier_end],
        [0, barrier_height])
    return barrier
