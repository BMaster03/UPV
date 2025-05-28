import numpy as np
import matplotlib.pyplot as plt

k = np.arange(51) 

# Valores que tomará el valor de 'r'
rvec = (0.8, -0.8, 1.2, -1.2, 1, -1)

plt.figure()

plt.subplots_adjust(top=0.95, bottom=0.1,hspace=0.3, wspace=0.2)

for i, r in enumerate(rvec):
    plt.subplot(3, 2, i+1)
    plt.stem(k, r**k, 'b', markerfmt = 'b.')
    plt.grid()
    plt.title(f'r={r}')

plt.show()