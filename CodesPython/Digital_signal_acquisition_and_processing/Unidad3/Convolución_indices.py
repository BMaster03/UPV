import numpy as np

def convolucion_indices(x, nx, h, nh):
    """
    Función que realiza la convolución entre dos señales y entrega los índices
    de la señal resultante

    Recibe:
    x: amplitudes de la señal x
    nx = índices de la señal x
    h: amplitud de la señal h
    nh: índices de la señal h

    Entrega:
    y, ny: ampplitudes e índices del resultado 
    """

    ini = nx[0] + nh[0]
    fin = nx[-1] + nh[-1]

    ny = np.arange(ini, fin+1)
    y = np.convolve(x, h)
    return y, ny

x = np.array([1,2,3,1])
nx = np.arange(0,4)

h = np.array([1,2,1,-1])
nh = np.arange(-1,3)

y, ny = convolucion_indices(x, nx, h, nh)
print(y, ny)



