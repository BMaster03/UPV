import numpy as np
import matplotlib.pyplot as plt
import time

t = np.linspace(0, 0.05, 1000)

x_t = 0.8*np.sin(2*np.pi*250*t) + np.sin(2*np.pi*500*t)

fs = 2000.0
n = np.arange(201)

x_n = 0.8*np.sin(2*np.pi*250*n/fs) + np.sin(2*np.pi*500*n/fs)

plt.figure()

plt.subplot(2,1,1)
plt.plot(t, x_t, 'g')
plt.grid()

N = 4096

xnrell = np.zeros(N)
xnrell[0: len(x_n)] = x_n

ini = time.time()

#X_m = mi_DFT(xnrell

X_m = np.fft.fft(xnrell)

fin = time.time()
print(f'Tiempo transcurrido: {fin-ini} segundos')

Xm_mitad = X_m[0:N//2]

magXm_mitad = np.abs(Xm_mitad)

m = np.arange(N/2)
fan = m * (fs/N)

plt.subplot(2,1,2)
plt.plot(fan, magXm_mitad, 'b')
plt.grid()

plt.show()

