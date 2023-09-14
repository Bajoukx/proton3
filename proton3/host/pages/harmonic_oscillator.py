"""The streamlit page for the harmonic oscillator potential."""

from absl import app
import streamlit as st

from proton3.audio import file_generator
from proton3.audio import utils


def main(_):
    st.set_page_config(page_title="Harmonic Oscillator Potential")

    st.write('''
            This is the sound of a particle in a harmonic oscillator potential.
             
            The potential is defined as V(x) = x^2. It is the analogue of a
            a mass on a spring in classical mechanics. In it, a particle is
            able to move freely in space, but is pulled back to the center
            by the spring.
            ''')

    particle = utils.get_waferform('quantum_oscillator_1d')

    number_of_energy_levels = 30

    energy_level = st.select_slider('Energy Level',
                                    options=range(number_of_energy_levels),
                                    value=0)

    st.line_chart(particle.array[energy_level])

    file_generator.loop_save_raw_wave(particle.array[energy_level])
    st.audio('temp_audio.wav')


if __name__ == "__main__":
    app.run(main)
