from tkinter import ttk, Button

class MainWindow:
    def on_button_click(sef):
        pass
    def __init__(self, root):
        self.root = root
        self.button = ttk.Button(self.root, text="Realizar acción", command= self.on_button_click)
        self.button.pack()
