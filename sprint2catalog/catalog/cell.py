import tkinter as tk
import requests
from PIL import Image, ImageTk
from detail_window import DetailWindow

class Cell:
    import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests

class Cell:
    def __init__(self, title, image_url, description):
        self.title = title
        self.image_url = image_url
        self.description = description
        self.load_image()

    def load_image(self):
        try:
            response = requests.get(self.image_url)
            response.raise_for_status()

            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            image = image.resize((100, 100), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(image)
        except (requests.RequestException, Exception) as e:
            print(f"Error al cargar la imagen: {e}")
            # Cargar una imagen de reemplazo en caso de error
            self.image_tk = ImageTk.PhotoImage(Image.new("RGB", (100, 100), (255, 255, 255)))
    def create_detail_window(self, root):
        detail_window = DetailWindow(root, self.title, self.image_path, self.description)
