#=========================================================DCOUMENTACION INTERNA====================================================================================
# -- Objetivo: Crear una aplicacion grafica que simule el funcionamiento de una cola (FIFO) con operaciones de encolar, desencolar y verificar si la cola esta vacia.
# -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
# -- Descipcion: Utilizar una clase en la cual se realizan las 3 funciones de una cola, y una clase principal que maneja la interfaz grafica con Tkinter.
# -- Recursos: Libreria, Widgets Tkinter 
# -- Procesos: Uso de un vector de botones para representar los elementos de la cola, y manejo de excepciones para condiciones de overflow y underflow.
# -- Historia: Fecha de creacion 01/02/2026 Fecha de modificacion: 04/02/2026
# -- Ajustes pendientes: Ninguno 
# ================================================================================================================================================================== 
from tkinter import Label, Tk, Button, Spinbox, messagebox as mb, Entry

class cola:
    def __init__(self, py, title):
        self.data_queue = [None] * 10
        self.queue_pointer = 0
        self.titulo = Label(text=title)
        self.titulo.place(x=50, y=py)
        for i in range(10):
            self.data_queue[i] = Button(width=3)
            self.data_queue[i].place(x=i * 30 + 150, y=py)

    def enqueue(self, element): 
        if self.queue_pointer < 10:
            self.data_queue[self.queue_pointer]['text'] = element
            self.data_queue[self.queue_pointer].config(bg="light green")
            self.queue_pointer += 1
        else:
            raise Exception("Overflow Queue")

    def dequeue(self):
        if self.queue_pointer > 0:
            temp = self.data_queue[0]['text']
            for i in range(1,self.queue_pointer): 
                self.data_queue[i-1].config(bg="light pink")
                self.data_queue[i-1]['text'] = self.data_queue[i]['text']
                
            self.data_queue[self.queue_pointer-1].config(bg="SystemButtonFace")
            self.data_queue[self.queue_pointer-1]['text'] = ""  
            self.queue_pointer -= 1
            return temp
        else: 
            raise Exception("Underflow Queue")
    def empty(self): 
        return self.queue_pointer == 0


class app(Tk):
    def __init__(self):
        super().__init__()
        self.title("COLAS - Elmer Juarez C5A")
        self.geometry("800x550")
            
        self.spinbox_widget = Spinbox(self, from_=1, to=10, width=8)
        self.spinbox_widget.place(x=680, y=50)
        Label(self, text="Selecciona el No. de cola:", font=("Arial", 12)).place(x=470, y=50)
        Label(self, text="Ingresa un numero a encolar:", font=("Arial", 12)).place(x=470, y=20)
        self.entry_num = Entry(width=10)
        self.entry_num.place(x=680, y=20)
        self.btn_enqueue = Button(self, text="Enqueue", command=self.btn_enqueue, width=40, height=5, bg="light blue")
        self.btn_enqueue.place(x=470, y=80)
        self.btn_dequeue = Button(self, text="Dequeue", command=self.btn_dequeue, width=40, height=5, bg="light green")
        self.btn_dequeue.place(x=470, y=180)
        self.btn_empty = Button(self, text="Empty", command=self.btn_empty, width=40, height=5, bg="pink")
        self.btn_empty.place(x=470, y=280)
        self.vector = [None] * 10
        for i in range(10):
            self.vector[i] = cola(i * 50 + 20, f"Cola No: {i + 1}")

    def btn_enqueue(self):
        try: 
            element_entered = self.entry_num.get()
            num_queue = int(self.spinbox_widget.get()) - 1
            try:
                self.vector[num_queue].enqueue(element_entered)
            except Exception as error:
                mb.showerror("Error", str(error))
        except ValueError: 
            mb.showerror("ERROR", "Ingrese un numero valido")
    
    def btn_dequeue(self): 
        try: 
            num_queue = int(self.spinbox_widget.get()) - 1
            element_deque = self.vector[num_queue].dequeue()
            mb.showinfo("ATENCION", f"Se saco el numero {element_deque}, de la cola {num_queue + 1}")
        except Exception as error: 
                mb.showwarning("ERROR", str(error))
    
    def btn_empty(self): 
        num_queue = int(self.spinbox_widget.get()) -1
        if self.vector[num_queue].empty() != 0:  
            mb.showinfo("ATENCION", "La cola no tiene elementos")
        else: 
            mb.showinfo("ATENCION", "La cola tiene elementos")

if __name__ == "__main__":
    app().mainloop()




