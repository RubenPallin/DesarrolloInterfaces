# Importamos las bibliotecas necesarias
import threading
from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk
import requests
from window import MainWindow

# Definimos la clase LoadingWindow
class LoadingWindow:
    def __init__(self, root):
        # Inicializamos la ventana de carga
        self.root = root
        self.root.title("Cargando...")  # Establecemos el título
        self.root.geometry("170x128")  # Configuramos el tamaño
        self.root.resizable(False, False)  # Deshabilitamos la redimensión

        # Mostramos un mensaje de "Cargando datos..."
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        # Creamos un círculo de progreso
        label_bg_color = self.label.cget("bg")
        self.canvas = tk.Canvas(self.root, width=68, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        # Dibujamos el círculo de progreso
        self.draw_progress_circle(self.progress)

        self.finished = False
        self.json_data = []

        # Iniciamos una rosca de subproceso para obtener datos JSON
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        # Verificamos el estado del subproceso
        self.check_thread()

        # Configuramos el tamaño y la posición de la ventana de carga
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

    def draw_progress_circle(self, progress):
        # Dibujamos un círculo de progreso
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 35, 35,
                                start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)

    def update_progress_circle(self):
        # Actualizamos el círculo de progreso
        if self.progress < 180:
            self.progress += 10
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)

    def fetch_json_data(self):
        # Descargamos datos JSON desde una URL en GitHub
        github_url = "https://raw.githubusercontent.com/RubenPallin/DesarrolloInterfaces/main/recursos/catalog.json"

        try:
            response = requests.get(github_url)
            response.raise_for_status()  # Comprobamos si la solicitud fue exitosa

            if response.status_code == 200:
                self.json_data = response.json()
                self.finished = True
            else:
                messagebox.showerror("Error", f"Error al descargar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Manejamos errores de solicitud, por ejemplo, si la URL es incorrecta
            messagebox.showerror("Error", f"Error al descargar datos: {str(e)}")

    def check_thread(self):
        # Verificamos el estado del subproceso
        if self.finished:
            self.root.destroy()
            self.launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

    def launch_main_window(self, json_data):
        # Creamos la ventana principal y mostramos los datos JSON
        root = tk.Tk()
        app = MainWindow(root, json_data)
        root.mainloop()
