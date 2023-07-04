"""Generates files with waveforms."""

import re

import numpy as np
import scipy
import pydub


def generate_wav(waveform,
                 file_path,
                 sampling_frequency=44100,
                 scale_factor=32767):
    """Generates a .wav file from a waveform tensor."""

    if not re.search(r'\.wav$', file_path):
        file_path = file_path + '.wav'
    waveform_peak = np.max(np.abs(waveform))
    scaled_wave = np.int16(waveform / waveform_peak * scale_factor)
    scipy.io.wavfile.write(file_path, sampling_frequency, scaled_wave)


def repeat_and_save(waveform_file_path, file_path='temp_audio', n_repeats=10):
    """Repeats a waveform and saves it to a file."""
    audio = pydub.AudioSegment.from_file(waveform_file_path)
    repeated_audio = audio * n_repeats
    repeated_audio.export(file_path, format='wav')


def loop_save_raw_wave(waveform_array,
                       file_name='temp_audio.wav',
                       sampling_frequency=44100,
                       scale_factor=32767,
                       n_repeats=500):
    """Repeats a waveform and saves it to a file."""
    waveform_peak = np.max(np.abs(waveform_array))
    scaled_wave = np.int16(waveform_array / waveform_peak * scale_factor)
    waveform = pydub.AudioSegment(scaled_wave.tobytes(),
                                  frame_rate=sampling_frequency,
                                  sample_width=scaled_wave.dtype.itemsize,
                                  channels=1)
    repeated_waveform = waveform * n_repeats
    repeated_waveform.export(file_name, format='wav')
