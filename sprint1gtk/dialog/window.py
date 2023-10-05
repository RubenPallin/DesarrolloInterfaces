import tkinter as tk
from tkinter import ttk
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:
    def on_button_click(sef):
        pass
    def __init__(self, root):
        self.root = root
        self.question_label = tk.Label(root, text="¿Desea continuar?")
        self.question_label.pack()

        self.yes_button = ttk.Button(root, text="Sí", command=self.show_yes_window)
        self.yes_button.pack(side=tk.LEFT)

        self.no_button = ttk.Button(root, text="No", command=self.show_no_window)
        self.no_button.pack(side=tk.LEFT)

    def show_yes_window(self):
        question = "Ha elegido si"
        show_yes_window(question)

    def show_no_window(self):
        question = "Ha elegido no continuar."
        show_no_window(question)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    
