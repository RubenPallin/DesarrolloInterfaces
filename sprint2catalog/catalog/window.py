# Importación de bibliotecas
from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import DetailWindow
import requests
from io import BytesIO

class MainWindow():
    # Constructor de la clase
    def __init__(self, root, json_data):
        self.root = root
        self.json_data = json_data
        # Configura el título de la ventana principal
        root.title("5 personajes protagonistas")
        self.root = root  # Almacena la ventana raíz en una variable de instancia "self.root"

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("{}x{}+{}+{}".format(120, 120, int(x), int(y))) 

        # Crea una lista de objetos "Cell" que representan a los personajes protagonistas
        self.cells = []
        for data in self.json_data:
            # Extraigo los datos de cada JSONObject
            nombre = data.get("name")
            descripcion = data.get("description")
            # Estos dos pasos son para "descargar" la imagen y no enviarla como una URL
            image_url = data.get("image_url")

            # Creo una celda para cada dato (object) y la incluyo en una lista
            self.cells.append(Cell(nombre, image_url, descripcion))

        # Bucle para mostrar las celdas en la ventana
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.show_detail_window(cell))  # Vincula el clic izquierdo a la función "show_detail_window"

    def show_detail_window(self, cell):
        # Muestra la ventana de detalles cuando se hace clic en una celda
        detail_window = DetailWindow(self.root, cell)
