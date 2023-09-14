"""The streamlit page for the quantum barrier potential."""

from absl import app
import streamlit as st

from proton3.audio import file_generator
from proton3.audio import utils


def main(_):
    st.set_page_config(page_title="Quantum Barrier Potential")

    st.write('''
            This is the sound of a particle in a quantum barrier potential.

            The potential is defined as V(x) = 0 for all space apart from a
            small region, where it is defined as V(x) = 1. This potential is
            used to model the tunneling effect, where a particle is able to
            pass through a barrier that it would not be able to pass through
            classically.
            ''')

    particle = utils.get_waferform('quantum_barrier_1d')

    number_of_energy_levels = 30

    energy_level = st.select_slider('Energy Level',
                                    options=range(number_of_energy_levels),
                                    value=0)

    st.line_chart(particle.array[energy_level])

    file_generator.loop_save_raw_wave(particle.array[energy_level])
    st.audio('temp_audio.wav')


if __name__ == "__main__":
    app.run(main)