from funciones_filtrado import fpb_ideal, resp_frec
import sounddevice as sd
import matplotlib.pyplot as plt
import os
import numpy as np
import scipy.io.wavfile as wavfile
from scipy import signal

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, 'voz_bryan_5kHz.wav')
fs, senial = wavfile.read(audio_path)

# Verificar si el audio es estéreo o mono y seleccionar el primer canal
if len(senial.shape) == 2:
    xn = senial[:, 0]  # Primer canal (estéreo)
else:
    xn = senial  # Señal mono

N_muestras = len(xn)  # Número de muestras
duracion = N_muestras / fs  # Duración en segundos
print(f'Duración: {duracion:.2f} segundos')

# Reproducir la señal original
sd.play(xn, fs, blocking=True)

# Visualización de la señal (solo si es estéreo)
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

# Cálculo de la DFT
N = int(2 ** np.ceil(np.log2(len(xn))))  # Potencia de 2 más cercana
Xm = np.fft.fft(xn, N)
magXm = np.abs(Xm)
fan = (fs / N) * np.arange(N // 2)

plt.figure()
plt.plot(fan, magXm[0:N//2])
plt.title('Espectro de la señal original')
plt.grid()

### Diseño del filtro FIR pasabajas ###
Fp = 600  # Frecuencia de paso (Hz)
Fs = 1600  # Frecuencia de rechazo (Hz)
wp = 2 * np.pi * (Fp / fs)  # Frecuencia angular normalizada
ws = 2 * np.pi * (Fs / fs)
As = 50  # Atenuación en banda de rechazo (dB)

# Banda de transición y orden del filtro
delta_w = ws - wp
print(f'Banda de transición: {delta_w/np.pi:.4f}π rad/muestra')
M = int(np.ceil(11 * np.pi / delta_w) + 1)  # Orden del filtro
wc = (ws + wp) / 2  # Frecuencia de corte ideal

# Diseño del filtro con ventana de Blackman
hw = signal.firwin(M, wc/np.pi, window='blackman')

# Respuesta en frecuencia del filtro (usando tu función personalizada)
mag, ang, dB, ome = resp_frec(hw, N)

### Aplicación del filtro ###
Hm = np.fft.fft(hw, N)  # DFT de la respuesta al impulso
Ym = Xm * Hm  # Convolución en frecuencia
ynen = np.fft.ifft(Ym)  # Regreso al dominio del tiempo

# Ajuste de longitud para eliminar retraso del filtro
limi = (len(hw) - 1) // 2
lims = limi + len(xn)
yn = ynen[int(limi):int(lims)].real  # Parte real de la señal filtrada

# Opcional: Convolución directa en el tiempo (comparación)
yncon = np.convolve(xn, hw, mode='same')

# Gráficas comparativas
plt.figure()
plt.plot(np.arange(N_muestras)/fs, xn, label='Señal original')
plt.plot(np.arange(N_muestras)/fs, yn, 'r', label='Señal filtrada (DFT)')
plt.plot(np.arange(N_muestras)/fs, yncon, '--g', label='Señal filtrada (convolución)')
plt.legend()
plt.title('Comparación de métodos de filtrado')
plt.grid()

# Espectro de la señal filtrada
Ym2 = np.fft.fft(yn, N)
magYm2 = np.abs(Ym2[0:N//2])
plt.figure()
plt.plot(fan, magYm2, 'b')
plt.title('Espectro de la señal filtrada')
plt.grid()

# Reproducir la señal filtrada (convertida a int16 para compatibilidad)
yn_int16 = yn.astype('int16')
sd.play(yn_int16, fs, blocking=True)

# Guardar el resultado (opcional)
# wavfile.write('voz_filtrada.wav', fs, yn_int16)

plt.show()