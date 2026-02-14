# Cross-platform audio playback with conditional imports
# Supported platforms: Windows, macOS, Linux

import sys
import platform
import numpy as np

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()
print(f"Running on: {OS_NAME} ({PLATFORM})")

# Conditional import for audio library
try:
    import simpleaudio as sa
    print("Using simpleaudio for audio playback")
except ImportError:
    print("Warning: simpleaudio not available. Audio playback may not work.")
    sa = None

plot_enable = True # False

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 3  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

if plot_enable:
    import matplotlib.pyplot as plt
    plt.plot(audio)
    plt.show()

# Start playback
if sa is not None:
    print('Start playback')
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    # Wait for playback to finish before exiting
    play_obj.wait_done()
    print('Stop playback')
else:
    print('Error: simpleaudio is required for audio playback')
