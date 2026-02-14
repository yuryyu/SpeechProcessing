import sys
import platform
import sounddevice as sd
import soundfile as sf

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()
print(f"Running on: {OS_NAME} ({PLATFORM})")

filename = 'output_one.wav'
AMP = 2  # Amplify data - increase Volume of sound
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')
plot_enable = True
if plot_enable:
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()
print('Starting playing')
sd.play(data*AMP, fs)
status = sd.wait()  # Wait until file is done playing
print('Stop playing')
