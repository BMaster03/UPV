import numpy as np
import matplotlib.pyplot as plt

t_max = 1
t = np.linspace(0, t_max,1000)

F = 5 
xt = np.sin(2*np.pi*F*t)

# Muestreo de la señal analógica (Frecuencias) 
FN = 2 * F
fs = 4 * FN
# fs = 8

n = np.arange(t_max * fs + 1)
xn = np.sin(2*np.pi*F*n/fs)

plt.figure()
plt.subplots_adjust(top = 0.95, bottom = 0.1, hspace = 0.5)

plt.subplot(3,1,1)
plt.plot(t, xt, 'r')
plt.stem(n/fs, xn)
plt.grid()
plt.title("Señal analógica muestreada a 40 Hz")

plt.subplot(3,1,2)
plt.stem(n/fs, xn)
plt.grid()
plt.title("Suma de senos cardinales desplazdos y escalados")

# Reconstrucción de la señal por medio de funciones seno cardinal
xr = np.zeros_like(t) # crea un vector de puros ceros
for i in n:
    xsi = xn[i] * np.sinc(fs * (t - (i/fs))) # Funciones sinc, desplazadas y escaladas
    xr = xr + xsi # Acumulamos las funciones sinc
    plt.subplot(3,1,2)
    plt.plot(t, xsi)

plt.subplot(3,1,3)
plt.plot(t, xt, '--r', label = 'original')
plt.plot(t, xr, 'b', label = 'Reconstruida')
plt.grid()
plt.title("Comparación de la señal reconstruida con la original")
plt.legend()

plt.show()