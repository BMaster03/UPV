import numpy as np

def fpb_ideal(wc, M):
    pm = (M-1)/2 # punto medio del número de taps 
    n = np.arange(M)
    m = n - pm
    fpbi = (wc/np.pi) * np.sinc(m*wc/np.pi)

    return fpbi

def resp_frec(h, N):
    Hm = np.fft.fft(h, N)
    magH = np.abs(Hm)
    angH = np.angle(Hm)
    magH = magH[0:N//2]
    angH = angH[0:N//2]
    dB = 20 * np.log10((magH+1e-15)/np.max(max))
    m = np.arange(N/2)
    w = m * np.pi/((N/2)-1)

    return magH, angH, dB, w

