import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.02, 2000)

x1t = np.sin(2*np.pi*500*t)
x2t = np.sin(2*np.pi*2000*t)
x3t = np.sin(2*np.pi*3000*t)
x4t = np.sin(2*np.pi*4500*t)

fs = 5000  
n = np.arange(0, 100)  

x1n = np.sin(2*np.pi*500*n/fs)
x2n = np.sin(2*np.pi*2000*n/fs)
x3n = np.sin(2*np.pi*3000*n/fs)
x4n = np.sin(2*np.pi*4500*n/fs)

plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.subplot(4, 1, 1)
plt.plot(t, x1t, 'b')
plt.stem(n/fs, x1n)
plt.title("Señal Sinusoide de 500 Hz")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, x2t, 'c')
plt.stem(n/fs, x2n)
plt.title("Señal Sinusoide de 2000 Hz")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, x3t, 'g')
plt.stem(n/fs, x3n)
plt.title("Señal Sinusoide de 3000 Hz")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, x4t, 'r')
plt.stem(n/fs, x4n)
plt.title("Señal Sinusoide de 4500 Hz")
plt.grid()

plt.show()
