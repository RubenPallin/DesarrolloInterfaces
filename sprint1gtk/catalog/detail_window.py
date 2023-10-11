import tkinter as tk
from tkinter import ttk

class DetailWindow:

    def __init__(self, root, title, image, description):

        self.root = root
        self.title = title
        self.image = image
        self.description = description
        self.window = tk.Toplevel(root)
        self.window.title(self.title)

        image_label = ttk.Label(self.window, image = self.image)
        image_label.pack()
        title_label = ttk.Label(self.window, text = self.title, font=("JetBrains mono", 16))
        title_label.pack()
        description_label = ttk.Label(self.window, text = self.description, wraplength = 300)
        description_label.pack()
