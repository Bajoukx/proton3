"""A coletion of potentials for the schrodinger equation."""

import math

import numpy as np
import torch


def analytical_quantum_oscillator(state_number: int,
                                  x_start: float = -8,
                                  x_end: float = 8,
                                  steps: int = 441):
    """The analitical solution of the quantum harmonic oscillator.
    
    You can find the derivation of this function in the following link:
    https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator

    Args:
        state_number: The state number of the output.
        x_start: The start of the output vector.
        x_end: The end of the output vector.
        steps: The number of steps in the output vector.
    """
    feasible_vector = torch.linspace(x_start, x_end, steps)

    first_term = 1 / np.sqrt(2**state_number * np.math.factorial(state_number))
    second_term = (1 / math.pi)**(1 / 4)
    third_term = np.exp(
        -(feasible_vector**2) / 2) * torch.special.hermite_polynomial_h(
            feasible_vector, state_number)

    return first_term * second_term * third_term


def solve(potential):
    """Solves the schrodinger equation for a given potential.

    Args:
        potential: The potential function.
    """
    diagonal_potential = torch.diag(potential)

    potential_size = len(potential)
    ones = torch.ones_like(potential_size -1)
    super_diagonal = torch.diag(ones, diagonal=1)
    sub_diagonal = torch.ones_like(ones, diagonal=1)
    diagonal= torch.diag(ones - 3)

    hamiltonian = diagonal_potential + (diagonal + super_diagonal + sub_diagonal)

    return hamiltonian