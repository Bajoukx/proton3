"""Utils for audio processing."""

from proton3.systems import one_dimensional
from proton3.systems import two_dimensional


def read_wav_as_bytes(file_path):
    """Reads a wav file and returns it as bytes."""
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    return audio_bytes

def get_waferform(waveform_name):
    """Returns a waveform tensor."""
    if waveform_name == 'free_particle_1d':
        return one_dimensional.free_particle()
    if waveform_name == 'quantum_oscillator_1d':
        return one_dimensional.harmonic_oscillator()
    if waveform_name == 'quantum_barrier_1d':
        return one_dimensional.quantum_barrier()
    if waveform_name == 'quantum_oscillator_2d':
        return two_dimensional.harmonic_oscillator()
    raise ValueError('Unknown waveform: ' + waveform_name)
