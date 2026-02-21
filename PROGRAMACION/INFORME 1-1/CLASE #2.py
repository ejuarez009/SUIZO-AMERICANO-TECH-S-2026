from tkinter import* ; from tkinter import filedialog as fd; from tkinter import messagebox as mb

class Manage_files(Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry("500x300")
        
        self.text_box = Text(self, height=10, width=50)
        self.text_box.grid(row=0, column=0, columnspan=4)
        
        self.button_new = Button(text="Nuevo archivo", command=self.new_file)
        self.button_new.grid(row=1, column=0)
        self.button_open = Button(text="Abrir archivo", command=self.open_file)
        self.button_open.grid(row=1, column=1)
        self.button_save = Button(text="Grabar archivo", command=self.save_file)
        self.button_save.grid(row=1, column=2)
    
    def new_file(self): 
        message_warning = mb.askyesno("ATENCION", "El archivo no se ha guardado \n ¿Desea guardarlo?")
        if not message_warning and self.text_box.get(1.0, END): 
            self.text_box.delete(1.0, END)
        else: 
            route = fd.asksaveasfilename()
            with open(route,'w'): 
                mb.showinfo("¡FELICIDADES!","Se ha creado un archivo nuevo")
    
    def open_file(self): 
        route = fd.askopenfilename()
        with open(route, 'r', encoding='utf-8') as archivo: 
            content = archivo.read()
            self.text_box.insert(1.0, content)
    
    def save_file(self): 
        route = fd.asksaveasfilename()
        with open(route, 'w') as archivo:
            content = self.text_box.get(1.0, END)
            archivo.write(content)
        self.text_box.delete(1.0, END)
        mb.showinfo("ATENCION", "Se ha guardado el archivo exitosamente")

Manage_files().mainloop()