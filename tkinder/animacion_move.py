import tkinter as tk

def mover():
    canvas.move(rectangulo, 5, 0)  # Mover el rectángulo en incrementos de 5 píxeles hacia la derecha
    if canvas.coords(rectangulo)[0] < 300:  # Si el rectángulo no ha llegado a la posición final
        ventana.after(50, mover)  # Esperar 50 milisegundos y llamar a la función mover nuevamente

# Crear una ventana
ventana = tk.Tk()

# Crear un lienzo (canvas)
canvas = tk.Canvas(ventana, width=400, height=200)
canvas.pack()

# Crear un rectángulo en el lienzo
rectangulo = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Iniciar la animación
mover()

# Ejecutar la ventana
ventana.mainloop()
