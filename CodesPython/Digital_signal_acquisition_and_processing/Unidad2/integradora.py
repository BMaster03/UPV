import numpy as np 
import matplotlib.pyplot as plt 

xn = np.genfromtxt("muestras_obtenidas_con_arduino.txt")
xn = xn - ((np.max(xn)+np.min(xn))/2) 
n = np.arange(len(xn))
fs = 382 # con esta frecuencia de muestreo se obtiene el valor mas alto de la dft en la frecuencia de 60 hz que entrega la señal analógica

# graficación de la señal y la DFT con la FFT
plt.figure()

plt.subplot(3,1,1)
plt.plot(n/fs, xn, 'g')
plt.title("Signal in Discrate time")
plt.grid()

N = 4096 
Xm = np.fft.fft(xn, N) 
m = np.arange(N)

#frecuencia de analisis
f_an = m*fs/N

plt.subplot(3,1,2)
plt.plot(f_an[0:N//2], np.abs(Xm[0:N//2]), 'b')
plt.title("Signal in Discrate time")
plt.grid()
plt.show()

magXm = np.abs(Xm)

plt.subplot(3,1,3)
plt.plot(m, magXm, 'g')
plt.ylabel("Magnitud")
plt.grid()

plt.show()
