import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.002, 5000) 

fs1 = 50000  
fs2 = 25000  
f = 2000  

xlt = np.sin(2*np.pi*f*t)

n1 = np.arange(0, 100)  
xln1 = np.sin(2*np.pi*f*n1/fs1)

n2 = np.arange(0, 50)  
xln2 = np.sin(2*np.pi*f*n2/fs2)

plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.subplot(2, 1, 1)
plt.plot(t, xlt, 'b', label = 'Señal continua')  
plt.stem(n1/fs1, xln1, 'r', label = 'Muestras a 50 kHz')  
plt.title('Sinusoide de 2 kHz muestreada a 50 kHz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, xlt, 'b', label = 'Señal continua')  
plt.stem(n2/fs2, xln2, 'g', label = 'Muestras a 25 kHz') 
plt.title('Sinusoide de 2 kHz muestreada a 25 kHz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

plt.show()