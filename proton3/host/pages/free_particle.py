"""The streamlit page for the free particle potential."""

from absl import app
import streamlit as st

from proton3.audio import file_generator
from proton3.audio import utils


def main(_):
    st.set_page_config(page_title="Free Particle Potential")

    st.markdown('''
            This is the sound of a particle in a free particle potential.
             
            The potential is defined as V(x) = 0. It is the simplest example
            of a quantum system, as it is not affected by external forces.
            In it, a particle is able to move freely in space.
            ''')

    particle = utils.get_waferform('free_particle_1d')

    number_of_energy_levels = 30

    energy_level = st.select_slider('Energy Level',
                                    options=range(number_of_energy_levels),
                                    value=0)

    st.line_chart(particle.array[energy_level])

    file_generator.loop_save_raw_wave(
        particle.array[energy_level]
    )  #TODO: streamlit might be able to play the audio directly from the array
    st.audio('temp_audio.wav')


if __name__ == "__main__":
    app.run(main)
