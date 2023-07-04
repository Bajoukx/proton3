"""Script for hosting proton3 in streamlit."""

from absl import app
import st_pages


def main(_):
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
