"""Oscillator potentials for the Schrödinger equation."""

from proton3 import constants


def harmonic_oscillator_1d(particle):
    """Harmonic oscillator function in one dimension."""
    k = 100 * constants.ELECTRONVOLT / constants.ANGSTROM**2
    return 0.5 * k * particle.x**2


def harmonic_oscillator_2d(particle):
    """Harmonic oscillator function in two dimensions."""
    kx = 0.02
    ky = 0.02
    return 0.5 * kx * particle.x**2 + 0.5 * ky * particle.y**2
