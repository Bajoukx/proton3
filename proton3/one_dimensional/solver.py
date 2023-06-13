"""Solves the schrodinger equation for a given potential."""

import torch


def solve(potential):
    """Solves the schrodinger equation for a given potential.

    Args:
        potential: The potential function.
    """
    diagonal_potential = torch.diag(potential)
    print(diagonal_potential)

    potential_size = len(potential)
    ones = torch.ones(potential_size - 1)
    super_diagonal = torch.diag(ones, diagonal=1)
    sub_diagonal = torch.diag(ones, diagonal=1)

    diagonal_value = torch.ones(potential_size) - 3
    diagonal = torch.diag(diagonal_value)

    print(sub_diagonal)
    hamiltonian = diagonal_potential + (diagonal + super_diagonal +
                                        sub_diagonal)

    return hamiltonian
