from tkinter import filedialog as fd; from tkinter import simpledialog as sd; from tkinter import ttk; from tkinter import*; from tkinter import messagebox as mb
from datetime import datetime
import pickle 
import os 


class app(Tk): 
    def __init__(self):
        super().__init__()
        self.geometry("1300x600")
        self.title("Laboratorio #2 - Elmer Juarez")
        self.config(bg="skyblue")
        
        frame_tree = Frame(self, bg="skyblue")
        frame_tree.grid(row=0, column=0)
        self.label_ruta = Label(frame_tree,text="--ruta--", fg="gray", font=("arial", 14, "bold"))
        self.label_ruta.grid(row=0, column=0)
        
        encabezados = ["Nombre", "Edad", "Genero", "Enfermedad Diagnosticada", "Medico Asignado", "Fecha", "Costo", "Estado"]
        self.tree = ttk.Treeview(frame_tree, height=20, columns=encabezados)
        self.tree.heading("#0", text="Corrrelativo")
        for encabezado in encabezados:
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=110)
        self.tree.grid(row=1, column=0)        
        
        frame_button = Frame(self, bg="skyblue")
        frame_button.grid(row=1, column=0)
        Button(frame_button, text="Crear / Abrir", command=self.crear_abrir, width=30, height=2, bg="pink").grid(row=0, column=0, padx=3)
        Button(frame_button, text="Consulta General", command=self.consulta, width=30, height=2, bg="pink").grid(row=0, column=1, padx=3)
        Button(frame_button, text="Grabar", command=self.grabar, width=30, height=2, bg="lightgray").grid(row=0, column=2, padx=3)
        Button(frame_button, text="Modificar", command=self.modificar, width=30, height=2, bg="lightgray").grid(row=0, column=3, padx=3)
        Button(frame_button, text="Eliminar", command=self.eliminar, width=30, height=2, bg="lightgray").grid(row=0, column=4, padx=3)
        
        Button(frame_button, text="Buscar por nombre", command=self.buscarnom, width=30, height=2, bg="lightgreen").grid(row=1, column=1, padx=3)
        Button(frame_button, text="Buscar por medico", command=self.buscarmed, width=30, height=2, bg="lightgreen").grid(row=1, column=2, padx=3)
        Button(frame_button, text="Enfermedad y Costo", command=self.enfecosto, width=30, height=2, bg="lightgreen").grid(row=1, column=3, padx=3)

    def crear_abrir(self): 
        try: 
            estado = mb.askyesno("Atencion", "¿Desea abrir un archivo exitente?")
            if estado: 
                self.ruta = fd.askopenfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
                self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue", font=("arial", 14, "bold"))
                mb.showinfo("Atencion", "Se ha abierto un archivo")
            else: 
                self.ruta = fd.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
                self.label_ruta.config(text=f"RUTA: {self.ruta}", fg="blue", font=("arial", 14, "bold"))
                with open(self.ruta, 'wb') as archivo: 
                    archivo.write(b'')
                mb.showinfo("Atencion", "Se ha creado un archivo")
        except FileExistsError: 
            mb.showerror("Error", "No se ha abierto o creado un archivo")

    def consulta(self): 
        try: 
            self.tree.delete(*self.tree.get_children())
            with open(self.ruta,'rb') as archivo:
                correlativo = 1 
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        self.tree.insert("", END,text=str(correlativo), values=registro)
                        correlativo +=1
                    except EOFError: 
                        break
        except AttributeError: 
            mb.showerror("Error", "Debe haber cargado un archivo primero")
    
    def grabar(self): 
        root = Toplevel(self)
        root.geometry("300x300")
        root.config(bg="lightgreen")
        root.title("GRABA RREGISTRO")
        
        etiquetas = ["Nombre", "Edad", "Genero", "Enfermedad Diagnosticada", "Medico Asignado", "Fecha", "Costo", "Estado"]
        objetos = {}
        
        for i, etiqueta in enumerate(etiquetas): 
            Label(root,text=f"{etiqueta}:", font=("arial", "8", "bold"), bg="lightgreen").grid(row=i, column=0, sticky='w')
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry 
            
        
        def guardar(): 
            
            datos = []
            for tcaja in etiquetas: 
                tcaja = objetos[tcaja].get().strip() 
                if tcaja == "": 
                    mb.showerror("Error", "Debe llenar todos los campos")
                    return
                datos.append(tcaja)
            
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
            if int(edad) < 0 or int(edad) > 110:
                mb.showerror("Atencion", "La edad ingresada es invalida")
                return 
            if int(costo) < 100: 
                mb.showinfo("Atencion", "El costo es muy bajo")
                return 
            if str(estado).lower() not in ["activo", "inactivo"]: 
                mb.showerror("Error", "Estado del paciente invalido")
                return 
            
            
            print("hola")
            datos_correctos = [nombre, edad, genero, enfermedad, medico, fecha, costo, estado]
            
            try: 
                with open(self.ruta, 'ab') as archivo: 
                    pickle.dump(datos_correctos, archivo)
                mb.showinfo("Atencion", "Registro guarrdado correctamente")
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado un archivo antes")
                return
            
            self.consulta()
            
            for entry in objetos.values():
                entry.delete(0,END)
            
        Button(root, text="Guardar Registro", command=guardar, width=20, height=2).grid(row=8, column=0,pady=20)
        
    
    def validfecha(self, fecha): 
        try: 
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def modificar(self): 
        dato = sd.askstring("Modificacion","Ingrese el correlativo para modificar")
        bandera = False
        fila_objetivo = None
        valores = None
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)["text"]
            if str(correlativo) == str(dato): 
                bandera = True
                valores = self.tree.item(fila)["values"]
                fila_objetivo = fila

        if bandera == False: 
            mb.showerror("Atencion", "No se ha encontrado ese correlativo")
            return

        
        root = Toplevel(self)
        root.geometry("300x300")
        root.config(bg="pink")
        
        etiquetas = ["Nombre", "Edad", "Genero", "Enfermedad Diagnosticada", "Medico Asignado", "Fecha", "Costo", "Estado"]
        objetos = {}
        
        for i, etiqueta in enumerate(etiquetas): 
            Label(root,text=f"{etiqueta}:", font=("arial", "8", "bold"), bg="lightgreen").grid(row=i, column=0, sticky='w')
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry 
        
        for i in range(len(etiquetas)): 
            eti = etiquetas[i]
            caja = objetos[eti]
            
            if i == 5 or i ==6: 
                caja.insert(0, valores[i])
                caja.config(state="readonly")
                continue
            
            caja.insert(0,valores[i])
            
        def cargar(): 
            datos = []
            for entry in objetos.values():
                datos.append(entry.get())
                
            self.tree.item(fila_objetivo, values=datos)
            try: 
                with open(self.ruta, 'wb') as archivo: 
                    for fila in self.tree.get_children(): 
                        vals_nuevos = self.tree.item(fila)["values"]
                        pickle.dump(vals_nuevos, archivo)
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado un arhivo primero")
                return 

            mb.showinfo("Atencion", "Se ha modificado un registro")
            root.destroy()
            self.consulta()
        Button(root,text="Modificar Registro", command=cargar).grid(row=i+1, column=0)
        
        
    def eliminar(self): 
        try: 
            dato = sd.askinteger("Eliminacion", "Ingrese el correlativo a eliminar")
            bandera = False
            for fila in self.tree.get_children(): 
                correlativo = self.tree.item(fila)['text']
                if str(dato) == str(correlativo): 
                    self.tree.delete(fila)
                    bandera = True
                
            if bandera == False: 
                mb.showinfo("Atencion", "No se ha encontrado ese correlativo")
                return 
            
            with open(self.ruta, 'wb') as archivo: 
                for fila in self.tree.get_children(): 
                    registro = self.tree.item(fila)['values']
                    pickle.dump(registro, archivo)
                    mb.showinfo("Atencion", "Se ha eliminado un registro")
            self.consulta()
        except (AttributeError, FileNotFoundError): 
            mb.showerror("Error", "Debe haber cargado un archivo")
            
                
    
    
    def buscarnom(self): 
        dato = sd.askstring("Busqueda por nombre", "Ingrese el nombre a buscar:")
        seleccionados = []
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if str(registro[0]) == str(dato): 
                seleccionados.append(fila)
                self.tree.selection_set(seleccionados)
            else: 
                mb.showinfo("Error", "No se encontro ese registro")
    
    def buscarmed(self):
        dato = sd.askstring("Busqueda por medico", "Ingrese el nombre del medico a buscar:")
        seleccionados = []
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if str(registro[4]) == str(dato): 
                seleccionados.append(fila)
                self.tree.selection_set(seleccionados)
            else: 
                mb.showinfo("Error", "No se encontro ese registro")
    
    def enfecosto(self): 
        pass
    
app().mainloop()
