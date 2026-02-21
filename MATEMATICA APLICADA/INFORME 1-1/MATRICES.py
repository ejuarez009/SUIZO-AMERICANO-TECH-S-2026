#=========================================================DCOUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Realizar un programa que permita la manipulación de matrices, incluyendo la generación automática de matrices con números aleatorios, la suma de matrices y la multiplicación de matrices.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: El programa consta de una interfaz gráfica que permite al usuario generar matrices automáticamente con números aleatorios, sumar matrices ingresadas manualmente y multiplicar matrices también ingresadas manualmente.
# -- Lenguaje: Python3
# -- Recursos: Modulos de la libreria Tkinter y el modulo Random 
# -- Procesos: Utilizacion de diferentes clases para manejar las distintas funcionalidades relacionadas con las matrices. Ciclos, condicionales y manejo de excepciones para asegurar la correcta manipulación de matrices.
# -- Historia: Fecha de creacion 23/01/2026 Fecha de modificacion: 01/02/2026
# -- Ajustes pendientes: Ninguno 
# ======================================================================================================================================================================================================================================
from tkinter import*; from tkinter import messagebox as mb
from tkinter import Tk, Spinbox, Label, Button, Toplevel, Text, messagebox as mb, Frame
from random import randint
import numpy as np 

class Matrix_base(Tk):
    def __init__(self): 
        super().__init__()
        self.geometry("400x400")
        self.title("MATRICES - ELMER JUAREZ_C5A")
        
        button = Button(self, text="MATRICES AUTOMATICAS", command=self.llama_Matrix_auto, height=3, width=30)
        button.config(font=("Arial", 12, "bold"), bg="lightblue", fg="black")
        button.grid(row=0,column=1, padx=50, pady=20)
        
        button2 = Button(self, text="SUMA DE MATRICES", command=self.llama_Adition_matrices, height=3, width=30)
        button2.config(font=("Arial", 12, "bold"), bg="pink", fg="black")
        button2.grid(row=1,column=1)
        
        button3 = Button(self, text="MULTIPLICACION DE MATRICES", command=self.llama_Multiply_matrices)
        button3.config(font=("Arial", 12, "bold"), bg="lightgreen", fg="black", height=3, width=30)
        button3.grid(row=2,column=1, padx=50, pady=20)
        
        button4 = Button(self, text="DETERMINATES", command=self.llama_Determinats)
        button4.config(bg="lightyellow", font=("Arial", 12, "bold"), height=3, width=30)
        button4.grid(row=3, column=1)
        

    def llama_Matrix_auto(self): #LLAMA A LA VENTANA DE MATRICES AUTOMATICAS
        Matrix_auto(self)
    
    def llama_Adition_matrices(self): #LLAMA A LA VENTANA DE SUMA DE MATRICES
        Adition_matrices(self)
    def llama_Multiply_matrices(self): #LLAMA A LA VENTANA DE MULTIPLICACION DE MATRICES
        Multiply_matrices(self)
    def llama_Determinats(self): 
        Determinants(self)

