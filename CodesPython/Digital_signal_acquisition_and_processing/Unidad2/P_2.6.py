import numpy as np
import matplotlib.pyplot as plt
from CodigoDFT import mi_DFT_ciclos, mi_DFT

n = np.arange(0, 10)  #
xn = 0.9 * np.exp(1j * np.pi / 3 * n)  
N = 512
xnr = np.zeros(N, dtype=complex)  
xnr[0:len(xn)] = xn  

Xm = np.fft.fft(xnr)  
Xm1 = mi_DFT_ciclos(xnr, 3)  

magXm = np.abs(Xm)
magXm1 = np.abs(Xm1)

m = np.arange(N)
m1 = np.arange(N * 3)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(m, magXm, 'r')
plt.title('Magnitud 1 ciclo')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(m1, magXm1, 'g')
plt.title('Magnitud 3 ciclos')
plt.grid()

plt.show()