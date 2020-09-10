import scipy.io.wavfile as waves
from scipy.fft import fft
import scipy.fftpack as fftpk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

def fase3():
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
                #la amplitud de la señal portadora es mucho mayor
        moduladora=uncanal[0:k].astype(float)
        dt=1/fsonido
        t=np.arange(0,k*dt,dt)

        # Portadora:
        fc = 5500
        portadora = np.cos(2*np.pi*fc*t)

        # normalizar y subir a positiva
        moduladoranorm = moduladora/np.max(moduladora)
        moduladora = (1+ moduladoranorm)

        # Modular portadora
        Ac=1
        modulada = Ac*moduladora*portadora
        modulada=abs(fft(modulada))
        freq= fftpk.fftfreq(len(modulada),(1.0/fsonido))

        # SALIDA GRAFICA
        plt.plot(freq[range(len(modulada)//2)], modulada[range(len(modulada)//2)],label='modulada')
        plt.title(' Señal modulada en AM S(t)')
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.show()
    except:
        messagebox.showwarning("Error", "El audio no existe, por favor grabe uno desde la app")