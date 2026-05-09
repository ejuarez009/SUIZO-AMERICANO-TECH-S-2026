from tkinter import filedialog as fd, ttk; from tkinter import*
import re

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("800x600")
        self.title("Autor: Elmer Juarez")
        
        self.label_digitos = Label(text="--no.digitos--")
        self.label_digitos.pack()
        self.label_numeros = Label(text="--no.digitos--")
        self.label_numeros.pack()
        self.label_lineas = Label(text="--no.digitos--")
        self.label_lineas.pack()
        
        encabezados = ["No.", "Numero extraído", "Collatz"]
        self.tree = ttk.Treeview(height=20, columns=encabezados, show='headings')
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=200, anchor='center')
        self.tree.pack()
        
        Button(text="Analizar", command=self.analizar).pack()
        self.listac = []
    
    def analizar(self): 
        self.ruta = fd.askopenfilename()
        with open(self.ruta, 'r', encoding="utf-8-sig") as archivo: 
            contenido = archivo.read()
            lineas = contenido.splitlines()
            #contadores: 
            cn = 0 
            self.cd = 0 
            cl = 0
            for linea in lineas: 
                cl += 1
                numeros = re.findall(r"\d+", linea)
                for numero in numeros: 
                    self.listac = []
                    self.contardigitos(int(numero))
                    cn += 1
                    self.tree.insert("", END, values=(str(cn),numero, self.collatz(int(numero))))
            
            self.label_digitos.config(text=f"Cantidad de digitos{self.cd}")
            self.label_lineas.config(text=f"Contar Lineas:{cl}")
            self.label_numeros.config(text=f"Contar numeros:{cn}")
    
    def collatz(self, num): 
        self.listac.append(num)
        if num == 1: 
            return self.listac 
        else: 
            if num %2 == 0: 
                return self.collatz(num//2)
            else: 
                return self.collatz((num*3)+1)
    
    def contardigitos(self, num): 
        self.cd +=1
        if num < 10: 
            return 1
        else: 
            sinulti = num // 10
            return 1 + self.contardigitos(sinulti)


app().mainloop()
