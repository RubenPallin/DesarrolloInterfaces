from tkinter import Tk
from window import MainWindow

if __name__== "__main__":
    root = Tk()  # Crea una instancia de la clase "Tk" que representa la ventana principal de la aplicación
    app = MainWindow(root)  # Crea una instancia de la clase "MainWindow" y pasa la ventana raíz "root" como argumento
    root.mainloop()  # Inicia el bucle principal de la aplicación, que mantiene la ventana abierta y responde a eventos
