"""The streamlit page for the harmonic oscillator potential."""

from absl import app
import streamlit as st

from proton3.audio import utils

def main(_):
    st.set_page_config(
        page_title="Harmonic Oscillator Potential"
        )

    st.write("In development...")


if __name__ == "__main__":
    app.run(main)
