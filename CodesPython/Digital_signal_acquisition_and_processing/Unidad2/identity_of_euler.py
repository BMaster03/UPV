"""
    Program to visualize Euler's identity in 2D and 3D
"""

import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,6 * np.pi, 1000) # create space of three cicles because PI are definit in 2PI
z = np.exp(1j * w)

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(2,1,1)
plt.plot(w, np.real(z))
plt.title("Real part")
plt.grid()

plt.subplot(2,1,2)
plt.plot(w, np.imag(z))
plt.title("Imaginary part")
plt.grid()

ax = plt.figure() .add_subplot(projection = '3d', proj_type = 'ortho')
ax.plot(np.real(z), np.imag(z), w, 'b', lw = 2)
ax.grid()
ax.set_xlabel('Real part')
ax.set_ylabel('Imaginary part')
ax.set_zlabel('$\omega$')

plt.show()