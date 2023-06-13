"""Generates audio with the proton3 package."""

from absl import app
from absl import flags
from absl import logging

from proton3.one_dimensional import potentials, solver

FLAGS = flags.FLAGS

flags.DEFINE_integer('x_start', -8, 'The start of the output vector.')

flags.DEFINE_integer('x_end', 8, 'The end of the output vector.')

flags.DEFINE_integer('steps', 441, 'The number of steps in the output vector.')

flags.DEFINE_integer('state_number', 0, 'The state number of the output.')


def main(_):
    """"Generates audio with the proton3 package."""
    potential = potentials.quantum_barrier(0.5, 1, FLAGS.x_start, FLAGS.x_end, FLAGS.steps)

    hamiltonian = solver.solve(potential)
    print(hamiltonian)

if __name__ == '__main__':
    app.run(main)