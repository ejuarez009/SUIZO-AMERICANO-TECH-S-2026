#=========================================================DOCUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Realizar un programa que permita calcular los autovalores (Eigenvalues) de una matriz cuadrada de 2x2 o 3x3, verificando previamente que la matriz tenga determinante distinto de cero.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descripcion: El programa consta de una interfaz gráfica que permite al usuario ingresar una matriz de 2x2 o 3x3 manualmente o con valores aleatorios, verificar si su determinante es distinto de cero y calcular sus autovalores (λ).
# -- Lenguaje: Python3
# -- Recursos: Módulos de la librería Tkinter, módulo Random y NumPy
# -- Procesos: Se utiliza la clase principal como ventana base con botones de acceso. La clase Eigenvalues hereda de Toplevel y contiene: 
#              generación de matriz, llenado aleatorio, cálculo de determinante (reutilizado del código base) y cálculo de autovalores mediante numpy.
#              Se valida que la determinante sea ≠ 0 antes de mostrar los autovalores λ.
#              Se muestra el polinomio característico det(A - λI) = 0 expandido.
#              El aviso de matriz singular se muestra como label en la misma ventana (sin messagebox que tape la interfaz).
# -- Historia: Fecha de creación 15/04/2026 | Ajuste: 16/04/2026 - Polinomio característico + aviso inline + mejora de layout
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
        self.geometry("700x520")
        self.resizable(False, False)

        self.entries = []
        self.n = 0

        # ============================================================
        # FILA 0: controles izquierda | matriz derecha
        # ============================================================
        frame_controles = Frame(self)
        frame_controles.grid(row=0, column=0, padx=15, pady=12, sticky="nw")

        self.frame_matriz = Frame(self)
        self.frame_matriz.grid(row=0, column=1, padx=20, pady=12, sticky="n")

        # ============================
        # CONTROLES
        # ============================
        Label(frame_controles, text="Tamaño de la matriz:").grid(row=0, column=0, sticky="w")

        self.spin_size = Spinbox(frame_controles, values=(2, 3), width=5, state="readonly")
        self.spin_size.grid(row=0, column=1, padx=(4, 0))

        Button(frame_controles, text="Crear Matriz",
            command=self.crear_matriz, width=28).grid(row=1, column=0, columnspan=2, pady=(10, 3))

        Button(frame_controles, text="Llenar con números aleatorios",
            command=self.llenar_aleatorio, width=28).grid(row=2, column=0, columnspan=2, pady=3)

        Button(frame_controles, text="CALCULAR AUTOVALORES (λ)",
            command=self.calcular_eigenvalues,
            bg="lightyellow", font=("Arial", 10, "bold"), width=28).grid(row=3, column=0, columnspan=2, pady=3)

        Button(frame_controles, text="LIMPIAR",
            bg="red", fg="white", command=self.limpiar_matriz, width=28).grid(row=4, column=0, columnspan=2, pady=(3, 10))

        # ============================================================
        # FILA 1: panel de resultados — ocupa todo el ancho (col 0+1)
        # ============================================================
        frame_resultados = Frame(self, bd=1, relief="groove", bg="#f7f7f7")
        frame_resultados.grid(row=1, column=0, columnspan=2, padx=15, pady=(0, 12), sticky="ew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Título del panel
        Label(frame_resultados, text="Resultados", font=("Arial", 10, "bold"),
            bg="#f7f7f7", anchor="w").grid(row=0, column=0, columnspan=3, padx=10, pady=(6, 2), sticky="w")

        # ── Determinante ──────────────────────────────────────
        self.label_det = Label(frame_resultados, text="",
                            font=("Arial", 10), bg="#f7f7f7", anchor="w")
        self.label_det.grid(row=1, column=0, padx=10, pady=2, sticky="w")

        # ── Aviso singular (misma fila, a la derecha del det) ──
        self.label_aviso = Label(frame_resultados, text="",
                                font=("Arial", 9, "italic"), fg="darkorange",
                                bg="#f7f7f7", anchor="w", justify="left")
        self.label_aviso.grid(row=1, column=1, padx=(0, 10), pady=2, sticky="w")

        # ── Separador visual ──────────────────────────────────
        Frame(frame_resultados, height=1, bg="#cccccc").grid(
            row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=4)

        # ── Polinomio característico ──────────────────────────
        self.label_polinomio = Label(frame_resultados, text="",
                                    font=("Courier", 9), fg="darkblue",
                                    bg="#f7f7f7", justify="left", anchor="w")
        self.label_polinomio.grid(row=3, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        # ── Autovalores ───────────────────────────────────────
        self.label_eigen = Label(frame_resultados, text="",
                                font=("Arial", 10, "bold"),
                                bg="#f7f7f7", justify="left", anchor="w")
        self.label_eigen.grid(row=4, column=0, columnspan=2, padx=10, pady=(2, 8), sticky="w")


    # ============================
    # CREAR MATRIZ
    # ============================
    def crear_matriz(self):
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        self.entries = []
        self._limpiar_resultados()

        try:
            n = int(self.spin_size.get())
            if n not in (2, 3):
                raise ValueError
        except ValueError:
            mb.showerror("Error", "Solo se permiten matrices de 2×2 o 3×3")
            return

        self.n = n

        Label(self.frame_matriz, text=f"Matriz A ({n}×{n})",
              font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=n, pady=(0, 6))

        for i in range(n):
            fila = []
            for j in range(n):
                entry = Entry(self.frame_matriz, width=5, justify="center")
                entry.grid(row=i + 1, column=j, padx=3, pady=3)
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
    # LIMPIAR
    # ============================
    def limpiar_matriz(self):
        for fila in self.entries:
            for entry in fila:
                entry.delete(0, END)
                entry.insert(0, "0")
        self._limpiar_resultados()

    def _limpiar_resultados(self):
        self.label_det.config(text="")
        self.label_aviso.config(text="")
        self.label_polinomio.config(text="")
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
        return round(np.linalg.det(A), 6)

    # ============================
    # CONSTRUIR POLINOMIO CARACTERÍSTICO
    # ============================
    def construir_polinomio(self, A):
        coefs = np.poly(A)
        n = len(coefs) - 1
        terminos = []

        for i, c in enumerate(coefs):
            potencia = n - i

            # Redondeo limpio
            c = round(c.real, 4)

            if abs(c) < 1e-10:
                continue

            # Signo
            if c > 0 and terminos:
                signo = " + "
            elif c < 0:
                signo = " - " if terminos else "-"
            else:
                signo = ""

            valor = abs(c)

            # Construcción del término
            if potencia == 0:
                termino = f"{valor}"
            elif potencia == 1:
                termino = "λ" if valor == 1 else f"{valor}λ"
            else:
                termino = f"λ^{potencia}" if valor == 1 else f"{valor}λ^{potencia}"

            terminos.append(f"{signo}{termino}")

        polinomio = "".join(terminos)

        return f"Polinomio:\ndet(A - λI) = 0\n{polinomio} = 0"

    # ============================
    # CALCULAR AUTOVALORES (λ)
    # ============================
    def calcular_eigenvalues(self):
        if not self.entries:
            mb.showwarning("Atención", "Primero debe crear e ingresar la matriz")
            return

        try:
            A = self.obtener_matriz_numpy()
            self.label_aviso.config(text="")

            det = self.verificar_determinante(A)

            if det == 0:
                self.label_det.config(text=f"det(A) = {det}  ⚠ Matriz SINGULAR")
                self.label_aviso.config(text="λ = 0 es autovalor  |  Se calculan todos igualmente.")
            else:
                self.label_det.config(text=f"det(A) = {det}  ✔ Matriz invertible")

            self.label_polinomio.config(text=self.construir_polinomio(A))

            eigenvalues, _ = np.linalg.eig(A)

            resultado = "Autovalores (λ):\n"
            for idx, val in enumerate(eigenvalues, start=1):
                if val.imag == 0:
                    resultado += f"  λ{idx} = {round(val.real, 6)}\n"
                else:
                    pr = round(val.real, 6)
                    pi = round(val.imag, 6)
                    signo = "+" if pi >= 0 else "-"
                    resultado += f"  λ{idx} = {pr} {signo} {abs(pi)}i\n"

            self.label_eigen.config(text=resultado.strip())

        except Exception as e:
            mb.showerror("Error inesperado", f"Ocurrió un error al calcular:\n{str(e)}")


Main_base().mainloop()