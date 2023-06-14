"""Oscillator potentials for the Schrödinger equation."""


def harmonic_oscillator_1d(particle):
    """Harmonic oscillator function in one dimension."""
    return 0.5 * particle.x**2


def harmonic_oscillator_2d(particle):
    """Harmonic oscillator function in two dimensions."""
    return 0.5 * particle.x**2 + 0.5 * particle.y**2
