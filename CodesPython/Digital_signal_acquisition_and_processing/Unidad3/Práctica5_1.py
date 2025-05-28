import numpy as np
import scipy.io as io
from funciones_filtrado import fpb_ideal, resp_frec
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile as wavfile
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, 'voz_bryan_5kHz.wav')
fs, senial = wavfile.read(audio_path)

if len(senial.shape) == 2:
    xn = senial[:, 0]  
else:
    xn = senial  

N_muestras = len(xn)  
duracion = N_muestras / fs 
print(f'Duración: {duracion:.2f} segundos')

sd.play(senial, fs, blocking=True)

if len(senial.shape) == 2:
    plt.figure()
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(2, 1, 1)
    plt.plot(senial[:, 0])
    plt.title('Canal 1')
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.plot(senial[:, 1])
    plt.title('Canal 2')
    plt.grid()

N = int(2 ** np.ceil(np.log2(len(xn))))  
Xm = np.fft.fft(xn, N)
magXm = np.abs(Xm)
fan = (fs / N) * np.arange(N // 2)

plt.figure()
plt.plot(fan, magXm[0:N//2])
plt.title('Espectro de la señal original')
plt.grid()

# Diseño del filtro IIR pasabajas (Chebyshev I) 
Fp = 600  
Fs = 1600  
wp = 2 * np.pi * (Fp / fs)  # Frecuencia angular normalizada
ws = 2 * np.pi * (Fs / fs)
Rp = 1  
As = 50  
wp_norm = Fp / (fs/2)
ws_norm = Fs / (fs/2)

# Diseño del filtro IIR Chebyshev Tipo I
b, a = signal.iirdesign(wp_norm, ws_norm, Rp, As, ftype='cheby1')
w, H = signal.freqz(b, a)

print("Numerador (b):")
print([f'{bn:.4f}z^(-{i})' for i, bn in enumerate(b)])
print('------------------------------------------------------')
print("Denominador (a):")
print([f'{an:.4f}z^(-{i})' for i, an in enumerate(a)])

z, p, K = signal.tf2zpk(b, a)

yn = signal.lfilter(b, a, xn)

plt.figure()
plt.plot(np.arange(N_muestras)/fs, xn, label='Señal original')
plt.plot(np.arange(N_muestras)/fs, yn.real, 'r', label='Señal filtrada')
plt.legend()
plt.title('Comparación señal original vs filtrada')
plt.grid()

Ym2 = np.fft.fft(yn, N)
magYm2 = np.abs(Ym2[0:N//2])
plt.figure()
plt.plot(fan, magYm2, 'b')
plt.title('Espectro de la señal filtrada')
plt.grid()

yn_int16 = np.clip(yn.real, -32768, 32767).astype('int16')  # Asegurar rango válido
sd.play(yn_int16, fs, blocking=True)

plt.show()