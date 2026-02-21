from tkinter import Entry, Button, Label, Tk, messagebox as mb, Text, END
from tkinter import filedialog as fd
import os.path 

class ManejoArchivos(Tk): 
    def __init__(self): 
        super().__init__()

        self.geometry("800x560")
        self.title("Manejo de Archivos - Elmer Juarez_C5A")
        
        self.text_widget = Text(width=80, height=30)
        self.text_widget.pack()
        
        self.button_create = Button(text="CREAR ARCHIVO", command=self.crear, width=30, height=4)
        self.button_create.pack(side="left")
        self.button_save = Button(text="GRABAR ARCHIVO", command=self.grabar, width=30, height=4)
        self.button_save.pack(side="left")
        self.button_open = Button(text="LEER ARCHIVO", command=self.leer, width=30, height=4)
        self.button_open.pack(side="left")
    
    def crear(self):
        route = fd.asksaveasfilename(title="Seleccione un archivo")
        if not route:
            mb.showinfo("Información", "El achivo ya existe")
            conf_read = mb.askyesno("Confirmación", "¿Desea leer el archivo?")
            if conf_read is True: 
                self.leer()
            else: 
                return
        
        else: 
            conf_crear = mb.askyesno("Informacion", "El archivo no existe, ¿Desea crearlo?")
            if conf_crear is True: 
                with open(route, 'w', encoding='utf-8'): 
                    pass #Crea el archivo vacio
                mb.showinfo("Informacion", "Archivo creado exitosamente")
            else: 
                mb.showinfo("Información", "No se creó el archivo, ni leyo el archivo")
                
                

    def grabar(self): 
        route = fd.askopenfilename(title="Seleccione un archivo")
        if not route: 
            mb.showwarning("CUIDADO", "No se selecciono ningun archivo")
        else: 
            if self.text_widget == None: 
                mb.showwarning("CUIDADO", "No hay datos a guardar")
            else: 
                data = self.text_widget.get("1.0", END)
                with open(route, 'w', encoding='utf-8') as filecito: 
                    filecito.write(data)
                    mb.showinfo("Información", "Datos guardados correctamente")


    def leer(self):
        route = fd.askopenfilename(title="Seleccione un archivo")
        with open(route, 'r') as filecito: 
            info_doc = filecito.read()
            self.text_widget.delete("1.0", END)
            self.text_widget.insert("1.0", info_doc)
    
ManejoArchivos().mainloop()