import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Frecuencia angular en tiempo discreto (normalizada a 1)
# w = 2*pi*f/pi = 2*pi*(F/fs) / pi
wp = 0.2
ws = 0.3
Rp = 1
As = 20

# Fabricación del filtro
b, a = signal.iirdesign(wp, ws, Rp, As, ftype='cheby1')

# Respuesta en frecuencia
w, H = signal.freqz(b, a)

# Función de transferencia
print([f'{bn:.4}z**(-{i})' for i,bn in enumerate(b)])
print('------------------------------------------------------')
print([f'{an:.4}z**(-{i})' for i,an in enumerate(a)])

# Conversión a la forma ceros, polos y ganancia
z, p, K = signal.tf2zpk(b, a)

fig = plt.figure()
fig.subplots_adjust(hspace=0.4)  # Ajusta el espacio entre gráficas
plt.subplot(2,2,1)
plt.plot(w/np.pi, 20*np.log10( np.abs(H) ) )
plt.ylim([-30, 1])
plt.grid()
plt.xlabel('w'), plt.ylabel('dB'), plt.title('Magnitud')

plt.subplot(2,2,2)
# w=2*pi*(F/fs) --> F = w*fs/(2*pi)
plt.plot(w/np.pi, np.abs(H) )
plt.grid()
plt.xlabel('w'), plt.title('Respuesta en frecuencia (Hz)')

plt.subplot(2,2,3)
plt.plot(w/np.pi, np.angle(H, deg=True) )
plt.grid()
plt.xlabel('w'), plt.ylabel('Ángulo'), plt.title('Fase')

plt.subplot(2,2,4)
t = np.linspace(0, 2*np.pi, 401)
plt.plot(np.cos(t), np.sin(t), 'k-')  # Círculo unitario
plt.plot(p.real, p.imag, 'bx')
plt.title('Polos')
plt.axis('square')

plt.show()
