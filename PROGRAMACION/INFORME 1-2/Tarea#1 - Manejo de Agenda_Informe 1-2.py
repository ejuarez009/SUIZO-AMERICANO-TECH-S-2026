#==========================================================DOCUMENTACION INTERNA==========================================================
# PROGRAMA: Manejo de Agenda
# AUTOR: Elmer Juarez
# FECHA: 17/09/2024
# LENGUAJE: Python3
# DESCRIPCION: Este programa permite gestionar una agenda de contactos utilizando una interfaz gráfica.
#              Se pueden crear nuevos registros, modificar registros existentes, realizar consultas generales e individuales, y manejar archivos binarios para almacenar los datos de los contactos.
# FUNCIONALIDADES:
# 1. Crear un nuevo archivo de agenda.
# 2. Agregar nuevos registros de contactos.
# 3. Modificar registros existentes.
# 4. Realizar consultas generales para visualizar todos los contactos.
# 5. Realizar consultas individuales para buscar un contacto específico por nombre.
#HERRAMIENTAS UTILIZADAS:
# - Tkinter para la interfaz gráfica.
# - Pickle para el manejo de archivos binarios.
# - OS para verificar la existencia de archivos y obtener su tamaño.
#=============================================================================================================================================


from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb; from tkinter import ttk
import pickle
import os 

