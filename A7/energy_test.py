import wave
import pylab as pl
import numpy as np
import Volume as vp

file_pool = ['Al_page_13_78.wav']
file_path = 'A1/'

for file_name in file_pool:
    fw = wave.open(file_path+file_name,'r')
    params = fw.getparams()
    print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = fw.readframes(nframes)
    waveData = np.frombuffer(strData, dtype=np.int16)
    waveData = waveData*1.0/max(abs(waveData))  # normalization
    fw.close()

    # calculate volume
    frameSize = 256
    overLap = 128
    volume11 = vp.calVolume(waveData,frameSize,overLap)
    volume12 = vp.calVolumeDB(waveData,frameSize,overLap)

    # plot the wave
    time = np.arange(0, nframes)*(1.0/framerate)
    time2 = np.arange(0, len(volume11))*(frameSize-overLap)*1.0/framerate
    pl.subplot(311)
    pl.plot(time, waveData)
    pl.ylabel("Amplitude")
    pl.title('Energy of ' + file_name)

    pl.subplot(312)
    pl.plot(time2, volume11)
    pl.ylabel("absSum")

    pl.subplot(313)
    pl.plot(time2, volume12, c="g")
    pl.ylabel("Decibel(dB)")
    pl.xlabel("time (seconds)")
    pl.savefig("Energy_" + file_name.split('.wav')[0] + ".png")
    pl.show()
    pl.clf()


print('Test nicely ended, check root folder, please!')