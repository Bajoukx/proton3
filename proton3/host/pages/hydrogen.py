"""The streamlit page for the hydrogen potential."""

from absl import app
import streamlit as st

from proton3.audio import file_generator
from proton3.audio import utils


def main(_):
    st.set_page_config(page_title="Hydrogen Potential")

    st.write('''
            The sound of the simulation of a hydrogen atom in one dimension.
            
            The potential of the hydrogen atom can be defined  in one dimension
            as V(x) = -1/x. This is, of course, a simplification of the
            potential of the hydrogen atom in three dimensions.
            ''')

    particle = utils.get_waferform('hydrogen_atom_1d')
    number_of_energy_levels = 30

    energy_level = st.select_slider('Energy Level',
                                    options=range(number_of_energy_levels),
                                    value=0)

    st.line_chart(particle.array[energy_level])
    file_generator.loop_save_raw_wave(particle.array[energy_level])
    st.audio('temp_audio.wav')


if __name__ == "__main__":
    app.run(main)
