"""Script for hosting proton3 in streamlit."""

from absl import app
import streamlit as st
import st_pages


def main(_):
    st.set_page_config(page_title="Proton3")
    st.write("Welcome to proton3!")
    st.markdown("""
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
        """)

    st_pages.show_pages(
        [
            st_pages.Page('proton3/host/pages/home.py', 'ProTon3'),
            st_pages.Section(name='One Dimensional Systems'),
            st_pages.Page('proton3/host/pages/free_particle.py', 'Free Particle'),
            st_pages.Page('proton3/host/pages/harmonic_oscillator.py', 'Harmonic Oscillator')
        ]
    )
    st_pages.add_indentation()

if __name__ == "__main__":
    app.run(main)
