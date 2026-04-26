from tkinter import ttk; from tkinter import*; from tkinter import messagebox as mb
import math 

class app(Tk): 
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Laboratorio Compu - Elmer Juarez C5")
        Label(text="Ingrese el tamaño para el vector:").grid(row=0, column=3)
        self.entry_tam = Entry(self)
        self.entry_tam.grid(row=1, column=3)
        
        Button(text="Crear Vector", command=self.crear).grid(row=2, column=3)
    
    def crear(self): 
        try: 
            tamaño = int(self.entry_tam.get())
        except ValueError: 
            mb.showerror("Error", "Tamaño Invalido")
            
        vector = [0] * tamaño
        self.spointer = 0
        
        self.text_vector = Text(height=10, width=20)
        self.text_vector.grid(row=3, column=3)
        self.text_vector.insert(END,str(vector))
        Label(self,text="Ingrese el elemento para el vector:").grid(row=4, column=3)
        self.entry_element = Entry(width=10)
        self.entry_element.grid(row=5, column=3)
        
        Button(self,text="Agregar",command=self.push).grid(row=6, column=3)
        Button(self,text="Eliminar", command=self.pop).grid(row=7, column=3)
        Button(self,text="Recursiones", command=self.call_recus).grid(row=8, column=3)
        
        self.vector = vector

    def push(self): 
        numero = int(self.entry_element.get())
        if self.spointer < int(self.entry_tam.get()): 
            self.vector[self.spointer] = numero 
            self.spointer += 1
            self.text_vector.delete(1.0, END)
            self.text_vector.insert(END,str(self.vector))
            
            
    def pop(self): 
        if self.spointer > 0: 
            self.vector[self.spointer-1] = 0
            self.spointer -=1
            self.text_vector.delete(1.0, END)
            self.text_vector.insert(END,str(self.vector))
    
    def call_recus(self): 
        
        encabezados = ["Numero", "Invertir", "Sumar Digitos", "Contar Cero", "Primo", "Numero Binario"]
        self.tree = ttk.Treeview(self, height=10,columns= encabezados, show="headings")
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=100)
        self.tree.grid(row=9, column=3)
        
        for i in range(len(self.vector)): 
            elemento = self.vector[i]
            self.tree.insert("",END, values=(elemento, self.invertir(elemento), self.sumi(elemento), self.contc(elemento), 
                                            self.primo(elemento,elemento-1), self.entbin(elemento)))


    def invertir(self,num): 
        if num < 10: 
            return num 
        else: 
            ultimo = num % 10 
            sinultimo = num // 10 
            digitos = math.floor(math.log10(num)) + 1
            elevado = ultimo * 10**(digitos-1)
            return elevado + self.invertir(sinultimo)
    
    def sumi(self, num): 
        if num < 10: 
            return 1
        else: 
            return 1 + self.sumi(num//10)



    def contc(self, num): 
        if num == 0: 
            return 0 
        else: 
            ulti = num % 10 
            sinulti = num // 10 
            if ulti == 0:
                return 1 + self.contc(sinulti)
            else: 
                return self.contc(sinulti)
    
    def primo(self, num, numi): 
        if num == 1: 
            return "No es primo"
        if numi == 1: 
            return "Es primo"
        else: 
            if num % numi == 0: 
                return "Es primo"
            else: 
                return self.primo(num, numi-1)
    
    def entbin(self, num): 
        if num == 0: 
            return ""
        else: 
            ulti = num %2
            sinulti = num // 2
            return str(self.entbin(sinulti)) + str(ulti)
        
    
app().mainloop()