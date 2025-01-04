import tkinter as tk

def cambiar_tamano():
    coordenadas = canvas.coords(rectangulo)  # Obtener las coordenadas actuales del rectángulo
    ancho_actual = coordenadas[2] - coordenadas[0]
    alto_actual = coordenadas[3] - coordenadas[1]
    nuevo_ancho = ancho_actual + 10
    nuevo_alto = alto_actual + 10
    canvas.coords(rectangulo, coordenadas[0], coordenadas[1], coordenadas[0] + nuevo_ancho, coordenadas[1] + nuevo_alto)
    ventana.after(500, cambiar_tamano)  # Cambiar el tamaño cada 0.5 segundos

# Crear una ventana
ventana = tk.Tk()

# Crear un lienzo (canvas)
canvas = tk.Canvas(ventana, width=400, height=200)
canvas.pack()

# Crear un rectángulo en el lienzo
rectangulo = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Iniciar la animación
cambiar_tamano()

# Ejecutar la ventana
ventana.mainloop()
