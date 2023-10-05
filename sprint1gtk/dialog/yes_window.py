import tkinter as tk

def show_yes_window(question):
    yes_root = tk.Tk()
    yes_root.title("Respuesta: Sí")
    
    label = tk.Label(yes_root, text=question)
    label.pack()

    yes_root.mainloop()