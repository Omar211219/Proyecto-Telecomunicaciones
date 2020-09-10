from tkinter import *
from tkinter import messagebox
from os import remove
from Fase1 import fase1
from Fase2 import fase2
from Fase3 import fase3
from Fase4 import fase4
import os
import pygame

var=False

#----funciones-------------------------------------------------------

def grabar():
    pygame.mixer.quit()
    os.system('Grabar.pyw')

def salirapp():
    valor=messagebox.askquestion("Salir", "Desea salir de la app?")
    if valor=="yes":
        raiz.destroy()
    
def Play():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("Sound.wav")
        pygame.mixer.music.play()
    except:
        messagebox.showwarning("Error", "El audio no existe, por favor grabe uno desde la app")

def Pause():
    global var
    if var==False:
        pygame.mixer.music.pause()
        var=True
    elif var==True:
        pygame.mixer.music.unpause()
        var=False

def Stop():
    pygame.mixer.music.stop()

def Eliminar():
    pygame.mixer.quit()
    remove("Sound.wav")

#----Interfaz-------------------------------------------------------

raiz=Tk()

raiz.title("Proyecto")

raiz.iconbitmap("C:/Users/Luis Ramirez/Downloads/universidad/tele/pro/senal.ico")

raiz.config(bg="#49A")

raiz.resizable(width=False, height=False)

barra=Menu(raiz)

raiz.config(menu=barra, width=400, height=400)

#----------Barra-----------------------------------------------------

menu=Menu(barra, tearoff=0)
menu.add_command(label="Grabar", command=grabar)
menu.add_command(label="Salir", command=salirapp)
barra.add_cascade(label="Nuevo", menu=menu)

#---botones--------------------------------------------------------

fase1=Button(raiz, text="Fase 1", width=20, command=fase1, cursor="hand2")
fase1.grid(row=3, column=1)

fase2=Button(raiz, text="Fase 2", width=20, command=fase2, cursor="hand2")
fase2.grid(row=3, column=2)

fase3=Button(raiz, text="Fase 3", width=20, command=fase3, cursor="hand2")
fase3.grid(row=3, column=3)

fase4=Button(raiz, text="Fase 4", width=20, command=fase4, cursor="hand2")
fase4.grid(row=3, column=4)

imagen=PhotoImage(file="signal.png")
im=Label(raiz,image=imagen).grid(row=1, column=1, columnspan=4)

img1=PhotoImage(file="play.png")
play=Button(raiz, image=img1, command=Play, cursor="hand2")
play.grid(row=2, column=1)

img2=PhotoImage(file="pause.png")
play=Button(raiz, image=img2, command=Pause, cursor="hand2")
play.grid(row=2, column=2)

img3=PhotoImage(file="stop.png")
play=Button(raiz, image=img3, command=Stop, cursor="hand2")
play.grid(row=2, column=3)

img4=PhotoImage(file="trash.png")
play=Button(raiz, image=img4, command=Eliminar, cursor="hand2")
play.grid(row=2, column=4)

raiz.mainloop()