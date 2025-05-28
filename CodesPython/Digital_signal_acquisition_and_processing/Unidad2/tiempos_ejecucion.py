import numpy as np
from datetime import datetime
from CodigoDFT import mi_DFT, mi_FFT

xn = np.random.rand(1024) # con el random permite obtener un vector aleatorio de 1024 elementos
"""
# Medir el tiempo de ejecución de mi_DFT
tini = datetime.now() # Tiempo inicial
Xm = mi_DFT(xn)
tfin = datetime.now() # Tiempo final
c = tfin - tini # Tiempo transcurrido
print("Tiempo de ejecución con la función mi_DFT:", c.microseconds, "microsegundos")
"""
"""

# Medir el tiempo de ejecución de mi_FFT
tini = datetime.now() 
Xn = mi_FFT(xn)
tfin = datetime.now() 
c = tfin - tini 
print("Tiempo de ejecución con la función mi_FFT:", c.microseconds, "microsegundos")
"""

# Medir el tiempo de ejecución de np.fft.fft
tini = datetime.now() 
Xm = np.fft.fft(xn)
tfin = datetime.now() 
c = tfin - tini 
print("Tiempo de ejecución del algoritmo optimizado de numpy np.fft.fft:", c.microseconds, "microsegundos")