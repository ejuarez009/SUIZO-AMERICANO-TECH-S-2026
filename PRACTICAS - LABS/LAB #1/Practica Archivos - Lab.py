from tkinter import*; from tkinter import messagebox as mb; from tkinter import filedialog as fd; 
import os; from tkinter import ttk 

class Files(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("1350x800")
        self.title("Primer Laboratorio - Elmer Juarez C5A")
        
        #
        #=====================TEXTBOX=======================
        frame_wdigets = Frame(self)
        frame_wdigets.grid(row=0, column=0)
        self.label_route = Label(frame_wdigets, text="--ruta--", fg="gray")
        self.label_route.grid(row=0, column=0)
        self.textbox = Text(frame_wdigets, width=50, height=10)
        self.textbox.grid(row=1, column=0)
        self.route = None
        #======================TREEVIEWS=====================
        frame_trees = Frame(self)
        frame_trees.grid(row=1, column=0, pady=30)
        encabezados = ["No. Linea", "Cantidad de números", "Cantidad de dígitos", "Números", "Número de arrobas","Equivalente en binario", "Equivalente en romano"]
        self.tree = ttk.Treeview(frame_trees, height=20, columns=encabezados, show="headings")
        for columna in encabezados: 
            self.tree.heading(column=columna, text=columna)
            self.tree.column(columna,width=170)
        self.tree.grid(row=0, column=0, padx=50)

        #==================BUTTONS=========================
        frame_button = Frame(self)
        frame_button.grid(row=2, column=0, pady=10)
        self.button_create = Button(frame_button, text="CREAR ARCHIVO", command=self.create_file).grid(row=0, column=0)
        self.button_save = Button(frame_button, text="GRABAR ARCHIVO", command=self.save_file).grid(row=0, column=1)
        self.button_read = Button(frame_button, text="LEER ARCHIVO", command=self.read_file).grid(row=0, column=2)
        self.button_analizar = Button(frame_button, text="ANALIZAR ARCHIVO", command=self.analizar_numeros).grid(row=0, column=3)

    def create_file(self): 
        self.route = fd.asksaveasfilename(defaultextension='.txt', initialfile='.txt')
        self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
        if os.path.exists(self.route): 
            mesagec = mb.askyesno("ATENCION", "El archivo ya existe, ¿Desea abrirlo?")
            if mesagec: 
                self.read_file()
            else: 
                mb.showinfo("ATENCION", "No se creo o selecciono ningun archivo")
                return 
        try: 
            with open(self.route, 'w', encoding='utf-8') as archivo: 
                archivo.write("")
        except FileNotFoundError: 
            mb.showerror("ERROR", "No se creo ningun archivo")

    def save_file(self): 
        if self.route: 
            mb.showinfo("ATENCION", "¿Desea sobreescribir en el archivo los datos que estan en el objeto de texto?")
            self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
            with open(self.route, 'w', encoding='utf-8') as archivo: 
                contenido = self.textbox.get("1.0",END)
                archivo.write(contenido)
            msg_text = mb.askyesno("ATENCION", "Se han grabado los datos, ¿Desea limpiar el objeto de texto?")
            if msg_text: 
                self.textbox.delete("1.0",END)
        else: 
            self.route = fd.asksaveasfilename(defaultextension='.txt')
            self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
            with open(self.route, 'w', encoding='utf-8') as archivo: 
                contenido = self.textbox.get("1.0",END)
                archivo.write(contenido)
        
        
    def read_file(self): 
        self.route = fd.askopenfilename(defaultextension='.txt', filetypes=[("Archivos de texto", "*.txt")])
        if self.route == None: 
            mb.showwarning("CUIDADO", "No se selecciono ningun archivo")
            
        else: 
            self.label_route.config(text=f"RUTA: {self.route}", fg="blue")
            with open(self.route, 'r') as archivo: 
                #===========PARA EL TEXTBOX=================
                contenido = archivo.read()
                self.textbox.delete("1.0", END)
                self.textbox.insert("1.0", contenido)
                
                #===========PARA EL ANALISIS=============
                
    
    def analizar_numeros(self):
        with open(self.route, 'r') as archivo: 
            contenido = archivo.read()
            lineas = contenido.splitlines()
            self.cont_linea = 0
            
            for linea in lineas: 
                self.cont_linea += 1
                list_num = []
                num = ""
                cont_arro = 0
                cont_num = 0
                cont_digit = 0
                for character in linea: 
                    if character.isdigit(): 
                        num += character
                        cont_digit +=1
                    elif character == "@": 
                        cont_arro += 1
                    else: 
                        if num != "" : 
                            list_num.append(num)
                            cont_num +=1
                            num = ""
                
                if num != "": 
                    list_num.append(num)
                    cont_num +=1
                    
                info_tree = [self.cont_linea, cont_num, cont_digit, list_num, cont_arro, self.binario(list_num)]
                self.tree.insert("",END,values=info_tree)
    
    def binario(self,numeros): 
        list_binario = []
        patron = "0123456789ABCDEF"
        for i in range(len(numeros)): 
            binario = ""
            num = int(numeros[i])
            while num > 0: 
                resto = num % 16
                binario += str(patron[resto])
                num = num // 16
            list_binario.append(binario[::-1])
            binario = ""
        return list_binario
    
    
    
    
    
    
    def analizar_letras(self): 
        pass

Files().mainloop()