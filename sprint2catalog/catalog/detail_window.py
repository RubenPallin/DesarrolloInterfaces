from tkinter import Toplevel, Label, messagebox
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from io import BytesIO
import requests

class DetailWindow:
    def __init__(self, root, cell):
        self.root = root
        self.cell = cell

        # Crea una nueva ventana secundaria (ventana de detalles)
        self.detail_window = tk.Toplevel(root)
        self.detail_window.title(self.cell.title)

        # Carga la imagen de la instancia de Cell
        image = self.cell.image_tk
        image_label = ttk.Label(self.detail_window, image=image)
        image_label.image = image
        image_label.pack()

        title_label = ttk.Label(self.detail_window, text=self.cell.title, font=("JetBrains mono", 16))
        title_label.pack()

        description_label = ttk.Label(self.detail_window, text=self.cell.description, wraplength=300)
        description_label.pack()

        # Crea y muestra una etiqueta con la descripción.
        self.root.update_idletasks()
        x = ( self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = ( self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")


