#=========================================================DOCUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Implementar y comparar distintos algoritmos de ordenamiento (Burbuja, Inserción, Conteo y Selección) sobre un vector generado aleatoriamente.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descripción: El programa permite al usuario ingresar el tamaño de un vector, generarlo con números aleatorios de 3 dígitos y aplicar distintos algoritmos de ordenamiento.
#                  Muestra los resultados ordenados, el tiempo de ejecución, el número de comparaciones y movimientos en una interfaz gráfica construida con Tkinter.
# -- Lenguaje: Python 3
# -- Recursos: Librería Tkinter para la interfaz gráfica, módulo random para generación de números aleatorios y módulo time para medición de tiempos de ejecución.
# -- Procesos: 
#       1. El usuario ingresa el tamaño del vector.
#       2. Se genera un vector de números aleatorios de 3 dígitos.
#       3. El usuario puede ordenar el vector con cualquiera de los cuatro algoritmos disponibles.
#       4. Cada algoritmo muestra el vector ordenado en un Text box, junto con el número de comparaciones, movimientos y tiempo de ejecución.
# -- Historia: 
#       Fecha de creación: 13/02/2026
#       Fecha de modificación: 13/02/2026
# -- Ajustes pendientes: Mejorar la visualización de vectores grandes, agregar más algoritmos de ordenamiento.
# ======================================================================================================================================================================================================================================

from tkinter import *
from tkinter import messagebox as mb
from random import randint
import time

