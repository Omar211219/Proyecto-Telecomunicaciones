import scipy.io.wavfile as waves
from scipy.fft import fft
import scipy.fftpack as fftpk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

def fase2():
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

        # Phase que responde al audio original en la frecuencia
        N=len(uncanal)
        f=fft(uncanal)
        Y=np.unwrap(np.angle(f))
        X=(np.arange(0,1-1/N,1/N))*fsonido

        # Salida Grafica
        plt.plot(X[range(N//2)], Y[range(N//2)])
        plt.title('Fase 2 con Dominio en la Frecuencia')
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Amplitud")
        plt.show()
    except:
        messagebox.showwarning("Error", "El audio no existe, por favor grabe uno desde la app")