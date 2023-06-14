"""One dimensional systems and their Schrodinger equations."""

import qmsolve

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
