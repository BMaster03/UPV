import numpy as np
import matplotlib.pyplot as plt
from funciones_filtrado import fpb_ideal, resp_frec

wc1 = np.pi/3
wc2 = 2*np.pi/3
wc3 = np.pi

As = 60 # Atenuación mínima en la banda de rechazo

M = 45
n = np.arange(M)
# beta_f = 0.1102 * (As - 8.7)
beta_f = 5.8987
h = fpb_ideal(wc3, M) - fpb_ideal(wc2, M) + fpb_ideal(wc1,M) # 
w = np.kaiser(M, beta_f)
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
