import tkinter as tk

def toggle_visibility():
    if entry.winfo_ismapped() and label.winfo_ismapped():
        entry.grid_forget()
        label.grid_forget()
    else:
        entry.grid(row=0, column=0)
        label.grid(row=1, column=0)

root = tk.Tk()

# Crear el Entry y el Label
entry = tk.Entry(root)
label = tk.Label(root, text="Texto de ejemplo")

# Posicionar el Entry y el Label inicialmente
entry.grid(row=0, column=0)
label.grid(row=1, column=0)

# Botón para controlar la visibilidad
button = tk.Button(root, text="Alternar Visibilidad", command=toggle_visibility)
button.grid(row=2, column=0)

root.mainloop()
