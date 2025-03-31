import numpy as np
import scipy.io as io
from funciones_filtrado import fpb_ideal, resp_frec
import sounddevice as sd
import matplotlib.pyplot as plt


fs, senial = io.wavfile.read('voz_bryan_5kHz.wav')
# Para escuchar el audio
#sd.play(senial,'fs', blocking=True)
xn = senial # Senial discreta
N_muestras = len(xn) # Número de muestras
duracion = N_muestras/fs# Duración
print(f'Duración: {duracion:.2f} segundos')

plt.figure()
"""
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,1,1)
"""
plt.plot(senial)
plt.title('Canal 1')
plt.grid()
"""
plt.subplot(2,1,2)
plt.plot(senial)
plt.title('Canal 2')
plt.grid()
""" 

plt.show()
# DFT de la señal