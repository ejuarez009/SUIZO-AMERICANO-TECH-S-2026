from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb 
import numpy as np 


class Mange_Matrices_Files(Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("600x500")
        self.title("Manejo de archivos")
        
        self.label_route1 = Label(text="--ruta1--", fg="gray")
        self.label_route1.pack()
        self.label_route2 = Label(text="--ruta 2--", fg="gray")
        self.label_route2.pack()
        
        self.text_box1 = Text(width=50, height=10)
        self.text_box1.pack()
        self.text_box2 = Text(width=50, height=10)
        self.text_box2.pack()
        
        self.button_create = Button(text="CREAR ARRCHIVO", command=self.create)
        self.button_create.pack(side=LEFT)
        self.button_save = Button(text="GRABARR ARCHIVO", command=self.save)
        self.button_save.pack(side=LEFT)
        self.button_open = Button(text="ABRIR ARCHIVO", command=self.open_file)
        self.button_open.pack(side=LEFT)
        self.button_multi = Button(text="MULTIPLICAR MATRICES")
        self.button_multi.pack(side=LEFT)
        self.button_analizar = Button(text="ANALIZAR ARCHIVO", command=self.analizar)
        self.button_analizar.pack(side=LEFT)
    
        self.num_matriz = 0
        self.ruta_list = []

    def create(self): 
        message_ask = mb.askyesno("ATENCION", "¿Desea crear un archivo?")
        if message_ask: 
            ruta = fd.asksaveasfilename()
            with open(ruta, 'w'): 
                mb.showinfo("ATENCION", "Has creado un archivo exitosamente")
    
    
    def save(self): 
        ruta = fd.askopenfilename()
        with open(ruta, 'w') as archivo: 
            content = self.text_box1.get(1.0, END)
            archivo.write(content)
        self.text_box1.delete(1.0, END)
        mb.showinfo("Atencion", "La informacion para el archivo ha sido grabado exitosamente")
            
    def open_file(self): 
        ruta = fd.askopenfilename()
        self.ruta_list.append(ruta)
        self.num_matriz +=1 
        with open(ruta, 'r', encoding='utf-8') as archivo: 
            content = archivo.read() 
            if self.num_matriz == 1: 
                self.text_box2.insert(1.0, "===============MATRIZ 1=============\n")
            else:
                self.text_box2.insert(END, f"\n===============MATRIZ {self.num_matriz}=============\n")
            self.text_box2.insert(END, content)

    def analizar(self): 
        ruta = fd.askopenfilename()
        patron = "1234567890"
        patron2 = "aeiouAEIOU"
        with open(ruta, 'r', encoding='utf-8') as archivo: 
            contenido = archivo.readlines() 
            for linea in contenido: 
                contar_num = 0
                contar_vocales = 0
                for character in linea: 
                    if character in patron: 
                        contar_num += 1
                    elif character in patron2: 
                        contar_vocales += 1
            
                self.label_result.config(f"Numero de vocales: {contar_vocales}, Cantidad de numeros: {contar_num}")
            
            
Mange_Matrices_Files().mainloop()