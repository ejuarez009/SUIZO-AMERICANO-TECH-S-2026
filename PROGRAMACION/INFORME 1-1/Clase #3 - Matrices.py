import numpy as np 
from tkinter import*; from tkinter import messagebox as mb; from tkinter import filedialog as fd

class Matrix(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        
        Label(self, text="Ingrese el número de filas:").grid(row=0, column=0)
        Label(self, text="Ingrese el numero de columnas").grid(row=1,column=0)
        
        self.entry_column = Entry(width=10)
        self.entry_column.grid(row=0, column=1)
        self.entry_row = Entry(width=10)
        self.entry_row.grid(row=1, column=1)
        
        self.button_abrir = Button(text="ABRIR ARCHIVO", command=self.multiplicar).grid(row=2, column=0)
        
    
    def abrir(self): 
        ruta = fd.askopenfilename()
        return ruta                                      #ESTABAS ABRIENDO LA FUNCION ABRIR DESDE EL BOTON Y DEBERIA SER LA FUNCION MULTIPLICAR
    def multiplicar(self): 
        col = int(self.entry_column.get())
        ro = int(self.entry_row.get())
        
        if self.validar(col, ro):
            mb.showinfo("ATENCION", "Matriz Valida")
            matriz1 = np.loadtxt(self.abrir(), delimiter='-')
            matriz2 = np.random.randint(1, 25, (ro, col)) 
            print(matriz1)
            print('==============================================')
            print(matriz2)
            result = np.dot(matriz1, matriz2) #El metodo dot funciona para multiplicar dos matices asignandoles solo los parametros (Matrices)
            print("=======LA MULTIPLICACION DE LA MATRICES ES:=========")
            print(result)
        else:
            print("No válida")    
            
    
    def validar(self, p_row, p_column): 
        if p_row == 3 &  p_column == 3: 
            dato = True
        else: 
            dato = False
        return dato
    
Matrix().mainloop()