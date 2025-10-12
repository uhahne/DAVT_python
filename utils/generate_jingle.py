import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numpy as np
# Parameters for the jingle
sampling_rate = 44100  # Sampling rate in Hz
duration = 2  # Duration of the jingle in seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time axis

# Parameters for the new jingle
tone_duration = 0.4  # Duration of a single tone in seconds
silence_duration = 0.1  # Pause between tones in seconds
sampling_rate = 44100  # Sampling rate in Hz

# Frequencies of the tones in Hz (a simple melody)
frequencies = [440, 554, 659, 440, 349, 440]  # A, C#, E, A, F, A

# Create jingle
jingle = []

for freq in frequencies:
    # Sine tone for the given frequency
    t_tone = np.linspace(0, tone_duration, int(sampling_rate * tone_duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t_tone)
    jingle.append(tone)
    # Silence between tones
    t_silence = np.zeros(int(sampling_rate * silence_duration))
    jingle.append(t_silence)

# Concatenation of tones and silence into a signal
jingle = np.concatenate(jingle)

# Normalize the signal to the value range of int16
jingle = (jingle / np.max(np.abs(jingle)) * 32767).astype(np.int16)

# Save as WAV file
file_path = "./data/jingle.wav"
wavfile.write(file_path, sampling_rate, jingle)

# Load the original WAV file
sampling_rate, jingle = wavfile.read(file_path)

# Play the signal twice as fast (pitch up)
new_sampling_rate = sampling_rate * 2  # Double the playback speed

# Save the new file with changed sampling rate
file_path_fast = "./data/jingle_fast.wav"
wavfile.write(file_path_fast, int(new_sampling_rate), jingle)

# Play the signal half as fast (pitch down)
new_sampling_rate = sampling_rate // 2  # Halve the playback speed

# Save the new file with changed sampling rate
file_path_slow = "./data/jingle_slow.wav"
wavfile.write(file_path_slow, int(new_sampling_rate), jingle)

# Play the signal backwards
jingle_reversed = jingle[::-1]
file_path_reversed = "./data/jingle_reversed.wav"
wavfile.write(file_path_reversed, sampling_rate, jingle_reversed)

# reduce the volume to 30%
jingle_quiet = (jingle * 0.3).astype(np.int16)
file_path_quiet = "./data/jingle_quiet.wav"
wavfile.write(file_path_quiet, sampling_rate, jingle_quiet)