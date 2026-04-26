#=========================================================DCOUMENTACION INTERNA====================================================================================
# -- Objetivo: Crear una aplicacion grafica que simule el funcionamiento de una cola circular con operaciones de encolar, desencolar y verificar si la cola esta vacia.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: Utilizar una clase en la cual se realizan las 3 funciones de una cola, y una clase principal que maneja la interfaz grafica con Tkinter.
# -- Recursos: Libreria, Widgets Tkinter 
# -- Procesos: Uso de un vector de botones para representar los elementos de la cola, y manejo de excepciones para condiciones de overflow y underflow.
# -- Historia: Fecha de creacion 19/02/2026 Fecha de modificacion: 21/02/2026
# -- Ajustes pendientes: Ninguno 
# ================================================================================================================================================================== 
from tkinter import *; from tkinter import messagebox as mb 
from math import cos, sin
import math 

class Cola: 
    def __init__(self, centro, frame):
        self.queue_circular = [0] * 10 
        self.num_elemen = 0 
        self.inicio = 0
        #===========================COLA CIRCULAR===========================
        paso = (2* math.pi) / 10
        radio = 150
        for i in range(10): 
            angle = paso * i
            px = centro + radio * cos(angle)
            py = centro + radio * sin(angle)
            self.queue_circular[i] = Button(frame, width=5, bg="lightgray")
            self.queue_circular[i].place(x=px, y=py)
        #==========================================================
    def enqueue(self, elemen): 
        if self.num_elemen < 10: 
            final = (self.inicio + self.num_elemen) % 10 
            self.queue_circular[final]['text'] = elemen
            self.num_elemen += 1
        else: 
            raise Exception("Queue Overflow")
        
    def dequeue(self): 
        if self.num_elemen > 0: 
            temp = self.queue_circular[self.inicio].config(text="")
            self.inicio = (self.inicio + 1) % 10 
            self.num_elemen -= 1 
            return temp 
        else: 
            raise Exception("Queue Underflow")
    
    def empty(self): 
        return self.num_elemen == 0
    
class app(Tk): 
    def __init__(self): 
        super().__init__()
        self.title("COLAR CIRCULARES - ELMER JUAREZ C5")
        self.geometry("920x400")
        self.config(bg="lightblue")
        #===========================CREACION DE LA COLA ==============================
        frame_queue = Frame(self, width=400, height=400)
        frame_queue.place(x=0, y=0)
        self.cola = []
        self.cola.append(Cola(170, frame_queue))
        
        #===========================GUI======================================
        frame_gui = Frame(self, width=500, height=200, bg="pink")
        frame_gui.place(x=410, y=10)
        Label(frame_gui, text="Ingrese el numero para la cola:", font=("Arial", 12, "bold"), bg="pink").place(x=10, y=10)
        self.entry_element = Entry(frame_gui, width=10)
        self.entry_element.place(x=250, y=10)
        
        Button(frame_gui, text="ENCOLAR", command=self.enqueue_, width=20, height=4).place(x=10, y=50)
        Button(frame_gui, text="DESENCOLAR", command=self.dequeue_, width=20, height=4).place(x=170, y=50)
        Button(frame_gui, text="EMPTY", command=self.empty_queue, width=20, height=4).place(x=330, y=50)
        
    def enqueue_(self):
        try: 
            element = int(self.entry_element.get())
            self.cola[0].enqueue(element)
        except ValueError:
            mb.showerror("ERROR", "DATOS INVALIDOS")
        except Exception as error: 
            mb.showwarning("ERROR", str(error))
    
    def dequeue_(self): 
        try: 
            self.cola[0].dequeue()
        except Exception as error: 
            mb.showwarning("ERROR", str(error))
    
    def empty_queue(self): 
        if self.cola[0].empty():
            mb.showinfo("Atencion", "La cola esta vacia")
        else: 
            mb.showinfo("Atencion", "La cola esta llena")
app().mainloop()