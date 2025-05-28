import numpy as np 
import matplotlib.pyplot as plt

w = np.linspace(0, np.pi, 500)

Hejw = (0.0088 * np.exp(1j*3*w) + 0.0263 * np.exp(1j*2*w) + \
        0.0263 * np.exp(1j*w) + 0.0088) / (np.exp(1j*3*w)- \
        2.2343 * np.exp(1j*2*w) + 1.8758 * np.exp(1j*w) - 0.5713)

plt.figure()
plt.plot(w/np.pi, np.abs(Hejw),'g', lw = 2,)
plt.title("Filtro pasa bajas en un IIR con transformada Z")
plt.grid()

plt.show()