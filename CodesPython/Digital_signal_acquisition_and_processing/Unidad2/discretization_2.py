import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0,0.25,500)

x1t = 3*(np.cos(2*np.pi*50*t))
x2t = 3*(np.cos(2*np.pi*(-25)*t))
x3t = 3*(np.cos(2*np.pi*(25)*t))

fs = 75
n = np.arange(0,19)
x1n = 3*(np.cos(2*np.pi*50*n/fs))
x2n = 3*(np.cos(2*np.pi*(-25)*n/fs))
x3n =3*(np.cos(2*np.pi*(25)*n/fs))

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(3,1,1)
plt.plot(t, x1t, 'r')
plt.stem(n/fs, x1n)
plt.title("Sinusoide 50 Hz") # En cuantro periodos de muestreo hace un ciclo 
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, x2t, 'g')
plt.stem(n/fs, x2n)
plt.title("Sinusoide -25 Hz") # Realiza 5 ciclos en tiempo continuo, pero con las mismas muestras dicretizadas
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, x3t, 'b')
plt.stem(n/fs, x3n)
plt.title("Sinusoide 25 Hz") # Realiza 5 ciclos en tiempo continuo, pero con las mismas muestras dicretizadas
plt.grid()

plt.show()



