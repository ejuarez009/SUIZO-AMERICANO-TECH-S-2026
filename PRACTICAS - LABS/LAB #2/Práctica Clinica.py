from tkinter import filedialog as fd; from tkinter import simpledialog as sd; from tkinter import messagebox as mb 
from tkinter import *; from tkinter import ttk
import pickle 
import os 
from datetime import datetime

class app(Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("1300x600")
        self.title("Laboratorio #2 - Elmer Juarez C5")
        
        frame_botones = Frame(self)
        frame_botones.grid(row=0, column=0)
        
        Button(frame_botones, text="Crear/Abrir", command=self.crear_abrir).grid(row=0, column=0)
        Button(frame_botones, text="Consulta General", command=self.consulta).grid(row=0, column=1)
        Button(frame_botones, text="Grabar",command=self.grabar).grid(row=0, column=2)
        Button(frame_botones,text="Modificar", command=self.modificar).grid(row=0, column=3)
        Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=4)
        Button(frame_botones, text="Busqueda por nombre", command=self.buscn).grid(row=0, column=5)
        Button(frame_botones, text="Busqueda por medico", command=self.buscmed).grid(row=0, column=6)
        Button(frame_botones, text="Busqueda por enfermedad y costo", command=self.enfecosto).grid(row=0, column=7)
        
        frame_tree = Frame(self)
        frame_tree.grid(row=1, column=0)
        self.label_ruta = Label(frame_tree,text="--ruta--", fg="gray")
        self.label_ruta.grid(row=0, column=0)
        encabezados = ["Nombre", "Edad", "Genero","Enfermedad Diagnosticada", "Medico asignado", "Fecha", "Costo", "Estado"]
        
        self.tree = ttk.Treeview(frame_tree, height=20, columns=encabezados)
        self.tree.heading("#0", text="Correlativo")
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=1, column=0)
    
    def crear_abrir(self): 
        estado = mb.askyesno("Atencion", "¿Desea abrir un archivo existente?")
        if estado: 
            self.ruta = fd.askopenfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
            self.label_ruta.config(text=self.ruta,fg="blue")
        else: 
            self.ruta = fd.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
            self.label_ruta.config(text=self.ruta,fg="blue")
            with open(self.ruta, 'wb') as archivo: 
                archivo.write(b'')
    
    def consulta(self):
        try: 
            self.tree.delete(*self.tree.get_children())
            with open(self.ruta, 'rb') as archivo: 
                linea = 1
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        self.tree.insert("", END,text=str(linea), values=(registro))
                        linea+=1
                    except EOFError: 
                        mb.showinfo("Atencion", "Se han cargado los registros")
                        break
        except AttributeError: 
            mb.showerror("Error", "Debe cargar un archivo")
            

    def grabar(self): 
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Grabacion de Registros")
        
        etiquetas = ["Nombre", "Edad", "Genero", "Enfermedad Diagnosticada", "Medico asignado", "Fecha", "Costo", "Estado"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root, text=etiqueta).grid(row=i, column=0)
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
        
        def cargar(): 
            datos = []
            for caja in etiquetas: 
                caja = objetos[caja].get().strip()
                if caja == "": 
                    mb.showerror("Error", "Se debe de ingresar todos los campos")
                    break
                else: 
                    datos.append(caja)
            
            print(datos)
            nombre = datos[0]
            edad = datos[1] 
            genero = datos[2]
            enfermedad = datos[3]
            medico = datos[4]
            fecha = datos[5]
            costo = datos[6]
            estado = datos[7]
            
            if not self.validfecha(fecha): 
                return 
            
            if int(edad) < 0 and int(edad) >100: 
                mb.showerror("Error", "Edad Invalida")
                return 
            
            if int(costo) < 100: 
                mb.showinfo("Atencion", "El costo debe ser mayor a 100")
                return 
            
            
            datos_bien = [nombre, edad, genero, enfermedad, medico, fecha,costo, estado]
            try: 
                with open(self.ruta, 'ab') as archivo: 
                    pickle.dump(datos_bien, archivo)
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado un archivo")
                return 
            
            for entry in objetos.values(): 
                entry.delete(0, END)

            self.consulta()
        Button(root,text="Guardar Registro", command=cargar).grid(row=8, column=0)
        

            
    def validfecha(self, fecha): 
        try: 
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except: 
            mb.showerror("Error", "Formato de fecha invalida")
            return False
    
    def modificar(self): 
        dato = sd.askinteger("Modificacion", "Ingrese el correlativo para la modificacion")
        
        fila_buscada = None
        valores = None
        bandera = False
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)["text"]
            if str(dato) != correlativo: 
                mb.showinfo("Atencion", "No hay ningun registro con es correlativo")
                break
            else: 
                fila_buscada = fila 
                valores = self.tree.item(fila)["values"]
                bandera = True
                
        if bandera == False: 
            return
        
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Modificacion")
        
        etiquetas = ["Nombre", "Edad", "Genero", "Enfermedad Diagnosticada", "Medico asignado", "Fecha", "Costo", "Estado"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root, text=etiqueta).grid(row=i, column=0)
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
        
        for i in range(0,len(etiquetas)): 
            etiq = etiquetas[i]
            caja = objetos[etiq]
    
            if i == 5 or i == 6: 
                caja.insert(0, valores[i])
                caja.config(state="readonly")  # ← esto los bloquea
                continue
            caja.insert(0, valores[i])
            
            def cargar(): 
                datos = []
                for entry in objetos.values(): 
                    datos.append(entry.get())
                
                self.tree.item(fila_buscada, values=datos)
                try: 
                    with open(self.ruta, 'wb') as archivo: 
                        for fila in self.tree.get_children(): 
                            vals_nuevos = self.tree.item(fila)["values"]
                            pickle.dump(vals_nuevos, archivo)
                except AttributeError: 
                    mb.showerror("Atencion", "Debe haber cargado un archivo")
                
                mb.showinfo("Atencion", "Registro modificado correctamente")
                root.destroy()
            Button(root,text="Modificar registro", command=cargar).grid(row=8, column=0)
    
    def eliminar(self): 
        try: 
            dato = sd.askinteger("Eliminacion", "Ingrese el correlativo del registro a eliminar")
            for fila in self.tree.get_children(): 
                correlativo = self.tree.item(fila)["text"]
                if correlativo == str(dato): 
                    self.tree.delete(fila)
                    
            with open(self.ruta, 'wb') as archivo: 
                for fila in self.tree.get_children():
                    registro = self.tree.item(fila)["values"]
                    pickle.dump(registro, archivo)
                    
                mb.showinfo("Eliminacion", "Se ha eliminado un registro")
        except AttributeError: 
            mb.showerror("Error", "Debe seleccion y haber cargado un archivo")

    def buscn(self): 
        dato = sd.askstring("Busqueda por nombre", "Ingrese el nombre del paciente") 
        seleccionados = []
        for fila in self.tree.get_children(): 
            registros = self.tree.item(fila)["values"] 
            if str(dato) == registros[0]: 
                seleccionados.append(fila) 
                self.tree.selection_set(seleccionados)
            else: 
                mb.showinfo("Atencion", "No se encontro ningun registro")
    
    def buscmed(self): 
        dato = sd.askstring("Busqueda por nombre", "Ingrese el nombre del medico") 
        seleccionados = []
        for fila in self.tree.get_children(): 
            registros = self.tree.item(fila)["values"] 
            if str(dato) == registros[4]: 
                seleccionados.append(fila) 
                self.tree.selection_set(seleccionados)
            else: 
                mb.showinfo("Atencion", "No se encontro ningun registro")
    
    def enfecosto(self): 
        dato1 = sd.askstring("Busqueda por nombre", "Ingrese la enfermedad")
        dato2 = sd.askstring("Busqueda por medico", "Ingrese el costo") 
        seleccionados = []
        for fila in self.tree.get_children(): 
            registros = self.tree.item(fila)["values"] 
            if str(dato1) == registros[3] and str(dato2) == registros[4]: 
                seleccionados.append(fila) 
                self.tree.selection_set(seleccionados)
            else: 
                mb.showinfo("Atencion", "No se encontro ningun registro")
    
app().mainloop()