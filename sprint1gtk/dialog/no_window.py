import tkinter as tk

def show_no_window(question):
    no_root = tk.Tk()
    no_root.title("Respuesta: No")
    
    label = tk.Label(no_root, text=question)
    label.pack()

    no_root.mainloop()