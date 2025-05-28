import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 0.05, 10000)
xt = 2.5 + np.sin(2*np.pi*60*t) + np.sin(2*np.pi*240*t)

fs = 2000.0
n = np.arange(500)
xn = 2.5 + np.sin(2*np.pi*60*n/fs) + np.sin(2*np.pi*240*n/fs)

plt.figure(1)

plt.plot(t, xt)
plt.grid()
plt.title("Sinusoide en tiempo continuo")

# Análisis de los componentes de frecuencia de la señal
N = 2**13
Xm = np.fft.fft(xn - 2.5, N)
magXm = np.abs( Xm )
fan = (fs/N)*np.arange(N/2)

plt.figure(2)
plt.subplots_adjust(bottom=0.1,hspace=0.4)
plt.subplot(2,1,1)
plt.plot(fan, magXm[0:N//2])
plt.xlabel('Frecuencia (Hz)')
plt.grid() 

# Fabricación del filtro
# Frecuencias en Hz
Fp1 = 60   # Frecuencia de paso 1
Fs1 = 220     # Frecuencia de rechazo 1

# Frecuencias normalizadas (en términos de np.pi)
wp1 = (2*Fp1)/fs    # Frecuencia de paso 1; (2*np.pi*Fp1)/fs
ws1 = (2*Fs1)/fs    # Frecuencia de rechazo 1; ws1 = (2*np.pi*Fs1)/fs

As = 20
Rp = 1

# Fabricación del filtro
b, a = signal.iirdesign(wp1, ws1, Rp, As, ftype='cheby1')
print(b)
print(a)

# Respuesta en frecuencia
w, H = signal.freqz(b, a)

fig = plt.figure(3)
fig.subplots_adjust(hspace=0.4)
plt.subplot(1,2,1)
plt.plot( w*fs/(2*np.pi), 20*np.log10( np.absolute(H)+1e-16 ) )
plt.axis([0,300,-50,0])
plt.grid()
plt.xlabel('Frecuencia (Hz)'), plt.ylabel('dB'), plt.title('Magnitud')

# Obtención de la respuesta al impulso (n puntos)
# nh, resp_imp = signal.dimpulse( (b, a, 1/fs), n=50 ) # la b son los coeficientes de las muestras de entrada y a son los de las muestras de salida

# Aplicamos el filtro sobre la señal
yn = signal.lfilter(b, a, xn)

plt.subplot(1,2,2)
# w=2*pi*(F/fs) --> F = w*fs/(2*pi)
plt.plot( w*fs/(2*np.pi), np.abs(H) )
plt.xlabel('Frecuencia (Hz)'), plt.title('Respuesta en frecuencia (Hz)')
plt.axis([0,300,0,1.05])
plt.grid()

# Resultado del filtrado
plt.figure()
plt.plot(n/fs, xn)
plt.plot(n/fs, yn, 'r')
plt.grid()

# DFT de la salida
Ym = np.fft.fft(yn-2.5, N)
magYm = np.abs( Ym )

plt.figure(2)
plt.subplot(2,1,2)
plt.plot(fan, magYm[0:N//2], 'r')
plt.xlabel('Frecuencia (Hz)')
plt.grid()

plt.show()
