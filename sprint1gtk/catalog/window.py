from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk 


class MainWindow():

        def onButtonClicked(self, cell):
                message = "Has hecho click en la celda" + cell.title
                messagebox.showinfo("Información", message)

        def __init__(self, root):
                root.title("5 personajes protagonistas")
                self.root = root
                
                self.cells = [
                        Cell("Agallas el perro Cobarde", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Agallas.jpg", "Agallas es un perro muy tímido que debe proteger a sus amos, Muriel y don Justo, de situaciones paranormales y la presencia de alienígenas mal intencionados."),
                        Cell("Rayo Mcqueen", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Cars.jpeg", "Es un automóvil de carreras prosopopéyico protagonista de las películas de Cars, así como en varios de sus cortometrajes y series animadas, donde ejerce como el principal protagonista de la franquicia."),
                        Cell("Eric Cartman", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Cartman.jpg", "Es un personaje ficticio de la serie de dibujos animados estadounidense South Park."),
                        Cell("Axel Blaze", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Axel.jpg", "Personaje del anime Inazuma Eleven. Axel Blaze es el delantero estrella del Raimon y del Inazuma Japón, la selección nacional de Japón."),
                        Cell("Finn el humano", "C:/Users/rubip/DesarrolloInterfaces/Catalog/undefined/Finn.jpg", "es un personaje ficticio creado por Pedlenton Ward e introducido como el personaje principal de la serie animada Adventure Time.​")
                ]

                        #Bucle para leer la lista
                for i, cell in enumerate(self.cells):

                        label = ttk.Label(root, image = cell.imageTk, text = cell.title, compound = tk.BOTTOM)
                        label.grid(row = 0,column = i)
                        label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))
