"""The streamlit page for the harmonic oscillator potential."""

from absl import app
import streamlit as st

from proton3.audio import utils

def create_button_column(subtitle, button_names):
    st.write(f"## {subtitle}")
    for i, button_name in enumerate(button_names, start=1):
        st.button(f"{subtitle} {i}. {button_name}")

def main(_):
    st.set_page_config(page_title="Harmonic Oscillator Potential")

    title_html = """
    <div style="font-family: 'Brush Script MT', cursive; font-size: 48px; color: hotpink; text-shadow: 2px 2px 8px hotpink;">
        Harmonic Oscillator Potential
    </div>
"""
    st.markdown(title_html, unsafe_allow_html=True)

    # Create two columns for positive and negative buttons
    col1, col2 = st.columns(2)

    # List of buttons for positive and negative columns
    positive_buttons = ["Confidence", "Curiosity", "Optimism", "Familiarity", "Control", "Clarity", "Validation"]
    negative_buttons = ["Fear", "Uncertainty", "Disempowerment", "Mistrust", "Apprehension", "Concern", "Confusion"]

    # Create the button columns
    with col1:
        create_button_column("Positive", positive_buttons)

    with col2:
        create_button_column("Negative", negative_buttons)

if __name__ == "__main__":
    app.run(main)
