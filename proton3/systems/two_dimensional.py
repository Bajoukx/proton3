"""One dimensional systems and their Schrodinger equations."""

import qmsolve

from proton3.potentials import hydrogen
from proton3.potentials import oscillators


def harmonic_oscillator(x_size=512, n_states=30):
    """Returns the eigenstates of the harmonic oscillator."""

    potential = oscillators.harmonic_oscillator_2d

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=2,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states)
    return eigenstates


def hydrogen_atom(x_size=512, n_states=30):
    """Returns the eigenstates of the hydrogen atom."""

    potential = oscillators.hydrogen_atom_2d

    hamiltonian = qmsolve.Hamiltonian(particles=qmsolve.SingleParticle(),
                                      potential=potential,
                                      spatial_ndim=2,
                                      N=x_size,
                                      extent=20)

    eigenstates = hamiltonian.solve(max_states=n_states, method='lobpcg')
    return eigenstates
