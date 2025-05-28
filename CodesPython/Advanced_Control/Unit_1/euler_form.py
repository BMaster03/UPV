import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, 6*np.pi, 1000)
z = np.exp(1j * th) # e^(j * th)

plt.figure()
plt.subplots_adjust(top = 0.95, bottom = 0.1, hspace = 0.3, wspace = 0)

plt.subplot(2, 1, 1)
plt.plot(th, np.real(z), 'm', lw=2)
plt.grid()
plt.title("Real_Part")

