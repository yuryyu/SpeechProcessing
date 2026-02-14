import sounddevice as sd
from scipy.io.wavfile import write


file_name = "output_ee.wav"
fs = 44100  # Sample rate
seconds = 2  # Duration of recording
print('Start recording')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
sd.wait()  # Wait until recording is finished
print('Stop recording')
write(file_name, fs, myrecording)  # Save as WAV file