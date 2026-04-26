from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb; from tkinter import ttk
from tkinter import simpledialog as sd 
import os 
import pickle
from datetime import datetime

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("1100x500")
        self.title("Futbol")
        
        frame_botones = Frame(self)
        frame_botones.grid(row=1, column=0)
        Button(frame_botones,text="Crear/Abrir", command=self.crear_abrir).grid(row=0, column=0)
        Button(frame_botones,text="grabar", command=self.grabar).grid(row=0, column=1)
        Button(frame_botones,text="Consulta General", command=self.consulta).grid(row=0, column=2)
        Button(frame_botones,text="Modificar",command=self.modificar).grid(row=0, column=3)
        Button(frame_botones,text="Eliminar", command=self.eliminar).grid(row=0, column=4)
        Button(frame_botones,text="Buscar Posicion y Equipo", command=self.buscarposiequi).grid(row=0, column=5)
        
        encabezados = ["Nombre", "Equipo", "Posicion", "Fecha", "Edad", "Goles", "Asistencias"]
        frame_tree = Frame(self)
        frame_tree.grid(row=2, column=0)
        self.label_ruta = Label(text="--ruta--",fg="gray")
        self.label_ruta.grid(row=0, column=0)
        self.tree = ttk.Treeview(frame_tree, height=20,columns=encabezados)
        self.tree.heading("#0",text="Correlativo")
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=1, column=0, padx=20)

    def crear_abrir(self): 
        estado = mb.askyesno("Atencion", "¿Desea abrir un archivo existente?")
        try: 
            if estado: 
                self.ruta = fd.askopenfilename()
                self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")
            else: 
                self.ruta = fd.asksaveasfilename()
                self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue")
                with open(self.ruta, 'wb') as archivo: 
                    archivo.write(b'')
        except FileNotFoundError: 
            mb.showerror("Error", "Atencion no se ha creado un archivo")

    #============================================= Grabar Datos ===================================================
    def grabar(self): 
        ventana_grabar = Toplevel(self)
        ventana_grabar.geometry("300x300")
        
        etiquetas = ["Nombre", "Equipo", "Posicion", "Fecha", "Edad", "Goles", "Asistencias"]
        widgets = {}
        for i, text in enumerate(etiquetas): 
            Label(ventana_grabar, text=text).grid(row=i, column=0)
            
            entry = Entry(ventana_grabar)
            entry.grid(row=i, column=1)
            
            widgets[text]= entry
            
        
        def cargar():
            datos = []
            for entry in widgets.values():
                if entry == "" : 
                    mb.showerror("Erro", "Debe ingresar datos validos")
                else: 
                    datos.append(entry.get())

            nombre = datos[0]
            equipo = datos[1]
            posicion = datos[2]
            fecha = datos[3]
            edad = datos[4]
            goles = datos[5]
            asistencias = datos[6]
            
            posiciones = ["central", "delantero", "portero", "defensa"]
            
            if not self.validfecha(fecha): 
                return 
            
            if posicion.strip().lower() not in posiciones: 
                mb.showinfo("Cuidado", "Posicion invalida")
                return
            
            if int(edad) <= 15: 
                mb.showinfo("Cuidado", "Edad inválida")
                
            datos_tree = [nombre, equipo, posicion, fecha, edad, goles, asistencias]
            try: 
                with open (self.ruta, 'ab') as archivo: 
                    pickle.dump(datos_tree, archivo)
            except AttributeError: 
                mb.showerror("Error", "Debe Cargar un archivo primero")
                return

            for entry in widgets.values(): 
                entry.delete(0,END)
                
            mb.showinfo("Exito", "Registro Guardado exitosamente")
            
        
        Button(ventana_grabar, text="Cargar registro", command=cargar).grid(row=8, column=0)

    def validfecha(self, fecha): 
        try: 
            datetime.strptime(fecha,"%d/%m/%Y")
            return True
        except ValueError: 
            mb.showerror("Error", "Formato de fecha invalida")
            return False


