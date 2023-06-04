"""Generates files with waveforms."""

import scipy
import numpy as np


def generate_wav(waveform_tensor,
                 file_path,
                 sampling_frequency=44100,
                 scale_factor=32767):
    """Generates a .wav file from a waveform tensor."""
    numpy_waveform = waveform_tensor.numpy()
    waveform_peak = np.max(np.abs(waveform_tensor))
    scaled_wave = np.int16(numpy_waveform / waveform_peak * scale_factor)
    scipy.io.wavfile.write(file_path, sampling_frequency, scaled_wave)
