import numpy as np
import matplotlib.pyplot as plt

th = np.pi/8
k = np.arange(100) 
r = 0.95
z_k = (r**k)*np.exp(1j*th*k)

# Valores que tomará el valor de 'r'
rvec = (0.8, -0.8, 1.2, -1.2, 1, -1)

plt.figure()

plt.subplots_adjust(top=0.95, bottom=0.1,hspace=0.3, wspace=0.2)

plt.subplot(2, 1, 1)
plt.stem(k, np.real(z_k), 'm', markerfmt = 'm.')
plt.grid()
plt.title('Real_Part')

plt.subplot(2, 1, 2)
plt.stem(k, np.imag(z_k), 'm', markerfmt = 'm.')
plt.grid()
plt.title('Im_Part')

ax = plt.figure() .add_subplot(projection='3d', proj_type='ortho')
ax.plot(np.real(z_k), np.imag(z_k), k, '-m.', lw = 2)
ax.grid()
ax.set_xlabel('Real_part')
ax.set_ylabel('Im_part')
ax.set_zlabel('k')

plt.show()