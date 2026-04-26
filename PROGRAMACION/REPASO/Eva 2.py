from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb; from tkinter import ttk 
import pickle 
import os 

class Files(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("700x500")
        
        frame_buttons = Frame(self)
        frame_buttons.grid(row=1, column=0)
        
        self.btn_crear = Button(frame_buttons, text="Crear archivo binario", command=self.create).grid(row=0, column=0)
        self.btn_consul_ge = Button(frame_buttons,text="Consulta general", command=self.consultar).grid(row=0, column=1)
        self.btn_individual = Button(frame_buttons, text="Consulta individual", command=self.individual).grid(row=0, column=2)
        self.btn_registro = Button(frame_buttons, text="Nuevo Registro", command=self.registro).grid(row=0, column=3)
        
        
        frame_tree = Frame(self)
        frame_tree.grid(row=0, column=0, padx=20)
        
        self.label_ruta = Label(frame_tree,text="--ruta--", fg="gray")
        self.label_ruta.grid(row=0, column=0)
        
        encabezados = ["Codigo", "Nombre", "Apellido", "Profesion"]
        self.tree = ttk.Treeview(frame_tree, height=20, columns=encabezados, show='headings')
        for columna in encabezados: 
            self.tree.heading(columna, text=columna)
            self.tree.column(columna, width=150)
        self.tree.grid(row=1, column=0)

    def create(self): 
        pass

    def consultar(self): 
        ruta = fd.askopenfilename(defaultextension=".bin", filetypes=[("Archivos Binarios", "*.bin")])
        if not ruta: 
            mb.showwarning("CUIDADO", "No se ha seleccionado algun archivo")
            return
        self.label_ruta.config(text=f"RUTA: {ruta}", fg="blue")
        
        maxi = os.path.getsize(ruta)
        print(maxi)
        with open(ruta, 'rb') as archiv: 
            self.tree.delete()
            pos = 0 
            
            while pos < maxi: 
                datos = pickle.load(archiv)
                self.tree.insert("", END, values=datos)
                pos = archiv.tell()

    def individual(self): 
        pass

    def registro(self): 
        root2 = Toplevel()
        root2.geometry("300x200")
        root2.title("NUEVO REGISTRO")
        
        self.campos = {} #DICCIONARIO EL CUAL VA TENER DE CLAVE LA ETIQUETA Y DE VALOR EL ENTRY 
        labels = ["Codigo", "Nombre", "Apellido", "Profesion"]
        
        for i, text in enumerate(labels): 
            Label(root2,text=text).grid(row=i, column=0)
            
            entry = Entry(root2, width=10)
            entry.grid(row=i, column=1)
            
            self.campos[text] = entry
        
        Button(root2, text="Actualizar", command=self.save).grid(row=5, column=0, pady=20)

    def save(self): 
        pass

Files().mainloop()