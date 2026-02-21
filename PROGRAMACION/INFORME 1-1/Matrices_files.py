from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb
import numpy as np
import pandas as pd

class Matriz_files(Tk):
    def __init__(self): 
        super().__init__()
        
        self.geometry("400x300")
        self.title("Dimensiones  de la Matriz")
        
        self.entry_row = Entry(width=10)
        self.entry_row.grid(row=0, column=1)
        self.entry_column = Entry(width=10)
        self.entry_column.grid(row=1, column=1)
        
        Label(self, text="Ingrese el numero de fila:").grid(row=0, column=0)
        Label(self, text="Ingrese el numero de columnas:").grid(row=1, column=0)
        
        

Matriz_files().mainloop()
    