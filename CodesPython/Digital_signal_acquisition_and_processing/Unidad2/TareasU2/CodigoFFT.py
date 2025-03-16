import numpy as np

def mi_FFT(x):
    ''' Una implementación recursiva del algoritmo de Cooley-Tukey de la FFT 1D'''
    N = len(x)
    if N == 1:
        return x
    elif N % 2 > 0:
        raise ValueError('El tamaño de x debe ser una potencia de 2')
    else:
        X_even = mi_FFT(x[::2])
        X_odd = mi_FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[0:N // 2] * X_odd,
                                X_even + factor[N // 2:] * X_odd])