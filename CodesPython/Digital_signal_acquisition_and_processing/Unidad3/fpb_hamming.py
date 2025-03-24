import numpy as np
import matplotlib.pyplot as plt
from funciones_filtrado import fpb_ideal, resp_frec

# Frecuencia de paso
wp = 0.2 * np.pi

# Frecuencia de rechazo
ws = 0.3 * np.pi

# Atenuación mínima en la banda de rechazo
As = 50

# Banda de transición 
delta_w = ws - wp

# Orden de filtro (numero de taps)

M = np.ceil(6.6 * np.pi / delta_w)
n = np.arange(M)
wc = (ws + wp)/2 # frecuencia de corte del filtro PB ideal 
h = fpb_ideal(wc, M)
w = np.hamming(M)
hw = w * h

mag, ang, dB, ome = resp_frec(hw, 2 ** 13)

plt.figure()

plt.subplot(2,2,1)
plt.stem(n,h)
plt.grid()
plt.title("Respuesta al impulso del Fb ideal")
plt.xlabel('n')
plt.ylabel('h(n)')
plt.axis([0, M-1, -0.1, 0.3])

plt.subplot(2,2,2)
plt.stem(n, w)
plt.grid()
plt.title("Ventana Hamming")
plt.xlabel("n")
plt.ylabel("w(n)")

plt.subplot(2,2,3)
plt.stem(n, hw)
plt.grid()
plt.title("Respuesta al impulso con ventana")
plt.xlabel('n')
plt.ylabel('h(n)')
plt.axis([0, M-1, -0.1, 0.3])

plt.subplot(2,2,4)
plt.plot(ome/np.pi, dB, 'b')
plt.plot(ome/np.pi, ome * 0 - As, 'k') # línea de referencia
plt.grid()
plt.title("Magnitud de la respuesta en dB")
plt.xlabel(r"Frecuencia en unidades de $\pi$") # la r, 
plt.ylabel('dB')
plt.axis([0, 1, -100, 10])

plt.figure()
plt.plot(ome/np.pi, mag, 'b', lw = 2)
plt.grid()
plt.axis([0, 1.2, -0.2, 1.2])
plt.title("Magnitud de la respuesta en la escala lineal")
plt.xlabel(r"Frecuencia en unidades de $\pi$")

plt.show()
