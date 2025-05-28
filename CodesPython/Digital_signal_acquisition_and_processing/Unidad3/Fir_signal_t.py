import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from funciones_filtrado import fpb_ideal, resp_frec

t = np.linspace(0, 1, 1000)

x_t = 0.6*np.sin(2*np.pi*60*t) + 2*np.cos(2*np.pi*120*t) + 1.4*np.sin(2*np.pi*300*t) + 0.3*np.cos(2*np.pi*2500*t)

fs = 5000.0
n = np.arange(500)

x_n = 0.6*np.sin(2*np.pi*60*n/fs) + 2*np.cos(2*np.pi*120*n/fs) + 1.4*np.sin(2*np.pi*300*n/fs) + 0.3*np.cos(2*np.pi*2500*n/fs)

N = 2 ** 13

Xm = np.fft.fft(x_n, N)
magXm = np.abs(Xm)
fan = (fs/N) * np.arange(N//2)

plt.figure()
plt.plot(fan, magXm[0:N//2])
plt.grid()

# frecuencias del filtro, en Hz

Fs1 = 65
Fp1 = 110
Fp2 = 130
Fs2 = 165

# frecuencia angular discreta

ws1 = 2*np.pi*Fs1/fs # 2PI*F/fs => multiplicar dos veces Pi por la Frecuencia en tiempo continuo y todo esto sobre la frecuencia de muestreo
wp1 = 2*np.pi*Fp1/fs
wp2 = 2*np.pi*Fp2/fs
ws2 = 2*np.pi*Fs2/fs

As = 45

# Banda de transición 

delta_w = np.min([wp1-ws1, ws2 -wp2])
M = int(np.ceil((6.6 * np.pi)/(delta_w)) + 1)
n2 = np.arange(M)

wc1 = (ws1 + wp1)/2 # frecuencia de corte del filtro PB ideal 
wc2 = (wp2 + ws2)/2 # frecuencia de corte del filtro PB ideal 

hw = signal.firwin(M, [wc1/np.pi, wc2/np.pi], pass_zero = False, window = 'hamming')

mag, ang, dB, ome = resp_frec(hw, 2 ** 13)

# Aplicación del filtro construido

Hm = np.fft.fft(hw, N)

Ym = Xm * Hm

ynen = np.fft.ifft(Ym)

limi = (len(hw) - 1)/2
lims = limi + len(x_n)

yn = ynen[int(limi): int(lims)]


# calculadora de la convolución (dominio del timpo)
yncon = np.convolve(x_n, hw)
ync = yncon[int(limi) : int(lims)]

plt.figure()

plt.subplot(3,1,1)
plt.stem(n2,np.hamming(M))
plt.grid()
plt.title("Respuesta al impulso con ventana")
plt.xlabel("n")
plt.ylabel("h(n)")

plt.subplot(3,1,2)
plt.stem(n2, hw)
plt.grid()
plt.title("Ventana Hamming")
plt.xlabel("n")
plt.ylabel("w(n)")

plt.subplot(3,1,3)
plt.plot(ome/np.pi, dB, 'b')
plt.plot(ome/np.pi, ome * 0 - As, 'k') # línea de referencia
plt.grid()
plt.title("Magnitud de la respuesta en dB")
plt.xlabel(r"Frecuencia en unidades de $\pi$") # la r, 
plt.ylabel('dB')
plt.axis([0, 1, -100, 10])

plt.figure()
plt.plot(ome*fs/(2 * np.pi), mag, 'b', lw = 2)
plt.xlabel("Frecuencia en Hz")
plt.ylabel("Amplitud")
plt.grid()

plt.figure()
plt.plot(n/fs, x_n)
plt.plot(n/fs, yn.real, 'r')
plt.plot(n/fs, ync, '--g')
plt.grid()

plt.show()