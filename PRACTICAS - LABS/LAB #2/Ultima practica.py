from tkinter import filedialog as fd; from tkinter import simpledialog as sd; from tkinter import* 
from tkinter import ttk; from tkinter import messagebox as mb 
import pickle
from datetime import datetime

class app(Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("1200x600")
        self.title("Laboratorio #2 - Elmer Juarez C5")

        frame_button = Frame(self)
        frame_button.grid(row=1, column=0)
        Button(frame_button, text="Crear_abrir", command=self.crear_abrir, width=20, height=2, bg="pink").grid(row=0, column=1)
        Button(frame_button, text="Consulta general", command=self.consulta, width=20, height=2, bg="pink").grid(row=0, column=2)
        Button(frame_button, text="Grabar", command=self.grabar, width=20, height=2, bg="pink").grid(row=0, column=3)
        Button(frame_button, text="Modificar", command=self.modificar, width=20, height=2, bg="lightyellow").grid(row=0, column=4)
        Button(frame_button, text="Eliminar", command=self.eliminar, width=20, height=2, bg="lightyellow").grid(row=0, column=5)
        
        Button(frame_button, text="Busqueda por nombre", command=self.buscnom, width=20, height=2, bg="lightgreen").grid(row=1, column=2)
        Button(frame_button, text="Busqueda por plataforma", command=self.buscplat, width=20, height=2, bg="lightgreen").grid(row=1, column=3)
        Button(frame_button, text="Busqueda por genero y \n calificacion", command=self.bcombinada, width=20, height=2, bg="lightgreen").grid(row=1, column=4)
        
        
        fram_tree = Frame(self)
        fram_tree.grid(row=0, column=0)
        
        self.label_ruta = Label(fram_tree,text="--ruta--", font=("arial", 12, "bold"))
        self.label_ruta.grid(row=0, column=0)
        
        encabezados = ["Nombre del videojuego", "Plataforma", "Genero", "Precio", "Stock", "Fecha de Lanzamiento", "Calificacion"]
        self.tree = ttk.Treeview(fram_tree, height=20, columns=encabezados)
        self.tree.heading("#0", text="Correlativo")
        for encabezado in encabezados: 
            self.tree.heading(encabezado, text=encabezado)
            self.tree.column(encabezado, width=120)
        self.tree.grid(row=1, column=0)
        
    def crear_abrir(self): 
        try: 
            estado = mb.askyesno("Atencion", "¿Desea abrir un archivo existente?")
            if estado: 
                self.ruta = fd.askopenfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
                self.label_ruta.config(text=f"RUTA{self.ruta}",font=("arial", 12, "bold"), fg="blue")
            else: 
                self.ruta = fd.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivo Binario", "*.bin")])
                self.label_ruta.config(text=f"RUTA{self.ruta}",font=("arial", 12, "bold"), fg="blue")
                with open(self.ruta, 'wb') as archivo: 
                    archivo.write(b'')
        except (AttributeError, FileExistsError, FileNotFoundError): 
            mb.showerror("Error", "Debe seleccionar o crear algun archivo")
    
    def consulta(self): 
        try: 
            self.tree.delete(*self.tree.get_children())
            with open(self.ruta,'rb') as archivo: 
                correlativo = 1
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        self.tree.insert("", END, text=str(correlativo), values=registro)
                        correlativo += 1
                    except EOFError: 
                        mb.showinfo("Atencion", "Se han cargado los registros")
                        break
        except AttributeError: 
            mb.showerror("Error", "Debe haber cargado un archivo primero")
    
    
    def grabar(self): 
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Grabacion de Registro")
        
        etiquetas = ["Nombre del videojuego", "Plataforma", "Genero", "Precio", "Stock", "Fecha de Lanzamiento", "Calificacion"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root, text=etiqueta, font=("arial", 10, "bold")).grid(row=i, column=0, sticky='w')
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
        
        def cargar(): 
            datos = []
            for tcaja in etiquetas: 
                tcaja = objetos[tcaja].get().strip()
                if tcaja == "": 
                    mb.showerror("Error","Debe completar todos los campos")
                    return 
                datos.append(tcaja)
            
            nombre = datos[0]
            plataforma = datos[1]
            genero = datos[2]
            precio = datos[3]
            stock = datos[4]
            fecha = datos[5]
            calificacion = datos[6]
            
            if int(precio) < 0: 
                mb.showerror("Error", "Debe ingresar un precio valido")
                return 
            if int(stock) <=0: 
                mb.showinfo("Atencion", "Revise la mercancía")
                return 
            if not self.validfecha(fecha): 
                return
            
            datos_bien = [nombre, plataforma, genero, precio, stock, fecha, calificacion]
            try: 
                with open(self.ruta, 'ab') as archivo: 
                    pickle.dump(datos_bien, archivo)
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado un archivo primero")
                return 
            
            self.consulta()
            
            for entry in objetos.values(): 
                entry.delete(0, END)
                
            
        Button(root, text="Guardar registro", command=cargar).grid(row=8, column=0)

    def validfecha(self, fecha): 
        try: 
            datetime.strptime(fecha,"%d/%m/%Y")
            return True
        except ValueError: 
            return False
    
    def modificar(self): 
        dato = sd.askinteger("Modificacion", "Ingrese el correlativo del registro \n para modificarlo")
        
        bandera = False
        fila_objetivo = None
        valores = None 
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)['text']
            if str(dato) == str(correlativo): 
                fila_objetivo = fila 
                valores = self.tree.item(fila)['values']
                bandera = True
        
        if bandera == False: 
            mb.showinfo("Atencion", "No se encontro ese correlativo")
            return 
        
        root = Toplevel(self)
        root.geometry("300x300")
        root.title("Moficacion")
        
        etiquetas = ["Nombre del videojuego", "Plataforma", "Genero", "Precio", "Stock", "Fecha de Lanzamiento", "Calificacion"]
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root, text=etiqueta, font=("arial", 10, "bold")).grid(row=i, column=0, sticky='w')
            
            entry = Entry(root)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
            
        
        for i in range(len(etiquetas)): 
            etiq = etiquetas[i]
            caja = objetos[etiq]
            caja.insert(0, valores[i])
        
        def cargar(): 
            datos = []
            for entry in objetos.values(): 
                datos.append(entry.get())
            
            self.tree.item(fila_objetivo, values=datos)
            try: 
                with open(self.ruta, 'wb') as archivo: 
                    for fila in self.tree.get_children(): 
                        valos_buenos = self.tree.item(fila)["values"]
                        pickle.dump(valos_buenos, archivo)
                        mb.showinfo("Atencion", "Se ha modificado un registro")
            except AttributeError: 
                mb.showerror("Error", "Debe haber cargado un archivo primero")
                return 
            
            root.destroy()
            self.consulta()
        
        Button(root, text="Modificar registro", command=cargar).grid(row=i+1, column=0)
            

    def eliminar(self): 
        try: 
            dato = sd.askstring("Eliminacion", "Ingrese el correlativo para elimnar\n un registro")
            bandera = False
            for fila in self.tree.get_children(): 
                correlativo = self.tree.item(fila)["text"]
                if str(dato) == str(correlativo): 
                    self.tree.delete(fila)
                    bandera = True
                    
            print(correlativo)
            if bandera == False:
                mb.showinfo("Atencion", "No hay un registro con ese correlativo")
            
            with open(self.ruta,'wb') as archivo: 
                for fila in self.tree.get_children(): 
                    valores = self.tree.item(fila)["values"]
                    pickle.dump(valores, archivo)
                self.consulta()
        except AttributeError:
            mb.showerror("Error", "Debe de haber cargado un archivo primero")

    def buscnom(self): 
        dato = sd.askstring("Busqueda por nombre", "Ingrese el nombre del juego")
        seleccion = []
        bandera = False
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if str(dato) == str(registro[0]): 
                seleccion.append(fila)
                self.tree.selection_set(seleccion)
                bandera = True
        
        
        if bandera == False: 
            mb.showinfo("Atencion", "No se encontro ese juego")
            return
         
    def buscplat(self): 
        dato = sd.askstring("Busqueda por nombre", "Ingrese el nombre del juego")
        seleccion = []
        bandera = False 
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if str(dato) == str(registro[1]): 
                seleccion.append(fila)
                self.tree.selection_set(seleccion)
                bandera = True
        if bandera == False: 
            mb.showinfo("Atencion", "No se encontro ese juego")
            return
    
    def bcombinada(self): 
        dato1 = sd.askstring("Busqueda por genero", "Ingrese el genero de juego que busca")
        dato2 = sd.askstring("Busqueda por calificacion", "Ingrese la calificacion que busca")
        seleccion = []
        bandera = False
        for fila in self.tree.get_children(): 
            registro = self.tree.item(fila)["values"]
            if str(dato1) == registro[2] and str(dato2) == registro[6]: 
                seleccion.append(fila)
                self.tree.selection_set(seleccion)
                bandera = True
        if bandera == False: 
            mb.showinfo("Atencion", "No se encontro ese juego")
            return

app().mainloop()