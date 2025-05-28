import numpy as np 
from funciones_filtrado import fpb_ideal, resp_frec
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(1,0.1,1000)
xt = 0.6*np.sin(2*np.pi*60*t)+2*np.cos(2*np.pi*120*t)+1.4*np.sin(2*np.pi*300*t)+0.3*np.cos(2*np.pi*2500*t)

fs = 5000
n = np.arange(0,500)
xn = 0.6*np.sin(2*np.pi*60*n/fs)+2*np.cos(2*np.pi*120*n/fs)+1.4*np.sin(2*np.pi*300*n/fs)+0.3*np.cos(2*np.pi*2500*n/fs)
N = 2**13
print(N)
Xm = np.fft.fft(xn,N)
magXm = np.abs(Xm)
fan = (fs/N)*np.arange(N//2)

plt.figure()

plt.plot(fan,magXm[0:N//2])
plt.grid()

# Fabricacion del filtro FIR
Fs1 = 65 # Frecuencia de rechazo 1 en Hz
Fp1 = 110 # Frecuencia de paso 1 en Hz
Fp2 = 130 # Frecuecia de paso 2
Fs2 = 165 # Frecuencia de rechazo 2

# Frecuencia angular discreta 
ws1 = 2*np.pi*Fs1/fs # Frecuenciade rechazo 1
wp1 = 2*np.pi*Fp1/fs # Frecuencia de rechazo 1
wp2 = 2*np.pi*Fp2/fs # Frecuencia de rechazo 1
ws2 = 2*np.pi*Fs2/fs # Frecuencia de rechazo 1

As = 45 # Atenuacion minima en la banda de rechazo
delta_w = np.min((wp1-ws1,ws2-wp2)) #Banda de transición
# Orden del filtro (número de taps)
M = int(np.ceil(6.6*np.pi/delta_w)+1)
n2 = np.arange(M) # Indices del filtro
wc1 = (ws1+wp1)/2 # Frecucencia de corte 1
wc2 = (wp2+ws2)/2 # Frecuencia de corte 2
hw = signal.firwin(M, [wc1/np.pi,wc2/np.pi], pass_zero = False, window ='hamming')

# Respuesta en frecuencia de los coeficientes con ventana
mag,ang,dB,ome = resp_frec(hw,2**13)

"""
    Aplicamos el filtro construido
"""
# Aplicacion del filtro por el teorema de convolucion de la DFT
Hm = np.fft.fft(hw,N)
# Convolucion en el dominio de la frecuencia 
Ym = Xm * Hm
# De vuelta al dominio del tiempo
ynen = np.fft.ifft(Ym)
"""
Cortamos a la longitud que tenia xn, las muestras correctas se encuentran
en la parte central de la seññal resultante
"""
limi = (len(hw)-1)/2
lims = limi+len(xn)
yn = ynen[int (limi):int(lims)]
# Calculadora de la conolucion(dominio del tiempo)
yncon = np.convolve(xn,hw)
ync = yncon[int(limi):int(lims)]

plt.figure()
plt.subplot(3,1,1)
plt.stem(n2,np.hamming(M),'-b')
plt.grid()
plt.title('Ventana Hamming'),plt.xlabel('n'),plt.ylabel('w(n)')

plt.subplot(3,1,2)
plt.stem(n2,hw)
plt.grid()
plt.title('Respuesta al impulso con ventana'),plt.xlabel('n'), plt.ylabel('h(n)')
plt.xlabel('n')
plt.ylabel('w(n)')

plt.subplot(3,1,3)
plt.plot(ome/np.pi,dB,'b')
plt.plot(ome/np.pi,ome*0-As,'k') #Linea de referencia
plt.grid()
plt.title('Magnitud de la respuesta en dB')
plt.xlabel(r'Freuencai en unidades de $\pi$')
plt.ylabel('dB')
plt.axis([0,1,-100,10])

plt.figure()
plt.plot(ome*fs/(2*np.pi),mag,'b',lw=2)
plt.xlabel('Frecuencia en Hz'),plt.ylabel('Amplitud')
plt.grid()

plt.figure()
plt.plot(n/fs,xn)
plt.plot(n/fs,yn.real,'r')
plt.plot(n/fs,ync,'--g')
plt.grid()

plt.show()

