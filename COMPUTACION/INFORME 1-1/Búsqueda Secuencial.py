#=========================================================DCOUMENTACION INTERNA====================================================================================
# -- Objetivo: Crear un vector, encontrar su valor maximo, minimo,, cuantas veces se repite cada uno y el promedio.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: Generar un vector de tamaño n ingresado por el usuario, con valores aleatorios entre 1 y 20, luego encontrar el valor maximo y minimo del vector, cuantas veces se repite cada uno y el promedio de los valores del vector.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter y modulo Random 
# -- Procesos: Mediantes bucles for se recorre el vector para encontrar el valor maximo y minimo, y para calcular el promedio.
# -- Historia: Fecha de creacion 19/01/2026 Fecha de modificacion: 23/0/2026
# -- Ajustes pendientes: Ninguno 
# ==================================================================================================================================================================



from tkinter import Entry, Label, Tk, Button, messagebox as mb
from random import randint
class Vector(Tk):
    def __init__(self): 
        super().__init__()
        
        self.title("RECONEXION DE VECTORES - ELMER JUAREZ_C5A")
        self.geometry("500x200")
        self.title("ELMER JUAREZ - BUSQUEDA SECUENCIAL")
        
        self.label_size = Label(text="INGRESE EL TAMAÑO DEL VECTOR:").pack()
        self.entry_size = Entry(width=10)
        self.entry_size.pack()
        
        self.label_vex = Label(text="--vector--", foreground="light gray")
        self.label_vex.pack()
        self.label_max = Label(text="--valor maximo--", foreground="light gray")
        self.label_max.pack()    
        self.label_min = Label(text="--valor minimo--", foreground="light gray")
        self.label_min.pack()   
        self.label_prom = Label(text="--promedio--", foreground="light gray")
        self.label_prom.pack()  
        
        self.button_generate = Button(text="GENERAR Y MANIPULAR VECTOR", command=self.generar_vex).pack()
        self.button_max_min = Button(text="MAXIMO Y MINIMO", command=self.max_min).pack()
        self.button_prom = Button(text="PROMEDIO", command=self.promedio).pack()

    def generar_vex(self): 
        size = int(self.entry_size.get())
        
        if size <=0 : 
            mb.showwarning("ERROR", "Solo puede ingresar números enteros positivos")
        
        vector = [0] * size 
        for i in range(size): 
            vector[i] = randint(1, 20)
            
        self.label_vex.config(text=f"VECTOR: {vector}", foreground="black", wraplength=400, justify="left")
        
        #REDIMENSIONA LA VENTANA DEPENDIENDO DEL TAMAÑO DEL VECTOR
        width = self.label_vex.winfo_reqwidth() 
        height = self.label_vex.winfo_reqheight()
        self.geometry(f"{width+150}x{height+150}")
        
        self.vector = vector 
        
    def max_min(self): 
        maxi = 1  
        mini = 20 
        cont_max = 0
        cont_min = 0 

        vector = self.vector
        
        for i in range(len(vector)):    
            if maxi < vector[i]: 
                maxi = vector[i] 
                cont_max = 0
            if mini > vector[i]: 
                mini = vector[i]
                cont_min = 0
        
        for j in range(len(vector)):
            if maxi == vector[j]: 
                cont_max += 1
            if mini == vector[j]: 
                cont_min += 1
            
        if cont_max > 1: 
            self.label_max.config(text=f"El valor máximo es: {maxi} y se repite {cont_max} veces", foreground="black")   
            self.label_min.config(text=f"El valor mínimo es: {mini} y se repite {cont_min} veces", foreground="black") 
        else: 
            self.label_max.config(text=f"El valor máximo es: {maxi} y se repite {cont_max} vez", foreground="black") 
            self.label_min.config(text=f"El valor mínimo es: {mini} y se repite {cont_min} vez", foreground="black") 
        
    def promedio(self):    
        vector = self.vector
        promedio = 0 
        for i in range(len(vector)): 
            promedio += vector[i]
            
        promedio = promedio / len(vector)
        
        self.label_prom.config(text=f"El promedio es: {promedio}", foreground="black")

        
Vector().mainloop()