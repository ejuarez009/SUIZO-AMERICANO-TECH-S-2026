from tkinter import*; from tkinter import messagebox as mb; from tkinter import ttk
import math

class app(Tk): 
    def __init__(self): 
        super().__init__()
        self.title("Laboratorio de Practica #2")
        
        Label(text="Ingrese el tamaño del vector").grid(row=0, column=0, padx=30)
        self.entry_tam = Entry(self)
        self.entry_tam.grid(row=1, column=0, padx=30)
        
        Button(text="Crear Vector", command=self.crear).grid(row=2, column=0, padx=30)
        
        self.spointer = 0
        
    def crear(self): 
        try:
            tamaño = int(self.entry_tam.get())
        except ValueError: 
            mb.showerror("Error", "Ingrese un tamaño valido")
            
        self.vector = [0] * tamaño
        Label(text="El vector creado es:")
        self.text_box = Text(width=30, height=10, padx=30)
        self.text_box.grid(row=4, column=0, padx=30)
        self.text_box.insert(END, str(self.vector))
        
        Label(text="Ingrese los numeros para el vector").grid(row=5, column=0, padx=30)
        self.entry_num = Entry(self)
        self.entry_num.grid(row=6, column=0, padx=30)
        
        Button(text="Agregar", command=self.push).grid(row=7, column=0, padx=30)
        Button(text="Eliminar", command=self.pop).grid(row=8, column=0, padx=30)
        Button(text="Recursiones", command=self.call_recus).grid(row=9, column=0, padx=30)
        

    def push(self): 
        try: 
            numero = int(self.entry_num.get())
        except ValueError: 
            mb.showerror("Error", "Ingrese un numer valido")
        if self.spointer < int(self.entry_tam.get()): 
            self.vector[self.spointer] = numero 
            self.spointer +=1 
            self.text_box.delete(1.0, END)
            self.text_box.insert(END,str(self.vector))
            self.entry_num.delete(0,END)
        else: 
            mb.showinfo("Atencion", "El vector ya esta vacio")
    
    def pop(self): 
        if self.spointer > 0: 
            self.vector[self.spointer-1] = 0
            self.spointer -= 1
            self.text_box.delete(1.0, END)
            self.text_box.insert(END,str(self.vector))
        else: 
            mb.showinfo("Atencion", "El vector ya esta vacio")
    def call_recus(self): 
        
        
        encabezados = ["Numero", "Invertir", "Sumar Digitos", "Contar Cero", "Primo", "Numero Binario"]
        self.tree = ttk.Treeview(self, height=20,columns=encabezados, show='headings')
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=10, column=0, padx=30)
    
        for i in range(len(self.vector)): 
            elemento = self.vector[i]
            self.tree.insert("",END, values=(elemento, self.invertir(elemento), self.sumidigit(elemento), self.contarc(elemento), 
                                            self.primo(elemento, elemento-1), self.entbin(elemento)))
        
    
    def invertir(self, num): 
        if num < 10: 
            return num
        else: 
            ulti = num % 10 
            sinulti = num // 10 
            digito = math.floor(math.log10(num))+1
            elevado = ulti * 10**(digito-1)
            return elevado + self.invertir(sinulti)
    
    def sumidigit(self, num): 
        if num < 10: 
            return num
        else: 
            ulti = num % 10 
            sinulti = num // 10 
            return ulti + self.sumidigit(sinulti)
    
    def contarc(self,num): 
        if num == 0: 
            return 0 
        else: 
            ulti = num % 10 
            sinulti = num // 10 
            if ulti == 0: 
                return 1 + self.contarc(sinulti)
            else: 
                return self.contarc(sinulti)
    def primo(self, num, numi): 
        if num == 1: 
            return "No es primo"
        if numi == 1: 
            return "Es primo"
        else: 
            if num % numi == 0: 
                return "No es primo"
            else: 
                return self.primo(num, numi-1)
            
    def entbin(self, num): 
        if num == 0: 
            return ""
        else: 
            ulti = num % 2 
            sinulti = num // 2
            return str(self.entbin(sinulti)) + str(ulti)
    
app().mainloop()