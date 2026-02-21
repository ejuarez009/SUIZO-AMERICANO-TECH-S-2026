#=========================================================DCOUMENTACION INTERNA====================================================================================
# -- Objetivo: MEDIANTE MANEJO DE MATRICES Y ARCHIVOS, MULTIPLICAR DOS MATRICES LEIDAS DESDE ARCHIVOS DE TEXTO.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: El programa permite crear, grabar y abrir archivos de texto que contienen matrices.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter y modulo Random. Liberia Numpy para manejo de matrices.
# -- Procesos: Realizar las operaciones de crear, grabar, abrir archivos y multiplicar matrices.
# -- Historia: Fecha de creacion 31/01/2026 Fecha de modificacion: 02/02/2026
# -- Ajustes pendientes: Ninguno 
# ==================================================================================================================================================================
from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb 
import numpy as np

class Mange_Matrices_Files(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("800x470")
        self.title("MATRICES Y ARCHIVOS - ELMER JUAREZ C5")
        self.config(bg="skyblue")
        
        self.label_ruta1 = Label(text="")
        self.label_ruta1.pack()
        self.label_ruta2 = Label(text="")
        self.label_ruta2.pack()
        self.text_box1 = Text(width=50, height=10)
        self.text_box1.pack()
        self.text_box2 = Text(width=50, height=10)
        self.text_box2.pack(pady=20)
        
        self.button_create = Button(text="CREAR ARCHIVO", command=self.create_file, height=3)
        self.button_create.pack(side=LEFT)
        self.button_save = Button(text="GRABAR ARCHIVO", command=self.save_file, height=3)
        self.button_save.pack(side=LEFT)
        self.button_open = Button(text="ABRIR ARCHIVO", command=self.open_file, height=3)
        self.button_open.pack(side=LEFT)
        self.button_multiply = Button(text="MULTIPLICAR MATRICES", command=self.multiply_matrices, height=3)
        self.button_multiply.pack(side=LEFT)
        
        self.cont_matrices = 0 #CUENTA EL NUMERO DE MATRICES PARA CAMBIAR LA ETIQUETA DE ENCABEZADO
        self.ruta_select = [] #ALAMACENA LAS RUTAS PARA SER USADAS EN LA MULTIPLICACION DE MATRICES
        
    def create_file(self): 
        message_wn = mb.askyesno("ATENCION", "¿Desea crear un archivo?")
        if not message_wn: 
            route = fd.asksaveasfilename()
            with open(route, 'w'): 
                mb.showinfo("¡FELICIDADES!", "Se ha creado el archivo con éxito")
        else: 
            mb.showinfo("ATENCION", "No se creo ningun archivo")

    def save_file(self): 
        try: 
            route = fd.askopenfilename()
            with open(route, 'w') as archivo: 
                content = self.text_box1.get(1.0, END)
                archivo.write(content)
            self.text_box1.delete(1.0, END)
            mb.showinfo("ATENCION", "Ha grabado datos en un archivo correctamente")
        
        except Exception: 
            mb.showerror("ERROR", "Verfique bien las rutas")

    def open_file(self): 
        self.cont_matrices += 1
        try: 
            route = fd.askopenfilename()
            self.ruta_select.append(route)
            if self.cont_matrices == 1: 
                self.label_ruta1.config(text=route, fg="blue")
            else: 
                self.label_ruta2.config(text=route, fg="black")
            with open(route, 'r', encoding='utf-8') as archivo: 
                content = archivo.read()
                if self.cont_matrices == 1: #SI EL CONTADORR DE MATRICES ES UNA PUES LA ETIQUETA TENDRA DE VALOR UN UNO 
                    self.text_box1.insert(1.0, f"============MATRIZ {str(self.cont_matrices)}=========\n")
                else: 
                    self.text_box1.insert(END, f"\n============MATRIZ {str(self.cont_matrices)}=====\n")
                self.text_box1.insert(END, content)
            mb.showinfo("ATENCION", f"Se ha abierto exitosamente el archivo\n {route}")
            message_openagain = mb.askyesno("ATENCION", "¿Desea abrir otra matriz?")
            if message_openagain: 
                self.open_file() #PARA LLAMAR UNA FUNCION UTILIZAR < () > 
            else: 
                return
        except FileNotFoundError: #EXCEPCION DE ARCHIVO NO ENCONTRADO
            mb.showwarning("CUIDADO", "NO SE HA ABIERTO NINGUN ARCHIVO")
        

    def multiply_matrices(self): 
        matriz1 = np.loadtxt(self.ruta_select[0], delimiter='-') #SE OBTIENE LA RUTA EN DICHA POSICION PARA LA MATRIZ
        matriz2 = np.loadtxt(self.ruta_select[1], delimiter='-')
        

        if self.validar(matriz1, matriz2): 
            mb.showinfo("ATENCION", "Las matrices cuplen el criterio para la multiplicacion")
            self.text_box2.insert(1.0, "==============MATRIZ 1=============\n")
            self.text_box2.insert(END, str(matriz1))
            self.text_box2.insert(END, "\n==============MATRIZ 2==========\n")
            self.text_box2.insert(END, str(matriz2))
            self.text_box2.insert(END, "\n=============RESULTADO===============\n")
            result_multi = np.dot(matriz1, matriz2)
            self.text_box2.insert(END, str(result_multi))
        
        
    def validar(self, matriz1, matriz2): 
        return matriz1.shape[1] == matriz2.shape[0] #SHAPE: PODEMOS OBTENER EL NUMERO DE FILAS O COLUMNAS DE LA MATRIZ. DEVUELVE UNA TUPLA SI NO ESPECIFICAMOS
        #CRITERIO DE MULTPLICACION DE MATRICES COLUMAS DE LA PRIMERA = FILAS DE LA SEGUNDA
Mange_Matrices_Files().mainloop()