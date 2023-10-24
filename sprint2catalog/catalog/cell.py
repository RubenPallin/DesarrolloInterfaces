import tkinter as tk
import requests
from PIL import Image, ImageTk


class Cell:
    def __init__(self, title, image_url, description):
        self.title = title
        self.image_path = self.download_image(image_url)  # Descarga la imagen y obtiene la ruta local
        self.description = description
        self.load_image()

    def download_image(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()

            if response.status_code == 200:
                image_data = response.content
                image_filename = "local_image.jpg"  # Puedes definir un nombre de archivo local
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_data)
                return image_filename
            else:
                print(f"Error al descargar la imagen: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error al cargar la imagen: {e}")
        return None

    def load_image(self):
        if self.image_path:
            try:
                image = Image.open(self.image_path)
                # Redimensiona la imagen a 100x100 píxeles
                image = image.resize((100, 100), Image.LANCZOS)
                self.image_tk = ImageTk.PhotoImage(image)
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")
                self.image_tk = None
        else:
            self.image_tk = None
