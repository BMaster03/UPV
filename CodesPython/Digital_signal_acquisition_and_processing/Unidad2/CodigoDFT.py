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
