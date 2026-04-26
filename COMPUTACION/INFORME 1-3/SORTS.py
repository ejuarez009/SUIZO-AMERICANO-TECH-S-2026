#=========================================================DOCUMENTACION INTERNA=================================================================================================
# -- Objetivo: Implementar y comparar distintos algoritmos de ordenamiento (Burbuja, Inserción, Conteo, Selección y Quicksort) sobre un vector generado aleatoriamente.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descripción: El programa permite al usuario ingresar el tamaño de un vector, generarlo con números aleatorios de 3 dígitos y aplicar distintos algoritmos de ordenamiento.
#                  Muestra los resultados ordenados, el tiempo de ejecución, el número de comparaciones y movimientos en una interfaz gráfica construida con Tkinter.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter con sus modulas TTk, messagebox random.
# -- Procesos: 
#       1. El usuario ingresa el tamaño del vector.
#       2. Se genera un vector de números aleatorios de 3 dígitos.
#       3. El usuario puede ordenar el vector con cualquiera de los cuatro algoritmos disponibles.
#       4. Cada algoritmo muestra el vector ordenado en un Text box, junto con el número de comparaciones, movimientos y tiempo de ejecución.
# -- Historia: 
#       Fecha de creación: 13/02/2026
#       Fecha de modificación: 12/04/2026
# -- Ajustes pendientes: Mejorar la visualización de vectores grandes, agregar más algoritmos de ordenamiento.
# -- Cambios Realizados: Complementacion con el algoritmo de quikcsort, ademáas de que se agrego una mejor GUI
# ======================================================================================================================================================================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint
import time

