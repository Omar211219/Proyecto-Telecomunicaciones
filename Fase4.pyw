import scipy.io.wavfile as waves
from scipy.fft import fft
import scipy.fftpack as fftpk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

def fase4():
    try:
        audio='Sound.wav'
        fsonido, sonido = waves.read(audio)

        # Extrae un canal en caso de estéreo
        canales=sonido.shape
        cuantos=len(canales)
        canal = 0
        if (cuantos==1): # Monofónico
            uncanal=sonido
        if (cuantos>=2): # Estéreo
            uncanal=sonido[:,canal]

        k=500   # k son las muestras que utilizaremos de la senal original. al usar el largo del array como len(uncanal) 
            #la cantidad de la señal es mucho mayor
        moduladora=uncanal[0:k].astype(float)
        dt=1/fsonido
        t=np.arange(0,k*dt,dt)

        # Portadora:
        Fc=fsonido
        FS=2.2*Fc
        freqdev=75e3

        # Modular portadora
        int_x = np.cumsum(moduladora)/FS

        xi=np.cos(2*np.pi*freqdev*int_x)
        xq=np.sin(2*np.pi*freqdev*int_x)

        FM = np.cos(2*np.pi*Fc*t)*xi-np.sin(2*np.pi*Fc*t)*xq

        FM=abs(fft(FM))
        freq= fftpk.fftfreq(len(FM),(1.0/fsonido))

        # SALIDA GRAFICA
        plt.plot(freq[range(len(FM)//2)], FM[range(len(FM)//2)],label='modulada')
        plt.title(' Señal modulada en FM S(t)')
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.show()
    except:
        messagebox.showwarning("Error", "El audio no existe, por favor grabe uno desde la app")