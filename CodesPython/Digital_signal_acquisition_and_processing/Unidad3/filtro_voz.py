import os
import numpy as np
import scipy.io.wavfile as wavfile
from funciones_filtrado import fpb_ideal, resp_frec
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy import signal

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, 'voz_bryan_5kHz.wav')

fs, senial = wavfile.read(audio_path)

# Para escuchar el audio
# sd.play(senial, fs, blocking=True)
xn = senial  # Señal discreta
N_muestras = len(xn)  # Número de muestras
duracion = N_muestras / fs  # Duración
print(f'Duración: {duracion:.2f} segundos')
print(len(xn))

plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.subplot(2, 1, 1)
plt.plot(senial)
plt.title('Canal 1')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(senial, 'g')
plt.title('Canal 2')
plt.grid()

# DFT de la señal
N = int(2**np.ceil(np.log2(len(xn))))  # Siguiente potencia de 2
Xm = np.fft.fft(senial, N)
magXm = np.abs(Xm)
fan = (fs / N) * np.arange(N / 2)

plt.figure()
plt.plot(fan, magXm[0:N // 2])
plt.grid()

#### Filtro pasabajas ####
Fp = 4000  # Frecuencia de paso
Fs = 3000  # Frecuencia de rechazo
wp = 2 * np.pi * (Fp / fs)
ws = 2 * np.pi * (Fs / fs)

# Atenuación mínima en la banda de rechazo
As = 50
# Banda de transición
delta_w = wp - ws
print(f'delta_w/np.pi:.4f')
# Orden del filtro
M = int(np.ceil(11 * np.pi / delta_w) + 1)
n = np.arange(M)
wc = (ws + wp) / 2  # Frecuencia de corte del filtro PB ideal
hw = signal.firwin(M, wc / np.pi, window='blackman')
# Respuesta en frecuencia de los coeficientes con ventana
mag, ang, dB, ome = resp_frec(hw, N)

############## Aplicamos el filtro construido ##################
# Aplicación del filtro por el teorema de convolución de la DFT
Hm = np.fft.fft(hw, N)
# Convolución en el dominio de la frecuencia
Ym = Xm * Hm
# De vuelta al dominio del tiempo
ynen = np.fft.ifft(Ym)
# Cortamos a la longitud que tenía xn, las muestras correctas se encuentran
# en la parte central de la señal resultante
limi = (len(hw) - 1) / 2
lims = limi + len(xn)
yn = ynen[int(limi):int(lims)]
# Calculadora de la convolución (dominio del tiempo)
yncon = np.convolve(xn, hw)
ync = yncon[int(limi):int(lims)]

# Gráficas
plt.figure()
plt.plot(np.arange(N_muestras) / fs, xn, label='Señal original')
plt.plot(np.arange(N_muestras) / fs, yn.real, 'r', label='Señal filtrada DFT')
plt.plot(np.arange(N_muestras) / fs, ync, '--g', label='Señal filtrada convol')
plt.legend()

# Respuesta en frecuencia de la señal filtrada
Ym2 = np.fft.fft(yn, N)
Ym_mitad2 = Ym2[0:N // 2]
magYm_mitad2 = np.abs(Ym_mitad2)
# Gráfica de la respuesta en frecuencia
plt.figure()
plt.plot(fan, magYm_mitad2, 'b')
plt.grid()

# Muy importante convertir a entero de 16 bits para que no se distorsione la voz
yn = yn.real.astype('int16')
sd.play(yn.real, fs, blocking=True)
# wavfile.write('voz_filtrada.wav', rate=fs, data=2 * yn)
plt.show()
