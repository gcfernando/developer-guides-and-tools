"""
WAV and MP3

Create a WAV tone and compare a converted MP3 with its decoded waveform.

Run: python lesson.py
Change the frequency in new_inputs.csv to a value around 280 or 900. The script creates real WAV audio from those numbers and checks an MP3 round trip.
"""

from pathlib import Path
import numpy as np
import subprocess
from imageio_ffmpeg import get_ffmpeg_exe
from scipy.fft import dct
from scipy.io import wavfile
from scipy.signal import spectrogram
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


sample_rate = 8000
seconds = np.arange(sample_rate) / sample_rate


# 1. Build a short sound from a frequency in the CSV.
def write_tone(path, frequency):
    wave = 0.4 * np.sin(2 * np.pi * frequency * seconds)
    wavfile.write(path, sample_rate, wave.astype("float32"))


def audio_features(path):
    rate, audio = wavfile.read(path)
    freqs, _, power = spectrogram(audio, fs=rate, nperseg=256)
    max_mel = 2595 * np.log10(1 + (rate / 2) / 700)
    mel_centers = np.linspace(0, max_mel, 22)
    hz_edges = 700 * (10 ** (mel_centers / 2595) - 1)
    bands = []
    for left, center, right in zip(hz_edges, hz_edges[1:], hz_edges[2:]):
        weights = np.maximum(
            0,
            np.minimum(
                (freqs - left) / (center - left), (right - freqs) / (right - center)
            ),
        )
        bands.append(weights @ power)
    log_mel = np.log(np.maximum(bands, 1e-12))
    return dct(log_mel, axis=0, norm="ortho")[:8].mean(axis=1)


features = []


# 2. Read the tone frequencies. Each row describes one sound to make.
training = pd.read_csv(input_path)
for number, tone in enumerate(training["frequency_hz"]):
    path = f"tone_{number}.wav"
    write_tone(path, tone)
    features.append(audio_features(path))
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = KNeighborsClassifier(n_neighbors=1).fit(features, training["label"])
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
new = pd.read_csv(new_path)["frequency_hz"]
write_tone("new_tone.wav", new.iloc[0])
print("One MFCC row:", len(features[0]))
print("New WAV sound:", model.predict([audio_features("new_tone.wav")]).tolist())

# Exercise MP3 decoding with the same original sound.
ffmpeg = get_ffmpeg_exe()
subprocess.run(
    [ffmpeg, "-loglevel", "error", "-y", "-i", "new_tone.wav", "tone.mp3"], check=True
)
subprocess.run(
    [
        ffmpeg,
        "-loglevel",
        "error",
        "-y",
        "-i",
        "tone.mp3",
        "-ar",
        str(sample_rate),
        "-ac",
        "1",
        "decoded.wav",
    ],
    check=True,
)
print("Decoded MP3 sound:", model.predict([audio_features("decoded.wav")]).tolist())
for tone in new.iloc[1:]:
    write_tone("another_tone.wav", tone)
    print(tone, model.predict([audio_features("another_tone.wav")])[0])
