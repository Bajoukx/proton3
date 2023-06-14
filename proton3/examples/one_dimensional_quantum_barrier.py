"""Example of a 1 Dimensional harmonic oscillator."""

from absl import app
from absl import flags
from absl import logging

import qmsolve

from proton3.systems import one_dimensional

FLAGS = flags.FLAGS

flags.DEFINE_float('barr_start', 1.0, 'Start of the barrier.')

flags.DEFINE_float('barr_end', 1.1, 'End of the barrier.')

flags.DEFINE_float('barr_height', 1.0, 'Height of the barrier.')

flags.DEFINE_bool('visualize', False, 'Visualize the wavefunction.')


def main(_):
    """Generates the potential and solves the Schrodinger equation."""
    eigenstates = one_dimensional.quantum_barrier(FLAGS.barr_start,
                                                  FLAGS.barr_end,
                                                  FLAGS.barr_height)
    logging.debug('\n' + str(eigenstates.energies))

    if FLAGS.visualize:
        visualization = qmsolve.init_visualization(eigenstates)
        visualization.slider_plot()


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    app.run(main)
