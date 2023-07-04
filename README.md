# proton3

### How it works

With proton3, we aim to create audio oscillators based on simulations
based on quantum particles. Quantum simulations can be very
computationally expensive when done on a modern computer, so we are
going to limit ourselves to systems composed of just one or two
particles.

Specifically, we are solving the Schrödinger equation with numerical
methods. If this is the first time encontering the equation, we can
think of it as an analogue of the second law of motion, which states
that $F = m a$.

In order to understand some of the nomenclature that is coming next, let
us take a quick look at the time independent Schrödinger equation
$H \psi = E \psi$. The $E$ stands for energy level, $H$ for the
Hamiltonian and $\psi$ for the wave function.

We can think of the Hamiltoninan as the variable that represents the
system that the variable lives in. The Hamiltonian is comprised of both
information about the particle itself, like it's mass, and the
environment in which the particle exists.

The energy level represents the allowed values for the particle to have.
The lowest energy level is called ground state, and then they are
counted as first energy level, second energy level, ...

We will explain the concept of wave funtion later, for now we can think
of it as the position of the particle.

A really good book to learn more about the schrödinger equation is [A Student's Guide to the Schrödinger Equation
](
https://doi.org/10.1017/9781108876841).

### A song of quantum

A quantum synthesizer that udelizes quantum wavefunctions in order to generate
sound. Kindly supported by [Quantum Social Lab](https://quantumsociallab.de/).

## Installation

Proton3 is currently under development and not yet available on PyPI. To install
the latest version, we recommend cloning the repository, create a fresh
python virtual environment and run the following command in the root directory:

```bash
pip install . -e
```

## Usage

Currently the supported potentials used to generate sound are:

- Quantum Harmonic Oscillator (One Dimensional)
- Quantum Harmonic Oscillator (Two Dimensional)
- Quantum Barrier (One Dimensional)

In the future, we plan to support:

- Double Square Well
- Hydrogen Atom
