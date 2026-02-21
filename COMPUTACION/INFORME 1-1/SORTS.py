#=========================================================DOCUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Implementar los algoritmos de ordenamiento Burbuja, Inserción y Conteo para ordenar un vector de tamaño n generado aleatoriamente.
# -- Autor: [Tu Nombre]
# -- Descripción: El programa genera un vector de tamaño n con números aleatorios de 3 cifras y permite ordenarlo utilizando tres algoritmos distintos.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter, ttk, messagebox y modulos Random y Time
# -- Procesos: Se genera el vector mediante un ciclo y posteriormente se aplican los algoritmos de ordenamiento midiendo comparaciones, cambios y tiempo de ejecución.
# -- Historia: Fecha de creación 13/02/2026
# -- Ajustes pendientes: Ninguno
# ======================================================================================================================================================================================================================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint
import time


class Sorts(Tk):

    def __init__(self, className="Algoritmos de Ordenamiento"):
        super().__init__(className=className)
        self.geometry("600x500")
        self.config(bg="skyblue")

        # ============================= WIDGETS =============================
        Label(self, text="Ingrese el tamaño del vector:", bg="skyblue",
            font=("Arial", 10, "bold")).grid(row=0, column=0, pady=5)

        self.n = ttk.Spinbox(self, from_=1, to=200, width=10)
        self.n.grid(row=0, column=1)

        Button(self, text="Crear Vector", command=self.crear,
            bg="lightgreen", width=15).grid(row=0, column=2, padx=10)

        Button(self, text="Ordenar por Burbuja", command=self.burbuja,
            bg="pink", width=20).grid(row=1, column=0, pady=10)

        Button(self, text="Ordenar por Inserción", command=self.insercion,
            bg="orange", width=20).grid(row=1, column=1)

        Button(self, text="Ordenar por Conteo", command=self.conteo,
            bg="violet", width=20).grid(row=1, column=2)

        # ============================= OUTPUTS =============================
        self.vc = Label(self, text="", bg="skyblue")
        self.vc.grid(row=2, column=0, columnspan=3)

        self.vb = Label(self, text="", bg="skyblue", wraplength=550)
        self.vb.grid(row=3, column=0, columnspan=3)

        self.vi = Label(self, text="", bg="skyblue", wraplength=550)
        self.vi.grid(row=4, column=0, columnspan=3)

        self.vco = Label(self, text="", bg="skyblue", wraplength=550)
        self.vco.grid(row=5, column=0, columnspan=3)

    # ============================= CREAR VECTOR =============================
    def crear(self):
        try:
            n = int(self.n.get())
            self.vector = [randint(100, 999) for _ in range(n)]
            self.vc.config(text=f"VECTOR ORIGINAL: {self.vector}",
                        font=("Arial", 10, "bold"))
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

            self.vb.config(text=f"BURBUJA: {v}\nComparaciones: {com}  Cambios: {cam}  Tiempo: {t:.6f} segundos")

        except AttributeError:
            mb.showerror("ERROR", "Primero debe crear el vector")

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

            self.vi.config(text=f"INSERCIÓN: {v}\nComparaciones: {com}  Cambios: {cam}  Tiempo: {t:.6f} segundos")

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

            self.vco.config(text=f"CONTEO: {vd}\nComparaciones: {com}  Tiempo: {t:.6f} segundos")

        except AttributeError:
            mb.showerror("ERROR", "Primero debe crear el vector")


Sorts().mainloop()
