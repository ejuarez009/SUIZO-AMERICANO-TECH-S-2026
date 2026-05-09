from tkinter import*; from tkinter import filedialog as fd; from tkinter import ttk

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("900x900")
        self.title("Tildes y Letras")



app().mainloop()