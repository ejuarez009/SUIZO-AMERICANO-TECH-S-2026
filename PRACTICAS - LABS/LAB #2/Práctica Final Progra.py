from tkinter import* 
from tkinter import filedialog as fd 
from tkinter import simpledialog as sd 
from tkinter import messagebox as mb 
from tkinter import ttk
import pickle 
import os 
from datetime import datetime

class app(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("1000x500")
        
        frame_botones = Frame(self)
        frame_botones.grid(row=0, column=0)
        Button(frame_botones,text="Crear/Abrir", command=self.crear_abrir).grid(row=0, column=0)
        Button(frame_botones, text="Consulta General", command=self.consulta).grid(row=0, column=1)
        Button(frame_botones, text="Grabar Registro", command=self.grabar).grid(row=0, column=2)
        Button(frame_botones,text="Modificar", command=self.modificar).grid(row=0, column=3)
        Button(frame_botones,text="Eliminar", command=self.eliminar).grid(row=0, column=4)
        Button(frame_botones,text="Buscar por nombre", command=self.busquedanomposi).grid(row=0, column=5)

        frame_tree = Frame(self)
        frame_tree.grid(row=1, column=1)
                
        self.label_ruta = Label(text="--ruta--")
        self.label_ruta.grid(row=1, column=0)
        
        encabezados = ["Nombre", "Posicion", "Equipo", "Fecha", "Goles", "Asistencia", "Edad"]
        self.tree = ttk.Treeview(self, height=15, columns=encabezados)
        self.tree.heading("#0", text="Correlativo")
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=2, column=0)
    
    
    def crear_abrir(self): 
        estado = mb.askyesno("Atencion", "¿Desea abrir un archivo existente?")
        if estado: 
            self.ruta = fd.askopenfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
            self.label_ruta.config(text=f"Ruta: {self.ruta}")
        else: 
            self.ruta = fd.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
            self.label_ruta.config(text=f"Ruta:{self.ruta}")
            with open(self.ruta, 'wb') as archivo: 
                archivo.write(b'')
    
    def consulta(self): 
        try: 
            with open(self.ruta,'rb') as archivo: 
                self.tree.delete(*self.tree.get_children())
                linea = 1
                while True: 
                    try: 
                        registros = pickle.load(archivo)
                        self.tree.insert("",END,text=linea, values=registros)
                        linea += 1
                    except EOFError: 
                        mb.showinfo("Atencion", "Se ha cargado todos los registros correctamente")
                        break
        except AttributeError: 
            mb.showerror("Error", "Debe cargar un archivo primero")
    
    def eliminar(self): 
        try: 
            dato = sd.askstring("Eliminacion", "Busque el correlativo del registro para elimnarlo")
            for fila in self.tree.get_children(): 
                correlativo = self.tree.item(fila)['text']
                if str(correlativo) == str(dato): 
                    self.tree.delete(fila)
            
            for fila in self.tree.get_children(): 
                with open(self.ruta,'wb') as archivo: 
                    valores = self.tree.item(fila)['values']
                    pickle.dump(valores, archivo)
            mb.showinfo("Atencion", "Se ha eliminado un registro")
            self.consulta()
        except AttributeError: 
            mb.showerror("Error", "Debe cargar un archivo primero")

    
    def grabar(self):
        root = Toplevel(self)
        root.geometry("300x300")
        
        etiquetas = ["Nombre", "Posicion", "Equipo", "Fecha", "Goles", "Asistencias","Edad"]
        objetos = {}
        for i, text in enumerate(etiquetas): 
            Label(root,text=text).grid(row=i, column=0)
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[text] = entry
        
        def cargar(): 
            datos = []
            for caja in etiquetas: 
                texto = objetos[caja].get().strip()
                if texto == "": 
                    mb.showerror("Error", "Debe Ingresar todos los datos")
                    break
                else: 
                    datos.append(texto)
            
            
            nombre = datos[0]
            posicion = datos[1]
            equipo = datos[2]
            fecha = datos[3]
            goles = datos[4]
            asistencia = datos[5]
            edad = datos[6]
            
            posiciones = ["portero", "delantero", "defensa", "central"]
            
            if not self.validfecha(fecha):
                return 

            if posicion.strip().lower() not in posiciones: 
                mb.showinfo("Atencion", "Posicion invalida")
                return

            if posicion not in posiciones: 
                mb.showinfo("Atencion", "Posicion invalida")
                return

            if int(edad) <= 15: 
                mb.showinfo("Atencion", "La edad debe ser mayor a 15")
                return 

            else: 
                datos_bien = [nombre, posicion, equipo,fecha, goles,asistencia,edad]
                try: 
                    with open(self.ruta,'ab') as archivo: 
                        pickle.dump(datos_bien, archivo)
                except AttributeError:
                    mb.showerror("Error", "Debe de cargar un archivo primero")
                    return 
                
                for entry in objetos.values(): 
                    entry.delete(0,END)
                
                mb.showinfo("Atencion", "Registro guardado correctamente")
                root.destroy()
                self.consulta()
                
        Button(root,text="Guardar Registro", command=cargar).grid(row=7, column=0)
        
    def validfecha(self,fecha): 
            try: 
                datetime.strptime(fecha,"%d/%m/%Y")
                return True
            except ValueError: 
                mb.showinfo("Atencion", "Fomato de Fecha invalida")
                return False

    def modificar(self): 
        dato = sd.askinteger("Modificacion", "Busque el dato por correlativo para la modificacion")
        
        encontrado = False
        fila_buscada = None
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)['text']
            if str(dato) == str(correlativo):
                encontrado = True
                fila_buscada = fila
                valores = self.tree.item(fila)['values']
                break
            
        if encontrado == False: 
            mb.showinfo("Atencion", "No se encontro ningun registro")
            return 
        
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Modificacion")
        
        etiquetas = ["Nombre", "Posicion", "Equipo", "Fecha", "Goles", "Asistencias","Edad"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root,text=etiqueta).grid(row=i, column=0)
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
            
        
        for i in range (0,len(etiquetas)): 
            pos_etiqueta = etiquetas[i]
            caja = objetos[pos_etiqueta]
            caja.insert(0, valores[i])
        
        def cargar(): 
            datos = []
            for entry_mod in objetos.values(): 
                datos.append(entry_mod.get())

            self.tree.item(fila_buscada, values=datos)
            try: 
                with open(self.ruta, 'wb') as archivo: 
                    for fila in self.tree.get_children(): #Recorremos cada registro en el tree
                        valores_nuevos = list(self.tree.item(fila)['values'])
                        print(valores_nuevos)
                        pickle.dump(valores_nuevos, archivo)
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado una ruta")
            
            mb.showinfo("Atencion", "Registro cargado corectamente")
            root.destroy()
            
        
        Button(root, text="Cargar registro", command=cargar).grid(row=8, column=1)
            
    
    def busquedanomposi(self):
        dato = sd.askstring("Busqueda por Nombre", "Ingrese el nombre a buscar")
        dato2 = sd.askstring("Búsqueda por posicion", "Ingrese la posicion")
        seleccion = []
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if registro[0] == str(dato) and registro[1] == str(dato2): 
                seleccion.append(fila)
                self.tree.selection_set(seleccion)
            else:
                mb.showerror("Error", "No se encontro ningun registro")
        


app().mainloop()
