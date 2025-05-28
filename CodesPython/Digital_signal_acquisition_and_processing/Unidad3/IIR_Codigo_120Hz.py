import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 1000)
xt = 0.6*np.cos(2*np.pi*60*t) + 2*np.cos(2*np.pi*120*t) + 1.4*np.sin(2*np.pi*300*t) + 0.3*np.cos(2*np.pi*2500*t)

fs = 5000.0
n = np.arange(500)
xn = 0.6*np.cos(2*np.pi*60*n/fs) + 2*np.cos(2*np.pi*120*n/fs) + 1.4*np.sin(2*np.pi*300*n/fs) + 0.3*np.cos(2*np.pi*2500*n/fs)

# Análisis de los componentes de frecuencia de la señal
N = 2**13
Xm = np.fft.fft(xn, N)
magXm = np.abs( Xm )
fan = (fs/N)*np.arange(N/2)

plt.figure(1)
plt.subplots_adjust(bottom=0.1,hspace=0.4)
plt.subplot(2,1,1)
plt.plot(fan, magXm[0:N//2])
plt.xlabel('Frecuencia (Hz)')
plt.grid()

# Fabricación del filtro
# Frecuencias en Hz
Fs1 = 70     # Frecuencia de rechazo 1
Fp1 = 110    # Frecuencia de paso 1
Fp2 = 140    # Frecuencia de paso 2
Fs2 = 180    # Frecuencia de rechazo 2

# Frecuencias normalizadas (en términos de np.pi)
ws1 = (2*Fs1)/fs    # Frecuencia de rechazo 1; ws1 = (2*np.pi*Fs1)/fs
wp1 = (2*Fp1)/fs    # Frecuencia de paso 1; (2*np.pi*Fp1)/fs
wp2 = (2*Fp2)/fs    # Frecuencia de paso 2; (2*np.pi*Fp2)/fs
ws2 = (2*Fs2)/fs    # Frecuencia de rechazo 2; (2*np.pi*Fs2)/fs

As = 30
Rp = 1
wp = [wp1, wp2] # Con esto la función sabrá que es pasabanda
ws = [ws1, ws2] # Con esto la función sabrá que es pasabanda

# Fabricación del filtro
b, a = signal.iirdesign(wp, ws, Rp, As, ftype='cheby1')
print(np.roots(a))
print(np.abs(np.roots(a)))

# Respuesta en frecuencia
w, H = signal.freqz(b, a)

# Obtención de la respuesta al impulso (n puntos)
nh, resp_imp = signal.dimpulse( (b, a, 1/fs), n=50 ) # la b son los coeficientes de las muestras de entrada y a son los de las muestras de salida

# Aplicamos el filtro sobre la señal
yn = signal.lfilter(b, a, xn)

fig = plt.figure()
fig.subplots_adjust(hspace=0.4)
plt.subplot(1,2,1)
plt.plot( w*fs/(2*np.pi), 20*np.log10( np.absolute(H)+1e-16 ) )
plt.axis([0,300,-50,0])
plt.grid()
plt.xlabel('Frecuencia (Hz)'), plt.ylabel('dB'), plt.title('Magnitud')

plt.subplot(1,2,2)
# w=2*pi*(F/fs) --> F = w*fs/(2*pi)
plt.plot( w*fs/(2*np.pi), np.abs(H) )
plt.xlabel('Frecuencia (Hz)'), plt.title('Respuesta en frecuencia (Hz)')
plt.axis([0,3000,0,1.05])
plt.grid()

# Resultado del filtrado
plt.figure()
plt.plot(n/fs, xn)
plt.plot(n/fs, yn, 'r')
plt.grid()

# DFT de la salida
Ym = np.fft.fft(yn, N)
magYm = np.abs( Ym )

plt.figure(1)
plt.subplot(2,1,2)
plt.plot(fan, 2*magYm[0:N//2], 'r')
plt.xlabel('Frecuencia (Hz)')
plt.grid()

plt.show()
