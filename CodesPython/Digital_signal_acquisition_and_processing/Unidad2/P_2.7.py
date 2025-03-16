# DFT & IDFT
import numpy as np
from CodigoDFT import mi_DFT, mi_IDFT

t = np.linspace(0, 0.001, 500)

F_1 = 1000
F_2 = 2000

x_in = np.sin(2*np.pi*F_1*t) + 0.5*np.sin(2*np.pi*F_2*t + (3/4)*np.pi)

fs = 8000.0
n = np.arange(8) # es lo mismo que poner n = [0,7]

xn_in = np.sin(2*np.pi*F_1*n/fs) + 0.5*np.sin(2*np.pi*F_2*n/fs + (3/4)*np.pi)

Xm = mi_DFT(xn_in)
xnr = mi_IDFT(Xm)

tol = 1e-14
xnr.real[abs(xnr.real) < tol] = 0
xnr.imag[abs(xnr.imag) < tol] = 0

N = len(n)
m = np.arange(N)

f_an = m * fs/N

print(xn_in)
print(xnr)


