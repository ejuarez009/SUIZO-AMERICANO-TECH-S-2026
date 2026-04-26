#==================DOCUMENTACION INTERNA==========================
# AUTOR: ELMER JUAREZ 
# FECHA: 23/03/2026
# DESCRIPCION: RESOLVER LA PRUEBA PARCIAL INFORME 1-2
# LENGUAJE: PYTHON3
# HERRAMIENTAS: Librería de tkinter, modulos de tkinter, pickle y os.path
# PROCESOS PENDIENTES: NINGUNO

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk 
import pickle 
import os 

class Escuela(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("1000x750")
        self.title("Elmer Juarez")
        self.ruta = None

        #==========================OBJETO TREEVIEW========================
        Label(self, text="Datos a grabar").pack()
        
        self.textbox = Text(self, width=50, height=5)
        self.textbox.pack()
        
        self.label_ruta = Label(self, text="--ruta--", fg="gray")
        self.label_ruta.pack(pady=20)
        
        encabezados = ["Carnet", "Nombre", "Apellido", "Carrera", "Seccion", "Año"]
        self.tree = ttk.Treeview(self, height=20, columns=encabezados, show='headings')
        for columna in encabezados: 
            self.tree.heading(columna, text=columna)
            self.tree.column(columna, width=150)
        self.tree.pack(padx=20)

        #==========================BOTONES=================================
        Button(self, text="Crear archivo", command=self.crear).pack(side=LEFT, padx=5)
        Button(self, text="Abrir archivo", command=self.abrir).pack(side=LEFT, padx=5)
        Button(self, text="Grabar archivo", command=self.grabar).pack(side=LEFT, padx=5)
        Button(self, text="Consulta general", command=self.consulta_ge).pack(side=LEFT, padx=5)
        Button(self, text="Nuevo Registro", command=self.registro).pack(side=LEFT, padx=5)
        Button(self, text="Consulta por seccion y carrera", command=self.consulta_sec_carre).pack(side=LEFT, padx=5)
        
    #==========================ARCHIVO=================================
    def crear(self): 
        self.ruta = fd.asksaveasfilename(defaultextension=".bin")
        if not self.ruta: 
            mb.showinfo("ATENCION", "NO SE HA CREADO NINGUN ARCHIVO")
            return
        
        self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")  
        if not os.path.exists(self.ruta): 
            with open(self.ruta, 'wb') as archiv: 
                pass
            mb.showinfo("ATENCION", "Archivo creado correctamente")

    def abrir(self): 
        self.ruta = fd.askopenfilename(filetypes=[("Archivo binario", "*.bin")])
        if not self.ruta: 
            mb.showinfo("ATENCION", "NO SE SELECCIONO ARCHIVO")
            return
        
        self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")  
        with open(self.ruta, 'rb') as archiv: 
            self.textbox.delete(0, END)
            contenido = archiv.read()
            self.textbox.insert(END,contenido)
        mb.showinfo("ATENCION", "Archivo abierto correctamente")
    
    def grabar(self): 
        if not self.ruta: 
            mb.showerror("ERROR", "DEBE ABRIR O CREAR UN ARCHIVO PARA GRABAR DATOS")
        
        self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")  
        with open(self.ruta, 'ab') as archiv: 
            contenido = self.textbox.get("1.0",END)
            pickle.dump(contenido, archiv)
            self.textbox.delete(0,END)
        mb.showinfo("ATENCION", "Se ha abierto un archivo binario")

    #==========================CONSULTA GENERAL========================
    def consulta_ge(self): 
        if not self.ruta:
            mb.showwarning("CUIDADO", "Debe abrir un archivo primero")
            return
        
        self.tree.delete(*self.tree.get_children())

        try:
            self.ruta = fd.askopenfilename(defaultextension='.bin')
            maxi = os.path.getsize(self.ruta)
            with open(self.ruta, 'rb') as archiv: 
                pos = 0 
                while pos < maxi: 
                    datos = pickle.load(archiv)
                    self.tree.insert("", END, values=datos)
                    pos = archiv.tell()
            mb.showinfo("ATENCION", "Consulta general realizada")
        except Exception as e:
            mb.showerror("ERROR", str(e))

    #==========================REGISTRO=================================
    def registro(self): 
        root = Toplevel(self)
        root.geometry("400x400")
        root.title("NUEVO REGISTRO")
        
        labels = ["Carnet", "Nombre", "Apellido", "Carrera", "Seccion", "Año"]
        self.campos = {}

        for i, label in enumerate(labels): 
            Label(root, text=label).grid(row=i, column=0, pady=5)
            entry = Entry(root, width=20)
            entry.grid(row=i, column=1)
            self.campos[label] = entry
            
        Button(root, text="Guardar", command=self.salvar_registro).grid(row=len(labels), column=0, columnspan=2, pady=20)

    def salvar_registro(self): 
        if not self.ruta:
            mb.showwarning("CUIDADO", "Debe abrir o crear un archivo")
            return
        
        datos = []
        for entry in self.campos.values(): #extramos la info de los entrys
            datos.append(entry.get()) #se mete toda la info de los entrys en una lista
        
        try: 
            carne = int(datos[0])
            nombre = str(datos[1]) #MARDOOO NO SE COMO PONER EL TIPO DE DATO DOUBLE 
            apellido = str(datos[2])
            carrera = str(datos[3])
            seccion = str(datos[4])
            año = int(datos[5])
            
            datos_bien = [carne, nombre, apellido, carrera, seccion, año]
            
            with open(self.ruta, 'ab') as archiv: 
                pickle.dump(datos_bien, archiv)
                
            mb.showinfo("ATENCION", "Registro guardado")
            
            for entry in self.campos.values(): 
                entry.delete(0, END)
                
        except ValueError: 
            mb.showerror("ERROR", "Datos invalidos")

    #==========================CONSULTA FILTRADA========================
    def consulta_sec_carre(self): 
        root2 = Toplevel(self)
        root2.geometry("300x300")
        root2.title("BUSCAR")

        Label(root2, text="Seccion:").pack()
        entry_sec = Entry(root2)
        entry_sec.pack()

        Label(root2, text="Carrera:").pack()
        entry_carre = Entry(root2)
        entry_carre.pack()
        
        def buscar(): 
            if not self.ruta:
                mb.showwarning("CUIDADO", "Debe abrir archivo")
                return
            
            seccion = entry_sec.get().strip()
            carrera = entry_carre.get().strip()
            
            self.tree.delete(*self.tree.get_children())
            
            try:
                maxi = os.path.getsize(self.ruta)
                with open(self.ruta, 'rb') as archiv:
                    pos = 0
                    encontradito = False
                    
                    while pos < maxi:
                        datos = pickle.load(archiv)

                        if datos[3] == carrera and datos[4] == seccion:
                            self.tree.insert("", END, values=datos)
                            encontradito = True
                            
                        pos = archiv.tell()
                        
                if not encontradito:
                    mb.showinfo("RESULTADO", "No hay coincidencias")
                    
            except Exception as e:
                mb.showerror("ERROR", str(e))
                
        Button(root2, text="Buscar", command=buscar).pack(pady=10)
        
Escuela().mainloop()