class Sorts(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("770x950")
        self.config(bg="deep skyblue")
        self.title("Sorts de Ordenamiento - Elmer Juarez C5")
        
        frame_widgets = Frame(self, width=400, height=200, bg="deep skyblue")
        frame_widgets.grid(row=0, column=0, columnspan=2)
        
        # ============================= WIDGETS =============================
        Label(frame_widgets, text="Ingrese el tamaño del vector:", bg="deep skyblue",
            font=("Arial", 10, "bold")).grid(row=0, column=0, pady=5)

        self.n = ttk.Spinbox(frame_widgets,from_=1, to=200, width=10)
        self.n.grid(row=0, column=1)
        
        self.vc = Label(frame_widgets, text="", bg="deep skyblue")
        self.vc.grid(row=1, column=0, columnspan=6)
        
        Button(frame_widgets, text="Crear Vector", command=self.crear,
            bg="light cyan", width=15).grid(row=0, column=2, padx=10)
        
        
        frame_buttons = Frame(self, width=400, height=200, bg="deep skyblue")
        frame_buttons.grid(row=1, column=0, columnspan=2)

        Button(frame_buttons, text="Ordenar por Burbuja", command=self.burbuja,
            bg="pink", width=20, height=2).grid(row=1, column=0, pady=10)

        Button(frame_buttons,text="Ordenar por Inserción", command=self.insercion,
            bg="lightblue", width=20, height=2).grid(row=1, column=1)

        Button(frame_buttons,text="Ordenar por Conteo", command=self.conteo,
            bg="lightgray", width=20, height=2).grid(row=1, column=2)
    
        Button(frame_buttons,text="Ordenar por Seleccion", command=self.seleccion,
            bg="lightgreen", width=20, height=2).grid(row=1, column=3)
        
        Button(frame_buttons,text="Ordenar por Quicksort", command=self.call_quickly,
            bg="lightyellow", width=20, height=2).grid(row=1, column=4)

    # ============================= CREAR VECTOR =============================
    def crear(self):
        try:
            n = int(self.n.get())
            self.vector = [randint(100, 999) for _ in range(n)]
            self.vc.config(text=f"Vector Original: {self.vector}",
                        font=("Arial", 10, "bold"), wraplength="700", bg="skyblue")
        except ValueError:
            mb.showerror("ERROR", "Ingrese un tamaño válido")

    # ============================= BURBUJA =============================
    def burbuja(self):
        try:
            v = self.vector.copy()
            com = 0
            cam = 0
            inicio = time.time()

            for i in range(len(v)):
                for j in range(len(v) - i - 1):
                    com += 1
                    if v[j] > v[j + 1]:
                        v[j], v[j + 1] = v[j + 1], v[j]
                        cam += 1

            fin = time.time()
            t = fin - inicio
            
            frame_burbuja = Frame(self, width=500, height=200,  bg="pink")
            frame_burbuja.grid(row=2, column=0)
            
            Label(frame_burbuja, text="Ordenamiento por Burbuja", font=("arial",14, "bold") ).grid(row=0, column=0)
            text_box = Text(frame_burbuja, width=40, height=10)
            text_box.grid(row=1, column=0)

            text_box.insert(END,str(v))
            Label(frame_burbuja, text=f"Movimientos: {com} \n Comparaciones: {cam} \n Tiempo: {t:.6f}", bg="pink").grid(row=2, column=0)

        except AttributeError:
            mb.showerror("ERROR", "Primero debe crear el vector")
            return

    # ============================= INSERCIÓN =============================
    def insercion(self):
        
        try:
            v = self.vector.copy()
            com = 0
            cam = 0
            inicio = time.time()

            for i in range(1, len(v)):
                actual = v[i]
                j = i - 1
                while j >= 0 and v[j] > actual:
                    com += 1
                    v[j + 1] = v[j]
                    j -= 1
                    cam += 1
                v[j + 1] = actual

            fin = time.time()
            t = fin - inicio
            
            frame_insercion = Frame(self, width=500, height=200,bg="light blue")
            frame_insercion.grid(row=2, column=1)
            Label(frame_insercion, text="Ordenamiento por Insercion", font=("arial",14, "bold") ).grid(row=0, column=0)
            text_box = Text(frame_insercion, width=40, height=10)
            text_box.grid(row=1, column=0)

            text_box.insert(END,str(v))
            Label(frame_insercion, text=f"Movimientos: {com} \n Comparaciones: {cam} \n Tiempo: {t:.6f}", bg="lightblue").grid(row=2, column=0)

        except AttributeError:
            mb.showerror("ERROR", "Primero debe crear el vector")

    # ============================= CONTEO =============================
    def conteo(self):
        try:
            v = self.vector.copy()
            vd = [0] * len(v)
            com = 0
            inicio = time.time()

            for i in range(len(v)):
                c = 0
                for j in range(len(v)):
                    com += 1
                    if v[j] < v[i] or (v[j] == v[i] and j < i):
                        c += 1
                vd[c] = v[i]

            fin = time.time()
            t = fin - inicio
            
            frame_conteo = Frame(self, width=500, height=200)
            frame_conteo.grid(row=3, column=0, pady=10)
            Label(frame_conteo, text="Ordenamiento por Conteo", font=("arial",14, "bold") ).grid(row=0, column=0)
            text_box = Text(frame_conteo, width=40, height=10)
            text_box.grid(row=1, column=0)

            text_box.insert(END,str(v))
            Label(frame_conteo, text=f"Movimientos: {com} \n Comparaciones: {c} \n Tiempo: {t:.6f}").grid(row=2, column=0)


        except AttributeError:
            mb.showerror("ERROR", "Primero debe crear el vector")
    
    def seleccion(self): 
        try: 
            vector = self.vector.copy()
            
            c = 0  # comparaciones
            com = 0  # movimientos

            inicio = time.time()

            n = len(vector)
            for i in range(n):
                min_index = i
                
                for j in range(i + 1, n):
                    c += 1
                    if vector[j] < vector[min_index]:
                        min_index = j
                
                if min_index != i:
                    vector[i], vector[min_index] = vector[min_index], vector[i]
                    com += 1
            
            fin = time.time()
            t = fin - inicio
            
            frame_seleccion = Frame(self, width=500, height=200, bg="lightgreen")
            frame_seleccion.grid(row=3, column=1, padx=10, pady=20)
            Label(frame_seleccion, text="Ordenamiento por Seleccion", font=("arial",14, "bold") ).grid(row=0, column=0)
            text_box = Text(frame_seleccion, width=40, height=10)
            text_box.grid(row=1, column=0)

            text_box.insert(END,str(vector))
            Label(frame_seleccion, text=f"Movimientos: {com} \n Comparaciones: {c} \n Tiempo: {t:.6f}", bg="light green").grid(row=2, column=0)
            
        except (ValueError, AttributeError):
            mb.showerror("Error", "Cree el vector para realizar el ordenamiento")
    
    
    def call_quickly(self): 
        try: 
            arreglo = self.vector.copy()
            self.comp = 0 
            self.movs = 0
            contador = 0
            
            inicio = time.time()
            vector_ordenado = self.quicksort(arreglo, contador)
            tiempo = time.time() - inicio
            
            frame_quicksort = Frame(self, width=500, height=200, bg="light yellow")
            frame_quicksort.grid(row=4, column=0,pady=10, columnspan=2)
            Label(frame_quicksort, text="Ordenamiento por Quicksort", font=("arial",14, "bold") ).grid(row=0, column=0)
            text_box = Text(frame_quicksort, width=40, height=10)
            text_box.grid(row=1, column=0)

            text_box.insert(END,str(vector_ordenado))
            Label(frame_quicksort, text=f"Movimientos: {self.movs} \n Comparaciones: {self.comp} \n Tiempo: {tiempo:.6f}", bg="light yellow").grid(row=2, column=0)
            
            
        except (ValueError, AttributeError):
            mb.showerror("Error", "Cree el vector para realizar el ordenamiento")
    
    def quicksort(self, vector, contador): 
        if len(vector) <= 1: 
            return vector
        else: 
            pivote = vector[0]
            L1 = []
            L2 = []
            
            for i in vector[1:]:
                self.movs += 1
                contador += 1
                if i < pivote: 
                    self.comp += 1
                    L1.append(i)
                else: 
                    L2.append(i)
                    self.comp+= 1
            
            return self.quicksort(L1,contador) + [ pivote ] + self.quicksort(L2,contador)

Sorts().mainloop()