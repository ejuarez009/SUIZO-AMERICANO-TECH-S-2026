#=========================================================DCOUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Implementar el algoritmo de búsqueda binaria para encontrar un número ingresado por el usuario dentro de un vector ordenado de tamaño n generado aleatoriamente.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: El programa genera un vector ordenado de tamaño n con números aleatorios consecutivos y utiliza el algoritmo de búsqueda binaria para determinar si un número ingresado por el usuario está presente en el vector.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter y modulo Random 
# -- Procesos: Mediante ciclos se genera el vector ordenado de numeros aletorios consecutivos, y se va fragmentando el vector en mitades para buscar el numero ingresado por el usuario.
# -- Historia: Fecha de creacion 23/01/2026 Fecha de modificacion: 24/0/2026
# -- Ajustes pendientes: Ninguno 
# ======================================================================================================================================================================================================================================
from tkinter import*; from tkinter import messagebox as mb
from random import randint

class binary_search(Tk):
    def __init__(self, className="Búsqueda Binaria - Elmer Juarez C5"):
        super().__init__(className=className)
        self.geometry("450x300")
        self.config(bg="beige")

        # =============================WIDGETS DE LA INTERFAZ=======================
        Label(self, text="Ingrese el tamaño del vector:", font=("Arial", 10, "bold")).grid(row=0, column=0)
        Label(self, text="Ingrese el número a buscar:", font=("Arial", 10, "bold")).grid(row=1, column=0)
        self.entry_tam = Entry(width=10)
        self.entry_tam.grid(row=0, column=1)
        self.entry_user_num = Entry(width=10)
        self.entry_user_num.grid(row=1, column=1)

        #   ==========================OUTPUTS (LABELS)========================
        self.label_vector = Label(text="")
        self.label_vector.grid(row=2, column=0, columnspan=4)
        self.label_num = Label(text="")
        self.label_num.grid(row=3, column=0, columnspan=4)


        self.button_search = Button(self, text="Buscar", command=self.number_search, width=15, height=2, bg="pink", font=("Arial", 10, "bold"))
        self.button_search.grid(row=0, column=7, rowspan=2, padx=10)

    def number_search(self):
        try:
            num_lost = int(self.entry_user_num.get())
            size_vector = int(self.entry_tam.get())

            vector = [0] * size_vector
            for i in range(size_vector):
                element = randint(1, size_vector)
                vector[i] = element
                if vector[i-1] > vector[i]:
                    vector[i] = vector[i-1] + element
                

            find_num = False
            lim_inf = 0
            lim_sup = size_vector - 1

            while not find_num and lim_inf <= lim_sup:
                half = (lim_inf + lim_sup) // 2
                if num_lost == vector[half]:
                    find_num = True
                    break
                else:
                    if vector[half] > num_lost:
                        lim_sup = half - 1
                    else:
                        lim_inf = half + 1

            self.label_vector.config(text=f"VECTOR: {vector}", wraplength=400, font=("Arial", 10, "bold"))

            if find_num == True:
                self.label_num.config(text=f"Si se encontro el número {num_lost} en el vector", font=("Arial", 10, "bold"))
            else:
                self.label_num.config(text=f"No se econtró el número {num_lost} en el vector", font=("Arial", 10, "bold"))

        except ValueError:
            mb.showerror("ERROR", "Debe ingresar un número válido")

binary_search().mainloop()