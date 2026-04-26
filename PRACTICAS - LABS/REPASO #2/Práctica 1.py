from tkinter import*; from random import randint

class app(Tk): 
    def __init__(self): 
        super().__init__()

        self.geometry("300x300")

        Label(text="Ingrese el número a buscar").pack()
        self.entry_num = Entry()
        self.entry_num.pack()
        Button(text="Buscar número", command=self.revisar).pack()
        self.label_result = Label(text="")
        self.label_result.pack()

    def crear(self): 
        vector = [None]*10 
        for i in range(10): 
            vector[i] = randint(1,3)
        print(vector)
        return vector

    def buscar(self, vector, elemento): 
        pos = 0 
        while pos < len(vector): 
            if vector[pos] == elemento: 
                return pos 
            pos+=1 
        return -1 

    def revisar(self): 
        try: 
            numero = int(self.entry_num.get())
        except ValueError: 
            return 
        posicion = self.buscar(self.crear(), numero)
        print(posicion)

        if posicion > 0: 
            self.label_result['text'] = f"El numero {numero}, se encontro en la posicion {posicion}"
        else: 
            self.label_result['text'] = f"No se encontro el número"

#app().mainloop()


#* Cuantas veces se repitio, elementos pares, etc. 


vector = [2,4,1,7,4,5,6]

def quicksort(vector, s=""):
    print(s, vector)
    if len(vector) <=1: 
        return vector
    else: 
        l1 = []
        l2 = []
        elemento = vector[0]
        for evector in vector[1:]: 
            if elemento > evector: 
                l1.append(evector)
            else: 
                l2.append(evector)
        t = quicksort(l1) + [elemento] + quicksort(l2)
        print(s, "Devuelve",t)
        return t

print(quicksort(vector))


numero1 = int(input("Ingrese el numero 1:"))
numero2 = int(input("Ingrese el numero 2:"))
def numeros_amigos(num1, num2): 
    acu1=0
    acu2 = 0
    for i in range(1,num1): 
        if num1 % i == 0:
            acu1 += i 
    for i in range(1,num2): 
        if num2 % i == 0: 
            acu2 += i
    
    if acu1 == num2 and acu2 == num1: 
        return "Si son numeros amigos"
    else: 
        return "No son numeros amigos"

print(numeros_amigos(numero1, numero2))