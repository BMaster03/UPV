import numpy as np
from funciones_filtrado import fpb_ideal
import matplotlib.pyplot as plt

wc = 0.8
k = 1
N = 512

for M in range(5, 65, 10):
    # coeficientes creados con la función sinc
    codt = fpb_ideal(wc, M)
    fig = plt.figure(1)
    fig.subplots_adjust(hspace = 0.4) # ajuste de altura entre gráficas
    plt.subplot(3,2,k)
    plt.stem(np.arange(M), codt)
    plt.title(f"{M} taps")
    plt.grid()

    # magnitud de la DFT de los coeficientes
    magCodf = np.abs( np.fft.fft(codt, N)) # Magnitud de la DFT
    fig = plt.figure(2)
    fig.subplots_adjust(hspace = 0.4)
    plt.subplot(3,2,k)
    plt.plot(np.arange(N/2), magCodf[0:N//2])
    plt.title(f'{M} taps')
    plt.grid()

    # magnitud de la DFT de los coeficientes con ventana 
    cow = np.hamming(M) * codt # aplicamos la función ventana Hamming 
    magCodf = np.abs( np.fft.fft(cow, N)) # Magnitud de la DFT
    fig = plt.figure(3)
    fig.subplots_adjust(hspace = 0.4)
    plt.subplot(3,2,k)
    plt.plot(np.arange(N/2), magCodf[0:N//2])
    plt.title(f'{M} taps')
    plt.grid()

    k = k + 1

plt.show()
