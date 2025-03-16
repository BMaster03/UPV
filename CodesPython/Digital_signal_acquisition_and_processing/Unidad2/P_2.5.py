import numpy as np
import matplotlib.pyplot as plt
from CodigoDFT import mi_DFT

n = np.arange(0,10)

x1n = 3*np.cos(2*np.pi*(1/7)*n)
x2n = 0.8*np.sin(2*np.pi*(2/5)*n)
xsn = x1n+x2n

# Rellenamos con ceros para obtener 512 muestras
N = 256
xnr1 = np.zeros(N)
xnr2 = np.zeros(N)
xnrs = np.zeros(N)

xnr1[0:len(x1n)] = x1n
xnr2[0:len(x2n)] = x2n
xnrs[0:len(xsn)] = xsn

Xm1 = mi_DFT(xnr1)
Xm2 = mi_DFT(xnr2)
Xms = mi_DFT(xnrs)

magXm1 = np.abs(Xm1)
magXm2 = np.abs(Xm2)
magXms = np.abs(Xms)

m  = np.arange(N)

plt.figure()

plt.subplots_adjust(hspace=1,)
plt.subplot(2,1,1)
plt.plot(m,magXms, 'b')
plt.title('Magnitud de la DFT Xs(m)')
plt.grid()

X2s = Xm1+Xm2
magXm4 = np.abs(X2s)

plt.subplot(2,1,2)
plt.plot(m,magXm4, 'g')
plt.title('Magnitud de la DFT X2s(m)')
plt.grid()
plt.show()

print(np.sum(np.abs(Xms-X2s)))

plt.show()
