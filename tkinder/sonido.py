import tkinter as tk
import pygame

def reproducir_sonido():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/borbuja.mp3")
    pygame.mixer.music.play()

# Crear una ventana
ventana = tk.Tk()

# Crear un botón para reproducir el sonido
boton_sonido = tk.Button(ventana, text="Reproducir sonido", command=reproducir_sonido)
boton_sonido.pack()

# Ejecutar la ventana
ventana.mainloop()
