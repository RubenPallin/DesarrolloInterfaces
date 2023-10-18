import threading
from tkinter import ttk, messagebox  
import tkinter as tk 
from cell import Cell 
from PIL import Image, ImageTk  
import requests
from window import MainWindow

class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x128")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root,width=68, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.finished = False
        self.json_data = []

        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        self.check_thread()

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 35, 35,
                                start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)

    def update_progress_circle(self):
        if self.progress < 180:
            self.progress += 10
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)
    
    def fetch_json_data(self):
        github_url = "https://raw.githubusercontent.com/RubenPallin/DesarrolloInterfaces/main/recursos/catalog.json"

        try:
            response = requests.get(github_url)
            response.raise_for_status()  # Comprueba si la solicitud fue exitosa

            if response.status_code == 200:
                self.json_data = response.json()
                self.finished = True
            else:
                messagebox.showerror("Error", f"Error al descargar datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Maneja errores de solicitud, por ejemplo, si la URL es incorrecta
            messagebox.showerror("Error", f"Error al descargar datos: {str(e)}")

    def check_thread(self):
            if self.finished:
                self.root.destroy()
                self.launch_main_window(self.json_data)
            else:
                self.root.after(100, self.check_thread)

    def launch_main_window(self, json_data):
        root = tk.Tk()
        app = MainWindow(root,json_data)
        root.mainloop()
