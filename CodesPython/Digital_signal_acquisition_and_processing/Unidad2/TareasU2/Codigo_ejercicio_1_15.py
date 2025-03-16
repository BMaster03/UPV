import numpy as np
from datetime import datetime
from CodigoFFT import mi_FFT
from CodigoDFT import mi_DFT

xn = np.random.rand(1024)

# Medir el tiempo de ejecución de mi_DFT
tini = datetime.now() # Tiempo inicial
Xm = mi_DFT(xn)
tfin = datetime.now() # Tiempo final
c = tfin - tini # Tiempo transcurrido
print("Tiempo de ejecución de mi_DFT:", c.microseconds, "microsegundos")


"""
# Medir el tiempo de ejecución de mi_FFT
tini = datetime.now() # Tiempo inicial
Xm = mi_FFT(xn)
tfin = datetime.now() # Tiempo final
c = tfin - tini # Tiempo transcurrido
print("Tiempo de ejecución de mi_FFT:", c.microseconds, "microsegundos")

"""
"""
# Medir el tiempo de ejecución de np.fft.fft
tini = datetime.now() # Tiempo inicial
Xm = np.fft.fft(xn)
tfin = datetime.now() # Tiempo final
c = tfin - tini # Tiempo transcurrido 
print("Tiempo de ejecución de np.fft.fft:", c.microseconds, "microsegundos")
"""