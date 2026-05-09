from tkinter import END, Entry, Label, Button, messagebox as mb, Text, Tk
from tkinter.ttk import Treeview



class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("500x500")
        self.title("Laboratorio #3 - Elmer Juarez C5A")
        
        Label(text="Ingrese el tamaño del vector").pack()
        self.tam = Entry(self)
        self.tam.pack()
        Button(text="Crear vector", command=self.crear).pack()
        self.vpointer = 0
    
    def crear(self): 
        try: 
            tamaño = int(self.tam.get())
            if tamaño >= 9: 
                mb.showerror("Error", "Solo pueden ser vectores de una longitud de 8")
                return
        except ValueError: 
            mb.showerror("Error", "Ingres un valor válido")
        self.vector = [0] * tamaño
        
        self.label_vector = Label(text=str(self.vector))
        self.label_vector.pack()
        
        self.entry_element = Entry(self)
        self.entry_element.pack()
        Button(text="Insertar número", command=self.push).pack()
        Button(text="Eliminar número", command=self.pop).pack()
        Button(text="Mostrar", command=self.call_sum).pack()
        
    
    def push(self): 
        try: 
            elemento = int(self.entry_element.get())
            if elemento >= 99999: 
                mb.showerror("Error", "No pueden ser números tan grandes")
                return 
        except ValueError: 
            mb.showerror("Error", "Ingrese un valor válido")
            
        if self.vpointer < len(self.vector): 
            self.vector[self.vpointer] = elemento
            self.vpointer += 1
            self.label_vector['text'] = f"{self.vector}"
            self.entry_element.delete(0,END)
        else: 
            mb.showwarning("Cuidado", "Se ha alcanzado el limite del vector")
            return
    
    def pop(self): 
        if self.vpointer > 0: 
            self.vector[self.vpointer-1] = 0
            self.vpointer-=1
            self.label_vector['text'] = f"{self.vector}"
        else:
            mb.showinfo("Atencion", "El vector ya esta vacio")
            return
    
    
    def call_sum(self): 
        columnas = []
        for i in range(len(self.vector)): 
            columnas.append(i)
        
        self.tree = Treeview(columns=columnas,show='headings')
        self.tree.pack()
        
        for columna in columnas: 
            self.tree.heading(columna,text=f"Número {columna+1}")
        
        self.tree.insert("", "end", values=tuple(self.vector))
        
        conts = []
        for i in range(len(self.vector)): 
            num = self.vector[i]
            contd = self.contdigit(num)
            conts.append(contd)
        self.tree.insert("", "end", values=tuple(conts))
    
    def contdigit(self, num): 
        if num < 10: 
            return 1
        else: 
            return 1 + self.contdigit(num//10)

app().mainloop()