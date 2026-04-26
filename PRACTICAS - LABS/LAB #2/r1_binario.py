from tkinter import *
from tkinter import filedialog as f
from tkinter import ttk
import os.path
import pickle

def co(r):
    #Funcion correlativo
    rt = r
    with open(r,'rb') as archi:   
          while True:
            try:  
              lista = pickle.load(archi)
            except EOFError:
                break
    return lista[0]


class app(Tk):
    def __init__(self):
        super().__init__()
        self.ruta = Label(self,text="")
        self.ruta.pack()
        #Definir el treeview
        columnas=['Correlativo','Nombre','Edad']
        self.tr = ttk.Treeview(self,height=10,columns=columnas,show="headings")
        for col in columnas:
            self.tr.heading(col,text=col)
            self.tr.column(col,width=10,anchor=CENTER)
        self.tr.pack(expand=TRUE, fill=BOTH)
        #Button(self,text="ejecutar",command = co).pack()
        Button(self,text="Grabar",command=self.grabar).pack()

    def grabar(self):
        r = f.asksaveasfilename()
        self.ruta['text']=r
        vg = Toplevel()
        cor = Entry(vg,width=20)
        cor.pack()
        Label(vg,text="Correlativo").pack()
        nom = Entry(vg,width=20)
        nom.pack()
        Label(vg,text="Nombre").pack()
        edad = Entry(vg,width=20)
        edad.pack()
        Label(vg,text="Edad").pack()
        cor.insert('insert',int(co(r))+1)
        cor.config(state='readonly')

        def grabart():
            rt = self.ruta['text']


            corre = cor.get()
            lista = [corre,nom.get(),edad.get()]
            with open (rt,'ab') as archi:
              pickle.dump(lista,archi)

        Button(vg,text="Guardar datos",command=grabart).pack()

        vg.mainloop()





app().mainloop()

