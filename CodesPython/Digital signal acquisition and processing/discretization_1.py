import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0,0.25,500)

x1t = np.cos(2*np.pi*10*t)
x2t = np.cos(2*np.pi*50*t)

fs = 40
n = np.arange(0,11)
x1n = np.cos(2*np.pi*10*n/fs)
x2n = np.cos(2*np.pi*50*n/fs)

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(2,1,1)
plt.plot(t, x1t, 'r')
plt.stem(n/fs, x1n)
plt.title("Sinusoide 10 Hz") # En cuantro periodos de muestreo hace un ciclo 
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, x2t, 'g')
plt.stem(n/fs, x2n)
plt.title("Sinusoide 50 Hz") # Realiza 5 ciclos en tiempo continuo, pero con las mismas muestras dicretizadas
plt.grid()

plt.show()
