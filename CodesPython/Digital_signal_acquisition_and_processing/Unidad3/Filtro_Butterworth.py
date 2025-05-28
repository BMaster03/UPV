import numpy as np
from scipy import signal 
from matplotlib import pyplot as plt

# Frrecuencia andgualar en timepo discreto (normalizada a 1)
# w = 2*pi*f/pi = 2*np.pi*(F/fs)/np.pi

wp = 0.2
ws = 0.3 
Rp = 1
As = 15

# Fabricación del filtro 
b, a = signal.iirdesign(wp, ws, Rp, As, ftype = 'butter') #<--

w, H = signal.freqz(b, a)
# Función de transferencia
print([f'{bn:.4}z**(-{i})' for i, bn in enumerate(b)])
print('---------------------------------------------')
print([f'{an:.4}z**(-{i})' for i, an in enumerate(a)])

# conversión a la forma de ceros, polos y ganancia
z, p, K = signal.tf2zpk(b, a)

fig = plt.figure()
fig.subplots_adjust(hspace = 0.4)

plt.subplot(2,2,1)
plt.plot(w/np.pi, 20*np.log10(np.abs(H)))  # Respuesta en decibeles
plt.ylim(-30, 11)
plt.grid()
plt.xlabel(r'$\omega$'), plt.ylabel('dB'), plt.title('Magnitud')

plt.subplot(2,2,2)
plt.plot(w/np.pi, np.abs(H))
plt.grid()
plt.xlabel(r'$\omega$'), plt.title('Respuesta en frecuencia (unidades de $\pi$)')

plt.subplot(2,2,3)
plt.plot(w/np.pi, np.angle(H, deg=True))
plt.grid()
plt.xlabel(r'$\omega$'), plt.ylabel('Ángulo'), plt.title('Fase')

plt.subplot(2,2,4)
t = np.linspace(0, 2*np.pi, 401)

plt.plot(np.cos(t), np.sin(t), 'k-')  # Círculo unitario
plt.plot(p.real, p.imag, 'bx')
plt.title('Polos')
plt.axis('square')

plt.show()