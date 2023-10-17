import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    # Constructor de la clase
    def __init__(self, title, image_path, description):
        self.title = title  
        self.image_path = image_path  
        self.description = description  

        # Abre la imagen, la redimensiona a 100x100 píxeles y la almacena en "self.image_tk"
        resized_image = Image.open(self.image_path).resize((100, 100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)
