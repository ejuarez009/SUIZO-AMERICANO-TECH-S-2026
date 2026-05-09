from tkinter import*
from tkinter import filedialog as fd 
from tkinter import messagebox as mb 
import re


class app(Tk):
    def __init__(self): 
        super().__init__()
        self.geometry("300x300")
        self.title("Autor: Elmer Juarez")
        
        Button(text="Analizar", command=self.analizar).pack()

        self.label_fil = Label(text="--resultado fila--")
        self.label_fil.pack()
        
        self.label_col = Label(text="--resultado columna")
        
    def analizar(self): 
        self.ruta = fd.askopenfilename()
        with open(self.ruta,'r', encoding='utf-8') as archivo: 
            contenido = archivo.read()
            lineas = contenido.splitlines()
            sumrow = []
            sumcol = []
            filas = []
            for linea in lineas: 
                valores = re.findall(r"\d+", linea)
                acufila = 0
                for numero in valores: 
                    acufila += int(numero)
                sumrow.append(acufila)
                filas.append(list(valores))
            
            print(filas)
            print(sumrow)
            print(sumcol)
            for i in range(len(filas[0])): 
                suma = 0
                print(filas[i])
                for j in range(len(filas)): 
                    suma += int(filas[j][i])
                sumcol.append(suma)
            
            
            


app().mainloop()