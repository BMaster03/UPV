import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

F = 4 #4 Hertz

xt =np.sin(2*np.pi*F*t)

#Discretizamos la señal
n = np.arange(0,41) #Indices de las muestras
fs = 40.0 #40 muestras en un segundo
ts = 1.0 / fs #Periodo de muestreo
xn =np.sin(2*np.pi*F*n/fs)#Señal discretizada
print(f'ts={ts} segundos')

#La función figure genera una espacio en la pantalla que es una figura 
plt.figure()

plt.subplots_adjust(top = 0.975, bottom = 0.1, hspace = 0.25, wspace = 0.2)
#plt.subplots_adjust(top = 2.5, bottom = 0.3, hspace = 1, wspace = 0.1)
#plt.subplots_adjust(hspace = 0.5)
#Para ajustar el espacio entre las subgráficas

plt.subplot(3,1,1) #Definición de las subgraficas
plt.plot(t, xt, '-b', lw = 2)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal analógica')
plt.grid()

plt.subplot(3,1,2) #Definicion de las subgráficas
plt.stem(n, xn, linefmt='r', markerfmt='r.')
plt.xlabel('Indice de muestra (n)')
plt.ylabel('Amplitud')
plt.title('Señal discreta')
plt.grid()

plt.subplot(3,1,3) #Definicion de las subgráficas
plt.plot(t, xt, '-b', lw = 2)
plt.stem(n*ts, xn, linefmt ='r', markerfmt ='r.') #la función stem realiza una gráfica de tallo o discreta
plt.xlabel('Indice de muestra (n)')
plt.ylabel('Amplitud')
plt.title('Señal discreta')
plt.grid()

plt.show()

