"""Example of a 1 Dimensional harmonic oscillator."""

from absl import app
from absl import flags
from absl import logging

import qmsolve

from proton3.systems import two_dimensional

FLAGS = flags.FLAGS

flags.DEFINE_bool('visualize', False, 'Visualize the wavefunction.')


def main(_):
    """Generates the potential and solves the Schrodinger equation."""
    eigenstates = two_dimensional.harmonic_oscillator()
    logging.debug('\n' + str(eigenstates.energies))

    if FLAGS.visualize:
        visualization = qmsolve.init_visualization(eigenstates)
        visualization.slider_plot()


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    app.run(main)
