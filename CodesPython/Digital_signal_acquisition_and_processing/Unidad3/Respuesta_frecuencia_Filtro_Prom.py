import numpy as np
import matplotlib.pyplot as plt

hn = np.ones(5) * 0.2 # Coeficientes del filtro

N = 64 # Numeros de puntos de la DFT

hnr = np.zeros(N)

hnr[0:5] = hn

n = np.arange(N) # índices de muestra para el filtro 

# DFT de 64 puntos del filtro de promediado de 5 taps

Hm = np.fft.fft(hnr)

magHm = np.abs(Hm)
angHm = np.angle(Hm, deg = True) # deg = True: es para estar en grados 

plt.figure()

plt.subplot(3,1,1)
plt.stem(n, hnr)
plt.grid()

plt.subplot(3,1,2)
plt.stem(n, magHm)
plt.grid()

plt.subplot(3,1,3)
plt.stem(n, angHm)
plt.grid()

fs = 64

xn = np.sin(2*np.pi*(fs/32)*n/fs)

yn = np.convolve(xn, hn) # operación

print(np.max(yn))
print(magHm[2]) # valor de el vestor magHm

gm = 360/32 # grados por muestra
retar = 2 * gm
print(retar)

print(angHm[2])

plt.figure()

plt.subplot(2,1,1)
plt.plot(n, xn, '-bo', label = 'x(n)')
plt.plot(n, yn[0:N], '-r', label = 'y(n)')
plt.legend()
plt.grid()


F = 8
xn_2 = np.sin(2*np.pi*F*n/fs)
yn_2 = np.convolve(xn_2, hn) # operación

print(np.max(yn_2))
print(magHm[F]) # valor de el vestor magHm

gm = 360/F # grados por muestra
retar = 2 * gm
print(retar)

print(angHm[F])

plt.subplot(2,1,2)
plt.plot(n, xn_2, '-bo', label = 'x(n)')
plt.plot(n, yn_2[0:N], '-r', label = 'y(n)')
plt.legend()
plt.grid()

plt.show()

