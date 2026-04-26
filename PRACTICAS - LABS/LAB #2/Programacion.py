from tkinter import *; from tkinter import filedialog as fd; from tkinter import messagebox as mb; from tkinter import ttk; from tkinter import simpledialog as sd 
import pickle
import os
from datetime import datetime


class app(Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("1200x600")
        self.title("PRACTICA")
        
        
        self.label_ruta = Label(text="--RUTA--",foreground="blue")
        self.label_ruta.grid(row=0, column=0)
        
        #BOTONES 
        frame_button = Frame(self)
        frame_button.grid(row=1, column=0)
        
        Button(frame_button,text="Crear/Abrir Archivo", command=self.crear_abrir).grid(row=0, column=0)
        Button(frame_button,text="Grabar nuevo registro", command=self.nuevo_registro).grid(row=0, column=1)
        Button(frame_button, text="Consulta general", command=self.consulta_general).grid(row=0, column=3)
        
        self.label_correlativo = Label(frame_button, text="--correlativos--", fg="gray")
        self.label_correlativo.grid(row=1, column=0)
        
        
        #TREEVIEW
        frame_tree = Frame(self)
        frame_tree.grid(row=2,column=0)
        encabezados = ["Nombre", "Genero", "Playlist", "Fecha", "Duracion", "Interprete", "Frecuencia", "Calificacion"]
        self.tree = ttk.Treeview(frame_tree,height=20, columns=encabezados)
        self.tree.heading("#0", text="CORRELATIVO")
        for encabezado in encabezados: 
            self.tree.heading(encabezado,text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=0, column=0, padx=20)
    
    def crear_abrir(self):
        estado = mb.askyesno("ATENCION", "¿Desea abrir un archivo existente?")
        if estado: 
            self.ruta = fd.askopenfilename()
            self.label_ruta.config(text=self.ruta)
            correlativo = str(self.correlativo()+1)
            self.label_correlativo.config(text=f"CORRELATIVOS: {correlativo}", fg="red")
        else: 
            try: 
                self.ruta = fd.asksaveasfilename()
                self.label_ruta.config(text=self.ruta)
                self.label_correlativo.config(text=f"CORRELATIVOS: {str(self.correlativo()+1)}", fg="red")
                with open(self.ruta, 'wb') as archivo: 
                    archivo.write(b"") #CREAMOS UN ARCHIVO BINARIO VACIO
            except FileNotFoundError: 
                mb.showerror("ERROR", "No se ha creado ningun archivo")
    
    
    def correlativo(self): 
        try: 
            with open(self.ruta, 'rb') as archivo: 
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        
                    except EOFError: 
                        break
                return registro[0]
        except AttributeError: 
            mb.showerror("ERROR", "No se ha seleccionado un archivo")
    
    def nuevo_registro(self):
        try:
            global root2
            root2 = Toplevel(self)
            root2.geometry("500x500")
            root2.title("Grabar registro")
            
            labels = ["Nombre", "Género", "Fecha", "Duracion", "Interprete", "Frecuencia"]
            
            self.campos = {}
            
            for i, text in enumerate(labels): 
                Label(root2,text=text).grid(row=i, column=0)
                
                entry = Entry(root2,width=20)
                entry.grid(row=i, column=1)
                self.campos[text] = entry
            
            
            Button(root2,text="Grabar Datos", command=self.grabar).grid(row=7, column=0)
            
        except FileNotFoundError:
            mb.showerror("ERROR", "NO SE HA GRABADO NADA")
    
    
    def grabar(self): 
        
        datos = []
        for entry in self.campos.values(): ##RECORREMOS CADA ENTRY 
            datos.append(entry.get())
        
        nombre = datos[0]
        genero = datos[1]
        fecha = datos[2]
        duracion = datos[3]
        interprete = datos[4]
        frecuencia = int(datos[5])
        generos = ["rock", "reggaeton", "instrumental", "electronica", "pop"]
        
        
        if self.validfecha(fecha) and self.validduracion(duracion) and (genero.lower() in generos) and (frecuencia>0 and frecuencia<26): 
            playlist = ""
            calificacion = frecuencia // 5 + 1
            match genero: 
                case "rock": 
                    playlist = "exitos de rock"
                case "pop": 
                    playlist = "exitos de pop"
                case "instrumental": 
                    playlist = "exitos de instrumental"
                case "reggaeton": 
                    playlist = "exitos de reggaeton"
                case "electronica": 
                    playlist = "exitos de electronica"
            
            datos = [nombre, genero,playlist, fecha, duracion, interprete,frecuencia, calificacion]
            
            with open(self.ruta, 'ab') as archivo: 
                pickle.dump(datos, archivo)
            mb.showinfo("Atencion","Archivo guardado exitosamente")

            for entry in self.campos.values(): ##RECORREMOS CADA ENTRY 
                entry.delete(0,END)
        else: 
            mb.showerror("ERROR", "Debe ingresar datos válidos")
            root2.destrony()

            
        
    def validfecha(self, fecha): 
        try: 
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError: 
            mb.showinfo("ATENCION","Ingrese un formato adecuado para la fecha")
            return False
    
    def validduracion(self, duracion): 
        try: 
            datetime.strptime(duracion,"%M:%S")
            return True
        except ValueError: 
            mb.showinfo("ATENCION","Ingrese un formato adecuado para la duracion")
            return False
        
    
    def modificar(self): 
        try: 
            dato = sd.askstring("ATENCION", "Ingrese el datos a Buscar")
            with open(self.ruta, 'rb') as archivo: 
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        if registro[0] == dato:
                            root3 = Toplevel()
                            Label(root3, text="CORRELATIVO")
                            entry_corre = Entry(root3, width=10)
                            entry_corre.pack()
                            entry_corre.insert(END, str(self.correlativo()))
                            labels = ["Nombre", "Genero", "Fecha", "Duracion", "Interprete", "Frecuencia"]
                            
                            
                            
                    except EOFError:
                        mb.showinfo("Se ha modificado un archivo")
        except AttributeError: 
            pass
    
    def actualizar(self): 
        pass
            
    def consulta_general(self): 
        try: 
            with open(self.ruta, "rb") as archivo: 
                self.tree.delete(*self.tree.get_children()) #Limpiamos el treeview antes de agregar data
                while True: 
                    try: 
                        datos = pickle.load(archivo)
                        self.tree.insert("", END, text=self.correlativo()+2, values=datos)
                    
                    except EOFError: 
                        break
                    
        except AttributeError:
            mb.showerror("ERROR", "Debe seleccionar un archivo primero")
    
    def buscar(self): 
        root3 = Toplevel(self)
        root3.geometry("300x300")
        root3.title("Consultas Individuales")
        
        dato = sd.askstring("Busqueda", "Ingrese el nombre del interprete a buscar")

        Button(text="Buscar por correlativo", command=bcorrelativo)
        
        def bcorrelativo(dato): 
            with open(self.ruta,'rb') as archivo:
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        if registro[0] == dato:
                            self.tree.insert("")
                    except EOFError: 
                        break

#RUTINAS DE BÚSQUEDA
# while True: 
#     try: 
#         registro = pickle.load()
#     except EOFError: 
#         break



app().mainloop()