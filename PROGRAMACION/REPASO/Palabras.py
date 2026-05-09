from tkinter import*; from tkinter import messagebox as mb; from tkinter import filedialog as fd 
from tkinter import ttk
import re


class app(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("1100x500")
        self.title("Práctica de Palabras - Laboratorio #3")
        
        Label(text="Ingrese la palabras a buscar").grid(row=0, column=0)
        self.entry_word = Entry()
        self.entry_word.grid(row=1, column=0)
        
        self.label_stack = Label(text="--vector--")
        self.label_stack.grid(row=2, column=0)
        
        self.textbox = Text(width=50, height=10)
        self.textbox.grid(row=3, column=0)
        
        self.label_ruta = Label(text="--ruta--", fg="gray")
        self.label_ruta.grid(row=4, column=0)
        
        
        Button(text="Crear un archivo", command=self.crear).grid(row=5, column=0)
        Button(text="Abrir archivo", command=self.abrir).grid(row=6, column=0)
        Button(text="Grabar Archivo", command=self.grabar).grid(row=7, column=0)
        Button(text="Ingresar palabra", command=self.push).grid(row=8, column=0)
        Button(text="Sacar una palabra", command=self.pop).grid(row=9, column=0)
        Button(text="Analizar archivo", command=self.analizar).grid(row=10, column=0)
        
        self.stack = [""] * 3
        self.spointer = 0
        self.ruta = None
    
    
    def crear(self): 
        try: 
            self.ruta = fd.asksaveasfilename()
            self.label_ruta.config(text=f"RUTA:{self.ruta}", fg="blue")
        except FileNotFoundError, FileExistsError: 
            mb.showerror("Error", "No se ha creado un archivo")
            return
        
        with open(self.ruta, 'w', encoding='utf-8') as archivo:
            archivo.write('')
    
    def abrir(self): 
        try: 
            self.ruta = fd.askopenfilename()
            self.label_ruta.config(text=f"RUTA:{self.ruta}", fg="blue")
        except FileNotFoundError, FileExistsError: 
            mb.showerror("Error", "No se ha creado un archivo")
        with open(self.ruta, 'r', encoding='utf-8') as archivo: 
            contenido = archivo.read()
            self.textbox.delete(1.0, END)
            self.textbox.insert(END, contenido)
    
    def grabar(self): 
        if self.ruta == None: 
            estado = mb.askyesno("Atencion", "No hay un archivo abierto para grabar \n¿Desea abrir un archivo?")
            if estado: 
                self.abrir()
            else: 
                mb.showinfo("Atencion", "No se ha abierto ningun archivo")
        else: 
            contenido = self.textbox.get(1.0, END)
            with open(self.ruta, 'w', encoding='utf-8') as archivo: 
                archivo.write(contenido)
                self.textbox.delete(1.0, END)
    
    def push(self): 
        palabra = str(self.entry_word.get())
        if self.spointer < 3: 
            self.stack[self.spointer] = palabra.lower()
            self.spointer +=1
            self.label_stack.config(text=f"{self.stack}", fg="green")
            self.entry_word.delete(0, END)
        else: 
            mb.showwarning("Cuidado", "Ha llegado al límite del vector")
    
    def pop(self): 
        if self.spointer > 0: 
            self.stack[self.spointer-1] = ""
            self.spointer -= 1
            self.label_stack.config(text=f"{self.stack}", fg="red")
        else: 
            mb.showwarning("Cuidado", "No hay palabras para sacar")

    def analizar(self): 
        if self.ruta == None:
            mb.showinfo("Atencion", "Debe abrir un archivo primero") 
            return 
        
        
        encabezados = ["Palabra", "Longitud", "Frecuencia"]
        tree = ttk.Treeview(height=20, columns=encabezados, show='headings')
        for encabezado in encabezados: 
            tree.heading(encabezado, text=encabezado)
        tree.grid(row=1, column=1, rowspan=10, padx=20)
        
        #Omite las posiciones que esten vacias
        stack2 = []
        for e in self.stack: 
            if e != "": 
                stack2.append(e)
        
        contador = 0
        with open(self.ruta, 'r', encoding='utf-8') as archivo: 
            contenido = archivo.read()
            lineas = contenido.splitlines()
            for i in range(len(stack2)): #Ir buscando en el archivo la palabra del stack
                for linea in lineas: 
                    palabras = re.split(r"[' '\t\n,]", linea)
                    for palabra in palabras: 
                        if palabra.lower() == stack2[i]: 
                            print(palabra, stack2[i])
                            contador +=1
                if contador > 0: 
                    tree.insert("", END, values=(stack2[i], len(self.stack[i]), contador))
                else:
                    tree.insert("",END,values=(stack2[i], len(self.stack[i]), "No se encontró"))
                contador = 0
                        


app().mainloop()