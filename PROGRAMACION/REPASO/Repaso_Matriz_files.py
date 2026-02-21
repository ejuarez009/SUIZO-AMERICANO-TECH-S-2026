from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb 
import numpy as np 

class Manage_flies_matriz(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("500x500")
        self.title("Manejo de Matrices mediante archivos")
        
        self.ruta_archivo1 = Label(text="--ruta archivo1--", fg="gray")
        self.ruta_archivo1.pack()
        self.ruta_archivo2 = Label(text="--ruta archivo2--", fg="gray")
        self.ruta_archivo2.pack()
        self.txt_box1 = Text(width=30, height=10)
        self.txt_box1.pack()
        self.txt_box2 = Text(width=30, height=10)
        self.txt_box2.pack(pady=10)
        
        self.button_abrir1 = Button(text="Abrir archivo No.1", command=self.abir1)
        self.button_abrir1.pack(side=LEFT)
        self.button_abrir2 = Button(text="Abrir archivo No.2", command=self.abrir2)
        self.button_abrir2.pack(side=LEFT)
        self.button_grabar = Button(text="Grabar archivo",command=self.grabar)
        self.button_grabar.pack(side=LEFT)
        self.button_crear = Button(text="Crear archivo", command=self.crear)
        self.button_crear.pack(side=LEFT)
        self.button_multi = Button(text="Multiplicar matrices", command=self.multiplicacion)
        self.button_multi.pack(side=LEFT)
    
    def crear(self): 
        message_showwarning = mb.askyesno("ATENCION", "¿Desea Crear un archivo?")
        if not message_showwarning and self.txt_box.get(1.0, END): 
            self.txt_box.delete(1.0, END)
        else: 
            ruta = fd.asksaveasfilename()
            with open(ruta, 'w'): 
                mb.showinfo("ATENCION", "Se ha creado un nuevo archivo exitosamente")
    
    def grabar(self): 
        ruta = fd.askopenfilename()
        self.ruta_archivo.config(text="")
        self.ruta_archivo.config(text=f"{ruta}", fg="black")
        with open(ruta, 'w') as archivo: 
            content = self.txt_box1.get(1.0, END)
            archivo.write(content)
        self.txt_box1.delete(1.0, END)
        mb.showinfo("ATENCION", "¡Se ha creado el archivo exitosamente!")
        
    def abir1(self): 
        ruta = fd.askopenfilename()
        self.ruta_archivo1.config(text="")
        self.ruta_archivo1.config(text=f"RUTA #1: {ruta}", fg="black")
        with open(ruta, 'r',encoding='utf-8') as archivo: 
            content = archivo.read()
            self.txt_box1.insert(1.0,"=========MATRIZ 1=========\n")
            self.txt_box1.insert(END,content)
        self.ruta_matriz1 = ruta

    def abrir2(self): 
        ruta = fd.askopenfilename()
        self.ruta_archivo2.config(text="")
        self.ruta_archivo2.config(text=f"RUTA #2: {ruta}", fg="blue")
        with open(ruta, 'r', encoding='utf-8') as archivo: 
            content = archivo.read()
            self.txt_box1.insert(END, "\n=========MATRIZ 2=========\n")
            self.txt_box1.insert(END, content)
        self.ruta_matriz2 = ruta
    
    def multiplicacion(self): 
        matriz1 = np.loadtxt(self.ruta_matriz1, delimiter='-')
        matriz2 = np.loadtxt(self.ruta_matriz2,delimiter='-')
        
        col1 = matriz1.shape
        row2 = matriz2.shape
        try:
            if self.validar(col1, row2): 
                mb.showinfo("ATENCION", "¡Las matrices son validas para multiplicar!")
            
                self.txt_box2.insert(1.0,"=========MATRIZ 1: =========\n")
                self.txt_box2.insert(END,matriz1)
                self.txt_box2.insert(END,"\n======MATRIZ 2: ========\n")
                self.txt_box2.insert(END, matriz2)
                self.txt_box2.insert(END,"\n=========RESULTADO==========\n")
                result = np.dot(matriz1, matriz2)
                self.txt_box2.insert(END,result)
        except Exception as e: 
            mb.showerror("ERROR", f"¡Las matrices no son validas para multiplicar! Error: {e}")
    
    def validar(self, p_col1, p_row2): 
        return p_col1 == p_row2

Manage_flies_matriz().mainloop()