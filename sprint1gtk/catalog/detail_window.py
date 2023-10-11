import tkinter as tk
from tkinter import ttk

class DetailWindow:

    # Constructor de la clase
    def __init__(self, root, title, image, description):
        # Inicializa la ventana de detalles con la información proporcionada
        self.root = root  
        self.title = title  
        self.image = image  
        self.description = description  
        
        # Crea una nueva ventana secundaria (ventana de detalles)
        self.window = tk.Toplevel(root)  # Crea una ventana secundaria que se abre en la ventana raíz
        self.window.title(self.title)  # Establece el título de la ventana de detalles con el título del personaje

        # Crea etiquetas para mostrar la imagen, el título y la descripción del personaje
        image_label = ttk.Label(self.window, image=self.image)
        image_label.pack()  

        title_label = ttk.Label(self.window, text=self.title, font=("JetBrains mono", 16))  
        title_label.pack()  

        description_label = ttk.Label(self.window, text=self.description, wraplength=300) 
        description_label.pack() 
