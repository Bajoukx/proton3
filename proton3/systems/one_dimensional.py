"""One dimensional systems and their Schrodinger equations."""

from functools import partial

import qmsolve

from proton3.potentials import barriers
from proton3.potentials import coloumb
from proton3.potentials import free
from proton3.potentials import oscillators


def harmonic_oscillator(x_size=512, n_states=30):
    """Returns the eigenstates of the harmonic oscillator."""

    potential = oscillators.harmonic_oscillator_1d

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=1,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states)
    return eigenstates


def quantum_barrier(
        barrier_start=1,  # pylint: disable=unused-argument
        barrier_end=1.1,  # pylint: disable=unused-argument
        barrier_height=1,  # pylint: disable=unused-argument
        x_size=512,
        n_states=30):
    """Returns the eigenstates of the harmonic oscillator."""

    potential = partial(barriers.quantum_barrier_1d,
                        barrier_start=1,
                        barrier_end=1.1,
                        barrier_height=1)

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=1,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states)
    return eigenstates


def free_particle(x_size=512, n_states=30):
    """Returns the eigenstates of a free particle"""

    potential = partial(free.free_particle_1d)

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=1,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states)
    return eigenstates


def hydrogen_atom(x_size=512, n_states=30):
    """Returns the eigenstates of the hydrogen atom."""

    potential = partial(coloumb.coloumb_potential_1d)

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=1,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states)
    return eigenstates