class Matrix_auto(Toplevel): 
    def __init__(self, master=None):
        super().__init__(master)        
        self.config(bg="skyblue")
        self.label_row = Label(self,text="Ingrese el No. de fila")
        self.label_row.grid(row=0, column=0)
        self.label_col = Label(self,text="Ingrese el No. de columna")
        self.label_col.grid(row=1, column=0)
        
        self.input_row = Entry(self,width=15)
        self.input_row.grid(row=0, column=1)
        self.input_col = Entry(self,width=15)
        self.input_col.grid(row=1, column=1)
        
        self.label_matriz1 = Label(self,text="MATRIZ 1")
        self.label_matriz1.grid(row=3, column=0, pady=10)
        self.label_matriz2 = Label(self,text="MATRIZ 2")
        self.label_matriz2.grid(row=4, column=0, pady=30)
        
        
        #BOTONES
        button_generar = Button(self,text="Generar Matriz 1", command=lambda: self.generar_matriz(self.label_matriz1, 1)) #CON LAMBDA PARA PASAR PARAMETROS Y REUTILIZAR A LA MATRIZ
        button_generar.grid(row=0, column=2)
        self.button_generar2 = Button(self,text="Generar Matriz 2", command=lambda: self.generar_matriz(self.label_matriz2, 2))
        self.button_generar2.grid(row=0, column=3)
        self.button_generar2.config(state="disabled")  
        
        
    def generar_matriz(self, label_destino, numero_matriz): 
        rows = int(self.input_row.get())
        cols = int(self.input_col.get())
        
        matriz = [None] * rows
        for i in range(rows): 
            matriz[i] = [0] * cols 
        
        self.matriz = matriz

        matriz_format = "[\n"
        for y in range(rows):
            fila = "[ "
            for x in range(cols):
                matriz[y][x] = randint(1, 100)
                if x < cols -1: 
                    fila += str(matriz[y][x]).ljust(3) + ", "
                else: 
                    fila += str(matriz[y][x]).ljust(3)
            fila += " ]"
            matriz_format += fila + "\n"
        matriz_format += "]"
        
        
        if numero_matriz == 1: 
            self.matriz1 = matriz
            label_destino.config(text= f"La matriz #1  es:\n{matriz_format}")
            self.button_generar2.config(state="active")
        else: 
            self.matriz2 = matriz
            
            label_destino.config(text= f"La matriz #2 es:\n{matriz_format}")
            
            self.button_suma = Button(self,text="SUMAR MATRICES",command=self.sumar_matrices)
            self.button_suma.grid(row=1, column=2, columnspan=2)
            
            self.label_suma = Label(self,text="MATRIZ_RESULTANTE")
            self.label_suma.grid(row=3 , column=2, rowspan=2)
    
    def sumar_matrices(self): 
        matriz1 = self.matriz1
        matriz2 = self.matriz2
        new_matriz = self.matriz
        
        matriz_format = "[\n"
        for i in range(len(matriz1)):
            fila = "["
            for j in range(len(matriz1[0])):
                new_matriz[i][j] = matriz1[i][j] + matriz2[i][j]
                
                if j < len(matriz1[0]) - 1: 
                    fila += str(new_matriz[i][j]).ljust(3) + ", "
                else: 
                    fila += str(new_matriz[i][j]).ljust(3)
            fila += " ]"
            matriz_format += fila + "\n"
        matriz_format += "]"

        self.label_suma.config(text=f"El resultado de la suma es: \n {matriz_format}")   

