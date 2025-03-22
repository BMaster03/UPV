from datetime import datetime
from CodigoFFT import mi_FFT
import matplotlib.pyplot as plt
import numpy as np

def gen_sig(fs):
    ts = 1.0 / fs
    t = np.arange(0, 1, ts)
    freq = 1.0
    xt = 3 * np.sin(2 * np.pi * freq * t)
    return xt

fs = 128
ts = 1.0 / fs
t = np.arange(0, 1, ts)

f1, f2, f3 = 1, 4, 7
xt = 3 * np.sin(2 * np.pi * f1 * t)
xt += np.sin(2 * np.pi * f2 * t)
xt += 0.5 * np.sin(2 * np.pi * f3 * t)

plt.figure(figsize=(8, 6))
plt.plot(t, xt, 'purple', label='Señal en el tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal en el dominio del tiempo')
plt.grid()
plt.legend()

Xm = mi_FFT(xt)

N = len(Xm)
n = np.arange(N)
T = N / fs
ft = n / T

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(ft, abs(Xm), 'green', markerfmt=" ", basefmt="-g", label='FFT Completa')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT |X(freq)|')
plt.title('FFT Completa')
plt.grid()
plt.legend()

n_oneside = N // 2
f_oneside = ft[:n_oneside]
X_oneside = Xm[:n_oneside] / n_oneside

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'orange', markerfmt=" ", basefmt="-o", label='FFT Normalizada')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT Normalizada |X(freq)|')
plt.title('FFT Normalizada (Un solo lado)')
plt.grid()
plt.legend()
plt.tight_layout()

fs_high = 2048
xt_high = gen_sig(fs_high)

tini = datetime.now()
Xm_high = mi_FFT(xt_high)
tfin = datetime.now()
c = tfin - tini
print(f"Tiempo de ejecución de la FFT: {c.microseconds} microsegundos")

plt.show()