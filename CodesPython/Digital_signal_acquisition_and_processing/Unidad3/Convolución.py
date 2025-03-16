import numpy as np

x = np.array([1,2,3,1])
h = np.array([1,2,1,-1])

yn = np.convolve(x, h) # desplazar, multiplicar, acumular 

print(yn)

