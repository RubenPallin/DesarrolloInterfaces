# Importación de bibliotecas
from tkinter import ttk, messagebox  
import tkinter as tk 
from cell import Cell 
from PIL import Image, ImageTk  
from detail_window import DetailWindow 

class MainWindow():
    # Constructor de la clase
    def __init__(self, root, json_data):
        self.root = root
        self.json_data = json_data
        # Configura el título de la ventana principal
        root.title("5 personajes protagonistas")
        self.root = root  # Almacena la ventana raíz en una variable de instancia "self.root"

        # Crea una lista de objetos "Cell" que representan a los personajes protagonistas
        self.cells = [
            Cell("Agallas el perro Cobarde", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Agallas.jpg", "Agallas es un perro muy tímido que debe proteger a sus amos, Muriel y don Justo, de situaciones paranormales y la presencia de alienígenas mal intencionados."),
            Cell("Rayo Mcqueen", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Cars.jpeg", "Es un automóvil de carreras prosopopéyico protagonista de las películas de Cars, así como en varios de sus cortometrajes y series animadas, donde ejerce como el principal protagonista de la franquicia."),
            Cell("Eric Cartman", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Cartman.jpg", "Es un personaje ficticio de la serie de dibujos animados estadounidense South Park."),
            Cell("Axel Blaze", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Axel.jpg", "Personaje del anime Inazuma Eleven. Axel Blaze es el delantero estrella del Raimon y del Inazuma Japón, la selección nacional de Japón."),
            Cell("Finn el humano", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Finn.jpg", "Es un personaje ficticio creado por Pedlenton Ward e introducido como el personaje principal de la serie animada Adventure Time.​")
        ]

        # Bucle para mostrar las celdas en la ventana
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)  # Coloca la etiqueta en una fila específica de la ventana
            label.bind("<Button-1>", lambda event, cell=cell: self.onButtonClicked(cell))  # Vincula el clic izquierdo a la función "onButtonClicked"

    # Método llamado cuando se hace clic en una celda
    def onButtonClicked(self, cell):
        detail_window = DetailWindow(self.root, cell.title, cell.image_tk, cell.description)
