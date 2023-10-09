from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():

        def on_button_clicked(self, cell):
                message = "Has hecho click en la celda" + cell.title
                messagebox.showinfo("Información", message)

        def __init__(self, root):
                root.title("MainWindow")

                self.cells = [
                        Cell("Personaje 1", "C:\Users\rubip\DesarrolloInterfaces\Fotos_DesarrolloInt\Agallas_edit"),
                        Cell("Personaje 2", "C:\Users\rubip\DesarrolloInterfaces\Fotos_DesarrolloInt\Cars_edit"),
                        Cell("Personaje 3", "C:\Users\rubip\DesarrolloInterfaces\Fotos_DesarrolloInt\Cartman_edit"),
                        Cell("Personaje 4", "C:\Users\rubip\DesarrolloInterfaces\Fotos_DesarrolloInt\Axel_edit"),
                        Cell("Personaje 5", "C:\Users\rubip\DesarrolloInterfaces\Fotos_DesarrolloInt\Finn_edit")
                ]

                for i, cell in enumerate(self.cells):
                        label = ttk.label(root, image= cell.image_tk, text=cell.title, compound= tk.BOTTOM)
                        label.grid(row=i, column=0)
                        label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))
