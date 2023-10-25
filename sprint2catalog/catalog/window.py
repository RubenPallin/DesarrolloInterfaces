# Importamos las bibliotecas necesarias
from tkinter import Toplevel, Label, messagebox, ttk
import tkinter as tk
from cell import Cell
from detail_window import DetailWindow
from tkinter import Canvas, Scrollbar, Frame

# Definimos la clase MainWindow
class MainWindow:
    def __init__(self, root, json_data):
        # Inicializamos la clase con la ventana raíz y los datos JSON
        self.root = root
        self.json_data = json_data

        # Establecer el título de la ventana principal
        root.title("5 personajes protagonistas")
        
        # Calcular la posición para centrar la ventana en la pantalla
        x = (self.root.winfo_screenwidth() - 150) / 2
        y = (self.root.winfo_screenheight() - 200) / 2
        self.root.geometry("150x200+{}+{}".format(int(x), int(y)))

        # Configurar el menú de ayuda
        self.setup_menu_ayuda()

        # Crear un lienzo y una barra de desplazamiento
        self.canvas = Canvas(self.root)
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        # Configurar el evento para ajustar el scroll automáticamente
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Crear la ventana dentro del lienzo y vincularla con la barra de desplazamiento
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Inicializar una lista para almacenar objetos Cell (representando personajes)
        self.cells = []
        for data in self.json_data:
            nombre = data.get("name")
            descripcion = data.get("description")
            image_url = data.get("image_url")
            self.cells.append(Cell(nombre, image_url, descripcion))

        # Agregar cada elemento (celda) a la ventana desplazable
        for i, cell in enumerate(self.cells):
            self.add_item(cell)

        # Configurar la disposición de la ventana y la barra de desplazamiento
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def add_item(self, cell):
        # Crear un marco (Frame) para cada elemento en la ventana desplazable
        frame = Frame(self.scrollable_frame)
        frame.pack(pady=10)

        # Crear una etiqueta (Label) para mostrar la imagen y el título del elemento
        label = ttk.Label(frame, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
        label.grid(row=0, column=0)

        # Vincular la función show_detail_window al hacer clic en la etiqueta
        label.bind("<Button-1>", lambda event, clickedCell=cell: self.show_detail_window(clickedCell))

    def setup_menu_ayuda(self):
        # Configurar un menú de ayuda en la ventana principal
        def show_about_dialog():
            messagebox.showinfo("Acerca de", "Información acerca del desarrollador.")

        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Acerca de", command=show_about_dialog)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        self.root.config(menu=menubar)

    def show_detail_window(self, cell):
        # Mostrar la ventana de detalles cuando se hace clic en una celda
        detail_window = DetailWindow(self.root, cell)
