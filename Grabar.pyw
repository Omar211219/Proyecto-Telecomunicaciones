import pyaudio
import wave
from tkinter import *
import threading
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "Sound.wav"

def clear_contador():
    global contador,contador1,contador2
    contador=0
    contador1=0
    contador2=0

def dire():
    directorio_actual.set(os.getcwd())

def iniciar():
    global grabando
    clear_contador()
    bloqueo('disabled')
    grabando=True
    t=threading.Thread(target=Grabar)
    t.start()
    t1=threading.Thread(target=cuenta)
    t1.start()

def formato(c):
    if c<10:
        c="0"+str(c)
    return c

def cuenta():
    global proceso
    global contador,contador1,contador2
    time['text'] = str(formato(contador1))+":"+str(formato(contador2))+":"+str(formato(contador))
    contador+=1
    if contador==60:
        contador=0
        contador2+=1
    if contador2==60:
        contador2=0
        contador1+=1
    proceso=time.after(1000, cuenta)

def bloqueo(s):
    btnIniciar.config(state=s)

def parar():
    global grabando
    if grabando==True:
        grabando=False
    bloqueo('normal')
    raiz.destroy()

def Grabar():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    while grabando==True:
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

raiz=Tk()
raiz.title("Grabar")
raiz.iconbitmap("C:/Users/Luis Ramirez/Downloads/universidad/tele/pro/record.ico")
raiz.config(bg="grey")
raiz.resizable(width=False, height=False)

grabando=False
p = pyaudio.PyAudio()

time = Label(raiz, fg='green', width=8, height=2, text="00:00:00", bg="black", font=("","30"))
time.grid(row=1, column=1, columnspan=2)

img1=PhotoImage(file="grabar.png")
btnIniciar=Button(raiz, image=img1, command=iniciar, cursor="hand2")
btnIniciar.grid(row=2, column=1)

img2=PhotoImage(file="detener.png")
btnParar=Button(raiz, image=img2, command=parar, cursor="hand2")
btnParar.grid(row=2, column=2)

raiz.mainloop()