import sys
import platform
import sounddevice as sd
from scipy.io.wavfile import write

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()
print(f"Running on: {OS_NAME} ({PLATFORM})")

fs = 44100  # Sample rate
seconds = 3  # Duration of recording
print('Start recording')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print('Stop recording')
write('output_one.wav', fs, myrecording)  # Save as WAV file