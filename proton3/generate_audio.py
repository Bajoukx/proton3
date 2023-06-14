"""Generate audio as a wav file."""

import os

from absl import app
from absl import flags
from absl import logging

from proton3.audio import file_generator
from proton3.systems import one_dimensional

FLAGS = flags.FLAGS

flags.DEFINE_string('file_path', 'files',
                    'Path to the output file inside audio directory.')

flags.DEFINE_integer('sampling_frequency', 44100, 'Sampling frequency.')

flags.DEFINE_integer('scale_factor', 32767, 'Scale factor.')

flags.DEFINE_integer('eigenstate', 0, 'Eigenstate to generate.')

flags.DEFINE_string('waveform', 'quantum_oscillator_1d',
                    'Type of waveform to generate.')


def get_waferform(waveform_name):
    """Returns a waveform tensor."""
    if waveform_name == 'quantum_oscillator_1d':
        return one_dimensional.harmonic_oscillator()
    if waveform_name == 'quantum_barrier_1d':
        return one_dimensional.quantum_barrier()
    raise ValueError('Unknown waveform: ' + waveform_name)


def main(_):
    """Generates a waveform and saves it to a file."""

    waveform = get_waferform(FLAGS.waveform).array[:, FLAGS.eigenstate]

    file_name = FLAGS.waveform + '_' + str(FLAGS.eigenstate)
    file_path = os.path.join('audio_files', FLAGS.file_path, file_name)

    file_generator.generate_wav(waveform, file_path, FLAGS.sampling_frequency,
                                FLAGS.scale_factor)


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    app.run(main)
