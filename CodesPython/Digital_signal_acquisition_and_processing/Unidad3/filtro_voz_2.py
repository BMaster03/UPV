import numpy as np
import scipy.io.wavfile as wav
from funciones_filtrado import fpb_ideal, resp_frec
import sounddevice as sd
import matplotlib.pyplot as plt

fs, senial = wav.read('voz_bryan_5kHz.wav')

# Verificar si el audio es mono o estéreo
if len(senial.shape) == 1:
    xn = senial  # Audio mono
    es_estereo = False
else:
    xn = senial[:, 0]  # Audio estéreo, tomar canal izquierdo
    es_estereo = True

# Número de muestras y duración
N_muestras = len(xn)
duracion = N_muestras / fs
print(f'Duración: {duracion:.2f} segundos')

# Reproducir el audio
# sd.play(senial, fs, blocking=True)

plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.subplot(2, 1, 1)
plt.plot(xn)
plt.title('Canal 1')
plt.grid()

if es_estereo: # Si el audio es estéreo, graficar el segundo canal
    plt.subplot(2, 1, 2)
    plt.plot(senial[:, 1])
    plt.title('Canal 2')
    plt.grid()

plt.show()

# DFT de la señal