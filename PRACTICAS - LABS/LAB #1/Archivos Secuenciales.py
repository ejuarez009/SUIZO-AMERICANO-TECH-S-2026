from tkinter import*; from tkinter import messagebox as mb; from tkinter import filedialog as fd; from tkinter import ttk 

class Archivos_secuenciales(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("600x700")
        
        self.textbox = Text(width=50, height=20)
        self.textbox.grid(row=0, column=0, columnspan=5)   # centrado dentro de su celda
        
        #===========================TREEVIEW============================
        encabezados = ["Linea del archivo", "Número obtenido", "Número en binario"]
        self.Treeview = ttk.Treeview(height=10, columns=encabezados, show="headings")
        for column in encabezados: 
            self.Treeview.heading(column, text=column)
            self.Treeview.column(column, width=180, anchor=CENTER)
        self.Treeview.grid(row=2, column=0, pady=50, columnspan=5)
        
        
    def analizar(self): 
        if not self.route: 
            mb.showerror("ERROR", "No se ha seleccionado un archivo")
        else: 
            route = self.route 
            patron_num = "0123456789"
            patron_letras = "abcdefgihjklmnopqrstuvwxyz"
            with open(route, 'r', encoding='utf-8') as archiv: 
                contenido = archiv.readlines()
                list_nums = []
                cont_lineas = 0
                for linea in contenido.lower(): 
                    cont_lineas += 1
                    for char in linea: 
                        if char in patron_num and char not in patron_letras : 
                            if char == " " or char == ",":
                                list_nums.append(char)
        #=====================CONVERSION A BINARIO=======================
        list_binarios = []
        for num in list_nums: 
            while num > 0: 
                temp = num % 2 
                binary += str(temp)
                num = num // 2
            list_binarios.append(num)
            binary = ""
            
        #======================CONVERSION ROMANOS===========================
        num_romanos = 0
        
        self.Treeview.insert("",END,text=cont_lineas, values=0)
        
        
Archivos_secuenciales().mainloop()