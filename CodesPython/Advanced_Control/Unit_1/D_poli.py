import numpy as np 
import matplotlib.pyplot as plt
import control as ctl 

# Función que realiza la división polinomial
def ldiv(NP, DP, nterms):
    # NP es un vector que contiene los coeficientes del numerador
    # DP es un vector que contiene los coeficientes del denominador
    # El grado más alto del numerador o denominador deben ser rellenados
    # con ceros
    # Verificamos si el numerador es solo un número
    if NP.ndim == 0:
        NP = np.array([NP]) # Lo convertimos en array
    dif_grado = len(NP)-len(DP)
    # Si la diferencia de tamaño es negativa, significa que el grado
    # del numerador es menor que el del denominador. Si es positiva,
    # el grado del denominador es menor que el del numerador.
    if dif_grado < 0:
        # Agregamos tantos ceros al numerador, como lo indique
        # la diferencia
        NP = np.concatenate( (np.zeros(np.abs(dif_grado)), NP) )
    else:
        # Agregamos tantos ceros al denominador, como lo indique
        # la diferencia
        DP = np.concatenate( (np.zeros(np.abs(dif_grado)), DP) )
   
    cociente = np.zeros(nterms) # Cociente
    for i in range(nterms):
        cociente[i] = NP[0]/DP[0]
        temp = np.sum( np.array( [ NP,-1*DP*cociente[i] ] ), axis=0 )
        NP = np.concatenate( (temp[1:],[0]) )

    return cociente

z = ctl.tf('z') # variable simbólica
Gz = (0.4673*z - 0.3393)/(z**2 - 1.5327*z + 0.6607)
print(Gz)
