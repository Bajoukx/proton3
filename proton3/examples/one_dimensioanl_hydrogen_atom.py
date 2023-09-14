"""A representation of the hydrogen atom in one dimension."""

from absl import app
from absl import flags
from absl import logging

import qmsolve

from proton3.systems import one_dimensional

FLAGS = flags.FLAGS

flags.DEFINE_bool('visualize', False, 'Visualize the wavefunction.')


def main(_):
    """Generates the potential and solves the Schrodinger equation."""
    eigenstates = one_dimensional.hydrogen_atom()
    logging.debug('\n' + str(eigenstates.energies))

    if FLAGS.visualize:
        visualization = qmsolve.init_visualization(eigenstates)
        visualization.slider_plot()


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    app.run(main)