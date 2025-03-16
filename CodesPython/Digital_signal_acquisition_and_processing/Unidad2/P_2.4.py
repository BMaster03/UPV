# Propiedad de simetría (DFT)
import numpy as np
from CodigoDFT import mi_DFT
import matplotlib.pyplot as plt

n = np.arange(11)
xn = 3*np.sin(2*np.pi*(1/10)*n)

N = 512
xnr = np.zeros(N)
xnr [0:len(xn)] = xn

Xm = mi_DFT(xnr)

magXm = np.abs(Xm)

m = np.arange(N)

plt.figure()
plt.subplot(3,1,1)
plt.plot(m, Xm.real, 'r')
plt.ylabel("Real Part")
plt.grid()

plt.subplot(3,1,2)
plt.plot(m, Xm.imag, 'b')
plt.ylabel("Imagine Part")
plt.grid()

plt.subplot(3,1,3)
plt.plot(m, magXm, 'g')
plt.ylabel("Magnitud")
plt.grid()

mm = 5
print(np.abs(Xm[mm]) - np.abs(Xm[N-mm]))
      
n = np.arange(11)
xn = np.exp(1j * np.pi * (1/10)*n)

N = 512
xnr = np.zeros(N, dtype = complex)
xnr [0:len(xn)] = xn

Xm = mi_DFT(xnr)

magXm = np.abs(Xm)

m = np.arange(N)

plt.figure()
plt.subplot(3,1,1)
plt.plot(m, Xm.real, 'r')
plt.ylabel("Real Part")
plt.grid()

plt.subplot(3,1,2)
plt.plot(m, Xm.imag, 'b')
plt.ylabel("Imagine Part")
plt.grid()

plt.subplot(3,1,3)
plt.plot(m, magXm, 'g')
plt.ylabel("Magnitud")
plt.grid()

mm = 5
print(np.abs(Xm[mm]) - np.abs(Xm[N-mm]))
      
plt.show()
