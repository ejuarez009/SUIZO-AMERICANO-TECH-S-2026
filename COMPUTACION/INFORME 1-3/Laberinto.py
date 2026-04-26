from tkinter import*; from tkinter import filedialog as fd; from tkinter import messagebox as mb 
from time import sleep


class Laberintos(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("550x550")
        self.title("Elmer Juarez C5A")

        Button(text="Abrir archivo", command=self.abrir).grid(row=0, column=0)
        Button(text="Resolver laberinto", command=self.resolver).grid(row=0, column=1)
        self.canva = Canvas(width=500, height=500,background="lightgreen")
        self.canva.grid(row=1, column=0)
        
        
        self.encontrado = False
        self.cubito = None
        self.inicio = None
        self.pausa_exploracion = 0.05
        self.pausa_camino = 0.0012
        self.canva.bind("<Button-1>", self.posicionar)
        
    
    
    def posicionar(self, event): 
        px = event.x // 10 
        py = event.y // 13 
        if py < len(self.lineas) and px < len(self.lineas[0]): #Si el click esta dentro del laberinto (rows, cols)
            if self.lineas [py][px] == " ": #Verficia que si se haya seleccionado un cuadro del camino
                self.inicio = (py, px) #Crea cordenadas para el inicio
                if self.cubito == None: #Verifica que no haya un cubo existente
                    self.cubito = self.canva.create_rectangle(px*10, py*13, px*10+10, py*13+13, fill="blue") #Si, crea el cubito
                
                else: 
                    self.canva.coords(self.cubito,px*10, py*13, px*10+10, py*13+13) #Si ya existe uno, actualiza las cordenadas del cubito creado
                    self.canva.update() 
        else: 
            mb.showinfo("Atencion", "Debe seleccionar un camino del laberinto")
            return
        
    
    
    def abrir(self): 
        ruta = fd.askopenfilename(defaultextension=".txt")
        with open(ruta, 'r') as archivo: 
            self.contenido = archivo.read()
            self.lineas = self.contenido.splitlines()
            self.lab_visual(self.lineas)
    
    def lab_visual(self, lineas): 
        px = 0 
        py = 0
        for linea in lineas:#Recorre cada una de las lineas en la lista de lineas
            for char in linea: #Reccorre cada caracter de la linea (Matriz)
                if char == " ": 
                    color = "White"
                elif char == "E": 
                    color = "#008000"
                else: 
                    color = "Black"

                self.canva.create_rectangle(px,py,px+10,py+13, fill=color)
                px += 10 #Va colocando los cuadros respectivamente de cada caracter del archivo, separacion de 10 pixeles
            py+=13 #Realiza el salto de lineas es decir la distancia entre una fila de abajo y la consecutiva
            px = 0 #Se regresa al extremo inicial del canvas
    
    def recursion(self, nl, rows, char): 
        
        if rows not in range(len(nl)) or char not in range (len(nl[0])):
            return None

        car = nl[rows][char]

        if car == "E": 
            return [(rows, char)]

        if car != " ": 
            return None
        
        nl[rows][char] = "V"
        if self.cubito is not None:
            self.canva.coords(self.cubito, char*10, rows*13, char*10+10, rows*13+13)
            self.canva.update()
            sleep(self.pausa_exploracion)
        
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ruta = self.recursion(nl, rows + dr, char + dc)
            if ruta is not None:
                return [(rows, char)] + ruta

        return None

    def animar_camino(self, ruta):
        for fila, columna in ruta:
            if self.lineas[fila][columna] != "E":
                self.canva.create_rectangle(columna*10, fila*13, columna*10+10, fila*13+13, fill="deep sky blue")

            if self.cubito is not None:
                self.canva.coords(self.cubito, columna*10, fila*13, columna*10+10, fila*13+13)

            self.canva.update()
            sleep(self.pausa_camino)


    
    def resolver(self): 
        newlines = []
        for linea in range(len(self.lineas)): 
            vcaminos = []
            for char in range(len(self.lineas[0])): 
                vcaminos.append(self.lineas[linea][char]) 
            newlines.append(vcaminos)
            
        
        if self.inicio: 
            linea, char= self.inicio
            ruta = self.recursion(newlines, int(linea), int(char))
            if ruta is not None:
                self.animar_camino(ruta)
            else:
                mb.showinfo("Atencion", "No se encontro salida desde el punto inicial")
        else: 
            mb.showinfo("Atencion", "No ha seleccionado un inicio")
            return
        
    def mover_jugador(self, fila, columna): 
        px = columna * 10 
        py = fila * 13
        if self.cubito != None: 
            self.cubito = self.canva.create_rectangle(px*10, py*13, px*10+10, py*13+13, fill="blue")
        else: 
            self.canva.coords(self.cubito,px*10, py*13, px*10+10, py*13+13)
        
        self.update()
        sleep(0.9)
    
Laberintos().mainloop()