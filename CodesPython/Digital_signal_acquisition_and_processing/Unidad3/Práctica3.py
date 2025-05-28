import numpy as np 
from funciones_filtrado import fpb_ideal, resp_frec
import matplotlib.pyplot as plt
from scipy import signal

As = 60 # Atenuacion minima en la banda de rechazo
wc1 = np.pi/3 # frecucencia de corte 1
wc2 = 2*np.pi/3 # frecuencia de corte 2
M = 45
n = np.arange(M)
beta = 5.9

hw = signal.firwin(M, [wc1/np.pi,wc2/np.pi], window = ('kaiser', beta))
mag, ang, dB, ome = resp_frec(hw,2**13)

plt.figure()

plt.subplot(2,2,1)
plt.stem(n,hw)
plt.grid()
plt.title('Respuesta al impulso del filtro')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.axis([0,M-1,-0.2,0.7])

plt.subplot(2,2,2)
plt.stem(n,signal.windows.kaiser(M, beta))
plt.grid()
plt.title('Ventana Kaiser')
plt.xlabel('n')
plt.ylabel('w(n)')

plt.subplot(2,2,3)
plt.stem(n,hw)
plt.grid()
plt.title('Respuesta al impulso con ventana')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.axis([0,M-1,-0.4,0.5])

plt.subplot(2,2,4)
plt.plot(ome/np.pi,dB,'b')
plt.plot(ome/np.pi,ome*0-As,'k') #Linea de referencia
plt.grid()
plt.title('Magnitud de la respuesta en dB')
plt.xlabel(r"Frecuencia en unidades de $\pi$")
plt.ylabel('dB')
plt.axis([0,1,-100,10])

plt.figure(2)
plt.plot(ome/np.pi,mag,'b',lw=2)
plt.grid()
plt.axis([0,1.2,-0.2,1.2])

plt.title('Magnitud de la respuesta en escala lineal')
plt.xlabel(r"Frecuencai en unidades de $\pi$")

plt.show()
