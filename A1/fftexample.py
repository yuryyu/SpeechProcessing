# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10 * np.pi, 100)
# y = np.sin(x)
#
# plt.ion()
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# line1, = ax.plot(x, y, 'b-')
#
# for phase in np.linspace(0, 10 * np.pi, 100):
#     line1.set_ydata(np.sin(0.5 * x + phase))
#     fig.canvas.draw()
#


# ''' FFT example '''
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack
#
# # Number of samplepoints
# N = 600
# # sample spacing
# T = 1.0 / 800.0
# x = np.linspace(0.0, N*T, N)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# yf = scipy.fftpack.fft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
#
# fig, ax = plt.subplots()
# ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# plt.show()

import matplotlib.pyplot as plt
import numpy as np


Fs = 150.0  # sampling rate
Ts = 1.0/Fs # sampling interval
t = np.arange(0,1,Ts) # time vector

ff =12   # frequency of the signal
y = np.sin(2*np.pi*ff*t)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
print(range(int(n/2)))
frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
print('End of FFT script!')
plt.show()




# print('Start!')
# x=int(input('Enter number:'))
#
# y=x+200
# print('The input is: ' + str(y))


# import os
# print("Monitoring broadcast packets on the network for 1 minute")
# b='sudo tshark -i eth0 -R "eth.dst==FF:FF:FF:FF:FF:FF" -a duration:10>output.txt'
# os.popen(b)
# f=open('output.txt','r')
# print ("To view the type of broadcast packets open the file output.txt")
