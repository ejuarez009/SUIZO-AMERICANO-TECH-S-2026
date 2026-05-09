from tkinter import *; from tkinter import filedialog as fd; from tkinter import messagebox as mb #type: ignore
from tkinter.ttk import Treeview
import re


class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("600x600")

        self.title("Practica Archivos - Elmer Juarez")
        self.textbox = Text(width=40, height=10)
        self.textbox.pack()
        
        Button(text="Crear archivo", command=self.crear).pack(side=LEFT)
        Button(text="Abrir archivo", command=self.abrir).pack(side=LEFT)
        Button(text="Grabar", command=self.grabar).pack(side=LEFT)
        Button(text="Analizar Archivo", command=self.analizar).pack(side=LEFT) #type:ignore
        
        self.label_ruta = Label(text="--ruta--", fg="gray")
        self.label_ruta.pack()
        
    
    def crear(self): 
        self.ruta = fd.askopenfilename()
        self.label_ruta.config(text=f"RUTA:{self.ruta}", fg="blue")
        with open(self.ruta, 'w', encoding='utf-8') as archivo: 
            archivo.write('')
    
    def abrir(self): 
        self.ruta = fd.askopenfilename()
        self.label_ruta.config(text=f"RUTA:{self.ruta}",fg="blue")
        with open(self.ruta, 'r', encoding='utf-8') as archivo:
            
            cont_digit = 0
            patron = "0123456789"
            for linea in archivo.readlines():
                for char in linea: 
                    if char in patron:
                        cont_digit+=1
            print(cont_digit)
            
            for linea in archivo.readlines():
                texto = re.split(r"[\s\t\n*]+", linea)
                print(texto)
                for dato in texto: 
                    print(dato)

    def grabar(self): 
        if not self.ruta: 
            mb.showinfo("Atencion", "Debe haber creado o abierto el archivo")
    
    def analizar(self, filas): 
        cont_digit = 0
        patron = "0123456789"
        
    def conjetura(self,num): 
        
    
    def hexadecimal(self, num): 
        pass
    
    def binario(self, num): 
        pass
    
    def romanos(self, num): 
        pass


app().mainloop()