#========================================== Consultas =========================================
    def consulta(self): 
        try:
            self.tree.delete(*self.tree.get_children())
            with open(self.ruta, 'rb') as archivo:                  
                linea = 1 
                while True: 
                    try: 
                        datos = pickle.load(archivo)
                        self.tree.insert("", END,text=str(linea), values=datos)
                        linea += 1
                    except EOFError: 
                        break
        except FileNotFoundError: 
            mb.showerror("Error", "Debe abrir o crear un archivo primero")
    
    def modificar(self): 
        dcorrelativo = sd.askinteger("Modificar", "Buscar por correlativo")
        if dcorrelativo is None:
            return

        fila_objetivo = None
        valores = None
        for fila in self.tree.get_children():
            correlativo = self.tree.item(fila)["text"]
            if str(dcorrelativo) == str(correlativo):
                fila_objetivo = fila
                valores = self.tree.item(fila)["values"]
                break

        if fila_objetivo is None:
            mb.showinfo("Modificar", "No se encontro el correlativo en la tabla")
            return

        vmodificar = Toplevel(self)
        vmodificar.geometry("320x240")

        etiquetas = ["Nombre", "Equipo", "Posicion", "Fecha", "Edad", "Goles", "Asistencias"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas):
            Label(vmodificar, text=etiqueta).grid(row=i, column=0)
            entry = Entry(vmodificar)
            entry.grid(row=i, column=1)
            objetos[etiqueta] = entry

        for i in range(len(etiquetas)):
            etiqueta_actual = etiquetas[i]
            objetos[etiqueta_actual].insert(0, valores[i])
                
                
        def guardar_cambios():
            datos = []
            for entry in objetos.values():
                datos.append(entry.get())

            # Actualizar tabla en memoria
            self.tree.item(fila_objetivo, values=datos)
            # Reescribir archivo completo con lo que hay en la tabla
            try:
                with open(self.ruta, "wb") as archivo:
                    for fila in self.tree.get_children():
                        valos = list(self.tree.item(fila)["values"])
                        pickle.dump(valos, archivo)
            except AttributeError:
                mb.showerror("Error", "Primero abra o cree un archivo")
                return

            mb.showinfo("Exito", "Registro modificado")
            vmodificar.destroy()

        Button(vmodificar, text="Guardar cambios", command=guardar_cambios).grid(row=8, column=0, columnspan=2, pady=8)

    def eliminar(self): 
        try: 
            dato = sd.askstring("Eliminacion", "Ingrese el correlativo del registro a eliminar")
            for fila in self.tree.get_children(): 
                correlativo = self.tree.item(fila)['text']
                if str(dato) == correlativo: 
                    self.tree.delete(fila)
                
            for fila in self.tree.get_children():
                valores = self.tree.item(fila)['values']
                with open(self.ruta, 'ab') as archivo: 
                    pickle.dump(valores, archivo)
        except AttributeError: 
            mb.showerror("Error", "No ha enrutado nada")
    
    
    def buscarposiequi(self): 
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Buscar Posicion")
        
        Label(root,text="Ingresar posicion").grid(row=0, column=0)
        entry_pos = Entry(root)
        entry_pos.grid(row=0, column=1)
        
        Label(root,text="Ingresar equipo").grid(row=1, column=0)
        entry_equi = Entry(root)
        entry_equi.grid(row=1, column=1)
        def buscar(): 
            try: 
                equipo = entry_equi.get().strip().lower()
                posicion = entry_pos.get().strip().lower()
                if not equipo or not posicion:
                    mb.showinfo("Atencion", "Ingrese equipo y posicion")
                    return

                bandera = False
                self.tree.delete(*self.tree.get_children())
                linea = 1
                with open(self.ruta, 'rb') as archivo:
                    while True: 
                        try: 
                            registros = pickle.load(archivo)
                            reg_equipo = str(registros[1]).strip().lower()
                            reg_posicion = str(registros[2]).strip().lower()
                            if equipo == reg_equipo and posicion == reg_posicion:
                                self.tree.insert("", END, text=str(linea), values=registros)
                                linea += 1
                                bandera = True
                        except EOFError: 
                            break 
                if not bandera: 
                    mb.showinfo("Atencion","No se ha encontrado ningun registro")
            except AttributeError: 
                mb.showerror("Atencion", "Debe cargar un archivo")
        Button(root, text="Buscar", command=buscar).grid(row=3, column=1)
        
app().mainloop()