import tkinter as tk

def cambiar_color():
    color_actual = canvas.itemcget(rectangulo, "fill")
    nuevo_color = "red" if color_actual == "blue" else "blue"
    canvas.itemconfig(rectangulo, fill=nuevo_color)
    ventana.after(1000, cambiar_color)  # Cambiar el color cada 1 segundo

# Crear una ventana
ventana = tk.Tk()

# Crear un lienzo (canvas)
canvas = tk.Canvas(ventana, width=400, height=200)
canvas.pack()

# Crear un rectángulo en el lienzo
rectangulo = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Iniciar la animación
cambiar_color()

# Ejecutar la ventana
ventana.mainloop()
