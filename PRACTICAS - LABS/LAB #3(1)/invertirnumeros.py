from tkinter import* 
from tkinter import messagebox as mb 
from tkinter import ttk

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.title("Autor: Elmer Juarez")
        self.spointer = 0

        Label(text="Ingrese un número").grid(row=0, column=0, padx=20)
        self.entry_tam = Entry()
        self.entry_tam.grid(row=1, column=0, padx=20)
        Button(text="Crear vector", command=self.crear).grid(row=2, column=0, padx=20)
        
        
    
    def crear(self): 
        try: 
            tamaño = int(self.entry_tam.get())
        except ValueError: 
            mb.showinfo("Atencion", "Ingrese un tamaño válido")

        vector = [0]*tamaño
        self.vector = vector 
        
        self.textbox = Text(width=50, height=10)
        self.textbox.grid(row=3, column=0, padx=20)
        self.textbox.insert(1.0, str(vector))
        self.entry_num = Entry()
        self.entry_num.grid(row=4, column=0, padx=20)
        Button(text="Ingresar número", command=self.push).grid(row=5, column=0, padx=20)
        Button(text="Sacar Números", command=self.pop).grid(row=6, column=0, padx=20)
        Button(text="Hacer Recursiones", command=self.call_recus).grid(row=7, column=0, padx=20)
        
    
    def push(self): 
        try: 
            elemento = int(self.entry_num.get())
        except ValueError: 
            mb.showinfo("Atencion", "Ingrese un número válido")
        vect = self.vector
        if self.spointer < 10: 
            vect[self.spointer] = elemento
            self.spointer += 1
            self.textbox.delete(1.0, END)
            self.textbox.insert(1.0, str(vect))
        else: 
            mb.showwarning("Cuidado", "Ya se lleno el vector")
    
    def pop(self): 
        vect = self.vector
        if self.spointer > 0: 
            vect[self.spointer-1] = 0
            self.spointer -= 1
            self.textbox.delete(1.0, END)
            self.textbox.insert(1.0, str(f"{vect}"))
        else: 
            mb.showwarning("Atencion", "Ya no hay elementos a sacar")
            
    
    def call_recus(self): 
        encabezados = []
        vector2 = []
        for j in self.vector: 
            if j != 0: 
                vector2.append(j)
                
        for numero in vector2: 
            encabezados.append(numero)
        
        self.tree = ttk.Treeview(height=5, columns=encabezados, show='headings')
        for encabezado in encabezados: 
            self.tree.column(encabezado, width=100, anchor='center')
        self.tree.grid(row=8, column=0, padx=20, pady=20)
        
        listanum = []
        invertidos = []
        hexadecimales = []
        binarios = []
        for i in range(len(vector2)): 
            num = vector2[i]
            listanum.append(num)
            
            numt = self.invertir(num)
            invertidos.append(numt)
            
            hexa = self.hexadecimal(num)
            hexadecimales.append(hexa)
            
            bins = self.bina(num)
            binarios.append(bins)
        
        self.tree.insert("", END, values=tuple(listanum))
        self.tree.insert("", END, values=tuple(invertidos))
        self.tree.insert("", END, values=tuple(hexadecimales))
        self.tree.insert("", END, values=tuple(binarios))
        
    def invertir(self, num): 
        if num < 10: 
            return num
        else: 
            ult = num % 10 
            sinult = num // 10 
            elevado = ult * 10**(len(str(sinult)))    
            return elevado + self.invertir(sinult)
    
    def hexadecimal(self, num): 
        if int(num) == 0: 
            return "" 
        else: 
            residuo = int(num) % 16 
            resto = int(num) // 16 
            return self.hexadecimal(str(resto)) + "0123456789ABCDEF"[residuo]
    
    def bina(self, num): 
        if num == 0: 
            return ""
        else: 
            residuo = num % 2
            resto = num // 2
            return self.bina(resto) + str(residuo)

app().mainloop()