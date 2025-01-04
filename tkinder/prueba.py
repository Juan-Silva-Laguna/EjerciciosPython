
import tkinter as tk
import pygame

def button_click():
    print("¡Haz hecho clic en una etiqueta!")
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/borbuja.mp3")
    pygame.mixer.music.play()

root = tk.Tk()

# Carga la imagen principal
image_main = tk.PhotoImage(file="C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/piches.png")

# Carga las imágenes para los lados
image_left = tk.PhotoImage(file="C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/piches.png")
image_right = tk.PhotoImage(file="C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/piches.png")

# Define las dimensiones deseadas para la imagen
width = 80
height = 80

# Redimensiona la imagen a las dimensiones especificadas
resized_image_main = image_main.subsample(image_main.width() // width, image_main.height() // height)
resized_image_left = image_left.subsample(image_left.width() // width, image_left.height() // height)
resized_image_right = image_right.subsample(image_right.width() // width, image_right.height() // height)

# Crea una etiqueta con la imagen
label_main = tk.Label(root, image=resized_image_main)
label_left = tk.Label(root, image=resized_image_left)
label_right = tk.Label(root, image=resized_image_right)


# Vincula el evento del clic a la función button_click para todas las etiquetas
labels = [label_main, label_left, label_right]
for label in labels:
    label.bind("<Button-1>", lambda event: button_click())

# Posiciona las etiquetas en una cuadrícula
label_main.grid(row=0, column=1)
label_left.grid(row=0, column=0)
label_right.grid(row=0, column=2)

root.mainloop()
