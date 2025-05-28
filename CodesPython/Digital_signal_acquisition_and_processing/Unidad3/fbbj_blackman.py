import numpy as np
import matplotlib.pyplot as plt
from funciones_filtrado import fpb_ideal, resp_frec

ws1 = 0.2*np.pi # Frecuencia de rechazo 1
wp1 = 0.35*np.pi # Frecuencia de paso 1
wp2 = 0.65*np.pi # Frecuencia de rechazo 2
ws2 = 0.8*np.pi # Frecuencia de paso 2

As = 60

delta_w = np.min((wp1 - ws1, ws2 -wp2)) # es para obtener el mínimo entre esas dos bandas de transición

M = np.ceil(11 * np.pi / delta_w) + 1
n = np.arange(M) # índices del filtro 
wc1 = (ws1 + wp1)/2
wc2 = (wp2 + ws2)/2
h = fpb_ideal(wc2, M) - fpb_ideal(wc1, M)
w = np.blackman(M)
hw = w * h
mag, ang, dB, ome = resp_frec(hw, 2**13)


plt.figure()

plt.subplot(2,2,1)
plt.stem(n,h)
plt.grid()
plt.title("Respuesta al impulso del Filtro")
plt.xlabel('n')
plt.ylabel('h(n)')
plt.axis([0, M-1, -0.4, 0.5])

plt.subplot(2,2,2)
plt.stem(n, w)
plt.grid()
plt.title("Ventana Blackman")
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


