"""Collection of potentials for the schrodinger equation."""

import torch


def quantum_barrier(width, height, x_start, x_end, steps):
    """A potential barrier.

    Args:
        width: The width of the barrier.
        height: The height of the barrier.
        x_start: The start of the output vector.
        x_end: The end of the output vector.
        steps: The number of steps in the output vector.
    """
    feasible_vector = torch.linspace(x_start, x_end, steps)
    barrier = torch.zeros_like(feasible_vector)
    barrier[feasible_vector.abs() < width] = height
    return barrier
