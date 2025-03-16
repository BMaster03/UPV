import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,1000) #replicador de tiempo continuo (muestras discretas de dos segundos, mil de ellas)

senial_orig = np.sin(2*np.pi*1*t)

senial_1 = 0.5*np.sin(2*np.pi*1*t)
senial_2 = np.sin(2*np.pi*1*t - np.pi/5)
senial_3 = np.sin(2*np.pi*2*t)
senial_4 = 0.5*np.sin(2*np.pi*2*t - np.pi/5)

plt.figure()

plt.subplots_adjust(top = 0.95, bottom = 0.1, hspace = 0.3, wspace = 0.2)

#gráfica_1
plt.subplot(2,2,1)
plt.plot(t, senial_orig, 'b')
plt.plot(t, senial_1, 'g')
plt.ylim([-1.05, 1.05])
plt.grid() #genera un mallado por detrás de la gráfica

#gráfica_2
plt.subplot(2,2,2)
plt.plot(t, senial_orig, 'b')
plt.plot(t, senial_2, 'r')
plt.ylim([-1.05, 1.05])
plt.grid()

#gráfica_3
plt.subplot(2,2,3)
plt.plot(t, senial_orig, 'b')
plt.plot(t, senial_3, 'k')
plt.ylim([-1.05, 1.05])
plt.grid()

#gráfica_4
plt.subplot(2,2,4)
plt.plot(t, senial_orig, 'g')
plt.plot(t, senial_4, 'r')
plt.ylim([-1.05, 1.05])
plt.grid()

plt.show()

