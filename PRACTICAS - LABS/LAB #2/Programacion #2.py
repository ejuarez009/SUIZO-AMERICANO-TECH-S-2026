from tkinter import* ; from tkinter import messagebox as mb; from tkinter import ttk; from tkinter import filedialog as fd
from tkinter import simpledialog as sd 
from datetime import datetime
import os 
import pickle


class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("700x700")
        self.title("Repaso de Lab / Progra Binarios")
        
        Button(self,text="Crear/Abrir", command=self.crear_abrir).place(x=10, y=10)
        Button(self, text="Grabar registro", command=self.grabar).place(x=10, y=50)
        Button(self, text="Consulta General", command=self.consulta_ge).place(x=10, y=50)

        campos = ["Nombre", "Genero", "Fecha", "Duracion", "Interprete","Frecuencia"]
        self.campos_e = {}
        for i, text in enumerate(campos): 
            Label(self,text=text).place(x=150, y=i*25+50)
            
            entry = Entry(self)
            entry.place(x=280, y=i*25+50)
            
            self.campos_e[text] = entry
    
    def crear_abrir(self): 
        estado = mb.askyesno("ATENCION","¿Desea crear archivo?")
        if estado: 
            self.ruta = fd.askopenfilename(filetypes=[("Archivo Binario", "*.bin")], defaultextension=".bin")
        else: 
            self.ruta = fd.asksaveasfilename(filetypes=[("Archivo Binario", "*.bin")], defaultextension=".bin")
            with open(self.ruta, "wb") as archivo: 
                archivo.write(b'')
    
    def grabar(self): 
        
        datos = []
        for entry in self.campos_e.values(): 
            datos.append(entry.get())
        
        nombre = datos[0]
        genero = datos[1]
        fecha = datos[2]
        duracion = datos[3]
        interprete = datos[4]
        frecuencia = datos[5]
        generos = ["rock", "pop", "reggaeton", "electronica", "instrumental"]
        
        if self.validfecha(fecha) and self.validdura(duracion) and (genero.lower() in generos) and (frecuencia in range(0,26)): 
            playlist = f"exitos de {genero}"
            calificacion = (frecuencia - 1)// 5 + 1
            
            datos_g = [nombre,genero,playlist,fecha,duracion,interprete,frecuencia,calificacion]
            
            with open(self.ruta,'ab') as archivo: 
                pickle.dump(datos_g, archivo)

            for entry in self.campos_e.values(): 
                entry.delete(0,END)
            
            self.actualizar() #! invocar a actualizar para grabar el registro en el archivo
            
            
            
    def validfecha(self,fecha): 
        try: 
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            mb.showinfo("Atencion", "Formato de Fecha Invalida")
            return False
    
    def validdura(self,duracion): 
        try: 
            datetime.strptime(duracion, "%M:%S")
            return True
        except ValueError:
            mb.showinfo("Atencion", "Formato de Duracion Invalida")
            return False
    
    def actualizar(self): 
        self.tree.delete(*self.tree.get_children())
        with open(self.ruta, 'rb') as archivo: 
            final = os.path.getsize(self.ruta)
            pos = 0 
            linea = 1
            while pos<final: 
                datos = pickle.load(archivo)
                self.tree.insert("",END,text=str(linea), values=(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7]))
                linea += 1
                pos = archivo.tell()
            
    
    
    def consulta_ge(self): 
        root = Toplevel()
        root.geometry("1200x600")
        headers = ["Nombre", "Genero", "Playlist", "Fecha", "Duracion", "Interprete", "Frecuencia", "Calificacion"]
        self.tree = ttk.Treeview(root, columns=headers )
        self.tree.heading("#0", text="CORRELATIVO")
        for header in headers: 
            self.tree.heading(header, text=header)
            self.tree.column(header, width=150)
        self.tree.pack(pady=50)
        
        Button(root,text="Eliminar", command=self.eliminar).pack(pady=10)
        Button(root,text="Modificar", command=self.modificar).pack(pady=10)
        
        self.actualizar() #! LLAMAR A ACTUALIZAR PARA INSERTAR LOS DATOS DEL ARCHIVO
    
    def eliminar(self): 
        dato = sd.askstring("Atencion", "Ingrese un dato a eliminar")
        if int(dato) == 1: 
            mb.showwarning("CUIDADO", "El archivo no puede quedar vacío")
            return 
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)["text"] #! OBTIENE EL CORRELATIVO DEL REGISTRO
            if dato == correlativo: 
                self.tree.delete(fila)
                
        for fila in self.tree.get_children(): 
            valores = self.tree.item(fila)["values"]
            with open(self.ruta,'wb') as archivo: 
                pickle.dump(valores, archivo)
        
        self.actualizar()
        
        
    def modificar(self): 
        correlativo = sd.askinteger("Atencion", "Ingrese un correlativo a modificar")
        for fila in self.tree.get_children(): 
            corre_re = self.tree.item(fila)['text']
            if str(correlativo) == str(corre_re): 
                valores = self.tree.item(fila)["values"]
                break
        
        
        vm = Toplevel(self)
        vm.geometry("300x300") 
        
        campos = ["Nombre", "Genero", "Fecha", "Duracion", "Interprete","Frecuencia"]
        widgets = {}
        for i, text in enumerate(campos): 
            Label(vm,text=text).place(x=150, y=i*25+50)
            
            entry = Entry(vm)
            entry.place(x=280, y=i*25+50)
            
            widgets[text] = entry
        
        self.widgets = widgets
        
        def md(): 
            for entry in self.widgets.values(): 
                entry.delete(0,END)
                j = 0
                entries = list(self.widgets.values()) 
                
            for i, valor in enumerate(valores):
                if i in (2, 7):
                    continue
                entries[j].insert(0, valor)
                j += 1
            
        Button(vm, text="Modificar", command=md)
        
    def buscar(self): 
        pass
app().mainloop() 