class Sorts(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1020x450")
        self.title("SORTS - ELMER JUAREZ/C5A")

        # ===================== ENTRADA =====================
        Label(self, text="Ingrese el tamaño del vector:").place(x=10, y=10)
        self.entry_tam = Entry(width=20)
        self.entry_tam.place(x=180, y=10)

        self.btn_generar = Button(self, text="Generar Vector", command=self.generate_vector)
        self.btn_generar.place(x=350, y=7)

        # ===================== VECTOR =====================
        self.label_vector = Label(self, text="Vector generado: []", font=("Arial", 10))
        self.label_vector.place(x=10, y=40)

        # ===================== TÍTULOS =====================
        self.label_burbuja = Label(self, text="Ordenamiento por Burbuja", font=("Arial", 11, "bold"))
        self.label_burbuja.place(x=10, y=70)

        self.label_insercion = Label(self, text="Ordenamiento por Inserción", font=("Arial", 11, "bold"))
        self.label_insercion.place(x=260, y=70)

        self.label_conteo = Label(self, text="Ordenamiento por Conteo", font=("Arial", 11, "bold"))
        self.label_conteo.place(x=510, y=70)

        self.label_seleccion = Label(self, text="Ordenamiento por Selección", font=("Arial", 11, "bold"))
        self.label_seleccion.place(x=760, y=70)

        # ===================== TEXTBOX =====================
        self.text_box1 = Text(width=30, height=10)
        self.text_box1.place(x=10, y=200)

        self.text_box2 = Text(width=30, height=10)
        self.text_box2.place(x=260, y=200)

        self.text_box3 = Text(width=30, height=10)
        self.text_box3.place(x=510, y=200)

        self.text_box4 = Text(width=30, height=10)
        self.text_box4.place(x=760, y=200)

        # ===================== ETIQUETAS =====================
        # Burbuja
        self.cont_comp1 = Label(self, text="")
        self.cont_comp1.place(x=10, y=110)
        self.cont_mov1 = Label(self, text="")
        self.cont_mov1.place(x=10, y=130)
        self.tiempo1 = Label(self, text="")
        self.tiempo1.place(x=10, y=150)

        # Inserción
        self.cont_comp2 = Label(self, text="")
        self.cont_comp2.place(x=260, y=110)
        self.cont_mov2 = Label(self, text="")
        self.cont_mov2.place(x=260, y=130)
        self.tiempo2 = Label(self, text="")
        self.tiempo2.place(x=260, y=150)

        # Conteo
        self.cont_comp3 = Label(self, text="")
        self.cont_comp3.place(x=510, y=110)
        self.cont_mov3 = Label(self, text="")
        self.cont_mov3.place(x=510, y=130)
        self.tiempo3 = Label(self, text="")
        self.tiempo3.place(x=510, y=150)

        # Selección
        self.text_box_comp4 = Label(self, text="")
        self.text_box_comp4.place(x=760, y=110)
        self.text_mov4 = Label(self, text="")
        self.text_mov4.place(x=760, y=130)
        self.tiempo4 = Label(self, text="")
        self.tiempo4.place(x=760, y=150)

        # ===================== BOTONES =====================
        self.btn_burbuja = Button(self, text="Ordenar Burbuja", command=self.sort_burble)
        self.btn_burbuja.place(x=10, y=170)

        self.btn_insercion = Button(self, text="Ordenar Inserción", command=self.sort_insercion)
        self.btn_insercion.place(x=260, y=170)

        self.btn_conteo = Button(self, text="Ordenar Conteo", command=self.sort_conteo)
        self.btn_conteo.place(x=510, y=170)

        self.btn_seleccion = Button(self, text="Ordenar Selección", command=self.sort_seleccion)
        self.btn_seleccion.place(x=760, y=170)

    # ===================== GENERAR VECTOR =====================
    def generate_vector(self):
        try:
            size = int(self.entry_tam.get())
            vector = [randint(100, 999) for _ in range(size)]
            self.vector_orig = vector
            self.label_vector.config(text=f"Vector generado: {vector}")
        except ValueError:
            mb.showwarning("CUIDADO", "Ingresa un número válido")

    # ===================== ORDENAMIENTOS =====================
    def sort_burble(self):
        self.text_box1.delete("1.0", END)
        vector = self.vector_orig.copy()
        cont_comp = cont_mov = 0
        inicio = time.time()
        for i in range(len(vector)):
            for j in range(len(vector)-i-1):
                cont_mov += 1
                if vector[j] > vector[j+1]:
                    vector[j], vector[j+1] = vector[j+1], vector[j]
                    cont_comp += 1
        tiempo = time.time() - inicio
        vector_str = str(vector)
        self.cont_comp1.config(text=f"Comparaciones: {cont_comp}")
        self.cont_mov1.config(text=f"Movimientos: {cont_mov}")
        self.tiempo1.config(text=f"Tiempo: {tiempo:.6f}s")
        self.text_box1.insert("1.0", vector_str)

    def sort_insercion(self):
        self.text_box2.delete("1.0", END)
        vector = self.vector_orig.copy()
        cont_comp = cont_mov = 0
        inicio = time.time()
        for i in range(1, len(vector)):
            j = i
            cont_mov += 1
            while j > 0 and vector[j-1] > vector[j]:
                vector[j], vector[j-1] = vector[j-1], vector[j]
                cont_comp += 1
                j -= 1
        tiempo = time.time() - inicio
        vector_str = str(vector)
        self.cont_comp2.config(text=f"Comparaciones: {cont_comp}")
        self.cont_mov2.config(text=f"Movimientos: {cont_mov}")
        self.tiempo2.config(text=f"Tiempo: {tiempo:.6f}s")
        self.text_box2.insert("1.0", vector_str)

    def sort_conteo(self):
        self.text_box3.delete("1.0", END)
        vector = self.vector_orig.copy()
        n = len(vector)
        new_vector = [0]*n
        cont_comp = cont_mov = 0
        inicio = time.time()
        for i in range(n):
            cont = 0
            for j in range(n):
                cont_mov += 1
                if vector[j] < vector[i] or (vector[j] == vector[i] and j>i):
                    cont += 1
                    cont_comp += 1
            new_vector[cont] = vector[i]
        tiempo = time.time() - inicio
        vector_str = str(new_vector)
        self.cont_comp3.config(text=f"Comparaciones: {cont_comp}")
        self.cont_mov3.config(text=f"Movimientos: {cont_mov}")
        self.tiempo3.config(text=f"Tiempo: {tiempo:.6f}s")
        self.text_box3.insert("1.0", vector_str)

    def sort_seleccion(self):
        self.text_box4.delete("1.0", END)
        vector = self.vector_orig.copy()
        cont_comp = cont_mov = 0
        inicio = time.time()
        n = len(vector)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                cont_mov += 1
                if vector[j] < vector[min_idx]:
                    min_idx = j
                    cont_comp += 1
            vector[i], vector[min_idx] = vector[min_idx], vector[i]
        
        vector_str = str(vector)
        tiempo = time.time() - inicio
        self.text_box_comp4.config(text=f"Comparaciones: {cont_comp}")
        self.text_mov4.config(text=f"Movimientos: {cont_mov}")
        self.tiempo4.config(text=f"Tiempo: {tiempo:.6f}s")
        self.text_box4.insert("1.0", vector_str)

Sorts().mainloop()