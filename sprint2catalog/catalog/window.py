# Importación de bibliotecas
from tkinter import ttk, messagebox  
import tkinter as tk 
from cell import Cell 
from PIL import Image, ImageTk  
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

        # Crea una lista de objetos "Cell" que representan a los personajes protagonistas
        self.cells = []
        for data in self.json_data:
            #extraigo los datos de cada JSONObject 
            nombre = data.get("name")
            descripcion = data.get("description")
                #estos dos pasos son para "descargar" la imagen y no enviarla como un url
            image_url = data.get("image_url")
            
            #creo una celda para cada dato(object) y la incluyo en una lista
            self.cells.append(Cell(nombre, image_url, descripcion))

        # Bucle para mostrar las celdas en la ventana
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: cell.create_detail_window(root))  # Vincula el clic izquierdo a la función "onButtonClicked"
