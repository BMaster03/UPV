from datetime import datetime
from CodigoFFT import mi_FFT 
import matplotlib.pyplot as plt
import numpy as np

fs = 128

ts = 1.0/fs
t = np.arange(0, 1, ts)

f1 = 1
xt = 3 * np.sin(2 * np.pi * f1 * t)

f2 = 4
xt += np.sin(2 * np.pi * f2 * t)

f3 = 7
xt += 0.5 * np.sin(2 * np.pi * f3 * t)

plt.figure(figsize=(8, 6))
plt.plot(t,xt,'r')
plt.ylabel('Amplitude')
plt.grid()

Xm = mi_FFT(xt)

N = len(Xm)
n = np.arange(N)
T = N / fs
ft = n/T

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(ft, abs(Xm), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = ft[:n_oneside]

# normalize the amplitude
X_oneside =Xm[:n_oneside]/n_oneside

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude |X(freq)|')
plt.tight_layout()


def gen_sig(fs):
    ''''
Función para generar una señal 1D simple con
diferentes frecuencias de muestreo
'''
    ts = 1.0 / fs
    t = np.arange(0, 1, ts)
    freq = 1.
    xt = 3 * np.sin(2 * np.pi * freq * t)
    return xt

# frecuencia de muestreo = 2048
fs = 2048
xt = gen_sig(fs)
tini = datetime.now() # Tiempo inicial
#Xm = mi_DFT(xt)
Xm = mi_FFT(xt)
#Xm = np.fft.fft(xt)
tfin = datetime.now() # Tiempo final
c = tfin - tini # Tiempo transcurrido
print(c.microseconds)

plt.show()
