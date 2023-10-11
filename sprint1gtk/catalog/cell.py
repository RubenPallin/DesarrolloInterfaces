import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, image_path, description):
        self.title = title
        self.path = image_path
        self.description = description

    
        resizedImage = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resizedImage)

        # Convierte la imagen redimensionada en un objeto ImageTk para usar en Tkinter
        self.imageTk = ImageTk.PhotoImage(resizedImage)