class Agenda (Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("1050x560")
        self.title("Manejo de Agenda - Elmer Juarez")
        
        #========================================================TREEVIEW========================================================
        encabezados = ["Nombre", "Apellidos", "Direccion", "Telefono Movil", "Telefono Fijo", "Correo Electronico"]
        Treeview = ttk.Treeview(self, height=20, columns=encabezados, show="headings")
        
        for column in encabezados: 
            Treeview.heading(column, text=column)
            Treeview.column(column, width=130)
        Treeview.grid(row=2, column=0, padx=20)
        self.tree = Treeview
        self.label_route = Label(text="-- ruta --", fg="gray", font=("Arial", 10, "bold"))
        self.label_route.grid(row=1, column=0, columnspan=5)
        
        #========================================================BOTONES========================================================
        frame_buttons = Frame(self)
        frame_buttons.grid(row=3, column=0, padx=20)
        
        Button(frame_buttons, text="MODIFICAR", command=self.modificar,height=2, width=25).grid(row=3, column=4, pady=20, padx=10)
        Button(frame_buttons, text="NUEVO REGISTRO", command=self.registro,height=2, width=25).grid(row=3, column=3, pady=20, padx=10)
        Button(frame_buttons, text="CONSULTA GENERAL", command=self.consulta_general,height=2, width=25).grid(row=3, column=1, pady=20, padx=10)
        Button(frame_buttons, text="CONSULTA INDIVIDUAL", command=self.individual,height=2, width=25).grid(row=3, column=2, pady=20, padx=10)
        Button(frame_buttons, text="CREAR", command=self.create_file,height=2, width=25).grid(row=3, column=0, pady=20, padx=10)
        

    #================================ REGISTRO ===========================================
    def registro(self): 
        root2 = Toplevel()
        root2.geometry("300x200")
        root2.title("NUEVO REGISTRO")
        labels = ["Nombre", "Apellidos", "Direccion", "Telefono Movil", "Telefono fijo", "Correo Electronico"]
        self.campos = {}
        
        for i, text in enumerate(labels): 
            Label(root2, text=text).grid(row=i, column=0, sticky='w')
            entry = Entry(root2, width=15)
            entry.grid(row=i, column=1)
            self.campos[text] = entry 

        Button(root2, text="Guardar", command=self.save).grid(row=7, column=0, columnspan=2, pady=20, height=2, width=15)

    def save(self):
        if not hasattr(self, "route"): ## EL HASATTR NOS PERMITE VER SI EL ATRIBUTO EXISTE, EN ESTE CASO LA RUTA DEL ARCHIVO
            mb.showerror("ERROR","Primero cree o abra un archivo")
            return
        
        datos = []
        for entry in self.campos.values():
            datos.append(entry.get())
            
        with open(self.route,'ab') as archiv:
            pickle.dump(datos,archiv)
        mb.showinfo("Guardado","Registro guardado correctamente")
        
        for entry in self.campos.values():
            entry.delete(0,END)

    #================================ MODIFICAR =================================
    def modificar(self): 
        if not self.tree.selection(): 
            mb.showerror("ERROR", "No se ha seleccionado ningun registro")
            return
        
        root3 = Toplevel()
        root3.geometry("250x250")
        root3.title("MODIFICAR REGISTRO")
        
        labels = ["Nombre", "Apellidos", "Direccion", "Telefono Movil", "Telefono fijo", "Correo Electronico"]
        self.headers = {}
        
        for i,text in enumerate(labels): 
            Label(root3,text=text).grid(row=i,column=0)
            entry = Entry(root3)
            entry.grid(row=i,column=1)
            self.headers[text] = entry
            
        id_registro = self.tree.focus()
        lista_registro = self.tree.item(id_registro)['values']
        
        for i in range(len(lista_registro)): 
            list(self.headers.values())[i].insert(END,lista_registro[i])
            
        Button(root3, text="Actualizar registro", command=self.actualizar).grid(row=7,columnspan=2)

    def actualizar(self): 
        datos_nuevos = [entry.get() for entry in self.headers.values()]
        registros = []
        
        with open(self.route,'rb') as archiv:
            while True:
                try:
                    registros.append(pickle.load(archiv))
                except EOFError:
                    break
                
        seleccionado = self.tree.focus()
        viejo = self.tree.item(seleccionado)['values']
        
        for i in range(len(registros)):
            if registros[i] == viejo:
                registros[i] = datos_nuevos
                
        with open(self.route,'wb') as archiv:
            for r in registros:
                pickle.dump(r,archiv)
                
        self.tree.item(seleccionado, values=datos_nuevos)
        
        mb.showinfo("Actualizado","Registro modificado")

    #================================ CONSULTA INDIVIDUAL ================================
    def individual(self): 
        root = Toplevel()
        root.geometry("250x120")
        root.title("Buscar")
        Label(root,text="Ingrese nombre").pack()
        
        entry = Entry(root)
        entry.pack()
        
        def buscar():
            nombre = entry.get().lower()
            self.tree.delete(*self.tree.get_children())
            try: 
                with open(self.route,'rb') as archiv:
                    while True:
                        try:
                            datos = pickle.load(archiv)
                            if datos[0].lower() == nombre:
                                self.tree.insert("",END,values=datos)
                        except EOFError:
                            break
            except AttributeError:
                mb.showerror("ERROR","Primero cree o abra un archivo")
                    
        Button(root,text="Buscar",command=buscar).pack()

    #================================ CONSULTA GENERAL ==================================
    def consulta_general(self): 
        self.route = fd.askopenfilename(defaultextension=".bin")
        if not self.route:
            return
        
        self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
        
        maxi = os.path.getsize(self.route)
        
        with open(self.route, 'rb') as archiv:
            self.tree.delete(*self.tree.get_children())
            pos = 0
            
            while pos < maxi: 
                datos = pickle.load(archiv)
                self.tree.insert("", END, values=datos)
                pos = archiv.tell()

    #================================ ARCHIVO =================================
    def create_file(self): 
        self.route = fd.asksaveasfilename(defaultextension='*.bin', filetypes=[("Archivo Binario", "*.bin")])
        if not self.route:
            mb.showinfo("Atención","No se creó ningún archivo")
            return
        
        self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
        
        if not os.path.exists(self.route):
            with open(self.route, 'wb') as archiv: 
                archiv.write(b'')
                
        mb.showinfo("Archivo","Archivo listo para usar")

Agenda().mainloop()