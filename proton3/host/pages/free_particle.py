"""The streamlit page for the free particle potential."""

from absl import app
import streamlit as st

from proton3.audio import utils

def main(_):
    st.set_page_config(
        page_title="Free Particle Potential"
        )

    st.write("This is the sound of a particle in a free particle potential.")

    particle = utils.get_waferform('free_particle_1d')
    st.line_chart(particle.array[0])

if __name__ == "__main__":
    app.run(main)