import numpy as np

def mi_DFT(x):
    N = len(x)
    X = np.zeros(N, dtype = complex)

    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + x[n] * (np.cos(arg) - 1j * np.sin(arg))

        X[m] = suma
        
    return X

def mi_IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype = complex)

    for n in range(N):
        suma = 0.0
        for m in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + X[m] * (np.cos(arg) + 1j * np.sin(arg))

        x[n] = suma

    return x/N

def mi_DFT_ciclos(x, ciclos):
    N = len(x)
    X = np.zeros(N * ciclos, dtype = complex)
    for m in range(N * ciclos):
        suma = 0
        for n in range(N):
            arg = (2*np.pi*m*n/N)
            suma = suma + x[n] * (np.cos(arg)-1j*np.sin(arg))

        X[m] = suma
    
    return X

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
