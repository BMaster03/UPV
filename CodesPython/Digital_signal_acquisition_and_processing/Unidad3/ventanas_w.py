import numpy as np 
import matplotlib.pyplot as plt

N = 55
n = np.arange(N)

fs = N

xn = np.sin(2*np.pi*4*n/fs)

plt.figure()

plt.subplots_adjust(hspace = 0.3)

plt.subplot(4,1,1)
plt.stem(n, xn)
plt.grid()
plt.title("Sinusoide discreta")

"""
wn_1 = (2/(N-1)) * ((N-1)/2) - np.abs(n - ((N-1)/2)) # función ventana triangular
xnwn_1 = wn_1 * xn
"""
wn_1 = np.bartlett(N)
xnwn_1 = wn_1 * xn

plt.subplot(4,1,2)
plt.plot(n, wn_1, 'r')
plt.stem(n, xnwn_1)
plt.grid()
plt.title("Sinusoide discreta con f.tringular")

"""
wn_2 = 0.5 - 0.5*np.cos((2*np.pi*n)/N) # función ventana hanning
xnwn_2 = wn_2*xn
"""
wn_2 = np.hanning(N)
xnwn_2 = wn_2 * xn

plt.subplot(4,1,3)
plt.plot(n, wn_2, 'r')
plt.stem(n, xnwn_2)
plt.grid()
plt.title("Sinusoide discreta con f.hanning")

"""
wn_3 = 0.54 - 0.46*np.cos((2*np.pi*n)/N) # función ventana hamming
xnwn_3 = wn_3*xn
"""
wn_3 = np.hamming(N)
xnwn_3 = wn_3 * xn

plt.subplot(4,1,4)
plt.plot(n, wn_2, 'r')
plt.stem(n, xnwn_2)
plt.grid()
plt.title("Sinusoide discreta con f.hamming")

plt.show()
