import scipy.io.wavfile as waves
from scipy.fft import fft
import scipy.fftpack as fftpk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

def fase1():
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
        
        # tranformar en la frecuencia
        f=abs(fft(uncanal))
        freq= fftpk.fftfreq(len(f),(1.0/fsonido))

        N = uncanal.shape[0]

        # Salida Grafica
        fig=plt.figure("Filtro")
        fig.subplots_adjust(hspace=0.5, wspace=0.5)

        p1=fig.add_subplot(2,1,1)
        p1.plot(np.arange(N) / fsonido, uncanal)
        p1.set_title('Audio Original')
        p1.set_xlabel("Time [s]")
        p1.set_ylabel("Amplitud")

        p2=fig.add_subplot(2,1,2)
        p2.plot(freq[range(len(f)//2)], f[range(len(f)//2)])
        p2.set_title('Fase 1 con Dominio en la Frecuencia')
        p2.set_xlabel("Frecuencia (Hz)")
        p2.set_ylabel("Amplitud")

        plt.show()
    except:
        messagebox.showwarning("Error", "El audio no existe, por favor grabe uno desde la app")