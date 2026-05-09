#DOCUMENTACION INTERNA
#AUTOR: ELMER JUAREZ 
#FECHA: 8/05/2026
#LENGUAJE: PYTHON3
#HERRAMIENTAS: LIBERÍA TKINTER, OBJETO TREEVIEW, MODULO FILEDIALOG 
#PROCESOS PENDIENTES: NINGUNO
#DESCRIPCIÓN: EN ESTE PROGRAMA EL CUAL MANEJA ARCHIVOS DE TEXTO, SE EXTRAEN LOS NÚMEROS PARA POSTERIORMENTE APLICARLE COLLATS Y NÚMEROS ROMANOS


from tkinter import*
from tkinter import filedialog as fd 
from tkinter import messagebox as mb 
from tkinter import ttk
import re

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("950x900")
        self.title("Laboratorio #3 - Elmer Juarez")
        
        self.label_ruta = Label(text="--ruta--", fg="gray")
        self.label_ruta.pack()
        
        self.textbox = Text(width=50, height=20)
        self.textbox.pack()
        
        
        self.labellin = Label(text="--lineas", fg="gray")
        self.labellin.pack()
        self.labeldig = Label(text="--digitos--", fg="gray")
        self.labeldig.pack()
        self.labelnum = Label(text="--numeros--", fg="gray")
        self.labelnum.pack()
        
        encabezados = ["No.", "Número extraído", "Collatz", "Romanos", "Binarios"]
        self.tree = ttk.Treeview(height=20, columns=encabezados, show='headings')
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=250, anchor='center')
        self.tree.pack()
        
        Button(text="Crear Archivo", command=self.crear).pack(side=LEFT)
        Button(text="Abrir Archivo", command=self.abrir).pack(side=LEFT)
        Button(text="Grabar", command=self.grabar).pack(side=LEFT)
        Button(text="Analizar archivo", command=self.analizar).pack(side=LEFT)
        
        
        self.ruta = None

        self.listacolatz = []

    def crear(self): 
        try: 
            self.ruta = fd.asksaveasfilename()
            self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")
        except (FileExistsError, FileNotFoundError): 
            mb.showerror("Error", "Debe crear un archivo")
            return 
        with open(self.ruta, 'w', encoding='utf-8') as archivo: 
            archivo.write('')
            
    def abrir(self): 
        try: 
            self.ruta = fd.askopenfilename()
            self.label_ruta.config(text=f"RUTA: {self.ruta}")
        except (FileExistsError, FileNotFoundError): 
            mb.showerror("Error", "Debe abrir un archivo")
            return 
        with open(self.ruta, 'r', encoding='utf-8-sig') as archivo: 
            contenido = archivo.read()
            if contenido == "": 
                mb.showinfo("Atencion", "El archivo esta vacío")
                
            self.textbox.delete(1.0, END)
            self.textbox.insert(1.0, contenido)
    
    def grabar(self): 
        if self.ruta == None: 
            mb.showerror("Error", "Debe haber cargado un archivo antes")
            estado = mb.askyesno("Atencion", "¿Desea abrir un archivo?")
            if estado: 
                self.abrir()
            else: 
                mb.showinfo("Atencion", "No se ha abierto ningun archivo")
                return
        contenido = self.textbox.get(1.0, END)
        with open(self.ruta,'w', encoding='utf-8-sig') as archivo: 
            archivo.write(contenido)
            self.textbox.delete(1.0, END)
            mb.showinfo("Atencion", "Se ha grabado el texto")
    
    def analizar(self): 
        if self.ruta == None: 
            mb.showinfo("Error", "Debe cargar un archivo para analizar")
            estado = mb.askyesno("Atencion", "¿Desea abrir un archivo?")
            if estado: 
                self.abrir()
            else: 
                mb.showinfo("Atencion", "No se ha abierto ningun archivo")
                return
        with open(self.ruta, 'r', encoding='utf-8-sig') as archivo: 
            contenido = archivo.read()
            lineas = contenido.splitlines()
            #CONTADORES
            contdigit = 0
            contnum = 0 
            contline = 0
            lista_nums = []
            for linea in lineas: 
                contline += 1
                valores = re.findall(r"\d+", linea)
                for numero in valores: 
                    lista_nums.append(numero)
                    contnum += 1
                    self.listacolatz = []
                    resultcolt = self.collatz(int(numero))
                    resultromanos = self.fromanos(int(numero))
                    contdigit += self.contard(int(numero))
                    resultbin = self.binarios(int(numero))
                    
                    self.tree.insert("", END, values=(contnum, numero, resultcolt, resultromanos, resultbin))
            print(lista_nums)
            self.labellin.config(text=f"Número de líneas: {contline}", fg="black")
            self.labeldig.config(text=f"Número de dígitos: {contdigit}", fg="black")
            self.labelnum.config(text=f"Cantidad de números: {contnum}", fg="black")
    
    def collatz(self, num): 
        self.listacolatz.append(num)
        if num == 1: 
            return self.listacolatz
        else: 
            if num % 2 == 0: 
                return self.collatz(num//2)
            else: 
                return self.collatz((num*3)+1)
    
    def fromanos(self, num): 
        romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        decimales = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        roms = ""
        while num > 0: 
            for k in range(num//decimales[i]): 
                roms += romanos[i]
                num -= decimales[i]
            i+=1
        return roms
    
    def contard(self, num): 
        if num < 10: 
            return 1 
        else: 
            sinulti = num // 10 
            return 1 + self.contard(sinulti)
    
    def binarios(self, num): 
        if num == 0: 
            return ""
        else: 
            residuo = num % 2
            resto = num // 2
            return self.binarios(resto) + str(residuo)

app().mainloop()
