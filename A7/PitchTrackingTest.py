import wave
import numpy as np
import pylab as pl
import PitchTracking as pt

# read wave file and get parameters.

file_pool = ['Al_page_13_78.wav']
file_path = 'A1/'

for indx,file_name in enumerate(file_pool):
    fw = wave.open(file_path+file_name,'r')

    params = fw.getparams()
    print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = fw.readframes(nframes)
    waveData = np.frombuffer(strData, dtype=np.int16)
    waveData = waveData*1.0/max(abs(waveData))  # normalization
    fw.close()

    # plot the wave
    time = np.arange(0, len(waveData)) * (1.0 / framerate)

    frameSize = 2048 # 512 matched for Fs=16k, 2048 for Fs=16k
    overLap = frameSize/2
    adxs=[0.9, 1.3, 0.9, 2.6]
    idx1 = int(adxs[indx]*framerate)
    print(idx1)
    idx2 = idx1+frameSize
    index1 = idx1*1.0 / framerate
    index2 = idx2*1.0 / framerate
    acf = pt.ACF(waveData[idx1:idx2])
    acf[0:10] = -acf[0]
    acfmax = np.argmax(acf)
    print('Autocorrelation Function Max Value:  '+str(acfmax))
    print(framerate*1.0/acfmax)

    pl.subplot(411)
    pl.title("ACF (Pitch Track)")
    pl.plot(time, waveData)
    pl.plot([index1,index1],[-1,1],'r')
    pl.plot([index2,index2],[-1,1],'r')
    pl.xlabel("time (seconds)")
    pl.ylabel("Amplitude")

    pl.subplot(412)
    pl.plot(np.arange(frameSize),waveData[idx1:idx2],'r')
    pl.xlabel("index in 1 frame")
    pl.ylabel("Amplitude")

    pl.subplot(413)
    pl.plot(np.arange(frameSize),acf,'g')
    pl.xlabel("index in 1 frame")
    pl.ylabel("ACF")

    # pitch tracking
    acfmethod = pt.ACF
    pitchtrack = pt.PitchTrack(waveData, framerate, frameSize, overLap, acfmethod)
    xpt = np.arange(0, len(pitchtrack)) *( len(waveData) *1.0/ len(pitchtrack) / framerate )
    pl.subplot(414)
    pl.plot(xpt,pitchtrack,'-*')
    pl.xlabel('time (seconds)')
    pl.ylabel('Frequency (Hz)')

    pl.savefig("ACF_" + file_name.split('.wav')[0] + ".png")
    pl.show()
    pl.clf()

# pl.show()
print('Test nicely ended, check root folder, please!')



