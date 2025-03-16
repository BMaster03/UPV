import numpy as np 
import matplotlib.pyplot as plt

t_1 = np.linspace(0,0.25,500)
t_2 = np.linspace(0,8,500)

x1t = np.cos(2*np.pi*10*t_1)
x2t = np.cos(2*np.pi*50*t_1)

x3t = np.cos(2*np.pi*(1/8)*t_2)
x4t = np.cos(2*np.pi*(-7/8)*t_2)

fs_1 = 40
fs_2 = 1

n_1 = np.arange(0,11)
n_2 = np.arange(0,8)

x1n = np.cos(2*np.pi*10*n_1/fs_1)
x2n = np.cos(2*np.pi*50*n_1/fs_1)

x3n = np.cos(2*np.pi*(1/8)*n_2/fs_2)
x4n = np.cos(2*np.pi*(-7/8)*n_2/fs_2)

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(2,1,1)
plt.plot(t_1, x1t, 'r')
plt.stem(n_1/fs_1, x1n)
plt.title("Sinusoide 10 Hz") 
plt.grid()

plt.subplot(2,1,2)
plt.plot(t_1, x2t, 'g')
plt.stem(n_1/fs_1, x2n)
plt.title("Sinusoide 50 Hz") 
plt.grid()

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(2,1,1)
plt.plot(t_2, x3t, 'r')
plt.stem(n_2/fs_2, x3n)
plt.title("Sinusoide 1/8 Hz") 
plt.grid()

plt.subplot(2,1,2)
plt.plot(t_2, x4t, 'g')
plt.stem(n_2/fs_2, x4n)
plt.title("Sinusoide -7/8 Hz") 
plt.grid()

plt.show()
