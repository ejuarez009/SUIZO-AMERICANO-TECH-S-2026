from tkinter import*; from tkinter import messagebox as mb 
from random import randint

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("400x600")
        self.title("Evaluacion Final Compu")
        
        Label(text="Ingrese el tamaño para el vector").pack()
        self.entry_tam = Entry(self)
        self.entry_tam.pack()
        Label(text="El vector es:").pack()
        self.text_vector = Text(width=30, height=10)
        self.text_vector.pack()
        Button(text="Crear Vector", command=self.vector).pack()
        Label(text="Vector Ordenado:").pack()
        
        self.text_ordenado = Text(width=30, height=10)
        self.text_ordenado.pack()
        Button(text="Vector Ordenado", command=self.ordenado).pack()

        Label(text="Ingrese el número a buscar").pack()
        self.entry_bnum = Entry(self)
        self.entry_bnum.pack()
        self.label_num = Label(text="--numero--")
        self.label_num.pack()
        Button(text="Buscar Número", command=self.busc).pack()
        
    def vector(self): 
        try: 
            tamaño = int(self.entry_tam.get())
        except ValueError: 
            mb.showerror("Error", "Ingresa datos validos")
            
        vector = [0] * tamaño
        for i in range(tamaño): 
            vector[i] = randint(1,20)

        self.text_vector.insert(END,str(vector))
        self.vector = vector

    def ordenado(self):
        try: 
            vector2 = self.vector
        except ValueError:
            mb.showerror("Error", "Vector no creado")
            return 
        
        vec_orden = self.quick(vector2)
        self.text_ordenado.insert(END,str(vec_orden))
        self.vec_ordenado = vec_orden
    
    def quick(self, vector): 
        if len(vector) <=1: 
            return vector 
        else: 
            pos = len(vector)//2
            pivote = vector[pos]
            menores = []
            mayores = []
            for i in range(pos): 
                if pivote < vector[i]: 
                    mayores.append(vector[i])
                else: 
                    menores.append(vector[i])
            for i in range(pos+1, len(vector)): 
                if pivote < vector[i]: 
                    mayores.append(vector[i])
                else: 
                    menores.append(vector[i])
            return self.quick(menores) + [pivote] + self.quick(mayores)
    
    def busc(self): 
        try: 
            bvector = self.vec_ordenado
            bnum = int(self.entry_bnum.get())
        except ValueError: 
            mb.showerror("Error", "Ingrese datos validos")
            
        li = 0
        ls = len(bvector)-1
        encontrado = self.bbinaria(bvector, bnum,li,ls)
        self.label_num.config(text=encontrado)

    def bbinaria(self,vector, num,li,ls): 
        if li>ls: 
            return "Número no encontrado"
        else: 
            mitad = (ls+li)//2 
            if vector[mitad] == num: 
                return f"Número encontrado, posicion:{mitad+1}"
            else:
                if vector[mitad]>num:
                    ls = mitad - 1
                    return self.bbinaria(vector, num, li, ls)
                else: 
                    li = mitad + 1
                    return self.bbinaria(vector, num, li, ls)
app().mainloop()