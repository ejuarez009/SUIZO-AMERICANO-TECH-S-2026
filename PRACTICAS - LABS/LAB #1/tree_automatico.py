from tkinter import *
from tkinter import ttk,filedialog as f
from tkinter import messagebox as mes
import pickle

def modi():
   if tr.selection():
        vt = Toplevel()
        vt.geometry("200x200")
        #Datos para modificar
        tcod = Entry(vt,width=20)
        tcod.pack()
        Label(vt,text="codigo")
        tnom = Entry(vt,width=20)
        tnom.pack()
        Label(vt,text="Nombre")
        tedad = Entry(vt,width=20)
        tedad.pack()
        Label(vt,text="Edad")
        tdir = Entry(vt,width=20)
        tdir.pack()
        Label(vt,text="Direccion")
        id = tr.focus()  # ID interno del ítem seleccionado
        lista = tr.item(tr.focus())['values']
        tcod.insert(END,lista[0])
        tnom.insert(END,lista[1])
        tedad.insert(END,lista[2])
        tdir.insert(END,lista[3])

        def actualizar():
              tc = tcod.get()
              tn = tnom.get()
              te = tedad.get()
              td = tdir.get()
              tr.item(id,values=(tc,tn,te,td))
    
        Button(vt,text="Actualizar",command=actualizar).pack()   
        
        vt.mainloop()
   else:
        print("No hay seleccion") 




#funciones de manipulación
def consultar():
    ruta = f.askopenfilename()
    with open(ruta,"rb") as archi:
      while True:
        try:
           datos = pickle.load(archi)
           tr.insert("",END,values=datos)
        except EOFError:
           break  

def indi():
    ruta = f.askopenfilename()
    dat = 200
    with open(ruta,"rb") as archi:
      tr.delete(*tr.get_children())
      while True:
        try:
           
           datos = pickle.load(archi)
           if datos[0] == dat:
              tr.insert("",END,values=datos)
        except EOFError:
           break  


def grabar():
     datos1 = [100,"juanito","34","34-23 zona 5"]
     datos2 = [200,"Pedrito","45","45-67 zona 10"]
     ruta = f.asksaveasfilename()
     with open(ruta,"ab") as archi:
          pickle.dump(datos1,archi)
          pickle.dump(datos2,archi) 


#Crear ventana
v = Tk()
v.geometry("400x400")
columnas = ["Codigo","Nombre","Edad","Direccion"]
#Creando el objeto
tr = ttk.Treeview(v,height=10, columns=columnas,show="headings")
for col in columnas:
    tr.heading(col,text=col)
    tr.column(col,width=50,anchor=CENTER)
tr.pack(expand=True, fill=BOTH)

# Scroll horizontal
#scroll_x = ttk.Scrollbar(v, orient="horizontal", command=tr.xview)
#tr.configure(xscrollcommand=scroll_x.set)

#Botones
Button(v,text="Grabar",command=grabar).pack(side='left')
Button(v,text="Cargar",command=consultar).pack(side='left')
Button(v,text="Individual",command=indi).pack(side='left')
Button(v,text="Modifica",command=modi).pack(side='left')


v.mainloop()