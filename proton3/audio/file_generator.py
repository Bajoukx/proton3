"""Generates files with waveforms."""

import scipy
import numpy as np


def generate_wav(waveform,
                 file_path,
                 sampling_frequency=44100,
                 scale_factor=32767):
    """Generates a .wav file from a waveform tensor."""

    file_path = file_path + '.wav'
    waveform_peak = np.max(np.abs(waveform))
    scaled_wave = np.int16(waveform / waveform_peak * scale_factor)
    scipy.io.wavfile.write(file_path, sampling_frequency, scaled_wave)
