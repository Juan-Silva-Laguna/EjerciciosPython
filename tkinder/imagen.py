from tkinter import *

ventana = Tk()
ventana.title("Imagen en Tk")
ventana.geometry("568x516")
# Cargar imagen del disco.
imagen = PhotoImage(file="C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/tkinder/piches.png")
# Insertarla en una etiqueta.
label = Label(ventana, image=imagen).place(x=0,y=0)
# label.pack()
ventana.mainloop()