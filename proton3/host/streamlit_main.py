"""Script for hosting proton3 in streamlit."""

from absl import app

import streamlit as st
from st_pages import Page, add_page_title, show_pages


def main(_):
    with st.echo('below'):
        show_pages([
            Page('proton3/host/pages/home.py', 'ProTon3'),
            Page('proton3/host/pages/free_particle.py', 'Free Particle'),
            Page('proton3/host/pages/hydrogen.py', 'Hydrogen Atom'),
            Page('proton3/host/pages/harmonic_oscillator.py',
                 'Harmonic Oscillator'),
            Page('proton3/host/pages/quantum_barrier.py', 'Quantum Barrier'),
        ])
        add_page_title()


if __name__ == "__main__":
    app.run(main)