class Adition_matrices(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("900x500")
        self.title("MATRICES MANUALES")
        self.config(bg="lightpink")

        self.matrices = []

        # ============================
        # FRAME DEL FORMULARIO
        # ============================
        self.form_frame = Frame(self, bg="lightgray")
        self.form_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        Label(self.form_frame, text="Filas").grid(row=0, column=0, sticky="w")
        self.input_row = Entry(self.form_frame, width=10)
        self.input_row.grid(row=0, column=1)

        Label(self.form_frame, text="Columnas").grid(row=1, column=0, sticky="w")
        self.input_col = Entry(self.form_frame, width=10)
        self.input_col.grid(row=1, column=1)

        Label(self.form_frame, text="Cantidad de matrices").grid(row=2, column=0, sticky="w")
        self.input_num_matriz = Entry(self.form_frame, width=10)
        self.input_num_matriz.grid(row=2, column=1)

        Button(self.form_frame, text="Generar matrices",
            command=self.generar_matrices).grid(row=3, column=0, columnspan=2, pady=5)

        Button(self.form_frame, text="Llenar con números aleatorios",
            command=self.fill_matrices).grid(row=4, column=0, columnspan=2, pady=5)

        Button(self.form_frame, text="Sumar matrices",
            command=self.sumar_matrices).grid(row=5, column=0, columnspan=2, pady=5)

        Button(self.form_frame, text="RESET", bg="red", fg="white",
            command=self.reset_matrices).grid(row=6, column=0, columnspan=2, pady=5)

        self.result_label = Label(self.form_frame, text="", font=("Arial", 10, "bold"))
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

        # ============================
        # FRAME DE MATRICES
        # ============================
        self.matrices_frame = Frame(self, bg="lightpink")
        self.matrices_frame.grid(row=1, column=0, sticky="nw", padx=10)

    # ============================
    # GENERAR MATRICES
    # ============================
    def generar_matrices(self):
        try:
            self.reset_matrices()

            rows = int(self.input_row.get())
            cols = int(self.input_col.get())
            num = int(self.input_num_matriz.get())

            for n in range(num):
                frame = Frame(self.matrices_frame, bd=2, relief="groove") #DESIGNAMOS ESPACIONES CON FRAME PARA LAS MATRICES 
                frame.grid(row=0, column=n, padx=20, pady=5)

                Label(frame, text=f"Matriz {n + 1}",
                    font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=cols, pady=5)

                matriz = []
                for i in range(rows):
                    fila = []
                    for j in range(cols):
                        e = Entry(frame, width=5, justify="center")
                        e.grid(row=i + 1, column=j, padx=2, pady=2)
                        e.insert(0, "0")
                        fila.append(e)
                    matriz.append(fila)

                self.matrices.append(matriz)

        except ValueError:
            mb.showerror("Error", "Ingrese valores numéricos válidos")

    # ============================
    # LLENAR CON ALEATORIOS
    # ============================
    def fill_matrices(self):
        for matriz in self.matrices:
            for fila in matriz:
                for entry in fila:
                    entry.delete(0, END)
                    entry.insert(0, randint(1, 9))

    # ============================
    # SUMAR MATRICES
    # ============================
    def sumar_matrices(self):
        if not self.matrices:
            return

        try:
            rows = len(self.matrices[0])
            cols = len(self.matrices[0][0])

            resultado = [[0] * cols for _ in range(rows)]

            for matriz in self.matrices:
                for i in range(rows):
                    for j in range(cols):
                        resultado[i][j] += int(matriz[i][j].get())

            texto = "MATRIZ RESULTANTE:\n[\n"
            for fila in resultado:
                texto += f"  {fila}\n"
            texto += "]"

            self.result_label.config(text=texto)

        except ValueError:
            mb.showwarning("Cuidado", "Todos los campos deben contener números")

    # ============================
    # RESET
    # ============================
    def reset_matrices(self):
        for widget in self.matrices_frame.winfo_children():
            widget.destroy()

        self.matrices.clear()
        self.result_label.config(text="")

class Multiply_matrices(Toplevel):       
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x300")
        self.title("MULTIPLICAR MATRICES")
        self.config(bg="lightgreen")
        
        # ============================
        # FRAME DEL FORMULARIO
        # ============================
        self.form_frame = Frame(self, bg="lightgray")
        self.form_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        Label(self.form_frame, text="Ingrese el tamaño para la\n fila de la matriz 1:").grid(row=0, column=0, rowspan=2)
        self.input_row1 = Entry(self.form_frame,width=10)
        self.input_row1.grid(row=0, column=1, rowspan=2)
        
        Label(self.form_frame, text="Ingrese el tamaño para la\n columna de la matriz 2:").grid(row=2, column=0, rowspan=2)
        self.input_col1 = Entry(self.form_frame,width=10)
        self.input_col1.grid(row=2, column=1, rowspan=2)
        
        Label(self.form_frame, text="Ingrese el tamaño para la\n fila de la matriz 2:").grid(row=5, column=0, rowspan=2)
        self.input_col2 = Entry(self.form_frame,width=10)
        self.input_col2.grid(row=5, column=1, rowspan=2)
        
        button_generar = Button(self.form_frame, text="Generar Matrices", command=self.generar_matrices)
        button_generar.grid(row=0, column=4)
        button_fillear = Button(self.form_frame, text="Llenar con Aleatorios", command=self.fill_random)
        button_fillear.grid(row=1, column=4)
        button_multiplicar = Button(self.form_frame, text="Multiplicar Matrices", command=self.multiply_matrices)
        button_multiplicar.grid(row=2, column=4)
        button_resetear = Button(self.form_frame, text="Resetear", command=self.reset_matrices)
        button_resetear.grid(row=3, column=4)
    
    
    def generar_matrices(self): 
        try: 
            row_matriz1 = int(self.input_row1.get())
            col_matriz1 = int(self.input_col1.get())
            row_matriz2 = col_matriz1
            col_matriz2 = int(self.input_col2.get())

            start_row = 8

            # ==================== MATRIZ 1 =======================================
            self.frame_matriz1 = Frame(self, bd=2, relief="groove")
            self.frame_matriz1.grid(row=start_row, column=0, padx=20, pady=5)

            Label(
                self.frame_matriz1,
                text="Matriz 1",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=0, columnspan=col_matriz1, pady=5)

            matriz1 = []
            for i in range(row_matriz1):
                fila = []
                for j in range(col_matriz1):
                    e = Entry(self.frame_matriz1, width=5)
                    e.grid(row=i+1, column=j, padx=2, pady=2)
                    e.insert(0, "0")
                    fila.append(e)
                matriz1.append(fila)

            # ============================== MATRIZ 2 ===================================
            self.frame_matriz2 = Frame(self, bd=2, relief="groove")
            self.frame_matriz2.grid(row=start_row, column=1, padx=20, pady=5)

            Label(
                self.frame_matriz2,
                text="Matriz 2",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=0, columnspan=col_matriz2, pady=5)

            matriz2 = []
            for i in range(row_matriz2):
                fila = []
                for j in range(col_matriz2):
                    e = Entry(self.frame_matriz2, width=5)
                    e.grid(row=i+1, column=j, padx=2, pady=2)
                    e.insert(0, "0")
                    fila.append(e)
                matriz2.append(fila)

            self.matriz1 = matriz1
            self.matriz2 = matriz2
        except ValueError: 
            mb.showerror("Error", "Ingrese valores numéricos válidos")

    
    def multiply_matrices(self):
        try: 
            A = self.matriz1
            B = self.matriz2

            filas_A = len(A)
            cols_A = len(A[0])
            cols_B = len(B[0])

            # ---- calcular matriz resultado ----
            resultado = []
            for i in range(filas_A):
                fila = []
                for j in range(cols_B):
                    suma = 0
                    for k in range(cols_A):
                        a = int(A[i][k].get())
                        b = int(B[k][j].get())
                        suma += a * b
                    fila.append(suma)
                resultado.append(fila)

            self.matriz_result = resultado

            # ---- borrar resultado anterior si existe ----
            if hasattr(self, "frame_result"):
                self.frame_result.destroy()

            # ---- mostrar resultado formateado ----
            frame_result = Frame(self, bd=2, relief="groove")
            frame_result.grid(row=20, column=0, columnspan=3, pady=10)

            Label(
                frame_result,
                text="Matriz Resultado",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=0, columnspan=cols_B, pady=5)

            for i in range(len(resultado)):
                for j in range(len(resultado[0])):
                    Label(
                        frame_result,
                        text=resultado[i][j],
                        width=5,
                        relief="solid"
                    ).grid(row=i+1, column=j, padx=2, pady=2)

            self.frame_result = frame_result
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al multiplicar las matrices: {str(e)}")

        
    def fill_random(self):
        try: 
            for fila in self.matriz1:
                for e in fila:
                    e.delete(0, "end")
                    e.insert(0, randint(1, 20))

            for fila in self.matriz2:
                for e in fila:
                    e.delete(0, "end")
                    e.insert(0, randint(1, 20))
        except AttributeError:
            mb.showwarning("Cuidado", "Primero genere las matrices")
    
    def reset_matrices(self):
        # ---- borrar matriz 1 ----
        if hasattr(self, "frame_matriz1"):
            self.frame_matriz1.destroy()
            del self.frame_matriz1

        # ---- borrar matriz 2 ----
        if hasattr(self, "frame_matriz2"):
            self.frame_matriz2.destroy()
            del self.frame_matriz2

        # ---- borrar matriz resultado ----
        if hasattr(self, "frame_result"):
            self.frame_result.destroy()
            del self.frame_result

        # ---- limpiar referencias ----
        self.matriz1 = []
        self.matriz2 = []

class Determinants(Toplevel): 
    def __init__(self, master=None):
        super().__init__(master)
        
        self.geometry("600x600")
        
        frame_widgets = Frame(self)
        frame_widgets.grid(row=0, column=0)
        
        Label(frame_widgets,text="Ingrese el número de filas").grid(row=0, column=0)
        self.input_row = Spinbox(frame_widgets, from_=0, to=10, increment=1, width=10, state='readonly')
        self.input_row.grid(row=0, column=1)
        Label(frame_widgets, text="Ingrese el núnmero de columnas:").grid(row=1, column=0)
        self.input_col = Spinbox(frame_widgets, from_=0, to=10, increment=1, width=10, state='readonly')
        self.input_col.grid(row=1, column=1)
        
        
        self.button_create = Button(frame_widgets, text="CREAR MATRIZ", command=self.crear_matriz).grid(row=2, column=1, padx=10,  pady=10)
        self.button_determinante = Button(frame_widgets, text="CALCULAR DETERMINANTE",command=self.determinants).grid(row=2, column=2, padx=10, pady=10)
        self.button_delete = Button(frame_widgets, text="LLENAR MATRIZ", command=self.fill_matriz).grid(row=2, column=3, padx=10, pady=10)
        self.button_delete = Button(frame_widgets, text="BORRAR MATRIZ", command=self.delete_matriz).grid(row=2, column=4, padx=10, pady=10)
        
        
        frame_label_det = Frame(self)
        frame_label_det.grid(row=2, column=0)           
        self.label_determinante = Label(frame_label_det, text="")
        self.label_determinante.grid(row=0, column=1, padx=30, pady=30)
        
        
    def crear_matriz(self): 
        rows = int(self.input_row.get())
        columns = int(self.input_col.get())
        
        if rows <= 1 or columns <= 1: 
            mb.showinfo("Atencion", "Solo se puede manejar matrices en 2D o mas dimensiones")
            
        self.frame_matriz = Frame(self)
        self.frame_matriz.grid(row=1, column=0)
        self.matriz = [[None]*columns for _ in range(rows)]

        for y in range(rows): 
            for x in range(columns):
                entry = Entry(self.frame_matriz, width=5)
                entry.grid(row=y+1, column=x)
                entry.insert(0,"0")
                self.matriz[y][x] = entry
            
        
    def determinants(self): 
        matriz_num = []
        for i in range(len(self.matriz)):
            rows = []
            for j in range(len(self.matriz[i])):
                cols = int(self.matriz[i][j].get())
                rows.append(cols)
            matriz_num.append(rows)
        
        determinante = np.linalg.det(np.array(matriz_num))
        self.label_determinante.config(text=f"La determinante es {round(determinante,4)}")
        
    def fill_matriz(self): 
        for row in range(len(self.matriz)):
            for col in range(len(self.matriz[row])): 
                self.matriz[row][col].delete(0,END)
                self.matriz[row][col].insert(0, randint(1,9))
                
    
    def delete_matriz(self): 
        if hasattr(self, "frame_matriz"):
            self.frame_matriz.destroy()
            del self.frame_matriz
            self.label_determinante.config(text="")

Matrix_base().mainloop() 