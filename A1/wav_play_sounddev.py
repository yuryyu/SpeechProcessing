# Cross-platform WAV file playback
# Supported platforms: Windows, macOS, Linux

import sys
import platform

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()
print(f"Running on: {OS_NAME} ({PLATFORM})")

import sounddevice as sd
import soundfile as sf

filename = 'Al_page_13_78.wav'
plot_enable = True

AMP = 1.2  # Amplify data - increase Volume of sound
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')

if plot_enable:
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()
print('Starting playing')
sd.play(data*AMP, fs)
status = sd.wait()  # Wait until file is done playing
print('Stop playing')