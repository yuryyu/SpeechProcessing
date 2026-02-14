import wave
import numpy as np
import matplotlib.pyplot as plt
import math


file_name = "output_ee.wav" #"Al_page_13_78.wav"


def power_log(x):
    return 2**(math.ceil(math.log(x, 2)))


fw = wave.open(file_name,'r')
print(fw.getparams())
soundInfo = fw.readframes(-1)
soundInfo = np.fromstring(soundInfo, np.int16)
f = fw.getframerate()
fw.close()
timeline = np.linspace(0, len(soundInfo)/f, len(soundInfo))

plt.subplot(211)
plt.plot(timeline, soundInfo)
plt.ylabel('Amplitude')
plt.title('Wave and spectrogram of '+file_name)
plt.axis([0, len(soundInfo)/f, np.min(soundInfo)*1.03, np.max(soundInfo)*1.03])

plt.subplot(212)
time_window = 0.04  # 40 ms
NFFTs=power_log((f*time_window))
#  NFFTs = 256 # 256 -> Fs/256= sec,
plt.specgram(soundInfo, NFFT=NFFTs,Fs=f)
plt.ylabel('Frequency')
plt.xlabel('time(seconds)')
plt.savefig("spectrogram_"+file_name.split('.wav')[0]+".png")
plt.show()
plt.clf()
