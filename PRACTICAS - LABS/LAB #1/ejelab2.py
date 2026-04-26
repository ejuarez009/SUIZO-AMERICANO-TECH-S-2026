#Ejercicio para laboratorio de ps
#El fin es construir un programa con todo lo necesario para cumplir con las rutinas
#Iniciamos con el diseño con nuestro objeto base el cual será el treeview

from tkinter import *; from tkinter import ttk,filedialog as f
import pickle
import os.path

def abrir():
    rt = f.askopenfilename()
    rutita['text']=(rt)


def cargar():
    #lista = ['1','100','Juanito Escarcha','Ingenieria']
    rt = rutita['text']
    pos = 0
    with open(rt,'rb') as archi:
        max = os.path.getsize(rt)
        while pos<max:
                lista = pickle.load(archi)
                tr.insert("",'end',text=lista[0],values=[(lista[1]),(lista[2]),(lista[3])])
                pos = archi.tell()

def nuevo():
    vgrabar = Tk()
    vgrabar.geometry("200x200")
    #Entradas
    corre = Entry(vgrabar,width=20)
    corre.pack()
    e1 = Label(vgrabar,text="Correlativo").pack()
    cod = Entry(vgrabar,width=20)
    cod.pack()
    e2 = Label(vgrabar,text="codigo").pack()
    nom = Entry(vgrabar,width=20)
    nom.pack()
    e3 = Label(vgrabar,text="Nombre").pack()
    car = Entry(vgrabar,width=20)
    car.pack()
    e4 = Label(vgrabar,text="Carrera").pack()
   

    #Guarda
    def grb():

        if rutita['text']=="":
            rt = f.asksaveasfilename()
            rutita['text']=(rt)
            lista = [corre.get(),cod.get(),nom.get(),car.get()]
            with open(rt,'ab') as arch:
                pickle.dump(lista,arch)
        else:
            rt=rutita['text']
            lista = [corre.get(),cod.get(),nom.get(),car.get()]
            with open(rt,'ab') as arch:
                pickle.dump(lista,arch)


    #Boton
    
    bg = Button(vgrabar,text="Guardar",command=grb).pack()
    




v=Tk()
#Generamos nuestro objeto base

tr = ttk.Treeview(v,height=10)
tr['columns']=("c1","c2","c3")
tr.heading("#0",text="Correlativo")
tr.heading("c1",text="Codigo")
tr.heading("c2",text="Nombre")
tr.heading("c3",text="Carrera")
tr.pack()
rutita = Label(v,text="")
rutita.pack()

#Boton
Button(v,text="Abrir existente",command=abrir, bg='yellow').pack(side='left')
Button(v,text="Cargar datos",command=cargar, bg='green').pack(side='left')
Button(v,text="Nuevo Registro",command=nuevo, bg='pink').pack(side='left')

v.mainloop()


