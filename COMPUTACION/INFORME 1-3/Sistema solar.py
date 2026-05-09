from tkinter import Tk, Canvas
from math import pi, cos, sin
from time import sleep

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        #===ESPACIO===
        self.geometry("1200x950")
        self.resizable(False, False)
        self.title("Sistema Solar - Elmer Juarez")
        self.canva1 = Canvas(bg='black', highlightbackground='black')
        self.canva1.pack(expand=True, fill='both')
        self.update()
        
        #======ESTRELLA======
        sol = planeta(self.canva1,40, "yellow", 0, 0, None)
        sol.traslacion()
        self.sol = sol
        
        #======PLANETAS======
        #Tierra
        self.tierra = planeta(self.canva1,20,"blue", 150, 2*pi/365.25, sol)
        self.luna = planeta(self.canva1, 5, "gray",50, 2*pi/27, self.tierra)
        
        # Mercurio
        self.mercurio = planeta(self.canva1, 6, "gray", 80, 2*pi/88, sol)

        # Venus
        self.venus = planeta(self.canva1, 10, "orange", 110, 2*pi/225, sol)

        # Marte
        self.marte = planeta(self.canva1, 10, "red", 190, 2*pi/687, sol)

        # Júpiter
        self.jupiter = planeta(self.canva1, 25, "brown", 250, 2*pi/4333, sol)

        # Saturno
        self.saturno = planeta(self.canva1, 22, "khaki", 320, 2*pi/10759, sol)

        # Urano
        self.urano = planeta(self.canva1, 18, "lightblue", 380, 2*pi/30687, sol)

        # Neptuno
        self.neptuno = planeta(self.canva1, 18, "blue", 440, 2*pi/60190, sol)
        
        
        self.animacion()
    
    def animacion(self): 
            self.sol.traslacion()
            
            self.tierra.traslacion()
            self.luna.traslacion()
            self.mercurio.traslacion()
            self.venus.traslacion()
            self.marte.traslacion()
            self.jupiter.traslacion()
            self.saturno.traslacion()
            self.urano.traslacion()
            self.neptuno.traslacion()
            
            self.canva1.after(50, self.animacion)

class planeta(): 
    def __init__(self, ubicacion,tamaño, color, radio, periodo, orbita): 
        
        #Instanciamos los planetas (guardar las propiedades)
        self.ubicacion = ubicacion
        self.tamaño = tamaño 
        self.color = color 
        self.radio = radio 
        self.periodo = periodo 
        self.orbita = orbita
        
        self.figura = None 
        self.angulo = 0
    
    def traslacion(self): 
        self.ubicacion.delete(self.figura)
        
        self.angulo += self.periodo
        if self.orbita == None:
            self.px = self.ubicacion.winfo_width() // 2
            self.py = self.ubicacion.winfo_height() // 2
        else: 
            self.px = self.orbita.px + self.radio * cos(self.angulo)
            self.py = self.orbita.py + self.radio * sin(self.angulo)

            if self.orbita != None and self.orbita.orbita == None:
                    self.ubicacion.create_oval(
                        self.orbita.px - self.radio,
                        self.orbita.py - self.radio,
                        self.orbita.px + self.radio,
                        self.orbita.py + self.radio,
                        outline="white",
                        dash=(2,2)
                    )
            
            
        self.figura = self.ubicacion.create_oval(
            self.px - self.tamaño, self.py - self.tamaño,
            self.px+ self.tamaño, self.py + self.tamaño,
            fill = self.color 
        )
        
app().mainloop()