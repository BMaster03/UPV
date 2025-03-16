from re import X
import numpy as np
import matplotlib.pyplot as plt
from CodigoDFT import mi_DFT

"""
    La dft entrega la magnitud, fase, frecuencia, la dft es simétrica, respecto a la fs 
    complejos conjugados cuando se repiten
"""

t = np.linspace(0, 0.001, 1000)

F_1 = 1000
F_2 = 2000

x_in = np.sin(2*np.pi*F_1*t) + 0.5*np.sin(2*np.pi*F_2*t + (3/4)*np.pi)

fs = 8000.0
n = np.arange(8)

xn_in = np.sin(2*np.pi*F_1*n/fs) + 0.5*np.sin(2*np.pi*F_2*n/fs + (3/4)*np.pi)

plt.figure()
plt.subplots_adjust(top = 0.975, bottom = 0.1, hspace = 0.35, wspace = 0.2)

plt.subplot(2,1,1)
plt.plot(t, x_in, 'b')
plt.stem(n/fs, xn_in)
plt.title('Señal continua & discreta')
plt.xlabel("Time")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(2,1,2)
plt.stem(n/fs, xn_in, 'r')
plt.title('Señal Discreta')
plt.xlabel("Time")
plt.ylabel("Amplitud")
plt.grid()

Xm = mi_DFT(xn_in)

tol = 1e-14
Xm.real[abs(Xm.real) < tol] = 0
Xm.imag[abs(Xm.imag) < tol] = 0

N = len(n)
m = np.arange(N)

f_an = m * fs/N

plt.figure()
plt.subplots_adjust(hspace = 0.25)

plt.subplot(2,2,1)
plt.stem(f_an, Xm.real)
plt.grid()
plt.title("Real Part")

plt.subplot(2,2,2)
plt.stem(f_an, Xm.real)
plt.grid()
plt.title("Imagin Part")

plt.subplot(2,2,3)
plt.stem(f_an, np.abs(Xm))
plt.grid()
plt.title("Magnitud")

plt.subplot(2,2,4)
plt.stem(f_an, np.angle(Xm, deg = True))
plt.grid()
plt.title("Angulo")

plt.show()
    