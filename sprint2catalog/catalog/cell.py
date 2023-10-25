# Importamos las bibliotecas necesarias
import tkinter as tk
import requests
from PIL import Image, ImageTk
from detail_window import DetailWindow
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests

# Definimos la clase Cell que representa un elemento (personaje) en nuestra aplicación
class Cell:

    def __init__(self, title, image_url, description):
        # Inicializamos la celda con el título, la URL de la imagen y la descripción
        self.title = title
        self.image_url = image_url
        self.description = description

        # Cargamos la imagen asociada a la celda
        self.load_image()

    def load_image(self):
        try:
            # Realizamos una solicitud HTTP para obtener la imagen desde la URL
            response = requests.get(self.image_url)
            response.raise_for_status()  # Comprobamos si la solicitud fue exitosa

            # Leemos los datos de la imagen y la redimensionamos a 100x100 píxeles
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            image = image.resize((100, 100), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(image)  # Convertimos la imagen en un formato compatible con tkinter
        except (requests.RequestException, Exception) as e:
            print(f"Error al cargar la imagen: {e}")
            # En caso de error, cargamos una imagen de reemplazo (imagen blanca de 100x100 píxeles)
            self.image_tk = ImageTk.PhotoImage(Image.new("RGB", (100, 100), (255, 255, 255)))

    def create_detail_window(self, root):
        # Creamos una ventana de detalles para mostrar la información del personaje
        detail_window = DetailWindow(root, self.title, self.image_path, self.description)
