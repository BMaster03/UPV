import numpy as np 
import matplotlib.pyplot as plt

t_1 = np.linspace(0, 0.03, 300)
t_2 = np.linspace(0, 0.02, 200)

x1t = 3 * np.sin(2 * np.pi * 50 * t_1)
x2t = 3 * np.sin(2 * np.pi * 50 * t_2) 

fs_1 = 300

n_1 = np.arange(0, 6)
n_2 = np.arange(0, 7)

x1n = 3 * np.sin(np.pi * n_1 / 3)
x2n = 3 * np.sin(np.pi * n_2 / 3)

plt.figure()
plt.subplots_adjust(hspace = 0.5)

plt.subplot(2, 1, 1)
plt.plot(t_1, x1t, 'r', label = 'Señal x1(t)')  
plt.title("Señal Sinusoide 1.5 a)") 
plt.xlabel("Tiempo (s)")  
plt.ylabel("Amplitud")    
plt.grid()
plt.legend()  

plt.subplot(2, 1, 2)
plt.plot(t_2, x2t, 'g', label = 'Señal x2(t)')  
plt.stem(n_2 / fs_1, x2n, label = 'Señal x2[n]')  
plt.title("Señal Sinusoide 1.5 c)") 
plt.xlabel("Tiempo (s)")  
plt.ylabel("Amplitud")     
plt.grid()
plt.legend()  

plt.show()