
from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb
from time import sleep

class Laberintos(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("550x550")
        self.title("Elmer Juarez C5A")

        Button(text="Abrir archivo", command=self.abrir).grid(row=0, column=0)
        Button(text="Resolver laberinto", command=self.resolver).grid(row=0, column=1)
        Button(text="Resetear", command=self.resetear).grid(row=0, column=2)
        self.canva = Canvas(width=500, height=500, background="lightgreen")
        self.canva.grid(row=1, column=0, columnspan=3)
        
        self.encontrado = False
        self.cubito = None
        self.inicio = None
        self.pausa_exploracion = 0.05
        self.pausa_camino = 0.01
        self.lineas = None
        self.canva.bind("<Button-1>", self.posicionar)
        
    
    def posicionar(self, event): 
        px = event.x // 10 
        py = event.y // 13 
        if py < len(self.lineas) and px < len(self.lineas[0]):
            if self.lineas[py][px] == " ":
                self.inicio = (py, px)
                if self.cubito == None:
                    self.cubito = self.canva.create_rectangle(px*10, py*13, px*10+10, py*13+13, fill="blue")
                else: 
                    self.canva.coords(self.cubito, px*10, py*13, px*10+10, py*13+13)
                    self.canva.update() 
        else: 
            mb.showinfo("Atencion", "Debe seleccionar un camino del laberinto")
    
    def abrir(self): 
        ruta = fd.askopenfilename(defaultextension=".txt")
        with open(ruta, 'r') as archivo: 
            self.contenido = archivo.read()
            self.lineas = self.contenido.splitlines()
            self.lab_visual(self.lineas)

        self.inicio = (1,1)
        px, py= self.inicio
        self.cubito = self.canva.create_rectangle(px*10, py*13, px*10+10, py*13+13, fill="blue")
    def lab_visual(self, lineas): 
        px = 0 
        py = 0
        for linea in lineas:
            for char in linea:
                if char == " ": 
                    color = "White"
                elif char == "E": 
                    color = "#008000"
                else: 
                    color = "Black"

                self.canva.create_rectangle(px, py, px+10, py+13, fill=color)
                px += 10
            py += 13
            px = 0
    
    # 🔥 NUEVA RECURSIÓN (tipo segundo código)
    def recursion(self, nl, rows, char): 
        
        if rows not in range(len(nl)) or char not in range(len(nl[0])):
            return False

        car = nl[rows][char]  

        if car == "E": 
            self.canva.create_rectangle(char*10, rows*13, char*10+10, rows*13+13, fill="red")
            return True

        if car != " ": 
            return False
        
        nl[rows][char] = "V"

        # mover cubito
        if self.cubito is not None:
            self.canva.coords(self.cubito, char*10, rows*13, char*10+10, rows*13+13)
            self.canva.update()
            sleep(self.pausa_exploracion)

        # explorar
        if (self.recursion(nl, rows+1, char) or
            self.recursion(nl, rows-1, char) or
            self.recursion(nl, rows, char+1) or
            self.recursion(nl, rows, char-1)):

            # dibujar camino correcto
            self.canva.create_rectangle(char*10, rows*13, char*10+10, rows*13+13, fill="deep sky blue")
            self.canva.update()
            sleep(self.pausa_camino)
            return True

        return False

    def resolver(self): 
        newlines = []
        for linea in range(len(self.lineas)): 
            vcaminos = []
            for char in range(len(self.lineas[0])): 
                vcaminos.append(self.lineas[linea][char]) 
            newlines.append(vcaminos)
            
        if self.inicio: 
            linea, char = self.inicio
            encontrado = self.recursion(newlines, int(linea), int(char))
            if not encontrado:
                mb.showinfo("Atencion", "No se encontro salida")
        else: 
            mb.showinfo("Atencion", "No ha seleccionado un inicio")
    
    
    def resetear(self): 
        self.canva.delete('all')
        
        if self.lineas: 
            self.lab_visual(self.lineas)
        
        self.cubito = None 
        self.inicio = None

Laberintos().mainloop()
