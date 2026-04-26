#=========================================================DOCUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Realizar un programa que permita calcular los autovalores (Eigenvalues) de una matriz cuadrada de 2x2 o 3x3, verificando previamente que la matriz tenga determinante distinto de cero.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descripcion: El programa consta de una interfaz gráfica que permite al usuario ingresar una matriz de 2x2 o 3x3 manualmente o con valores aleatorios, verificar si su determinante es distinto de cero y calcular sus autovalores (λ).
# -- Lenguaje: Python3
# -- Recursos: Módulos de la librería Tkinter, módulo Random y NumPy
# -- Procesos: Se utiliza la clase principal como ventana base con botones de acceso. La clase Eigenvalues hereda de Toplevel y contiene: 
#              generación de matriz, llenado aleatorio, cálculo de determinante (reutilizado del código base) y cálculo de autovalores mediante numpy.
#              Se valida que la determinante sea ≠ 0 antes de mostrar los autovalores λ.
# -- Historia: Fecha de creación 15/04/2026
# -- Ajustes pendientes: Ninguno
# ======================================================================================================================================================================================================================================

from tkinter import *
from tkinter import messagebox as mb
from tkinter import Spinbox
from random import randint
import numpy as np


# ============================================================
# CLASE BASE - VENTANA PRINCIPAL
# ============================================================
class Main_base(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("AUTOVALORES (λ) - ELMER JUAREZ_C5A")

        button = Button(self, text="AUTOVALORES (EIGENVALUES)", command=self.abrir_eigenvalues, height=3, width=30)
        button.config(font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
        button.grid(row=0, column=1, padx=50, pady=60)

    def abrir_eigenvalues(self):
        Eigenvalues(self)


# ============================================================
# CLASE EIGENVALUES - VENTANA DE CÁLCULO
# ============================================================
class Eigenvalues(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Autovalores (λ) - Eigenvalues")
        self.geometry("700x620")
        self.config(bg="#1e1e2e")
        self.resizable(False, False)

        self.entries = []     # Entradas de la matriz
        self.n = 0            # Tamaño actual de la matriz

        # ============================
        # TÍTULO
        # ============================
        Label(
            self,
            text="AUTOVALORES (EIGENVALUES)",
            font=("Courier", 16, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(pady=(20, 5))

        Label(
            self,
            text="Se utiliza det(A − λI) = 0  para encontrar los valores propios λ",
            font=("Courier", 9),
            bg="#1e1e2e",
            fg="#6c7086"
        ).pack(pady=(0, 10))

        # ============================
        # FRAME DE CONTROLES
        # ============================
        frame_controles = Frame(self, bg="#313244", bd=0)
        frame_controles.pack(padx=20, pady=5, fill="x")

        Label(
            frame_controles,
            text="Tamaño de la matriz:",
            font=("Courier", 11),
            bg="#313244",
            fg="#cdd6f4"
        ).grid(row=0, column=0, padx=15, pady=12)

        # Spinbox limitado a 2 o 3 únicamente
        self.spin_size = Spinbox(
            frame_controles,
            values=(2, 3),
            width=5,
            state="readonly",
            font=("Courier", 11),
            bg="#45475a",
            fg="#cdd6f4",
            buttonbackground="#89b4fa",
            relief="flat"
        )
        self.spin_size.grid(row=0, column=1, padx=10, pady=12)

        Button(
            frame_controles,
            text="Crear Matriz",
            command=self.crear_matriz,
            font=("Courier", 10, "bold"),
            bg="#a6e3a1",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        ).grid(row=0, column=2, padx=8)

        Button(
            frame_controles,
            text="Aleatorio",
            command=self.llenar_aleatorio,
            font=("Courier", 10, "bold"),
            bg="#f9e2af",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        ).grid(row=0, column=3, padx=8)

        Button(
            frame_controles,
            text="Limpiar",
            command=self.limpiar_matriz,
            font=("Courier", 10, "bold"),
            bg="#f38ba8",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5
        ).grid(row=0, column=4, padx=8)

        # ============================
        # FRAME DE LA MATRIZ
        # ============================
        self.frame_matriz = Frame(self, bg="#1e1e2e")
        self.frame_matriz.pack(pady=15)

        # ============================
        # BOTÓN CALCULAR
        # ============================
        Button(
            self,
            text="▶  CALCULAR AUTOVALORES (λ)",
            command=self.calcular_eigenvalues,
            font=("Courier", 12, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(pady=10)

        # ============================
        # FRAME DE RESULTADOS
        # ============================
        self.frame_resultados = Frame(self, bg="#313244", bd=0)
        self.frame_resultados.pack(padx=20, pady=5, fill="x")

        self.label_det = Label(
            self.frame_resultados,
            text="",
            font=("Courier", 11),
            bg="#313244",
            fg="#a6e3a1"
        )
        self.label_det.pack(pady=(12, 4))

        self.label_eigen = Label(
            self.frame_resultados,
            text="",
            font=("Courier", 13, "bold"),
            bg="#313244",
            fg="#cba6f7",
            justify="left"
        )
        self.label_eigen.pack(pady=(4, 12))

        # ============================
        # NOTA INFORMATIVA
        # ============================
        Label(
            self,
            text="Nota: si det(A) = 0, la matriz es singular y λ = 0 es un autovalor trivial.\nSe mostrará una advertencia pero igual se calcularán los autovalores.",
            font=("Courier", 8),
            bg="#1e1e2e",
            fg="#6c7086",
            justify="center"
        ).pack(pady=(5, 0))

    # ============================
    # CREAR MATRIZ
    # ============================
    def crear_matriz(self):
        # Limpiar frame anterior
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        self.entries = []
        self.label_det.config(text="")
        self.label_eigen.config(text="")

        try:
            n = int(self.spin_size.get())
            if n not in (2, 3):
                raise ValueError
        except ValueError:
            mb.showerror("Error", "Solo se permiten matrices de 2×2 o 3×3")
            return

        self.n = n

        # Encabezado de la matriz
        Label(
            self.frame_matriz,
            text=f"Matriz A ({n}×{n})",
            font=("Courier", 11, "bold"),
            bg="#1e1e2e",
            fg="#89dceb"
        ).grid(row=0, column=0, columnspan=n, pady=(0, 8))

        # Crear las entradas de la matriz
        for i in range(n):
            fila = []
            for j in range(n):
                entry = Entry(
                    self.frame_matriz,
                    width=6,
                    font=("Courier", 13),
                    justify="center",
                    bg="#45475a",
                    fg="#cdd6f4",
                    insertbackground="#cdd6f4",
                    relief="flat",
                    bd=4
                )
                entry.grid(row=i + 1, column=j, padx=6, pady=6)
                entry.insert(0, "0")
                fila.append(entry)
            self.entries.append(fila)

    # ============================
    # LLENAR CON ALEATORIOS
    # ============================
    def llenar_aleatorio(self):
        if not self.entries:
            mb.showwarning("Atención", "Primero debe crear la matriz")
            return

        for fila in self.entries:
            for entry in fila:
                entry.delete(0, END)
                entry.insert(0, randint(-9, 9))

    # ============================
    # LIMPIAR MATRIZ (pone ceros)
    # ============================
    def limpiar_matriz(self):
        for fila in self.entries:
            for entry in fila:
                entry.delete(0, END)
                entry.insert(0, "0")
        self.label_det.config(text="")
        self.label_eigen.config(text="")

    # ============================
    # OBTENER MATRIZ NUMÉRICA
    # ============================
    def obtener_matriz_numpy(self):
        matriz = []
        for fila in self.entries:
            fila_vals = []
            for entry in fila:
                try:
                    fila_vals.append(float(entry.get()))
                except ValueError:
                    fila_vals.append(0.0)
            matriz.append(fila_vals)
        return np.array(matriz, dtype=float)

    # ============================
    # VERIFICAR DETERMINANTE
    # Reutilizado de la clase Determinants del código base
    # ============================
    def verificar_determinante(self, A):
        determinante = np.linalg.det(A)
        return round(determinante, 6)

    # ============================
    # CALCULAR AUTOVALORES (λ)
    # ============================
    def calcular_eigenvalues(self):
        if not self.entries:
            mb.showwarning("Atención", "Primero debe crear e ingresar la matriz")
            return

        try:
            A = self.obtener_matriz_numpy()

            # --- Verificación de determinante (reutilizada del código base) ---
            det = self.verificar_determinante(A)

            if det == 0.0:
                self.label_det.config(
                    text=f"⚠  det(A) = {det}  →  Matriz SINGULAR (λ = 0 es autovalor)",
                    fg="#f38ba8"
                )
                mb.showwarning(
                    "Advertencia",
                    f"det(A) = {det}\n\nLa matriz es singular (determinante = 0).\n"
                    "Esto significa que λ = 0 es uno de sus autovalores.\n"
                    "Se calcularán todos los autovalores igualmente."
                )
            else:
                self.label_det.config(
                    text=f"✓  det(A) = {det}  →  Matriz INVERTIBLE",
                    fg="#a6e3a1"
                )

            # --- Cálculo de autovalores con numpy ---
            eigenvalues, _ = np.linalg.eig(A)

            # Formatear la salida de autovalores λ
            resultado = "Autovalores (λ):\n"
            for idx, val in enumerate(eigenvalues, start=1):
                if val.imag == 0:
                    # Autovalor real
                    resultado += f"  λ{idx} = {round(val.real, 6)}\n"
                else:
                    # Autovalor complejo
                    parte_real = round(val.real, 6)
                    parte_img  = round(val.imag, 6)
                    signo      = "+" if parte_img >= 0 else "-"
                    resultado += f"  λ{idx} = {parte_real} {signo} {abs(parte_img)}i\n"

            self.label_eigen.config(text=resultado.strip())

        except Exception as e:
            mb.showerror("Error inesperado", f"Ocurrió un error al calcular:\n{str(e)}")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
Main_base().mainloop()